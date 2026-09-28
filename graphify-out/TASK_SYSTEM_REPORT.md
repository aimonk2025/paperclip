# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 161 files · ~397,606 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3930 nodes · 8253 edges · 159 communities (155 shown, 4 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 180 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- services/heartbeat.ts
- validators/issue.ts
- types/issue.ts
- heartbeatService
- services/workspace-runtime.ts
- issueRoutes
- routes/issues.ts
- services/issues.ts
- schema/issues.ts
- executeRun
- issueService
- issue-execution-policy.ts
- runGit
- readNonEmptyString
- services/pipelines.ts
- services/issue-tree-control.ts
- routes/pipelines.ts
- startRuntimeServicesForWorkspaceControlInvocation
- workspace-file-resources.ts
- execution-workspace-policy.ts
- issue-graph-liveness.ts
- issue-thread-interactions.ts
- wake-queue/index.ts
- enqueueWakeup
- services/routines.ts
- wake-queue/adapters/postgres.ts
- resolveTaskWatchdogMutationScope
- heartbeat-run-summary.ts
- routineService
- wake-queue/application/ports.ts
- services/execution-workspaces.ts
- task-watchdogs.ts
- types/workspace-runtime.ts
- spawnLocalRuntimeService
- active-run-watchdog/application/use-cases.ts
- run-dispatch/adapters/postgres.ts
- native-workspace-sync.ts
- pipelines-aggregation.ts
- listBlockedInboxIssues
- active-run-watchdog/adapters/postgres.ts
- run-dispatch/index.ts
- wake-queue/application/use-cases.ts
- executionWorkspaceService
- types/heartbeat.ts
- types/pipeline.ts
- managed-workspace-identity.ts
- workspace-operations.ts
- types/routine.ts
- transitionCaseInTransaction
- workspace-git-operation-scheduler.ts
- validators/routine.ts
- validators/pipeline.ts
- routes/execution-workspaces.ts
- pipelineRoutes
- heartbeat-run-runtime-status.ts
- pipelineService
- pluginManagedRoutineService
- run-dispatch/domain/policy.ts
- QueuedCommentQueueTransaction
- issueThreadInteractionService
- nowDate
- active-run-watchdog/application/types.ts
- issueRecoveryActionService
- WakeQueueTransaction
- wake-queue/domain/policy.ts
- scheduleBoundedRetryForRun
- workspace-instance-cleanup.ts
- pipeline-health.ts
- buildIssueSubtreeDiagnosticsResponse
- issue-continuation-summary.ts
- issueReferenceService
- WorkspaceGitOperationScheduler
- execution-workspace.ts
- pipeline-case-outputs.ts
- resolveWorkspaceForRun
- types/workspace-file-resource.ts
- validators/workspace-file-resource.ts
- readNonEmptyString
- acceptRequestConfirmation
- createPostgresRunDispatchAdapter
- issue-dependency-wakeups.ts
- workspace-operation-log-store.ts
- workspace-commands.ts
- blockedInboxIssueConditions
- availability
- routine-variables.ts
- appendHeartbeatRunEvent
- issue-rewake-throttle.ts
- workspace-runtime-leases.ts
- issue-attribution.ts
- issue-write-denial.ts
- heartbeat-stop-metadata.ts
- issue-thread-interaction-resolution.ts
- onboarding-first-task-assets.ts
- createPostgresWatchdogAdapter
- derivePipelineCaseLiveness
- taskWatchdogService
- dispatchRoutineRun
- listLocalFileCandidate
- src/issue-references.ts
- cross-issue-influence-limit.ts
- workspace-command-authz.ts
- resolveSessionBeforeForWakeup
- evaluateWatchdog
- types/issue-tree-control.ts
- assertCurrentStageAutomationTargetWriteAccess
- loadEffectiveRuntimeServicesByExecutionWorkspace
- issue-prefix.ts
- native-workspace-finalizer.ts
- task-search.ts
- workspace-realization.ts
- recordWorkspaceCommandOperation
- Run-Log Events
- parseIssueExecutionState
- issue-review-policy.ts
- inspectExecutionWorkspaceBranchForReconcile
- visibleIssueCondition
- legacy-controller-lease.ts
- validators/issue-tree-control.ts
- routineRoutes
- readExecutionWorkspaceConfig
- evaluateSessionCompaction
- syncPipelineStageAutomation
- services/workspace-readiness.ts
- IssueThreadInteractionBase
- deriveCommentId
- handleSuccessfulRunHandoff
- pipeline-conversation-context.ts
- upsertIssueWatchdogForIssue
- google-workspace-connectors.ts
- IssueCommentMetadataRowBase
- types/workspace-readiness.ts
- TransactionScope
- emitAgentTaskRun
- assessDelivery
- assertRequestConfirmationResolutionAllowedUnderLock
- listIssueBlockerAttentionMap
- readStringFromRecord
- nextCronTickInTimeZone
- statLocalCandidate
- routes/issue-tree-control.ts
- issueListRequestKey
- isRuntimeOwnedGitBranch
- buildRunEventRuntimeProgress
- issueApprovalService
- getIssueRelationSummaryMap
- adapter-login-lease.ts
- issueThreadInteractionResolutionError
- pipeline-case-type.ts
- workspace-operation.ts
- buildIssueChanges
- issue-goal-fallback.ts
- buildPipelineCaseContextMarkdown
- getAncestorCases
- PreparedNativeWorkspaceSync
- reviewedFingerprintForWatchdogIssue
- ipv4CidrRange
- resolveCreateIssueStatusDefault

## God Nodes (most connected - your core abstractions)
1. `heartbeatService()` - 198 edges
2. `issueRoutes()` - 193 edges
3. `executeRun()` - 178 edges
4. `issueService()` - 137 edges
5. `readNonEmptyString()` - 100 edges
6. `executionWorkspaceService()` - 60 edges
7. `enqueueWakeup()` - 56 edges
8. `routineService()` - 56 edges
9. `issueThreadInteractionService()` - 50 edges
10. `pipelineRoutes()` - 45 edges
11. `visibleIssueCondition()` - 36 edges
12. `spawnLocalRuntimeService()` - 34 edges
13. `reapOrphanedRuns()` - 30 edges
14. `issues` - 28 edges
15. `claimQueuedRun()` - 28 edges

## Surprising Connections (you probably didn't know these)
- `heartbeatService()` --indirect_call--> `sweepExpiredHeartbeatRunRuntimeStatuses()`  [INFERRED]
  server/src/services/heartbeat.ts → server/src/services/heartbeat-run-runtime-status.ts
- `AcceptedPlanDecompositionChild` --references--> `IssueExecutionWorkspaceSettings`  [EXTRACTED]
  packages/shared/src/types/issue.ts → packages/shared/src/types/workspace-runtime.ts
- `Issue` --references--> `IssueExecutionWorkspaceSettings`  [EXTRACTED]
  packages/shared/src/types/issue.ts → packages/shared/src/types/workspace-runtime.ts
- `PipelineCaseConversationSource` --references--> `Issue`  [EXTRACTED]
  packages/shared/src/types/pipeline.ts → packages/shared/src/types/issue.ts
- `createPostgresWatchdogAdapter()` --calls--> `issueRecoveryActionService()`  [EXTRACTED]
  server/src/modules/active-run-watchdog/adapters/postgres.ts → server/src/services/issue-recovery-actions.ts

## Import Cycles
- None detected.

## Communities (159 total, 4 thin omitted)

### Community 0 - "services/heartbeat.ts"
Cohesion: 0.01
Nodes (175): AcceptedPlanWakeRoutingDecision, ACTIVE_RUN_LOG_RUNTIME_STATUS_REFRESH_INTERVAL_MS, ACTIVE_RUN_OUTPUT_PROGRESS_FLUSH_INTERVAL_MS, activeRunExecutionPromises, activeRunExecutions, activeWakeupPromises, adapterSupportsManagedMcpConfig(), applyTaskDrain() (+167 more)

### Community 1 - "validators/issue.ts"
Cohesion: 0.01
Nodes (136): AcceptIssueThreadInteraction, acceptIssueThreadInteractionSchema, AddIssueComment, addIssueCommentSchema, askUserQuestionsAnswerSchema, askUserQuestionsPayloadSchema, askUserQuestionsQuestionOptionSchema, askUserQuestionsQuestionSchema (+128 more)

### Community 2 - "types/issue.ts"
Cohesion: 0.02
Nodes (124): AcceptedPlanDecomposition, AcceptedPlanDecompositionChildIssue, AcceptedPlanDecompositionResult, AcceptedPlanDecompositionStatus, AcceptedPlanDecompositionSummary, AskUserQuestionsAnswer, AskUserQuestionsPayload, AskUserQuestionsQuestion (+116 more)

### Community 3 - "heartbeatService"
Cohesion: 0.05
Nodes (99): buildProcessLossMessage(), cancelHeartbeatNativeRun(), computeWorkspaceBusyRetryDelayMs(), heartbeatService(), acknowledgeRemoteStop(), addContinuationExhaustedCommentOnce(), appendRunEvent(), applyRunDispatchPostCommitEffects() (+91 more)

### Community 4 - "services/workspace-runtime.ts"
Cohesion: 0.02
Nodes (95): ACTIVE_RUNTIME_PORT_RESERVATION_STATUSES, allocateAndReserveExposure(), AuthoritativeBaseRefResolution, buildCompanyExposureReservationLedger(), buildDirtyQuarantineRescueBranch(), defaultWorkspaceRuntimeExposureDeps(), detectPersistedExposureReservationDrift(), DirtyQuarantineRepairResult (+87 more)

### Community 5 - "issueRoutes"
Cohesion: 0.03
Nodes (65): actorMatchesExecutionParticipant(), applyCreateIssueStatusDefault(), assertCanManageIssueMonitor(), buildRequestItemVerdictsWakeIdempotencyKey(), companySearchRateLimitActor(), emptyWorkspaceNameMaps(), estimatedJsonBytes(), isAssigneeSelfCommentOnTerminalIssue() (+57 more)

### Community 6 - "routes/issues.ts"
Cohesion: 0.02
Nodes (91): ACTIVE_REVIEW_APPROVAL_STATUSES, ActivityExecutionParticipant, activityExecutionParticipantKey(), ActivityIssueRelationSummary, applyActorMonitorScheduledBy(), attachmentArtifactMetadataInputSchema, auditAgentIssueCommentAttributionSpoof(), auditAgentIssueCreateAttributionSpoof() (+83 more)

### Community 7 - "services/issues.ts"
Cohesion: 0.02
Nodes (93): ACCEPTED_PLAN_DECOMPOSITION_FINGERPRINT_CHILD_METADATA_KEYS, AcceptedPlanDecompositionInput, AcceptedPlanDocumentInteraction, ACTIVE_RUN_STATUSES, ALL_ISSUE_STATUSES, BLOCKED_INBOX_ACTIVE_RUN_STATUSES, BLOCKED_INBOX_PENDING_APPROVAL_STATUSES, BLOCKED_INBOX_PENDING_INTERACTION_STATUSES (+85 more)

### Community 8 - "schema/issues.ts"
Cohesion: 0.05
Nodes (48): agentSessionGoalActions, agentTaskSessions, environmentLeases, executionWorkspaceRuntimeLeases, executionWorkspaces, heartbeatRunEvents, heartbeatRunWatchdogDecisions, heartbeatRuns (+40 more)

### Community 9 - "executeRun"
Cohesion: 0.04
Nodes (66): resolveEffectiveWorkspaceStrategyType(), appendExcerpt(), applyRunScopedMentionedSkillKeys(), assertGitWorktreeBaseWorkspaceReady(), attachPaperclipSessionMetadataToSessionParams(), attestReviewedExternalChatRun(), buildExecutionWorkspaceConfigSnapshot(), buildPaperclipRuntimeMcpServers() (+58 more)

### Community 10 - "issueService"
Cohesion: 0.04
Nodes (45): ResolveAdditionalRunWorkspacesOptions, ResolveRunReferencedProjectsOptions, cancelIssueStatusesForHold(), activeInboxArchiveFields(), appendAcceptanceCriteriaToDescription(), applyStatusSideEffects(), assertExecutionTaskParent(), assertTransition() (+37 more)

### Community 11 - "issue-execution-policy.ts"
Cohesion: 0.08
Nodes (54): ActorLike, actorPrincipal(), applyIssueExecutionPolicyTransition(), applyIssueExecutionStageTransition(), applyIssueMonitorPolicyTransition(), applyMonitorTransition(), AssigneeLike, assigneePrincipal() (+46 more)

### Community 12 - "runGit"
Cohesion: 0.09
Nodes (53): acquireGitWorktreeCleanupLock(), assertDirtyQuarantineRuntimeServicesStopped(), assertGitIndexIsUnlocked(), branchIncoherenceValidationFailure(), cleanupExecutionWorkspaceArtifacts(), deleteGitBranchAtVerifiedTip(), detectDefaultBranch(), detectGitWorktreeInProgressOperation() (+45 more)

### Community 13 - "readNonEmptyString"
Cohesion: 0.06
Nodes (50): assertGitSensitiveAdapterWorkspaceValid(), assertPushCapabilityCheckoutValid(), buildPaperclipWakePayload(), buildSandboxProviderPluginNotReadyResultJson(), buildUnresolvedWorkspaceBaseRefResultJson(), clearInteractionContinuationWakeContext(), deriveTaskKey(), describeSessionResetReason() (+42 more)

### Community 14 - "services/pipelines.ts"
Cohesion: 0.06
Nodes (41): addFormVariablesForStage(), assertCaseKey(), assertValidParentCase(), buildPipelineAutomationIssueTitlePrefix(), buildPipelineCaseVariables(), CanonicalPipelineStageKind, cleanPipelineIssueTitlePart(), DEFAULT_STAGES (+33 more)

### Community 15 - "services/issue-tree-control.ts"
Cohesion: 0.08
Nodes (45): ACTIVE_RUN_STATUSES, ActiveCancelSnapshot, ActiveIssueTreePauseHoldGate, ActiveRunRow, ActorInput, actorMatchesComment(), buildAffectedAgents(), buildWarnings() (+37 more)

### Community 16 - "routes/pipelines.ts"
Cohesion: 0.08
Nodes (42): intakeFieldTypes, issueIdFromPipelineRouteRunContext(), listPipelineCaseDocumentRevisions(), listPipelineDocumentRevisions(), mapPipelineCaseDocumentRevision(), mapPipelineDocumentRevision(), PipelineRouteDb, acknowledgeDriftSchema (+34 more)

### Community 17 - "startRuntimeServicesForWorkspaceControlInvocation"
Cohesion: 0.10
Nodes (43): anyRuntimeServiceUsesHttpsExposure(), buildRuntimePortAllocationConflict(), canRetryDeferredPortBindCollision(), cleanupPersistedExposureRows(), cleanupRecordExposure(), clearIdleTimer(), createRuntimeProvisionCoordinator(), decideManagedRuntimeExposureBackfill() (+35 more)

### Community 18 - "workspace-file-resources.ts"
Cohesion: 0.05
Nodes (38): AutoDiscovered, availabilityResult(), availableFileList(), candidateFromExecutionWorkspace(), DENIED_SEGMENTS, ExecutionWorkspaceRow, expectedAvailabilityReason(), IMAGE_CONTENT_TYPES (+30 more)

### Community 19 - "execution-workspace-policy.ts"
Cohesion: 0.07
Nodes (38): assertAgentCanManageRuntimeServicesForWorkspace(), assertCanManageExecutionWorkspaceRuntimeServices(), assertCanManageProjectWorkspaceRuntimeServices(), assertLowTrustCanManageRuntimeForActor(), assertLowTrustCanManageRuntimeForIssue(), listReportingSubtreeAgentIds(), readRunIssueId(), WORKSPACE_RUNTIME_ELIGIBLE_ISSUE_STATUS_LIST (+30 more)

### Community 20 - "issue-graph-liveness.ts"
Cohesion: 0.11
Nodes (38): addAgentChainCandidates(), addOwnerCandidate(), classifyIssueGraphLiveness(), blockedFindingForLeaf(), firstBlockedChainFinding(), hasExplicitWaitingPath(), reviewFinding(), classifyIssueReviewPaths() (+30 more)

### Community 21 - "issue-thread-interactions.ts"
Cohesion: 0.07
Nodes (37): assertRequestConfirmationTargetIsCurrent(), buildInteractionResolvedCounts(), CreateInteractionOptions, DbTransaction, DEFAULT_RESOLVER_POLICY_BY_KIND, deriveResolutionReason(), deriveTargetType(), emitInteractionResolvedTelemetry() (+29 more)

### Community 22 - "wake-queue/index.ts"
Cohesion: 0.10
Nodes (30): createPostgresWakeQueueAdapter(), createWakeAdmissionReader(), createWakeAdmissionWriter(), QueuedCommentQueuePostgresAdapterDeps, RunRow, WakeRow, LockedQueuedCommentState, QueuedCommentActivityLogInput (+22 more)

### Community 23 - "enqueueWakeup"
Cohesion: 0.10
Nodes (36): buildTransaction(), claimPendingCleanupCapWarning(), claimPendingCleanupRetryAttempt(), deferPendingCleanupLease(), dispatchPendingNativeStatusWakeups(), enqueueWakeup(), hasActionableTimerWork(), markTimerHeartbeatChecked() (+28 more)

### Community 24 - "services/routines.ts"
Cohesion: 0.08
Nodes (35): IssueAssignmentWakeupDeps, queueIssueAssignmentWakeup(), WakeupSource, WakeupTriggerDetail, ACTIVITY_GATE_IGNORED_ACTIONS, Actor, assertRoutineCanEnable(), assertRoutineVariableDefinitions() (+27 more)

### Community 25 - "wake-queue/adapters/postgres.ts"
Cohesion: 0.10
Nodes (29): extractWakeCommentIds(), buildTransaction(), EXECUTION_PATH_HEARTBEAT_RUN_STATUSES, HeartbeatRunRow, IssueRow, toDeferredWakeCandidate(), toRequestedByActorType(), toRunSnapshot() (+21 more)

### Community 26 - "resolveTaskWatchdogMutationScope"
Cohesion: 0.10
Nodes (34): assertAgentInteractionRunAttribution(), assertAgentIssueCommentAllowed(), assertAgentIssueMutationAllowed(), assertCanAssignTasks(), assertFreshTaskWatchdogSourceMutation(), assertIssueReadAllowed(), assertIssueThreadInteractionContainmentAllowed(), assertIssueThreadInteractionWithdrawalAllowed() (+26 more)

### Community 27 - "heartbeat-run-summary.ts"
Cohesion: 0.11
Nodes (32): findLatestCompletedFinalAgentMessage(), buildHeartbeatRunIssueComment(), CHAT_RUN_PRESENTATION_AUTHORIZATION_REASON, CompletedFinalAgentMessageCandidate, decision(), findHeartbeatRunCompletionComment(), hasAcceptedSemanticResult(), hasYieldedSemanticResult() (+24 more)

### Community 28 - "routineService"
Cohesion: 0.07
Nodes (23): executionIssueTransientFailureClearedAtFromPayload(), executionIssueTransientFailureReason(), executionIssueTransientFailureStatusFromPayload(), legacyExecutionIssueTransientFailureStatus(), mapRoutineDescriptionDocument(), mapRoutineRevision(), nextResultText(), normalizeWebhookTimestampMs() (+15 more)

### Community 29 - "wake-queue/application/ports.ts"
Cohesion: 0.07
Nodes (22): AdmitWakeBehindIssueExecutionResult, CoalescedDeferredAdmissionReceipt, DeferredWakeCandidate, DurableWakeAdmissionReceipt, ExistingDeferredWake, LockedIssueExecution, PromoteDeferredWakeInput, RecoveryEscalationPort (+14 more)

### Community 30 - "services/execution-workspaces.ts"
Cohesion: 0.07
Nodes (31): assigneeMatchesExecutionPrincipal(), DbTransaction, EXECUTION_WORKSPACE_LIFECYCLE_GENERATION_METADATA_KEY, EXECUTION_WORKSPACE_REOPEN_FAILED_REASON, EXECUTION_WORKSPACE_REOPEN_PENDING_METADATA_KEY, EXECUTION_WORKSPACE_REOPEN_PENDING_SINCE_METADATA_KEY, ExecutionWorkspaceBranchReconcileActor, ExecutionWorkspaceBranchReconcileInspection (+23 more)

### Community 31 - "task-watchdogs.ts"
Cohesion: 0.08
Nodes (31): ActorFields, classifyTaskWatchdogSubtree(), IssueRow, issueUpdatedAtIso(), IssueWatchdogRow, IssueWatchdogUpsertInput, materialLeaf(), optionalIso() (+23 more)

### Community 32 - "types/workspace-runtime.ts"
Cohesion: 0.06
Nodes (30): ExecutionWorkspaceCloseAction, ExecutionWorkspaceCloseActionKind, ExecutionWorkspaceCloseGitReadiness, ExecutionWorkspaceCloseLinkedIssue, ExecutionWorkspaceCloseReadiness, ExecutionWorkspaceCloseReadinessState, ExecutionWorkspaceConfig, ExecutionWorkspaceDeliveryState (+22 more)

### Community 33 - "spawnLocalRuntimeService"
Cohesion: 0.11
Nodes (31): allocateIsolatedWorkspacePort(), allocateRuntimeServicePort(), buildExecutionWorkspaceCleanupEnv(), buildTemplateData(), canBindRuntimePort(), claimRuntimeServiceBindPort(), classifyExposureHostCollisions(), eaddrinuseTextNamesPort() (+23 more)

### Community 34 - "active-run-watchdog/application/use-cases.ts"
Cohesion: 0.11
Nodes (28): findLatestSameRunTerminalEvidence(), foldSourceResolvedRun(), BuildRunOutputSilenceDeps, BuildRunOutputSilenceRunInput, createBuildRunOutputSilence(), createScanSilentActiveRuns(), inspectSilentActiveRun(), resolveSourceIssue() (+20 more)

### Community 35 - "run-dispatch/adapters/postgres.ts"
Cohesion: 0.10
Nodes (22): CancelSuppressedRetryInput, CancelSuppressedRetryResult, HeartbeatRun, LoadGateFactsInput, LoadGateFactsResult, LoadStalenessFactsInput, NO_REVIEW_PARTICIPANT, queuedEffect() (+14 more)

### Community 36 - "native-workspace-sync.ts"
Cohesion: 0.14
Nodes (28): canonicalJson(), classifyNativeWorkspaceInbound(), cleanupNativeWorkspaceSync(), descriptorDirectory(), descriptorPath(), durableSeedPaths(), ensurePrivateDirectory(), leaseStamp() (+20 more)

### Community 37 - "pipelines-aggregation.ts"
Cohesion: 0.09
Nodes (29): ActiveWork, AttentionCaller, boundedLimit(), CASE_CHILDREN_TREE_MAX_DEPTH, CASE_CHILDREN_TREE_MAX_NODES, CaseChildNode, CaseChildrenRollup, caseDisplay() (+21 more)

### Community 38 - "listBlockedInboxIssues"
Cohesion: 0.10
Nodes (29): activeRunMapForIssues(), attentionBase(), blockedByMapForIssues(), blockedInboxResponseDescription(), blockedInboxSearchText(), chunkList(), countBlockedInboxIssues(), decodeDatabaseTextPreview() (+21 more)

### Community 39 - "active-run-watchdog/adapters/postgres.ts"
Cohesion: 0.12
Nodes (16): RECOVERY_ORIGIN_KIND_VALUES, FindCandidateSilentRunsInput, FindLatestDecisionResult, FindLatestSameRunTerminalEvidenceInput, RunningAgentSnapshot, WatchdogRunReader, WatchdogWriter, EvaluationIssueSnapshot (+8 more)

### Community 40 - "run-dispatch/index.ts"
Cohesion: 0.13
Nodes (23): PostCommitEffect, QueuedRunEvent, RunDispatchApplicationError, RunDispatchApplicationErrorCode, RunStatusEvent, createCancelStaleQueuedRun(), createDispatchResolvedInteractionIfCurrent(), createEvaluateScheduledRetryGate() (+15 more)

### Community 41 - "wake-queue/application/use-cases.ts"
Cohesion: 0.12
Nodes (23): WakeQueueHost, IssueSnapshot, AdmitWakeBehindIssueExecutionInput, createAdmitWakeBehindIssueExecution(), createReleaseIssueExecution(), currentAgentParticipant(), didAutomaticRecoveryFail(), EXECUTION_REVIEW_PARTICIPANT_RECOVERY_WAKE_REASONS (+15 more)

### Community 42 - "executionWorkspaceService"
Cohesion: 0.12
Nodes (25): acquireExecutionWorkspaceLifecycleLock(), assertBranchReconcileRuntimeServicesStopped(), assertBranchReconcileWorkspaceIsSafe(), bumpExecutionWorkspaceLifecycleGeneration(), clearMetadataReopenPendingConsumption(), executionWorkspaceService(), assertTerminalCleanupGitStateUnchanged(), cleanupTerminalWorkspace() (+17 more)

### Community 43 - "types/heartbeat.ts"
Cohesion: 0.07
Nodes (26): AgentRuntimeState, AgentTaskSession, AgentWakeupRequest, AgentWakeupResponse, AgentWakeupSkipped, ChatFailedRunRetryResponse, GitWorktreeBranchAncestryVerdict, GitWorktreeBranchIncoherenceEvidence (+18 more)

### Community 44 - "types/pipeline.ts"
Cohesion: 0.08
Nodes (26): PipelineAutomationRetryBlocker, PipelineAutomationRetryCleanupOptions, PipelineAutomationRetryEffectCounts, PipelineAutomationRetryPlan, PipelineAutomationRetryRequest, PipelineAutomationRetryRoutineRef, PipelineAutomationRetryScope, PipelineAutomationRetryStageRef (+18 more)

### Community 45 - "managed-workspace-identity.ts"
Cohesion: 0.12
Nodes (24): buildManagedWorkspaceGuestEnv(), isWorkspaceReadinessShape(), listManagedWorkspaceHandoffSubjects(), logManagedWorkspaceReadinessRejection(), ManagedWorkspaceIdentity, probeManagedWorkspaceHandoffSubjects(), probeManagedWorkspaceReadiness(), resolveManagedWorkspaceIdentity() (+16 more)

### Community 46 - "workspace-operations.ts"
Cohesion: 0.10
Nodes (21): activeRuntimeControls, appendExcerpt(), combineMetadata(), liveRuntimeControlOperationIds, ownerProcessIsAlive(), readRuntimeControlAction(), readRuntimeControlOwner(), RUNTIME_CONTROL_ACTIONS (+13 more)

### Community 47 - "types/routine.ts"
Cohesion: 0.10
Nodes (25): AcceptedPlanDecompositionChild, PipelineStageAutomation, Routine, RoutineAgentSummary, RoutineDescriptionDocument, RoutineDetail, RoutineEnvConfig, RoutineExecutionIssueOrigin (+17 more)

### Community 48 - "transitionCaseInTransaction"
Cohesion: 0.13
Nodes (26): assertActorCanApproveStageExit(), assertLatestReviewApprovalStillCurrent(), assertNoOpenBlockers(), assertStageEnabled(), assertStageTransitionGates(), childrenGateConfig(), computeCaseRollup(), enqueueStageAutomationLedger() (+18 more)

### Community 49 - "workspace-git-operation-scheduler.ts"
Cohesion: 0.09
Nodes (22): CacheEntry, clampInteger(), createSpawnRunner(), envInteger(), envOptions, getWorkspaceGitOperationSchedulerSnapshot(), PendingScan, signalChild() (+14 more)

### Community 50 - "validators/routine.ts"
Cohesion: 0.08
Nodes (24): isValidRoutineDateString(), ISSUE_EXECUTION_WORKSPACE_PREFERENCES, issueExecutionWorkspaceSettingsSchema, baseTriggerSchema, CreateRoutine, createRoutineSchema, CreateRoutineTrigger, createRoutineTriggerSchema (+16 more)

### Community 51 - "validators/pipeline.ts"
Cohesion: 0.08
Nodes (24): legacyPipelineStageKindSchema, PipelineAutomationRetryCleanupOptions, pipelineAutomationRetryCleanupOptionsSchema, PipelineAutomationRetryRequest, pipelineAutomationRetryRequestSchema, PipelineAutomationRetryScope, pipelineAutomationRetryScopeSchema, PipelineStageApprover (+16 more)

### Community 52 - "routes/execution-workspaces.ts"
Cohesion: 0.17
Nodes (22): executionWorkspaceRoutes(), assertRuntimeManageAllowed(), handleExecutionWorkspaceRuntimeCommand(), reconcileFailedRuntimeStart(), isReadableFile(), resolveFallbackSeedSourceConfigPath(), assertNoAgentHostWorkspaceCommandMutation(), cloneRecord() (+14 more)

### Community 53 - "pipelineRoutes"
Cohesion: 0.09
Nodes (24): activityActorForPipelineRoute(), actorForMutation(), assertIssueLinkMutationAllowed(), attentionCallerFor(), codedConflictForUnique(), extractIntakeFormFields(), getChildOutcomeSummaries(), getIssueMutationTarget() (+16 more)

### Community 54 - "heartbeat-run-runtime-status.ts"
Cohesion: 0.14
Nodes (23): decorateHeartbeatRunRuntimeStatus(), recordCurrentHeartbeatRunRuntimeProgress(), isHeartbeatRunRuntimeStatusActive(), publishHeartbeatRunRuntimeProgress(), readRuntimeStatusIssueIdCandidate(), recordHeartbeatRunRuntimeProgress(), clearHeartbeatRunRuntimeStatus(), cloneStatus() (+15 more)

### Community 55 - "pipelineService"
Cohesion: 0.15
Nodes (24): assertReviewTargetsInSet(), defaultRetryCleanup(), descendantCaseIds(), getPipelineOrThrow(), pipelineService(), assertAutomationAssigneeCanWriteTargetPipeline(), assertRoutineInCompany(), buildAutomationRetryPlan() (+16 more)

### Community 56 - "pluginManagedRoutineService"
Cohesion: 0.22
Nodes (22): buildRoutineDefaults(), managedByPlugin(), normalizeRef(), pluginManagedRoutineService(), createManagedRoutine(), declarationFor(), ensureDefaultTriggers(), get() (+14 more)

### Community 57 - "run-dispatch/domain/policy.ts"
Cohesion: 0.12
Nodes (22): BudgetBlockFacts, decideExecutionLock(), decideIssueOwnership(), decideIssueStatus(), decideQueuedRunStaleness(), decideReviewParticipant(), decideScheduledRetryGate(), DependencyBlockFacts (+14 more)

### Community 58 - "QueuedCommentQueueTransaction"
Cohesion: 0.18
Nodes (10): createQueuedCommentIssueLockWriter(), QueuedCommentQueueTransaction, createDiscardQueuedComment(), createEditQueuedComment(), createReorderQueuedComments(), requireMutationTarget(), updateQueueRunCommentIdsGuarded(), decideQueuedCommentActorOwnsEntry() (+2 more)

### Community 59 - "issueThreadInteractionService"
Cohesion: 0.09
Nodes (22): buildIssueDocumentTargetFromDocument(), buildSupersededByNewerInteractionResult(), buildSupersededByNewerRequestResult(), buildTaskCreationOrder(), emitInteractionCreatedTelemetry(), interactionNotFoundError(), isCommentAtOrAfterInteraction(), isEquivalentCreateRequest() (+14 more)

### Community 60 - "nowDate"
Cohesion: 0.12
Nodes (23): activityActorPatch(), actorOwnsLease(), adjustParentCounts(), assertActorProvenance(), assertJsonSize(), assertLeaseAvailable(), buildCaseDeepLink(), buildPipelineCaseContextPack() (+15 more)

### Community 61 - "active-run-watchdog/application/types.ts"
Cohesion: 0.15
Nodes (16): createProcessAdapter(), SESSIONED_LOCAL_ADAPTERS, RunProcessController, RunOutputSilenceSummary, RunProcessCleanupOutcome, RunProcessMetadata, RunStatus, ScanSilentActiveRunsResult (+8 more)

### Community 62 - "issueRecoveryActionService"
Cohesion: 0.16
Nodes (21): recordNativeTerminalRecoveryIfNeeded(), ACTIVE_RECOVERY_ACTION_STATUSES, asDatabaseDate(), DbOrTransaction, DbTransaction, isRecoveryBudgetExhausted(), IssueRecoveryActionRow, issueRecoveryActionService() (+13 more)

### Community 63 - "WakeQueueTransaction"
Cohesion: 0.11
Nodes (5): IssueLockWriter, WakeQueueTransaction, InvokableAgentSnapshot, RunSnapshot, RunSummary

### Community 64 - "wake-queue/domain/policy.ts"
Cohesion: 0.09
Nodes (21): DeferredWakeAgentFacts, DeferredWakeOutcomeDecision, DeferredWakeOutcomeFacts, DeferredWakePauseHoldFacts, DeferredWakeQueuedCommentDecision, DeferredWakeQueuedCommentFacts, ImmediateRecoveryContextLabels, PreDrainDecision (+13 more)

### Community 65 - "scheduleBoundedRetryForRun"
Cohesion: 0.13
Nodes (22): computeBoundedTransientHeartbeatRetrySchedule(), deriveTaskKeyWithHeartbeatFallback(), addPlanApprovalResumeFailureCommentOnce(), buildPlanApprovalResumeFailureComment(), buildPlanApprovalResumeFailureResult(), enqueueMissingIssueCommentRetry(), escalatePlanApprovalResumeFailureNeedsAttention(), getAcceptedPlanApprovalInteractionForRun() (+14 more)

### Community 66 - "workspace-instance-cleanup.ts"
Cohesion: 0.14
Nodes (19): cleanupWorktreeInstanceArtifacts(), defaultCleanupDependencies, defaultPostgresStopDependencies, EmbeddedPostgresStopDependencies, execFileAsync, isStrictChildPath(), pathExists(), processIsAlive() (+11 more)

### Community 67 - "pipeline-health.ts"
Cohesion: 0.14
Nodes (19): agentLabel(), asConfig(), automationAssigneeAgentId(), computePipelineHealth(), hasChildrenGateAutoAdvance(), hasOnEnterRoutineAutomation(), hasRunnableStageAutomation(), isPipelineTerminalStageKind() (+11 more)

### Community 68 - "buildIssueSubtreeDiagnosticsResponse"
Cohesion: 0.13
Nodes (21): blockerDiagnosticLabel(), buildIssueBlockerDiagnosis(), buildIssueBlockerDiagnosticsResponse(), buildIssueSubtreeDiagnosis(), buildIssueSubtreeDiagnosticsResponse(), buildIssueWakeDiagnosis(), buildIssueWakeDiagnosticsResponse(), dateToIso() (+13 more)

### Community 69 - "issue-continuation-summary.ts"
Cohesion: 0.17
Nodes (20): AgentSummaryInput, asNonEmptyString(), buildContinuationSummaryMarkdown(), bulletList(), continuationSummaryParksExecutor(), extractContinuationSummaryNextAction(), extractMarkdownSection(), extractPathCandidates() (+12 more)

### Community 70 - "issueReferenceService"
Cohesion: 0.18
Nodes (18): diffIssueSummaries(), emptySummary(), issueReferenceService(), issueById(), listIssueReferenceSummary(), replaceSourceMentions(), syncAllForCompany(), syncAllForIssue() (+10 more)

### Community 71 - "WorkspaceGitOperationScheduler"
Cohesion: 0.21
Nodes (4): abortError(), scanKey(), WorkspaceGitOperationScheduler, withRuntimeStartMutex()

### Community 72 - "execution-workspace.ts"
Cohesion: 0.10
Nodes (19): branchReconcileReasonSchema, executionWorkspaceCloseActionKindSchema, executionWorkspaceCloseActionSchema, executionWorkspaceCloseGitReadinessSchema, executionWorkspaceCloseLinkedIssueSchema, executionWorkspaceCloseReadinessSchema, executionWorkspaceCloseReadinessStateSchema, executionWorkspaceConfigSchema (+11 more)

### Community 73 - "pipeline-case-outputs.ts"
Cohesion: 0.18
Nodes (19): buildCaseContextMarkdown(), contentPath(), contextFetchHint(), DELIVERABLE_TITLE_PATTERNS, deliverableDocumentRank(), downloadPath(), formatPipelineCaseOutputContextMarkdown(), normalizePreviewText() (+11 more)

### Community 74 - "resolveWorkspaceForRun"
Cohesion: 0.13
Nodes (19): buildAnchorFallbackWorkspaceNotes(), defaultAdditionalProjectWorkspaceDeps(), deriveRepoNameFromRepoUrl(), ensureManagedProjectWorkspace(), hasResolvableSessionWorkspaceCwd(), resolveAnchorWorkspaceForRun(), resolveWorkspaceForRun(), isConfinedRemoteStagingDriver() (+11 more)

### Community 75 - "types/workspace-file-resource.ts"
Cohesion: 0.11
Nodes (18): NormalizedWorkspaceFileAvailabilityQuery, ResolvedWorkspaceResource, WorkspaceFileAvailabilityQuery, WorkspaceFileAvailabilityRequest, WorkspaceFileAvailabilityResponse, WorkspaceFileAvailabilityResult, WorkspaceFileContent, WorkspaceFileContentEncoding (+10 more)

### Community 76 - "validators/workspace-file-resource.ts"
Cohesion: 0.11
Nodes (18): normalizedWorkspaceFileAvailabilityQuerySchema, resolvedWorkspaceResourceSchema, utf8ByteLength(), WorkspaceFileAvailabilityRequestInput, workspaceFileAvailabilityRequestSchema, workspaceFileAvailabilityResponseSchema, workspaceFileAvailabilityResultSchema, workspaceFileContentSchema (+10 more)

### Community 77 - "readNonEmptyString"
Cohesion: 0.20
Nodes (19): buildQueuedCommentQueue(), cancelScheduledRetrySupersededByComment(), findQueuedCommentWake(), lockQueuedCommentState(), queueCommentsForWake(), readObject(), resolveRunIssueWorkspaceInheritanceSource(), listSuccessfulRunHandoffStates() (+11 more)

### Community 78 - "acceptRequestConfirmation"
Cohesion: 0.17
Nodes (19): buildAdministrativeOutcomeResult(), buildIssueDocumentTargetFromSnapshot(), buildSkippedOutcomeResult(), buildStaleTargetResult(), buildSupersededByCommentResult(), expireStaleRequestConfirmationTarget(), hydrateInteraction(), isNativeCompletionReview() (+11 more)

### Community 79 - "createPostgresRunDispatchAdapter"
Cohesion: 0.27
Nodes (17): buildReviewParticipantFacts(), classifyRetryReasonKind(), createPostgresRunDispatchAdapter(), cancelStaleQueuedRun(), cancelStaleRunInTx(), cancelSuppressedRetryInTx(), decideCurrentRunStaleness(), dispatchResolvedInteractionIfCurrent() (+9 more)

### Community 80 - "issue-dependency-wakeups.ts"
Cohesion: 0.19
Nodes (17): buildIssueBlockersResolvedWakeIdempotencyKey(), buildIssueBlockersResolvedWakeStateKey(), buildIssueBlockersResolvedWakeStateKeyWithoutCycle(), buildStateKey(), findExistingIssueBlockersResolvedWakeForReadyState(), formatIssueBlockersResolvedWakeCycle(), hashBlockerReadyStateDigest(), IDEMPOTENT_DEPENDENCY_WAKE_STATUS_SET (+9 more)

### Community 81 - "workspace-operation-log-store.ts"
Cohesion: 0.12
Nodes (10): createLocalFileWorkspaceOperationLogStore(), ensureDir(), getWorkspaceOperationLogStore(), resolveWithin(), WorkspaceOperationLogFinalizeSummary, WorkspaceOperationLogHandle, WorkspaceOperationLogReadOptions, WorkspaceOperationLogReadResult (+2 more)

### Community 82 - "workspace-commands.ts"
Cohesion: 0.21
Nodes (16): WorkspaceCommandDefinition, WorkspaceRuntimeService, buildWorkspaceCommandDefinition(), deriveWorkspaceCommandId(), findWorkspaceCommandDefinition(), isRecord(), listWorkspaceCommandDefinitions(), listWorkspaceServiceCommandDefinitions() (+8 more)

### Community 83 - "blockedInboxIssueConditions"
Cohesion: 0.12
Nodes (16): createdFromIssueCondition(), assertValidAssigneeAgentFilter(), blockedInboxIssueConditions(), hasPlanDocumentCondition(), inboxVisibleForUserCondition(), lowTrustBoundaryIssueCondition(), myLastCommentAtExpr(), myLastReadAtExpr() (+8 more)

### Community 84 - "availability"
Cohesion: 0.38
Nodes (17): candidateFromProjectWorkspace(), isHttpStatus(), normalizeWorkspaceRelativePath(), remoteResource(), workspaceFileResourceService(), availability(), discoverUniqueProjectWorkspaceMatch(), getIssue() (+9 more)

### Community 85 - "routine-variables.ts"
Cohesion: 0.20
Nodes (14): BUILTIN_ROUTINE_VARIABLE_NAMES, defaultRoutineVariable(), extractRoutineVariableNames(), HUMAN_TIMESTAMP_FORMATTER, interpolateRoutineTemplate(), isBuiltinRoutineVariable(), isRoutineDateVariableName(), isValidRoutineVariableName() (+6 more)

### Community 86 - "appendHeartbeatRunEvent"
Cohesion: 0.18
Nodes (13): allocateHeartbeatRunEventSeq(), appendHeartbeatRunEvent(), AppendHeartbeatRunEventInput, AppendHeartbeatRunEventResult, contiguousCursor(), HeartbeatRunEventConflictError, persistReprojectedWorkspaceDiffs(), projectCodexWorkspaceDiffsFromTrace() (+5 more)

### Community 87 - "issue-rewake-throttle.ts"
Cohesion: 0.13
Nodes (15): computeIssueRewakeCooldownMs(), evaluateIssueRewakeThrottle(), ISSUE_NEW_INPUT_ACTIVITY_ACTIONS, ISSUE_PROGRESS_ACTIVITY_ACTIONS, ISSUE_REWAKE_BASE_COOLDOWN_MS, ISSUE_REWAKE_LOOKBACK_MS, ISSUE_REWAKE_MAX_COOLDOWN_MS, ISSUE_REWAKE_NO_PROGRESS_THRESHOLD (+7 more)

### Community 88 - "workspace-runtime-leases.ts"
Cohesion: 0.14
Nodes (12): evaluateStaleOwner(), ExecutionWorkspaceRuntimeLeaseRow, LEASED_WORKSPACE_RUNTIME_ACTIONS, LeaseTx, parseOwnerKey(), TERMINAL_HEARTBEAT_RUN_STATUSES, WORKSPACE_RUNTIME_ELIGIBLE_ISSUE_STATUSES, WORKSPACE_RUNTIME_LEASE_TTL_MS (+4 more)

### Community 89 - "issue-attribution.ts"
Cohesion: 0.14
Nodes (8): CLOSED_EXECUTION_WORKSPACE_STATUSES, ExecutionWorkspaceGuardTarget, OriginatingActor, ResponsibleUserAttribution, ResponsibleUserSource, Issue, PipelineCaseConversationSource, ExecutionWorkspace

### Community 90 - "issue-write-denial.ts"
Cohesion: 0.20
Nodes (11): actorLabel(), assigneeLabel(), describeIssueWriteDenial(), ISSUE_WRITE_DENIAL_CODES, issueLabel(), issueWriteDenialApiMessage(), IssueWriteDenialCode, IssueWriteDenialContext (+3 more)

### Community 91 - "heartbeat-stop-metadata.ts"
Cohesion: 0.23
Nodes (13): isMaxTurnExhaustionRun(), buildHeartbeatRunStopMetadata(), defaultTimeoutSecForAdapter(), hasOwn(), HeartbeatRunOutcome, HeartbeatRunStopMetadata, HeartbeatRunStopReason, HeartbeatRunTimeoutPolicy (+5 more)

### Community 92 - "issue-thread-interaction-resolution.ts"
Cohesion: 0.21
Nodes (13): assertIssueThreadInteractionResolverAudience(), canonicalizeStoredResolverPolicy(), canonicalStoredPolicy(), evaluateIssueThreadInteractionResolverAudience(), ISSUE_THREAD_INTERACTION_RESOLUTION_DENIAL_CODES, issueThreadInteractionAttentionAgentAllowed(), IssueThreadInteractionResolutionDenialCode, IssueThreadInteractionResolverActor (+5 more)

### Community 93 - "onboarding-first-task-assets.ts"
Cohesion: 0.23
Nodes (13): buildOnboardingFirstAgentInstructionsBundle(), buildOnboardingFirstTaskBrief(), buildOnboardingFirstTaskOpeningQuestion(), fillFirstTaskPlaceholders(), loadFirstTaskAsset(), ONBOARDING_FIRST_TASK_OPENING_INTERVIEW_OPTION_ID, ONBOARDING_FIRST_TASK_OPENING_QUESTION_ID, ONBOARDING_FIRST_TASK_OPENING_TASK_OPTION_ID (+5 more)

### Community 94 - "createPostgresWatchdogAdapter"
Cohesion: 0.19
Nodes (10): createPostgresWatchdogAdapter(), findCandidateSilentRuns(), findEvaluationIssueById(), findOpenStaleRunEvaluation(), findRunForCompany(), findSourceIssue(), selectEvaluationIssueSnapshot(), isRecoveryOriginKind() (+2 more)

### Community 95 - "derivePipelineCaseLiveness"
Cohesion: 0.15
Nodes (13): derivePipelineCaseLiveness(), getCaseDetail(), isLiveIssueStatus(), isWaitingIssueStatus(), latestBreakdownCreatedEvent(), loadBuiltFromAutomation(), parsePermissionPreflightFingerprint(), readBreakdownRequestKeys() (+5 more)

### Community 96 - "taskWatchdogService"
Cohesion: 0.24
Nodes (11): watchdogMapForIssues(), issueIdFromRunContext(), issueIdFromWakePayload(), readNonEmptyString(), summarizeIssueWatchdog(), taskWatchdogService(), collectClassifierInput(), collectCompletedRunIssueIds() (+3 more)

### Community 97 - "dispatchRoutineRun"
Cohesion: 0.21
Nodes (13): collectProvidedRoutineVariables(), createRoutineDispatchFingerprint(), createRoutineEnvFingerprint(), isPlainRecord(), mergeRoutineRunPayload(), normalizeRoutineDispatchFingerprintValue(), readManagedRoutineIssueTemplate(), resolveRoutineVariableValues() (+5 more)

### Community 98 - "listLocalFileCandidate"
Cohesion: 0.24
Nodes (13): denyReasonForPathSegments(), directoryResource(), enumerateWorkspaceDirectoryChildren(), enumerateWorkspaceFiles(), isInsideRoot(), listItemFromDirectory(), listLocalDirectoryChildCandidate(), listLocalFileCandidate() (+5 more)

### Community 99 - "src/issue-references.ts"
Cohesion: 0.32
Nodes (11): buildIssueReferenceHref(), extractIssueReferenceIdentifiers(), extractIssueReferenceMatches(), findIssueReferenceMatches(), ISSUE_REFERENCE_IDENTIFIER_RE, IssueReferenceMatch, normalizeIssueIdentifier(), parseIssueReferenceHref() (+3 more)

### Community 100 - "cross-issue-influence-limit.ts"
Cohesion: 0.24
Nodes (11): assertCrossIssueInfluenceWithinRunCap(), issueWriteDenialLabels(), CROSS_ISSUE_INFLUENCE_ENFORCE_AT, CROSS_ISSUE_INFLUENCE_LIMIT, CrossIssueInfluenceDecision, CrossIssueInfluenceKind, crossIssueInfluenceLimitError(), crossIssueInfluenceRunContextError() (+3 more)

### Community 101 - "workspace-command-authz.ts"
Cohesion: 0.55
Nodes (11): collectAgentAdapterWorkspaceCommandPaths(), collectExecutionWorkspaceCommandPaths(), collectExecutionWorkspaceConfigCommandPaths(), collectIssueWorkspaceCommandPaths(), collectProjectExecutionWorkspaceCommandPaths(), collectProjectWorkspaceCommandPaths(), collectWorkspaceRuntimeCommandPaths(), collectWorkspaceStrategyCommandPaths() (+3 more)

### Community 102 - "resolveSessionBeforeForWakeup"
Cohesion: 0.36
Nodes (12): buildExplicitResumeSessionOverride(), getAdapterSessionCodec(), getTaskSession(), hasResolvablePriorSessionWorkspaceForWake(), resolveExplicitResumeSessionOverride(), resolveSessionBeforeForWakeup(), isCanonicalSessionIdForAdapter(), normalizeResumeParamsForAdapter() (+4 more)

### Community 103 - "evaluateWatchdog"
Cohesion: 0.24
Nodes (12): canonicalJson(), isShrinkOfReviewedSnapshot(), isWatchdogReviewDisposition(), parseStopSnapshot(), evaluateWatchdog(), hasLivePathForIssue(), markTerminalWatchdogIssueReviewed(), sameFingerprintWatchdogReviewIsStillOpen() (+4 more)

### Community 104 - "types/issue-tree-control.ts"
Cohesion: 0.20
Nodes (10): IssueTreeControlPreview, IssueTreeHold, IssueTreeHoldMember, IssueTreeHoldReleasePolicy, IssueTreePreviewAgent, IssueTreePreviewIssue, IssueTreePreviewRun, IssueTreePreviewTotals (+2 more)

### Community 105 - "assertCurrentStageAutomationTargetWriteAccess"
Cohesion: 0.22
Nodes (11): assertCaseAccess(), assertCurrentStageAutomationTargetWriteAccess(), assertPipelineAccess(), assertPipelineCompanyAccess(), assertPipelineWriteAccess(), assertStageAutomationTargetWriteAccess(), readStageAutomationId(), readStageAutomationTargetPipelineId() (+3 more)

### Community 106 - "loadEffectiveRuntimeServicesByExecutionWorkspace"
Cohesion: 0.29
Nodes (10): loadEffectiveRuntimeServicesByExecutionWorkspace(), noActiveRuntimeServicesForWorkspaceCondition(), usesInheritedProjectRuntimeServices(), listCurrentRuntimeServicesForExecutionWorkspaces(), listCurrentRuntimeServicesForProjectWorkspaces(), runtimeServiceIdentityKey(), RuntimeServiceReadDb, selectConfiguredRuntimeServiceRows() (+2 more)

### Community 107 - "issue-prefix.ts"
Cohesion: 0.20
Nodes (7): DbTransaction, ISSUE_PREFIX_FALLBACK, IssuePrefixReadDb, issuePrefixSuffixForAttempt(), IssuePrefixWriteDb, MAX_ISSUE_PREFIX_ATTEMPTS, pickAvailableIssuePrefix()

### Community 108 - "native-workspace-finalizer.ts"
Cohesion: 0.33
Nodes (10): readString(), record(), resumeNativeWorkspaceFinalization(), workspaceSyncFailure(), finalizedWorkspaceStamp(), finalizePreparedRuntime(), persistLeaseStamp(), persistRunReference() (+2 more)

### Community 109 - "task-search.ts"
Cohesion: 0.31
Nodes (10): coverage(), escapeTaskSearchPattern(), FILLER, parseTaskSearch(), TaskSearch, taskSearchAny(), taskSearchCtes(), taskSearchFieldMatch() (+2 more)

### Community 110 - "workspace-realization.ts"
Cohesion: 0.47
Nodes (10): buildWorkspaceRealizationRecord(), buildWorkspaceRealizationRecordFromDriverInput(), buildWorkspaceRealizationRequest(), parseObject(), readAdditionalSources(), readNumber(), readPathAliases(), readString() (+2 more)

### Community 111 - "recordWorkspaceCommandOperation"
Cohesion: 0.22
Nodes (11): buildWorkspaceCommandEnv(), createProcessOutputCapture(), createProvisioningRuntimeServiceRecord(), executeProcess(), getGitWorktreeBranchAncestryVerdict(), readWorkspaceSeedOperationEvidence(), recordWorkspaceCommandOperation(), resolveShell() (+3 more)

### Community 112 - "Run-Log Events"
Cohesion: 0.18
Nodes (10): Codex resume usage snapshot, Execution recovery, Native Local Process Stop Evidence, Native PRP Run-Log Events, Native Restart Recovery Run-Log Event, Related instrumentation, Run-Log Events, Run Phase Timing Run-Log Event (+2 more)

### Community 113 - "parseIssueExecutionState"
Cohesion: 0.22
Nodes (10): hasExecutionParticipant(), hasScheduledMonitor(), assertInReviewReviewPath(), assertSafeRecoveryHandBackGates(), classifySourceRecoveryRevalidation(), revalidateActiveSourceRecovery(), revalidateActiveSourceRecoveryForRead(), summarizeIssueMonitor() (+2 more)

### Community 114 - "issue-review-policy.ts"
Cohesion: 0.33
Nodes (9): assertIssueThreadInteractionResolutionAllowed(), assertPendingReviewInteractionVerdictAllowed(), resolvePendingReviewInteractionRestriction(), assertIssueReviewVerdictActorAllowed(), isIssueReviewVerdictInteraction(), IssueReviewRequester, IssueReviewVerdictActor, resolveIssueReviewRequester() (+1 more)

### Community 115 - "inspectExecutionWorkspaceBranchForReconcile"
Cohesion: 0.27
Nodes (10): execFileAsync, explainGitWorktreeBranchReconcileInspection(), getGitWorktreeBranchAncestryVerdict(), inspectExecutionWorkspaceBranchForReconcile(), inspectGitCloseReadiness(), pathExists(), readGitStdout(), resolveLocalBranchCommit() (+2 more)

### Community 116 - "visibleIssueCondition"
Cohesion: 0.24
Nodes (8): executionIssueCondition(), visibleIssueCondition(), listLiveIssueByRoutineIds(), buildStoppedFingerprintComment(), isTerminalIssueStatus(), stoppedFingerprintMetadata(), ensureReusableWatchdogIssue(), findTaskWatchdogIssue()

### Community 117 - "legacy-controller-lease.ts"
Cohesion: 0.22
Nodes (9): hasLiveLegacyController(), LEGACY_CONTROLLER_LEASE_MS, LEGACY_CONTROLLER_RENEW_MS, legacyControllerBootId, legacyControllerClaim(), renewLegacyControllerLease(), revokeExpiredLegacyController(), Run (+1 more)

### Community 118 - "validators/issue-tree-control.ts"
Cohesion: 0.22
Nodes (8): CreateIssueTreeHold, createIssueTreeHoldSchema, issueTreeControlModeSchema, issueTreeHoldReleasePolicySchema, PreviewIssueTreeControl, previewIssueTreeControlSchema, ReleaseIssueTreeHold, releaseIssueTreeHoldSchema

### Community 120 - "readExecutionWorkspaceConfig"
Cohesion: 0.42
Nodes (9): assertLockedBranchReconcileWorkspaceStillMatchesInspection(), cloneRecord(), isRecord(), mergeExecutionWorkspaceConfig(), readDesiredState(), readExecutionWorkspaceConfig(), readNullableString(), readServiceStates() (+1 more)

### Community 121 - "evaluateSessionCompaction"
Cohesion: 0.22
Nodes (9): deriveNormalizedUsageDelta(), formatCount(), evaluateSessionCompaction(), getLatestRunForSession(), getOldestRunForSession(), resolveNormalizedUsageForSession(), parseSessionCompactionPolicy(), readRawUsageTotals() (+1 more)

### Community 122 - "syncPipelineStageAutomation"
Cohesion: 0.28
Nodes (9): legacyPipelineAutomationTitle(), appendPipelineAutomationRoutineRevision(), syncPipelineStageAutomation(), reconcilePipelineStageConfigVariables(), resolvePipelineAutomationTitleTemplate(), routineActorPatch(), routineRevisionSnapshotRoutine(), sanitizePipelineRoutineVariableRecords() (+1 more)

### Community 123 - "services/workspace-readiness.ts"
Cohesion: 0.33
Nodes (7): isManagedWorkspaceInstance(), readSeedManifestSummary(), resolveWorkspaceReadiness(), resolveWorkspaceReadinessState(), resolveWorkspaceSeedMarkerDir(), SeedManifestSummary, WorkspaceReadinessDeps

### Community 124 - "IssueThreadInteractionBase"
Cohesion: 0.25
Nodes (8): AskUserQuestionsInteraction, ConnectionIntentInteraction, IssueThreadInteractionActorFields, IssueThreadInteractionBase, RequestCheckboxConfirmationInteraction, RequestConfirmationInteraction, RequestItemVerdictsInteraction, SuggestTasksInteraction

### Community 125 - "deriveCommentId"
Cohesion: 0.29
Nodes (8): allowsIssueInteractionWake(), deriveCommentId(), readNonEmptyString(), finalizeIssueCommentPolicy(), findRunIssueComment(), hasDeferredIssueCommentWake(), patchRunIssueCommentStatus(), shouldRequireIssueCommentForWake()

### Community 126 - "handleSuccessfulRunHandoff"
Cohesion: 0.29
Nodes (8): addSuccessfulRunHandoffCommentOnce(), buildDetectedSuccessfulRunProgressSummary(), handleSuccessfulRunHandoff(), hasUnmanagedBackgroundTaskEvidence(), issueUiLink(), withUnmanagedBackgroundTaskStopReason(), redactDetectedSuccessfulRunProgressSummaryForBoard(), redactSuccessfulRunHandoffEvidence()

### Community 127 - "pipeline-conversation-context.ts"
Cohesion: 0.32
Nodes (7): fenceMarkdown(), formatPipelineConversationBodyDocumentContextMarkdown(), loadPipelineConversationBodyDocumentContext(), PIPELINE_CASE_BODY_CASE_DOCUMENT_KEY, PipelineConversationBodyDocumentContext, QueryableDb, truncateWithFlag()

### Community 128 - "upsertIssueWatchdogForIssue"
Cohesion: 0.29
Nodes (8): assertWatchdogAgentInvokable(), assertWatchedIssue(), isActiveTaskWatchdogUniqueConflict(), isIssueWatchdogUniqueConflict(), isUniqueConstraintConflict(), normalizeInstructions(), updateIssueWatchdogRow(), upsertIssueWatchdogForIssue()

### Community 129 - "google-workspace-connectors.ts"
Cohesion: 0.29
Nodes (3): GOOGLE_WORKSPACE_CONNECTOR_PROFILE_IDS, GOOGLE_WORKSPACE_CONNECTOR_PROFILES, GoogleWorkspaceConnectorProfileId

### Community 130 - "IssueCommentMetadataRowBase"
Cohesion: 0.29
Nodes (7): IssueCommentMetadataAgentLinkRow, IssueCommentMetadataCodeRow, IssueCommentMetadataIssueLinkRow, IssueCommentMetadataKeyValueRow, IssueCommentMetadataRowBase, IssueCommentMetadataRunLinkRow, IssueCommentMetadataTextRow

### Community 131 - "types/workspace-readiness.ts"
Cohesion: 0.29
Nodes (6): WORKSPACE_READINESS_STATES, WorkspaceLoginHandoffTicketResponse, WorkspaceReadiness, WorkspaceReadinessProbeResult, WorkspaceReadinessState, WorkspaceSeedReadinessState

### Community 132 - "TransactionScope"
Cohesion: 0.29
Nodes (4): createAdmissionTransactionScope(), requireAdmissionTx(), requireTransactionScopeTx(), TransactionScope

### Community 133 - "emitAgentTaskRun"
Cohesion: 0.48
Nodes (6): emitAgentTaskRun(), emitAgentTaskRunById(), HeartbeatRun, readNonEmptyString(), readUsageToken(), resolveDurationSeconds()

### Community 134 - "assessDelivery"
Cohesion: 0.29
Nodes (7): deriveExecutionWorkspaceDeliveryState(), assessDelivery(), listDeliveryPullRequestProducts(), listWorkspaceIssueTree(), issueTerminalTimestamp(), parseGitHubRepository(), pullRequestMatchesWorkspaceRepository()

### Community 135 - "assertRequestConfirmationResolutionAllowedUnderLock"
Cohesion: 0.33
Nodes (7): assertInteractionResolutionAllowed(), assertRequestConfirmationResolutionAllowedUnderLock(), isRequestConfirmationLikeKind(), assertIssueOpenForInteractionResolution(), isTerminalIssueStatus(), resolverActor(), shouldReturnAcceptedConfirmationToCreatorAgent()

### Community 136 - "listIssueBlockerAttentionMap"
Cohesion: 0.29
Nodes (7): appendBlockerAttentionEdges(), blockerSampleIdentifier(), createIssueBlockerAttention(), createIssueDependencyReadiness(), listIssueBlockerAttentionMap(), listIssueDependencyReadinessMap(), listPendingFinalizeBlockerIssueIds()

### Community 137 - "readStringFromRecord"
Cohesion: 0.33
Nodes (7): freshChatSourceAfterPublishedControl(), isTreeHoldInteractionCheckoutAllowed(), readChatWakeCommentIds(), readStringFromRecord(), resolveChatOriginPublicationBindings(), resolvePublishedInteractionPromptBindings(), resolveResponsibleUserIdForIssueCreate()

### Community 138 - "nextCronTickInTimeZone"
Cohesion: 0.33
Nodes (7): assertTimeZone(), floorToMinute(), getZonedMinuteFormatter(), getZonedMinuteParts(), isSubHourlyCronExpression(), matchesCronMinute(), nextCronTickInTimeZone()

### Community 139 - "statLocalCandidate"
Cohesion: 0.38
Nodes (7): contentTypeForPath(), listItemFromStat(), looksLikeText(), previewCapForKind(), previewKindForKnownContentType(), sniffUnknownPreviewKind(), statLocalCandidate()

### Community 140 - "routes/issue-tree-control.ts"
Cohesion: 0.47
Nodes (4): errorToMessage(), issueTreeControlRoutes(), RESUME_EXECUTABLE_STATUSES, waitForRunCancellationTasks()

### Community 141 - "issueListRequestKey"
Cohesion: 0.53
Nodes (6): issueListActorIdentity(), issueListClientIdentity(), issueListRequestKey(), normalizeIssueListCacheValue(), shortHash(), stableJson()

### Community 142 - "isRuntimeOwnedGitBranch"
Cohesion: 0.40
Nodes (5): GIT_BRANCH_OWNERSHIP_METADATA_KEY, GIT_BRANCH_OWNERSHIP_METADATA_VERSION, hasCurrentGitBranchOwnershipMetadata(), isRuntimeOwnedGitBranch(), restartDesiredRuntimeServicesOnStartup()

### Community 143 - "buildRunEventRuntimeProgress"
Cohesion: 0.67
Nodes (6): buildRunEventRuntimeProgress(), readFirstLiveRunProgressString(), readLiveRunAssistantSnippet(), readLiveRunProgressString(), readLiveRunToolName(), sanitizeLiveRunProgressText()

### Community 144 - "issueApprovalService"
Cohesion: 0.47
Nodes (5): issueApprovalService(), assertIssueAndApprovalSameCompany(), getApproval(), getIssue(), LinkActor

### Community 145 - "getIssueRelationSummaryMap"
Cohesion: 0.40
Nodes (6): getCurrentScheduledRetriesForIssues(), getCurrentScheduledRetryForIssue(), getIssueRelationSummaryMap(), withIssueRelationSummaries(), summarizeIssueRelationRow(), terminalExplicitBlockersByRoot()

### Community 146 - "adapter-login-lease.ts"
Cohesion: 0.40
Nodes (3): AcquireLoginLeaseArgs, BuildLoginLeaseAcquireArgsOptions, LoginLeaseMetadata

### Community 147 - "issueThreadInteractionResolutionError"
Cohesion: 0.60
Nodes (5): issueThreadInteractionResolutionError(), interactionAlreadyResolvedError(), interactionIssueClosedError(), interactionTerminalError(), getPendingInteractionForResolution()

### Community 148 - "pipeline-case-type.ts"
Cohesion: 0.67
Nodes (3): caseTypeMatchesPipeline(), CaseTypePipelineRef, deriveCaseType()

### Community 149 - "workspace-operation.ts"
Cohesion: 0.50
Nodes (3): WorkspaceOperation, WorkspaceOperationPhase, WorkspaceOperationStatus

### Community 150 - "buildIssueChanges"
Cohesion: 0.83
Nodes (3): buildIssueChanges(), canonicalIdArray(), truncateIssueChangeText()

### Community 151 - "issue-goal-fallback.ts"
Cohesion: 0.50
Nodes (3): MaybeId, resolveIssueGoalId(), resolveNextIssueGoalId()

### Community 152 - "buildPipelineCaseContextMarkdown"
Cohesion: 0.67
Nodes (4): buildPipelineCaseContextMarkdown(), buildPipelineStageEntryPreamble(), formatMarkdownContextScalar(), pipelineCaseFieldContextLines()

### Community 153 - "getAncestorCases"
Cohesion: 0.50
Nodes (4): getAncestorCases(), isCarryOverIdentityFieldKey(), inheritedBreakdownFields(), shouldCarryOverField()

### Community 155 - "reviewedFingerprintForWatchdogIssue"
Cohesion: 1.00
Nodes (3): normalizeStopFingerprint(), reviewedFingerprintForWatchdogIssue(), stopFingerprintFromText()

## Knowledge Gaps
- **1228 isolated node(s):** `agentTaskSessions`, `agentSessionGoalActions`, `environmentLeases`, `executionWorkspaceRuntimeLeases`, `heartbeatRunEvents` (+1223 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `issueService()` connect `issueService` to `services/heartbeat.ts`, `upsertIssueWatchdogForIssue`, `heartbeatService`, `issueRoutes`, `services/issues.ts`, `listIssueBlockerAttentionMap`, `readStringFromRecord`, `issue-execution-policy.ts`, `services/issue-tree-control.ts`, `routes/pipelines.ts`, `getIssueRelationSummaryMap`, `execution-workspace-policy.ts`, `issue-thread-interactions.ts`, `buildIssueChanges`, `issue-goal-fallback.ts`, `services/routines.ts`, `wake-queue/adapters/postgres.ts`, `heartbeat-run-summary.ts`, `routineService`, `task-watchdogs.ts`, `run-dispatch/adapters/postgres.ts`, `listBlockedInboxIssues`, `active-run-watchdog/adapters/postgres.ts`, `pipelineRoutes`, `issueThreadInteractionService`, `resolveWorkspaceForRun`, `readNonEmptyString`, `acceptRequestConfirmation`, `createPostgresRunDispatchAdapter`, `blockedInboxIssueConditions`, `createPostgresWatchdogAdapter`, `taskWatchdogService`, `task-search.ts`, `visibleIssueCondition`, `readExecutionWorkspaceConfig`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Why does `issueRoutes()` connect `issueRoutes` to `emitAgentTaskRun`, `routes/issues.ts`, `services/issues.ts`, `issueService`, `issue-execution-policy.ts`, `issueListRequestKey`, `enqueueWakeup`, `services/routines.ts`, `resolveTaskWatchdogMutationScope`, `routes/execution-workspaces.ts`, `QueuedCommentQueueTransaction`, `issueThreadInteractionService`, `issueRecoveryActionService`, `buildIssueSubtreeDiagnosticsResponse`, `readNonEmptyString`, `acceptRequestConfirmation`, `issue-dependency-wakeups.ts`, `issue-thread-interaction-resolution.ts`, `onboarding-first-task-assets.ts`, `cross-issue-influence-limit.ts`, `workspace-command-authz.ts`, `parseIssueExecutionState`, `issue-review-policy.ts`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Why does `heartbeatService()` connect `heartbeatService` to `services/heartbeat.ts`, `executeRun`, `issueService`, `readNonEmptyString`, `services/issue-tree-control.ts`, `wake-queue/index.ts`, `enqueueWakeup`, `services/routines.ts`, `heartbeat-run-summary.ts`, `routineService`, `run-dispatch/index.ts`, `executionWorkspaceService`, `workspace-operations.ts`, `heartbeat-run-runtime-status.ts`, `scheduleBoundedRetryForRun`, `resolveWorkspaceForRun`, `taskWatchdogService`, `resolveSessionBeforeForWakeup`, `evaluateSessionCompaction`, `deriveCommentId`, `handleSuccessfulRunHandoff`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 44 inferred relationships involving `heartbeatService()` (e.g. with `applyTaskDrain()` and `computeTaskDrain()`) actually correct?**
  _`heartbeatService()` has 44 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `issueRoutes()` (e.g. with `applyCreateIssueStatusDefault()` and `summarizeIssueRelationForActivity()`) actually correct?**
  _`issueRoutes()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `issueService()` (e.g. with `addStopRelayCommentIfNeeded()` and `archiveInbox()`) actually correct?**
  _`issueService()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `agentTaskSessions`, `agentSessionGoalActions`, `environmentLeases` to the rest of the system?**
  _1228 weakly-connected nodes found - possible documentation gaps or missing edges._