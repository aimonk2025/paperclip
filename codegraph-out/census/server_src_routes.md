# Capability census — routes

**59 files · 59,433 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 53 |
| validates input | 53 |
| reads config | 12 |
| caches | 11 |
| enforces a timeout | 10 |
| retries | 10 |
| reads from disk | 8 |
| emits telemetry | 8 |
| parses JSON events | 6 |
| classifies errors | 6 |
| handles cancellation | 6 |
| tracks token usage | 5 |
| captures a session id | 5 |
| streams incrementally | 3 |
| spawns a process | 2 |
| buffers partial lines | 2 |
| writes to disk | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `issues.ts` | 12824 | ISSUE_LIST_SERVER_CACHE_MAX_ENTRIES, __getIssueListResponseCacheSizeForTests, __clearIssueListResponseCacheForTests, issueRoutes |
| `openapi.ts` | 7787 | buildOpenApiDocument, buildOpenApiSpec, openApiRoutes |
| `agents.ts` | 5188 | agentRoutes |
| `access.ts` | 4876 | createInviteToken, companyInviteExpiresAt, buildJoinDefaultsPayloadForAccept, mergeJoinDefaultsPayloadForReplay, canReplayOpenClawGatewayInviteAccept +7 |
| `plugins.ts` | 3140 | PluginRouteJobDeps, PluginRouteWebhookDeps, PluginRouteToolDeps, PluginRouteBridgeDeps, PluginRouteToolGatewayDeps +1 |
| `pipelines.ts` | 2913 | pipelineRoutes |
| `cases.ts` | 1542 | buildCasePatchUpdateValues, caseRoutes |
| `companies.ts` | 1536 | CompanyRoutesOptions, companyRoutes |
| `company-skills.ts` | 1410 | companySkillRoutes |
| `environments.ts` | 1407 | isPlatformProvisionedEnvironment, applyPlatformProvisionedEnvironmentFloor, environmentRoutes |
| `tool-access.ts` | 1392 | toolAccessRoutes |
| `execution-workspaces.ts` | 1360 | executionWorkspaceRoutes |
| `secrets.ts` | 1127 | secretRoutes |
| `file-resources.ts` | 940 | WorkspaceFileResourceService, createFileResourceLimiter, createFileResourceListLimiter, createFileResourceAvailabilityLimiter, fileResourceRoutes |
| `tool-gateway.ts` | 830 | mcpGatewayProtocolRoutes, toolGatewayRoutes |
| `org-chart-svg.ts` | 777 | OrgNode, OrgChartStyle, ORG_CHART_STYLES, OrgChartOverlay, renderOrgChartSvg +1 |
| `adapters.ts` | 717 | adapterRoutes |
| `projects.ts` | 691 | projectRoutes |
| `routines.ts` | 670 | routineRoutes |
| `approvals.ts` | 535 | approvalRoutes |
| `plugin-ui-static.ts` | 510 | resolvePluginUiDir, PluginUiStaticRouteOptions, pluginUiStaticRoutes |
| `user-profiles.ts` | 437 | userProfileRoutes |
| `board-chat.ts` | 405 | isConciergeReply, boardChatRoutes |
| `costs.ts` | 404 | parseCostDateRange, parseCostLimit, costRoutes |
| `issue-tree-control.ts` | 395 | issueTreeControlRoutes |

## Contract members — each is a capability

**WorkspaceFileResourceService** (28 members)

```
getIssue, availability, issueId, input, opts, list, workspace, projectId, workspaceId, path, mode, q, limit, offset, issue, scanContext, resolve, issueId, input, opts, readContent, issueId, input, opts, prepareDownload, issueId, input, opts
```

**ActorSecretContext** (6 members)

```
consumerType, consumerId, actorType, actorId, actorSource, responsibleUserId
```

**OrgNode** (6 members)

```
id, name, role, status, reports, collapsedReports
```

**InstanceDatabaseBackupRunResult** (6 members)

```
trigger, backupDir, retention, startedAt, finishedAt, durationMs
```

**WorkspaceRuntimeControlAuthorization** (4 members)

```
actorType, agentId, runId, issueId
```

**OrgChartOverlay** (2 members)

```
companyName, stats
```

**PluginRouteJobDeps** (2 members)

```
scheduler, jobStore
```

**PluginRouteBridgeDeps** (2 members)

```
workerManager, streamBus
```

## Structural duplication — the reduction lever

Identical logic across N files. This is where a rebuild gets smaller
WITHOUT losing features — unlike dropping capabilities.

| Repeated in | Shape |
|---|---|
| **14 files** | `const actor = getActorInfo(req); await logActivity(db, { companyId, ac…` |
| **13 files** | `companyId, actorType: actor.actorType, actorId: actor.actorId, agentId…` |
| **12 files** | `await logActivity(db, { companyId, actorType: actor.actorType, actorId…` |
| **5 files** | `actorType: actor.actorType, actorId: actor.actorId, agentId: actor.age…` |
| **4 files** | `const decision = await access.decide({ actor: req.actor, action: "comp…` |
| **4 files** | `await logActivity(db, { companyId: existing.companyId, actorType: acto…` |

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
| WorkspaceFileResourceService.getIssue | | |
| WorkspaceFileResourceService.availability | | |
| WorkspaceFileResourceService.issueId | | |
| WorkspaceFileResourceService.input | | |
| WorkspaceFileResourceService.opts | | |
| WorkspaceFileResourceService.list | | |
| WorkspaceFileResourceService.workspace | | |
| WorkspaceFileResourceService.projectId | | |
| WorkspaceFileResourceService.workspaceId | | |
| WorkspaceFileResourceService.path | | |
| WorkspaceFileResourceService.mode | | |
| WorkspaceFileResourceService.q | | |
| WorkspaceFileResourceService.limit | | |
| WorkspaceFileResourceService.offset | | |
| WorkspaceFileResourceService.issue | | |
| WorkspaceFileResourceService.scanContext | | |
| WorkspaceFileResourceService.resolve | | |
| WorkspaceFileResourceService.issueId | | |
| WorkspaceFileResourceService.input | | |
| WorkspaceFileResourceService.opts | | |
| WorkspaceFileResourceService.readContent | | |
| WorkspaceFileResourceService.issueId | | |
| WorkspaceFileResourceService.input | | |
| WorkspaceFileResourceService.opts | | |
| WorkspaceFileResourceService.prepareDownload | | |
| WorkspaceFileResourceService.issueId | | |
| WorkspaceFileResourceService.input | | |
| WorkspaceFileResourceService.opts | | |
| ActorSecretContext.consumerType | | |
| ActorSecretContext.consumerId | | |
| ActorSecretContext.actorType | | |
| ActorSecretContext.actorId | | |
| ActorSecretContext.actorSource | | |
| ActorSecretContext.responsibleUserId | | |
| OrgNode.id | | |
| OrgNode.name | | |
| OrgNode.role | | |
| OrgNode.status | | |
| OrgNode.reports | | |
| OrgNode.collapsedReports | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
