# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 285 files · ~486,585 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 4245 nodes · 11456 edges · 155 communities (147 shown, 8 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 129 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- heartbeat.ts
- server-utils.ts
- heartbeatService
- acpx-engine/execute.ts
- readPaperclipRuntimeSkillEntries
- gateway/server/execute.ts
- execution-target.ts
- openclaw-gateway/src/server/execute.ts
- hermes/src/server/execute.ts
- opencode-local/src/server/execute.ts
- adapter-utils/src/index.ts
- http2-bridge-server.ts
- sandbox-managed-runtime.ts
- client.ts
- native-session-executor.ts
- codex-local/src/server/execute.ts
- executeRun
- readNonEmptyString
- ssh.ts
- run-contracts.ts
- sandbox-callback-bridge.ts
- claude-local/src/server/execute.ts
- pi-local/src/server/execute.ts
- codex-local/src/server/quota.ts
- tool_access.ts
- command-managed-runtime.ts
- grok-local/src/server/index.ts
- kimi-local/src/server/execute.ts
- settlement-sequence.ts
- grok-local/src/server/execute.ts
- duplex-observability.ts
- printAcpxStreamEvent
- agentService
- cursor-local/src/server/execute.ts
- claude-local/src/server/quota.ts
- startup-timing.ts
- codex-home.ts
- device-login-service.ts
- gemini-local/src/server/execute.ts
- codex-local/src/server/index.ts
- run-site-host.ts
- git-workspace-sync.ts
- claude-local/src/server/acp.ts
- ensureAdapterExecutionTargetCommandResolvable
- claude-local/src/server/test.ts
- claude-local/src/server/index.ts
- codex-auth-cache.ts
- buildAdapterEnvConfig
- codex-local/src/server/acp.ts
- execution-workspaces.ts
- createDuplexReadinessGate
- gemini-local/src/server/acp.ts
- kimi-local/src/server/acp.ts
- workspace-restore-merge.ts
- local-process-sandbox.ts
- prepareCodexSkillRuntime
- codex-local/src/index.ts
- run-dispatch/adapters/postgres.ts
- native-question-bridge.ts
- createRunnerdBackendWithinSessionClaim
- device-login-export.ts
- paperclip-runner-permissions.ts
- gemini-local/src/ui/parse-stdout.ts
- executionWorkspaceService
- migrateRunnerdStateRootForExecution
- acpx-engine/constants.ts
- duplex-frame-codec.ts
- parseAcpxStdoutLine
- scheduleBoundedRetryForRun
- record
- remote-managed-runtime.ts
- setup-token-parse.ts
- run-coordinator.ts
- resolveWorkspaceForRun
- appendRunEvent
- kimi-local/src/index.ts
- wake-queue/adapters/postgres.ts
- .execute
- bridge-transport-contract.ts
- TranscriptEntry
- codex-local/src/server/runtime-config.ts
- resolveSessionBeforeForWakeup
- reconcileRetainedNativeSessionCleanup
- createPostgresWatchdogAdapter
- device-login-reaper.ts
- claude-config.ts
- createDeviceLoginService
- session-compaction.ts
- AdapterSessionCodec
- codex-local/src/server/test.ts
- LoginPtySession
- remote-command.ts
- grok-local/src/ui/parse-stdout.ts
- workspace-runtime-leases.ts
- AdapterAuthSessionStore
- claude-local/src/server/models.ts
- readExecutionWorkspaceConfig
- runTurn
- command-redaction.ts
- codex-local/src/ui/parse-stdout.ts
- cursor-local/src/ui/parse-stdout.ts
- openclaw-gateway/src/ui/parse-stdout.ts
- opencode-local/src/ui/parse-stdout.ts
- observeSandboxDelete
- runner-connectivity.ts
- resolvePaperclipInstanceRootForAdapter
- probe-diagnostics.ts
- cursor-cloud/src/ui/parse-stdout.ts
- cursor-local/src/cli/format-event.ts
- codex-local/src/server/parse.ts
- gateway/ui/parse-stdout.ts
- inspectExecutionWorkspaceBranchForReconcile
- loadWarmNativeCheckpoint
- RuntimeProgressSink
- createHandle
- evaluateSessionCompaction
- probe-env.ts
- opencode-local/src/cli/format-event.ts
- handleSuccessfulRunHandoff
- RunSite
- mcp-isolation-harness.ts
- claude-local/src/index.ts
- pi-local/src/cli/format-event.ts
- pi-local/src/server/runtime-config.ts
- buildOwnerResponse
- assessDelivery
- setup-token-reaper.ts
- createRuntimeProgressReporter
- codex-auth-merge-scripts.ts
- buildRunEventRuntimeProgress
- CodexOutputInactivityMonitorHandle
- grok-local/src/cli/format-event.ts
- openclaw-gateway/src/index.ts
- adapter_auth_sessions.ts
- claimPendingCleanupCapWarning
- native-safe-replacement.ts
- cursor-cloud/src/index.ts
- gateway/cli/index.ts
- hermes/src/cli/format-event.ts
- openclaw-gateway/src/cli/format-event.ts
- usesInheritedProjectRuntimeServices
- Adapter Authoring Notes
- managed_agent_profiles.ts
- remote_agent_profiles.ts

## God Nodes (most connected - your core abstractions)
1. `heartbeatService()` - 189 edges
2. `asString()` - 163 edges
3. `executeRun()` - 150 edges
4. `parseObject()` - 134 edges
5. `readNonEmptyString()` - 100 edges
6. `execute()` - 85 edges
7. `asNumber()` - 83 edges
8. `execute()` - 70 edges
9. `createAcpxEngineExecutor()` - 62 edges
10. `execute()` - 59 edges
11. `startAdapterExecutionTargetPaperclipBridge()` - 57 edges
12. `execute()` - 56 edges
13. `execute()` - 55 edges
14. `execute()` - 54 edges
15. `execute()` - 54 edges

## Surprising Connections (you probably didn't know these)
- `executeRun()` --calls--> `cleanupGitHubOperationLaunchers()`  [EXTRACTED]
  server/src/services/heartbeat.ts → packages/adapter-utils/src/execution-target.ts
- `executeRun()` --calls--> `prepareGitHubExecutionEnvironment()`  [EXTRACTED]
  server/src/services/heartbeat.ts → packages/adapter-utils/src/execution-target.ts
- `executeRun()` --calls--> `prepareGitHubOperationLaunchers()`  [EXTRACTED]
  server/src/services/heartbeat.ts → packages/adapter-utils/src/execution-target.ts
- `executeRun()` --calls--> `startAdapterExecutionTargetPaperclipBridge()`  [EXTRACTED]
  server/src/services/heartbeat.ts → packages/adapter-utils/src/execution-target.ts
- `executeRun()` --calls--> `githubBrokerEnvironment()`  [EXTRACTED]
  server/src/services/heartbeat.ts → packages/adapter-utils/src/github-launcher.ts

## Import Cycles
- 3-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 3-file cycle: `packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts`
- 3-file cycle: `packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts`
- 4-file cycle: `packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/sandbox-callback-bridge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts`
- 4-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 4-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 4-file cycle: `packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts`
- 4-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 4-file cycle: `packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts`
- 5-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/sandbox-callback-bridge.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 5-file cycle: `packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/http2-bridge-server.ts -> packages/adapter-utils/src/sandbox-callback-bridge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts`
- 5-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/sandbox-managed-runtime.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 5-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 5-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/http2-bridge-server.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 5-file cycle: `packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/remote-managed-runtime.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts`
- 5-file cycle: `packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/sandbox-managed-runtime.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts`
- 5-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/sandbox-run-log-stream.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 5-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/command-managed-runtime.ts`
- 5-file cycle: `packages/adapter-utils/src/execution-target.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/execution-target.ts`
- 5-file cycle: `packages/adapter-utils/src/command-managed-runtime.ts -> packages/adapter-utils/src/workspace-restore-merge.ts -> packages/adapter-utils/src/server-utils.ts -> packages/adapter-utils/src/types.ts -> packages/adapter-utils/src/ssh.ts -> packages/adapter-utils/src/command-managed-runtime.ts`

## Communities (155 total, 8 thin omitted)

### Community 0 - "heartbeat.ts"
Cohesion: 0.01
Nodes (165): AcceptedPlanWakeRoutingDecision, ACTIVE_RUN_LOG_RUNTIME_STATUS_REFRESH_INTERVAL_MS, ACTIVE_RUN_OUTPUT_PROGRESS_FLUSH_INTERVAL_MS, activeRunExecutionPromises, activeRunExecutions, activeWakeupPromises, adapterSupportsManagedMcpConfig(), applyTaskDrain() (+157 more)

### Community 1 - "server-utils.ts"
Cohesion: 0.03
Nodes (127): isCompatibleSession(), PaperclipChatFilePreparationDelivery, acquireMaterializeLock(), asBoolean(), asNumber(), ASSIGNMENT_SHAPED_PAPERCLIP_WAKE_REASONS, asString(), ChildProcessWithEvents (+119 more)

### Community 2 - "heartbeatService"
Cohesion: 0.05
Nodes (90): buildProcessLossMessage(), cancelHeartbeatNativeRun(), computeWorkspaceBusyRetryDelayMs(), heartbeatService(), acknowledgeRemoteStop(), applyRunDispatchPostCommitEffects(), applyWakeQueuePostCommitEffects(), buildRunLivenessInput() (+82 more)

### Community 3 - "acpx-engine/execute.ts"
Cohesion: 0.04
Nodes (91): ACPX_INHERITED_HOST_ENV_KEYS, ACPX_INHERITED_PROVIDER_ENV_KEYS, AcpxEngineBillingIdentity, AcpxEngineSettings, AcpxExecutionPhase, AcpxHandshakeTimeoutError, AcpxHandshakeTransportLostError, AcpxRuntimeFactory (+83 more)

### Community 4 - "readPaperclipRuntimeSkillEntries"
Cohesion: 0.06
Nodes (82): resolveSelectedRuntimeSkills(), buildManagedSkillOrigin(), buildPersistentSkillSnapshot(), buildRuntimeMountedSkillSnapshot(), canonicalizeDesiredPaperclipSkillReference(), ensurePaperclipSkillSymlink(), isPaperclipSkillSourceMissing(), readInstalledSkillTargets() (+74 more)

### Community 5 - "gateway/server/execute.ts"
Cohesion: 0.06
Nodes (83): agentConfigurationDoc, createServerAdapter(), label, models, sessionManagement, type, getConfigSchema(), apiUrl() (+75 more)

### Community 6 - "execution-target.ts"
Cohesion: 0.04
Nodes (77): RFC-9113, mapHttp2EventToDuplexLossReason(), AdapterCommandCapableExecutionTarget, adapterExecutionTargetCommandRunner(), adapterExecutionTargetFromRemoteExecution(), AdapterExecutionTargetProcessOptions, adapterExecutionTargetShellCommand(), adapterExecutionTargetTimeoutMs() (+69 more)

### Community 7 - "openclaw-gateway/src/server/execute.ts"
Cohesion: 0.05
Nodes (73): appendWakeText(), asRecord(), autoApproveDevicePairing(), base64UrlEncode(), buildAgentParams(), buildDeviceAuthPayloadV3(), buildPaperclipEnvForWake(), buildWakePayload() (+65 more)

### Community 8 - "hermes/src/server/execute.ts"
Cohesion: 0.06
Nodes (61): UsageSummary, agentConfigurationDoc, createServerAdapter(), getRuntimeCommandSpec(), label, models, sessionManagement, type (+53 more)

### Community 9 - "opencode-local/src/server/execute.ts"
Cohesion: 0.07
Nodes (63): disposeFreshStagedRuntime(), adapterExecutionTargetSessionIdentity(), adapterExecutionTargetSessionMatches(), ensureAdapterExecutionTargetRuntimeCommandInstalled(), overrideAdapterExecutionTargetRemoteCwd(), readAdapterExecutionTargetHomeDir(), runAdapterExecutionTargetShellCommand(), isPaperclipRecoveryWakePayload() (+55 more)

### Community 10 - "adapter-utils/src/index.ts"
Cohesion: 0.05
Nodes (59): ADAPTER_LOGIN_COMPLETION_CLAIMS, ADAPTER_LOGIN_PANEL_MODES, ADAPTER_LOGIN_TIMEOUT_POLICIES, AdapterLoginCapability, AdapterLoginCompletionClaim, AdapterLoginCompletionContext, AdapterLoginPanelMode, AdapterLoginTimeoutPolicy (+51 more)

### Community 11 - "http2-bridge-server.ts"
Cohesion: 0.04
Nodes (56): bridgeResponseBodyLimitError(), readBridgeForwardResponseBody(), BridgeBodyReservation, BridgeProcessCapacityError, BridgeRouteBodyLedger, CanonicalBridgeRequestPath, CanonicalBridgeRequestPathRejection, CanonicalBridgeRequestPathResult (+48 more)

### Community 12 - "sandbox-managed-runtime.ts"
Cohesion: 0.05
Nodes (57): asNumber(), asObject(), assertRuntimeAssetKeyIsSafe(), assertSyncOperationsConfined(), asString(), buildDefaultExtractRuntimeAssetCommand(), buildRemoveDeletedPathsCommand(), buildSandboxExecutionSessionIdentity() (+49 more)

### Community 13 - "client.ts"
Cohesion: 0.06
Nodes (66): applyPendingMigrations(), applyPendingMigrationsManually(), clientFinalizer, clientsByHostPort, closeRegisteredClients(), columnExists(), columnHasDataType(), constraintExists() (+58 more)

### Community 14 - "native-session-executor.ts"
Cohesion: 0.04
Nodes (58): ActiveNativeSession, activeNativeSessions, cancelNativeSession(), CLEANUP_CANONICAL_FILES, closeIdleWarmNativeSessions(), closeIdleWarmNativeSessionsForRestart(), closeWarmNativeSessionsForEnvironment(), CODEX_HOME_NON_PERSISTENT_ENTRIES (+50 more)

### Community 15 - "codex-local/src/server/execute.ts"
Cohesion: 0.06
Nodes (61): parseLocalProcessFilesystemScope(), parseLocalProcessNetworkScope(), parseLocalProcessSandboxExtraPaths(), prepareCodexRemoteManagedHome(), resolveCodexExecutionEngineForRun(), resolveCodexAuthPrecedence(), buildCodexAuthInboundProvision(), mergeManagedCodexMcpGateways() (+53 more)

### Community 16 - "executeRun"
Cohesion: 0.04
Nodes (62): appendWithByteCap(), normalizePaperclipOperationalSkillPreference(), readPaperclipSkillSyncPreference(), writePaperclipSkillSyncPreference(), appendExcerpt(), applyRunScopedMentionedSkillKeys(), attachPaperclipSessionMetadataToSessionParams(), attestReviewedExternalChatRun() (+54 more)

### Community 17 - "readNonEmptyString"
Cohesion: 0.05
Nodes (62): assertGitSensitiveAdapterWorkspaceValid(), assertPushCapabilityCheckoutValid(), buildPaperclipWakePayload(), buildSandboxProviderPluginNotReadyResultJson(), buildUnresolvedWorkspaceBaseRefResultJson(), clearInteractionContinuationWakeContext(), enrichWakeContextSnapshot(), externalAttachmentOmissionNotice() (+54 more)

### Community 18 - "ssh.ts"
Cohesion: 0.08
Nodes (59): buildDuplexGatewayLaunchArgv(), ensureSandboxRunLogDirectory(), allocateLoopbackPort(), buildKnownHostsEntry(), buildSshEnvLabFixtureConfig(), buildSshSpawnTarget(), clearLocalDirectory(), clearRemoteDirectory() (+51 more)

### Community 19 - "run-contracts.ts"
Cohesion: 0.05
Nodes (51): AcpxPreparedRuntime, AcpxRemoteManagedHomeContext, AcpxRemoteManagedHomeResult, StagedRuntimeCacheEntry, AcpRuntimeResource, AcpxNonInteractivePermissions, AcpxPermissionMode, AcpxRunMode (+43 more)

### Community 20 - "sandbox-callback-bridge.ts"
Cohesion: 0.06
Nodes (41): runWithoutActiveStep(), authorizeSandboxCallbackBridgeRequestWithRoutes(), base64Chunks(), buildRemotePidLockAcquireScript(), buildRemotePidLockCleanupScript(), buildRunnerFailureMessage(), buildSandboxCallbackBridgeEnv(), createCommandManagedSandboxCallbackBridgeQueueClient() (+33 more)

### Community 21 - "claude-local/src/server/execute.ts"
Cohesion: 0.10
Nodes (55): buildRuntime(), adapterExecutionTargetRemoteCwd(), readAdapterExecutionTarget(), applyPaperclipWorkspaceEnv(), buildInvocationEnvForLogs(), buildPaperclipEnv(), ensureAbsoluteDirectory(), isForbiddenConfigEnvKey() (+47 more)

### Community 22 - "pi-local/src/server/execute.ts"
Cohesion: 0.07
Nodes (51): inferOpenAiCompatibleBiller(), readEnv(), adapterExecutionTargetIsRemote(), ensureAdapterExecutionTargetFile(), appendWithCap(), removeMaintainerOnlySkillSymlinks(), resolveProcessGroupId(), resumeReadable() (+43 more)

### Community 23 - "codex-local/src/server/quota.ts"
Cohesion: 0.07
Nodes (43): QuotaWindow, main(), parseArgs(), ProbeArgs, quotaErrorFamilyJson(), stringifyError(), classifyCodexAuthRefreshFailure(), CodexAuthRefreshFailureClass (+35 more)

### Community 24 - "tool_access.ts"
Cohesion: 0.06
Nodes (39): agentConfigRevisions, agentRuntimeState, agentSessionGoalActions, agentTaskSessions, agents, completionContracts, costEvents, executionWorkspaceRuntimeLeases (+31 more)

### Community 25 - "command-managed-runtime.ts"
Cohesion: 0.07
Nodes (35): assertPostUploadCommandsConfined(), base64EncodedLength(), bestEffortRemoveRemotePath(), bufferToArrayBuffer(), buildSyncInChmodCommand(), buildSyncInExtractDirectoryCommand(), buildUniqueStagingPath(), CommandManagedRuntimeAsset (+27 more)

### Community 26 - "grok-local/src/server/index.ts"
Cohesion: 0.08
Nodes (41): assertUsableGrokAuthShape(), checkStagedGrokCredentialReadiness(), CredentialReadinessResult, DeviceLoginReadinessError, ExistingHomeState, isEnoentError(), promoteGrokDeviceLoginCredential(), PromoteGrokDeviceLoginCredentialInput (+33 more)

### Community 27 - "kimi-local/src/server/execute.ts"
Cohesion: 0.10
Nodes (42): adapterExecutionTargetUsesManagedHome(), adapterExecutionTargetUsesPaperclipBridge(), resolveAdapterExecutionTargetTimeout(), resolveAdapterExecutionTargetTimeoutSec(), asStringArray(), buildRuntimeToolsEnv(), modelSupportsEffort(), resolveKimiThinkingEffort() (+34 more)

### Community 28 - "settlement-sequence.ts"
Cohesion: 0.07
Nodes (26): AcquiredRunResources, CleanupScope, LedgerStateError, ResourceDisposition, ResourceId, RunResourcePayloads, RunResourceRegistration, RunSiteKind (+18 more)

### Community 29 - "grok-local/src/server/execute.ts"
Cohesion: 0.08
Nodes (43): DEFAULT_PAPERCLIP_AGENT_PROMPT_TEMPLATE, DEFAULT_PAPERCLIP_CONVERSATION_PROMPT_TEMPLATE, hashSkillDirectory(), joinPromptSections(), materializedSkillFingerprintMatches(), materializePaperclipSkillCopy(), renderPaperclipWakePrompt(), renderTemplate() (+35 more)

### Community 30 - "duplex-observability.ts"
Cohesion: 0.05
Nodes (34): APPROVED_PROVIDERS, createDuplexObservability(), DUPLEX_APPROVED_PROVIDER, DUPLEX_COUNTER_CHANNEL_OPEN_TOTAL, DUPLEX_COUNTER_FALLBACK_TOTAL, DUPLEX_COUNTER_LOSS_TOTAL, DUPLEX_COUNTER_SESSION_LEAK_TOTAL, DUPLEX_DIMENSION_KEYS (+26 more)

### Community 31 - "printAcpxStreamEvent"
Cohesion: 0.10
Nodes (31): asNumber(), asString(), parseJson(), pickToolUseId(), printAcpxStreamEvent(), statusLine(), stringify(), execute (+23 more)

### Community 32 - "agentService"
Cohesion: 0.09
Nodes (43): AgentConfigSnapshot, agentService(), assertBuiltInAgentMetadataMutationAllowed(), assertCompanyShortnameAvailable(), assertNoCycle(), currentUtcMonthWindow(), enforceClaudeOAuthBindingClaim(), ensureManager() (+35 more)

### Community 33 - "cursor-local/src/server/execute.ts"
Cohesion: 0.10
Nodes (37): adapterExecutionTargetDuplexObservabilityRecorder(), adapterExecutionTargetEnablesSandboxDuplexBridge(), defaultPathForPlatform(), ensurePathInEnv(), agentConfigurationDoc, CURSOR_FALLBACK_MODEL_IDS, DEFAULT_CURSOR_LOCAL_MODEL, label (+29 more)

### Community 34 - "claude-local/src/server/quota.ts"
Cohesion: 0.11
Nodes (41): main(), parseArgs(), ProbeArgs, stringifyError(), AnthropicExtraUsage, AnthropicUsageResponse, AnthropicUsageWindow, buildClaudeCliShellProbeCommand() (+33 more)

### Community 35 - "startup-timing.ts"
Cohesion: 0.08
Nodes (37): ActiveStepContext, activeStepContextStorage, buildActiveStepContext(), buildStepEvent(), BUILT_IN_PROVIDER_FAMILIES, clampSpanLabel(), createRuntimeSpanRunner(), emitSkippedStartupStep() (+29 more)

### Community 36 - "codex-home.ts"
Cohesion: 0.09
Nodes (38): buildManagedMcpBlock(), CODEX_SYNC_ALLOWLIST, CodexCredentialAuthMode, CodexCredentialReadiness, CodexCredentialReadinessInput, codexHomeHasMatchingApiKeyAuth(), codexHomeHasUsableAuth(), COPIED_SHARED_FILES (+30 more)

### Community 37 - "device-login-service.ts"
Cohesion: 0.06
Nodes (33): AcquireLoginLeaseInput, ADAPTER_AUTH_PROMOTION_CLAIM_MS, AdapterAuthSessionConflictError, AdapterAuthSessionRow, adapterLoginPromotionLockKey(), CompareAndSetAdapterAuthSessionStatusInput, createWorkerBoundLoginPtyOpener(), CredentialPromotionContext (+25 more)

### Community 38 - "gemini-local/src/server/execute.ts"
Cohesion: 0.14
Nodes (31): ensureAdapterExecutionTargetDirectory(), resolveGeminiExecutionEngineForRun(), buildGeminiHeadlessEnv(), buildGeminiRuntimeEnv(), ensureGeminiSkillsInjected(), execute(), executeGeminiAcp, hasNonEmptyEnvValue() (+23 more)

### Community 39 - "codex-local/src/server/index.ts"
Cohesion: 0.10
Nodes (27): checkStagedCredentialReadiness(), CredentialReadinessResult, DeviceLoginReadinessError, PromoteDeviceLoginCredentialInput, PromoteDeviceLoginCredentialOutcome, PromoteDeviceLoginCredentialResult, requireSafeCompanyId(), CODEX_SANDBOX_AUTH_EXISTS_COMMAND (+19 more)

### Community 40 - "run-site-host.ts"
Cohesion: 0.10
Nodes (17): AcpRunContext, HostReuseCandidate, PlacedWorkspace, SessionReuseStore, SitePlan, AcpxAgentProcessIdentity, AcpxProcessIdentitySink, ChildStderrState (+9 more)

### Community 41 - "git-workspace-sync.ts"
Cohesion: 0.10
Nodes (30): buildHardenedGitEnv(), buildRemoteGitDeltaBundleScript(), createImportedGitRef(), createRemoteGitExportRef(), createUnrelatedHistoryGraftCommit(), deleteLocalGitRef(), ExpensiveWorkspaceGitExecutor, ExpensiveWorkspaceGitInput (+22 more)

### Community 42 - "claude-local/src/server/acp.ts"
Cohesion: 0.10
Nodes (31): buildAcpLoginProbeUnavailableCheck(), buildClaudeAcpConfig(), ClaudeAcpExecutor, ClaudeAcpExecutorOptions, claudeAcpUnavailableReason(), ClaudeEngineResolutionInput, ClaudeEngineSelection, ClaudeExecutionEngine (+23 more)

### Community 43 - "ensureAdapterExecutionTargetCommandResolvable"
Cohesion: 0.11
Nodes (29): stageAcpRemoteRuntime(), describeAdapterExecutionTarget(), ensureAdapterExecutionTargetCommandResolvable(), ensureSandboxCommandResolvable(), maybeRunSandboxInstallCommand(), prepareAdapterExecutionTargetRuntime(), probeSandboxCommandResolvable(), requireSandboxRunner() (+21 more)

### Community 44 - "claude-local/src/server/test.ts"
Cohesion: 0.14
Nodes (29): adapterExecutionTargetToRemoteSpec(), resolveAdapterExecutionTargetCommandForLogs(), runAdapterExecutionTargetProcess(), resolveClaudeModel(), resolveClaudeExecutionEngineForRun(), testClaudeAcpEnvironment(), prepareSandboxClaudeProbeRuntime(), cacheKeyForTarget() (+21 more)

### Community 45 - "claude-local/src/server/index.ts"
Cohesion: 0.11
Nodes (24): LoginRunnerDisposable, LoginRunnerLifecycleOptions, LoginRunnerLog, LoginRunnerOutcome, LoginRunnerRaceResult, LoginRunnerResult, raceLoginRunnerExit(), resetClaudeCliCapabilitiesCacheForTests() (+16 more)

### Community 46 - "codex-auth-cache.ts"
Cohesion: 0.13
Nodes (29): withDirectoryMergeLock(), assertAccountHomeCacheDirStillValid(), clearCodexAuthCache(), clearCodexAuthCacheEntry(), CODEX_AUTH_CACHE_OFF_SWITCH_ENV, ensureCodexAuthCacheEntryDir(), ensureCodexAuthCacheEntryDirExclusive(), EnsureCodexAuthCacheEntryDirExclusiveResult (+21 more)

### Community 47 - "buildAdapterEnvConfig"
Cohesion: 0.11
Nodes (20): buildAdapterEnvConfig(), isVersionSelector(), parseEnvBindings(), parseEnvVars(), CreateConfigValues, buildClaudeLocalConfig(), parseCommaArgs(), parseJsonObject() (+12 more)

### Community 48 - "codex-local/src/server/acp.ts"
Cohesion: 0.12
Nodes (30): buildCodexAcpConfig(), CodexAcpExecutor, CodexAcpExecutorOptions, codexAcpUnavailableReason(), CodexEngineResolutionInput, CodexEngineSelection, CodexExecutionEngine, commandIsResolvable() (+22 more)

### Community 49 - "execution-workspaces.ts"
Cohesion: 0.07
Nodes (30): assigneeMatchesExecutionPrincipal(), DbTransaction, EXECUTION_WORKSPACE_LIFECYCLE_GENERATION_METADATA_KEY, EXECUTION_WORKSPACE_REOPEN_FAILED_REASON, EXECUTION_WORKSPACE_REOPEN_PENDING_METADATA_KEY, EXECUTION_WORKSPACE_REOPEN_PENDING_SINCE_METADATA_KEY, ExecutionWorkspaceBranchReconcileActor, ExecutionWorkspaceBranchReconcileInspection (+22 more)

### Community 50 - "createDuplexReadinessGate"
Cohesion: 0.10
Nodes (17): CommandManagedDuplexChannel, closeDuplexChannelWithinBudget(), createDuplexReadinessGate(), finish(), createGrowableByteBuffer(), createHttp2PrefaceScanningChannel(), deliver(), overflowAndStop() (+9 more)

### Community 51 - "gemini-local/src/server/acp.ts"
Cohesion: 0.12
Nodes (29): buildGeminiAcpConfig(), commandIsResolvable(), createGeminiAcpExecutor(), findCommandOnPath(), firstNonEmptyString(), firstShellToken(), GeminiAcpExecutor, GeminiAcpExecutorOptions (+21 more)

### Community 52 - "kimi-local/src/server/acp.ts"
Cohesion: 0.13
Nodes (27): buildKimiAcpConfig(), commandIsResolvable(), createKimiAcpExecutor(), findCommandOnPath(), firstNonEmptyString(), firstShellToken(), hasPathSeparator(), isNonEmpty() (+19 more)

### Community 53 - "workspace-restore-merge.ts"
Cohesion: 0.13
Nodes (25): excludePatternMatches(), isRelativePathOrDescendant(), pathContainsSegmentOrDescendant(), shouldExcludePath(), acquireDirectoryMergeLock(), captureDirectorySnapshot(), copySnapshotEntry(), directoryEntryMatchesBaseline() (+17 more)

### Community 54 - "local-process-sandbox.ts"
Cohesion: 0.13
Nodes (26): addParentDirectories(), assertUnixSocketPathLength(), buildLocalProcessSandboxSpawnTarget(), connectProxyError(), createNetworkProxyBridge(), createNetworkProxyTempDir(), executableReadPaths(), isNetworkTargetAllowed() (+18 more)

### Community 55 - "prepareCodexSkillRuntime"
Cohesion: 0.09
Nodes (26): buildSkillSetKey(), defaultPaperclipInstanceDir(), defaultStateDir(), ensureCopiedFile(), ensureParentDir(), ensureSymlink(), findAncestorBin(), hashPathContents() (+18 more)

### Community 56 - "codex-local/src/index.ts"
Cohesion: 0.12
Nodes (24): PAPERCLIP_RUNNER_DEFAULT_MODELS, agentConfigurationDoc, CODEX_LOCAL_ASTRA_REASONING_EFFORTS, CODEX_LOCAL_DEFAULT_REASONING_EFFORTS, CODEX_LOCAL_FAST_MODE_SUPPORTED_MODELS, CODEX_LOCAL_MODEL_ALIASES, CodexLocalReasoningEffort, codexLocalReasoningEffortsForModel() (+16 more)

### Community 57 - "run-dispatch/adapters/postgres.ts"
Cohesion: 0.15
Nodes (24): buildReviewParticipantFacts(), CancelSuppressedRetryInput, CancelSuppressedRetryResult, classifyRetryReasonKind(), createPostgresRunDispatchAdapter(), cancelStaleQueuedRun(), cancelStaleRunInTx(), cancelSuppressedRetryInTx() (+16 more)

### Community 58 - "native-question-bridge.ts"
Cohesion: 0.13
Nodes (24): activeTargets, authorizedNativeRun(), canonicalResponse(), DbTransaction, deliverNativeQuestionResponse(), deliverNativeQuestionResponseDurably(), flushNativeQuestionResponses(), NATIVE_QUESTION_CANCELLATION_CONTEXT_KEY (+16 more)

### Community 59 - "createRunnerdBackendWithinSessionClaim"
Cohesion: 0.14
Nodes (26): assertRemoteRunnerBuildMetadata(), buildNativeHarnessBackupManifest(), buildRemoteCodexLauncherCommand(), canonicalJson(), compatibleNativeHarnessBackupManifests(), createRunnerdBackendWithinSessionClaim(), digestBackupDirectory(), harnessBackupCandidates() (+18 more)

### Community 60 - "device-login-export.ts"
Cohesion: 0.17
Nodes (23): promoteDeviceLoginCredential(), readSubscriptionAccountId(), writeCodexAuthCacheEntry(), copyBackCodexAuth(), CopyBackCodexAuthInput, CopyBackCodexAuthOutcome, resolveManagedCodexHomeDir(), assertAuthPathIsRegularOrAbsent() (+15 more)

### Community 61 - "paperclip-runner-permissions.ts"
Cohesion: 0.14
Nodes (21): AcpxPermissionMode, CodexPermissionMode, isPaperclipRunnerProvider(), normalizeLegacyRunnerProvider(), OpenCodePermissionMode, PAPERCLIP_RUNNER_IDLE_TIMEOUT_DEFAULT_MS, PAPERCLIP_RUNNER_IDLE_TIMEOUT_MAX_MS, PAPERCLIP_RUNNER_PERMISSION_CAPABILITIES (+13 more)

### Community 62 - "gemini-local/src/ui/parse-stdout.ts"
Cohesion: 0.18
Nodes (20): agentConfigurationDoc, DEFAULT_GEMINI_LOCAL_MODEL, label, models, SANDBOX_INSTALL_COMMAND, type, buildGeminiLocalConfig(), parseCommaArgs() (+12 more)

### Community 63 - "executionWorkspaceService"
Cohesion: 0.14
Nodes (21): acquireExecutionWorkspaceLifecycleLock(), assertBranchReconcileRuntimeServicesStopped(), assertBranchReconcileWorkspaceIsSafe(), bumpExecutionWorkspaceLifecycleGeneration(), clearMetadataReopenPendingConsumption(), executionWorkspaceService(), cleanupTerminalWorkspace(), clearReopenPendingConsumptionUnderLock() (+13 more)

### Community 64 - "migrateRunnerdStateRootForExecution"
Cohesion: 0.20
Nodes (24): assertRetainedNativeSourceArchiveSettled(), cleanupArchiveRootIdentity(), cleanupCanonicalVacancy(), durableIdentityMatchesExecution(), durableIdentityMatchesSession(), isSafeNativeStateDirectory(), legacyCompanyRunnerdStateRoot(), legacyRunnerdStateRoot() (+16 more)

### Community 65 - "acpx-engine/constants.ts"
Cohesion: 0.12
Nodes (18): ACPX_ADAPTER_AGENT_IDS, ACPX_DUPLEX_LOSS_CANCEL_DEADLINE_MS, ACPX_HANDSHAKE_TIMEOUT_MS, ACPX_HANDSHAKE_TRANSPORT_POLL_MS, AcpxAdapterType, AcpxAgentId, DEFAULT_ACP_ENGINE_AGENT, DEFAULT_ACP_ENGINE_MODE (+10 more)

### Community 66 - "duplex-frame-codec.ts"
Cohesion: 0.14
Nodes (20): decodeDuplexLine(), DEFAULT_MAX_DUPLEX_FRAME_BYTES, DUPLEX_FRAME_VERSION, DuplexCloseFrame, DuplexDecodeResult, DuplexEncodeResult, DuplexErrorFrame, DuplexFrame (+12 more)

### Community 67 - "parseAcpxStdoutLine"
Cohesion: 0.19
Nodes (19): asNumber(), asRecord(), asString(), parseAcpxStdoutLine(), parseJson(), pickToolUseId(), statusText(), stringify() (+11 more)

### Community 68 - "scheduleBoundedRetryForRun"
Cohesion: 0.13
Nodes (22): computeBoundedTransientHeartbeatRetrySchedule(), addPlanApprovalResumeFailureCommentOnce(), buildPlanApprovalResumeFailureComment(), buildPlanApprovalResumeFailureResult(), enqueueMissingIssueCommentRetry(), escalatePlanApprovalResumeFailureNeedsAttention(), getAcceptedPlanApprovalInteractionForRun(), getActiveRecoveryActionId() (+14 more)

### Community 69 - "record"
Cohesion: 0.14
Nodes (22): clearNativeRuntimeRequestResolutions(), clearSteeringDeliveries(), createGovernedWaitEventObservation(), executePaperclipNativeSession(), executePaperclipNativeSessionWithinScope(), materializeRuntimeQuestionFallback(), nativeConversationReplyResult(), nativeProviderRecoveryEvidence() (+14 more)

### Community 70 - "remote-managed-runtime.ts"
Cohesion: 0.14
Nodes (19): GIT_ARCHIVE_EXCLUDES, asNumber(), asObject(), asString(), buildRemoteExecutionSessionIdentity(), PreparedRemoteManagedRuntime, prepareRemoteManagedRuntime(), readRemoteFile() (+11 more)

### Community 71 - "setup-token-parse.ts"
Cohesion: 0.14
Nodes (20): findBrowserCodePrompt(), hasValidQuery(), isValidRedirectUri(), isValidScope(), parseSetupTokenCredential(), parseSetupTokenPrompt(), reassembleUrl(), SETUP_TOKEN_AFTER_ANCHOR (+12 more)

### Community 72 - "run-coordinator.ts"
Cohesion: 0.16
Nodes (12): AcpxEngineExecutorOptions, ConsumedRunResources, PreTurnFailedCause, StartupReady, StartupResult, finalizedReport(), ReproducibleOutcome, runAttempt() (+4 more)

### Community 73 - "resolveWorkspaceForRun"
Cohesion: 0.13
Nodes (20): assertGitWorktreeBaseWorkspaceReady(), buildAnchorFallbackWorkspaceNotes(), defaultAdditionalProjectWorkspaceDeps(), deriveRepoNameFromRepoUrl(), ensureManagedProjectWorkspace(), execFile, resolveAnchorWorkspaceForRun(), resolveWorkspaceForRun() (+12 more)

### Community 74 - "appendRunEvent"
Cohesion: 0.12
Nodes (20): decorateHeartbeatRunRuntimeStatus(), appendRunEvent(), clearDetachedRunWarning(), finalizeIssueCommentPolicy(), findRunIssueComment(), hasDeferredIssueCommentWake(), isServerStdioBoundHotRestartRun(), patchRunIssueCommentStatus() (+12 more)

### Community 75 - "kimi-local/src/index.ts"
Cohesion: 0.14
Nodes (15): buildSandboxNpmInstallCommand(), shellSingleQuote(), agentConfigurationDoc, DEFAULT_KIMI_LOCAL_MODEL, EFFORT_CAPABLE_MODELS, KIMI_SUPPORTED_EFFORTS, KimiEffort, label (+7 more)

### Community 76 - "wake-queue/adapters/postgres.ts"
Cohesion: 0.11
Nodes (6): EXECUTION_PATH_HEARTBEAT_RUN_STATUSES, HeartbeatRunRow, IssueRow, toDeferredWakeCandidate(), toRequestedByActorType(), WakeQueuePostgresAdapterDeps

### Community 77 - ".execute"
Cohesion: 0.15
Nodes (14): archiveExcludeArgs(), assertSafeExtractedCheckpoint(), assertSafeRemoteCheckpointArchive(), cleanupRemoteRunnerAfterIdentityFailure(), createRemoteRunnerProcessLauncher(), parseRemoteRunnerProcessIdentity(), processEnvironment(), readRemoteRunnerState() (+6 more)

### Community 78 - "bridge-transport-contract.ts"
Cohesion: 0.14
Nodes (10): RFC-7231, DEFAULT_DUPLEX_BROKER_BUDGETS, DUPLEX_CHANNEL_LOST_ERROR_CODE, DuplexBrokerBudgets, DuplexBrokerRunDisposition, isSafeBridgeMethod(), SAFE_BRIDGE_METHODS, DuplexLossReason (+2 more)

### Community 79 - "TranscriptEntry"
Cohesion: 0.16
Nodes (14): HOME_PATH_PATTERNS, HomePathRedactionOptions, isPlainObject(), REDACTED_HOME_PATH_USER, redactHomePathUserSegments(), redactHomePathUserSegmentsInValue(), redactTranscriptEntryPaths(), TranscriptEntry (+6 more)

### Community 80 - "codex-local/src/server/runtime-config.ts"
Cohesion: 0.24
Nodes (17): buildMergedConfigToml(), configTomlBackupPath(), emitProviderTable(), escapeTomlString(), expandEnvPlaceholders(), isPlainObject(), parseCodexProvidersConfig(), ParsedCodexProvidersConfig (+9 more)

### Community 81 - "resolveSessionBeforeForWakeup"
Cohesion: 0.20
Nodes (18): buildExplicitResumeSessionOverride(), deriveTaskKey(), deriveTaskKeyWithHeartbeatFallback(), describeSessionResetReason(), getAdapterSessionCodec(), getTaskSession(), hasResolvablePriorSessionWorkspaceForWake(), hasResolvableSessionWorkspaceCwd() (+10 more)

### Community 82 - "reconcileRetainedNativeSessionCleanup"
Cohesion: 0.25
Nodes (18): appendRetainedNativeCleanupEvent(), assertCleanupActivationCommitted(), buildNativeProviderEnvironment(), cleanupProcessAbsent(), cleanupProviderHomeSnapshot(), cleanupStateSnapshot(), copyCleanupProviderHome(), createRunnerdBackend() (+10 more)

### Community 83 - "createPostgresWatchdogAdapter"
Cohesion: 0.16
Nodes (11): createPostgresWatchdogAdapter(), findCandidateSilentRuns(), findEvaluationIssueById(), findOpenStaleRunEvaluation(), findRunForCompany(), findSourceIssue(), selectEvaluationIssueSnapshot(), isRecoveryOriginKind() (+3 more)

### Community 84 - "device-login-reaper.ts"
Cohesion: 0.13
Nodes (11): DeviceLoginReaper, DeviceLoginReaperDeps, LoginLeaseRef, ProductionLoginSessionReaperRuntimeDeps, ReaperSweepResult, TaggedLease, ADAPTER_AUTH_ACTIVE_STATUSES, AdapterAuthReaperStore (+3 more)

### Community 85 - "claude-config.ts"
Cohesion: 0.23
Nodes (15): AdapterExecutionTargetShellOptions, buildSeedSnapshotKey(), collectSeedFiles(), isAlreadyExistsError(), isNonEmptyString(), materializeSeedSnapshot(), nonEmpty(), pathExists() (+7 more)

### Community 86 - "createDeviceLoginService"
Cohesion: 0.19
Nodes (10): AdapterLoginPrompt, createDeviceLoginService(), abandonAfterLostClaim(), cancelOwnerSession(), readOwnerSession(), runLogin(), conditionalTransition(), terminate() (+2 more)

### Community 87 - "session-compaction.ts"
Cohesion: 0.17
Nodes (15): ADAPTER_MANAGED_SESSION_POLICY, ADAPTER_SESSION_MANAGEMENT, AdapterSessionManagement, DEFAULT_SESSION_COMPACTION_POLICY, getAdapterSessionManagement(), isRecord(), LEGACY_SESSIONED_ADAPTER_TYPES, NativeContextManagement (+7 more)

### Community 88 - "AdapterSessionCodec"
Cohesion: 0.21
Nodes (10): AdapterSessionCodec, asRecord(), normalize(), readRepos(), readString(), sessionCodec, asStringEnvMap(), looksLikeRepoUrl() (+2 more)

### Community 89 - "codex-local/src/server/test.ts"
Cohesion: 0.26
Nodes (13): resolveAdapterExecutionTargetCwd(), isCodexAuthCacheEnabled(), selectVendCredential(), prepareManagedCodexHome(), parseCodexJsonl(), codexHomeDir(), commandLooksLike(), firstNonEmptyLine() (+5 more)

### Community 90 - "LoginPtySession"
Cohesion: 0.14
Nodes (5): createLoginPtyTransport(), LoginPtySession, LoginPtySessionOpener, LoginPtyTransport, buildSandboxLoginDriver()

### Community 91 - "remote-command.ts"
Cohesion: 0.22
Nodes (14): candidateSandboxCommandPaths(), candidateSandboxPathEntries(), commandBasename(), CURSOR_SANDBOX_BIN_DIRS, DEFAULT_CURSOR_COMMAND_BASENAMES, hasPathSeparator(), preferredSandboxCommandBasenames(), prepareCursorSandboxCommand() (+6 more)

### Community 92 - "grok-local/src/ui/parse-stdout.ts"
Cohesion: 0.30
Nodes (12): applyTurnBoundary(), countBackticks(), createTurnBoundaryState(), endsWithSentenceClose(), TurnBoundaryState, asRecord(), asString(), createGrokStdoutParser() (+4 more)

### Community 93 - "workspace-runtime-leases.ts"
Cohesion: 0.14
Nodes (12): evaluateStaleOwner(), ExecutionWorkspaceRuntimeLeaseRow, LEASED_WORKSPACE_RUNTIME_ACTIONS, LeaseTx, parseOwnerKey(), TERMINAL_HEARTBEAT_RUN_STATUSES, WORKSPACE_RUNTIME_ELIGIBLE_ISSUE_STATUSES, WORKSPACE_RUNTIME_LEASE_TTL_MS (+4 more)

### Community 94 - "AdapterAuthSessionStore"
Cohesion: 0.15
Nodes (5): AdapterAuthSessionStore, resolveProfile(), start(), LoginSessionLease, LoginSessionRuntime

### Community 95 - "claude-local/src/server/models.ts"
Cohesion: 0.29
Nodes (12): BEDROCK_MODELS, dedupeModels(), fetchAnthropicModels(), fingerprint(), isBedrockEnv(), listClaudeModels(), loadClaudeModels(), mergedWithFallback() (+4 more)

### Community 96 - "readExecutionWorkspaceConfig"
Cohesion: 0.27
Nodes (13): assertLockedBranchReconcileWorkspaceStillMatchesInspection(), cloneRecord(), assertTerminalCleanupGitStateUnchanged(), hydrateWorkspace(), runTerminalWorkspaceCleanup(), isRecord(), mergeExecutionWorkspaceConfig(), readDesiredState() (+5 more)

### Community 97 - "runTurn"
Cohesion: 0.27
Nodes (5): TurnCompletion, runTurn(), StartedTurn, TurnFinalizeInput, TurnSteps

### Community 98 - "command-redaction.ts"
Cohesion: 0.20
Nodes (11): COMMAND_CLI_SECRET_OPTION_RE, COMMAND_ENV_SECRET_ASSIGNMENT_RE, COMMAND_SECRET_HINTS, JSON_ESCAPED_SECRET_FIELD_RE, JSON_SECRET_FIELD_RE, maybeContainsSecretText(), redactCommandText(), redactDiagnosticText() (+3 more)

### Community 99 - "codex-local/src/ui/parse-stdout.ts"
Cohesion: 0.45
Nodes (11): asNumber(), asRecord(), asString(), errorText(), parseCodexItem(), parseCodexStdoutLine(), parseCommandExecutionItem(), parseFileChangeItem() (+3 more)

### Community 100 - "cursor-local/src/ui/parse-stdout.ts"
Cohesion: 0.56
Nodes (11): asNumber(), asRecord(), asString(), compactShellToolInput(), formatShellToolResultForLog(), parseAssistantMessage(), parseCursorStdoutLine(), parseCursorToolCallEvent() (+3 more)

### Community 101 - "openclaw-gateway/src/ui/parse-stdout.ts"
Cohesion: 0.30
Nodes (8): normalizeOpenClawGatewayStreamLine(), buildOpenClawGatewayConfig(), parseJsonObject(), asRecord(), asString(), parseAgentEventLine(), parseOpenClawGatewayStdoutLine(), safeJsonParse()

### Community 102 - "opencode-local/src/ui/parse-stdout.ts"
Cohesion: 0.36
Nodes (9): buildOpenCodeLocalConfig(), parseCommaArgs(), asNumber(), asRecord(), asString(), errorText(), parseOpenCodeStdoutLine(), parseToolUse() (+1 more)

### Community 103 - "observeSandboxDelete"
Cohesion: 0.29
Nodes (10): createDeviceLoginReaper(), sweep(), sweepCleanupPending(), sweepExpiredSessions(), sweepOrphanLeases(), LoginSessionCleanupRuntime, encodePendingTerminal(), isConfirmedDelete() (+2 more)

### Community 104 - "runner-connectivity.ts"
Cohesion: 0.24
Nodes (9): buildDirectRunnerConnectUrl(), connectPath(), PAPERCLIP_RUNNER_CONNECT_PATH_PREFIX, PAPERCLIP_RUNNER_INGRESS_PORT, PaperclipRunnerTransport, PaperclipRunnerTransportError, resolvePaperclipRunnerTransport(), RunnerIngressAuthorization (+1 more)

### Community 105 - "resolvePaperclipInstanceRootForAdapter"
Cohesion: 0.29
Nodes (10): expandHomePrefix(), resolvePaperclipInstanceRootForAdapter(), buildClaudePromptBundleKey(), ClaudePromptBundle, ensureReadableFile(), hashPathContents(), nonEmpty(), prepareClaudePromptBundle() (+2 more)

### Community 106 - "probe-diagnostics.ts"
Cohesion: 0.20
Nodes (10): buildAcpAuthMissingChecks(), ADAPTER_TEST_HOST_TARGET_LABEL, ALLOWED_LOGIN_URL_HOST_SUFFIXES, buildClaudeLoginRequiredHint(), classifyThrownErrorClass(), normalizeClaudeLoginUrl(), resolveAdapterTestTargetLabel(), SandboxProbeDiagnosticClassification (+2 more)

### Community 107 - "cursor-cloud/src/ui/parse-stdout.ts"
Cohesion: 0.42
Nodes (8): printCursorCloudEvent(), asRecord(), asString(), parseAssistantMessage(), parseCursorCloudStdoutLine(), parseSdkMessage(), safeJsonParse(), stringifyUnknown()

### Community 108 - "cursor-local/src/cli/format-event.ts"
Cohesion: 0.55
Nodes (9): asNumber(), asRecord(), asString(), printAssistantMessage(), printCursorStreamEvent(), printLegacyToolEvent(), printToolCallEventTopLevel(), printUserMessage() (+1 more)

### Community 109 - "codex-local/src/server/parse.ts"
Cohesion: 0.44
Nodes (9): buildCodexErrorHaystack(), dateFromTimeZoneWallClock(), extractCodexRetryNotBefore(), isCodexProviderQuotaError(), isCodexTransientUpstreamError(), nextClockTimeInTimeZone(), normalizeResetTimeZone(), parseLocalClockTime() (+1 more)

### Community 110 - "gateway/ui/parse-stdout.ts"
Cohesion: 0.42
Nodes (7): asRecord(), asString(), extractDirectReasoningText(), extractReasoningText(), parseHermesGatewayStdoutLine(), safeJsonParse(), stripAnsi()

### Community 111 - "inspectExecutionWorkspaceBranchForReconcile"
Cohesion: 0.27
Nodes (10): execFileAsync, explainGitWorktreeBranchReconcileInspection(), getGitWorktreeBranchAncestryVerdict(), inspectExecutionWorkspaceBranchForReconcile(), inspectGitCloseReadiness(), pathExists(), readGitStdout(), resolveLocalBranchCommit() (+2 more)

### Community 112 - "loadWarmNativeCheckpoint"
Cohesion: 0.27
Nodes (10): hasIdleWarmNativeSessionOwner(), legacyCompanyNativeSessionCheckpointPath(), legacyCompanyNativeSessionScopeKey(), legacyNativeSessionCheckpointPath(), loadWarmNativeCheckpoint(), nativeSessionCheckpointDirectory(), nativeSessionCheckpointPath(), nativeSessionConfigDigest() (+2 more)

### Community 113 - "RuntimeProgressSink"
Cohesion: 0.33
Nodes (5): RuntimeProgressSink, classifyWorkspaceRestoreFailure(), describeWorkspaceRestoreFailure(), createWorkspaceRestoreTeardown(), WorkspaceRestoreTeardownRuntime

### Community 114 - "createHandle"
Cohesion: 0.36
Nodes (8): createHandle(), buildTickScript(), emitBytes(), loop(), parseTickOutput(), sleep(), tick(), decodeBase64Section()

### Community 115 - "evaluateSessionCompaction"
Cohesion: 0.22
Nodes (9): hasSessionCompactionThresholds(), deriveNormalizedUsageDelta(), formatCount(), evaluateSessionCompaction(), getLatestRunForSession(), getOldestRunForSession(), resolveNormalizedUsageForSession(), readRawUsageTotals() (+1 more)

### Community 116 - "probe-env.ts"
Cohesion: 0.31
Nodes (8): buildLocalAdapterTestProbeEnv(), isNonEmptyString(), LOCAL_PROBE_ALLOWED_CALLER_ENV_KEYS, LocalProbeEnvironment, PROXY_ENV_KEYS, readCaseInsensitive(), resolveTrustedExecutable(), WINDOWS_INTERPRETER_ENV_KEYS

### Community 117 - "opencode-local/src/cli/format-event.ts"
Cohesion: 0.54
Nodes (6): asNumber(), asRecord(), asString(), errorText(), printOpenCodeStreamEvent(), safeJsonParse()

### Community 118 - "handleSuccessfulRunHandoff"
Cohesion: 0.29
Nodes (8): addSuccessfulRunHandoffCommentOnce(), buildDetectedSuccessfulRunProgressSummary(), handleSuccessfulRunHandoff(), hasUnmanagedBackgroundTaskEvidence(), issueUiLink(), withUnmanagedBackgroundTaskStopReason(), redactDetectedSuccessfulRunProgressSummaryForBoard(), redactSuccessfulRunHandoffEvidence()

### Community 120 - "mcp-isolation-harness.ts"
Cohesion: 0.33
Nodes (3): CommandResult, commandVersion(), runCommand()

### Community 121 - "claude-local/src/index.ts"
Cohesion: 0.29
Nodes (6): agentConfigurationDoc, DEFAULT_CLAUDE_LOCAL_MODEL, label, models, SANDBOX_INSTALL_COMMAND, type

### Community 122 - "pi-local/src/cli/format-event.ts"
Cohesion: 0.52
Nodes (5): asRecord(), asString(), extractTextContent(), printPiStreamEvent(), safeJsonParse()

### Community 123 - "pi-local/src/server/runtime-config.ts"
Cohesion: 0.48
Nodes (6): expandEnvPlaceholders(), isPlainObject(), ParsedProviderConfig, parseProviderConfig(), PreparedPiRuntimeConfig, preparePiRuntimeConfig()

### Community 124 - "buildOwnerResponse"
Cohesion: 0.33
Nodes (5): buildFailure(), buildOwnerResponse(), readActiveOwnerSession(), decodePendingTerminal(), resolvePublicStatus()

### Community 125 - "assessDelivery"
Cohesion: 0.29
Nodes (7): deriveExecutionWorkspaceDeliveryState(), assessDelivery(), listDeliveryPullRequestProducts(), listWorkspaceIssueTree(), issueTerminalTimestamp(), parseGitHubRepository(), pullRequestMatchesWorkspaceRepository()

### Community 126 - "setup-token-reaper.ts"
Cohesion: 0.33
Nodes (5): createProductionSetupTokenReaper(), createSetupTokenReaper(), ProductionSetupTokenReaperDeps, SetupTokenReaper, SetupTokenReaperDeps

### Community 127 - "createRuntimeProgressReporter"
Cohesion: 0.53
Nodes (6): clampPercent(), createRuntimeProgressReporter(), buildFailLine(), buildLine(), emit(), formatMb()

### Community 128 - "codex-auth-merge-scripts.ts"
Cohesion: 0.33
Nodes (5): SandboxManagedRuntimeAssetProvision, CODEX_AUTH_MERGE_DECISION_SCRIPT_BYTES, CODEX_AUTH_MERGE_DECISION_SCRIPT_NAME, CODEX_AUTH_MERGE_EXTRACT_SCRIPT_BYTES, CODEX_AUTH_MERGE_EXTRACT_SCRIPT_NAME

### Community 129 - "buildRunEventRuntimeProgress"
Cohesion: 0.67
Nodes (6): buildRunEventRuntimeProgress(), readFirstLiveRunProgressString(), readLiveRunAssistantSnippet(), readLiveRunProgressString(), readLiveRunToolName(), sanitizeLiveRunProgressText()

### Community 131 - "grok-local/src/cli/format-event.ts"
Cohesion: 0.70
Nodes (3): asRecord(), asString(), printGrokStreamEvent()

### Community 132 - "openclaw-gateway/src/index.ts"
Cohesion: 0.40
Nodes (4): agentConfigurationDoc, label, models, type

### Community 133 - "adapter_auth_sessions.ts"
Cohesion: 0.40
Nodes (3): ADAPTER_AUTH_SESSION_ACTIVE_STATES, adapterAuthSessions, AdapterAuthSessionState

### Community 135 - "claimPendingCleanupCapWarning"
Cohesion: 0.50
Nodes (5): claimPendingCleanupCapWarning(), claimPendingCleanupRetryAttempt(), pendingCleanupAttemptsSql(), pendingCleanupCapWarnedSql(), pendingCleanupMetadataObjectSql()

### Community 136 - "native-safe-replacement.ts"
Cohesion: 0.60
Nodes (4): NATIVE_SAFE_REPLACEMENT_REASON, processAlive(), reconcileSafeNativeReplacements(), record()

### Community 137 - "cursor-cloud/src/index.ts"
Cohesion: 0.50
Nodes (3): agentConfigurationDoc, label, type

### Community 141 - "usesInheritedProjectRuntimeServices"
Cohesion: 0.67
Nodes (3): loadEffectiveRuntimeServicesByExecutionWorkspace(), noActiveRuntimeServicesForWorkspaceCondition(), usesInheritedProjectRuntimeServices()

## Knowledge Gaps
- **811 isolated node(s):** `ACPX_ADAPTER_AGENT_IDS`, `AcpxAdapterType`, `AcpxAgentId`, `defaultModuleDir`, `PaperclipAcpRuntimeOptions` (+806 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `asString()` connect `server-utils.ts` to `acpx-engine/execute.ts`, `gateway/server/execute.ts`, `openclaw-gateway/src/server/execute.ts`, `opencode-local/src/server/execute.ts`, `codex-local/src/server/execute.ts`, `claude-local/src/server/execute.ts`, `pi-local/src/server/execute.ts`, `kimi-local/src/server/execute.ts`, `grok-local/src/server/execute.ts`, `cursor-local/src/server/execute.ts`, `gemini-local/src/server/execute.ts`, `claude-local/src/server/acp.ts`, `ensureAdapterExecutionTargetCommandResolvable`, `claude-local/src/server/test.ts`, `codex-local/src/server/acp.ts`, `gemini-local/src/server/acp.ts`, `kimi-local/src/server/acp.ts`, `codex-local/src/index.ts`, `AdapterSessionCodec`, `codex-local/src/server/test.ts`, `codex-local/src/server/parse.ts`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Why does `heartbeatService()` connect `heartbeatService` to `heartbeat.ts`, `scheduleBoundedRetryForRun`, `claimPendingCleanupCapWarning`, `resolveWorkspaceForRun`, `appendRunEvent`, `executeRun`, `readNonEmptyString`, `resolveSessionBeforeForWakeup`, `evaluateSessionCompaction`, `handleSuccessfulRunHandoff`, `executionWorkspaceService`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Why does `asNumber()` connect `server-utils.ts` to `heartbeat.ts`, `heartbeatService`, `acpx-engine/execute.ts`, `gateway/server/execute.ts`, `openclaw-gateway/src/server/execute.ts`, `opencode-local/src/server/execute.ts`, `codex-local/src/server/execute.ts`, `executeRun`, `readNonEmptyString`, `claude-local/src/server/execute.ts`, `pi-local/src/server/execute.ts`, `kimi-local/src/server/execute.ts`, `grok-local/src/server/execute.ts`, `cursor-local/src/server/execute.ts`, `gemini-local/src/server/execute.ts`, `claude-local/src/server/acp.ts`, `ensureAdapterExecutionTargetCommandResolvable`, `claude-local/src/server/test.ts`, `codex-local/src/server/acp.ts`, `gemini-local/src/server/acp.ts`, `kimi-local/src/server/acp.ts`, `codex-local/src/server/test.ts`, `codex-local/src/server/parse.ts`, `evaluateSessionCompaction`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `heartbeatService()` (e.g. with `applyTaskDrain()` and `computeTaskDrain()`) actually correct?**
  _`heartbeatService()` has 43 INFERRED edges - model-reasoned connections that need verification._
- **What connects `ACPX_ADAPTER_AGENT_IDS`, `AcpxAdapterType`, `AcpxAgentId` to the rest of the system?**
  _811 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `heartbeat.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.014484087436050761 - nodes in this community are weakly interconnected._
- **Should `server-utils.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.034879624192601294 - nodes in this community are weakly interconnected._