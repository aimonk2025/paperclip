# Code graph report — paperclip-latest

**Deterministic export from the CodeGraph DB — no LLM.** Leiden via graphify.cluster; HTML via graphify's own renderer. Generated 2026-09-20T00:55:24. Spec: ransack references/code-graph-standard.md.

- nodes: **63,698**
- edges: **82,656**
  - calls: 90,274
  - references: 32,406
  - instantiates: 484
  - imports: 129
  - implements: 16
  - extends: 2
- communities: **1360**

## God nodes

| degree | symbol | kind | file |
|---|---|---|---|
| 1038 | `map` | constant | `scripts/release-registry-versions.mjs` |
| 1011 | `from` | property | `server/src/services/status-card-update-engine.ts` |
| 822 | `set` | method | `packages/kv-demo-mcp-server/src/store.ts` |
| 822 | `filter` | property | `packages/plugins/sdk/src/testing.ts` |
| 711 | `has` | method | `packages/kv-demo-mcp-server/src/store.ts` |
| 611 | `cn` | function | `ui/src/lib/utils.ts` |
| 593 | `api` | constant | `ui/src/api/client.ts` |
| 591 | `Partial` | constant | `ui/storybook/stories/decision-card.stories.tsx` |
| 545 | `Db` | type_alias | `server/src/__tests__/access-routes-permissions-upgrade.test.ts` |
| 528 | `insert` | method | `server/src/services/batch-insert.ts` |
| 452 | `Button` | function | `packages/plugins/plugin-llm-wiki/src/ui/app.tsx` |
| 403 | `update` | method | `ui/storybook/.storybook/node-crypto-browser-shim.ts` |
| 388 | `logActivity` | function | `server/src/services/activity-log.ts` |
| 381 | `replace` | function | `server/src/services/company-skill-policy.ts` |
| 355 | `add` | method | `server/src/services/environment-custom-image-terminal-sessions.ts` |
| 337 | `unprocessable` | function | `server/src/errors.ts` |
| 303 | `find` | function | `server/src/services/external-objects.ts` |
| 302 | `notFound` | function | `packages/plugins/sandbox-providers/kubernetes/test/unit/lease-lifecycle.test.ts` |
| 289 | `issueRoutes` | function | `server/src/routes/issues.ts` |
| 271 | `getActorInfo` | function | `server/src/routes/authz.ts` |
| 263 | `Issue` | interface | `packages/shared/src/types/issue.ts` |
| 261 | `assertCompanyAccess` | function | `server/src/routes/authz.ts` |
| 261 | `limit` | property | `server/src/services/company-search-rate-limit.ts` |
| 232 | `getById` | method | `server/src/services/environment-custom-image-terminal-sessions.ts` |
| 228 | `sql` | property | `packages/db/src/check-migration-safety.ts` |

## Communities (hub-labeled)

| id | ~size | label |
|---|---|---|
| 0 | ~1052 | logActivity |
| 1 | ~987 | Button |
| 2 | ~683 | from |
| 3 | ~562 | next |
| 4 | ~561 | has |
| 5 | ~545 | map |
| 6 | ~510 | Badge |
| 7 | ~500 | insert |
| 8 | ~484 | Db |
| 9 | ~424 | set |
| 10 | ~419 | unprocessable |
| 11 | ~404 | Navigate |
| 12 | ~369 | api |
| 13 | ~343 | StoryFrame |
| 14 | ~338 | cn |
| 15 | ~336 | Secrets |
| 16 | ~328 | Tooltip |
| 17 | ~286 | StatusCardDetailDrawer |
| 18 | ~286 | relativeTime |
| 19 | ~283 | Link |
| 20 | ~281 | Agent |
| 21 | ~269 | ToolProfileWithDetails |
| 22 | ~252 | set |
| 23 | ~247 | executeRun |
| 24 | ~238 | PluginContext |
| 25 | ~234 | secretService |
| 26 | ~231 | toolAccessService |
| 27 | ~216 | fn |
| 28 | ~216 | buildHostServices |
| 29 | ~207 | issueService |
