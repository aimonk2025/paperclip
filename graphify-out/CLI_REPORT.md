# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 105 files · ~101,751 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1443 nodes · 4102 edges · 66 communities
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 38 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- worktree.ts
- service-manager.ts
- pipelines.ts
- resolveCommandContext
- skills.ts
- doctor.ts
- teams.ts
- worktree-merge-history-lib.ts
- registry.ts
- update.ts
- board-auth.ts
- company.ts
- test-drive.ts
- addCommonClientOptions
- feedback.ts
- client/secrets.ts
- worktree-lib.ts
- install.ts
- install-store.ts
- home.ts
- onboard.ts
- onboard-service.ts
- BaseClientOptions
- registerCompanyCommands
- http.ts
- agent.ts
- worktreeCleanupCommand
- runWorktreeReseed
- printOutput
- commands/run.ts
- src/client/context.ts
- src/index.ts
- Paperclip is the app people use to manage AI agents for work.
- config/env.ts
- handleCommandError
- managed-agent.ts
- runWorktreeInit
- resolveConfigPath
- readConfig
- routines.ts
- common.ts
- service.ts
- connect.ts
- channels.ts
- env-lab.ts
- ensureWorktreeSeeded
- prompt.ts
- renderCompanyImportResult
- registerIssueCommands
- createStoredZipArchive
- promptForImportSelection
- routine-api.ts
- token.ts
- server.ts
- project.ts
- commands/env.ts
- approval.ts
- cost.ts
- client/run.ts
- normalizeGithubImportSource
- goal.ts
- resolveDefaultConfigPath
- listCompaniesForContext
- connections.ts
- helpers/zip.ts

## God Nodes (most connected - your core abstractions)
1. `printOutput()` - 134 edges
2. `resolveCommandContext()` - 125 edges
3. `BaseClientOptions` - 122 edges
4. `addCommonClientOptions()` - 114 edges
5. `handleCommandError()` - 110 edges
6. `apiPath()` - 94 edges
7. `registerCompanyCommands()` - 49 edges
8. `readConfig()` - 45 edges
9. `resolveConfigPath()` - 41 edges
10. `formatInlineRecord()` - 38 edges
11. `onboard()` - 32 edges
12. `runWorktreeInit()` - 31 edges
13. `registerPluginCommands()` - 28 edges
14. `registerSkillsCommands()` - 27 edges
15. `doctor()` - 24 edges

## Surprising Connections (you probably didn't know these)
- `AgentListOptions` --inherits--> `BaseClientOptions`  [EXTRACTED]
  cli/src/commands/client/agent.ts → cli/src/commands/client/common.ts
- `AgentLocalCliOptions` --inherits--> `BaseClientOptions`  [EXTRACTED]
  cli/src/commands/client/agent.ts → cli/src/commands/client/common.ts
- `AgentInboxMineOptions` --inherits--> `BaseClientOptions`  [EXTRACTED]
  cli/src/commands/client/agent.ts → cli/src/commands/client/common.ts
- `AgentWakeOptions` --inherits--> `BaseClientOptions`  [EXTRACTED]
  cli/src/commands/client/agent.ts → cli/src/commands/client/common.ts
- `AgentJsonPayloadOptions` --inherits--> `BaseClientOptions`  [EXTRACTED]
  cli/src/commands/client/agent.ts → cli/src/commands/client/common.ts

## Import Cycles
- 2-file cycle: `cli/src/checks/index.ts -> cli/src/checks/log-check.ts -> cli/src/checks/index.ts`
- 2-file cycle: `cli/src/checks/index.ts -> cli/src/checks/llm-check.ts -> cli/src/checks/index.ts`
- 2-file cycle: `cli/src/checks/index.ts -> cli/src/checks/managed-install-check.ts -> cli/src/checks/index.ts`
- 2-file cycle: `cli/src/checks/index.ts -> cli/src/checks/port-check.ts -> cli/src/checks/index.ts`
- 2-file cycle: `cli/src/checks/index.ts -> cli/src/checks/secrets-check.ts -> cli/src/checks/index.ts`
- 2-file cycle: `cli/src/checks/index.ts -> cli/src/checks/service-health-check.ts -> cli/src/checks/index.ts`
- 2-file cycle: `cli/src/checks/index.ts -> cli/src/checks/storage-check.ts -> cli/src/checks/index.ts`

## Communities (66 total, 0 thin omitted)

### Community 0 - "worktree.ts"
Cohesion: 0.04
Nodes (71): acquireWorktreeSeedLock(), activeSeedInterruptHandlers, applyMergePlan(), backupWorktreeReseedTarget(), ClosableDb, collectClaimedWorktreePorts(), ConfiguredStorage, CopiedGitHooksResult (+63 more)

### Community 1 - "service-manager.ts"
Cohesion: 0.06
Nodes (21): assertForegroundRunAllowed(), CommandResult, CommandRunner, defaultCommandRunner(), escapeRegExp(), escapeSystemd(), escapeXml(), execFileAsync (+13 more)

### Community 2 - "pipelines.ts"
Cohesion: 0.08
Nodes (53): addPipelineOptions(), asObject(), asOptionalObject(), AutomationOptions, BlockOptions, buildIngestBody(), buildReviewEdits(), CaseDetail (+45 more)

### Community 3 - "resolveCommandContext"
Cohesion: 0.09
Nodes (46): resolveCommandContext(), addPluginConfigGet(), addPluginConfigPost(), addPluginGet(), addPluginJobGet(), addPluginJobPost(), addPluginKeyPost(), addPluginLocalFolderGet() (+38 more)

### Community 4 - "skills.ts"
Cohesion: 0.10
Nodes (45): formatInlineRecord(), renderValue(), AgentSkillSyncOptions, appendQueryParam(), auditCompanySkills(), CatalogBrowseOptions, CatalogInstallOptions, checkCompanySkills() (+37 more)

### Community 5 - "doctor.ts"
Cohesion: 0.11
Nodes (30): configCheck(), databaseCheck(), isInsideOsTmpDir(), deploymentAuthCheck(), CheckResult, llmCheck(), logCheck(), hasManagedArtifacts() (+22 more)

### Community 6 - "teams.ts"
Cohesion: 0.09
Nodes (42): appendQueryParam(), buildCatalogTeamStatusRow(), buildMissingInstalledTeamStatusRow(), buildSourcePolicy(), buildTeamInstallOptions(), buildTeamOptions(), catalogTeamCompanyPath(), CatalogTeamInstalledStatus (+34 more)

### Community 7 - "worktree-merge-history-lib.ts"
Cohesion: 0.06
Nodes (39): AgentRow, AssetRow, buildWorktreeMergePlan(), CommentMergeAction, CommentRow, compareIssueCoreFields(), DocumentRevisionRow, DocumentRevisionTableRow (+31 more)

### Community 8 - "registry.ts"
Cohesion: 0.07
Nodes (32): printHttpStdoutEvent(), httpCLIAdapter, printProcessStdoutEvent(), processCLIAdapter, adaptersByType, claudeLocalCLIAdapter, codexLocalCLIAdapter, cursorCloudCLIAdapter (+24 more)

### Community 9 - "update.ts"
Cohesion: 0.13
Nodes (28): compareVersions(), DATABASE_UNREACHABLE_CODES, Dependencies, detectInstallMode(), emit(), execFileAsync, hasPaperclipInstanceData(), InstallMode (+20 more)

### Community 10 - "board-auth.ts"
Cohesion: 0.12
Nodes (27): BoardAuthCredential, BoardAuthStore, ChallengeStatusResponse, CreateChallengeResponse, defaultBoardAuthStore(), getStoredBoardCredential(), isTruthyEnv(), loginBoardCli() (+19 more)

### Community 11 - "company.ts"
Cohesion: 0.08
Nodes (30): AgentMeResponse, buildImportTransferManifest(), CHUNKED_IMPORT_THRESHOLD_BYTES, CompanyCollisionMode, CompanyCommandOptions, CompanyDeleteOptions, CompanyDeleteSelectorMode, CompanyExportOptions (+22 more)

### Community 12 - "test-drive.ts"
Cohesion: 0.11
Nodes (28): GitWorkspaceInfo, isLinkedGitWorktree(), StartedServer, assertTestDriveDatabaseIsolation(), bootstrapTestDrive(), dashboardUrl(), errorMessage(), HARNESS_DEFINITIONS (+20 more)

### Community 13 - "addCommonClientOptions"
Cohesion: 0.21
Nodes (26): addAdapterPatch(), addAdapterPost(), addCompanyAdapterGet(), addCompanyAdapterPost(), addJsonPost(), parseJson(), registerAdapterCommands(), addCommonClientOptions() (+18 more)

### Community 14 - "feedback.ts"
Cohesion: 0.12
Nodes (27): asRecord(), buildFeedbackVoteRecord(), collectJsonFilesForArchive(), compactText(), crc32(), createStoredZipArchive(), defaultFeedbackExportDirName(), ensureEmptyOutputDirectory() (+19 more)

### Community 15 - "client/secrets.ts"
Cohesion: 0.10
Nodes (27): asRecord(), asStringArray(), buildInlineMigrationSecretName(), buildMigratedAgentEnv(), collectInlineSecretMigrationCandidates(), DEFAULT_DECLARATION_INCLUDE, InlineSecretMigrationCandidate, isSensitiveEnvKey() (+19 more)

### Community 16 - "worktree-lib.ts"
Cohesion: 0.08
Nodes (27): buildWorktreeConfig(), buildWorktreeEnvEntries(), DEFAULT_WORKTREE_HOME, formatShellExports(), generateWorktreeColor(), hslComponentToHex(), hslToHex(), MINIMAL_WORKTREE_EXCLUDED_TABLES (+19 more)

### Community 17 - "install.ts"
Cohesion: 0.14
Nodes (26): assertSupportedNodeVersion(), confirmGitInstall(), ensureShimOnPath(), execFileAsync, gitBuildEnv(), installCommand(), installGitPayload(), installNpmPayload() (+18 more)

### Community 18 - "install-store.ts"
Cohesion: 0.15
Nodes (25): otherServiceDefinitions(), uninstallCommand(), UninstallDependencies, addManagedPathBlock(), assertManagedInstallStore(), assertManagedShimWritable(), assertOwnedByCurrentUser(), assertPayloadPath() (+17 more)

### Community 19 - "home.ts"
Cohesion: 0.22
Nodes (18): defaultConfig(), Section, SECTION_LABELS, describeLocalInstancePaths(), resolveDefaultBackupDir(), resolveDefaultEmbeddedPostgresDir(), resolveDefaultLogsDir(), resolveDefaultSecretsKeyFilePath() (+10 more)

### Community 20 - "onboard.ts"
Cohesion: 0.13
Nodes (23): canCreateBootstrapInviteImmediately(), describeServerBinding(), isEphemeralNpxExecution(), onboard(), ONBOARD_ENV_KEYS, OnboardDefaults, OnboardOptions, parseBooleanFromEnv() (+15 more)

### Community 21 - "onboard-service.ts"
Cohesion: 0.13
Nodes (21): HealthResult, probeHealth(), ServiceCheckDependencies, serviceHealthChecks(), InstallManifest, defaultDashboardDependencies, defaultDependencies, EnsureShimResult (+13 more)

### Community 22 - "BaseClientOptions"
Cohesion: 0.14
Nodes (24): ActivityListOptions, AdapterOptions, BaseClientOptions, DashboardGetOptions, InteractionAcceptOptions, InteractionReasonOptions, InteractionRespondOptions, IssueAttachmentDownloadOptions (+16 more)

### Community 23 - "registerCompanyCommands"
Cohesion: 0.09
Nodes (24): assertDeleteConfirmation(), assertDeleteFlags(), buildCompanyDashboardUrl(), buildDefaultImportAdapterOverrides(), confirmOverwriteExportDirectory(), formatSourceLabel(), formatTargetLabel(), isInteractiveTerminal() (+16 more)

### Community 24 - "http.ts"
Cohesion: 0.15
Nodes (12): ApiClientOptions, ApiConnectionError, buildConnectionErrorMessage(), buildHealthCheckUrl(), buildUrl(), formatConnectionCause(), PaperclipApiClient, RecoverAuthInput (+4 more)

### Community 25 - "agent.ts"
Cohesion: 0.12
Nodes (22): AgentDeleteOptions, AgentInboxMineOptions, AgentInstructionsFileOptions, AgentInstructionsFilePutOptions, AgentJsonPayloadOptions, AgentListOptions, AgentLocalCliOptions, AgentResetSessionOptions (+14 more)

### Community 26 - "worktreeCleanupCommand"
Cohesion: 0.13
Nodes (23): detectGitWorkspaceInfo(), branchExistsOnAnyRemote(), branchHasUniqueCommits(), copyDirectoryContents(), copyGitHooksToWorktreeGitDir(), ensureRepairTargetWorktree(), extractExecSyncErrorMessage(), installDependenciesBestEffort() (+15 more)

### Community 27 - "runWorktreeReseed"
Cohesion: 0.14
Nodes (23): collectMergePlan(), formatSeededWorktreeExecutionQuarantineSummary(), parseWorktreeMergeScopes(), openConfiguredStorage(), parseGitWorktreeList(), promptForProjectMappings(), promptForSourceEndpoint(), registerWorktreeCommands() (+15 more)

### Community 28 - "printOutput"
Cohesion: 0.24
Nodes (21): addAdminUserPost(), addCompanyList(), addCompanyPost(), addCompanyPut(), addJoinAction(), addJsonPatch(), addJsonPut(), addMemberPatch() (+13 more)

### Community 29 - "commands/run.ts"
Cohesion: 0.16
Nodes (19): ensureDevWorkspaceBuildDeps(), formatError(), getMissingModuleSpecifier(), importServerEntry(), isModuleNotFoundError(), maybeEnableUiDevMiddleware(), resolveBootstrapInviteBaseUrl(), runCommand() (+11 more)

### Community 30 - "src/client/context.ts"
Cohesion: 0.23
Nodes (19): ClientContext, defaultClientContext(), findContextFileFromAncestors(), normalizeContext(), normalizeProfile(), parseJson(), readContext(), resolveContextPath() (+11 more)

### Community 31 - "src/index.ts"
Cohesion: 0.13
Nodes (16): parseJson(), registerActivityCommands(), registerApprovalCommands(), registerAssetCommands(), registerClientAuthCommands(), registerConnectCommand(), registerDashboardCommands(), registerEmailCommands() (+8 more)

### Community 32 - "Paperclip is the app people use to manage AI agents for work."
Cohesion: 0.10
Nodes (19): Community, Community & Plugins, Contributing, Development, FAQ, Features, Importing & Exporting Companies, License (+11 more)

### Community 33 - "config/env.ts"
Cohesion: 0.27
Nodes (17): agentJwtSecretCheck(), emptyEnvFileContents(), ensureAgentJwtSecret(), ensureToolActionSigningSecret(), isNonEmpty(), loadAgentJwtEnvFile(), loadedEnvFiles, loadPaperclipEnvFile() (+9 more)

### Community 34 - "handleCommandError"
Cohesion: 0.27
Nodes (17): handleCommandError(), addBinaryCompanyGet(), addCompanyGet(), addCompanyPostJson(), addDelete(), addIdGet(), addPatchJson(), addPostEmpty() (+9 more)

### Community 35 - "managed-agent.ts"
Cohesion: 0.24
Nodes (18): anthropicRequest(), assertManagedAgentModel(), assertSafeManagedAgent(), assertSafeManagedEnvironment(), CLAUDE_MANAGED_BETA_VERSION, CLAUDE_MANAGED_QUALIFIED_MODEL, CLAUDE_MANAGED_SYSTEM_PROMPT, listAll() (+10 more)

### Community 36 - "runWorktreeInit"
Cohesion: 0.23
Nodes (19): closeDb(), detectGitBranchName(), inspectLegacyWorktreeDatabase(), isWorktreeSeedMode(), resolveWorktreeLocalPaths(), sanitizeWorktreeInstanceId(), nonEmpty(), openConfiguredDb() (+11 more)

### Community 37 - "resolveConfigPath"
Cohesion: 0.25
Nodes (15): addAllowedHostname(), configure(), normalizeHostnameInput(), parseHostnameCsv(), atomicWriteFile(), backupInvalidConfig(), configExists(), durableCopyFile() (+7 more)

### Community 38 - "readConfig"
Cohesion: 0.20
Nodes (15): bootstrapCeoInvite(), createInviteToken(), hashToken(), resolveBaseUrl(), resolveDbUrl(), inferApiBaseFromConfig(), dbBackupCommand(), DbBackupOptions (+7 more)

### Community 39 - "routines.ts"
Cohesion: 0.19
Nodes (17): ClosableDb, closeDb(), disableAllRoutinesCommand(), disableAllRoutinesInConfig(), DisableAllRoutinesResult, EmbeddedPostgresCtor, EmbeddedPostgresHandle, EmbeddedPostgresInstance (+9 more)

### Community 40 - "common.ts"
Cohesion: 0.19
Nodes (14): ClientContextProfile, ApiRequestError, AssetOptions, buildApiUrl(), downloadAsset(), parseFetchResponse(), safeJson(), uploadAsset() (+6 more)

### Community 41 - "service.ts"
Cohesion: 0.26
Nodes (16): CommonOptions, HealthResult, healthUrl(), output(), probeHealth(), registerServiceCommands(), resolveManager(), resolveRestartExpectedVersion() (+8 more)

### Community 42 - "connect.ts"
Cohesion: 0.29
Nodes (14): normalizeApiBase(), resolveApiBase(), askProfileName(), assertNotCancelled(), buildExports(), chooseAgent(), chooseCompany(), choosePersona() (+6 more)

### Community 43 - "channels.ts"
Cohesion: 0.19
Nodes (13): ChannelDescriptor, channelForVersion(), ChannelName, channelsCommand(), ChannelsOptions, ChannelState, collectChannelState(), defaultRunCommand() (+5 more)

### Community 44 - "env-lab.ts"
Cohesion: 0.35
Nodes (13): buildEnvLabCleanupCommand(), collectEnvLabDoctorStatus(), EnvLabCliInvocation, envLabDoctorCommand(), envLabDownCommand(), envLabStatusCommand(), envLabUpCommand(), printJson() (+5 more)

### Community 45 - "ensureWorktreeSeeded"
Cohesion: 0.27
Nodes (14): dispatchSeedInterruption(), dispatchSeedSigint(), dispatchSeedSigterm(), ensureWorktreeSeeded(), formatWorktreeSeedFailureDiagnostic(), resolveWorktreeSeedMarkerPaths(), markWorktreeSeedPending(), readLegacyWorktreeSeedPendingMarker() (+6 more)

### Community 46 - "prompt.ts"
Cohesion: 0.29
Nodes (12): agentSummary(), assertAgentMatchesReference(), createOrCommentForAgent(), defaultPromptTitle(), normalizePrompt(), PromptOptions, PromptResult, readApiKeyEnvOption() (+4 more)

### Community 47 - "renderCompanyImportResult"
Cohesion: 0.29
Nodes (12): actionChip(), appendMessageBlock(), appendPreviewExamples(), buildDefaultImportAdapterMessages(), pluralize(), renderCompanyImportPreview(), renderCompanyImportResult(), summarizeImportAgentResults() (+4 more)

### Community 48 - "registerIssueCommands"
Cohesion: 0.20
Nodes (12): buildFeedbackTraceQuery(), buildApiUrl(), downloadAttachment(), filterIssueRows(), parseCsv(), parseFetchResponse(), parseHiddenAt(), parseJson() (+4 more)

### Community 49 - "createStoredZipArchive"
Cohesion: 0.25
Nodes (10): collectPackageFileBytes(), estimateInlineImportBytes(), fileEntryInlineBytes(), resolveChunkedImportZip(), resolveInlineSourceFromPath(), shouldIncludePortableFile(), crc32(), createStoredZipArchive() (+2 more)

### Community 50 - "promptForImportSelection"
Cohesion: 0.27
Nodes (10): buildDefaultImportSelectionState(), buildImportSelectionCatalog(), buildSelectedFilesFromImportSelection(), collectEntityFiles(), collectFilesUnderDirectory(), findPortableExtensionPath(), getGroupLabel(), normalizePortablePath() (+2 more)

### Community 51 - "routine-api.ts"
Cohesion: 0.42
Nodes (9): addCompanyPost(), addIdDelete(), addIdGet(), addIdPatch(), addIdPost(), CompanyOptions, JsonOptions, parseJson() (+1 more)

### Community 52 - "token.ts"
Cohesion: 0.24
Nodes (9): AgentKeyRow, AgentTokenOptions, BoardKeyRow, BoardTokenOptions, CreatedAgentKey, CreatedBoardKey, registerTokenCommands(), resolveAgent() (+1 more)

### Community 53 - "server.ts"
Cohesion: 0.42
Nodes (8): BaseServerInput, buildCustomServerConfig(), buildPresetServerConfig(), detectTailnetBindHost(), inferConfiguredBind(), resolveQuickstartServerConfig(), cancelled(), promptServer()

### Community 54 - "project.ts"
Cohesion: 0.31
Nodes (8): parseCsv(), parseNullableString(), parseOptionalJson(), ProjectCreateOptions, ProjectDeleteOptions, ProjectListOptions, ProjectUpdateOptions, registerProjectCommands()

### Community 55 - "commands/env.ts"
Cohesion: 0.36
Nodes (8): collectDeploymentEnvRows(), defaultSecretsKeyFilePath(), defaultStorageBaseDir(), envCommand(), EnvSource, EnvVarRow, quoteShellValue(), uniqueByKey()

### Community 56 - "approval.ts"
Cohesion: 0.25
Nodes (7): ApprovalCommentOptions, ApprovalCreateOptions, ApprovalDecisionOptions, ApprovalListOptions, ApprovalResubmitOptions, parseCsv(), parseJsonObject()

### Community 57 - "cost.ts"
Cohesion: 0.46
Nodes (7): addCompanyGet(), addCompanyPostJson(), CompanyOptions, IncidentOptions, JsonPayloadOptions, parseJson(), registerCostCommands()

### Community 58 - "client/run.ts"
Cohesion: 0.25
Nodes (7): fetchLog(), RunEventsOptions, RunIssueSummary, RunListOptions, RunLiveOptions, RunLogOptions, RunWatchdogOptions

### Community 59 - "normalizeGithubImportSource"
Cohesion: 0.33
Nodes (7): buildGithubImportUrl(), isGithubSegment(), isGithubShorthand(), isHttpUrl(), looksLikeRepoUrl(), normalizeGithubImportPath(), normalizeGithubImportSource()

### Community 60 - "goal.ts"
Cohesion: 0.33
Nodes (5): GoalCreateOptions, GoalDeleteOptions, GoalListOptions, GoalUpdateOptions, parseNullableString()

### Community 61 - "resolveDefaultConfigPath"
Cohesion: 0.47
Nodes (5): applyDataDirOverride(), DataDirCommandSupport, DataDirOptionLike, resolveDefaultConfigPath(), resolveDefaultContextPath()

### Community 62 - "listCompaniesForContext"
Cohesion: 0.40
Nodes (5): createCompanyForContext(), isBoardAccessRequiredError(), isInstanceAdminRequiredError(), listCompaniesForContext(), resolveCurrentCompanyId()

### Community 63 - "connections.ts"
Cohesion: 0.60
Nodes (4): callRuntimeConnectionTool(), registerConnectionIntentCommands(), RuntimeConnectionOptions, writeResult()

### Community 64 - "helpers/zip.ts"
Cohesion: 0.70
Nodes (4): crc32(), createStoredZipArchive(), writeUint16(), writeUint32()

## Knowledge Gaps
- **244 isolated node(s):** `claudeLocalCLIAdapter`, `codexLocalCLIAdapter`, `openCodeLocalCLIAdapter`, `piLocalCLIAdapter`, `cursorLocalCLIAdapter` (+239 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BaseClientOptions` connect `BaseClientOptions` to `pipelines.ts`, `resolveCommandContext`, `skills.ts`, `teams.ts`, `board-auth.ts`, `company.ts`, `addCommonClientOptions`, `feedback.ts`, `client/secrets.ts`, `agent.ts`, `printOutput`, `src/index.ts`, `handleCommandError`, `managed-agent.ts`, `common.ts`, `connect.ts`, `prompt.ts`, `routine-api.ts`, `token.ts`, `project.ts`, `approval.ts`, `cost.ts`, `client/run.ts`, `goal.ts`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `resolveCommandContext()` connect `resolveCommandContext` to `pipelines.ts`, `skills.ts`, `teams.ts`, `registry.ts`, `board-auth.ts`, `company.ts`, `addCommonClientOptions`, `feedback.ts`, `client/secrets.ts`, `BaseClientOptions`, `registerCompanyCommands`, `agent.ts`, `printOutput`, `src/client/context.ts`, `src/index.ts`, `handleCommandError`, `managed-agent.ts`, `common.ts`, `connect.ts`, `prompt.ts`, `registerIssueCommands`, `routine-api.ts`, `token.ts`, `project.ts`, `approval.ts`, `cost.ts`, `client/run.ts`, `goal.ts`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `apiPath()` connect `addCommonClientOptions` to `pipelines.ts`, `teams.ts`, `board-auth.ts`, `company.ts`, `feedback.ts`, `client/secrets.ts`, `BaseClientOptions`, `registerCompanyCommands`, `agent.ts`, `printOutput`, `src/index.ts`, `handleCommandError`, `managed-agent.ts`, `common.ts`, `connect.ts`, `prompt.ts`, `registerIssueCommands`, `routine-api.ts`, `token.ts`, `project.ts`, `approval.ts`, `cost.ts`, `client/run.ts`, `goal.ts`, `listCompaniesForContext`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **What connects `claudeLocalCLIAdapter`, `codexLocalCLIAdapter`, `openCodeLocalCLIAdapter` to the rest of the system?**
  _244 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `worktree.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.0381340244353943 - nodes in this community are weakly interconnected._
- **Should `service-manager.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.05519480519480519 - nodes in this community are weakly interconnected._
- **Should `pipelines.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.08106219426974144 - nodes in this community are weakly interconnected._