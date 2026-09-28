# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 12 files · ~92,116 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 590 nodes · 1369 edges · 62 communities (43 shown, 19 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 49 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- heartbeat.ts
- heartbeatService
- executeRun
- budgetService
- scheduleBoundedRetryForRun
- readNonEmptyString
- resolveSessionBeforeForWakeup
- reapOrphanedRuns
- getRun
- cancelRunInternal
- resolveWorkspaceForRun
- enqueueWakeup
- heartbeat-stop-metadata.ts
- claimQueuedRun
- startNextQueuedRunForAgent
- types/cost.ts
- updateRuntimeState
- evaluateSessionCompaction
- handleSuccessfulRunHandoff
- types/budget.ts
- costRoutes
- resolveInstructionsConfigFingerprintMetadata
- mergeCoalescedContextSnapshot
- resolveExecutionRunAdapterConfig
- buildPaperclipWakePayload
- buildRunEventRuntimeProgress
- readWorkspaceConfigFingerprintFromMetadata
- validators/budget.ts
- validators/cost.ts
- resolveTaskSessionConfigFreshness
- readTaskDrain
- claimPendingCleanupCapWarning
- budget_incidents.ts
- createManagedMcpRunConfig
- execFile
- configuredPaperclipApiBaseUrl
- provisionExecutionWorkspaceForFreshnessDecision
- resolveResponsibleUserIdForRunSeed
- isHeartbeatRunRuntimeStatusActive
- startTaskDrain
- boundHeartbeatRunEventPayloadForStorage
- buildWorkspaceConfigFreshnessOperation
- readConfigFingerprintFromSessionParams
- readTransientRecoveryContractFromRun
- cost_events.ts
- buildEffectiveRunWorkspaceConfigMetadata
- ChatControlRecoveryUnresolvedError
- compactRunLogChunk
- ConfigurationIncompleteFailure
- resolveRunScopedMentionedSkillKeys
- filterZombieCoalesceTarget
- fingerprintFinalizeWorkspaceBranchValidation
- hasGithubPrWorkflowSkill
- completeSkillTestRunForHeartbeatOutcome
- persistRunProcessMetadata
- NativeSessionResumeScheduledError
- NativeWorkspaceFinalizeScheduledError
- resolveWorkspaceAfterLowTrustPreflight
- resolveAdditionalRunWorkspaces
- resolveNativeSandboxLifecycle
- WorkspaceBusyDeferral
- WorkspaceValidationFailure

## God Nodes (most connected - your core abstractions)
1. `heartbeatService()` - 189 edges
2. `executeRun()` - 141 edges
3. `readNonEmptyString()` - 100 edges
4. `enqueueWakeup()` - 41 edges
5. `reapOrphanedRuns()` - 28 edges
6. `appendRunEvent()` - 24 edges
7. `scheduleBoundedRetryForRun()` - 21 edges
8. `claimQueuedRun()` - 20 edges
9. `cancelRunInternal()` - 20 edges
10. `budgetService()` - 18 edges
11. `getRun()` - 18 edges
12. `startNextQueuedRunForAgent()` - 17 edges
13. `drainRunningRunsForShutdown()` - 14 edges
14. `getAgent()` - 13 edges
15. `cancelActiveForAgentInternal()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `heartbeatService()` --calls--> `budgetService()`  [EXTRACTED]
  server/src/services/heartbeat.ts → server/src/services/budgets.ts
- `updateRuntimeState()` --calls--> `costService()`  [EXTRACTED]
  server/src/services/heartbeat.ts → server/src/services/costs.ts
- `mergeRunStopMetadataForAgent()` --calls--> `buildHeartbeatRunStopMetadata()`  [EXTRACTED]
  server/src/services/heartbeat.ts → server/src/services/heartbeat-stop-metadata.ts
- `mergeRunStopMetadataForAgent()` --calls--> `mergeHeartbeatRunStopMetadata()`  [EXTRACTED]
  server/src/services/heartbeat.ts → server/src/services/heartbeat-stop-metadata.ts
- `costService()` --calls--> `budgetService()`  [EXTRACTED]
  server/src/services/costs.ts → server/src/services/budgets.ts

## Import Cycles
- None detected.

## Communities (62 total, 19 thin omitted)

### Community 0 - "heartbeat.ts"
Cohesion: 0.02
Nodes (101): AcceptedPlanWakeRoutingDecision, ACTIVE_RUN_LOG_RUNTIME_STATUS_REFRESH_INTERVAL_MS, ACTIVE_RUN_OUTPUT_PROGRESS_FLUSH_INTERVAL_MS, activeRunExecutionPromises, activeRunExecutions, activeWakeupPromises, BOUNDED_TRANSIENT_HEARTBEAT_RETRY_DELAYS_MS, CANCELLABLE_HEARTBEAT_RUN_STATUSES (+93 more)

### Community 1 - "heartbeatService"
Cohesion: 0.08
Nodes (29): heartbeatService(), buildRunLivenessInput(), cancelInvocationsForAgentsInternal(), cancelPendingWakeupsForAgentsInternal(), cancelPendingWakeupsForBudgetScope(), classifyAndPersistRunLiveness(), clearIssueMonitorAndRecover(), countValue() (+21 more)

### Community 2 - "executeRun"
Cohesion: 0.06
Nodes (35): appendExcerpt(), applyRunScopedMentionedSkillKeys(), attachPaperclipSessionMetadataToSessionParams(), attestReviewedExternalChatRun(), buildExecutionWorkspaceConfigSnapshot(), buildPaperclipTaskMarkdown(), buildReferencedProjectRunObservability(), buildRunWorkspaceHints() (+27 more)

### Community 3 - "budgetService"
Cohesion: 0.11
Nodes (26): BudgetEnforcementScope, budgetService(), buildPolicySummary(), createIncidentIfNeeded(), hydrateIncidentRows(), pauseAndCancelScopeForBudget(), pauseScopeForBudget(), resolveOpenIncidentsForPolicy() (+18 more)

### Community 4 - "scheduleBoundedRetryForRun"
Cohesion: 0.09
Nodes (31): computeBoundedTransientHeartbeatRetrySchedule(), deriveTaskKeyWithHeartbeatFallback(), addPlanApprovalResumeFailureCommentOnce(), buildPlanApprovalResumeFailureComment(), buildPlanApprovalResumeFailureResult(), enqueueMissingIssueCommentRetry(), escalatePlanApprovalResumeFailureNeedsAttention(), finalizeIssueCommentPolicy() (+23 more)

### Community 5 - "readNonEmptyString"
Cohesion: 0.10
Nodes (23): assertGitSensitiveAdapterWorkspaceValid(), assertPushCapabilityCheckoutValid(), buildSandboxProviderPluginNotReadyResultJson(), buildUnresolvedWorkspaceBaseRefResultJson(), hasGitMetadata(), hasGitPushRemote(), issueIdFromRunContext(), issueIdFromWakePayload() (+15 more)

### Community 6 - "resolveSessionBeforeForWakeup"
Cohesion: 0.22
Nodes (17): buildExplicitResumeSessionOverride(), deriveTaskKey(), describeSessionResetReason(), getAdapterSessionCodec(), getTaskSession(), hasResolvablePriorSessionWorkspaceForWake(), hasResolvableSessionWorkspaceCwd(), resolveExplicitResumeSessionOverride() (+9 more)

### Community 7 - "reapOrphanedRuns"
Cohesion: 0.18
Nodes (17): buildProcessLossMessage(), decorateHeartbeatRunRuntimeStatus(), appendRunEvent(), clearDetachedRunWarning(), emitTerminalAgentTaskRun(), enqueueProcessLossRetry(), markNativeOwnershipUnverified(), reapOrphanedRuns() (+9 more)

### Community 8 - "getRun"
Cohesion: 0.18
Nodes (17): acknowledgeRemoteStop(), deferPendingCleanupLease(), getRun(), hasUnsafeTextProjectionDatabase(), readPendingCleanupRetryAttempts(), recoverNativeRunsAfterRestart(), releaseEnvironmentLeasesForRun(), resumeExecutionWaitComments() (+9 more)

### Community 9 - "cancelRunInternal"
Cohesion: 0.25
Nodes (16): cancelHeartbeatNativeRun(), computeWorkspaceBusyRetryDelayMs(), cancelActiveForAgentInternal(), cancelBudgetScopeWork(), cancellationTerminationGraceMs(), cancelQueuedRunForHeartbeatDailyCap(), cancelRunInternal(), drainRunningRunsForShutdown() (+8 more)

### Community 10 - "resolveWorkspaceForRun"
Cohesion: 0.21
Nodes (14): buildAnchorFallbackWorkspaceNotes(), defaultAdditionalProjectWorkspaceDeps(), deriveRepoNameFromRepoUrl(), ensureManagedProjectWorkspace(), resolveAnchorWorkspaceForRun(), resolveWorkspaceForRun(), isConfinedRemoteStagingDriver(), isFalsyRuntimeEnvValue() (+6 more)

### Community 11 - "enqueueWakeup"
Cohesion: 0.16
Nodes (14): addContinuationExhaustedCommentOnce(), dispatchPendingNativeStatusWakeups(), enqueueWakeup(), getIssueExecutionContext(), handleIssueReviewPathDisposition(), handleRunLivenessContinuation(), hasActionableTimerWork(), markTimerHeartbeatChecked() (+6 more)

### Community 12 - "heartbeat-stop-metadata.ts"
Cohesion: 0.23
Nodes (13): isMaxTurnExhaustionRun(), buildHeartbeatRunStopMetadata(), defaultTimeoutSecForAdapter(), hasOwn(), HeartbeatRunOutcome, HeartbeatRunStopMetadata, HeartbeatRunStopReason, HeartbeatRunTimeoutPolicy (+5 more)

### Community 13 - "claimQueuedRun"
Cohesion: 0.24
Nodes (11): applyRunDispatchPostCommitEffects(), cancelQueuedRunForBlockedDependencies(), claimQueuedRun(), currentUtcDayWindow(), getHeartbeatDailyCapBlock(), promoteDueScheduledRetries(), publishRunLifecyclePluginEvent(), publishRunLifecyclePluginEventData() (+3 more)

### Community 14 - "startNextQueuedRunForAgent"
Cohesion: 0.22
Nodes (11): applyWakeQueuePostCommitEffects(), countRunningRunsForAgent(), finalizeAgentStatus(), getAgent(), issueRunPriorityRank(), listCompanyAgentOrgRows(), normalizeOptionalNonNegativeInteger(), parseHeartbeatPolicy() (+3 more)

### Community 15 - "types/cost.ts"
Cohesion: 0.20
Nodes (9): CostByAgent, CostByAgentModel, CostByBiller, CostByProject, CostByProviderModel, CostEvent, CostSummary, CostWindowSpendRow (+1 more)

### Community 16 - "updateRuntimeState"
Cohesion: 0.20
Nodes (10): ensureRuntimeState(), getRuntimeState(), updateRuntimeState(), normalizeBilledCostCents(), normalizeLedgerBillingType(), normalizeUsageTotals(), resolveCacheAdjustedCostUsd(), resolveLedgerBiller() (+2 more)

### Community 17 - "evaluateSessionCompaction"
Cohesion: 0.22
Nodes (9): deriveNormalizedUsageDelta(), formatCount(), evaluateSessionCompaction(), getLatestRunForSession(), getOldestRunForSession(), resolveNormalizedUsageForSession(), parseSessionCompactionPolicy(), readRawUsageTotals() (+1 more)

### Community 18 - "handleSuccessfulRunHandoff"
Cohesion: 0.29
Nodes (8): addSuccessfulRunHandoffCommentOnce(), buildDetectedSuccessfulRunProgressSummary(), handleSuccessfulRunHandoff(), hasUnmanagedBackgroundTaskEvidence(), issueUiLink(), withUnmanagedBackgroundTaskStopReason(), redactDetectedSuccessfulRunProgressSummaryForBoard(), redactSuccessfulRunHandoffEvidence()

### Community 19 - "types/budget.ts"
Cohesion: 0.29
Nodes (6): BudgetIncident, BudgetIncidentResolutionInput, BudgetOverview, BudgetPolicy, BudgetPolicySummary, BudgetPolicyUpsertInput

### Community 20 - "costRoutes"
Cohesion: 0.38
Nodes (3): costRoutes(), parseCostDateRange(), parseCostLimit()

### Community 21 - "resolveInstructionsConfigFingerprintMetadata"
Cohesion: 0.29
Nodes (7): buildEffectiveRunSessionConfigMetadata(), buildSessionConfigCategoryValues(), hashFileContentsForConfigFingerprint(), isPathInsideRoot(), resolveInstructionsConfigFingerprintMetadata(), resolveRootBoundInstructionsFingerprintPath(), sanitizeSecretManifestForConfigFingerprint()

### Community 22 - "mergeCoalescedContextSnapshot"
Cohesion: 0.33
Nodes (7): clearInteractionContinuationWakeContext(), enrichWakeContextSnapshot(), hasInteractionContinuationWakeContext(), isInteractionResolutionWakePayload(), mergeCoalescedContextSnapshot(), mergeWakeCommentIds(), normalizeInteractionContinuationWakeContext()

### Community 23 - "resolveExecutionRunAdapterConfig"
Cohesion: 0.47
Nodes (6): assertLowTrustEnvConfigAllowed(), formatMissingBindingForOperator(), isConfiguredEnvBindingValue(), resolveExecutionRunAdapterConfig(), stripForbiddenEnvBindings(), stripForbiddenEnvFromAdapterConfig()

### Community 24 - "buildPaperclipWakePayload"
Cohesion: 0.33
Nodes (6): buildPaperclipWakePayload(), externalAttachmentOmissionNotice(), mergeExternalAttachmentOmissions(), readExternalAttachmentOmissions(), resolveExternalChatWakeProvider(), sanitizeAgentSessionMessageText()

### Community 25 - "buildRunEventRuntimeProgress"
Cohesion: 0.67
Nodes (6): buildRunEventRuntimeProgress(), readFirstLiveRunProgressString(), readLiveRunAssistantSnippet(), readLiveRunProgressString(), readLiveRunToolName(), sanitizeLiveRunProgressText()

### Community 26 - "readWorkspaceConfigFingerprintFromMetadata"
Cohesion: 0.33
Nodes (6): changedEffectiveRunWorkspaceConfigCategories(), describeEffectiveRunWorkspaceConfigCategories(), parseStoredWorkspaceConfigCategoryFingerprints(), readWorkspaceConfigCategoriesFromMetadata(), readWorkspaceConfigFingerprintFromMetadata(), resolveExecutionWorkspaceConfigFreshness()

### Community 27 - "validators/budget.ts"
Cohesion: 0.40
Nodes (4): ResolveBudgetIncident, resolveBudgetIncidentSchema, UpsertBudgetPolicy, upsertBudgetPolicySchema

### Community 28 - "validators/cost.ts"
Cohesion: 0.40
Nodes (4): CreateCostEvent, createCostEventSchema, UpdateBudget, updateBudgetSchema

### Community 29 - "resolveTaskSessionConfigFreshness"
Cohesion: 0.50
Nodes (5): changedEffectiveRunSessionConfigCategories(), describeEffectiveRunConfigCategories(), readConfiguredModelFromSessionParams(), resolveTaskSessionConfigFreshness(), shouldResetTaskSessionForModelChange()

### Community 30 - "readTaskDrain"
Cohesion: 0.40
Nodes (5): getTaskDrainStatus(), isTruthyRuntimeEnvValue(), readTaskDrain(), resolveHeartbeatSchedulingSuppression(), stopTaskDrain()

### Community 31 - "claimPendingCleanupCapWarning"
Cohesion: 0.50
Nodes (5): claimPendingCleanupCapWarning(), claimPendingCleanupRetryAttempt(), pendingCleanupAttemptsSql(), pendingCleanupCapWarnedSql(), pendingCleanupMetadataObjectSql()

### Community 33 - "createManagedMcpRunConfig"
Cohesion: 0.50
Nodes (4): adapterSupportsManagedMcpConfig(), createManagedMcpRunConfig(), gatewayAppliesToRun(), gatewayConnectionIds()

### Community 34 - "execFile"
Cohesion: 0.50
Nodes (4): assertGitWorktreeBaseWorkspaceReady(), execFile, isGitCheckout(), materializeManagedProjectWorkspace()

### Community 35 - "configuredPaperclipApiBaseUrl"
Cohesion: 0.50
Nodes (4): buildPaperclipRuntimeMcpServers(), configuredPaperclipApiBaseUrl(), createAdapterRuntimeToolAccess(), paperclipApiBaseUrl()

### Community 36 - "provisionExecutionWorkspaceForFreshnessDecision"
Cohesion: 0.50
Nodes (4): formatInheritedExecutionWorkspaceReuseFailure(), isWorkspaceValidationFailure(), provisionExecutionWorkspaceForFreshnessDecision(), resolveExecutionWorkspaceReuseProvisioningPolicy()

### Community 37 - "resolveResponsibleUserIdForRunSeed"
Cohesion: 0.50
Nodes (4): isManualUserRun(), resolveCompanyDefaultResponsibleUserId(), resolveParentIssueResponsibleUserId(), resolveResponsibleUserIdForRunSeed()

### Community 38 - "isHeartbeatRunRuntimeStatusActive"
Cohesion: 0.67
Nodes (4): recordCurrentHeartbeatRunRuntimeProgress(), isHeartbeatRunRuntimeStatusActive(), publishHeartbeatRunRuntimeProgress(), recordHeartbeatRunRuntimeProgress()

### Community 39 - "startTaskDrain"
Cohesion: 0.67
Nodes (3): applyTaskDrain(), computeTaskDrain(), startTaskDrain()

### Community 40 - "boundHeartbeatRunEventPayloadForStorage"
Cohesion: 0.67
Nodes (3): boundHeartbeatRunEventPayloadForStorage(), boundRunEventValue(), truncateRunEventString()

### Community 41 - "buildWorkspaceConfigFreshnessOperation"
Cohesion: 0.67
Nodes (3): buildWorkspaceConfigFreshnessOperation(), recordWorkspaceConfigFreshnessOperation(), workspaceConfigFreshnessActionLabel()

### Community 42 - "readConfigFingerprintFromSessionParams"
Cohesion: 0.67
Nodes (3): parseStoredConfigCategoryFingerprints(), readConfigCategoriesFromSessionParams(), readConfigFingerprintFromSessionParams()

### Community 43 - "readTransientRecoveryContractFromRun"
Cohesion: 0.67
Nodes (3): readHeartbeatRunErrorFamily(), readTransientRecoveryContractFromRun(), readTransientRetryNotBeforeFromRun()

## Knowledge Gaps
- **133 isolated node(s):** `ScopeRecord`, `PolicyRow`, `IncidentRow`, `CostDateRange`, `SUBSCRIPTION_BILLING_TYPES` (+128 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `heartbeatService()` connect `heartbeatService` to `heartbeat.ts`, `executeRun`, `budgetService`, `scheduleBoundedRetryForRun`, `readNonEmptyString`, `resolveSessionBeforeForWakeup`, `reapOrphanedRuns`, `getRun`, `cancelRunInternal`, `resolveWorkspaceForRun`, `enqueueWakeup`, `claimQueuedRun`, `startNextQueuedRunForAgent`, `updateRuntimeState`, `evaluateSessionCompaction`, `handleSuccessfulRunHandoff`, `mergeCoalescedContextSnapshot`, `readTaskDrain`, `claimPendingCleanupCapWarning`, `resolveResponsibleUserIdForRunSeed`, `isHeartbeatRunRuntimeStatusActive`, `startTaskDrain`, `filterZombieCoalesceTarget`, `completeSkillTestRunForHeartbeatOutcome`, `persistRunProcessMetadata`?**
  _High betweenness centrality (0.327) - this node is a cross-community bridge._
- **Why does `executeRun()` connect `executeRun` to `heartbeatService`, `scheduleBoundedRetryForRun`, `readNonEmptyString`, `resolveSessionBeforeForWakeup`, `reapOrphanedRuns`, `getRun`, `cancelRunInternal`, `resolveWorkspaceForRun`, `enqueueWakeup`, `heartbeat-stop-metadata.ts`, `claimQueuedRun`, `startNextQueuedRunForAgent`, `updateRuntimeState`, `evaluateSessionCompaction`, `handleSuccessfulRunHandoff`, `resolveInstructionsConfigFingerprintMetadata`, `mergeCoalescedContextSnapshot`, `resolveExecutionRunAdapterConfig`, `buildPaperclipWakePayload`, `readWorkspaceConfigFingerprintFromMetadata`, `resolveTaskSessionConfigFreshness`, `createManagedMcpRunConfig`, `execFile`, `configuredPaperclipApiBaseUrl`, `provisionExecutionWorkspaceForFreshnessDecision`, `isHeartbeatRunRuntimeStatusActive`, `buildWorkspaceConfigFreshnessOperation`, `readTransientRecoveryContractFromRun`, `buildEffectiveRunWorkspaceConfigMetadata`, `compactRunLogChunk`, `resolveRunScopedMentionedSkillKeys`, `fingerprintFinalizeWorkspaceBranchValidation`, `completeSkillTestRunForHeartbeatOutcome`, `persistRunProcessMetadata`, `resolveWorkspaceAfterLowTrustPreflight`, `resolveNativeSandboxLifecycle`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Why does `readNonEmptyString()` connect `readNonEmptyString` to `heartbeat.ts`, `heartbeatService`, `executeRun`, `scheduleBoundedRetryForRun`, `resolveSessionBeforeForWakeup`, `reapOrphanedRuns`, `getRun`, `resolveWorkspaceForRun`, `enqueueWakeup`, `claimQueuedRun`, `startNextQueuedRunForAgent`, `updateRuntimeState`, `evaluateSessionCompaction`, `handleSuccessfulRunHandoff`, `resolveInstructionsConfigFingerprintMetadata`, `mergeCoalescedContextSnapshot`, `resolveExecutionRunAdapterConfig`, `buildPaperclipWakePayload`, `readWorkspaceConfigFingerprintFromMetadata`, `resolveTaskSessionConfigFreshness`, `createManagedMcpRunConfig`, `execFile`, `configuredPaperclipApiBaseUrl`, `resolveResponsibleUserIdForRunSeed`, `isHeartbeatRunRuntimeStatusActive`, `readConfigFingerprintFromSessionParams`, `readTransientRecoveryContractFromRun`, `buildEffectiveRunWorkspaceConfigMetadata`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `heartbeatService()` (e.g. with `applyTaskDrain()` and `computeTaskDrain()`) actually correct?**
  _`heartbeatService()` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `enqueueWakeup()` (e.g. with `heartbeatService()` and `executeRun()`) actually correct?**
  _`enqueueWakeup()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `reapOrphanedRuns()` (e.g. with `heartbeatService()` and `settleRecoveredNativeWorkspace()`) actually correct?**
  _`reapOrphanedRuns()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `ScopeRecord`, `PolicyRow`, `IncidentRow` to the rest of the system?**
  _133 weakly-connected nodes found - possible documentation gaps or missing edges._