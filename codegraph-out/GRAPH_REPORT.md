# Code graph report

**Generated deterministically — no LLM.** `leiden` consensus over 3 seeds, resolution 2.5.

NMI across seeds: `[0.8552, 0.8639]` — a single run is ~85% reproducible, so **all counts below are approximate**.

- nodes: **39,067**
- edges: **120,842**
- communities: **~383**

## God nodes

| degree | symbol | file |
|---|---|---|
| 2089 | `from` | `server/src/services/status-card-update-engine.ts` |
| 1821 | `set` | `packages/kv-demo-mcp-server/src/store.ts` |
| 1613 | `map` | `scripts/release-registry-versions.mjs` |
| 1252 | `issueRoutes` | `server/src/routes/issues.ts` |
| 1191 | `cn` | `ui/src/lib/utils.ts` |
| 1128 | `insert` | `server/src/services/batch-insert.ts` |
| 1109 | `has` | `packages/kv-demo-mcp-server/src/store.ts` |
| 1097 | `filter` | `packages/plugins/sdk/src/testing.ts` |
| 878 | `update` | `ui/storybook/.storybook/node-crypto-browser-shim.ts` |
| 731 | `unprocessable` | `server/src/errors.ts` |
| 726 | `json` | `tests/e2e/mcp-user-stories.spec.ts` |
| 684 | `fn` | `packages/plugins/sdk/src/testing.ts` |
| 675 | `logActivity` | `server/src/services/activity-log.ts` |
| 635 | `agentRoutes` | `server/src/routes/agents.ts` |
| 624 | `Partial` | `ui/storybook/stories/decision-card.stories.tsx` |
| 597 | `api` | `ui/src/api/client.ts` |
| 566 | `add` | `server/src/services/environment-custom-image-terminal-sessions.ts` |
| 551 | `notFound` | `packages/plugins/sandbox-providers/kubernetes/test/unit/lease-lifecycle.test.ts` |
| 550 | `sql` | `packages/db/src/check-migration-safety.ts` |
| 550 | `Db` | `server/src/__tests__/access-routes-permissions-upgrade.test.ts` |

## Communities

| ~size | depth | conductance | stability | hubs |
|---|---|---|---|---|
| ~1655 | moderate | 0.456 | 0.888 | `Button`, `Badge`, `IssueProperties`, `Link` |
| ~1192 | shallow | 0.53 | 0.613 | `issueService`, `environmentService`, `companySearchService`, `costService` |
| ~1168 | moderate | 0.321 | 0.334 | `issueRoutes`, `logActivity`, `agentRoutes`, `getActorInfo` |
| ~1162 | moderate | 0.433 | 0.333 | `Partial`, `Issue`, `Agent`, `IssueDetailChatTabProps` |
| ~1153 | moderate | 0.454 | 0.333 | `IssueDetail`, `Inbox`, `IssuesList`, `detail` |
| ~917 | shallow | 0.551 | 0.335 | `buildWorktreeMergePlan`, `useLiveRunTranscripts`, `listIssueBlockerAttentionMap`, `getTimeline` |
| ~863 | deep | 0.176 | 0.333 | `parseObject`, `execute`, `execute`, `asString` |
| ~844 | deep | 0.163 | 0.333 | `runDatabaseBackup`, `onboard`, `PaperclipConfig`, `runCommand` |
| ~840 | deep | 0.218 | 0.333 | `TooltipProvider`, `expectForwardBranchReconciled`, `ToastProvider`, `expectContainedWorkspaceBranchFailure` |
| ~719 | deep | 0.178 | 0.333 | `createHostClientHandlers`, `PluginContext`, `gated`, `registerActionHandlers` |
| ~718 | moderate | 0.35 | 0.333 | `executeRun`, `readNonEmptyString`, `heartbeatService`, `parseObject` |
| ~711 | moderate | 0.455 | 0.334 | `Input`, `DialogContent`, `Dialog`, `DialogTitle` |
| ~707 | moderate | 0.352 | 0.333 | `decisionQueueRoutes`, `assertDecisionAccess`, `agentPath`, `IssueListFilters` |
| ~706 | moderate | 0.438 | 0.463 | `useCompany`, `useBreadcrumbs`, `AppDetail`, `AppsConnect` |
| ~698 | moderate | 0.447 | 0.333 | `unprocessable`, `secretService`, `pipelineService`, `createAwsSecretsManagerProvider` |
| ~672 | moderate | 0.309 | 0.338 | `shellQuote`, `destroy`, `startAdapterExecutionTargetProcessSessionBridge`, `listen` |
| ~664 | shallow | 0.738 | 0.334 | `RoutineVariable`, `classifyTaskWatchdogSubtree`, `CreateConfigValues`, `AskUserQuestionsCard` |
| ~604 | deep | 0.156 | 0.333 | `SettingsBody`, `usePluginAction`, `KitchenSinkConsole`, `WikiRouteSidebar` |
| ~594 | moderate | 0.344 | 0.333 | `fileResourceRoutes`, `setupEnvironmentCustomImageTerminalWebSocketServer`, `SetupTokenSessionService`, `WorkspaceGitOperationScheduler` |
| ~589 | shallow | 0.641 | 0.333 | `createTestHarness`, `requireCapability`, `budgetService`, `pluginRegistryService` |
| ~580 | shallow | 0.556 | 0.333 | `notFound`, `accessRoutes`, `conflict`, `routineService` |
| ~558 | moderate | 0.268 | 0.333 | `spawnLocalRuntimeService`, `asString`, `ensurePersistedExecutionWorkspaceAvailable`, `ensureGitWorktreeBranchCoherent` |
| ~537 | moderate | 0.431 | 0.333 | `decisionQueueService`, `instanceSettingsService`, `applyMergePlan`, `seedLowTrustFixture` |
| ~512 | deep | 0.144 | 0.664 | `registerRouteMocks`, `createMockSandbox`, `registerRouteMocks`, `registerServiceMocks` |
| ~510 | moderate | 0.418 | 0.333 | `replace`, `analyzeMigrationSafety`, `parseOptionalString`, `parseDriverConfig` |

## Shallow modules — as much crossing the seam as inside it

- **`issueService`** — ~1192 nodes, conductance 0.53
- **`buildWorktreeMergePlan`** — ~917 nodes, conductance 0.551
- **`RoutineVariable`** — ~664 nodes, conductance 0.738
- **`createTestHarness`** — ~589 nodes, conductance 0.641
- **`notFound`** — ~580 nodes, conductance 0.556
- **`readNonEmptyString`** — ~264 nodes, conductance 0.536

## Intent vs reality

Behaviour that spans several packages — the seam may be misplaced.

- ~1655 nodes, purity 0.58 across 19 packages — hubs: `Button`, `Badge`, `IssueProperties`
- ~1192 nodes, purity 0.19 across 98 packages — hubs: `issueService`, `environmentService`, `companySearchService`
- ~1162 nodes, purity 0.28 across 26 packages — hubs: `Partial`, `Issue`, `Agent`
- ~1153 nodes, purity 0.33 across 20 packages — hubs: `IssueDetail`, `Inbox`, `IssuesList`
- ~917 nodes, purity 0.19 across 68 packages — hubs: `buildWorktreeMergePlan`, `useLiveRunTranscripts`, `listIssueBlockerAttentionMap`
- ~844 nodes, purity 0.53 across 25 packages — hubs: `runDatabaseBackup`, `onboard`, `PaperclipConfig`
- ~840 nodes, purity 0.39 across 49 packages — hubs: `TooltipProvider`, `expectForwardBranchReconciled`, `ToastProvider`
- ~711 nodes, purity 0.5 across 15 packages — hubs: `Input`, `DialogContent`, `Dialog`
- ~706 nodes, purity 0.19 across 34 packages — hubs: `useCompany`, `useBreadcrumbs`, `AppDetail`
- ~698 nodes, purity 0.24 across 33 packages — hubs: `unprocessable`, `secretService`, `pipelineService`

---

**Read this as a map of pressure, not a module manifest.** Stable: large clusters, their hubs, conductance. Unstable: exact counts and small-community boundaries.