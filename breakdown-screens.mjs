// Break fscr into per-screen child tickets with subtasks. Atomic tasks, parent = container only.
import { readFile, writeFile } from "node:fs/promises";
const API = "http://127.0.0.1:3100/api", CID = process.env.COMPANY_ID;
const APP = "/Users/chetan/Documents/verify-ads-app", AD = APP + "/agentic-ads";
const ids = JSON.parse(await readFile("/Users/chetan/Documents/paperclip/.setup-ids.json", "utf8"));
const FE = ids.agents["Frontend Eng"];
const call = async (m, p, b) => {
  const r = await fetch(API + p, { method: m, headers: { "Content-Type": "application/json" }, body: b ? JSON.stringify(b) : undefined });
  const t = await r.text(); let j = null; try { j = JSON.parse(t); } catch {}
  return r.ok ? { ok: true, data: j } : { ok: false, error: (j?.error || t).slice(0, 140) };
};
async function mkIssue(parent, title, description, status = "backlog", assignee = FE) {
  let r = await call("POST", `/issues/${parent}/children`, { title, description, status, assigneeAgentId: assignee });
  if (!r.ok) r = await call("POST", `/companies/${CID}/issues`, { parentId: parent, title, description, status, assigneeAgentId: assignee });
  return r;
}
async function block(child, parent) {
  let r = await call("POST", `/issues/${child}/blocked-by`, { blockerIssueId: parent });
  if (!r.ok) r = await call("PATCH", `/issues/${child}`, { blockedBy: [parent] });
  return r.ok;
}
const READ = `\n## Read first\n- ${AD}/claude-design/screens-extracted/MANIFEST.md — this screen's design source (render-value keys)\n- ${AD}/screens/BACKLOG.md — claim protocol + shared components built (EvidenceDrawer, vd-switch, channel renderer) + confirmed gaps\n- ${AD}/screens/HOW-TO-SPEC-A-SCREEN.md\n\n## Done means\nWired into app.ts, pnpm verify + ng build clean, browser-checked. Claim per BACKLOG.md protocol. NEVER commit.`;

const DONE = [["g1","Portfolio"],["b2","Client overview"],["d6","Insights"],["d10","Recommendations"],["d13","Applied changes"],["b18","Alert rules"],["b17","Alert inbox"],["f1","Sales"],["f7","Attribution quality"],["b7","Settings — Connections"],["d14","Settings — Autonomy"],["b22","Settings — Team & roles"]];
const OPEN = [["e20","Forecast & budget"],["e21","Seasonality"],["d21","Digest"],["g3","Campaigns"],["g4","Campaign detail"],["c2","Report builder"],["d15","Settings — Guardrails"],["d16","Settings — Memory"],["a14","Settings — Onboarding"],["b23","Settings — Branding"],["h3","Settings — Superadmin"]];
const CH = [["ch-adgroups","Google Ads — Ad groups"],["ch-ads","Google Ads — Ads"],["ch-keywords","Google Ads — Keywords"],["ch-terms","Google Ads — Search terms"],["ch-m-campaigns","Meta Ads — Campaigns"],["ch-adsets","Meta Ads — Ad sets"],["ch-m-ads","Meta Ads — Ads"],["ch-placements","Meta Ads — Placements"],["ch-audiences","Meta Ads — Audiences"],["ch-landing","GA4 — Landing pages"],["ch-sources","GA4 — Traffic sources"],["ch-queries","GSC — Queries"],["ch-pages","GSC — Pages"]];
const EPIC = ids.issues.fscr;
let n = 0, errs = [];

for (const [c, label] of DONE) { const r = await mkIssue(EPIC, `Screen ${c}: ${label}`, `Record: built, verified, browser-checked (per screens/BACKLOG.md).`, "done", null); r.ok ? n++ : errs.push(`${c}:${r.error}`); }

for (const [c, label] of OPEN) {
  const p = await mkIssue(EPIC, `Screen ${c}: ${label}`, `Build the **${label}** screen (${c}).\n\n## Sub-tasks below\n1. Spec — write screens/${c}-*/spec.md per HOW-TO-SPEC-A-SCREEN.md, check MANIFEST render keys + shared components first\n2. Build & wire — component, route, NAV, data stubs matching BFF contracts\n3. Verify — pnpm verify + ng build + browser check, update BACKLOG.md status\n${READ}`);
  if (!p.ok) { errs.push(`${c}:${p.error}`); continue; } n++;
  ids.issues["scr-" + c] = p.data.id;
  const subs = [["spec", `Spec screen ${c}: write spec.md + tickets per HOW-TO-SPEC-A-SCREEN.md. Check MANIFEST for design source; grep shared components (EvidenceDrawer, vd-switch) before inventing new.`], ["build", `Build screen ${c}: component + route + NAV wiring + data stubs. Follow spec from the spec sub-task. OnPush per .claude/rules/frontend.md.`], ["verify", `Verify screen ${c}: pnpm verify, ng build clean, browser-check against MANIFEST design, update screens/BACKLOG.md row to done.`]];
  let prev = null;
  for (const [s, d] of subs) {
    const r = await mkIssue(p.data.id, `${c} — ${s}`, `${d}\n${READ}`, "backlog");
    if (!r.ok) { errs.push(`${c}/${s}:${r.error}`); continue; } n++;
    ids.issues[`scr-${c}-${s}`] = r.data.id;
    if (prev) await block(r.data.id, prev);
    prev = r.data.id;
  }
}

const rend = await mkIssue(EPIC, "Shared component: channel data-table renderer", `ONE generic renderer covering all 13 ch-* screens, per MANIFEST.md ("13 screens sharing ONE generic renderer"). Build BEFORE any ch-* screen ticket — all 13 are blocked by this.\n\n## Done means\nRenderer accepts per-screen config (columns, filters, data shape); tests cover at least 2 configs; wired examples in storybook/spec.${READ}`);
if (rend.ok) { n++; ids.issues["scr-renderer"] = rend.data.id; } else errs.push(`renderer:${rend.error}`);
for (const [c, label] of CH) {
  const r = await mkIssue(rend.ok ? rend.data.id : EPIC, `Screen ${c}: ${label} (config)`, `Configure the shared channel renderer for **${label}** — per-screen config only, no bespoke component. Blocked by the renderer ticket.${READ}`);
  if (!r.ok) { errs.push(`${c}:${r.error}`); continue; } n++;
  ids.issues["scr-" + c] = r.data.id;
  await block(r.data.id, ids.issues["scr-renderer"]);
}
console.log(`created ${n}, errors: ${errs.length ? errs.join(" | ") : "none"}`);
await writeFile("/Users/chetan/Documents/paperclip/.setup-ids.json", JSON.stringify(ids, null, 2));
