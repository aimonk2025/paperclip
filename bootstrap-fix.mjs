// Fix pass: skills import (per-skill), agents with valid roles, assignments, verify.
const API = "http://127.0.0.1:3100/api";
const CID = process.env.COMPANY_ID;
const REPO = "/Users/chetan/Documents/verify-ads-app";
const LSK = REPO + "/agentic-ads/.agents/skills";
const warn = []; const log = (...a) => console.log(...a);
async function call(m, p, b) {
  const r = await fetch(API + p, { method: m, headers: { "Content-Type": "application/json" }, body: b ? JSON.stringify(b) : undefined });
  const t = await r.text(); let j = null; try { j = JSON.parse(t); } catch {}
  return r.ok ? { ok: true, data: j } : { ok: false, error: (j?.error || t).toString().slice(0, 160) };
}
const { readFile, writeFile, mkdir } = await import("node:fs/promises");
const ids = JSON.parse(await readFile(".setup-ids.json", "utf8"));

// ---------- 1. skills ----------
log("\n== skills ==");
const GH = ["implement", "tdd", "code-review", "codebase-design", "domain-modeling", "research", "prototype", "resolving-merge-conflicts", "writing-for-agents"];
const imported = [];
for (const s of GH) {
  const r = await call("POST", `/companies/${CID}/skills/import`, { source: `mattpocock/skills/${s}` });
  if (r.ok) imported.push(s); else { warn.push(`skill ${s}: ${r.error}`); log(`! ${s}: ${r.error}`); }
}
let dbg = await call("POST", `/companies/${CID}/skills/import`, { source: `${LSK}/diagnosing-bugs` });
if (dbg.ok) imported.push("diagnosing-bugs"); else { warn.push(`diagnosing-bugs: ${dbg.error} (repo-local copy still available to agents via cwd)`); log(`! diagnosing-bugs local: ${dbg.error}`); }
log(`imported ${imported.length}: ${imported.join(", ")}`);

// ---------- 2. agents (valid roles) ----------
log("\n== agents ==");
const OC = "zai-coding-plan/glm-5.2", ceoId = ids.agents.CEO;
const AGENTS = [
  { name: "API Contracts Eng", role: "engineer", adapter: "opencode_local", model: OC, skills: ["implement", "tdd", "codebase-design", "domain-modeling"], budget: 4000,
    rules: "# Role: API/Contracts Engineer\nOwn the ServiceClient factory, BFF contract schemas, E13 capability tokens. Contracts are the product: a consumer change never breaks a provider. First work: ServiceClient factory." },
  { name: "Backend Eng", role: "engineer", adapter: "opencode_local", model: OC, skills: ["implement", "tdd", "codebase-design", "diagnosing-bugs"], budget: 4000,
    rules: "# Role: Backend Engineer\nOwns middleware (rate governor, audit log, pg-boss sync jobs) + platform adapters. D2: bids/budgets only within human floors/ceilings; never pauses. Order: MW-01 → MW-03 → MW-02. Spec: docs/03-specs/36-middleware-build-spec.md" },
  { name: "Database Eng", role: "engineer", adapter: "opencode_local", model: OC, skills: ["implement", "tdd", "codebase-design", "domain-modeling"], budget: 4000,
    rules: "# Role: Database Engineer\nOwns warehouse facts/dims, migrations, RLS, TS→SQL codegen. D21: never sum across currencies. D39: TS generates SQL, Postgres aggregates, the LLM never computes a number." },
  { name: "Frontend Eng", role: "engineer", adapter: "opencode_local", model: OC, skills: ["implement", "tdd", "prototype", "diagnosing-bugs"], budget: 4000,
    rules: "# Role: Frontend Engineer (Angular)\nscreens/BACKLOG.md is truth. Check MANIFEST.md + shared components before speccing. done = pnpm verify + ng build clean, browser-checked." },
  { name: "Reviewer", role: "qa", adapter: "claude_local", model: "claude-sonnet-5", skills: ["code-review"], budget: 3000,
    rules: "# Role: Reviewer — the human merge gate\nRun code-review on every diff: Standards axis (repo CLAUDE.md) + Spec axis (implements the ticket?). Verdict + findings on the issue. You review; the human merges." },
  { name: "Researcher", role: "researcher", adapter: "hermes_local", model: "zai/glm-5.3", skills: ["research", "domain-modeling", "writing-for-agents"], budget: 2000,
    rules: "# Role: Researcher\n/research against primary sources; findings to docs/research/ with citations. Keep registry.json + terminology sharp." },
];
const BASE = `# Operating rules — read first, follow absolutely\nRead before ANY task:\n1. ${REPO}/agentic-ads/docs/agents/instructions.md — style, tests, reporting, machine rules\n2. ${REPO}/agentic-ads/docs/agents/domain.md — reading order; NEVER bulk-read docs/\n3. ${REPO}/SEQUENCE.md — dependency graph, what's done/next\n\nHard rules: NEVER commit (diff is for a human). NEVER install system packages. NEVER use Docker. Match surrounding code; comments explain why. A false green is the worst outcome.\n`;
const HB = `# Heartbeat checklist\n1. Check env: PAPERCLIP_TASK_ID, PAPERCLIP_WAKE_REASON\n2. GET my assigned issues\n3. None → exit cleanly with one-line status. Do NOT invent work.\n4. Work ONE issue via /implement flow (tdd at seams)\n5. Post diff/work product, move to in_review. NEVER commit.\n`;
for (const a of AGENTS) {
  const r = await call("POST", `/companies/${CID}/agents`, { name: a.name, role: a.role, title: a.name, adapterType: a.adapter, adapterConfig: { model: a.model, cwd: REPO }, reportsToAgentId: ceoId, heartbeatEnabled: false, desiredSkills: a.skills });
  if (!r.ok) { warn.push(`agent ${a.name}: ${r.error}`); log(`! ${a.name}: ${r.error}`); continue; }
  ids.agents[a.name] = r.data.id;
  const bud = await call("PATCH", `/agents/${r.data.id}`, { budgetMonthlyCents: a.budget });
  const dir = `/Users/chetan/.paperclip/instances/default/companies/${CID}/agents/${r.data.id}`;
  await mkdir(dir, { recursive: true });
  await writeFile(`${dir}/AGENTS.md`, BASE + "\n" + a.rules + "\n");
  await writeFile(`${dir}/HEARTBEAT.md`, HB);
  log(`+ ${a.name} [${a.role}/${a.adapter}] $${a.budget / 100}/mo${bud.ok ? "" : " [budget FAILED]"}`);
}

// ---------- 3. assign ready issues ----------
log("\n== assignments ==");
const assign = { mw1: "Backend Eng", mw3: "Backend Eng", fscr: "Frontend Eng" };
for (const [k, who] of Object.entries(assign)) {
  if (!ids.issues[k] || !ids.agents[who]) continue;
  const r = await call("PATCH", `/issues/${ids.issues[k]}`, { assigneeAgentId: ids.agents[who] });
  log(`${k} → ${who}: ${r.ok ? "ok" : r.error}`);
}

// ---------- 4. verify ----------
log("\n== verify ==");
const skills = await call("GET", `/companies/${CID}/skills`);
if (skills.ok) log(`company skills: ${skills.data.length} → ${skills.data.map(s => s.slug || s.key?.split("/").pop()).filter(Boolean).join(", ")}`);
const agents = await call("GET", `/companies/${CID}/agents`);
if (agents.ok) for (const a of agents.data) log(`${(a.status || "?").padEnd(6)} ${a.name.padEnd(20)} ${String(a.adapterType).padEnd(14)} hb=${JSON.stringify(a.heartbeatEnabled ?? a.adapterConfig?.heartbeatEnabled ?? "?")}`);
log("\nWARNINGS:", warn.length ? warn : "none");
await writeFile(".setup-ids.json", JSON.stringify(ids, null, 2));
log("ids updated");
