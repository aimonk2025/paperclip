// Paperclip bootstrap for Agentic Ads — idempotent-ish: run once.
const API = "http://127.0.0.1:3100/api";
const CID = process.env.COMPANY_ID;
const REPO = "/Users/chetan/Documents/verify-ads-app";
const DOCS = REPO + "/agentic-ads";
if (!CID) { console.error("set COMPANY_ID"); process.exit(1); }

const OC_MODEL = "zai-coding-plan/glm-5.2";
const results = { agents: [], skills: null, project: null, goal: null, issues: [], warnings: [] };
const idByName = {};

async function call(method, path, body) {
  const res = await fetch(API + path, {
    method,
    headers: { "Content-Type": "application/json" },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let json = null; try { json = JSON.parse(text); } catch {}
  if (!res.ok) return { ok: false, status: res.status, error: (json?.error || text || "").toString().slice(0, 220) };
  return { ok: true, data: json };
}

const BASE_RULES = `# Operating rules — read first, follow absolutely

Read these repo files before starting ANY task:
1. ${DOCS}/docs/agents/instructions.md — style, tests, reporting, machine rules
2. ${DOCS}/docs/agents/domain.md — reading order; NEVER bulk-read docs/ (334k tokens)
3. ${REPO}/SEQUENCE.md — the dependency graph; what's done/next and why

Hard rules (from the repo, non-negotiable):
- NEVER commit. The diff is for a human to read.
- NEVER install system packages. No brew, no apt, no global npm. If missing, stop and say so.
- NEVER use Docker. Postgres runs natively.
- Match surrounding code. Comments explain why, never what.
- A false green is the worst outcome. If it did not work, show the output.
`;

const HEARTBEAT = `# Heartbeat checklist
1. Check env: PAPERCLIP_TASK_ID, PAPERCLIP_WAKE_REASON
2. GET my assigned issues (todo/in_progress)
3. If none: exit cleanly with a one-line status comment. Do NOT invent work.
4. Work ONE issue: read its links, run the /implement flow (tdd at test seams)
5. Post the diff/work product to the issue. Move to in_review. NEVER commit.
`;

const AGENTS = [
  { name: "CEO", skip: true },
  { name: "API Contracts Eng", role: "worker", adapter: "opencode_local", model: OC_MODEL,
    title: "API/Contracts Engineer",
    skills: ["implement", "tdd", "codebase-design", "domain-modeling"],
    rules: `# Role: API/Contracts Engineer\nYou own the ServiceClient factory (18-backend-prd.md §ServiceClient), BFF contract schemas, and E13 capability tokens.\n- Contracts are the product: a consumer change never breaks a provider.\n- First work: ServiceClient factory (~2 days, makes 42↔14 topology reversible).` },
  { name: "Backend Eng", role: "worker", adapter: "opencode_local", model: OC_MODEL,
    title: "Backend Engineer",
    skills: ["implement", "tdd", "codebase-design", "diagnosing-bugs"],
    rules: `# Role: Backend Engineer\nYou own middleware (rate governor, audit log, pg-boss sync jobs) and platform adapters.\n- D2: the agent may only move bids/budgets within human-set floors/ceilings. It never pauses.\n- Build order: MW-01 rate governor → MW-03 audit log → MW-02 pg-boss (after 01).\n- Spec: ${DOCS}/docs/03-specs/36-middleware-build-spec.md` },
  { name: "Database Eng", role: "worker", adapter: "opencode_local", model: OC_MODEL,
    title: "Database Engineer",
    skills: ["implement", "tdd", "codebase-design", "domain-modeling"],
    rules: `# Role: Database Engineer\nYou own warehouse facts/dims, migrations, RLS, TS→SQL codegen.\n- D21: no currency conversion, ever. Never sum across currencies.\n- D39: all mathematics is Python; TypeScript generates SQL; Postgres aggregates. The LLM never computes a number.\n- Spec: ${DOCS}/docs/04-prd/20-database-prd.md` },
  { name: "Frontend Eng", role: "worker", adapter: "opencode_local", model: OC_MODEL,
    title: "Frontend Engineer (Angular)",
    skills: ["implement", "tdd", "prototype"],
    rules: `# Role: Frontend Engineer\n- ${DOCS}/screens/BACKLOG.md is the single source of truth for screen work.\n- Check claude-design/screens-extracted/MANIFEST.md + shared components BEFORE speccing a screen.\n- Build state: done = pnpm verify + ng build clean, browser-checked.` },
  { name: "Reviewer", role: "worker", adapter: "claude_local", model: "claude-sonnet-5",
    title: "Code Reviewer (high effort)",
    skills: ["code-review"],
    rules: `# Role: Reviewer — the human merge gate\nRun /code-review on every diff: Standards axis (repo CLAUDE.md + Fowler smells) and Spec axis (does it implement the ticket?).\n- Verdict + specific findings on the issue. You review; the human merges.` },
  { name: "Researcher", role: "worker", adapter: "hermes_local", model: "zai/glm-5.3",
    title: "Researcher (Hermes/GLM-5.3)",
    skills: ["research", "domain-modeling"],
    rules: `# Role: Researcher\n- Use /research against primary sources; findings land in ${DOCS}/docs/research/ with citations.\n- Help the DB/Domain engs keep registry.json and terminology sharp (domain-modeling).` },
];

// ---------- 1. import mattpocock skills ----------
console.log("\n== 1. skills import ==");
results.skills = await call("POST", `/companies/${CID}/skills/import`, { source: "mattpocock/skills" });
console.log(results.skills.ok
  ? `imported: ${results.skills.data.imported?.length ?? "?"} warnings: ${JSON.stringify(results.skills.data.warnings ?? []).slice(0, 200)}`
  : `FAILED: ${results.skills.error}`);

// ---------- 2. agents ----------
console.log("\n== 2. agents ==");
const existing = await call("GET", `/companies/${CID}/agents`);
const ceoId = existing.ok ? existing.data.find(a => a.role === "ceo")?.id : null;
idByName["CEO"] = ceoId;
const budgets = { "CEO": 5000, "API Contracts Eng": 4000, "Backend Eng": 4000, "Database Eng": 4000, "Frontend Eng": 4000, "Reviewer": 3000, "Researcher": 2000 };

for (const spec of AGENTS) {
  if (spec.skip) { console.log(`CEO exists: ${ceoId}`); continue; }
  let r = await call("POST", `/companies/${CID}/agents`, {
    name: spec.name, role: spec.role, title: spec.title,
    adapterType: spec.adapter,
    adapterConfig: { model: spec.model, cwd: REPO },
    reportsToAgentId: ceoId,
    heartbeatEnabled: false,
    desiredSkills: spec.skills,
  });
  if (!r.ok) { // retry without desiredSkills (attach later after import settles)
    r = await call("POST", `/companies/${CID}/agents`, {
      name: spec.name, role: spec.role, title: spec.title,
      adapterType: spec.adapter, adapterConfig: { model: spec.model, cwd: REPO },
      reportsToAgentId: ceoId, heartbeatEnabled: false,
    });
  }
  if (r.ok) {
    const id = r.data.id; idByName[spec.name] = id;
    results.agents.push({ name: spec.name, id, adapter: spec.adapter });
    const bud = await call("PATCH", `/agents/${id}`, { budgetMonthlyCents: budgets[spec.name] });
    if (!bud.ok) results.warnings.push(`budget ${spec.name}: ${bud.error}`);
    console.log(`+ ${spec.name} (${spec.adapter}/${spec.model}) ${budgets[spec.name] ? "$" + budgets[spec.name] / 100 + "/mo" : ""}${bud.ok ? "" : " [budget failed]"}`);
  } else { results.warnings.push(`agent ${spec.name}: ${r.error}`); console.log(`! ${spec.name} FAILED: ${r.error}`); }
}

// attach skills post-create (works even when create-time attach failed)
for (const spec of AGENTS) {
  const id = idByName[spec.name]; if (!id || !spec.skills) continue;
  const s = await call("POST", `/agents/${id}/skills/sync`, { desiredSkills: spec.skills });
  if (!s.ok) results.warnings.push(`skillsync ${spec.name}: ${s.error}`);
}

// ---------- 3. instructions bundles ----------
console.log("\n== 3. instructions ==");
import { writeFile, mkdir } from "node:fs/promises";
for (const spec of AGENTS) {
  const id = idByName[spec.name]; if (!id) continue;
  const dir = `/Users/chetan/.paperclip/instances/default/companies/${CID}/agents/${id}`;
  try {
    await mkdir(dir, { recursive: true });
    await writeFile(`${dir}/AGENTS.md`, BASE_RULES + "\n" + (spec.rules ?? `# Role: ${spec.name}\nOrchestrator. Delegate per SEQUENCE.md ordering; strategy must respect decisions D1–D46 (append-only, not re-litigable). Import order: middleware first.`) + "\n");
    await writeFile(`${dir}/HEARTBEAT.md`, spec.name === "CEO"
      ? `# CEO heartbeat\n1. Check env + pending approvals for me\n2. Review issues board vs SEQUENCE.md ordering\n3. Comment status on in-flight issues; reassign stale ones\n4. Propose (never self-execute) new work — approvals go to the board\n5. Exit cleanly\n`
      : HEARTBEAT);
  } catch (e) { results.warnings.push(`instructions ${spec.name}: ${e.message.slice(0, 120)}`); }
}
console.log("instructions written for: " + Object.keys(idByName).filter(k => idByName[k]).join(", "));

// ---------- 4. project + goal ----------
console.log("\n== 4. project/goal ==");
results.project = await call("POST", `/companies/${CID}/projects`, { name: "agentic-ads", description: "Multi-tenant agentic advertising SaaS", workspacePath: REPO, repoUrl: "https://github.com/aimonk2025/verify-ads-app" });
if (!results.project.ok) results.project = await call("POST", `/companies/${CID}/projects`, { name: "agentic-ads", path: REPO });
console.log(results.project.ok ? `project: ${results.project.data.id}` : `project FAILED: ${results.project.error}`);
const projId = results.project.ok ? results.project.data.id : null;
results.goal = await call("POST", `/companies/${CID}/goals`, { title: "Ship the V1 spine", description: "Ship the Agentic Ads V1 spine in 10 weeks: ServiceClient factory → middleware (rate governor, audit log, sync jobs) → agent layer, following the dependency graph in SEQUENCE.md. Docs/ is the source of truth; decisions D1–D46 are final and not re-litigable." });
console.log(results.goal.ok ? `goal: ${results.goal.data.id}` : `goal FAILED: ${results.goal.error}`);
const goalId = results.goal.ok ? results.goal.data.id : null;

// ---------- 5. issues ----------
console.log("\n== 5. issues ==");
const I = (key, title, desc, status, extra = {}) => ({ key, title, desc, status, ...extra });
const ISSUES = [
  // DONE record — rbac (5)
  I("rbac1", "RBAC: permission matrix", "roles/permissions matrix design + impl", "done"),
  I("rbac2", "RBAC: DB guard", "row-level guard on tenant queries", "done"),
  I("rbac3", "RBAC: team API", "team management endpoints", "done"),
  I("rbac4", "RBAC: frontend Team screen", "Team screen + permission service", "done"),
  I("rbac5", "RBAC: status tracking", "STATUS discipline (now SEQUENCE.md)", "done"),
  // DONE record — bff (4)
  I("bff1", "BFF: migrations + DB setup", "migrations, native Postgres, RLS", "done"),
  I("bff2", "BFF: connections endpoints", "platform connection CRUD", "done"),
  I("bff3", "BFF: reports endpoints", "report engine API", "done"),
  I("bff4", "BFF: sync endpoint", "manual sync trigger", "done"),
  // DONE record — max report coverage (6)
  I("mrc1", "GA4: metadata sync + report families", "dimension/metric catalog + families", "done"),
  I("mrc2", "GSC: remaining dimensions + sitemaps", "country/device/searchAppearance + sitemaps", "done"),
  I("mrc3", "Meta: breakdowns on insights", "breakdown param passthrough", "done"),
  I("mrc4", "Meta: async insights runner", "async run/poll/download + throttling", "done"),
  I("mrc5", "Google Ads: segments + IS/quality families", "segment columns + impression share", "done"),
  I("mrc6", "Google Ads: demographic/geo/placement/audience views", "8 new GAQL view fetchers", "done"),
  I("scr1", "Screens: 12/36 built", "g1 b2 d6 d10 d13 b18 b17 f1 f7 b7 d14 b22", "done"),
  // READY — middleware
  I("mw1", "MW-01: per-tenant rate governor", "migration 003 + server/src/rate-governor.ts + wire into sync.controller.ts. Spec 36. Caps: meta 1/s, google_ads 4/s, ga4 0.25/s, gsc 0.25/s. AdapterError('rate_limit').", "todo", { assign: "Backend Eng", priority: "high" }),
  I("mw3", "MW-03: audit log (append-only)", "migration 004 + server/src/audit.ts recordAudit() only write path + BEFORE UPDATE/DELETE trigger. OWNS migration 004 (agency-panel/02 consumes, does not own).", "todo", { assign: "Backend Eng", priority: "high" }),
  I("mw2", "MW-02: pg-boss sync jobs", "scheduler/worker/retries/DLQ + per-connection cron w/ jitter. Read sync.controller.ts current state first (clientId added since ticket written).", "backlog", { assign: "Backend Eng", blockedBy: ["mw1"] }),
  // platform-admin (backlog, verify status first)
  I("pa1", "Admin identity: admin_users, login, guard", "platform-admin ticket 01", "backlog"),
  I("pa2", "Tenant catalog + lifecycle", "suspend/reactivate/terminate + enforcement", "backlog", { blockedBy: ["pa1"] }),
  I("pa3", "Admin Angular app", "apps/admin login/list/detail/lifecycle", "backlog", { blockedBy: ["pa1", "pa2"] }),
  // agency-panel (backlog; 02 rewritten per collision decision)
  I("ap1", "Clients CRUD + picker", "agency-panel ticket 01", "backlog"),
  I("ap2", "Audit log VIEWER (consumes MW-03 table)", "REWRITTEN: builds screen/read path on audit.mutation_log from MW-03; does NOT own server/src/audit.ts or migration 004.", "backlog", { blockedBy: ["mw3"] }),
  I("ap3", "Feature flags", "table + routes + screen; shares migration numbering coordination with ap2", "backlog"),
  // needs to-tickets / decisions
  I("f37", "Spec 37 grill: agent control surface (5 open decisions)", "USER-INVOKED grill-with-docs session; then to-spec update; registry before agent layer.", "backlog", { priority: "high" }),
  I("fmem", "Memory/Ken → to-tickets", "specs 07+31 exist; run to-tickets", "backlog", { priority: "high" }),
  I("fwf", "Workflow engine → to-tickets", "spec 27 complete (Aug 20); wizard not node-graph; pipeline types from Paperclip extraction", "backlog"),
  I("fwh", "Warehouse facts/dims → to-tickets", "unblocked; specs in DB PRD", "backlog"),
  I("fagent", "Agent layer (spec 29, 8 roles)", "BLOCKED: needs audit log, memory/Ken, control-surface registry, queue re-decision (BullMQ→pg-boss re-eval)", "backlog", { blockedBy: ["mw3", "fmem", "f37"] }),
  I("fmut", "Mutations over HTTP", "deliberately deferred until audit log exists", "backlog", { blockedBy: ["mw3"] }),
  I("fauth", "Production auth (JWT/session)", "deferred by standing directive — not a gap", "backlog"),
  I("fscr", "Screens epic: remaining 24", "BACKLOG.md queue; per-screen spec+tickets flow already documented", "backlog", { assign: "Frontend Eng" }),
];
const issueIds = {};
for (const it of ISSUES) {
  const body = { title: it.title, description: it.desc, status: it.status, priority: it.priority ?? "medium" };
  if (it.assign && idByName[it.assign]) body.assigneeAgentId = idByName[it.assign];
  if (projId) body.projectId = projId;
  if (goalId) body.goalId = goalId;
  const r = await call("POST", `/companies/${CID}/issues`, body);
  if (!r.ok) { results.warnings.push(`issue ${it.key}: ${r.error}`); console.log(`! ${it.key}: ${r.error}`); continue; }
  issueIds[it.key] = r.data.id;
  process.stdout.write(it.status === "done" ? "." : `+${it.key} `);
}
console.log(`\nissues: ${Object.keys(issueIds).length}/${ISSUES.length} created`);

// blocked-by edges
let edges = 0;
for (const it of ISSUES) {
  if (!it.blockedBy || !issueIds[it.key]) continue;
  for (const b of it.blockedBy) {
    if (!issueIds[b]) continue;
    const r = await call("PATCH", `/issues/${issueIds[it.key]}`, { blockedByIssueIds: [issueIds[b]] });
    if (r.ok) edges++; else {
      const r2 = await call("POST", `/issues/${issueIds[it.key]}/blocked-by`, { issueId: issueIds[b] });
      if (r2.ok) edges++; else results.warnings.push(`edge ${b}→${it.key}: ${r2.error}`);
    }
  }
}
console.log(`edges: ${edges}`);

// ---------- 6. verify heartbeats off ----------
console.log("\n== 6. verify ==");
const final = await call("GET", `/companies/${CID}/agents`);
if (final.ok) for (const a of final.data) {
  const hb = a.adapterConfig?.heartbeatIntervalSec ?? a.heartbeatIntervalSec ?? null;
  console.log(`${a.status.padEnd(7)} ${a.name.padEnd(20)} ${a.adapterType} hb=${a.heartbeatEnabled === undefined ? JSON.stringify(hb) : a.heartbeatEnabled}`);
}
console.log("\nWARNINGS:", results.warnings.length ? results.warnings : "none");
import { writeFile as wf } from "node:fs/promises";
await wf("/Users/chetan/Documents/paperclip/.setup-ids.json", JSON.stringify({ companyId: CID, agents: idByName, issues: issueIds }, null, 2));
console.log("saved .setup-ids.json");
