# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 59 files · ~127,751 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1310 nodes · 2523 edges · 67 communities (61 shown, 6 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 28 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- services/workspace-runtime.ts
- workspace-file-resources.ts
- routes/execution-workspaces.ts
- workspace-git-operation-scheduler.ts
- workspace-instance-cleanup.ts
- sandbox-provider-runtime.ts
- workspace-operations.ts
- sandbox-managed-runtime.ts
- runGit
- startRuntimeServicesForWorkspaceControlInvocation
- git-workspace-sync.ts
- types/workspace-runtime.ts
- services/execution-workspaces.ts
- local-process-sandbox.ts
- sandbox-callback-bridge.ts
- spawnLocalRuntimeService
- execution-workspace-policy.ts
- native-workspace-sync.ts
- executionWorkspaceService
- quarantineDirtyWorktreeBranchIncoherence
- prepareSandboxManagedRuntime
- workspace-restore-merge.ts
- execution-workspace.ts
- worktree-port-registry.ts
- types/workspace-file-resource.ts
- validators/workspace-file-resource.ts
- workspace-commands.ts
- plugin-runtime-sandbox.ts
- finalizePreparedRuntime
- LoginPtySession
- createCommandManagedSandboxCallbackBridgeQueueClient
- startSandboxCallbackBridgeWorker
- workspace-realization.ts
- recordWorkspaceCommandOperation
- execution_workspaces.ts
- readExecutionWorkspaceConfig
- sandbox-run-log-stream.ts
- loadEffectiveRuntimeServicesByExecutionWorkspace
- sandbox-orphan-cleanup-spool.ts
- run-site-sandbox.ts
- inspectExecutionWorkspaceBranchForReconcile
- legacy-controller-lease.ts
- createHandle
- services/workspace-readiness.ts
- native-chat-workspace.ts
- provider-trace-workspace-diff-reprojection.ts
- ensureServerWorkspaceLinksCurrent
- SandboxRunSite
- shellQuote
- google-workspace-connectors.ts
- types/workspace-readiness.ts
- assessDelivery
- GitWorkspaceSnapshot
- parseSandboxRemoteExecutionSpec
- workspace-restore-teardown.ts
- execution-workspace-guards.ts
- Issue Workspace Runtime Controls
- SandboxRunLogTailHandle
- adapter-login-lease.ts
- isRuntimeOwnedGitBranch
- resolveRuntimeServiceExposure
- PreparedNativeWorkspaceSync
- workspace-operation.ts
- SandboxHttp2BridgeGateway
- sandbox-install-command.ts
- session-workspace-cwd.ts
- resolveRuntimeProvision

## God Nodes (most connected - your core abstractions)
1. `executionWorkspaceService()` - 52 edges
2. `prepareSandboxManagedRuntime()` - 38 edges
3. `spawnLocalRuntimeService()` - 34 edges
4. `runGit()` - 26 edges
5. `WorkspaceGitOperationScheduler` - 22 edges
6. `startRuntimeServicesForWorkspaceControlInvocation()` - 20 edges
7. `prepareNativeWorkspaceSync()` - 19 edges
8. `handleExecutionWorkspaceRuntimeCommand()` - 18 edges
9. `readExecutionWorkspaceConfig()` - 18 edges
10. `ensurePersistedExecutionWorkspaceAvailable()` - 18 edges
11. `quarantineDirtyWorktreeBranchIncoherence()` - 17 edges
12. `realizeExecutionWorkspace()` - 17 edges
13. `ensureRuntimeServicesForRunInvocation()` - 17 edges
14. `executionWorkspaceRoutes()` - 15 edges
15. `availability()` - 15 edges

## Surprising Connections (you probably didn't know these)
- `readDescriptor()` --calls--> `parseDirectorySnapshot()`  [EXTRACTED]
  server/src/services/native-runtime/native-workspace-sync.ts → packages/adapter-utils/src/workspace-restore-merge.ts
- `finalizePreparedRuntime()` --calls--> `directorySnapshotSha256()`  [EXTRACTED]
  server/src/services/native-runtime/native-workspace-sync.ts → packages/adapter-utils/src/workspace-restore-merge.ts
- `finalizePreparedRuntime()` --calls--> `captureDirectorySnapshot()`  [EXTRACTED]
  server/src/services/native-runtime/native-workspace-sync.ts → packages/adapter-utils/src/workspace-restore-merge.ts
- `NativeWorkspaceSyncDescriptor` --references--> `GitWorkspaceSnapshot`  [EXTRACTED]
  server/src/services/native-runtime/native-workspace-sync.ts → packages/adapter-utils/src/git-workspace-sync.ts
- `PreparedNativeWorkspaceSync` --references--> `WorkspaceInboundMode`  [EXTRACTED]
  server/src/services/native-runtime/native-workspace-sync.ts → packages/adapter-utils/src/sandbox-managed-runtime.ts

## Import Cycles
- None detected.

## Communities (67 total, 6 thin omitted)

### Community 0 - "services/workspace-runtime.ts"
Cohesion: 0.02
Nodes (83): ACTIVE_RUNTIME_PORT_RESERVATION_STATUSES, allocateAndReserveExposure(), AuthoritativeBaseRefResolution, buildCompanyExposureReservationLedger(), buildDirtyQuarantineRescueBranch(), buildWorkspaceReadyMetadata(), defaultWorkspaceRuntimeExposureDeps(), detectPersistedExposureReservationDrift() (+75 more)

### Community 1 - "workspace-file-resources.ts"
Cohesion: 0.06
Nodes (75): AutoDiscovered, availabilityResult(), availableFileList(), candidateFromExecutionWorkspace(), candidateFromProjectWorkspace(), contentTypeForPath(), DENIED_SEGMENTS, denyReasonForPathSegments() (+67 more)

### Community 2 - "routes/execution-workspaces.ts"
Cohesion: 0.06
Nodes (64): baseWorkspaceDeclaresInstanceConfig(), canonicalRegularFile(), CanonicalWorktreeSeedSource, errorCode(), inspectDeclaredEntry(), readInstanceId(), RegisteredWorktreeSeedSourceInput, resolveCanonicalWorktreeSeedSource() (+56 more)

### Community 3 - "workspace-git-operation-scheduler.ts"
Cohesion: 0.07
Nodes (28): setExpensiveWorkspaceGitExecutor(), abortError(), CacheEntry, clampInteger(), createSpawnRunner(), envInteger(), envOptions, getWorkspaceGitOperationSchedulerSnapshot() (+20 more)

### Community 4 - "workspace-instance-cleanup.ts"
Cohesion: 0.07
Nodes (43): buildManagedWorkspaceGuestEnv(), isWorkspaceReadinessShape(), listManagedWorkspaceHandoffSubjects(), logManagedWorkspaceReadinessRejection(), ManagedWorkspaceIdentity, probeManagedWorkspaceHandoffSubjects(), probeManagedWorkspaceReadiness(), resolveManagedWorkspaceIdentity() (+35 more)

### Community 5 - "sandbox-provider-runtime.ts"
Cohesion: 0.07
Nodes (27): AcquireSandboxLeaseInput, acquireSandboxProviderLease(), assertProviderConfig(), buildFakeSandboxProbe(), DestroySandboxLeaseInput, destroySandboxProviderLease(), FakeSandboxProvider, findReusableSandboxProviderLeaseId() (+19 more)

### Community 6 - "workspace-operations.ts"
Cohesion: 0.06
Nodes (31): createLocalFileWorkspaceOperationLogStore(), ensureDir(), getWorkspaceOperationLogStore(), resolveWithin(), WorkspaceOperationLogFinalizeSummary, WorkspaceOperationLogHandle, WorkspaceOperationLogReadOptions, WorkspaceOperationLogReadResult (+23 more)

### Community 7 - "sandbox-managed-runtime.ts"
Cohesion: 0.07
Nodes (37): AdditionalSourceStagingFailure, buildUniqueStagingPath(), copyDurableSeedArchive(), copySelectedWorkspaceEntries(), copyWorkspaceEntry(), delay(), escapeTarExcludeLiteral(), execFile (+29 more)

### Community 8 - "runGit"
Cohesion: 0.12
Nodes (37): acquireGitWorktreeCleanupLock(), cleanupExecutionWorkspaceArtifacts(), deleteGitBranchAtVerifiedTip(), detectDefaultBranch(), detectGitWorktreeInProgressOperation(), directoryExists(), ensurePersistedExecutionWorkspaceAvailable(), findRegisteredGitWorktreeByBranch() (+29 more)

### Community 9 - "startRuntimeServicesForWorkspaceControlInvocation"
Cohesion: 0.14
Nodes (35): canRetryDeferredPortBindCollision(), cleanupPersistedExposureRows(), cleanupRecordExposure(), clearIdleTimer(), createRuntimeProvisionCoordinator(), decideStaleExposureReclaim(), discardFailedDeferredRuntimeStart(), ensureRuntimeServicesForRun() (+27 more)

### Community 10 - "git-workspace-sync.ts"
Cohesion: 0.10
Nodes (31): buildHardenedGitEnv(), buildRemoteGitDeltaBundleScript(), createImportedGitRef(), createRemoteGitExportRef(), createUnrelatedHistoryGraftCommit(), deleteLocalGitRef(), ExpensiveWorkspaceGitExecutor, ExpensiveWorkspaceGitInput (+23 more)

### Community 11 - "types/workspace-runtime.ts"
Cohesion: 0.06
Nodes (32): ExecutionWorkspaceCloseAction, ExecutionWorkspaceCloseActionKind, ExecutionWorkspaceCloseGitReadiness, ExecutionWorkspaceCloseLinkedIssue, ExecutionWorkspaceCloseReadiness, ExecutionWorkspaceCloseReadinessState, ExecutionWorkspaceConfig, ExecutionWorkspaceDeliveryState (+24 more)

### Community 12 - "services/execution-workspaces.ts"
Cohesion: 0.07
Nodes (31): assigneeMatchesExecutionPrincipal(), DbTransaction, EXECUTION_WORKSPACE_LIFECYCLE_GENERATION_METADATA_KEY, EXECUTION_WORKSPACE_REOPEN_FAILED_REASON, EXECUTION_WORKSPACE_REOPEN_PENDING_METADATA_KEY, EXECUTION_WORKSPACE_REOPEN_PENDING_SINCE_METADATA_KEY, ExecutionWorkspaceBranchReconcileActor, ExecutionWorkspaceBranchReconcileInspection (+23 more)

### Community 13 - "local-process-sandbox.ts"
Cohesion: 0.11
Nodes (28): addParentDirectories(), assertUnixSocketPathLength(), buildLocalProcessSandboxSpawnTarget(), connectProxyError(), createNetworkProxyBridge(), createNetworkProxyTempDir(), executableReadPaths(), isNetworkTargetAllowed() (+20 more)

### Community 14 - "sandbox-callback-bridge.ts"
Cohesion: 0.07
Nodes (20): authorizeSandboxCallbackBridgeRequestWithRoutes(), createSandboxCallbackBridgeAsset(), CreateSandboxHttp2BridgeGatewayOptions, DEFAULT_SANDBOX_CALLBACK_BRIDGE_HEADER_ALLOWLIST, DEFAULT_SANDBOX_CALLBACK_BRIDGE_MAX_BODY_BYTES, DEFAULT_SANDBOX_CALLBACK_BRIDGE_ROUTE_ALLOWLIST, getSandboxCallbackBridgeServerSource(), HTTP2_SANDBOX_CALLBACK_BRIDGE_ROUTE_ALLOWLIST (+12 more)

### Community 15 - "spawnLocalRuntimeService"
Cohesion: 0.10
Nodes (31): allocateIsolatedWorkspacePort(), allocateRuntimeServicePort(), buildExecutionWorkspaceCleanupEnv(), buildRuntimePortAllocationConflict(), buildTemplateData(), canBindRuntimePort(), claimRuntimeServiceBindPort(), classifyExposureHostCollisions() (+23 more)

### Community 16 - "execution-workspace-policy.ts"
Cohesion: 0.08
Nodes (17): buildExecutionWorkspaceAdapterConfig(), cloneRecord(), ExecutionWorkspaceEnvironmentResolution, ExecutionWorkspaceEnvironmentSource, hasReusableExecutionWorkspaceBinding(), isUnrunnableWorktreeCombo(), ManagedSandboxUnavailableError, ParsedExecutionWorkspaceMode (+9 more)

### Community 17 - "native-workspace-sync.ts"
Cohesion: 0.16
Nodes (25): directorySnapshotSha256(), serializeDirectorySnapshot(), classifyNativeWorkspaceInbound(), cleanupNativeWorkspaceSync(), descriptorDirectory(), descriptorPath(), durableSeedPaths(), ensurePrivateDirectory() (+17 more)

### Community 18 - "executionWorkspaceService"
Cohesion: 0.14
Nodes (21): acquireExecutionWorkspaceLifecycleLock(), assertBranchReconcileRuntimeServicesStopped(), assertBranchReconcileWorkspaceIsSafe(), bumpExecutionWorkspaceLifecycleGeneration(), clearMetadataReopenPendingConsumption(), executionWorkspaceService(), cleanupTerminalWorkspace(), clearReopenPendingConsumptionUnderLock() (+13 more)

### Community 19 - "quarantineDirtyWorktreeBranchIncoherence"
Cohesion: 0.13
Nodes (22): assertDirtyQuarantineRuntimeServicesStopped(), assertGitIndexIsUnlocked(), branchIncoherenceValidationFailure(), ensureGitWorktreeBranchCoherent(), executionWorkspaceUsesInheritedProjectRuntimeServices(), explainGitWorktreeBranchIncoherence(), findActiveRuntimeServiceBlockingDirtyQuarantine(), findGitWorktreeBranchContention() (+14 more)

### Community 20 - "prepareSandboxManagedRuntime"
Cohesion: 0.13
Nodes (12): assertRuntimeAssetKeyIsSafe(), assertSyncOperationsConfined(), createTarballFromDirectory(), emitRuntimeStatus(), makeTransferProgress(), mergeExcludes(), persistDurableSeedArchive(), prepareSandboxManagedRuntime() (+4 more)

### Community 21 - "workspace-restore-merge.ts"
Cohesion: 0.18
Nodes (19): acquireDirectoryMergeLock(), captureDirectorySnapshot(), copySnapshotEntry(), directoryEntryMatchesBaseline(), entriesMatch(), hashFile(), isLockStale(), isSafeSnapshotRelativePath() (+11 more)

### Community 22 - "execution-workspace.ts"
Cohesion: 0.10
Nodes (19): branchReconcileReasonSchema, executionWorkspaceCloseActionKindSchema, executionWorkspaceCloseActionSchema, executionWorkspaceCloseGitReadinessSchema, executionWorkspaceCloseLinkedIssueSchema, executionWorkspaceCloseReadinessSchema, executionWorkspaceCloseReadinessStateSchema, executionWorkspaceConfigSchema (+11 more)

### Community 23 - "worktree-port-registry.ts"
Cohesion: 0.19
Nodes (17): acquireRegistryLock(), isProcessAlive(), probeRegistryLockOwner(), readProcessIdentity(), readRegistryLockOwner(), RegistryLockLease, RegistryLockOwner, releaseRegistryLock() (+9 more)

### Community 24 - "types/workspace-file-resource.ts"
Cohesion: 0.11
Nodes (18): NormalizedWorkspaceFileAvailabilityQuery, ResolvedWorkspaceResource, WorkspaceFileAvailabilityQuery, WorkspaceFileAvailabilityRequest, WorkspaceFileAvailabilityResponse, WorkspaceFileAvailabilityResult, WorkspaceFileContent, WorkspaceFileContentEncoding (+10 more)

### Community 25 - "validators/workspace-file-resource.ts"
Cohesion: 0.11
Nodes (18): normalizedWorkspaceFileAvailabilityQuerySchema, resolvedWorkspaceResourceSchema, utf8ByteLength(), WorkspaceFileAvailabilityRequestInput, workspaceFileAvailabilityRequestSchema, workspaceFileAvailabilityResponseSchema, workspaceFileAvailabilityResultSchema, workspaceFileContentSchema (+10 more)

### Community 26 - "workspace-commands.ts"
Cohesion: 0.21
Nodes (16): WorkspaceCommandDefinition, WorkspaceRuntimeService, buildWorkspaceCommandDefinition(), deriveWorkspaceCommandId(), findWorkspaceCommandDefinition(), isRecord(), listWorkspaceCommandDefinitions(), listWorkspaceServiceCommandDefinitions() (+8 more)

### Community 27 - "plugin-runtime-sandbox.ts"
Cohesion: 0.17
Nodes (12): CapabilityScopedInvoker, DEFAULT_GLOBALS, isWithinRoot(), LoadedModule, loadPluginModuleInSandbox(), looksLikeEsm(), MODULE_PATH_SUFFIXES, normalizeModuleExports() (+4 more)

### Community 28 - "finalizePreparedRuntime"
Cohesion: 0.24
Nodes (14): readString(), record(), resumeNativeWorkspaceFinalization(), workspaceSyncFailure(), canonicalJson(), finalizedWorkspaceStamp(), finalizePreparedRuntime(), persistLeaseStamp() (+6 more)

### Community 29 - "LoginPtySession"
Cohesion: 0.15
Nodes (4): createLoginPtyTransport(), LoginPtySession, LoginPtySessionOpener, LoginPtyTransport

### Community 30 - "createCommandManagedSandboxCallbackBridgeQueueClient"
Cohesion: 0.29
Nodes (14): base64Chunks(), buildRemotePidLockAcquireScript(), buildRemotePidLockCleanupScript(), buildRunnerFailureMessage(), buildSandboxCallbackBridgeEnv(), createCommandManagedSandboxCallbackBridgeQueueClient(), normalizeTimeoutMs(), requireSuccessfulResult() (+6 more)

### Community 31 - "startSandboxCallbackBridgeWorker"
Cohesion: 0.22
Nodes (6): createFileSystemSandboxCallbackBridgeQueueClient(), pathExists(), SandboxCallbackBridgeQueueClient, startSandboxCallbackBridgeWorker(), withTimeout(), writeBridgeResponse()

### Community 32 - "workspace-realization.ts"
Cohesion: 0.36
Nodes (12): buildWorkspaceRealizationRecord(), buildWorkspaceRealizationRecordFromDriverInput(), buildWorkspaceRealizationRequest(), parseObject(), readAdditionalSources(), readNumber(), readPathAliases(), readString() (+4 more)

### Community 33 - "recordWorkspaceCommandOperation"
Cohesion: 0.18
Nodes (13): buildWorkspaceCommandEnv(), createProcessOutputCapture(), createProvisioningRuntimeServiceRecord(), executeProcess(), getGitWorktreeBranchAncestryVerdict(), quoteShellArg(), readWorkspaceSeedOperationEvidence(), recordWorkspaceCommandOperation() (+5 more)

### Community 34 - "execution_workspaces.ts"
Cohesion: 0.27
Nodes (6): environmentLeases, executionWorkspaceRuntimeLeases, executionWorkspaces, projectWorkspaces, workspaceOperations, workspaceRuntimeServices

### Community 35 - "readExecutionWorkspaceConfig"
Cohesion: 0.30
Nodes (12): assertLockedBranchReconcileWorkspaceStillMatchesInspection(), cloneRecord(), assertTerminalCleanupGitStateUnchanged(), hydrateWorkspace(), runTerminalWorkspaceCleanup(), isRecord(), mergeExecutionWorkspaceConfig(), readDesiredState() (+4 more)

### Community 36 - "sandbox-run-log-stream.ts"
Cohesion: 0.25
Nodes (8): createSandboxRunLogTailFactory(), normalizePositiveInt(), SandboxRunLogSink, SandboxRunLogTailFactory, SandboxRunLogTailFactoryOptions, TailStreamState, preferredShellForSandbox(), shellCommandArgs()

### Community 37 - "loadEffectiveRuntimeServicesByExecutionWorkspace"
Cohesion: 0.29
Nodes (10): loadEffectiveRuntimeServicesByExecutionWorkspace(), noActiveRuntimeServicesForWorkspaceCondition(), usesInheritedProjectRuntimeServices(), listCurrentRuntimeServicesForExecutionWorkspaces(), listCurrentRuntimeServicesForProjectWorkspaces(), runtimeServiceIdentityKey(), RuntimeServiceReadDb, selectConfiguredRuntimeServiceRows() (+2 more)

### Community 38 - "sandbox-orphan-cleanup-spool.ts"
Cohesion: 0.20
Nodes (4): createSandboxOrphanCleanupSpool(), DeferredOrphanCleanupRecord, resolveDefaultSpoolDir(), SandboxOrphanCleanupSpool

### Community 39 - "run-site-sandbox.ts"
Cohesion: 0.29
Nodes (9): createSandboxRunSite(), ManagedHomeSeamResult, SandboxRunSiteOptions, SandboxRunSiteTransport, StagedRuntimeStoreEntry, StagedWorkspace, StageWorkspace, withStagingLease() (+1 more)

### Community 40 - "inspectExecutionWorkspaceBranchForReconcile"
Cohesion: 0.27
Nodes (10): execFileAsync, explainGitWorktreeBranchReconcileInspection(), getGitWorktreeBranchAncestryVerdict(), inspectExecutionWorkspaceBranchForReconcile(), inspectGitCloseReadiness(), pathExists(), readGitStdout(), resolveLocalBranchCommit() (+2 more)

### Community 41 - "legacy-controller-lease.ts"
Cohesion: 0.22
Nodes (6): LEGACY_CONTROLLER_LEASE_MS, LEGACY_CONTROLLER_RENEW_MS, legacyControllerBootId, renewLegacyControllerLease(), Run, watchLegacyControllerLease()

### Community 42 - "createHandle"
Cohesion: 0.36
Nodes (8): createHandle(), buildTickScript(), emitBytes(), loop(), parseTickOutput(), sleep(), tick(), decodeBase64Section()

### Community 43 - "services/workspace-readiness.ts"
Cohesion: 0.33
Nodes (7): isManagedWorkspaceInstance(), readSeedManifestSummary(), resolveWorkspaceReadiness(), resolveWorkspaceReadinessState(), resolveWorkspaceSeedMarkerDir(), SeedManifestSummary, WorkspaceReadinessDeps

### Community 44 - "native-chat-workspace.ts"
Cohesion: 0.32
Nodes (5): findNativeChatWorkspaceScope(), materializeNativeChatTaskRoot(), NativeChatProjectWorkspace, NativeChatWorkspaceScope, segment()

### Community 45 - "provider-trace-workspace-diff-reprojection.ts"
Cohesion: 0.36
Nodes (7): persistReprojectedWorkspaceDiffs(), projectCodexWorkspaceDiffsFromTrace(), record(), stableTurnId(), WorkspaceDiffPayload, WorkspaceDiffReprojectionSkipReason, WorkspaceDiffTraceProjection

### Community 46 - "ensureServerWorkspaceLinksCurrent"
Cohesion: 0.29
Nodes (8): discoverWorkspacePackagePaths(), visit(), ensureServerWorkspaceLinksCurrent(), findServerWorkspaceLinkMismatches(), findWorkspaceRoot(), isLinkedGitWorktreeCheckout(), readJsonFile(), runWorkspaceJobForControl()

### Community 48 - "shellQuote"
Cohesion: 0.38
Nodes (7): buildDefaultExtractRuntimeAssetCommand(), buildRemoveDeletedPathsCommand(), buildWorkspaceTarExtractCommand(), createRemoteTarballFromDirectoryCommand(), preserveFindArgs(), shellQuote(), tarExcludeFlags()

### Community 49 - "google-workspace-connectors.ts"
Cohesion: 0.29
Nodes (3): GOOGLE_WORKSPACE_CONNECTOR_PROFILE_IDS, GOOGLE_WORKSPACE_CONNECTOR_PROFILES, GoogleWorkspaceConnectorProfileId

### Community 50 - "types/workspace-readiness.ts"
Cohesion: 0.29
Nodes (6): WORKSPACE_READINESS_STATES, WorkspaceLoginHandoffTicketResponse, WorkspaceReadiness, WorkspaceReadinessProbeResult, WorkspaceReadinessState, WorkspaceSeedReadinessState

### Community 51 - "assessDelivery"
Cohesion: 0.29
Nodes (7): deriveExecutionWorkspaceDeliveryState(), assessDelivery(), listDeliveryPullRequestProducts(), listWorkspaceIssueTree(), issueTerminalTimestamp(), parseGitHubRepository(), pullRequestMatchesWorkspaceRepository()

### Community 52 - "GitWorkspaceSnapshot"
Cohesion: 0.33
Nodes (5): GitWorkspaceSnapshot, PreparedSandboxManagedRuntime, DirectorySnapshot, SerializedDirectorySnapshot, NativeWorkspaceSyncDescriptor

### Community 53 - "parseSandboxRemoteExecutionSpec"
Cohesion: 0.40
Nodes (6): asNumber(), asObject(), asString(), buildSandboxExecutionSessionIdentity(), parseSandboxRemoteExecutionSpec(), sandboxExecutionSessionMatches()

### Community 54 - "workspace-restore-teardown.ts"
Cohesion: 0.53
Nodes (4): classifyWorkspaceRestoreFailure(), describeWorkspaceRestoreFailure(), createWorkspaceRestoreTeardown(), WorkspaceRestoreTeardownRuntime

### Community 55 - "execution-workspace-guards.ts"
Cohesion: 0.33
Nodes (3): CLOSED_EXECUTION_WORKSPACE_STATUSES, ExecutionWorkspaceGuardTarget, ExecutionWorkspace

### Community 56 - "Issue Workspace Runtime Controls"
Cohesion: 0.33
Nodes (5): Control Services, Discover the Workspace, Issue Workspace Runtime Controls, MCP Tools, Read the URL

### Community 58 - "adapter-login-lease.ts"
Cohesion: 0.40
Nodes (3): AcquireLoginLeaseArgs, BuildLoginLeaseAcquireArgsOptions, LoginLeaseMetadata

### Community 59 - "isRuntimeOwnedGitBranch"
Cohesion: 0.50
Nodes (4): GIT_BRANCH_OWNERSHIP_METADATA_KEY, GIT_BRANCH_OWNERSHIP_METADATA_VERSION, hasCurrentGitBranchOwnershipMetadata(), isRuntimeOwnedGitBranch()

### Community 60 - "resolveRuntimeServiceExposure"
Cohesion: 0.40
Nodes (5): anyRuntimeServiceUsesHttpsExposure(), decideManagedRuntimeExposureBackfill(), isManagedHttpsDefaultCandidate(), resolveManagedRuntimeHttpsMode(), resolveRuntimeServiceExposure()

### Community 62 - "workspace-operation.ts"
Cohesion: 0.50
Nodes (3): WorkspaceOperation, WorkspaceOperationPhase, WorkspaceOperationStatus

### Community 66 - "resolveRuntimeProvision"
Cohesion: 1.00
Nodes (3): readRuntimeProvisionCommand(), resolveRuntimeProvision(), resolveRuntimeProvisionCommand()

## Knowledge Gaps
- **376 isolated node(s):** `StageWorkspace`, `SandboxRunSiteOptions`, `SandboxRunSiteTransport`, `GitCommandResult`, `ExpensiveWorkspaceGitInput` (+371 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WorkspaceGitOperationScheduler` connect `workspace-git-operation-scheduler.ts` to `services/workspace-runtime.ts`, `workspace-file-resources.ts`, `services/execution-workspaces.ts`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Why does `executionWorkspaceService()` connect `executionWorkspaceService` to `services/workspace-runtime.ts`, `routes/execution-workspaces.ts`, `readExecutionWorkspaceConfig`, `loadEffectiveRuntimeServicesByExecutionWorkspace`, `workspace-operations.ts`, `inspectExecutionWorkspaceBranchForReconcile`, `services/execution-workspaces.ts`, `assessDelivery`, `quarantineDirtyWorktreeBranchIncoherence`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **What connects `StageWorkspace`, `SandboxRunSiteOptions`, `SandboxRunSiteTransport` to the rest of the system?**
  _376 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `services/workspace-runtime.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.02456140350877193 - nodes in this community are weakly interconnected._
- **Should `workspace-file-resources.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.05860805860805861 - nodes in this community are weakly interconnected._
- **Should `routes/execution-workspaces.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.05859969558599695 - nodes in this community are weakly interconnected._
- **Should `workspace-git-operation-scheduler.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.07312925170068027 - nodes in this community are weakly interconnected._