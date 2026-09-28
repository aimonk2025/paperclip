# Capability census — plugins

**125 files · 39,258 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 48 |
| enforces a timeout | 31 |
| validates input | 19 |
| caches | 18 |
| writes to disk | 16 |
| captures a session id | 15 |
| retries | 13 |
| handles cancellation | 12 |
| reads from disk | 10 |
| spawns a process | 10 |
| reads config | 9 |
| emits telemetry | 9 |
| buffers partial lines | 8 |
| streams incrementally | 8 |
| parses JSON events | 7 |
| classifies errors | 3 |
| tracks token usage | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `plugin-llm-wiki/src/wiki/core.ts` | 4980 | DEFAULT_WIKI_ID, DEFAULT_SPACE_SLUG, OPERATION_ORIGIN_KIND, PUBLIC_DISTILLATION_AUTO_APPLY_RESTRICTION, WikiEventIngestionSource +81 |
| `sdk/src/testing.ts` | 2773 | TestHarnessOptions, TestHarnessLogEntry, TestHarnessPerformActionOptions, TestHarness, EnvironmentEventRecord +12 |
| `sandbox-providers/daytona/src/plugin.ts` | 2750 | getPluginTracer, __setDaytonaPluginContextForTest, setDaytonaTimingClockForTest, setDaytonaHandleFreshnessClockForTest, __resetDaytonaSandboxHandleCacheForTest +1 |
| `sdk/src/protocol.ts` | 2393 | JSONRPC_VERSION, JsonRpcId, JsonRpcInvocationScope, JsonRpcInvocationContext, JsonRpcRequest +111 |
| `sdk/src/worker-rpc-host.ts` | 2260 | WorkerRpcHostOptions, WorkerRpcHost, isWorkerEntrypoint, RunWorkerOptions, runWorker +1 |
| `sdk/src/types.ts` | 2175 | ScopeKey, EventFilter, PluginEvent, PluginJobContext, ToolRunContext +81 |
| `sdk/src/host-client-factory.ts` | 1091 | CapabilityDeniedError, InvocationScopeDeniedError, HostServices, HostClientFactoryOptions, HostClientHandlers +2 |
| `plugin-llm-wiki/src/worker.ts` | 1081 | — |
| `examples/plugin-kitchen-sink-example/src/worker.ts` | 1062 | — |
| `sandbox-providers/kubernetes/src/plugin.ts` | 1036 | — |
| `sandbox-providers/daytona/src/file-sync.ts` | 1019 | withProviderSpan, assertConfinedSandboxPath, parseTarVerboseListingLine, splitLinkEntryOnce, performSyncIn +1 |
| `sandbox-providers/exe-dev/src/plugin.ts` | 964 | validateSshPrivateKey |
| `sandbox-providers/kubernetes/src/file-sync.ts` | 917 | PodStreamExec, assertConfinedSandboxPath, parseTarVerboseListingLine, splitLinkEntryOnce, performSyncIn +1 |
| `plugin-workspace-diff/src/workspace-diff.ts` | 845 | WORKSPACE_DIFF_CAPS, workspaceDiffService |
| `create-paperclip-plugin/src/index.ts` | 700 | ScaffoldPluginOptions, isValidPluginName, shellQuote, scaffoldPluginProject, DashboardWidget +1 |
| `sandbox-providers/modal/src/plugin.ts` | 660 | parseDriverConfig |
| `plugin-llm-wiki/src/manifest.ts` | 601 | PLUGIN_ID, WIKI_ROOT_FOLDER_KEY, WIKI_MAINTAINER_AGENT_KEY, WIKI_MAINTAINER_SKILL_KEY, WIKI_INGEST_SKILL_KEY +17 |
| `sdk/src/ui/components.ts` | 597 | MetricTrend, MetricCardProps, StatusBadgeVariant, StatusBadgeProps, DataTableColumn +50 |
| `sdk/src/define-plugin.ts` | 522 | PluginHealthDiagnostics, PluginConfigValidationResult, PluginWebhookInput, PluginApiRequestInput, PluginApiResponse +4 |
| `paperclip-plugin-fake-sandbox/src/plugin.ts` | 500 | — |
| `sandbox-providers/novita/src/plugin.ts` | 492 | NovitaDriverConfig, parseNovitaDriverConfig, buildShellCommand |
| `sdk/src/ui/types.ts` | 488 | PluginBridgeError, PluginHostContext, PluginRenderCloseHandler, PluginRenderCloseLifecycle, PluginRenderEnvironmentContext +22 |
| `sandbox-providers/cloudflare/bridge-template/src/routes.ts` | 480 | handleBridgeRequest |
| `sandbox-providers/e2b/src/plugin.ts` | 474 | — |
| `sandbox-providers/kubernetes/src/pod-exec.ts` | 444 | shQuote, wrapCommandWithEnv, execInPod, execInPodStreaming |

## Contract members — each is a capability

**WorkerToHostMethods** (385 members)

```
params, result, params, companyId, folderKey, path, access, requiredDirectories, requiredFiles, result, params, result, params, result, params, result, params, companyId, folderKey, relativePath, contents, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, entityType, scopeKind, scopeId, externalId, title, status, data, result, id, entityType, scopeKind, scopeId, externalId, title, status, data, createdAt, updatedAt, params, entityType, scopeKind, scopeId, externalId, limit, offset, result, id, entityType, scopeKind, scopeId, externalId, title, status, data, createdAt, updatedAt, params, result, params, result, params, result, params, result, params, companyId, message, entityType, entityId, metadata, result, params, name, value, tags, companyId, result, params, result, params, level, message, meta, companyId, result, params, name, attributes, status, startTimeMs, endTimeMs, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, workspaceId, companyId, result, params, result, params, result, params, result, params, result, params, routineKey, companyId, assigneeAgentId, projectId, result, params, routineKey, companyId, assigneeAgentId, projectId, result, params, routineKey, companyId, status, result, params, routineKey, companyId, assigneeAgentId, projectId, result, params, result, params, result, params, result, params, companyId, projectId, assigneeAgentId, originKind, originKindPrefix, originId, status, includePluginOperations, limit, offset, result, params, result, params, companyId, projectId, goalId, parentId, inheritExecutionWorkspaceFromIssueId, title, description, status, priority, assigneeAgentId, assigneeUserId, requestDepth, billingCode, assigneeAdapterOverrides, surfaceVisibility, originKind, originId, originRunId, blockedByIssueIds, labelIds, executionWorkspaceId, executionWorkspacePreference, executionWorkspaceSettings, actorAgentId, actorUserId, actorRunId, result, params, issueId, patch, companyId, result, params, result, params, issueId, companyId, blockedByIssueIds, actorAgentId, actorUserId, actorRunId, result, params, issueId, companyId, blockerIssueIds, actorAgentId, actorUserId, actorRunId, result, params, issueId, companyId, blockerIssueIds, actorAgentId, actorUserId, actorRunId, result, params, issueId, companyId, actorAgentId, actorRunId, result, params, issueId, companyId, includeRoot, includeRelations, includeDocuments, includeActiveRuns, includeAssignees, result, params, issueId, companyId, reason, contextSource, idempotencyKey, actorAgentId, actorUserId, actorRunId, result, params, issueIds, companyId, reason, contextSource, idempotencyKeyPrefix, actorAgentId, actorUserId, actorRunId, result, params, issueId, companyId, includeSubtree, billingCode, result, params, result, params, issueId, body, companyId, authorAgentId, actorUserId, result, params, issueId, companyId, interaction, authorAgentId, result, params, result, params, issueId, interactionId, companyId, action, actorUserId, reason, result, params, result, params, result, params, result, params, result, params, issueId, key, body, companyId, title, format, changeSummary, result, params, result, params, result, params, result, params, approvalId, companyId, action, actorUserId, decisionNote, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, result, params, companyId, title, description, level, status, parentId, ownerAgentId, result, params, goalId, patch, companyId, result, params, result, params, result, params, memberId, companyId, patch, membershipRole, status
```

**PluginIssuesClient** (113 members)

```
list, companyId, projectId, assigneeAgentId, originKind, originKindPrefix, originId, status, includePluginOperations, limit, offset, get, create, companyId, projectId, goalId, parentId, inheritExecutionWorkspaceFromIssueId, title, description, status, priority, assigneeAgentId, assigneeUserId, requestDepth, billingCode, assigneeAdapterOverrides, surfaceVisibility, originKind, originId, originRunId, blockedByIssueIds, labelIds, executionWorkspaceId, executionWorkspacePreference, executionWorkspaceSettings, actor, update, issueId, patch, blockedByIssueIds, labelIds, executionWorkspaceSettings, companyId, actor, assertCheckoutOwner, issueId, companyId, actorAgentId, actorRunId, getSubtree, issueId, companyId, options, requestWakeup, issueId, companyId, options, reason, contextSource, idempotencyKey, requestWakeups, issueIds, companyId, options, reason, contextSource, idempotencyKeyPrefix, listComments, createComment, issueId, body, companyId, options, createInteraction, issueId, interaction, companyId, options, suggestTasks, issueId, interaction, companyId, options, askUserQuestions, issueId, interaction, companyId, options, requestConfirmation, issueId, interaction, companyId, options, requestCheckboxConfirmation, issueId, interaction, companyId, options, listInteractions, respondInteraction, issueId, interactionId, input, companyId, listAttachments, getAttachmentContent, attachmentId, companyId, options, documents, relations, summaries
```

**HostToWorkerMethods** (74 members)

```
initialize, health, shutdown, validateConfig, configChanged, onEvent, runJob, handleWebhook, handleApiRequest, getData, performAction, executeTool, detectExternalObjects, params, result, resolveExternalObject, params, result, refreshExternalObjects, params, result, environmentValidateConfig, params, result, environmentProbe, params, result, environmentAcquireLease, params, result, environmentResumeLease, params, result, environmentReleaseLease, params, result, environmentDestroyLease, params, result, environmentRealizeWorkspace, params, result, environmentExecute, params, result, environmentSyncIn, params, result, environmentSyncOut, params, result, environmentStartInteractiveSetup, params, result, environmentGetInteractiveSetup, params, result, environmentCaptureTemplate, params, result, environmentCancelInteractiveSetup, params, result, environmentDeleteTemplate, params, result, setupTokenPtyOpen, params, result, setupTokenPtyInput, setupTokenPtyStop, setupTokenPtyClose, params, result
```

**PluginDefinition** (52 members)

```
setup, onHealth, multiCompanyConfig, onConfigChanged, newConfig, context, onShutdown, onValidateConfig, onWebhook, onApiRequest, onDetectExternalObjects, params, onResolveExternalObject, params, onRefreshExternalObjects, params, onEnvironmentValidateConfig, params, onEnvironmentProbe, params, onEnvironmentAcquireLease, params, onEnvironmentResumeLease, params, onEnvironmentReleaseLease, params, onEnvironmentDestroyLease, params, onEnvironmentRealizeWorkspace, params, onEnvironmentExecute, params, onEnvironmentSyncIn, params, onEnvironmentSyncOut, params, onEnvironmentStartInteractiveSetup, params, onEnvironmentGetInteractiveSetup, params, onEnvironmentCaptureTemplate, params, onEnvironmentCancelInteractiveSetup, params, onEnvironmentDeleteTemplate, params, onSetupTokenPtyOpen, params, onSetupTokenPtyInput, onSetupTokenPtyStop, onSetupTokenPtyClose, params
```

**PluginContext** (33 members)

```
manifest, config, localFolders, events, jobs, launchers, db, http, secrets, activity, state, entities, projects, executionWorkspaces, routines, skills, companies, issues, approvals, agents, goals, access, authorization, data, actions, streams, execution, setupTokenPty, tools, metrics, telemetry, logger, tracer
```

**TestHarness** (29 members)

```
ctx, seed, companies, projects, issues, issueComments, issueInteractions, issueAttachments, approvals, agents, goals, projectWorkspaces, executionWorkspaces, accessMembers, principalGrants, setConfig, emit, runJob, key, params, options, getState, simulateSessionEvent, logs, activity, metrics, telemetry, dbQueries, dbExecutes
```

**SandboxOrchestrator** (25 members)

```
claim, clients, namespace, manifest, getStatus, clients, namespace, name, findPod, clients, namespace, name, streamLogs, clients, namespace, podName, onChunk, release, waitForCompletion, clients, namespace, name, opts, pause, resume
```

**DistillationRunRow** (21 members)

```
id, cursorId, workItemId, projectId, projectName, rootIssueId, rootIssueIdentifier, sourceWindowStart, sourceWindowEnd, sourceHash, status, costCents, retryCount, warnings, metadata, operationIssueId, operationIssueIdentifier, operationIssueTitle, affectedPagePaths, createdAt, updatedAt
```

## Case sets — each arm is a case you must handle or drop

- **EnvironmentEventRecord** (13): validateConfig, probe, acquireLease, resumeLease, releaseLease, destroyLease, realizeWorkspace, execute, startInteractiveSetup, getInteractiveSetup, captureTemplate, cancelInteractiveSetup, deleteTemplate
- **PluginIssuesClient** (13): title, description, status, priority, assigneeAgentId, assigneeUserId, billingCode, originKind, originId, originRunId, requestDepth, executionWorkspaceId, executionWorkspacePreference
- **PluginLocalFolderProblem** (11): not_configured, not_absolute, missing, not_directory, not_readable, not_writable, missing_directory, missing_file, path_traversal, symlink_escape, atomic_write_failed
- **PluginEnvironmentInteractiveSetupStatus** (8): starting, waiting_for_user, capturing, promoted, cancelled, timed_out, failed, missing
- **PluginRenderCloseEvent** (6): escapeKey, backdrop, hostNavigation, programmatic, submit, unknown
- **PaperclipIngestionProfileEffectiveState** (5): enabled, disabled, policy_blocked, pending_approval, enabled_no_scopes
- **PluginEnvironmentTemplateRefKind** (4): snapshot, image, provider_template, unknown
- **PluginEnvironmentInteractiveSetupConnectionType** (1): ssh

## Structural duplication — the reduction lever

Identical logic across N files. This is where a rebuild gets smaller
WITHOUT losing features — unlike dropping capabilities.

| Repeated in | Shape |
|---|---|
| **8 files** | `categories: ["automation"], capabilities: ["environment.drivers.regist…` |
| **7 files** | `ctx.logger.info("T sandbox provider plugin ready"); }, async onHealth(…` |
| **7 files** | `}, async onHealth() { return { status: "ok", message: "T sandbox provi…` |
| **7 files** | `async onHealth() { return { status: "ok", message: "T sandbox provider…` |
| **7 files** | `author: "T", categories: ["automation"], capabilities: ["environment.d…` |
| **6 files** | `import { defineConfig } from "vitest/config"; export default defineCon…` |

## Decision ledger — fill this in, leave nothing blank

| Capability | KEEP / DROP | Reason |
|---|---|---|
| authenticates | | |
| buffers partial lines | | |
| caches | | |
| captures a session id | | |
| classifies errors | | |
| emits telemetry | | |
| enforces a timeout | | |
| handles cancellation | | |
| parses JSON events | | |
| reads config | | |
| reads from disk | | |
| retries | | |
| spawns a process | | |
| streams incrementally | | |
| tracks token usage | | |
| validates input | | |
| writes to disk | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.folderKey | | |
| WorkerToHostMethods.path | | |
| WorkerToHostMethods.access | | |
| WorkerToHostMethods.requiredDirectories | | |
| WorkerToHostMethods.requiredFiles | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.folderKey | | |
| WorkerToHostMethods.relativePath | | |
| WorkerToHostMethods.contents | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.entityType | | |
| WorkerToHostMethods.scopeKind | | |
| WorkerToHostMethods.scopeId | | |
| WorkerToHostMethods.externalId | | |
| WorkerToHostMethods.title | | |
| WorkerToHostMethods.status | | |
| WorkerToHostMethods.data | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.id | | |
| WorkerToHostMethods.entityType | | |
| WorkerToHostMethods.scopeKind | | |
| WorkerToHostMethods.scopeId | | |
| WorkerToHostMethods.externalId | | |
| WorkerToHostMethods.title | | |
| WorkerToHostMethods.status | | |
| WorkerToHostMethods.data | | |
| WorkerToHostMethods.createdAt | | |
| WorkerToHostMethods.updatedAt | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.entityType | | |
| WorkerToHostMethods.scopeKind | | |
| WorkerToHostMethods.scopeId | | |
| WorkerToHostMethods.externalId | | |
| WorkerToHostMethods.limit | | |
| WorkerToHostMethods.offset | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.id | | |
| WorkerToHostMethods.entityType | | |
| WorkerToHostMethods.scopeKind | | |
| WorkerToHostMethods.scopeId | | |
| WorkerToHostMethods.externalId | | |
| WorkerToHostMethods.title | | |
| WorkerToHostMethods.status | | |
| WorkerToHostMethods.data | | |
| WorkerToHostMethods.createdAt | | |
| WorkerToHostMethods.updatedAt | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.message | | |
| WorkerToHostMethods.entityType | | |
| WorkerToHostMethods.entityId | | |
| WorkerToHostMethods.metadata | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.name | | |
| WorkerToHostMethods.value | | |
| WorkerToHostMethods.tags | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.level | | |
| WorkerToHostMethods.message | | |
| WorkerToHostMethods.meta | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.name | | |
| WorkerToHostMethods.attributes | | |
| WorkerToHostMethods.status | | |
| WorkerToHostMethods.startTimeMs | | |
| WorkerToHostMethods.endTimeMs | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.workspaceId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.routineKey | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.assigneeAgentId | | |
| WorkerToHostMethods.projectId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.routineKey | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.assigneeAgentId | | |
| WorkerToHostMethods.projectId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.routineKey | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.status | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.routineKey | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.assigneeAgentId | | |
| WorkerToHostMethods.projectId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.projectId | | |
| WorkerToHostMethods.assigneeAgentId | | |
| WorkerToHostMethods.originKind | | |
| WorkerToHostMethods.originKindPrefix | | |
| WorkerToHostMethods.originId | | |
| WorkerToHostMethods.status | | |
| WorkerToHostMethods.includePluginOperations | | |
| WorkerToHostMethods.limit | | |
| WorkerToHostMethods.offset | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.projectId | | |
| WorkerToHostMethods.goalId | | |
| WorkerToHostMethods.parentId | | |
| WorkerToHostMethods.inheritExecutionWorkspaceFromIssueId | | |
| WorkerToHostMethods.title | | |
| WorkerToHostMethods.description | | |
| WorkerToHostMethods.status | | |
| WorkerToHostMethods.priority | | |
| WorkerToHostMethods.assigneeAgentId | | |
| WorkerToHostMethods.assigneeUserId | | |
| WorkerToHostMethods.requestDepth | | |
| WorkerToHostMethods.billingCode | | |
| WorkerToHostMethods.assigneeAdapterOverrides | | |
| WorkerToHostMethods.surfaceVisibility | | |
| WorkerToHostMethods.originKind | | |
| WorkerToHostMethods.originId | | |
| WorkerToHostMethods.originRunId | | |
| WorkerToHostMethods.blockedByIssueIds | | |
| WorkerToHostMethods.labelIds | | |
| WorkerToHostMethods.executionWorkspaceId | | |
| WorkerToHostMethods.executionWorkspacePreference | | |
| WorkerToHostMethods.executionWorkspaceSettings | | |
| WorkerToHostMethods.actorAgentId | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.actorRunId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.patch | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.blockedByIssueIds | | |
| WorkerToHostMethods.actorAgentId | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.actorRunId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.blockerIssueIds | | |
| WorkerToHostMethods.actorAgentId | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.actorRunId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.blockerIssueIds | | |
| WorkerToHostMethods.actorAgentId | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.actorRunId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.actorAgentId | | |
| WorkerToHostMethods.actorRunId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.includeRoot | | |
| WorkerToHostMethods.includeRelations | | |
| WorkerToHostMethods.includeDocuments | | |
| WorkerToHostMethods.includeActiveRuns | | |
| WorkerToHostMethods.includeAssignees | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.reason | | |
| WorkerToHostMethods.contextSource | | |
| WorkerToHostMethods.idempotencyKey | | |
| WorkerToHostMethods.actorAgentId | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.actorRunId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueIds | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.reason | | |
| WorkerToHostMethods.contextSource | | |
| WorkerToHostMethods.idempotencyKeyPrefix | | |
| WorkerToHostMethods.actorAgentId | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.actorRunId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.includeSubtree | | |
| WorkerToHostMethods.billingCode | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.body | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.authorAgentId | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.interaction | | |
| WorkerToHostMethods.authorAgentId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.interactionId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.action | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.reason | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.issueId | | |
| WorkerToHostMethods.key | | |
| WorkerToHostMethods.body | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.title | | |
| WorkerToHostMethods.format | | |
| WorkerToHostMethods.changeSummary | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.approvalId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.action | | |
| WorkerToHostMethods.actorUserId | | |
| WorkerToHostMethods.decisionNote | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.title | | |
| WorkerToHostMethods.description | | |
| WorkerToHostMethods.level | | |
| WorkerToHostMethods.status | | |
| WorkerToHostMethods.parentId | | |
| WorkerToHostMethods.ownerAgentId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.goalId | | |
| WorkerToHostMethods.patch | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.result | | |
| WorkerToHostMethods.params | | |
| WorkerToHostMethods.memberId | | |
| WorkerToHostMethods.companyId | | |
| WorkerToHostMethods.patch | | |
| WorkerToHostMethods.membershipRole | | |
| WorkerToHostMethods.status | | |
| PluginIssuesClient.list | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.projectId | | |
| PluginIssuesClient.assigneeAgentId | | |
| PluginIssuesClient.originKind | | |
| PluginIssuesClient.originKindPrefix | | |
| PluginIssuesClient.originId | | |
| PluginIssuesClient.status | | |
| PluginIssuesClient.includePluginOperations | | |
| PluginIssuesClient.limit | | |
| PluginIssuesClient.offset | | |
| PluginIssuesClient.get | | |
| PluginIssuesClient.create | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.projectId | | |
| PluginIssuesClient.goalId | | |
| PluginIssuesClient.parentId | | |
| PluginIssuesClient.inheritExecutionWorkspaceFromIssueId | | |
| PluginIssuesClient.title | | |
| PluginIssuesClient.description | | |
| PluginIssuesClient.status | | |
| PluginIssuesClient.priority | | |
| PluginIssuesClient.assigneeAgentId | | |
| PluginIssuesClient.assigneeUserId | | |
| PluginIssuesClient.requestDepth | | |
| PluginIssuesClient.billingCode | | |
| PluginIssuesClient.assigneeAdapterOverrides | | |
| PluginIssuesClient.surfaceVisibility | | |
| PluginIssuesClient.originKind | | |
| PluginIssuesClient.originId | | |
| PluginIssuesClient.originRunId | | |
| PluginIssuesClient.blockedByIssueIds | | |
| PluginIssuesClient.labelIds | | |
| PluginIssuesClient.executionWorkspaceId | | |
| PluginIssuesClient.executionWorkspacePreference | | |
| PluginIssuesClient.executionWorkspaceSettings | | |
| PluginIssuesClient.actor | | |
| PluginIssuesClient.update | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.patch | | |
| PluginIssuesClient.blockedByIssueIds | | |
| PluginIssuesClient.labelIds | | |
| PluginIssuesClient.executionWorkspaceSettings | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.actor | | |
| PluginIssuesClient.assertCheckoutOwner | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.actorAgentId | | |
| PluginIssuesClient.actorRunId | | |
| PluginIssuesClient.getSubtree | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.requestWakeup | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.reason | | |
| PluginIssuesClient.contextSource | | |
| PluginIssuesClient.idempotencyKey | | |
| PluginIssuesClient.requestWakeups | | |
| PluginIssuesClient.issueIds | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.reason | | |
| PluginIssuesClient.contextSource | | |
| PluginIssuesClient.idempotencyKeyPrefix | | |
| PluginIssuesClient.listComments | | |
| PluginIssuesClient.createComment | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.body | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.createInteraction | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.interaction | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.suggestTasks | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.interaction | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.askUserQuestions | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.interaction | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.requestConfirmation | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.interaction | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.requestCheckboxConfirmation | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.interaction | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.listInteractions | | |
| PluginIssuesClient.respondInteraction | | |
| PluginIssuesClient.issueId | | |
| PluginIssuesClient.interactionId | | |
| PluginIssuesClient.input | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.listAttachments | | |
| PluginIssuesClient.getAttachmentContent | | |
| PluginIssuesClient.attachmentId | | |
| PluginIssuesClient.companyId | | |
| PluginIssuesClient.options | | |
| PluginIssuesClient.documents | | |
| PluginIssuesClient.relations | | |
| PluginIssuesClient.summaries | | |
| HostToWorkerMethods.initialize | | |
| HostToWorkerMethods.health | | |
| HostToWorkerMethods.shutdown | | |
| HostToWorkerMethods.validateConfig | | |
| HostToWorkerMethods.configChanged | | |
| HostToWorkerMethods.onEvent | | |
| HostToWorkerMethods.runJob | | |
| HostToWorkerMethods.handleWebhook | | |
| HostToWorkerMethods.handleApiRequest | | |
| HostToWorkerMethods.getData | | |
| HostToWorkerMethods.performAction | | |
| HostToWorkerMethods.executeTool | | |
| HostToWorkerMethods.detectExternalObjects | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.resolveExternalObject | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.refreshExternalObjects | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentValidateConfig | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentProbe | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentAcquireLease | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentResumeLease | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentReleaseLease | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentDestroyLease | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentRealizeWorkspace | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentExecute | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentSyncIn | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentSyncOut | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentStartInteractiveSetup | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentGetInteractiveSetup | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentCaptureTemplate | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentCancelInteractiveSetup | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.environmentDeleteTemplate | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.setupTokenPtyOpen | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |
| HostToWorkerMethods.setupTokenPtyInput | | |
| HostToWorkerMethods.setupTokenPtyStop | | |
| HostToWorkerMethods.setupTokenPtyClose | | |
| HostToWorkerMethods.params | | |
| HostToWorkerMethods.result | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
