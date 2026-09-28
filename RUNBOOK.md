# Agentic Ads on Paperclip — RUNBOOK

**Server:** `/Users/chetan/Documents/paperclip` · UI: http://127.0.0.1:3100 · API mode: local_trusted
**Node:** handled automatically — `.npmrc` has `use-node-version=26.8.2`, so pnpm runs Paperclip on Node 26 for this project only (your default node 22 is untouched). No PATH sourcing needed.
**IDs:** `.setup-ids.json` (company, agents, issues) · bootstrap scripts: `bootstrap-org.mjs`, `bootstrap-fix.mjs` (idempotent-ish; re-run needs care).

## Daily start

```bash
cd /Users/chetan/Documents/paperclip && pnpm dev
# optional one-word alias in ~/.zshrc:
#   alias paperclip-dev='cd /Users/chetan/Documents/paperclip && pnpm dev'
```

Subsequent starts take ~30–60s. Server is up when http://127.0.0.1:3100 returns 200.

## The org (all heartbeats OFF — event-only: agents wake on assignment or @mention only)

| Agent | Role | Runtime / model | Owns |
|---|---|---|---|
| CEO | ceo | opencode · zai-coding-plan/glm-5.2 | delegation per SEQUENCE.md |
| API Contracts Eng | engineer | opencode · glm-5.2 | ServiceClient factory, contracts, E13 tokens |
| Backend Eng | engineer | opencode · glm-5.2 | middleware MW-01→03→02, adapters |
| Database Eng | engineer | opencode · glm-5.2 | warehouse, migrations, RLS |
| Frontend Eng | engineer | opencode · glm-5.2 | screens/BACKLOG.md |
| Reviewer | qa | **claude_local · claude-sonnet-5** | code-review gate — you merge |
| Researcher | researcher | **hermes_local · zai/glm-5.3** | research, domain terms |

Skills attached (company library): implement, tdd, code-review, codebase-design, domain-modeling, research, prototype, resolving-merge-conflicts, writing-for-agents. `diagnosing-bugs` was blocked by the import trust gate (ships scripts) — agents reach it via the repo's own `.agents/skills/diagnosing-bugs` (their cwd), referenced in their AGENTS.md.

## Work loop (how a ticket ships)

1. **Issues page** → MW-01 (todo, assigned Backend Eng). Heartbeats are off, so nothing runs until you either assign a new issue (wake-on-assignment) or open an agent and click **Run Heartbeat**.
2. Watch the run stream (Agents → Backend Eng → Runs).
3. Agent posts diff as work product, moves issue to `in_review` — never commits.
4. Assign the issue to **Reviewer** (or @Reviewer in a comment) → code-review skill → findings on the issue.
5. **You merge.** Update SEQUENCE.md when a track changes state (single planning truth).

## Status views

- Dashboard: task breakdown + agent states + spend. Issues board: kanban per status (done column collapses).
- Blocked Inbox: what's jammed and why (blocked-by edges mirror SEQUENCE.md).
- The 9 dependency edges (mw2←mw1, pa2←pa1, pa3←pa1+pa2, ap2←mw3, fagent←mw3+fmem+f37, fmut←mw3) make out-of-order starts structurally impossible.

## Known caveats

- **GitHub**: `GITHUB_TOKEN` stored as company secret → external-reference status pills on pasted PR/issue links. Provider auths are local CLI logins (claude/opencode/hermes) — no raw API keys needed.
- **Project workspace binding**: project `agentic-ads` exists but the workspace-to-repo binding should be confirmed in UI (Projects → agentic-ads → set workspace path to `/Users/chetan/Documents/verify-ads-app`) so skills scan + worktrees anchor correctly.
- **Audit-log collision resolved**: agency-panel/02 imported as audit log *viewer* consuming MW-03's table (MW-03 owns `server/src/audit.ts` + migration 004).
- Verify the heartbeat toggles read OFF in each agent's page on first login (default is off; no intervals were set).
- `.setup.env` holds COMPANY_ID; `.setup-ids.json` all entity ids for scripting.
