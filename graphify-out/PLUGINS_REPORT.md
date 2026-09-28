# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 220 files · ~301,262 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3185 nodes · 6089 edges · 180 communities (145 shown, 35 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 84 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- sdk/src/types.ts
- sdk/src/index.ts
- core.ts
- testing.ts
- host-client-factory.ts
- validators/plugin.ts
- routes.ts
- ui/index.ts
- worker-rpc-host.ts
- bridge-client.ts
- daytona/src/plugin.ts
- startWorkerRpcHost
- exe-dev/src/plugin.ts
- define-plugin.ts
- Paperclip Distill
- plugin-kitchen-sink-example/src/worker.ts
- plugin-llm-wiki/src/worker.ts
- plugin-loader.ts
- types/plugin.ts
- routes/plugins.ts
- kubernetes/src/plugin.ts
- daytona/src/file-sync.ts
- normalizeWikiId
- workspace-diff.ts
- plugin-host-services.ts
- PluginWorkerManager
- modal/src/plugin.ts
- PluginLoader
- PluginJobScheduler
- pluginManagedAgentService
- plugin-database.ts
- createPluginWorkerHandle
- paperclip-plugin-fake-sandbox/src/plugin.ts
- login-pty.ts
- novita/src/plugin.ts
- ui/types.ts
- plugin-environment-driver.ts
- distillPaperclipProjectPage
- create-paperclip-plugin/src/index.ts
- pluginRoutes
- PluginToolDispatcher
- bundled-plugins.ts
- PluginLifecycleManager
- contracts.ts
- duplex-command-stream.ts
- kubernetes/src/file-sync.ts
- plugin-local-folders.ts
- pluginManagedRoutineService
- e2b/src/plugin.ts
- job-orchestrator.ts
- lease-lifecycle.ts
- plugin-dev-watcher.ts
- plugin-managed-skills.ts
- schema/plugins.ts
- plugin-llm-wiki/src/manifest.ts
- createTestHarness
- hooks.ts
- tableName
- diff-model.ts
- sandboxHandleCache
- PluginIssuesClient
- dev-server.ts
- plugin-worker-manager.ts
- readNonEmptyString
- adapter-defaults.ts
- tenant-orchestrator.ts
- plugin-secrets-handler.ts
- plugin-llm-wiki/tests/plugin.spec.ts
- templates.ts
- adapter-plugin-store.ts
- plugin-event-bus.ts
- `@paperclipai/plugin-sdk`
- createPaperclipDistillationRun
- plugin
- @paperclipai/plugin-kubernetes (alpha)
- updateEventIngestionSettings
- Security boundary
- Slot component descriptions
- createOperationIssue
- plugin-workspace-diff/src/worker.ts
- executeInSession
- plugin-runtime-sandbox.ts
- e2b.d.ts
- scoped-network-egress.ts
- PluginCapabilityValidator
- openDuplexChannel
- Steps
- createPluginJobScheduler
- PluginWorkerHandle
- AGENTS.md — LLM Wiki Schema
- AGENTS.md — LLM Wiki Schema
- contentHash
- createPluginToolDispatcher
- plugin-orchestration-smoke-example/src/worker.ts
- workspace-diff.spec.ts
- buildUntrackedFilePatch
- LLM Wiki
- LLM Wiki
- LLM Wiki
- plugin-file-browser-example/src/worker.ts
- plugin-manifest-validator.ts
- closeDuplexChannelRouteOnWorkerExit
- `@paperclipai/plugin-modal`
- pod-exec.ts
- PluginLocalFoldersClient
- buildHostServices
- plugin-host-service-cleanup.ts
- File Browser Example Plugin
- UI slots and launchers
- issue-attachments.ts
- wiki-route-sidebar-ui.spec.ts
- LoginPtySession
- image-allowlist.ts
- upload-interceptor.ts
- requestedCompanyScope
- Index
- Index
- Cloudflare Sandbox Bridge Template
- Sandbox
- PluginLoginPtyWorkerSession
- PluginAgentsClient
- PluginProjectsClient
- plugin-capability-validator.ts
- DuplexChannelHostSession
- LoginPtyHostSession
- @paperclipai/plugin-hello-world-example
- Plugin Orchestration Smoke Example
- LLM Wiki Maintainer
- `@paperclipai/plugin-cloudflare-sandbox`
- Directory-constraint (`bwrap`) findings for the Daytona session path
- `@paperclipai/plugin-daytona`
- `@paperclipai/plugin-e2b`
- `@paperclipai/plugin-exe-dev`
- `@paperclipai/plugin-novita-sandbox`
- Hooks reference
- UI authoring note
- plugin-authoring-smoke-example/tests/plugin.spec.ts
- plugin-hello-world-example/src/index.ts
- _kind-harness.ts
- PluginAgentSessionsClient
- PluginGoalsClient
- PluginIssueDocumentsClient
- PluginLogger
- Plugin Authoring Smoke Example
- Real-time streaming (`ctx.streams`)
- PluginAccessInvitesClient
- PluginAccessMembersClient
- PluginApprovalsClient
- HostNavigation
- @paperclipai/plugin-kitchen-sink-example
- defaultWikiSpaceRow
- daytona/src/index.ts
- daytona/vitest.config.ts
- kubernetes/src/index.ts
- plugin-log-retention.ts
- @paperclipai/create-paperclip-plugin
- Log
- Log
- CapabilityDeniedError
- InvocationScopeDeniedError
- isValidCronExpression
- CapabilityScopedInvoker
- raw/plugin-boundaries.md
- Knowledge
- concepts/plugin-boundaries.md

## God Nodes (most connected - your core abstractions)
1. `createHostClientHandlers()` - 78 edges
2. `createPluginWorkerHandle()` - 63 edges
3. `startWorkerRpcHost()` - 56 edges
4. `plugin` - 53 edges
5. `dispatchMethod()` - 41 edges
6. `PluginDefinition` - 36 edges
7. `PluginLifecycleManager` - 35 edges
8. `pluginRoutes()` - 33 edges
9. `normalizeWikiId()` - 31 edges
10. `PluginLoader` - 30 edges
11. `distillPaperclipProjectPage()` - 29 edges
12. `methodNotImplemented()` - 28 edges
13. `EnvironmentTestHarnessOptions` - 26 edges
14. `PluginWorkerManager` - 26 edges
15. `resolveSpace()` - 25 edges

## Surprising Connections (you probably didn't know these)
- `plugin` --indirect_call--> `namespace()`  [INFERRED]
  packages/plugins/sandbox-providers/kubernetes/src/plugin.ts → packages/plugins/sdk/src/host-client-factory.ts
- `PluginManagedRoutineServiceOptions` --references--> `PluginWorkerManager`  [EXTRACTED]
  server/src/services/plugin-managed-routines.ts → server/src/services/plugin-worker-manager.ts
- `plugin` --calls--> `getEventIngestionSettings()`  [EXTRACTED]
  packages/plugins/plugin-llm-wiki/src/worker.ts → packages/plugins/plugin-llm-wiki/src/wiki/core.ts
- `plugin` --calls--> `getPaperclipIngestionProfile()`  [EXTRACTED]
  packages/plugins/plugin-llm-wiki/src/worker.ts → packages/plugins/plugin-llm-wiki/src/wiki/core.ts
- `plugin` --calls--> `updatePaperclipIngestionProfile()`  [EXTRACTED]
  packages/plugins/plugin-llm-wiki/src/worker.ts → packages/plugins/plugin-llm-wiki/src/wiki/core.ts

## Import Cycles
- 3-file cycle: `server/src/services/plugin-lifecycle.ts -> server/src/services/plugin-loader.ts -> server/src/services/plugin-tool-dispatcher.ts -> server/src/services/plugin-lifecycle.ts`

## Communities (180 total, 35 thin omitted)

### Community 0 - "sdk/src/types.ts"
Cohesion: 0.02
Nodes (45): PluginPerformActionContext, AgentSessionSendResult, NOOP_PLUGIN_SPAN, PluginAccessClient, PluginActionsClient, PluginActivityClient, PluginActivityLogEntry, PluginAuthorizationClient (+37 more)

### Community 1 - "sdk/src/index.ts"
Cohesion: 0.04
Nodes (91): createPluginBundlerPresets(), EsbuildLikeOptions, PluginBundlerPresetInput, PluginBundlerPresets, RollupLikeConfig, PluginApiResponse, HostServices, ChannelBytesWireValue (+83 more)

### Community 2 - "core.ts"
Cohesion: 0.03
Nodes (85): assertSourceWithinConfiguredLimit(), BootstrapInput, byteLength(), CaptureSourceInput, CreateSpaceInput, DEFAULT_EVENT_INGESTION_SETTINGS, DEFAULT_SPACE_SLUG, DEFAULT_WIKI_ID (+77 more)

### Community 3 - "testing.ts"
Cohesion: 0.05
Nodes (49): PluginEnvironmentAcquireLeaseParams, PluginEnvironmentCancelInteractiveSetupParams, PluginEnvironmentCancelInteractiveSetupResult, PluginEnvironmentCaptureTemplateParams, PluginEnvironmentCaptureTemplateResult, PluginEnvironmentDeleteTemplateParams, PluginEnvironmentDeleteTemplateResult, PluginEnvironmentDestroyLeaseParams (+41 more)

### Community 4 - "host-client-factory.ts"
Cohesion: 0.05
Nodes (75): addBlockers(), assertCheckoutOwner(), close(), configure(), create(), createComment(), createHostClientHandlers(), createInteraction() (+67 more)

### Community 5 - "validators/plugin.ts"
Cohesion: 0.03
Nodes (61): entityScopedLauncherPlacementZones, InstallPlugin, installPluginSchema, jsonSchemaSchema, launcherBoundsByEnvironment, ListPluginState, listPluginStateSchema, PatchPluginConfig (+53 more)

### Community 6 - "routes.ts"
Cohesion: 0.08
Nodes (47): isAuthorizedRequest(), readBearerToken(), timingSafeStringEqual(), BridgeExecuteParams, buildLoginShellScript(), coerceExecuteResult(), executeInSandbox(), isValidShellEnvKey() (+39 more)

### Community 7 - "ui/index.ts"
Cohesion: 0.07
Nodes (55): ActionBar, ActionBarItem, ActionBarProps, AssigneePicker, AssigneePickerProps, AssigneePickerSelection, DataTable, DataTableColumn (+47 more)

### Community 8 - "worker-rpc-host.ts"
Cohesion: 0.06
Nodes (44): PaperclipPlugin, PluginApiRequestInput, PluginConfigValidationResult, PluginHealthDiagnostics, PluginWebhookInput, createErrorResponse(), createNotification(), createRequest() (+36 more)

### Community 9 - "bridge-client.ts"
Cohesion: 0.06
Nodes (39): BridgeClientHeaders, BridgeClientOptions, BridgeErrorBody, BridgeExecuteOptions, buildHeaders(), CloudflareBridgeError, consumeExecuteEventStream(), createCloudflareBridgeClient() (+31 more)

### Community 10 - "daytona/src/plugin.ts"
Cohesion: 0.05
Nodes (38): buildCreateParams(), buildResources(), buildSandboxLabels(), closeDaytonaDuplexChannelsForLease(), createDaytonaClient(), createSandbox(), DaytonaDriverConfig, daytonaDuplexChannelByRoute (+30 more)

### Community 11 - "startWorkerRpcHost"
Cohesion: 0.10
Nodes (48): startWorkerRpcHost(), actionContextFromParams(), actorTypeOrSystem(), allowsEvent(), cleanup(), dispatchMethod(), handleApiRequest(), handleConfigChanged() (+40 more)

### Community 12 - "exe-dev/src/plugin.ts"
Cohesion: 0.08
Nodes (39): manifest, buildCreateCommand(), buildEnvFlags(), buildFlag(), buildLease(), buildLoginShellScript(), buildRepeatedFlag(), buildSshArgs() (+31 more)

### Community 13 - "define-plugin.ts"
Cohesion: 0.06
Nodes (26): definePlugin(), PluginConfigChangeContext, PluginDefinition, DetectExternalObjectsParams, DetectExternalObjectsResult, PluginDuplexChannelCloseParams, PluginDuplexChannelCloseResult, PluginDuplexChannelOpenParams (+18 more)

### Community 14 - "Paperclip Distill"
Cohesion: 0.04
Nodes (41): Index Refresh, Inputs, Tools, Verification, Voice, What this skill does NOT do, Workflow, Anti-patterns to avoid (+33 more)

### Community 15 - "plugin-kitchen-sink-example/src/worker.ts"
Cohesion: 0.08
Nodes (41): DEFAULT_CONFIG, EXPORT_NAMES, JOB_KEYS, PAGE_ROUTE, PLUGIN_ID, PLUGIN_VERSION, RUNTIME_LAUNCHER, SAFE_COMMANDS (+33 more)

### Community 16 - "plugin-llm-wiki/src/worker.ts"
Cohesion: 0.09
Nodes (42): WIKI_MAINTENANCE_ROUTINE_KEYS, WIKI_ROOT_FOLDER_KEY, agentDetails(), agentResource(), bindingTable(), bootstrapWikiRoot(), getOverview(), getResourceBinding() (+34 more)

### Community 17 - "plugin-loader.ts"
Cohesion: 0.07
Nodes (42): resolveBundledCatalogRoot(), ADAPTER_ENV_PASSTHROUGH, buildLocalPluginBuildCommand(), buildLocalPluginBuildCommands(), buildLocalPluginRecoveryCommand(), buildPluginWorkerEnv(), buildStandaloneBundledPluginInstallArgs(), buildStandaloneBundledPluginInstallCommand() (+34 more)

### Community 18 - "types/plugin.ts"
Cohesion: 0.05
Nodes (43): JsonSchema, PaperclipPluginManifestV1, PluginApiRouteCompanyResolution, PluginApiRouteDeclaration, PluginCompanySettings, PluginConfig, PluginDatabaseDeclaration, PluginDatabaseNamespaceRecord (+35 more)

### Community 19 - "routes/plugins.ts"
Cohesion: 0.07
Nodes (34): AvailableBundledPlugin, bundledPluginMetadata(), __dirname, discoverBundledPlugins(), DiscoveredBundledPlugin, EXPERIMENTAL_BUNDLED_PLUGIN_PACKAGE_NAMES, fileExists(), findPackageJsonFiles() (+26 more)

### Community 20 - "kubernetes/src/plugin.ts"
Cohesion: 0.08
Nodes (26): RFC-1123, createKubeConfig(), CreateKubeConfigInput, makeKubeClients(), DEFAULT_RESOURCE_QUOTA, deriveTenantNamespace(), plugin, TODO: use params.runId as stand-in for agentId in labels; future (+18 more)

### Community 21 - "daytona/src/file-sync.ts"
Cohesion: 0.15
Nodes (34): assertConfinedSandboxPath(), assertSandboxCommandOk(), assertSandboxCommandOkWithOutput(), assertSandboxPathsConfined(), assertTarballEntriesConfined(), canonicalizerPreamble(), compressFileToHostTemp(), countHostFiles() (+26 more)

### Community 22 - "normalizeWikiId"
Cohesion: 0.15
Nodes (34): archiveSpace(), assertPagePath(), assertPageWriteAllowed(), assertRawPath(), assertWikiPath(), bootstrapSpace(), bootstrapSpaceFiles(), captureWikiSource() (+26 more)

### Community 23 - "workspace-diff.ts"
Cohesion: 0.13
Nodes (30): WorkspaceDiffFileStatus, addStatusEntries(), collectFiles(), DiffScope, ensureFile(), execFileAsync, GitStatusEntry, isMaxBufferError() (+22 more)

### Community 24 - "plugin-host-services.ts"
Cohesion: 0.08
Nodes (29): ALLOWED_PROTOCOLS, BufferedLogEntry, buildPinnedRequestOptions(), clampProviderSpanAttributes(), clampProviderSpanName(), clampSpanStatus(), executePinnedHttpRequest(), flushPluginLogBuffer() (+21 more)

### Community 25 - "PluginWorkerManager"
Cohesion: 0.08
Nodes (17): computeETag(), MIME_TYPES, PluginUiStaticRouteOptions, pluginUiStaticRoutes(), resolvePluginUiDir(), PluginRouteWebhookDeps, resolvePluginSandboxProviderDriverById(), LifecycleEventName (+9 more)

### Community 26 - "modal/src/plugin.ts"
Cohesion: 0.09
Nodes (19): manifest, buildLoginShellScript(), buildSandboxCreateParams(), createModalClient(), createSandboxFor(), deleteStdinPath(), ensureRemoteWorkspace(), formatErrorMessage() (+11 more)

### Community 27 - "PluginLoader"
Cohesion: 0.09
Nodes (17): execFileAsync, getDeclaredPageRoutePaths(), getMinimumHostVersion(), isPluginPackageName(), PluginLoader, activatePlugin(), assertPageRoutePathsAvailable(), buildDiscoveredPlugin() (+9 more)

### Community 28 - "PluginJobScheduler"
Cohesion: 0.09
Nodes (14): PluginRouteJobDeps, createPluginJobCoordinator(), PluginJobCoordinator, PluginJobCoordinatorOptions, PluginJobScheduler, PluginJobSchedulerOptions, SchedulerDiagnostics, TriggerJobResult (+6 more)

### Community 29 - "pluginManagedAgentService"
Cohesion: 0.18
Nodes (29): adapterPreference(), applyInstructionTemplateVariables(), bindingExternalId(), declarationPatch(), declaredInstructionFiles(), fallbackAdapterType(), managedAgentPauseReason(), managedMetadata() (+21 more)

### Community 30 - "plugin-database.ts"
Cohesion: 0.12
Nodes (23): ApplyPluginMigrationsOptions, assertAllowedPublicRead(), assertIdentifier(), assertNoBannedSql(), derivePluginDatabaseNamespace(), extractQualifiedRefs(), normaliseSql(), PluginDatabaseClient (+15 more)

### Community 31 - "createPluginWorkerHandle"
Cohesion: 0.15
Nodes (28): createPluginWorkerHandle(), attachStdioHandlers(), callInternal(), cancelPendingRestart(), clearExecuteRoute(), clearInvocation(), closeDuplexChannelTerminal(), closeLoginPtyRouteOnWorkerExit() (+20 more)

### Community 32 - "paperclip-plugin-fake-sandbox/src/plugin.ts"
Cohesion: 0.09
Nodes (19): manifest, buildCommandEnvironment(), buildCommandLine(), buildSetupProviderLeaseId(), buildTemplateRef(), encodeRefPart(), FakeDriverConfig, FakeLeaseState (+11 more)

### Community 33 - "login-pty.ts"
Cohesion: 0.09
Nodes (19): assertDescriptor(), composeLaunchLine(), createDaytonaLoginHomeFs(), createDaytonaLoginPtySessionOpener(), DaytonaExecResult, DaytonaLoginHomeFs, DaytonaLoginPtyOptions, DaytonaPtyHandle (+11 more)

### Community 34 - "novita/src/plugin.ts"
Cohesion: 0.11
Nodes (21): manifest, buildShellCommand(), buildStdinPath(), connectSandbox(), createSandbox(), ensureWorkspace(), executeInSandbox(), formatErrorMessage() (+13 more)

### Community 35 - "ui/types.ts"
Cohesion: 0.07
Nodes (22): HostNavigationLinkOptions, HostNavigationLinkProps, HostNavigationOptions, PluginBridgeError, PluginCommentAnnotationProps, PluginCommentContextMenuItemProps, PluginCompanySettingsPageProps, PluginDataResult (+14 more)

### Community 36 - "plugin-environment-driver.ts"
Cohesion: 0.14
Nodes (26): cancelPluginEnvironmentInteractiveSetup(), capturePluginEnvironmentTemplate(), deletePluginEnvironmentTemplate(), destroyPluginEnvironmentLease(), executePluginEnvironmentCommand(), getPluginEnvironmentInteractiveSetup(), INTERACTIVE_SETUP_WORKER_METHODS, listReadyPluginEnvironmentDrivers() (+18 more)

### Community 37 - "distillPaperclipProjectPage"
Cohesion: 0.15
Nodes (27): appendProjectLogContents(), assertExpectedHash(), autoApplyEnabled(), conceptBullet(), decisionsPageContents(), distillPaperclipProjectPage(), excerpt(), getDistillationAutoApplyRestriction() (+19 more)

### Community 38 - "create-paperclip-plugin/src/index.ts"
Cohesion: 0.14
Nodes (23): packageToDirName(), parseArg(), runCli(), RunCliDeps, formatFileDependency(), getLocalSdkPackagePath(), getLocalSharedPackagePath(), getRepoRootFromSdkPath() (+15 more)

### Community 39 - "pluginRoutes"
Cohesion: 0.08
Nodes (10): assertPluginManagementVisible(), pluginRoutes(), logPluginMutationActivity(), resolvePluginAuditCompanyIds(), resolvePlugin(), canonicalizeLocalPluginPath(), isWithinBundledPluginRoot(), LocalPluginPathValidation (+2 more)

### Community 40 - "PluginToolDispatcher"
Cohesion: 0.09
Nodes (7): PluginRouteToolDeps, PluginToolDispatcher, PluginToolRegistry, RegisteredTool, TOOL_NAMESPACE_SEPARATOR, ToolExecutionResult, ToolListFilter

### Community 41 - "bundled-plugins.ts"
Cohesion: 0.14
Nodes (23): BUNDLED_CATALOG_ROOT_ENV_VAR, BUNDLED_PLUGIN_CATALOG, BundledPluginCatalogEntry, BundledPluginProvisionerDeps, canonicalize(), DEFAULT_BUNDLED_CATALOG_ROOT, ensureBundledPlugins(), error() (+15 more)

### Community 42 - "PluginLifecycleManager"
Cohesion: 0.10
Nodes (9): isValidTransition(), PluginLifecycleManager, assertTransition(), deactivatePluginRuntime(), emitDomain(), requirePlugin(), stopWorkerIfRunning(), transition() (+1 more)

### Community 43 - "contracts.ts"
Cohesion: 0.11
Nodes (21): normalizePathQuery(), queryBooleanSchema, WorkspaceDiffCaps, workspaceDiffCapsSchema, workspaceDiffFilePatchSchema, workspaceDiffFileSchema, workspaceDiffFileStatusSchema, WorkspaceDiffPatchKind (+13 more)

### Community 44 - "duplex-command-stream.ts"
Cohesion: 0.11
Nodes (16): buildDuplexChannelLaunchWrapper(), createDaytonaDuplexChannelSessionOpener(), DAYTONA_DUPLEX_WRITE_ERROR_REASON, DaytonaDuplexChannelOptions, DaytonaDuplexWriteErrorReason, DuplexChannelSession, DuplexChannelSessionOpener, openDaytonaDuplexChannelSession() (+8 more)

### Community 45 - "kubernetes/src/file-sync.ts"
Cohesion: 0.24
Nodes (23): assertConfinedSandboxPath(), assertTarballEntriesConfined(), canonicalizerPreamble(), countHostFiles(), createHostTarball(), execFileAsync, extractHostTarball(), parseTarVerboseListingLine() (+15 more)

### Community 46 - "plugin-local-folders.ts"
Cohesion: 0.19
Nodes (22): assertPathInsideRoot(), assertPluginLocalFolderKey(), deletePluginLocalFolderFile(), ensureDirectoryInsideRoot(), findLocalFolderDeclaration(), inspectChildPath(), inspectPluginLocalFolder(), isInsideRoot() (+14 more)

### Community 47 - "pluginManagedRoutineService"
Cohesion: 0.22
Nodes (22): buildRoutineDefaults(), managedByPlugin(), normalizeRef(), pluginManagedRoutineService(), createManagedRoutine(), declarationFor(), ensureDefaultTriggers(), get() (+14 more)

### Community 48 - "e2b/src/plugin.ts"
Cohesion: 0.13
Nodes (17): manifest, buildLoginShellScript(), buildTimeoutExecuteResult(), connectForCleanup(), connectSandbox(), createSandbox(), E2bDriverConfig, ensureSandboxWorkspace() (+9 more)

### Community 49 - "job-orchestrator.ts"
Cohesion: 0.14
Nodes (10): getJobStatus(), jobOrchestrator, JobStatus, JobTimeoutError, sleep(), waitForJobCompletion(), KubeClients, TODO: requires custom in-cluster controller for k8s — kubelet does not (+2 more)

### Community 50 - "lease-lifecycle.ts"
Cohesion: 0.14
Nodes (18): deleteJob(), findPodForJob(), checkLeaseResumable(), DestroyLeaseInput, destroyLeaseResources(), ignoreNotFound(), isKubeNotFoundError(), ResumeCheckInput (+10 more)

### Community 51 - "plugin-dev-watcher.ts"
Cohesion: 0.15
Nodes (19): createPluginDevWatcher(), close(), handlePluginDisabled(), handlePluginEnabled(), handlePluginLoaded(), handlePluginUnloaded(), unwatchPlugin(), watchLocalPluginById() (+11 more)

### Community 52 - "plugin-managed-skills.ts"
Cohesion: 0.21
Nodes (22): buildDeclaredSkillFiles(), buildDefaultMarkdown(), buildPackageFiles(), buildSkillDefaults(), canonicalSkillKey(), pluginKeySlug(), pluginManagedSkillService(), declarationFor() (+14 more)

### Community 53 - "schema/plugins.ts"
Cohesion: 0.13
Nodes (12): pluginCompanySettings, pluginConfig, pluginDatabaseNamespaces, pluginMigrations, pluginEntities, pluginJobRuns, pluginJobs, pluginLogs (+4 more)

### Community 54 - "plugin-llm-wiki/src/manifest.ts"
Cohesion: 0.09
Nodes (19): CURSOR_WINDOW_ROUTINE_KEY, DEFAULT_MAX_PAPERCLIP_CURSOR_WINDOW_CHARS, DEFAULT_MAX_PAPERCLIP_ISSUE_SOURCE_CHARS, DEFAULT_MAX_PAPERCLIP_ROUTINE_RUN_CHARS, DEFAULT_MAX_SOURCE_BYTES, DEFAULT_PAPERCLIP_COST_CENTS_PER_1K_CHARS, INDEX_REFRESH_ROUTINE_KEY, INDEX_REFRESH_SKILL_KEY (+11 more)

### Community 55 - "createTestHarness"
Cohesion: 0.12
Nodes (12): createEnvironmentTestHarness(), callHook(), record(), createTestHarness(), actionContextFor(), actorTypeOrSystem(), getPrincipalGrants(), localFolderFileKey() (+4 more)

### Community 56 - "hooks.ts"
Cohesion: 0.15
Nodes (19): copyTextToClipboard(), createSdkUiComponent(), useHostContext(), useHostLocation(), useHostNavigation(), usePluginAction(), usePluginData(), usePluginStream() (+11 more)

### Community 57 - "tableName"
Cohesion: 0.15
Nodes (21): affectedPagePathsFromRunMetadata(), countPaperclipHistoricalPages(), distillationCursorTable(), distillationRunTable(), enableActiveProjectDistillation(), filterReadableRows(), getDistillationOverview(), getDistillationPageProvenance() (+13 more)

### Community 58 - "diff-model.ts"
Cohesion: 0.17
Nodes (18): WorkspaceDiffFile, WorkspaceDiffFilePatch, WorkspaceDiffWarning, buildFilePatch(), buildFilePatches(), DiffFileViewModel, DiffPatchViewModel, DiffRenderMode (+10 more)

### Community 59 - "sandboxHandleCache"
Cohesion: 0.14
Nodes (18): assertHandleMatchesLease(), handleFreshnessNow(), isRecord(), runnerIngressGenerationStore, sandboxAccountDiscriminator(), sandboxHandleActivityGates, sandboxHandleCache, sandboxHandleCacheKey() (+10 more)

### Community 61 - "dev-server.ts"
Cohesion: 0.18
Nodes (15): main(), parseArg(), Closeable, contentType(), ensureUiDir(), getUiBuildSnapshot(), listFilesRecursive(), normalizeFilePath() (+7 more)

### Community 62 - "plugin-worker-manager.ts"
Cohesion: 0.11
Nodes (18): ActiveInvocation, appendStderrExcerpt(), createDuplexRouteSlotController(), createPluginWorkerManager(), DEFAULT_MAX_CONCURRENT_DUPLEX_ROUTES, DUPLEX_ROUTE_INPUT_MAX_BYTES, DUPLEX_ROUTE_PENDING_WRITE_MAX_BYTES, DuplexChannelOpenInput (+10 more)

### Community 63 - "readNonEmptyString"
Cohesion: 0.26
Nodes (19): closeLoginPtyTerminal(), contextForWorkerMessage(), deriveInvocationScope(), handleWorkerNotification(), isRecord(), openLoginPtySession(), queuePreBindLoginPtyExit(), queuePreBindLoginPtyOutput() (+11 more)

### Community 64 - "adapter-defaults.ts"
Cohesion: 0.14
Nodes (14): AdapterDefaults, buildAdapterEnv(), fromRegistryEntry(), getAdapterDefaults(), KNOWN_ADAPTER_TYPES, REGISTRY, resolveRunAdapterType(), AdapterRegistryEntry (+6 more)

### Community 65 - "tenant-orchestrator.ts"
Cohesion: 0.29
Nodes (16): BuildCiliumNetworkPolicyInput, buildCiliumNetworkPolicyManifest(), createIgnoringAlreadyExists(), ensureCiliumNetworkPolicy(), ensureLimitRange(), ensureNamespace(), ensureNetworkPolicies(), ensureNetworkPolicy() (+8 more)

### Community 66 - "plugin-secrets-handler.ts"
Cohesion: 0.16
Nodes (13): assertSecretRefBinding(), createPluginSecretsHandler(), createRateLimiter(), extractSecretRefBindingsFromConfig(), walk(), extractSecretRefPathsFromConfig(), extractSecretRefsFromConfig(), isPlainRecord() (+5 more)

### Community 67 - "plugin-llm-wiki/tests/plugin.spec.ts"
Cohesion: 0.12
Nodes (14): PAPERCLIP_DISTILL_SKILL_KEY, WIKI_MAINTAINER_AGENT_KEY, OPERATION_ORIGIN_KIND, WikiSkillResource, DEFAULT_MANAGED_SKILL, DEFAULT_MANAGED_SKILLS, existingAgent(), mockPageContentsByPath (+6 more)

### Community 68 - "templates.ts"
Cohesion: 0.12
Nodes (14): agentInstructionFiles(), BOOTSTRAP_FILES, DEFAULT_AGENT_INSTRUCTION_FILES, DEFAULT_AGENT_INSTRUCTIONS, DEFAULT_GITIGNORE, DEFAULT_IDEA, DEFAULT_INDEX, DEFAULT_LOG (+6 more)

### Community 69 - "adapter-plugin-store.ts"
Cohesion: 0.25
Nodes (16): adapterPluginPaths(), AdapterPluginRecord, AdapterSettings, addAdapterPlugin(), ensureDirs(), getAdapterPluginByType(), getAdapterPluginsDir(), getDisabledAdapterTypes() (+8 more)

### Community 70 - "plugin-event-bus.ts"
Cohesion: 0.15
Nodes (8): createPluginEventBus(), emit(), matchesPattern(), passesFilter(), PluginEventBus, PluginEventBusEmitResult, ScopedPluginEventBus, Subscription

### Community 71 - "`@paperclipai/plugin-sdk`"
Cohesion: 0.12
Nodes (16): Agent sessions (two-way chat), Bundler presets, Current deployment caveats, Events, Install, Issue Orchestration APIs, Launcher surfaces and modals, Local dev server (hot-reload events) (+8 more)

### Community 72 - "createPaperclipDistillationRun"
Cohesion: 0.17
Nodes (16): appendBoundedSection(), assemblePaperclipSourceBundle(), assertPaperclipSourceScopePayload(), assertRequestedCharacterLimit(), createPaperclipDistillationRun(), createPaperclipDistillationWorkItem(), distillationWorkItemTable(), estimateSourceCostCents() (+8 more)

### Community 73 - "plugin"
Cohesion: 0.14
Nodes (15): createSshConnection(), detectSandboxShellCommand(), ensureSandboxStarted(), evictSandboxHandle(), expiresAtForMinutes(), getOrCreateSession(), getSandbox(), getSandboxOrNull() (+7 more)

### Community 74 - "@paperclipai/plugin-kubernetes (alpha)"
Cohesion: 0.12
Nodes (15): Backends, Configuration, Development, For `job` backend (stable fallback), For `sandbox-cr` backend (default, recommended), Installation, Lessons learned (from openclaw-operator), Migrating from `job` to `sandbox-cr` (+7 more)

### Community 75 - "updateEventIngestionSettings"
Cohesion: 0.26
Nodes (15): countPaperclipProfileOverlaps(), defaultPaperclipIngestionProfile(), evaluatePaperclipProfilePolicy(), eventIngestionStateKey(), getEventIngestionSettings(), getPaperclipIngestionProfile(), normalizeBoolean(), normalizeEventIngestionSettings() (+7 more)

### Community 76 - "Security boundary"
Cohesion: 0.13
Nodes (14): Detection contract, Firm rule, How to apply this rule, Optional CLI installation, Provider isolation assumption, Required on PATH, Runtime dependencies, Sandbox Runtime Requirements (+6 more)

### Community 77 - "Slot component descriptions"
Cohesion: 0.13
Nodes (15): `commentAnnotation`, `commentContextMenuItem`, `contextMenuItem`, `dashboardWidget`, `detailTab`, `globalToolbarButton`, `page`, `projectSidebarItem` (+7 more)

### Community 78 - "createOperationIssue"
Cohesion: 0.16
Nodes (14): buildQueryPrompt(), createOperationIssue(), isTerminalSessionEvent(), operationBillingCode(), operationBillingContext(), operationIssueOriginId(), operationMetadata(), operationPromptWithSpaceContext() (+6 more)

### Community 79 - "plugin-workspace-diff/src/worker.ts"
Cohesion: 0.29
Nodes (10): manifest, plugin, readOptionalString(), readString(), resolveDefaultBaseRef(), resolveProjectWorkspaceDefaultBaseRef(), createGitWorkspace(), execFileAsync (+2 more)

### Community 80 - "executeInSession"
Cohesion: 0.20
Nodes (13): buildLoginShellScript(), createSessionStreamBuffer(), executeInSession(), executeOneShot(), isGitNetworkCommand(), isValidShellEnvKey(), readSessionExitCode(), resolveTimeoutMs() (+5 more)

### Community 81 - "plugin-runtime-sandbox.ts"
Cohesion: 0.20
Nodes (11): DEFAULT_GLOBALS, isWithinRoot(), LoadedModule, loadPluginModuleInSandbox(), looksLikeEsm(), MODULE_PATH_SUFFIXES, normalizeModuleExports(), PluginSandboxError (+3 more)

### Community 82 - "e2b.d.ts"
Cohesion: 0.15
Nodes (6): CommandExitError, e2b, SandboxBackgroundHandle, SandboxNotFoundError, SandboxRunResult, TimeoutError

### Community 83 - "scoped-network-egress.ts"
Cohesion: 0.19
Nodes (11): BuildNetworkPolicyInput, buildNetworkPolicyManifests(), PRIVATE_AND_LINK_LOCAL_EXCEPT_CIDRS, NOTE: operator-supplied CIDRs are intentionally NOT port-scoped —, RFC-1918, appendNetworkEgressDenyHint(), createScopedNetworkEgressPolicy(), createScopedNetworkEgressPolicyOrReleaseWorkload() (+3 more)

### Community 85 - "openDuplexChannel"
Cohesion: 0.27
Nodes (13): bufferPreBindDuplexFrame(), deliverDuplexChannelChunk(), killProcess(), openDuplexChannel(), recordDuplexChannelProtocolError(), replayPreBindDuplexFrames(), resolveDuplexRouteByPair(), retireDuplexWorkerOnViolation() (+5 more)

### Community 86 - "Steps"
Cohesion: 0.15
Nodes (12): 1. Build the plugin, 2. Start paperclip-server in dev mode, 3. Install the plugin via the CLI, 4. Create a company and a kubernetes sandbox environment, 5. Probe the environment, 6. Trigger an agent run, 7. Verify the tenant resources, 8. Tear down (+4 more)

### Community 87 - "createPluginJobScheduler"
Cohesion: 0.24
Nodes (9): createPluginJobScheduler(), advanceSchedulePointer(), dispatchJob(), dispatchManualRun(), ensureNextRunTimestamps(), registerPlugin(), start(), tick() (+1 more)

### Community 89 - "AGENTS.md — LLM Wiki Schema"
Cohesion: 0.17
Nodes (11): AGENTS.md — LLM Wiki Schema, Customization, index.md format, Ingest, Layout, Lint, log.md format, Operations (+3 more)

### Community 90 - "AGENTS.md — LLM Wiki Schema"
Cohesion: 0.17
Nodes (11): AGENTS.md — LLM Wiki Schema, Customization, index.md format, Ingest, Layout, Lint, log.md format, Operations (+3 more)

### Community 91 - "contentHash"
Cohesion: 0.24
Nodes (11): contentHash(), extractWikiLinks(), inferPageType(), inferTitle(), isTemplateFile(), mergeLocalPageRows(), patchForPage(), readTemplate() (+3 more)

### Community 92 - "createPluginToolDispatcher"
Cohesion: 0.22
Nodes (6): createPluginToolDispatcher(), handlePluginEnabled(), registerFromDb(), createPluginToolRegistry(), addTool(), buildName()

### Community 93 - "plugin-orchestration-smoke-example/src/worker.ts"
Cohesion: 0.29
Nodes (6): manifest, plugin, SmokeInput, SmokeSummary, stringField(), tableName()

### Community 94 - "workspace-diff.spec.ts"
Cohesion: 0.24
Nodes (7): WorkspaceDiffQueryOptions, WORKSPACE_DIFF_CAPS, workspaceDiffService(), createTempRepo(), execFileAsync, runGit(), tempDirs

### Community 95 - "buildUntrackedFilePatch"
Cohesion: 0.29
Nodes (10): buildTrackedPatch(), buildUntrackedFilePatch(), buildUntrackedPatch(), countAddedLines(), isProbablyBinary(), isWithinDirectory(), reservePatchBytes(), resolveWorkspaceFilePath() (+2 more)

### Community 96 - "LLM Wiki"
Cohesion: 0.20
Nodes (9): Architecture, Indexing and logging, LLM Wiki, Note, Operations, Optional: CLI tools, The core idea, Tips and tricks (+1 more)

### Community 97 - "LLM Wiki"
Cohesion: 0.20
Nodes (9): Alpha Verification, Build Options, Development, Install Into Paperclip, LLM Wiki, Local File Layout, Managed Agent Instructions, Phase 5 Security Gate (+1 more)

### Community 98 - "LLM Wiki"
Cohesion: 0.20
Nodes (9): Architecture, Indexing and logging, LLM Wiki, Note, Operations, Optional: CLI tools, The core idea, Tips and tricks (+1 more)

### Community 99 - "plugin-file-browser-example/src/worker.ts"
Cohesion: 0.33
Nodes (6): manifest, extractFilePaths(), looksLikePath(), plugin, resolveWorkspace(), sanitizeWorkspacePath()

### Community 100 - "plugin-manifest-validator.ts"
Cohesion: 0.22
Nodes (5): ManifestParseFailure, ManifestParseResult, ManifestParseSuccess, PluginManifestValidator, SUPPORTED_VERSIONS

### Community 101 - "closeDuplexChannelRouteOnWorkerExit"
Cohesion: 0.22
Nodes (7): acquireDuplexRouteSlot(), acquireLoginPtyRouteSlot(), clearDuplexChannelLifetimeTimer(), closeDuplexChannelRouteOnWorkerExit(), releaseDuplexRouteSlot(), releaseLoginPtyRouteSlot(), DuplexRouteSlotController

### Community 102 - "`@paperclipai/plugin-modal`"
Cohesion: 0.22
Nodes (8): Configuration, Install, Local development, Operator verification, Package layout, `@paperclipai/plugin-modal`, Reuse semantics, Runtime support note

### Community 103 - "pod-exec.ts"
Cohesion: 0.32
Nodes (7): execInPod(), execInPodStreaming(), NOTE: `stdinPayload.length` is the Buffer's BYTE length (correct for, NOTE: tty=false so stdout and stderr arrive on separate channels. If tty=true, shQuote(), WebSocketLike, wrapCommandWithEnv()

### Community 105 - "buildHostServices"
Cohesion: 0.29
Nodes (5): buildHostServices(), getStoredLocalFolders(), setStoredLocalFolder(), PluginStateStore, scopeConditions()

### Community 106 - "plugin-host-service-cleanup.ts"
Cohesion: 0.25
Nodes (3): LifecycleLike, PluginHostServiceCleanupController, PluginWorkerRuntimeEvent

### Community 107 - "File Browser Example Plugin"
Cohesion: 0.25
Nodes (7): Capabilities, File Browser Example Plugin, Local Install (Dev), Settings, Slots, Structure, Worker

### Community 108 - "UI slots and launchers"
Cohesion: 0.25
Nodes (8): Capabilities, External Object Reference Providers, Launcher actions and render options, Restricted Database Namespace, Scoped API Routes, Slot types / launcher placement zones, Trusted Local Folders, UI slots and launchers

### Community 109 - "issue-attachments.ts"
Cohesion: 0.43
Nodes (5): FetchLike, IngestSourceActionResult, readIngestOperationIssueId(), readUploadError(), uploadIssueAttachmentFile()

### Community 110 - "wiki-route-sidebar-ui.spec.ts"
Cohesion: 0.29
Nodes (3): BridgeGlobal, FileTreeNodeLike, FileTreePropsLike

### Community 112 - "image-allowlist.ts"
Cohesion: 0.38
Nodes (6): globMatch(), resolveImage(), ResolveImageConfig, ResolveImageDefaults, ResolveImageInput, rewriteRegistry()

### Community 113 - "upload-interceptor.ts"
Cohesion: 0.29
Nodes (4): BufferState, FastUploadInterceptor, InterceptDecision, InterceptStateFlush

### Community 114 - "requestedCompanyScope"
Cohesion: 0.38
Nodes (7): gated(), isRecord(), readNonEmptyString(), requestedCompanyScope(), requireCapability(), requireInvocationCompanyScope(), resolveRequiredCompanyId()

### Community 115 - "Index"
Cohesion: 0.29
Nodes (6): Concepts, Entities, Index, Projects, Sources, Synthesis

### Community 116 - "Index"
Cohesion: 0.29
Nodes (6): Concepts, Entities, Index, Projects, Sources, Synthesis

### Community 117 - "Cloudflare Sandbox Bridge Template"
Cohesion: 0.29
Nodes (6): Cloudflare Sandbox Bridge Template, Deploy, Local development, Notes, Prerequisites, What it does

### Community 122 - "plugin-capability-validator.ts"
Cohesion: 0.33
Nodes (5): CapabilityCheckResult, FEATURE_CAPABILITIES, LAUNCHER_PLACEMENT_CAPABILITIES, OPERATION_CAPABILITIES, UI_SLOT_CAPABILITIES

### Community 125 - "@paperclipai/plugin-hello-world-example"
Cohesion: 0.33
Nodes (5): API Surface, Local Install (Dev), Notes, @paperclipai/plugin-hello-world-example, What It Demonstrates

### Community 126 - "Plugin Orchestration Smoke Example"
Cohesion: 0.33
Nodes (5): Development, Install Into Paperclip, Plugin Orchestration Smoke Example, Scoped Route Smoke, What it exercises

### Community 127 - "LLM Wiki Maintainer"
Cohesion: 0.33
Nodes (5): Identity, LLM Wiki Maintainer, Operating Loop, Skills, Wiki Root

### Community 128 - "`@paperclipai/plugin-cloudflare-sandbox`"
Cohesion: 0.33
Nodes (5): Bridge template, Configuration, Install, Local development, `@paperclipai/plugin-cloudflare-sandbox`

### Community 129 - "Directory-constraint (`bwrap`) findings for the Daytona session path"
Cohesion: 0.33
Nodes (5): Directory-constraint (`bwrap`) findings for the Daytona session path, Removal scope, Summary, What a future re-introduction needs, Why the goal is dropped for now

### Community 130 - "`@paperclipai/plugin-daytona`"
Cohesion: 0.33
Nodes (5): Configuration, Install, Local development, Package layout, `@paperclipai/plugin-daytona`

### Community 131 - "`@paperclipai/plugin-e2b`"
Cohesion: 0.33
Nodes (5): Configuration, Install, Local development, Package layout, `@paperclipai/plugin-e2b`

### Community 132 - "`@paperclipai/plugin-exe-dev`"
Cohesion: 0.33
Nodes (5): Configuration, Install, Local development, Package layout, `@paperclipai/plugin-exe-dev`

### Community 133 - "`@paperclipai/plugin-novita-sandbox`"
Cohesion: 0.33
Nodes (5): Configuration, Install, Local development, Package layout, `@paperclipai/plugin-novita-sandbox`

### Community 134 - "Hooks reference"
Cohesion: 0.33
Nodes (6): Hooks reference, `useHostContext()`, `useHostNavigation()`, `usePluginAction(key)`, `usePluginData<T>(key, params?)`, `usePluginStream<T>(channel, options?)`

### Community 135 - "UI authoring note"
Cohesion: 0.33
Nodes (6): Shared Assignee and Project Pickers, Shared FileTree, Shared Markdown Components, Slot component props, UI authoring note, UI quick start

### Community 138 - "_kind-harness.ts"
Cohesion: 0.50
Nodes (3): deleteNamespaceIfExists(), KIND_CONTEXT, kubectl()

### Community 143 - "Plugin Authoring Smoke Example"
Cohesion: 0.40
Nodes (4): Build Options, Development, Install Into Paperclip, Plugin Authoring Smoke Example

### Community 144 - "Real-time streaming (`ctx.streams`)"
Cohesion: 0.40
Nodes (5): Host-side architecture, Real-time streaming (`ctx.streams`), Streaming agent responses to the UI, UI side, Worker side

### Community 149 - "@paperclipai/plugin-kitchen-sink-example"
Cohesion: 0.50
Nodes (3): Install, Notes, @paperclipai/plugin-kitchen-sink-example

### Community 150 - "defaultWikiSpaceRow"
Cohesion: 1.00
Nodes (3): defaultWikiSpaceRow(), mockPersistedWikiSpace(), wikiSpaceRow()

## Knowledge Gaps
- **708 isolated node(s):** `pluginCompanySettings`, `pluginConfig`, `pluginDatabaseNamespaces`, `pluginMigrations`, `pluginEntities` (+703 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **35 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ScopedPluginEventBus` connect `plugin-event-bus.ts` to `sandboxHandleCache`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `sandboxHandleCache` connect `sandboxHandleCache` to `plugin`, `daytona/src/plugin.ts`, `sdk/src/index.ts`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `namespace()` connect `host-client-factory.ts` to `kubernetes/src/plugin.ts`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **What connects `pluginCompanySettings`, `pluginConfig`, `pluginDatabaseNamespaces` to the rest of the system?**
  _708 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `sdk/src/types.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.021052631578947368 - nodes in this community are weakly interconnected._
- **Should `sdk/src/index.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.044568868980963045 - nodes in this community are weakly interconnected._
- **Should `core.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.029001367989056087 - nodes in this community are weakly interconnected._