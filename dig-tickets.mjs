import { readFile, writeFile } from "node:fs/promises";
const API="http://127.0.0.1:3100/api",CID=process.env.COMPANY_ID,APP="/Users/chetan/Documents/verify-ads-app";
const ids=JSON.parse(await readFile("/Users/chetan/Documents/paperclip/.setup-ids.json","utf8"));
const BE=ids.agents["Backend Eng"],FE=ids.agents["Frontend Eng"],CE=ids.agents.CEO;
const call=async(m,p,b)=>{const r=await fetch(API+p,{method:m,headers:{"Content-Type":"application/json"},body:b?JSON.stringify(b):undefined});const t=await r.text();let j=null;try{j=JSON.parse(t)}catch{};return r.ok?{ok:true,data:j}:{ok:false,error:(j?.error||t).slice(0,120)}};
const E=t=>`Evidence: ${t}. Source: Claude/Hermes session dig 2026-09-13.`;
const T=[ // [title, desc, status, parentKey|null, assignee|null]
["FIX SWEEP: adapters (GA4/GSC dates+pagination+realtime/cohortSpec; Meta async runner; gAds segments/views)",E("commit b9ff6c6; Hermes bug-hunt fan-out"),"done",null,null],
["FIX SWEEP: RBAC security review — 11 fixes (privilege escalation, last-owner lockout)",E("commit 65ea347; Hermes 11:39/11:45"),"done",null,null],
["FIX SWEEP: Angular core-services (fail-closed, real team wiring)",E("commit f963bcf; Hermes 12:16"),"done",null,null],
["FIX SWEEP: Angular screens honesty (real connections, demo labels)",E("commit 6ca4f77; Hermes 12:32"),"done",null,null],
["FIX SWEEP: reports-flow 8 E2E bugs (error mapping, idempotency lifecycle)",E("commit 3ba2eb9; Hermes 13:02"),"done",null,null],
["FIX SWEEP: server/BFF 7 verified bugs + warnings persistence",E("commit b9ff6c6; Hermes 11:09"),"done",null,null],
["SCOPE: d1 Chat cut from build (NAV, spec, tickets, design removed)",E("commit cf0cc6f"),"done",null,null],
["DOCS: spec 36 + 37 authored (grill→spec→tickets; pg-boss decision)",E("docs/03-specs/36,37; session 4d7fce"),"done",null,null],
["DOCS: SEQUENCE.md master track graph + HANDOFF-NEXT.md (absorbed 3 status files)",E("session 4d7fce"),"done",null,null],
["DOCS: docs wiki hub + folder indexes; PRD 18/19 reality-adjusted; README rewritten",E("commits ed9ce45, 07f2292"),"done",null,null],
["TOOLING: graphify-out rebuilt (249 files, 10 chunks)",E("commit 6149bc6; Hermes Sep 7"),"done",null,null],
["TOOLING: verify:styles + graph query tooling; 32 frontend-rule violations fixed",E("commits 4ac1abd, 11eb9bd"),"done",null,null],
["DESIGN: bundle split → 37 per-screen files + MANIFEST",E("commit e3ad7c2"),"done",null,null],
["CSS: --on-tone token, Proper Caps, ALL-CAPS, redundant titles",E("commits fd392a9, 0913173"),"done",null,null],
["DOCS: lessons corpus L-001..L-017 + INDEX",E("docs/lessons; Hermes"),"done",null,null],
["TOOLING: one-command dev (pnpm dev FE+BE, server .env)",E("commit d0cb8b5"),"done",null,null],
["RESEARCH: 7 competitor scrapes (optmyzr, hyperfx, ryze, outloop, junior, syntermedia, logos)",E("competitor-scrapes/"),"done",null,null],
["DOCS: architecture HTML diagrams (setup, relationships, timeline, registry)",E("docs/build/*.html; Hermes Sep 7"),"done",null,null],
["DOCS: old agentic-ads corpus synced into repo (specs 28–31, business docs)",E("commit be7ad5e"),"done",null,null],
["TOOL: Workbench standalone (23 checks, sabotages, invariants, runs.db; `wb` bin; 65 tests, proven on 2nd repo)",E("~/Documents/coding-systems/workbench; Claude 05fc6a Aug 30 — never tracked anywhere"),"done",null,null],
["URGENT: commit + push MW-03 audit rebuild (built, 184 tests green, files UNCOMMITTED in worktree)","Audit log is marked done but server/src/audit.ts + 004_audit_log.sql sit uncommitted. Commit and push, then close. "+E("worktree status; session dig"),"todo",null,BE],
["Grill pass: spec 37 agent-control-surface — close 5 open decisions","Needs Chetan live. Blocks registry, prompts, agent layer. "+E("spec 37 design-only; session 4d7fce"),"backlog",null,null],
["Agent-control registry + kill-switch (spec 37 Phase 1)","Sequenced BEFORE agent layer. Blocked by grill pass.","backlog","f37",null],
["Agent prompt text — 8 roles as versioned rows","Not hardcoded strings. Blocked by registry.","backlog",null,null],
["Mutations-over-HTTP approval UI (new track — none exists)","fmut's real remaining blocker. Design + build approval queue UI.","backlog","fmut",null],
["Billing: Stripe integration (trials, grace period, coupons, stop-subscription)","Discussed Hermes 14:10–14:14; only in platform-admin spec. Stripe decision unconfirmed by Chetan.","backlog",null,null],
["DEPLOY: admin.verified-digital.com subdomain","apps/admin built, never deployed. Infra + DNS.","backlog",null,null],
["Rate-governor override table (per-tenant overrides)","Static caps only today.","backlog",null,BE],
["RENAME: duplicate 004_* migrations (both apply via exact-filename tracking; numbering inconsistency)","Low priority cleanup.","backlog",null,BE],
["Build check-* guard scripts + GDPR purge manifest (referenced in .claude/rules but nonexistent) OR de-reference them","pnpm check currently = prettier only. Decide + do.","backlog",null,BE],
["COMMIT: verify-plan repo STATUS stub + mirrored docs (uncommitted)","","backlog",null,null],
["HERMES: rewrite skill 'verify-ads-app-development' desc (3 attempts failed 60-char budget)","","backlog",null,null],
["MVP cut to hit END-OF-SEPTEMBER deadline — plan scope vs remaining tracks","Stated goal, tracked nowhere. CEO to propose cut list (screens subset, agent layer phase 1?). "+E("Claude 05fc6a"),"backlog",null,CE],
["SHARED: Confirm & Apply modal (phased apply: snapshot→validate→execute→verify)","g1/d10 Approve buttons render but do nothing (grepped). Own shared ticket; don't build speculatively per-screen.","backlog","fscr",FE],
["SHARED: per-screen empty-state copy in vd-states","Generic copy ships for all screens; EMPTY is per-screen-keyed. Cross-shell change.","backlog","fscr",FE],
["SHARED: ChangeDetectionStrategy.OnPush repo-wide (absent from EVERY component)","Guard or one-pass fix — never bolt onto one component.","backlog","fscr",FE],
["FIX: screens/BACKLOG.md footer says 11 done, table shows 12","One-line fix.","backlog","fscr",FE],
["BLOCKED-EXTERNAL: live platform verification (real Google/Meta/GA4/GSC credentials)","Business-side. See docs/05-business/16-build-status.md action list.","backlog",null,null],
];
let ok=0;const errs=[];
for(const [title,desc,status,parent,assignee] of T){
 const body={title,description:desc,status,projectId:ids.project||undefined,assigneeAgentId:assignee||undefined};
 if(parent&&ids.issues[parent])body.parentId=ids.issues[parent];
 let r=await call("POST",`/companies/${CID}/issues`,body);
 if(!r.ok&&parent&&ids.issues[parent])r=await call("POST",`/issues/${ids.issues[parent]}/children`,{title,description:desc,status,assigneeAgentId:assignee||undefined});
 if(!r.ok){errs.push(title.slice(0,40)+": "+r.error);continue}
 ok++;ids.issues["dig-"+title.slice(0,24)]=r.data.id;
}
const m=await call("PATCH",`/issues/${ids.issues.mw2}`,{status:"todo",assigneeAgentId:BE});
const all=await call("GET",`/companies/${CID}/issues?limit=200`);
const arr=all.data.issues??all.data;const by={};for(const i of arr)by[i.status]=(by[i.status]||0)+1;
console.log(`created ${ok}/${T.length}; mw2→todo/BE:${m.ok?"ok":m.error}; TOTAL ${arr.length}: ${JSON.stringify(by)}`);
if(errs.length)console.log("ERRS:",errs.join("\n"));
await writeFile("/Users/chetan/Documents/paperclip/.setup-ids.json",JSON.stringify(ids,null,2));
