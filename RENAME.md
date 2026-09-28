# Rename: paperclip → foresights-os

Decision (confirmed by user): rename this repo's product identity end-to-end,
everywhere — npm scope, GitHub org/repo, CLI binary name, env vars, telemetry
namespace, symbols, docs, branding. Full cutover, not an alias/shim.

Known collision, accepted: the user has a separate, unrelated product also
called Foresights-OS (a Tauri desktop knowledge-vault app). This repo (an
AI-agent-company control plane) is a different product. Name collision is
intentional and accepted — do not try to disambiguate further unless told to.

## Do we actually need npm / GitHub / a CLI name change?

Answering the question as asked, not just "yes because it's part of renaming":

- **npm**: not load-bearing to keep the old name. `@paperclipai/*` is a real,
  currently-published scope (confirmed live: `@paperclipai/server@2026.831.1`,
  `paperclipai` CLI has 1447 published versions on npm, CI has a working
  `NPM_TOKEN` publish step in `.github/workflows/release.yml`). npm has no
  rename operation — old package names can only be deprecated, never
  reassigned or deleted. So "renaming npm" really means: stop publishing under
  the old scope, start publishing under a new one, deprecate the old packages
  pointing at the new ones. This is a few `npm deprecate` calls plus updating
  CI, not a blocker.
- **GitHub**: not strictly required either, but cheap to do — GitHub repo/org
  renames transparently redirect old clone/API URLs, so this is low-risk
  compared to npm. Recommend renaming in place (keep issues/stars/PR history)
  rather than standing up a new org.
- **CLI binary name** (`paperclipai`): this is the command a human types.
  Purely a decision, no technical requirement either way. Since the product is
  becoming foresights-os, the bin name should match it for consistency, unless
  you want to keep `paperclipai` as a stable command name for existing users.

Recommendation: rename all three, since the goal is a real rebrand and none of
the three block correctness — they're identity/branding surfaces, not runtime
architecture.

## Concrete naming decisions needed (pick or confirm defaults)

| Surface | Old | Proposed default |
|---|---|---|
| npm scope | `@paperclipai` | `@foresights-os` |
| CLI bin | `paperclipai` | `foresights-os` |
| GitHub org | `paperclipai` | `foresights-os` |
| GitHub repo | `paperclip` | `foresights-os` |
| Env var prefix | `PAPERCLIP_*` | `FORESIGHTS_OS_*` |
| Telemetry namespace | `paperclip.*` (dotted events) | `foresights_os.*` |
| Root package name | `paperclip` | `foresights-os` |

If you don't object, I'll proceed with these defaults when executing.

## Measured scope (confirmed by grep/codegraph, this session)

- 5,515 case-insensitive occurrences of "paperclip" repo-wide (excluding
  node_modules, pnpm-lock.yaml, .codegraph, .git).
- 45 `package.json` files in the workspace; 40 of them are under the
  `@paperclipai/*` scope (server, ui, db, shared, all adapters, all plugins,
  cli, mcp servers, sandbox providers, etc).
- CLI bin `paperclipai` (`cli/package.json`), published, `publishConfig.access:
  public`.
- `server` and `cli` (at least) have `publishConfig` and are actively
  published — this is not a private-only monorepo.
- GitHub remote: `github.com/paperclipai/paperclip`.
- `PAPERCLIP_*` env vars: dozens distinct (e.g. `PAPERCLIP_AGENT_ID`,
  `PAPERCLIP_AGENT_JWT_AUDIENCE`, `PAPERCLIP_ACPX_*` family, `PAPERCLIP_ADAPTERS`).
  These are read by the running server/CLI/adapters — a live surface, not
  cosmetic.
- Telemetry: generated contract at
  `packages/shared/src/telemetry/generated/paperclip-telemetry.ts` with dotted
  event names like `paperclip.agent.turn`, `paperclip.capability.*`. Per
  AGENTS.md this is the **strict-review telemetry path** (opt-out, sends data
  to a Paperclip-owned endpoint by default) — renaming the namespace needs a
  regenerated contract + README update + privacy review, not a blind
  find/replace.
- Domain references in code/CI: `paperclip.ai`, `paperclip.com`,
  `paperclip.dev` literal strings.
- Symbol-level identifiers found via `codegraph query paperclip`:
  `PaperclipLockupProps`, `PaperclipSemanticDispatcher`,
  `PaperclipControlPlaneBinding`, `PaperclipRunnerPermissionOption`,
  `PaperclipAgentTaskRunDimensions`, `PaperclipGoalCreatedDimensions`, etc —
  these need identifier renames (definition + every call site), not just
  string substitution, or the codebase won't compile.
- Brand assets: `ui/src/components/PaperclipLockup.tsx`,
  `docs/images/logo-{dark,light}.svg`, `server/src/ui-branding.ts` +
  associated branding routes/tests.
- `doc/`: 189 files reference "paperclip"; `doc/connections/CONNECTOR-PLAYBOOK.md`
  alone has 80 occurrences (external plugin-author-facing doc).
- Plugin authoring surface: `create-paperclip-plugin` scaffolding package and
  `createPaperclipPlugin()` helper function — used by **third-party plugin
  authors**, not just internal code. Renaming this changes the API surface
  anyone building a Paperclip plugin sees.
- CI: `.github/workflows/release.yml` is the one workflow that actually runs
  `npm publish` with `NPM_TOKEN`.

## Why this can't be one global sed

Three different rename mechanics are mixed together:
1. **Pure text/string rename** (docs, comments, UI copy, docker/CI yaml,
   domain strings) — safe as a global find/replace once case variants are
   handled (Paperclip / paperclip / PAPERCLIP / paperclipai).
2. **Structural rename that must keep the codebase compiling** (package
   names, imports of `@paperclipai/x`, TS identifiers like
   `PaperclipLockupProps`, DB/schema exports, env var names read via
   `process.env.PAPERCLIP_X`) — needs codegraph-assisted rename (find
   definition + every call site) and a typecheck/build gate after each batch,
   not a blind sed, or intermediate states won't compile and it's hard to
   bisect where a break was introduced.
3. **External identity operations** (npm publish under a new scope + deprecate
   old, GitHub org/repo rename, telemetry contract regeneration + privacy
   review) — one-time manual/CI operations, not code edits, done at the end
   once the code itself is fully renamed and green.

## Phased plan (dependency-ordered, each phase gated)

Gate after each phase per AGENTS.md §7: run the narrowest relevant check
first (targeted typecheck/test for the touched package); run the full
`pnpm -r typecheck && pnpm test:run && pnpm build` at the end of the whole
rename, and again before any PR/hand-off.

**Phase 0 — Freeze naming decisions**
Confirm the table above (npm scope, CLI bin, env prefix, telemetry namespace).
Nothing else starts until this is locked, because every later phase reuses
these exact strings.

**Phase 1 — Workspace package renames**
Rename all 40 `@paperclipai/*` package names to `@foresights-os/*` in every
`package.json`, plus every internal `workspace:*` dependency reference to
those names (adapters, plugins, shared, db, mcp servers, sandbox providers).
Rename root package `paperclip` → `foresights-os`. Rename CLI package name +
`bin` entry `paperclipai` → `foresights-os`.
Gate: `pnpm install` succeeds (workspace links resolve), `pnpm -r typecheck`.

**Phase 2 — Import path + identifier rename (codegraph-assisted)**
Update every `import ... from "@paperclipai/x"` across the repo to the new
scope (mechanical, but must hit all ~5,515-string-occurrence files, not just
`package.json`s). Then use `codegraph query paperclip` / `codegraph impact
<symbol>` to enumerate every `Paperclip*`-named exported class/interface/type
(e.g. `PaperclipLockupProps`, `PaperclipSemanticDispatcher`,
`PaperclipControlPlaneBinding`) and rename definition + all call sites
together per symbol — never rename a definition without checking impact
first.
Gate: `pnpm -r typecheck`.

**Phase 2b — Stateful identity strings (auth, DB, frontend prefs) — NEW, needs a decision**

Found on closer inspection of db/auth/frontend/RBAC specifically. These are
NOT plain renames — they are identity strings baked into *live state* on
every existing install (your own dev machine's DB, any deployed instance's
sessions). Renaming them has a real upgrade consequence, not just a cosmetic
one:

- **Embedded Postgres identity**: DB name, username, AND password are all the
  literal string `"paperclip"` (`server/src/index.ts`:
  `postgres://paperclip:paperclip@127.0.0.1:<port>/paperclip`,
  `ensurePostgresDatabase(..., "paperclip")`). Renaming this means new
  installs get a `foresights-os` DB/user, but **existing local/prod databases
  still have DB name/creds `paperclip`** — code must either keep reading the
  old name for existing installs (migration-aware) or you accept a one-time
  manual DB rename per instance.
- **Auth session cookie prefix**: derived as `` `paperclip-${instanceId}` ``
  in `server/src/auth/better-auth.ts:57`. Renaming this **logs out every
  active session** on the next deploy (old cookie name is no longer read).
  Acceptable one-time event, or does it need a dual-read transition period?
- **Signed-token domain-separation strings**: `workspace-login-handoff.ts`
  hashes tickets with literal strings `paperclip.workspace-login-handoff.<v>`
  and `paperclip.workspace-readiness-probe.<v>` baked into the HMAC input.
  Renaming these **invalidates any in-flight handoff ticket** at the moment
  of deploy (short-lived tokens, so low actual risk — but worth stating, not
  silently changing crypto input).
- **Cross-service headers**: `x-paperclip-workspace-readiness-token`,
  `x-paperclip-workspace-readiness-user-id/email`, and `x-paperclip-cloud-*`
  headers are a contract between this server and whatever calls it
  (workspace handoff caller, cloud proxy). If anything external sends these
  headers today, a rename breaks that caller until it's updated too — check
  whether workspace-handoff/cloud-proxy call sites are in this repo (covered
  by Phase 2) or external (need coordinated rollout).
- **Frontend saved preference key**: `localStorage` key `"paperclip.theme"`
  in `ui/index.html`. Renaming this **silently resets every user's saved
  theme** to default on next load, unless you migrate the old key forward.
- **Frontend page title / PWA name**: `ui/index.html` `<title>Paperclip</title>`
  and `apple-mobile-web-app-title="Paperclip"` — plain cosmetic rename, no
  state concern, just flagging it was missing from Phase 5 originally.
- **Local dev admin identity**: `local@paperclip.local` hardcoded — cosmetic,
  safe rename.
- **RBAC**: no role/permission-specific literals found; RBAC code only
  references "paperclip" via package imports (Phase 1/2) and one env var
  (`PAPERCLIP_RESPONSIBLE_USER_AUTHZ_MODE`, covered by Phase 3). No dedicated
  RBAC phase needed.

**Decided (user, pre-launch, no real users yet): clean one-time break.**
No dual-read/migration shims for DB identity, session cookie prefix, or
saved theme key. New installs get `foresights-os` identity everywhere;
any existing local dev DB just gets recreated under the new name/creds.

**Phase 3 — Env vars**
Rename `PAPERCLIP_*` → `FORESIGHTS_OS_*` across server/adapters/CLI/docker/CI,
including `.env.example` files and any docs that list env vars. Since this is
a full cutover (no alias), grep for `process.env.PAPERCLIP` and
`Bun.env.PAPERCLIP` (or equivalent) after the rename to confirm zero
survivors.
Gate: `pnpm test:run` for server + adapters (env vars are read at startup —
this is the phase most likely to break silently without a test run).

**Phase 4 — Telemetry contract (strict-review path per AGENTS.md)**
Regenerate `packages/shared/src/telemetry/generated/paperclip-telemetry.ts`
(rename file too) with the new `foresights_os.*` dotted event namespace.
Update `packages/shared/src/telemetry/README.md` in the same change (required
by AGENTS.md). Flag for a privacy review before merge — this is the one
phase that isn't "just a rename," it changes what a live telemetry event
looks like.
Gate: telemetry contract test suite (`client-contract.test.ts`,
`readme-contract.test.ts`).

**Phase 5 — Branding assets**
Rename `PaperclipLockup.tsx` → e.g. `ForesightsOSLockup.tsx`, swap
`docs/images/logo-{dark,light}.svg` for new artwork (or placeholder if new
artwork isn't ready yet — flag this explicitly rather than shipping the old
logo under a new name), update `ui-branding.ts` and related branding
route/tests, update any UI copy strings that say "Paperclip".
Gate: UI component tests for branding (`ui-branding.test.ts`,
`company-branding-route.test.ts`, `invite-logo-route.test.ts`) +
`pnpm check:token-gates` if any styling touched.

**Phase 6 — Plugin authoring surface**
Rename `create-paperclip-plugin` package and `createPaperclipPlugin()`
helper. This is the one phase with an external-developer-facing breaking
change (anyone who scaffolded a plugin with the old tool). Decide: hard
rename, or keep the old export as a deprecated re-export for one release?
(Default recommendation: hard rename, since you said full cutover — but flag
this explicitly since it's the one place a real third party could be
affected, not just you.)
Gate: plugin SDK test suite + one example plugin build
(`plugin-hello-world-example`) to confirm scaffolding still works end to end.

**Phase 7 — Docs**
Global replace across `doc/` (189 files) and `AGENTS.md`/`README.md`,
including `doc/connections/CONNECTOR-PLAYBOOK.md` (80 occurrences, most
dense). Update domain string literals (`paperclip.ai/.com/.dev`) to their
foresights-os equivalents, or to placeholders if the new domains aren't
registered yet — call that out rather than inventing a domain.
Gate: none (docs), but grep-verify zero remaining case-insensitive
"paperclip" hits outside intentionally-kept historical references (e.g.
CHANGELOG entries, which should stay as history, not be rewritten).

**Phase 8 — Docker / CI**
Rename image tags, workflow names/comments, and any `paperclip` strings in
`Dockerfile*`, `docker-compose*.yml`, `.github/workflows/*.yml` (including the
one publish-bearing workflow, `release.yml`). Update `NPM_TOKEN` target scope
if npm publish config changes (new scope needs its own npm org/token setup —
external action, see Phase 9).
Gate: `docker build` for at least the main `Dockerfile` and one
`docker/agent-runtime/Dockerfile.*` to confirm the rename didn't break image
build args/labels.

**Phase 9 — External identity operations (one-time, not code)**
- npm: create `@foresights-os` org on npmjs, publish first versions of the
  renamed packages, then `npm deprecate @paperclipai/x "moved to
  @foresights-os/x"` for each of the 40 old packages (and `paperclipai` CLI)
  pointing at the new name. Old packages stay resolvable forever (npm never
  deletes) — deprecation is the correct hygiene move, not deletion.
- GitHub: rename org `paperclipai` → `foresights-os` and repo `paperclip` →
  `foresights-os` in place (keeps issues/PRs/stars, GitHub auto-redirects old
  URLs). Update the git remote locally after rename:
  `git remote set-url origin https://github.com/foresights-os/foresights-os`.
- Update any external references to the old GitHub URL that GitHub's redirect
  won't cover (e.g. hardcoded URLs in docs already handled in Phase 7,
  webhook configs, deploy configs pointing at the old clone URL).

**Phase 10 — Final full verification**
`pnpm -r typecheck && pnpm test:run && pnpm build`, plus a final repo-wide
grep for residual case-insensitive "paperclip" outside intentional history
(CHANGELOG, git log messages — never rewritten). Report any survivors
explicitly rather than silently leaving them.

## Order rationale

Phases 1→3 must happen before 2 can fully compile (package names first,
then everything that imports them, then env vars which are runtime-only and
independent of the type system). Phase 4 (telemetry) is isolated and can run
in parallel with 5/6/7/8 once phases 1-3 are green, since none of those touch
the telemetry contract. Phase 9 (external ops) must be last — no point
publishing/renaming externally until the code itself is fully renamed and
gated green, or you'd publish a broken package under the new name.

## Effort note

Given your build cadence (agentic coding, not a traditional team), phases 1-8
are mechanical-but-large — the actual work is running codegraph-assisted
rename scripts and clearing typecheck/test errors batch by batch, which is a
tool-throughput problem, not a design problem. The one place effort is
genuinely bounded by reality rather than typing speed is Phase 9: npm org
creation, GitHub org rename, and confirming redirects/publishes actually work
externally — that's a real external-system loop, not something to estimate
by lines changed.

## Open questions before execution starts

1. Confirm the naming table above (scope/bin/env-prefix/telemetry namespace),
   or override any row.
2. Phase 5: do you have new foresights-os brand artwork (logo SVGs) ready, or
   should this phase ship a placeholder / defer the actual asset swap?
3. Phase 6: hard rename `createPaperclipPlugin`, or keep a deprecated
   re-export for compatibility?
4. Phase 7: do `paperclip.ai` / `.com` / `.dev` domains have real
   foresights-os replacements registered, or are these placeholders for now?
5. Do you want this done as one long sequential run, or batched (e.g. "two
   phases at a time, verified and committed, then move to the next") per your
   usual delegation cadence?
