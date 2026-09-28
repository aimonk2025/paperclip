# RANSACK — measurement pack

`/Users/chetan/Documents/coding-systems/paperclip/paperclip-latest`  ·  generated in 27s  ·  **no LLM: every number is parsed or computed**

> Measure before you rebuild. These numbers set the target; the
> ladder decides what is actually yours to build.

---

## Structural inventory — THE COUNT TO MATCH

Community detection finds where code is dense. This counts the
things. **Parity is the default** — if they ship 12 adapters and
you build 5, that is an unfinished port, not a simplification.

| where | kind | count | members |
|---|---|---|---|
| `ui/src/adapters` | adapter | **13** | `claude-local`, `codex-local`, `cursor`, `cursor-cloud`, `gemini-local`, `grok-local`, `hermes-gateway`, `hermes-local` +5 |
| `packages/adapters` | adapter | **11** | `claude-local`, `codex-local`, `cursor-cloud`, `cursor-local`, `gemini-local`, `grok-local`, `hermes`, `hermes-gateway` +3 |
| `packages` | package | **9** | `adapter-utils`, `db`, `google-sheets-mcp-server`, `kv-demo-mcp-server`, `mcp-server`, `shared`, `skills-catalog`, `tailscale-https-broker` +1 |
| `packages/plugins/sandbox-providers` | plugin | **7** | `cloudflare`, `daytona`, `e2b`, `exe-dev`, `kubernetes`, `modal`, `novita` |
| `packages/plugins/plugin-llm-wiki/skills` | plugin | **6** | `index-refresh`, `paperclip-distill`, `wiki-ingest`, `wiki-lint`, `wiki-maintainer`, `wiki-query` |
| `server/src` | sibling-group | **5** | `adapters`, `middleware`, `routes`, `services`, `storage` |
| `packages/plugins` | plugin | **5** | `create-paperclip-plugin`, `paperclip-plugin-fake-sandbox`, `plugin-llm-wiki`, `plugin-workspace-diff`, `sdk` |
| `packages/plugins/examples` | plugin | **5** | `plugin-authoring-smoke-example`, `plugin-file-browser-example`, `plugin-hello-world-example`, `plugin-kitchen-sink-example`, `plugin-orchestration-smoke-example` |
| `packages/skills-catalog/catalog/bundled/paperclip-operations` | skill | **5** | `issue-triage`, `reflection-coach`, `status-card-query`, `summarize-status`, `task-planning` |
| `skills` | skill | **5** | `paperclip`, `paperclip-board`, `paperclip-converting-plans-to-tasks`, `paperclip-create-agent`, `para-memory-files` |
| `packages/adapters/hermes/src` | adapter | **4** | `cli`, `gateway`, `server`, `ui` |
| `<root>` | sibling-group | **3** | `cli`, `server`, `ui` |

**Entrypoints:** cli (40) · migration (40) · http server (19) · mcp server (16) · websocket (7) · worker/queue (4) · cron/schedule (2)

**Largest unions:** `ToolAccessReasonCode` (16 arms), `ProjectConfigFieldKey` (15 arms), `PaperclipEventName` (14 arms), `PipelineHealthWarningCode` (13 arms), `IssueBlockedInboxReason` (12 arms), `CatalogTeamFileKind` (12 arms)

Full detail: `ransack-out/INVENTORY.md`

## Survey — history, schema, config

```
================================================================
COVERAGE
  indexed              : 4712
  NOT indexed          : 1474
        613 .json
        435 .md
        226 .sql
         91 .png
         41 .sh
         29 .svg

DATABASE  (invisible to the index — parsed here)
  226 migrations · 188 tables · 2421 columns · 645 indexes
  foreign keys 683 (602 ALTER TABLE + 81 inline) · enums 0 · RLS statements 0

MODULES   : 42
TESTS     : 1372 test / 3343 source (ratio 0.41)
CONFIG    : 316 env vars · 60 flags

WHAT KEPT BREAKING  (fix/revert commits)
   39  server/src/services/heartbeat.ts
   26  server/src/routes/issues.ts
   23  server/src/services/issues.ts
   14  server/src/__tests__/heartbeat-process-recovery.test.ts
   13  ui/src/pages/Inbox.test.tsx
   13  packages/adapters/codex-local/src/server/execute.ts
   12  server/src/index.ts
   12  ui/src/pages/Inbox.tsx

OLDEST UNTOUCHED  (stable or abandoned — check which)
  2026-02-16  server/src/middleware/index.ts
  2026-02-16  server/src/middleware/validate.ts
  2026-02-17  cli/src/checks/port-check.ts
  2026-02-17  cli/src/prompts/llm.ts
  2026-02-17  cli/src/utils/net.ts
  2026-02-17  packages/db/drizzle.config.ts
================================================================
```

## Call-graph completeness

```
========================================================================
UNRESOLVED REFERENCE CLASSIFICATION
========================================================================
  resolved edges        : 122,407
  unresolved refs (raw) : 144,617
  naive "failure rate"  : 54%  ← MISLEADING

    12,990   9.0%  external-runtime
            e.g. AbortController, Array, ArrayBuffer, Blob, Boolean
       183   0.1%  external-package
            e.g. clsx, express, modal, multer, open
     1,811   1.3%  test-framework
            e.g. assert, beforeAll, describe, expect, it
    44,644  30.9%  external-unknown
            e.g. A, ACCESS, ALIAS, AND, ANY
       570   0.4%  parse-artifact
            e.g. doc__0_the_one_hard_prerequisite_a_local, doc__10_outbound_synchronization_and_wri, doc__13_auto_recover_vs_explicit_recover, doc__16_4_recommended_extensions_not_req, doc__1_1_hex_colors_exact_near_matches_a
★        2   0.0%  workspace-package
            e.g. paperclipai
★   84,417  58.4%  true-gap
            e.g. API, AcceptInvitePreview, AccessSection, AccountingModelCard, ActionCard

========================================================================
THE HONEST NUMBERS
========================================================================
  NOT a defect (external code, correctly unresolved) : 59,628 (41%)
  needs TYPE INFERENCE (a.b on a local var)          : 0 (0%)  ← inherent to AST-only analysis
  indexer noise (parse artifacts)                    : 570
  ★ actually fixable                                 : 84,419 (58%)
       path-alias  (@/... tsconfig alias)   : 0
       workspace-package (monorepo imports) : 2
       true-gap (name IS a node here)       : 84,417

========================================================================
★ CALL-GRAPH COMPLETENESS — the number that matters
========================================================================
  resolved call edges          : 32,617
  unresolved INTERNAL calls    : 84,419
  >>> CALL-GRAPH COMPLETENESS  : 27.9%

  impact/callers sees ~28% of internal call edges.
  Treat results as a FLOOR, but a tight one — not the 48% the raw
  unresolved_refs count implies.

  NOTE: unresolved IMPORTS are harmless. Verified — `cn` imported
  via the "@/lib/utils" alias still resolves 20 callers correctly.
  The index links call edges by symbol, not by import specifier.

  top fixable names:
      4,275  eq
      2,759  map
      2,358  get
      2,280  from
      1,977  join
      1,797  set
      1,546  and
      1,428  has
      1,384  asString
      1,043  resolve
        847  update
        804  json
```

## Modules — Leiden consensus (WHERE the modules are)

```
==========================================================================
ALGORITHM leiden   RESOLUTION 2.5   SEEDS 5
NMI vs seed-1: [0.9357, 0.9208, 0.931, 0.9413]   (1.0 = identical partition)
→ a SINGLE run is ~92% reproducible. Counts below are APPROXIMATE.
stable co-memberships kept: 12,572
COMMUNITIES: ~238 (size >= 4)
==========================================================================

~ 642 nodes  [deep    ] conductance 0.25 stab 0.582
     packages: ui/src/components(79), packages/adapters(78), server/src/__tests__(78)
     hubs    : replace, rewriteFile, formatClaudeCliDetail, code, hasSelectiveWhere

~ 631 nodes  [moderate] conductance 0.43 stab 0.543
     packages: services/issues.ts(115), server/src/__tests__(65), services/recovery(56)
     hubs    : issueService, count, environmentService, accessService, visibleIssueCondition

~ 397 nodes  [deep    ] conductance 0.11 stab 0.2
     packages: packages/adapters(294), packages/adapter-utils(91), server/src/routes(4)
     hubs    : execute, execute, execute, execute, execute

~ 377 nodes  [moderate] conductance 0.26 stab 0.201
     packages: ui/src/components(121), ui/src/pages(64), server/src/__tests__(47)
     hubs    : setTimeout, useHeldSelfTalk, scrollToLatestCommentWithSettle, check, createSessionReuseStore

~ 370 nodes  [moderate] conductance 0.29 stab 0.203
     packages: ui/src/pages(132), ui/src/lib(58), ui/src/components(46)
     hubs    : useCompany, useBreadcrumbs, AppsConnect, Layout, useNavigate

~ 354 nodes  [moderate] conductance 0.48 stab 0.2
     packages: ui/src/components(69), ui/src/pages(60), packages/plugins(55)
     hubs    : createTestHarness, firstNonEmptyLine, listIssueBlockerAttentionMap, isInCompany, localFolderKey

~ 351 nodes  [moderate] conductance 0.41 stab 0.579
     packages: ui/src/lib(49), ui/src/components(35), packages/teams-catalog(30)
     hubs    : sort, teamsCatalogService, classifyTaskWatchdogSubtree, buildCatalogTeam, renderCatalogProvenanceYaml

~ 349 nodes  [moderate] conductance 0.36 stab 0.514
     packages: packages/db(64), server/src/__tests__(20), server/src/index.ts(19)
     hubs    : startServer, createPluginJobScheduler, createDurableRunLogStore, reconcilePendingMigrationHistory, inspectMigrations

~ 315 nodes  [moderate] conductance 0.34 stab 0.2
     packages: services/company-skills.ts(186), packages/adapter-utils(22), cli/src/install-store.ts(17)
     hubs    : companySkillService, dirname, normalizePortablePath, auditInstalledSkillBytes, ensureSkillInventoryCurrent

~ 293 nodes  [deep    ] conductance 0.23 stab 0.77
     packages: services/heartbeat.ts(184), server/src/routes(14), services/recovery(10)
     hubs    : executeRun, redactCurrentUserText, appendRunEvent, claimQueuedRun, startNextQueuedRunForAgent

~ 271 nodes  [moderate] conductance 0.27 stab 0.579
     packages: ui/src/lib(164), ui/src/pages(43), ui/src/hooks(21)
     hubs    : IssueDetail, Inbox, handleKeyDown, runs, Dashboard

~ 262 nodes  [moderate] conductance 0.44 stab 0.393
     packages: services/secrets.ts(68), services/workspace-file-resources.ts(34), server/src/secrets(25)
     hubs    : unprocessable, secretService, workspaceFileResourceService, HttpError, createSecretProposalsService

~ 253 nodes  [deep    ] conductance 0.03 stab 0.6
     packages: cli/src/commands(222), cli/src/__tests__(18), packages/shared(5)
     hubs    : action, printOutput, resolveCommandContext, handleCommandError, addCommonClientOptions

~ 224 nodes  [deep    ] conductance 0.23 stab 0.205
     packages: server/src/__tests__(32), packages/adapter-utils(31), services/workspace-git-operation-scheduler.ts(25)
     hubs    : UnixBrokerClient, listen, WorkspaceGitOperationScheduler, destroy, BrokerClientError

~ 216 nodes  [moderate] conductance 0.31 stab 0.366
     packages: cli/src/commands(38), server/src/__tests__(25), packages/plugins(18)
     hubs    : exit, onboard, confirm, require, runCommand

~ 214 nodes  [moderate] conductance 0.36 stab 0.2
     packages: ui/src/components(87), ui/src/lib(48), ui/src/pages(31)
     hubs    : AgentConfigForm, NewIssueDialog, mark, BoardChat, NewAgentDialog

~ 195 nodes  [moderate] conductance 0.33 stab 0.2
     packages: services/company-portability.ts(121), server/src/routes(14), server/src/__tests__(9)
     hubs    : parseYamlScalar, companyPortabilityService, exportBundle, importBundle, normalizeAgentUrlKey

~ 188 nodes  [moderate] conductance 0.40 stab 0.2
     packages: server/src/routes(96), services/summary-slots.ts(21), server/src/__tests__(17)
     hubs    : forbidden, summarySlotService, toolGatewayRoutes, builtInAgentRoutes, actorMiddleware

==========================================================================
INTENT vs REALITY — ~53 module(s) whose behaviour crosses package lines
==========================================================================

~642 nodes · purity 0.12 across 85 packages
  packages : ui/src/components(79), packages/adapters(78), server/src/__tests__(78), packages/plugins(50)
  hubs     : replace, rewriteFile, formatClaudeCliDetail

~631 nodes · purity 0.18 across 92 packages
  packages : services/issues.ts(115), server/src/__tests__(65), services/recovery(56), server/src/routes(45)
  hubs     : issueService, count, environmentService

~377 nodes · purity 0.32 across 42 packages
  packages : ui/src/components(121), ui/src/pages(64), server/src/__tests__(47), packages/adapter-utils(34)
  hubs     : setTimeout, useHeldSelfTalk, scrollToLatestCommentWithSettle

~370 nodes · purity 0.36 across 31 packages
  packages : ui/src/pages(132), ui/src/lib(58), ui/src/components(46), ui/src/hooks(16)
  hubs     : useCompany, useBreadcrumbs, AppsConnect

~354 nodes · purity 0.19 across 53 packages
  packages : ui/src/components(69), ui/src/pages(60), packages/plugins(55), packages/adapters(30)
  hubs     : createTestHarness, firstNonEmptyLine, listIssueBlockerAttentionMap

~351 nodes · purity 0.14 across 62 packages
  packages : ui/src/lib(49), ui/src/components(35), packages/teams-catalog(30), ui/src/pages(28)
  hubs     : sort, teamsCatalogService, classifyTaskWatchdogSubtree

~349 nodes · purity 0.18 across 71 packages
  packages : packages/db(64), server/src/__tests__(20), server/src/index.ts(19), cli/src/commands(13)
  hubs     : startServer, createPluginJobScheduler, createDurableRunLogStore

~315 nodes · purity 0.59 across 31 packages
  packages : services/company-skills.ts(186), packages/adapter-utils(22), cli/src/install-store.ts(17), cli/src/commands(16)
  hubs     : companySkillService, dirname, normalizePortablePath

~262 nodes · purity 0.26 across 31 packages
  packages : services/secrets.ts(68), services/workspace-file-resources.ts(34), server/src/secrets(25), services/pipelines.ts(20)
  hubs     : unprocessable, secretService, workspaceFileResourceService

~224 nodes · purity 0.14 across 38 packages
  packages : server/src/__tests__(32), packages/adapter-utils(31), services/workspace-git-operation-scheduler.ts(25), packages/plugins(22)
  hubs     : UnixBrokerClient, listen, WorkspaceGitOperationScheduler

==========================================================================
DEPTH  (codebase-design: low conductance = deep module)
==========================================================================
  ~95 deep    — lots of behaviour, small seam. Good.
  ~2 shallow — as much crossing the seam as inside it.
      ~44 nodes, conductance 0.539 — decisionService
      ~33 nodes, conductance 0.538 — projectService

==========================================================================
READ THIS AS: a map of pressure, NOT a module manifest.
Stable: large high-conductance clusters and their hubs.
Unstable: exact counts and small-community boundaries.
==========================================================================
```

## Capability census (WHAT each module does)

Enumerated from the discovered modules, not from a guess at where things live.
**You cannot subtract a concept you never saw.**

| module | ~size | depth | hub | capabilities | inventory |
|---|---|---|---|---|---|
| `ui/src/components` | ~642 | deep | `replace` | 20 | `ransack-out/census/ui_src_components.md` |
| `packages/adapters` | ~397 | deep | `execute` | 25 | `ransack-out/census/packages_adapters.md` |
| `ui/src/pages` | ~370 | moderate | `useCompany` | 21 | `ransack-out/census/ui_src_pages.md` |
| `ui/src/lib` | ~351 | moderate | `sort` | 25 | `ransack-out/census/ui_src_lib.md` |
| `packages/db` | ~349 | moderate | `startServer` | 25 | `ransack-out/census/packages_db.md` |
| `cli/src/commands` | ~253 | deep | `action` | 25 | `ransack-out/census/cli_src_commands.md` |

Each inventory carries a KEEP/DROP ledger. A DROP row needs a concept in YOUR system it maps to nothing in.

## Artifacts

- `ransack-out/graph.json` — nodes, edges, community, stability
- `ransack-out/graph.html` — interactive, self-contained
- `ransack-out/GRAPH_REPORT.md` — god nodes, depth, drift
- `ransack-out/census/` — per-module capability inventories
- `ransack-out/INVENTORY.md` — families, packages, entrypoints

---

## Next

1. **Verify before trusting** — `ransack <repo> --verify`
   gives an LLM the checks to run against this pack.
2. **Census** — enumerate every capability before deciding anything.
3. **Ladder** — what does the platform or an installed dep already own?
4. **Subtract their domain** — concepts that map to nothing in your system.
5. **Keep 2-4 ideas**, write completion conditions, then build.

The test: *could you rewrite this without the original open?*
