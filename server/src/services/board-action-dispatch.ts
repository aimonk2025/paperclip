/**
 * Dispatch for approved board-chat proposals.
 *
 * The board concierge proposes a control-plane change in chat; the change is
 * parked as a `board_action` approval and only happens here, after a human
 * approves it. Called from `approvalService.approve` behind its `applied`
 * idempotency guard, so a double-approve cannot double-dispatch.
 *
 * Authority: everything runs as the approving user. The proposal carries no
 * privilege of its own — if the payload names a target the approver could not
 * otherwise touch, the underlying service is the thing that must refuse.
 */
import type { Db } from "@paperclipai/db";

import { coerceAction, isProposable } from "../routes/board-chat-actions.js";
import type { ProposableAction } from "../routes/board-chat-actions.js";

export type BoardActionDispatchResult =
  | { status: "dispatched"; detail: string }
  | { status: "failed"; reason: string };

/**
 * Rebuild a typed action from the approval payload.
 *
 * The payload is JSON that has been through the database, so it goes back
 * through the same coercion the parser uses rather than being trusted: a row
 * edited out-of-band must not reach a service call.
 */
export function readProposalPayload(
  payload: Record<string, unknown>,
): ProposableAction | null {
  const action = coerceAction(payload.action);
  return action && isProposable(action) ? action : null;
}

/**
 * Execute one approved board action.
 *
 * Never throws: a failed dispatch must not roll back the approval itself —
 * the human's decision is recorded either way, and the failure is reported so
 * the caller can surface it.
 */
export async function dispatchBoardAction(
  db: Db,
  input: {
    companyId: string;
    payload: Record<string, unknown>;
    decidedByUserId: string;
  },
): Promise<BoardActionDispatchResult> {
  const action = readProposalPayload(input.payload);
  if (!action) {
    return { status: "failed", reason: "unreadable_payload" };
  }

  // Dynamic import: `issues.ts` is a large module and `approvals.ts` — this
  // module's only caller — is reachable from it transitively in some paths.
  // `approvals.ts` already uses this pattern for the same reason.
  const { issueService } = await import("./issues.js");
  const issueSvc = issueService(db);

  /** Refuse any issue the approval's company does not own. */
  async function assertIssueInCompany(issueId: string): Promise<boolean> {
    const existing = await issueSvc.getById(issueId);
    return Boolean(existing && existing.companyId === input.companyId);
  }

  try {
    switch (action.type) {
      case "CREATE_ISSUE": {
        const { type: _type, ...draft } = action;
        const created = await issueSvc.create(input.companyId, {
          ...draft,
          description: draft.description ?? "",
          status: draft.status ?? "todo",
          priority: draft.priority ?? "medium",
          createdByUserId: input.decidedByUserId,
          responsibleUserId: input.decidedByUserId,
          trustExplicitResponsibleUserId: true,
        } as Parameters<typeof issueSvc.create>[1]);
        return { status: "dispatched", detail: `issue:${created.id}` };
      }

      case "UPDATE_ISSUE": {
        if (!(await assertIssueInCompany(action.issueId))) {
          return { status: "failed", reason: "issue_not_in_company" };
        }
        // Apply the proposed patch verbatim. Writing the human-readable
        // `summary` into a field here would silently do the wrong thing —
        // most board updates are a status change, not a prose edit.
        await issueSvc.update(action.issueId, {
          ...action.patch,
          actorUserId: input.decidedByUserId,
        });
        return { status: "dispatched", detail: `issue:${action.issueId}` };
      }

      case "ADD_COMMENT": {
        if (!(await assertIssueInCompany(action.issueId))) {
          return { status: "failed", reason: "issue_not_in_company" };
        }
        await issueSvc.addComment(action.issueId, action.body, {
          userId: input.decidedByUserId,
        });
        return { status: "dispatched", detail: `issue:${action.issueId}` };
      }

      case "HIRE_AGENT": {
        // Hiring has a first-class approval type with its own activation,
        // budget and notification handling, and board-chat routes hire
        // proposals straight to it. Reaching here means a `board_action`
        // carried a hire payload — a routing bug, not something to half-run.
        return { status: "failed", reason: "hire_must_use_hire_agent_approval" };
      }
    }
  } catch (error) {
    return {
      status: "failed",
      reason: error instanceof Error ? error.message : "dispatch_error",
    };
  }
}
