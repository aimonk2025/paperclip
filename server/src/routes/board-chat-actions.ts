/**
 * Board chat action signals.
 *
 * Two channels share one grammar, separated only by their delimiter:
 *
 *   %%ACTIONS%%    receipts   — "I did this". Surfaced to the UI. Never executed.
 *   %%PROPOSALS%%  proposals  — "I want to do this". Parked as a pending
 *                               approval and executed only once a human
 *                               approves (services/board-action-dispatch.ts).
 *
 * `board-chat.ts` strips both envelopes out of the durable comment body.
 *
 * Untrusted-input note: conversation history is replayed into the prompt as
 * `<turn>` bodies, so a user can paste a literal envelope and the model may
 * echo it back. Actions whose fingerprint already appears in the prompt are
 * dropped — echoed user text must not manufacture an action.
 */
import {
  ISSUE_PRIORITIES,
  ISSUE_STATUSES,
  type IssuePriority,
  type IssueStatus,
} from "@paperclipai/shared";

/** Fields a proposal may change on an existing issue. */
export interface IssuePatch {
  status?: IssueStatus;
  priority?: IssuePriority;
  title?: string;
  description?: string;
  assigneeAgentId?: string | null;
}

/** Fields a new issue may be created with. */
export interface IssueDraft {
  title: string;
  description?: string;
  status?: IssueStatus;
  priority?: IssuePriority;
  assigneeAgentId?: string;
  projectId?: string;
  parentIssueId?: string;
}

/**
 * Actions the board skill can announce or propose.
 *
 * `HIRE_AGENT` carries the whole hire payload rather than a summary: the
 * substance of a hire is the adapter config and system prompt, and a proposal
 * that dropped them would approve an agent nobody reviewed.
 */
export type BoardAction =
  | { type: "CREATE_COMPANY"; name: string }
  | { type: "HIRE_AGENT"; name: string; role: string; hire: Record<string, unknown> }
  | ({ type: "CREATE_ISSUE" } & IssueDraft)
  | { type: "UPDATE_ISSUE"; issueId: string; summary: string; patch: IssuePatch }
  | { type: "ADD_COMMENT"; issueId: string; body: string }
  | {
      type: "RESOLVE_APPROVAL";
      approvalId: string;
      decision: "approve" | "reject" | "request-revision";
    };

export type BoardActionType = BoardAction["type"];

/**
 * Cap per turn. A model that loops can emit envelopes without bound; the UI
 * renders one card per action, so surface the overflow as a flag rather than
 * silently dropping or rendering hundreds.
 */
export const MAX_ACTIONS_PER_TURN = 10;

export interface ParseBoardActionsResult {
  actions: BoardAction[];
  truncated: boolean;
}

const ACTIONS_ENVELOPE_RE = /%%ACTIONS%%([\s\S]*?)%%\/ACTIONS%%/g;
const PROPOSALS_ENVELOPE_RE = /%%PROPOSALS%%([\s\S]*?)%%\/PROPOSALS%%/g;

const APPROVAL_DECISIONS = ["approve", "reject", "request-revision"] as const;

/**
 * Action types a proposal may carry.
 *
 * `CREATE_COMPANY` is excluded because an approval is company-scoped — there is
 * no company to hang the request on. `RESOLVE_APPROVAL` is excluded because a
 * proposal that resolves another approval, dispatched on approval, is a
 * privilege-escalation loop: approving one thing would silently approve
 * another. Both remain valid as receipts.
 */
export const PROPOSABLE_ACTION_TYPES = [
  "HIRE_AGENT",
  "CREATE_ISSUE",
  "UPDATE_ISSUE",
  "ADD_COMMENT",
] as const satisfies readonly BoardActionType[];

export type ProposableAction = Extract<
  BoardAction,
  { type: (typeof PROPOSABLE_ACTION_TYPES)[number] }
>;

export function isProposable(action: BoardAction): action is ProposableAction {
  return (PROPOSABLE_ACTION_TYPES as readonly string[]).includes(action.type);
}

/** Extract announced actions (receipts) from a board reply. */
export function parseBoardActions(
  output: string,
  prompt?: string,
): ParseBoardActionsResult {
  return parseEnvelopes(ACTIONS_ENVELOPE_RE, output, prompt);
}

/** Extract proposals, dropping any type that must not be dispatched. */
export function parseBoardProposals(
  output: string,
  prompt?: string,
): { actions: ProposableAction[]; truncated: boolean } {
  const { actions, truncated } = parseEnvelopes(
    PROPOSALS_ENVELOPE_RE,
    output,
    prompt,
  );
  return { actions: actions.filter(isProposable), truncated };
}

function parseEnvelopes(
  envelopeRe: RegExp,
  output: string,
  prompt?: string,
): ParseBoardActionsResult {
  const promptFingerprints = prompt
    ? new Set(collectActions(envelopeRe, prompt).map(fingerprint))
    : new Set<string>();

  const seen = new Set<string>();
  const actions: BoardAction[] = [];
  let truncated = false;

  for (const action of collectActions(envelopeRe, output)) {
    const fp = fingerprint(action);
    if (seen.has(fp)) continue;
    if (promptFingerprints.has(fp)) continue;
    if (actions.length >= MAX_ACTIONS_PER_TURN) {
      truncated = true;
      break;
    }
    seen.add(fp);
    actions.push(action);
  }

  return { actions, truncated };
}

/** Every well-formed action in `text`, in order, before dedup or capping. */
function collectActions(envelopeRe: RegExp, text: string): BoardAction[] {
  const out: BoardAction[] = [];
  // matchAll on a shared /g regex is safe: it clones lastIndex internally.
  for (const match of text.matchAll(envelopeRe)) {
    out.push(...parseEnvelope(match[1]));
  }
  return out;
}

/**
 * An envelope body is JSON: a single action, a bare array, or `{actions: []}`.
 * Malformed JSON yields nothing — a broken envelope must not fail the turn,
 * because the reply text around it is still worth showing the user.
 */
function parseEnvelope(body: string): BoardAction[] {
  const trimmed = body.trim();
  if (!trimmed) return [];

  let parsed: unknown;
  try {
    parsed = JSON.parse(trimmed);
  } catch {
    return [];
  }

  const raw = Array.isArray(parsed)
    ? parsed
    : isRecord(parsed) && Array.isArray(parsed.actions)
      ? parsed.actions
      : [parsed];

  const out: BoardAction[] = [];
  for (const entry of raw) {
    const action = coerceAction(entry);
    if (action) out.push(action);
  }
  return out;
}

export function coerceAction(raw: unknown): BoardAction | null {
  if (!isRecord(raw)) return null;
  const type = pick(raw, ["type"]).toUpperCase();

  switch (type) {
    case "CREATE_COMPANY": {
      const name = pick(raw, ["name", "companyName", "title"]);
      return name ? { type, name } : null;
    }

    case "HIRE_AGENT": {
      // The hire body is the payload the agent-hires endpoint expects. Keep it
      // whole; `name` and `role` are lifted out only for display and dedup.
      const hire = isRecord(raw.hire) ? raw.hire : raw;
      const name = pick(hire, ["name"]);
      const role = pick(hire, ["role"]);
      if (!name || !role) return null;
      return { type, name, role, hire: stripEnvelopeKeys(hire) };
    }

    case "CREATE_ISSUE": {
      const title = pick(raw, ["title", "name"]);
      if (!title) return null;
      const draft: IssueDraft = { title };
      const description = pick(raw, ["description", "body"]);
      if (description) draft.description = description;
      const status = asStatus(pick(raw, ["status"]));
      if (status) draft.status = status;
      const priority = asPriority(pick(raw, ["priority"]));
      if (priority) draft.priority = priority;
      const assigneeAgentId = pick(raw, ["assigneeAgentId", "assignee"]);
      if (assigneeAgentId) draft.assigneeAgentId = assigneeAgentId;
      const projectId = pick(raw, ["projectId"]);
      if (projectId) draft.projectId = projectId;
      const parentIssueId = pick(raw, ["parentIssueId", "parentId"]);
      if (parentIssueId) draft.parentIssueId = parentIssueId;
      return { type, ...draft };
    }

    case "UPDATE_ISSUE": {
      const issueId = pick(raw, ["issueId", "id"]);
      const summary = pick(raw, ["summary", "change"]);
      if (!issueId || !summary) return null;

      const source = isRecord(raw.patch) ? raw.patch : raw;
      const patch: IssuePatch = {};
      const status = asStatus(pick(source, ["status"]));
      if (status) patch.status = status;
      const priority = asPriority(pick(source, ["priority"]));
      if (priority) patch.priority = priority;
      const title = pick(source, ["title"]);
      if (title) patch.title = title;
      const description = pick(source, ["description"]);
      if (description) patch.description = description;
      if ("assigneeAgentId" in source) {
        const assignee = source.assigneeAgentId;
        if (assignee === null) patch.assigneeAgentId = null;
        else if (typeof assignee === "string" && assignee.trim()) {
          patch.assigneeAgentId = assignee.trim();
        }
      }

      // An update that changes nothing is not an update. Without this a
      // proposal could be approved and quietly do nothing at all.
      if (Object.keys(patch).length === 0) return null;
      return { type, issueId, summary, patch };
    }

    case "ADD_COMMENT": {
      const issueId = pick(raw, ["issueId", "id"]);
      const body = pick(raw, ["body", "text", "comment"]);
      return issueId && body ? { type, issueId, body } : null;
    }

    case "RESOLVE_APPROVAL": {
      const approvalId = pick(raw, ["approvalId", "id"]);
      const decision = pick(raw, ["decision", "verdict"]).toLowerCase();
      if (!approvalId || !isApprovalDecision(decision)) return null;
      return { type, approvalId, decision };
    }

    default:
      return null;
  }
}

/**
 * Identity of an action, for dedup and the prompt echo guard.
 *
 * Serializing the whole action rather than listing fields by hand means a field
 * added later is fingerprinted automatically — the failure mode otherwise is a
 * real second action being swallowed as a duplicate. Key order is stable
 * because every action is built by `coerceAction`.
 */
export function fingerprint(action: BoardAction): string {
  return JSON.stringify(action);
}

/** Drop protocol keys so they cannot reach the hire endpoint as fields. */
function stripEnvelopeKeys(hire: Record<string, unknown>): Record<string, unknown> {
  const { type: _type, hire: _hire, ...rest } = hire;
  return rest;
}

function asStatus(value: string): IssueStatus | null {
  return (ISSUE_STATUSES as readonly string[]).includes(value)
    ? (value as IssueStatus)
    : null;
}

function asPriority(value: string): IssuePriority | null {
  return (ISSUE_PRIORITIES as readonly string[]).includes(value)
    ? (value as IssuePriority)
    : null;
}

function isApprovalDecision(
  value: string,
): value is (typeof APPROVAL_DECISIONS)[number] {
  return (APPROVAL_DECISIONS as readonly string[]).includes(value);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function pick(source: Record<string, unknown>, keys: string[]): string {
  for (const key of keys) {
    const value = source[key];
    if (typeof value === "string" && value.trim()) return value.trim();
  }
  return "";
}
