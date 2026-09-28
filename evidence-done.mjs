// Append "What was done" evidence to every done issue: git stat / screen folder / scratch ticket text.
import { readFile, writeFile } from "node:fs/promises";
import { execSync } from "node:child_process";
const API = "http://127.0.0.1:3100/api", CID = process.env.COMPANY_ID, APP = "/Users/chetan/Documents/verify-ads-app";
const ids = JSON.parse(await readFile("/Users/chetan/Documents/paperclip/.setup-ids.json", "utf8"));
const call = async (m, p, b) => { const r = await fetch(API + p, { method: m, headers: { "Content-Type": "application/json" }, body: b ? JSON.stringify(b) : undefined }); const t = await r.text(); let j = null; try { j = JSON.parse(t); } catch {}; return r.ok ? { ok: true, data: j } : { ok: false, error: t.slice(0, 80) } };
const gs = sha => { try { return execSync(`git -C ${APP} show --stat --format="%h %s" ${sha}`, { encoding: "utf8" }).split("\n").slice(0, 14).join("\n"); } catch { return null; } };
const SHA = [[/adapters.*GA4|bug-hunt/, "b9ff6c6"], [/RBAC security review/, "65ea347"], [/core-services/, "f963bcf"], [/honesty/, "6ca4f77"], [/reports-flow/, "3ba2eb9"], [/server\/BFF 7/, "b9ff6c6"], [/d1 Chat/, "cf0cc6f"], [/spec 36 \+ 37/, null], [/SEQUENCE\.md master/, null], [/docs wiki hub/, "ed9ce45"], [/graphify-out/, "6149bc6"], [/verify:styles/, "4ac1abd"], [/bundle split/, "e3ad7c2"], [/--on-tone/, "fd392a9"], [/lessons corpus/, null], [/one-command dev/, "d0cb8b5"], [/corpus synced/, "be7ad5e"], [/Rate governor MW-01/, "1b08ec8"], [/Audit log MW-03/, null], [/Feature flags/, "2ec67b6"], [/Platform-admin identity/, "2ec67b6"], [/admin Angular console|apps\/admin/, "a6b25bf"], [/Clients CRUD/, "68a5f14"], [/find-first|Dynamic report engine/, "ae2acd5"], [/migrations-db|BFF NestJS|native Postgres/, "a20c85a"], [/RBAC full stack|matrix/, "f148cbc"], [/MW-01|rate governor/i, "1b08ec8"]];
const SCRATCH = [[/RBAC — matrix/, ".scratch/rbac/01-matrix.md"], [/RBAC — db-guard/, ".scratch/rbac/02-db-guard.md"], [/RBAC — team API/, ".scratch/rbac/03-team-api.md"], [/RBAC — frontend/, ".scratch/rbac/04-frontend.md"], [/BFF — migrations/, ".scratch/backend-bff/01-migrations-db.md"], [/BFF — connections/, ".scratch/backend-bff/02-connections.md"], [/BFF — reports/, ".scratch/backend-bff/03-reports.md"], [/BFF — sync/, ".scratch/backend-bff/04-sync.md"], [/GA4 metadata/, ".scratch/max-report-coverage/01-ga4-metadata-and-families.md"], [/GSC dimensions/, ".scratch/max-report-coverage/02-gsc-dimensions-sitemaps.md"], [/Meta breakdowns/, ".scratch/max-report-coverage/03-meta-breakdowns.md"], [/Meta async/, ".scratch/max-report-coverage/04-meta-async-runner.md"], [/gAds segments/, ".scratch/max-report-coverage/05-gads-segments-is-quality.md"], [/gAds views/, ".scratch/max-report-coverage/06-gads-views.md"], [/pg-boss sync jobs/, ".scratch/middleware-build/02-pgboss-sync-jobs.md"], [/rate governor/i, ".scratch/middleware-build/01-rate-governor.md"], [/audit log/i, ".scratch/middleware-build/03-audit-log.md"]];
const all = await call("GET", `/companies/${CID}/issues?limit=200`);
const arr = all.data.issues ?? all.data;
let n = 0, skipped = 0;
for (const i of arr) {
  if (i.status !== "done") continue;
  let done = null;
  const sha = SHA.find(([re]) => re.test(i.title))?.[1];
  if (sha) { const s = gs(sha); if (s) done = `Commit evidence:\n\`\`\`\n${s}\n\`\`\``; }
  if (!done && /^Screen /.test(i.title)) {
    const code = i.title.match(/Screen ([a-z]\d+|ch-[a-z-]+)/)?.[1];
    if (code) { try { const ls = execSync(`ls ${APP}/agentic-ads/screens/ | grep ${code} ; ls ${APP}/agentic-ads/screens/*${code}*/ 2>/dev/null | head -8`, { encoding: "utf8" }).trim(); done = `Built artifacts:\n\`\`\`\n${ls}\n\`\`\``; } catch {} }
  }
  if (!done) { const f = SCRATCH.find(([re]) => re.test(i.title))?.[1]; if (f) { try { done = `Ticket source (${f}):\n\`\`\`markdown\n` + (await readFile(APP + "/agentic-ads/" + f, "utf8")).slice(0, 1800) + "\n```"; } catch { try { done = "Ticket source:\n```markdown\n" + (await readFile(APP + "/" + f, "utf8")).slice(0, 1800) + "\n```"; } catch {} } } }
  if (!done) { skipped++; continue; }
  const desc = (i.description || "") + `\n\n## What was done\n${done}\n`;
  const r = await call("PATCH", `/issues/${i.id}`, { description: desc });
  if (r.ok) n++;
}
console.log(`evidenced ${n} done issues, skipped ${skipped} (no match)`);
