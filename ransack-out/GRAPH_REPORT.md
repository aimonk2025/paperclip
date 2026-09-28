# Code graph report

**Generated deterministically — no LLM.** `leiden` consensus over 5 seeds, resolution 2.5.

NMI across seeds: `[0.9357, 0.9208, 0.931, 0.9413]` — a single run is ~92% reproducible, so **all counts below are approximate**.

- nodes: **11,635**
- edges: **31,890**
- communities: **~238**

## God nodes

| degree | symbol | file |
|---|---|---|
| 1777 | `select` | `ui/src/components/folders/FolderControls.tsx` |
| 1064 | `replace` | `server/src/services/company-skill-policy.ts` |
| 738 | `find` | `server/src/services/external-objects.ts` |
| 683 | `unprocessable` | `server/src/errors.ts` |
| 604 | `companySkillService` | `server/src/services/company-skills.ts` |
| 525 | `sort` | `ui/src/pages/TeamCatalog.tsx` |
| 433 | `secretService` | `server/src/services/secrets.ts` |
| 430 | `issueService` | `server/src/services/issues.ts` |
| 415 | `setTimeout` | `scripts/smoke/mcp-fixture-harness.mjs` |
| 348 | `action` | `server/src/services/workspace-operations.ts` |
| 347 | `printOutput` | `cli/src/commands/client/common.ts` |
| 339 | `parseYamlScalar` | `server/src/services/company-portability.ts` |
| 299 | `resolveCommandContext` | `cli/src/commands/client/common.ts` |
| 297 | `handleCommandError` | `cli/src/commands/client/common.ts` |
| 293 | `addCommonClientOptions` | `cli/src/commands/client/common.ts` |
| 288 | `registerIssueCommands` | `cli/src/commands/client/issue.ts` |
| 276 | `executeRun` | `server/src/services/heartbeat.ts` |
| 268 | `startWorkerRpcHost` | `packages/plugins/sdk/src/worker-rpc-host.ts` |
| 262 | `limit` | `server/src/services/tool-gateway.ts` |
| 259 | `warn` | `packages/shared/src/telemetry/client.ts` |

## Communities

| ~size | depth | conductance | stability | hubs |
|---|---|---|---|---|
| ~642 | deep | 0.246 | 0.582 | `replace`, `rewriteFile`, `formatClaudeCliDetail`, `code` |
| ~631 | moderate | 0.431 | 0.543 | `issueService`, `count`, `environmentService`, `accessService` |
| ~397 | deep | 0.107 | 0.2 | `execute`, `execute`, `execute`, `execute` |
| ~377 | moderate | 0.258 | 0.201 | `setTimeout`, `useHeldSelfTalk`, `scrollToLatestCommentWithSettle`, `check` |
| ~370 | moderate | 0.288 | 0.203 | `useCompany`, `useBreadcrumbs`, `AppsConnect`, `Layout` |
| ~354 | moderate | 0.476 | 0.2 | `createTestHarness`, `firstNonEmptyLine`, `listIssueBlockerAttentionMap`, `isInCompany` |
| ~351 | moderate | 0.412 | 0.579 | `sort`, `teamsCatalogService`, `classifyTaskWatchdogSubtree`, `buildCatalogTeam` |
| ~349 | moderate | 0.361 | 0.514 | `startServer`, `createPluginJobScheduler`, `createDurableRunLogStore`, `reconcilePendingMigrationHistory` |
| ~315 | moderate | 0.336 | 0.2 | `companySkillService`, `dirname`, `normalizePortablePath`, `auditInstalledSkillBytes` |
| ~293 | deep | 0.227 | 0.77 | `executeRun`, `redactCurrentUserText`, `appendRunEvent`, `claimQueuedRun` |
| ~271 | moderate | 0.269 | 0.579 | `IssueDetail`, `Inbox`, `handleKeyDown`, `runs` |
| ~262 | moderate | 0.442 | 0.393 | `unprocessable`, `secretService`, `workspaceFileResourceService`, `HttpError` |
| ~253 | deep | 0.033 | 0.6 | `action`, `printOutput`, `resolveCommandContext`, `handleCommandError` |
| ~224 | deep | 0.235 | 0.205 | `UnixBrokerClient`, `listen`, `WorkspaceGitOperationScheduler`, `destroy` |
| ~216 | moderate | 0.313 | 0.366 | `exit`, `onboard`, `confirm`, `require` |
| ~214 | moderate | 0.357 | 0.2 | `AgentConfigForm`, `NewIssueDialog`, `mark`, `BoardChat` |
| ~195 | moderate | 0.328 | 0.2 | `parseYamlScalar`, `companyPortabilityService`, `exportBundle`, `importBundle` |
| ~188 | moderate | 0.396 | 0.2 | `forbidden`, `summarySlotService`, `toolGatewayRoutes`, `builtInAgentRoutes` |
| ~184 | deep | 0.205 | 0.2 | `spawnLocalRuntimeService`, `handleExecutionWorkspaceRuntimeCommand`, `reconcilePersistedRuntimeServicesOnStartup`, `startRuntimeServicesForWorkspaceControlInvocation` |
| ~179 | moderate | 0.308 | 0.578 | `digest`, `execute`, `pluginDatabaseService`, `resolveCloudTenantActor` |
| ~177 | moderate | 0.271 | 0.2 | `PipelineSettings`, `focus`, `Routines`, `RoutineDetail` |
| ~173 | moderate | 0.402 | 0.244 | `companySkillRoutes`, `logActivity`, `validate`, `projectRoutes` |
| ~151 | deep | 0.169 | 0.588 | `register`, `registerWikiTools`, `registerActionHandlers`, `distillPaperclipProjectPage` |
| ~148 | deep | 0.229 | 0.2 | `getItem`, `WhatNeedsMe`, `DecisionQueuePage`, `TweakPanel` |
| ~134 | moderate | 0.297 | 0.2 | `createPluginWorkerHandle`, `setStatus`, `setAttribute`, `callInternal` |

## Shallow modules — as much crossing the seam as inside it

- **`decisionService`** — ~44 nodes, conductance 0.539
- **`projectService`** — ~33 nodes, conductance 0.538

## Intent vs reality

Behaviour that spans several packages — the seam may be misplaced.

- ~642 nodes, purity 0.12 across 85 packages — hubs: `replace`, `rewriteFile`, `formatClaudeCliDetail`
- ~631 nodes, purity 0.18 across 92 packages — hubs: `issueService`, `count`, `environmentService`
- ~377 nodes, purity 0.32 across 42 packages — hubs: `setTimeout`, `useHeldSelfTalk`, `scrollToLatestCommentWithSettle`
- ~370 nodes, purity 0.36 across 31 packages — hubs: `useCompany`, `useBreadcrumbs`, `AppsConnect`
- ~354 nodes, purity 0.19 across 53 packages — hubs: `createTestHarness`, `firstNonEmptyLine`, `listIssueBlockerAttentionMap`
- ~351 nodes, purity 0.14 across 62 packages — hubs: `sort`, `teamsCatalogService`, `classifyTaskWatchdogSubtree`
- ~349 nodes, purity 0.18 across 71 packages — hubs: `startServer`, `createPluginJobScheduler`, `createDurableRunLogStore`
- ~315 nodes, purity 0.59 across 31 packages — hubs: `companySkillService`, `dirname`, `normalizePortablePath`
- ~262 nodes, purity 0.26 across 31 packages — hubs: `unprocessable`, `secretService`, `workspaceFileResourceService`
- ~224 nodes, purity 0.14 across 38 packages — hubs: `UnixBrokerClient`, `listen`, `WorkspaceGitOperationScheduler`

---

**Read this as a map of pressure, not a module manifest.** Stable: large clusters, their hubs, conductance. Unstable: exact counts and small-community boundaries.