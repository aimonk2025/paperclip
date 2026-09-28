// Enrich all non-done AGE issues with full context from the repo's ticket files + SEQUENCE.md.
import { readFile, writeFile } from "node:fs/promises";
const API = "http://127.0.0.1:3100/api", CID = process.env.COMPANY_ID;
const APP = "/Users/chetan/Documents/verify-ads-app";
const AD = APP + "/agentic-ads";
const ids = JSON.parse(await readFile("/Users/chetan/Documents/paperclip/.setup-ids.json", "utf8"));
const call = async (m, p, b) => {
  const r = await fetch(API + p, { method: m, headers: { "Content-Type": "application/json" }, body: b ? JSON.stringify(b) : undefined });
  const t = await r.text(); let j = null; try { j = JSON.parse(t); } catch {}
  return r.ok ? { ok: true, data: j } : { ok: false, error: (j?.error || t).slice(0, 120) };
};
const AGE = {}; for (const [k, v] of Object.entries(ids.issues)) AGE[v] = k;
const ident = k => ids.issues[k] ? "AGE-" + (Number(Object.keys(ids.issues).indexOf(k)) && "") : "";
// identifier lookup via API later; deps by key name for readability
const tryRead = async p => { try { return await readFile(p, "utf8"); } catch { return null; } };
const trim = (s, n) => (s.length > n ? s.slice(0, n) + "\n…(truncated — read the full file)" : s);

// key: {file, spec[], why, deps[], unblocks[], doneMeans, statusNow}
const MAP = {
  mw1: { file: ".scratch/middleware-build/01-rate-governor.md", spec: [AD + "/docs/03-specs/36-middleware-build-spec.md"], why: "Every outbound platform API call must pass one governor so multi-tenant traffic is safe and the agent layer can be governed later.", deps: [], unblocks: ["mw2", "fagent"], doneMeans: "Rate governor merged, enforced on all platform adapters, tests green.", statusNow: "done" },
  mw3: { file: ".scratch/middleware-build/03-audit-log.md", spec: [AD + "/docs/03-specs/36-middleware-build-spec.md"], why: "Append-only audit trail of every mutation — the precondition for mutations over HTTP and agent-layer mutations.", deps: [], unblocks: ["mw2", "fmut", "fagent"], doneMeans: "Consolidated on audit.mutation_log with append-only trigger enforced (per SEQUENCE.md).", statusNow: "done" },
  mw2: { file: ".scratch/middleware-build/02-pgboss-sync-jobs.md", spec: [AD + "/docs/03-specs/36-middleware-build-spec.md"], why: "Recurring data freshness: pg-boss jobs that drive warehouse ETL inputs and tiered sync frequency.", deps: ["mw1", "mw3"], unblocks: ["fwf"], doneMeans: "Sync jobs scheduled via pg-boss, wired to rate governor, observable failures." },
  pa1: { file: ".scratch/platform-admin/01-admin-identity.md", spec: [], why: "Separate platform_owner/ops/support_readonly identity system — distinct from spec 37's agent control surface (see SEQUENCE.md note).", deps: [], unblocks: ["pa2", "pa3"] },
  pa2: { file: ".scratch/platform-admin/02-tenant-catalog.md", spec: [], why: "Tenant lifecycle (suspend/reactivate/terminate) as platform-admin operations.", deps: ["pa1"], unblocks: ["pa3"] },
  pa3: { file: ".scratch/platform-admin/03-admin-app.md", spec: [], why: "The admin app shell that hosts identity + tenant catalog.", deps: ["pa1", "pa2"], unblocks: [] },
  ap1: { file: ".scratch/agency-panel/01-clients-crud.md", spec: [], why: "Agency panel: manage client entities.", deps: [], unblocks: ["ap2", "ap3"] },
  ap2: { file: ".scratch/agency-panel/02-audit-log.md", spec: [AD + "/docs/03-specs/36-middleware-build-spec.md"], why: "REWRITTEN per decision: this is a read-only audit log VIEWER consuming MW-03's audit.mutation_log table. MW-03 is built → this is now unblocked.", deps: ["mw3"], unblocks: [] },
  ap3: { file: ".scratch/agency-panel/03-feature-flags.md", spec: [], why: "Per-tenant feature flag rollout control. SEQUENCE.md marks this BUILT.", deps: [], statusNow: "done" },
  f37: { file: null, spec: [AD + "/docs/03-specs/37-agent-control-surface-spec.md"], why: "Agent control surface (spec 37): design-only with 5 open decisions — needs its grill pass (Phase 0) BEFORE the agent layer. Registry sequences before agents.", deps: ["fmem"], unblocks: ["fagent"], doneMeans: "5 open decisions closed via grill pass; registry + control surface spec finalized." },
  fmem: { file: null, spec: [AD + "/docs/03-specs/07-memory-and-context-spec.md", AD + "/docs/03-specs/31-memory-and-context-management.md"], why: "Memory/Ken (spec 07): context bundles + directives the agent layer consumes. NOT STARTED — first agent-substrate item.", deps: [], unblocks: ["f37", "fagent"] },
  fwf: { file: null, spec: [], why: "Warehouse facts/dims (SEQUENCE: NOT STARTED) — real aggregates for Analyst/Recommender + tiered sync frequency.", deps: ["mw2"], unblocks: ["fwh"] },
  fwh: { file: null, spec: [], why: "Weekly/monthly rollup reports on top of warehouse facts.", deps: ["fwf"], unblocks: [] },
  fagent: { file: null, spec: [AD + "/docs/03-specs/29-multi-agent-architecture.md", AD + "/docs/03-specs/30-model-strategy-and-hermes.md"], why: "Agent layer (spec 29, 8 roles). Blocked by: memory/Ken (fmem), control-surface registry (f37), and a queue RE-DECISION — spec 29 still says BullMQ/Redis; re-evaluate vs pg-boss, don't copy blindly. Audit-log dependency CLEARED.", deps: ["fmem", "f37", "mw3"], unblocks: ["fmut", "fauth"], doneMeans: "8 agent roles running under control-surface governance with versioned prompts." },
  fmut: { file: null, spec: [], why: "Mutations over HTTP — deliberately deferred until the approval UI exists and audit log (MW-03, now BUILT) is in place. Next blocker is the approval UI (no track yet).", deps: ["mw3", "fagent"], unblocks: [] },
  fauth: { file: null, spec: [], why: "Production auth (JWT/session). DEFERRED BY STANDING DIRECTIVE — not a gap, do not pull forward.", deps: [], unblocks: [] },
  fscr: { file: null, spec: [AD + "/screens/BACKLOG.md", AD + "/screens/HOW-TO-SPEC-A-SCREEN.md"], why: "Screens epic: 12/36 done, 24 not-started (11 dedicated screens + 13 ch-* screens sharing ONE generic channel-table renderer — spec the renderer first, per BACKLOG.md). Per-screen: spec.md → tickets → build → verify. This epic will be broken into one child ticket per screen (Paperclip supports sub-issues).", deps: [], unblocks: [], doneMeans: "All 36 screens done per screens/BACKLOG.md (pnpm verify + ng build clean + browser-checked)." },
};

const results = [];
for (const [key, meta] of Object.entries(MAP)) {
  const id = ids.issues[key]; if (!id) { results.push(`${key}: NO ID`); continue; }
  const src = meta.file ? await tryRead(APP + "/" + meta.file) : null;
  const de = meta.deps.filter(d => ids.issues[d]).map(d => `${d} (${AGE[ids.issues[d]] ? "" : ""}see board)`);
  const desc = [
    `## Why`,
    meta.why || "",
    meta.deps.length ? `\n## Depends on\n${meta.deps.map(d => "- " + (ids.issues[d] ? "board issue " + d : d)).join("\n")}` : "",
    meta.unblocks?.length ? `\n## Unblocks\n${meta.unblocks.map(d => "- " + d).join("\n")}` : "",
    src ? `\n## Ticket source (${APP}/${meta.file})\n\`\`\`markdown\n${trim(src, 2600)}\n\`\`\`` : "\n## Source\nComposed from SEQUENCE.md (no .scratch ticket file for this one).",
    meta.spec.length ? `\n## Read first\n${meta.spec.map(s => "- " + s).join("\n")}\n- ${APP}/SEQUENCE.md — track graph + status\n- ${APP}/CLAUDE.md — rules router` : `\n## Read first\n- ${APP}/SEQUENCE.md\n- ${APP}/CLAUDE.md`,
    `\n## Done means\n${meta.doneMeans || "Per the ticket source above + repo verify commands."}`,
  ].filter(Boolean).join("\n");
  const r = await call("PATCH", `/issues/${id}`, { description: desc });
  let s = "";
  if (meta.statusNow) { const rs = await call("PATCH", `/issues/${id}`, { status: meta.statusNow }); s = rs.ok ? ` [status→${meta.statusNow}]` : ` [status FAIL ${rs.error}]`; }
  results.push(`${key}: ${r.ok ? "enriched" : "FAIL " + r.error}${s}`);
}
console.log(results.join("\n"));
await writeFile("/Users/chetan/Documents/paperclip/.setup-ids.json", JSON.stringify(ids, null, 2));
