# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 110 files · ~164,091 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1300 nodes · 2395 edges · 94 communities (84 shown, 10 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 49 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- services/agents.ts
- services/built-in-agents.ts
- AgentSkillsTab.tsx
- agentRoutes
- validators/agent.ts
- agent-instructions.ts
- SidebarAgents.tsx
- types/agent.ts
- OrgChart.tsx
- AgentConfigForm.tsx
- pluginManagedAgentService
- AgentDetail.tsx
- AgentDetail.production.tsx
- Agents.tsx
- Agents.production.tsx
- NewAgentSetup.tsx
- builtInAgentService
- agent-eligibility.ts
- org-chart-svg.ts
- findSingleAgent
- AgentSecretAccessEditor.tsx
- services/managed-agent-profiles.ts
- api/agents.ts
- services/remote-agent-profiles.ts
- agentmail-api.ts
- ensure
- AgentContextualSidebar.tsx
- agent-conversations.ts
- AgentActionButtons.tsx
- schema/agents.ts
- ConfigureBuiltInAgentModal.tsx
- AgentConfigForm
- agent-auth-jwt.ts
- routes/agents.ts
- agent-invokability.ts
- readBuiltInAgentMarker
- recent-agent-chats.ts
- asRecord
- InboxAgentPolicyControl.tsx
- redactPathText
- LogViewer
- LogViewer
- AgentToolsTab.tsx
- AgentCapsule.tsx
- NewAgentDialog.tsx
- asNonEmptyString
- routes/built-in-agents.ts
- agent-assignability.ts
- builtInAgents.ts
- IssueChatFeedbackButtons
- AgentIconPicker.tsx
- AgentDetail
- redactPathText
- asNonEmptyString
- cardWidth
- agent-action-audit.ts
- Setup
- AgentsUsingSkillDialog.tsx
- agent-task-run-telemetry.ts
- ActiveAgentsPanel.tsx
- asNonEmptyString
- validateManagedAgentBinding
- inboxAgentPolicyRoutes
- AgentChat.tsx
- buildNewAgentRuntimeConfig
- buildAgentDetail
- defaultRenderCard
- agentmail.ts
- default-agent-instructions.ts
- agent-config-patch.ts
- onboarding-agent-role.ts
- agent-url-key.ts
- types/inbox-agent-policy.ts
- validators/inbox-agent-policy.ts
- materializeDefaultInstructionsBundleForNewAgent
- assertSetupTokenLoginProviderCapability
- resolveDesiredSkillAssignment
- agent-start-lock.ts
- inboxAgentPolicyService
- legacy-agent-config.ts
- claude-agent-id-header.ts
- assertFreshPaperclipRunnerProvider
- decideAgentRead
- assertCanApplyProtectedAgentChange
- built-in-agent-toast.ts
- restoreAgentConfigHistoryEntry
- getRunSnapshotIssueId
- managed_agent_profiles.ts
- remote_agent_profiles.ts
- user_inbox_agent_policies.ts
- AgentApiKeyScope
- KeysTab

## God Nodes (most connected - your core abstractions)
1. `agentRoutes()` - 104 edges
2. `builtInAgentService()` - 49 edges
3. `agentService()` - 33 edges
4. `agentsApi` - 24 edges
5. `AgentConfigForm()` - 20 edges
6. `pluginManagedAgentService()` - 19 edges
7. `ensure()` - 18 edges
8. `deriveBundleState()` - 15 edges
9. `LogViewer()` - 15 edges
10. `LogViewer()` - 15 edges
11. `agentInstructionsService()` - 14 edges
12. `updateAgent()` - 14 edges
13. `provision()` - 14 edges
14. `readBuiltInAgentMarker()` - 13 edges
15. `AgentSkillsTab()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `assertExternalInstructionsAdmin()` --calls--> `agentInstructionsBundleMode()`  [EXTRACTED]
  server/src/routes/agents.ts → server/src/services/agent-instructions.ts
- `agentRoutes()` --calls--> `renderOrgChartPng()`  [EXTRACTED]
  server/src/routes/agents.ts → server/src/routes/org-chart-svg.ts
- `agentRoutes()` --calls--> `renderOrgChartSvg()`  [EXTRACTED]
  server/src/routes/agents.ts → server/src/routes/org-chart-svg.ts
- `agentRoutes()` --calls--> `agentInstructionsService()`  [EXTRACTED]
  server/src/routes/agents.ts → server/src/services/agent-instructions.ts
- `agentRoutes()` --calls--> `syncInstructionsBundleConfigFromFilePath()`  [EXTRACTED]
  server/src/routes/agents.ts → server/src/services/agent-instructions.ts

## Import Cycles
- None detected.

## Communities (94 total, 10 thin omitted)

### Community 0 - "services/agents.ts"
Cohesion: 0.07
Nodes (53): AgentPermissionsContext, asRecord(), defaultAgentPermissions(), normalizeAgentPermissions(), NormalizedAgentPermissions, permissionsImplyLowTrust(), AgentSecretBindingSyncService, asRecord() (+45 more)

### Community 1 - "services/built-in-agents.ts"
Cohesion: 0.05
Nodes (42): AUTO_PROVISION_ON_COMPANY_CREATE_KEYS, BUILT_IN_AGENT_DEFAULT_GRANTS, BUILT_INS_DIR, BuiltInAgentBundleDefinition, BuiltInAgentDefinition, builtInAgentNotConfiguredError(), BuiltInAgentProvisionActor, BuiltInAgentProvisionInput (+34 more)

### Community 2 - "AgentSkillsTab.tsx"
Cohesion: 0.08
Nodes (35): AgentSkillDraftState, AgentSkillSnapshotApplyResult, applyAgentSkillSnapshot(), arraysEqual(), isReadOnlyUnmanagedSkillEntry(), sameSkillSelection(), shouldScheduleSkillAutosave(), agentSkillMatchesSearch() (+27 more)

### Community 3 - "agentRoutes"
Cohesion: 0.05
Nodes (18): agentRoutes(), allowedEnvironmentDriversForAgent(), assertAgentEnvironmentSelection(), assertBoardCanManageAgentsForCompany(), assertCanReadAgent(), assertCanReadConfigurations(), assertDeviceLoginAdapter(), assertExternalInstructionsAdmin() (+10 more)

### Community 4 - "validators/agent.ts"
Cohesion: 0.05
Nodes (41): adapterConfigSchema, agentApiKeyScopeSchema, agentInstructionsBundleModeSchema, AgentMineInboxQuery, agentMineInboxQuerySchema, agentPermissionsSchema, agentRuntimeConfigSchema, BuiltInAgentEmptyMutation (+33 more)

### Community 5 - "agent-instructions.ts"
Cohesion: 0.16
Nodes (40): AgentInstructionsBundle, agentInstructionsBundleMode(), AgentInstructionsFileDetail, AgentInstructionsFileSummary, agentInstructionsService(), deleteFile(), ensureWritableBundle(), exportFiles() (+32 more)

### Community 6 - "SidebarAgents.tsx"
Cohesion: 0.11
Nodes (34): BuiltInAgentStatus, BuiltInLifecycleChip(), AGENT_SORT_CHOICES, agentTimestamp(), AGENT_SORT_CHOICES, agentTimestamp(), SidebarAgents(), sortAgents() (+26 more)

### Community 7 - "types/agent.ts"
Cohesion: 0.06
Nodes (39): AgentOrgChainHealth, ADAPTER_AUTH_PANEL_MODES, ADAPTER_AUTH_SESSION_INTERNAL_STATUSES, ADAPTER_AUTH_SESSION_STATUSES, AdapterAuthPanelMode, AdapterAuthSessionFailure, AdapterAuthSessionInternalStatus, AdapterAuthSessionOwnerResponse (+31 more)

### Community 8 - "OrgChart.tsx"
Cohesion: 0.09
Nodes (37): OrgNode, clampZoom(), collectEdges(), walk(), fitChartToViewport(), flattenLayout(), walk(), layoutForest() (+29 more)

### Community 9 - "AgentConfigForm.tsx"
Cohesion: 0.07
Nodes (23): adapterLabels, CollapsibleSection(), DraftInput(), DraftNumberInput(), help, roleLabels, ToggleField(), ToggleWithNumber() (+15 more)

### Community 10 - "pluginManagedAgentService"
Cohesion: 0.18
Nodes (29): adapterPreference(), applyInstructionTemplateVariables(), bindingExternalId(), declarationPatch(), declaredInstructionFiles(), fallbackAdapterType(), managedAgentPauseReason(), managedMetadata() (+21 more)

### Community 11 - "AgentDetail.tsx"
Cohesion: 0.10
Nodes (22): AGENT_DETAIL_TABS, AgentRevisionsTab(), ConfigurationTab(), DISCARD_AGENT_CONFIG_CHANGES_MESSAGE, getRunSnapshotIssueId(), isMarkdown(), KeysTab(), LatestRunCard() (+14 more)

### Community 12 - "AgentDetail.production.tsx"
Cohesion: 0.09
Nodes (20): AgentChannelsPanel(), providerNames, AGENT_DETAIL_TABS, AgentConfigurePage(), AgentDetailView, ConfigurationTab(), DISCARD_AGENT_CONFIG_CHANGES_MESSAGE, isMarkdown() (+12 more)

### Community 13 - "Agents.tsx"
Cohesion: 0.12
Nodes (22): AGENT_FILTER_TAB_ITEMS, AGENT_FILTER_TABS, AgentMetaColumns(), Agents(), AgentsView, ConfigureBuiltInAgentModal, describeEnvironment(), describeMissingEnvironment() (+14 more)

### Community 14 - "Agents.production.tsx"
Cohesion: 0.12
Nodes (21): AGENT_FILTER_TAB_ITEMS, AGENT_FILTER_TABS, AgentMetaColumns(), Agents(), ConfigureBuiltInAgentModal, describeEnvironment(), describeMissingEnvironment(), EnvironmentDescriptor (+13 more)

### Community 15 - "NewAgentSetup.tsx"
Cohesion: 0.14
Nodes (15): AdapterLoginPanel(), AdapterMark(), AgentBasics, AgentBasicsDialog(), brandMarks, AgentProviderConnection(), ProviderConnection, NewAgentSetup() (+7 more)

### Community 16 - "builtInAgentService"
Cohesion: 0.24
Nodes (22): builtInAgentService(), bundleResourceStates(), createOrResetRoutine(), currentInstructionFiles(), getCurrentSkillFiles(), getManagedResourceBinding(), getRoutineByBinding(), importBundledSkill() (+14 more)

### Community 17 - "agent-eligibility.ts"
Cohesion: 0.15
Nodes (19): AgentEligibilityAgent, AgentEligibilityLifecycleReason, AgentInvalidOrgChainAncestor, AgentOrgChainEntry, AgentOrgChainInvalidReason, AgentWorkEligibility, ASSIGNABLE_AGENT_STATUSES, buildRepairGuidance() (+11 more)

### Community 18 - "org-chart-svg.ts"
Cohesion: 0.17
Nodes (18): collapseToAvatars(), countNodes(), estimateNextLevelWidth(), flattenDescendants(), LayoutNode, nodesAtDepth(), OrgChartOverlay, renderCards() (+10 more)

### Community 19 - "findSingleAgent"
Cohesion: 0.19
Nodes (20): autoProvisionBundledAgents(), ensureAgentDefaultGrants(), ensureBuiltInAgentAssignable(), ensureBuiltInAgentDefaultGrants(), ensureCompany(), ensureCompanyDefaultAgentGrants(), ensureRootAgentDefaultChangeGrants(), findSingleAgent() (+12 more)

### Community 20 - "AgentSecretAccessEditor.tsx"
Cohesion: 0.18
Nodes (18): AccessRow, AgentSecretAccessEditor(), addRow(), emit(), patchRow(), removeRow(), AgentSecretAccessEditorProps, AgentSecretBindingSummary (+10 more)

### Community 21 - "services/managed-agent-profiles.ts"
Cohesion: 0.20
Nodes (16): managedAgentProfileRoutes(), profileInput(), assertQualifiedRevisionUnchanged(), CLAUDE_MANAGED_BETA_VERSION, computeManagedAgentProfileRevision(), ManagedAgentProfileInput, ManagedAgentProfileRevisionInput, managedAgentProfileService() (+8 more)

### Community 22 - "api/agents.ts"
Cohesion: 0.13
Nodes (13): AdapterModel, AgentHireResponse, AgentKey, agentPath(), AgentPermissionUpdate, agentsApi, AgentWakeRequest, AvailableSkill (+5 more)

### Community 23 - "services/remote-agent-profiles.ts"
Cohesion: 0.22
Nodes (15): profileInput(), remoteAgentProfileRoutes(), remoteAgentService(), AGENTCORE_CONFIGURATION_KEYS, assertQualifiedRevisionUnchanged(), computeRemoteAgentProfileRevision(), RemoteAgentProfileInput, remoteAgentProfileService() (+7 more)

### Community 24 - "agentmail-api.ts"
Cohesion: 0.12
Nodes (8): AGENTMAIL_EVENTS, agentmailApi(), AgentmailApiError, AgentmailInbox, AgentmailMessage, agentmailMessageSchema, AgentmailScope, strings

### Community 25 - "ensure"
Cohesion: 0.20
Nodes (17): withBuiltInAgentMarker(), assertAdapterAllowed(), assertKnownBuiltInAgentModel(), defaultProvisionInput(), ensure(), findSingleRootManager(), provision(), builtInMetadata() (+9 more)

### Community 26 - "AgentContextualSidebar.tsx"
Cohesion: 0.19
Nodes (14): AgentContextualSidebar(), auditItems, localIcons, AGENT_DETAIL_NAVIGATION, agentDetailHref(), AgentDetailView, agentLegacyAuditSection(), AgentLocalDetailView (+6 more)

### Community 27 - "agent-conversations.ts"
Cohesion: 0.23
Nodes (13): AGENT_CHAT_DIRECTIVE, ConversationIdentity, conversationReplay(), deliverConversationComments(), isConversation(), isConversationExecutionWake(), isConversationReset(), isSupersededConversationRun() (+5 more)

### Community 28 - "AgentActionButtons.tsx"
Cohesion: 0.20
Nodes (9): AgentActionButtons(), duplicateInstructionFilePath(), loadDuplicateInstructionsBundle(), buildDuplicateAgentPayload(), cloneRecord(), duplicateAgentName(), DuplicateAgentSource, DuplicateInstructionsBundle (+1 more)

### Community 29 - "schema/agents.ts"
Cohesion: 0.19
Nodes (8): agentApiKeys, agentConfigRevisions, agentMemberships, agentRuntimeState, agentSessionGoalActions, agentTaskSessions, agentWakeupRequests, agents

### Community 30 - "ConfigureBuiltInAgentModal.tsx"
Cohesion: 0.20
Nodes (11): builtInAgentsApi, BuiltInAgentState, Field(), AdapterTypeDropdown(), ModelDropdown(), BuiltInAgentGateProps, ConfigureBuiltInAgentModal(), ConfigureBuiltInAgentModalProps (+3 more)

### Community 31 - "AgentConfigForm"
Cohesion: 0.15
Nodes (12): AgentConfigForm(), mark(), updateMaxTurnContinuation(), clampDelayMsFromSeconds(), clampInteger(), formatArgList(), isOverlayDirty(), overlayValuesEqual() (+4 more)

### Community 32 - "agent-auth-jwt.ts"
Cohesion: 0.27
Nodes (13): base64UrlDecode(), base64UrlEncode(), createLocalAgentJwt(), deriveCompanySigningKey(), jwtConfig(), JwtHeader, LocalAgentJwtClaims, parseBooleanEnv() (+5 more)

### Community 33 - "routes/agents.ts"
Cohesion: 0.14
Nodes (11): AGENT_SKILL_ASSIGNMENT_MODES, resolveAgentSelfTrustPreset(), hireRunLocks, readLiveRunsQueryInt(), readRunIssueId(), readRunLogLimitBytes(), requireAgentSkillAssignmentMode(), withHireRunLock() (+3 more)

### Community 34 - "agent-invokability.ts"
Cohesion: 0.20
Nodes (12): AgentInvokability, AgentInvokabilityBlockReason, AgentOrgRow, AgentStatus, blocked(), DIRECT_NON_INVOKABLE_STATUSES, evaluateAgentInvokability(), evaluateAgentInvokabilityFromDb() (+4 more)

### Community 35 - "readBuiltInAgentMarker"
Cohesion: 0.22
Nodes (11): assertBuiltInAgentMetadataMutationAllowed(), BUILT_IN_AGENT_METADATA_KEY, BuiltInAgentMarker, builtInAgentMarkersEqual(), isPlainRecord(), normalizeFeatureKeys(), readBuiltInAgentMarker(), findMarkedRows() (+3 more)

### Community 36 - "recent-agent-chats.ts"
Cohesion: 0.32
Nodes (10): AgentChatSidebar(), SidebarAgentChats(), key(), memory, orderChatAgents(), parseRecentAgentChats(), read(), recordAgentChatVisit() (+2 more)

### Community 37 - "asRecord"
Cohesion: 0.23
Nodes (12): applyCodexLocalKeyIsolation(), asEnvBindingString(), asRecord(), assertProviderTraceSettingTransition(), codexLocalAgentHome(), codexLocalEnvKeyConfigured(), normalizeNewAgentRuntimeConfig(), parseBooleanLike() (+4 more)

### Community 38 - "InboxAgentPolicyControl.tsx"
Cohesion: 0.21
Nodes (7): inboxAgentPolicyApi, AgentMultiSelect(), AgentMultiSelectOption, Draft, InboxAgentPolicyControl(), MODE_OPTIONS, policyKey()

### Community 39 - "redactPathText"
Cohesion: 0.24
Nodes (12): asRecord(), formatEnvForDisplay(), parseStoredLogContent(), redactCommandText(), redactEnvValue(), redactPathText(), redactPathValue(), RunInvocationCard() (+4 more)

### Community 40 - "LogViewer"
Cohesion: 0.21
Nodes (11): findScrollContainer(), heartbeatProgressLogLineKey(), isElementScrollContainer(), isWindowContainer(), LogViewer(), appendLogContent(), appendLogLines(), loadMorePersistedLog() (+3 more)

### Community 41 - "LogViewer"
Cohesion: 0.21
Nodes (11): findScrollContainer(), heartbeatProgressLogLineKey(), isElementScrollContainer(), isWindowContainer(), LogViewer(), appendLogContent(), appendLogLines(), loadMorePersistedLog() (+3 more)

### Community 42 - "AgentToolsTab.tsx"
Cohesion: 0.24
Nodes (7): AgentToolsTab(), isEligibleGitHubIdentityConnection(), isGitHubConnection(), mergeInstallDraft(), POLICY_EFFECT_LABEL, policyGovernsAgent(), selectorStringList()

### Community 43 - "AgentCapsule.tsx"
Cohesion: 0.20
Nodes (10): AGENT_GRADIENT_COUNT, AgentCapsule(), AgentCapsuleGlow, AgentCapsuleProps, AgentCapsuleSizePreset, AgentCapsuleState, normalizeGradient(), SIZE_PRESETS (+2 more)

### Community 44 - "NewAgentDialog.tsx"
Cohesion: 0.27
Nodes (5): ExternalAgentInviteDialog(), AgentOnboardingPromptInput, buildAgentOnboardingPrompt(), buildCandidateOnboardingUrls(), buildResolutionTestUrl()

### Community 45 - "asNonEmptyString"
Cohesion: 0.22
Nodes (11): asNonEmptyString(), asRecord(), buildHeartbeatProgressLogLine(), CostsSection(), RunDetail(), runDetailRefetchIntervalMs(), RunListItem(), runMetrics() (+3 more)

### Community 46 - "routes/built-in-agents.ts"
Cohesion: 0.24
Nodes (5): builtInAgentRoutes(), formatScheduleLabel(), redactBuiltInAgentListState(), WEEKDAY_LABELS, BuiltInAgentState

### Community 47 - "agent-assignability.ts"
Cohesion: 0.31
Nodes (9): AgentAssignmentConflictReason, AgentAssignmentKind, assertAssignableAgent(), AssignabilityAgent, assignmentMessage(), assignmentReasonFromHealth(), conflictDetails(), getAgent() (+1 more)

### Community 48 - "builtInAgents.ts"
Cohesion: 0.20
Nodes (9): BUILT_IN_AGENT_NOT_CONFIGURED_CODE, BUILT_IN_AGENT_PAUSED_CODE, BuiltInAgentBundleMeta, BuiltInAgentDefinition, BuiltInAgentProvisionInput, BuiltInManagedResourceKind, BuiltInManagedResourceState, BuiltInManagedResourceStockStatus (+1 more)

### Community 49 - "IssueChatFeedbackButtons"
Cohesion: 0.29
Nodes (6): IssueChatFeedbackButtons(), doVote(), handleSubmitReason(), handleThumbsDown(), handleThumbsUp(), handleVote()

### Community 50 - "AgentIconPicker.tsx"
Cohesion: 0.29
Nodes (6): AgentIcon(), AgentIconPicker(), AgentIconPickerProps, AgentIconProps, AGENT_ICONS, getAgentIcon()

### Community 51 - "AgentDetail"
Cohesion: 0.22
Nodes (7): agentConfigHistoryRestoreDelta(), AgentDetail(), handlePopState(), confirmAgentConfigNavigation(), formatOrgChainHealthPath(), parseAgentDetailView(), restoreAgentConfigHistoryEntry()

### Community 52 - "redactPathText"
Cohesion: 0.33
Nodes (9): formatEnvForDisplay(), parseStoredLogContent(), redactCommandText(), redactEnvValue(), redactPathText(), redactPathValue(), RunInvocationCard(), shouldRedactSecretValue() (+1 more)

### Community 53 - "asNonEmptyString"
Cohesion: 0.29
Nodes (8): applyCreateDefaultsByAdapterType(), asNonEmptyString(), ensureGatewayDeviceKey(), evaluateClaudeAuthSignal(), evaluateCodexAuthSignal(), generateEd25519PrivateKeyPem(), resolveInstructionsFilePath(), resolvePaperclipRunnerAdapterTransition()

### Community 54 - "cardWidth"
Cohesion: 0.29
Nodes (8): avatarGridHeight(), avatarGridRows(), avatarGridWidth(), cardHeight(), cardWidth(), layoutTree(), measureText(), subtreeWidth()

### Community 55 - "agent-action-audit.ts"
Cohesion: 0.36
Nodes (7): AgentActionAuditFilters, agentActionAuditService(), CursorValue, cursorValueSchema, decodeCursor(), encodeCursor(), excerpt()

### Community 56 - "Setup"
Cohesion: 0.50
Nodes (8): blocking(), Setup(), buildConfig(), finish(), pendingCredentials(), preparedConfig(), runTest(), testAgentSetup()

### Community 57 - "AgentsUsingSkillDialog.tsx"
Cohesion: 0.29
Nodes (3): AgentsUsingSkillDialog(), desiredSetsEqual(), SkillChange

### Community 58 - "agent-task-run-telemetry.ts"
Cohesion: 0.48
Nodes (6): emitAgentTaskRun(), emitAgentTaskRunById(), HeartbeatRun, readNonEmptyString(), readUsageToken(), resolveDurationSeconds()

### Community 59 - "ActiveAgentsPanel.tsx"
Cohesion: 0.29
Nodes (5): ActiveAgentsPanelProps, AgentRunCard, EMPTY_RUNS, EMPTY_TRANSCRIPT, runStatusLabels

### Community 60 - "asNonEmptyString"
Cohesion: 0.33
Nodes (7): asNonEmptyString(), buildHeartbeatProgressLogLine(), RunDetail(), runDetailRefetchIntervalMs(), RunListItem(), runMetrics(), usageNumber()

### Community 61 - "validateManagedAgentBinding"
Cohesion: 0.33
Nodes (6): assertAdapterTestEnvironmentForCompany(), buildSandboxIdentityCheck(), readMetadataString(), resolveAdapterTestExecutionContext(), testManagedEnvironment(), validateManagedAgentBinding()

### Community 63 - "AgentChat.tsx"
Cohesion: 0.53
Nodes (3): agentChatsApi, useAgentChatEnabled(), AgentChat()

### Community 64 - "buildNewAgentRuntimeConfig"
Cohesion: 0.53
Nodes (3): defaultCreateValues, buildNewAgentHirePayload(), buildNewAgentRuntimeConfig()

### Community 65 - "buildAgentDetail"
Cohesion: 0.40
Nodes (5): buildAgentAccessState(), buildAgentDetail(), canCreateAgents(), redactAgentRowForResponse(), redactForRestrictedAgentView()

### Community 66 - "defaultRenderCard"
Cohesion: 0.40
Nodes (5): defaultRenderCard(), escapeXml(), getRoleInfo(), guessRoleTag(), renderEmojiAvatar()

### Community 67 - "agentmail.ts"
Cohesion: 0.40
Nodes (3): AGENTMAIL_EMAIL_CONTRACT, AGENTMAIL_TOOLS, schema

### Community 68 - "default-agent-instructions.ts"
Cohesion: 0.50
Nodes (4): DEFAULT_AGENT_BUNDLE_FILES, DefaultAgentBundleRole, loadDefaultAgentInstructionsBundle(), resolveDefaultAgentBundleUrl()

### Community 69 - "agent-config-patch.ts"
Cohesion: 0.50
Nodes (4): buildAdapterConfigForTest(), AgentConfigOverlay, buildAgentUpdatePatch(), omitUndefinedEntries()

### Community 70 - "onboarding-agent-role.ts"
Cohesion: 0.40
Nodes (3): DEFAULT_AGENT_NAME, DEFAULT_AGENT_ROLE, WIZARD_SUPPLIED_NAMES

### Community 72 - "types/inbox-agent-policy.ts"
Cohesion: 0.50
Nodes (3): INBOX_AGENT_POLICY_MODES, InboxAgentPolicy, InboxAgentPolicyMode

### Community 73 - "validators/inbox-agent-policy.ts"
Cohesion: 0.50
Nodes (3): inboxAgentPolicyModeSchema, UpdateInboxAgentPolicy, updateInboxAgentPolicySchema

### Community 74 - "materializeDefaultInstructionsBundleForNewAgent"
Cohesion: 0.50
Nodes (4): adapterSupportsInstructionsBundle(), assertNoNewAgentLegacyPromptTemplate(), materializeDefaultInstructionsBundleForNewAgent(), resolveDefaultAgentInstructionsBundleRole()

### Community 75 - "assertSetupTokenLoginProviderCapability"
Cohesion: 0.50
Nodes (4): assertCodexLoginProviderCapability(), assertSandboxLoginEnvironment(), assertSetupTokenLoginProviderCapability(), resolveProviderSupportsLoginPty()

### Community 76 - "resolveDesiredSkillAssignment"
Cohesion: 0.50
Nodes (4): buildRuntimeSkillConfig(), resolveDesiredSkillAssignment(), shouldMaterializeRuntimeSkillsForAdapter(), mergeDesiredSkillEntries()

### Community 77 - "agent-start-lock.ts"
Cohesion: 0.67
Nodes (3): startLocksByAgent, waitForAgentStartLock(), withAgentStartLock()

### Community 79 - "legacy-agent-config.ts"
Cohesion: 0.83
Nodes (3): asNonEmptyString(), hasLegacyWorkingDirectory(), shouldShowLegacyWorkingDirectoryField()

### Community 81 - "assertFreshPaperclipRunnerProvider"
Cohesion: 0.67
Nodes (3): assertAdapterConfigConstraints(), assertFreshPaperclipRunnerProvider(), normalizeMediatedAdapterConfigForPersistence()

### Community 82 - "decideAgentRead"
Cohesion: 0.67
Nodes (3): assertAgentReadAllowed(), decideAgentRead(), filterAgentsForActor()

### Community 83 - "assertCanApplyProtectedAgentChange"
Cohesion: 0.67
Nodes (3): assertCanApplyAgentProfileChange(), assertCanApplyProtectedAgentChange(), assertCanManageInstructionsPath()

### Community 85 - "restoreAgentConfigHistoryEntry"
Cohesion: 0.67
Nodes (3): agentConfigHistoryRestoreDelta(), handlePopState(), restoreAgentConfigHistoryEntry()

### Community 86 - "getRunSnapshotIssueId"
Cohesion: 1.00
Nodes (3): getRunSnapshotIssueId(), LatestRunCard(), resolveLatestRunNavigation()

## Knowledge Gaps
- **315 isolated node(s):** `agentApiKeys`, `agentConfigRevisions`, `agentMemberships`, `agentRuntimeState`, `agentTaskSessions` (+310 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `agentRoutes()` connect `agentRoutes` to `routes/agents.ts`, `buildAgentDetail`, `agent-invokability.ts`, `asRecord`, `agent-instructions.ts`, `materializeDefaultInstructionsBundleForNewAgent`, `assertSetupTokenLoginProviderCapability`, `resolveDesiredSkillAssignment`, `assertFreshPaperclipRunnerProvider`, `decideAgentRead`, `assertCanApplyProtectedAgentChange`, `org-chart-svg.ts`, `asNonEmptyString`, `validateManagedAgentBinding`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Why does `agentInstructionsService()` connect `agent-instructions.ts` to `builtInAgentService`, `services/built-in-agents.ts`, `pluginManagedAgentService`, `agentRoutes`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Why does `agentsApi` connect `api/agents.ts` to `AgentSkillsTab.tsx`, `recent-agent-chats.ts`, `InboxAgentPolicyControl.tsx`, `SidebarAgents.tsx`, `OrgChart.tsx`, `AgentConfigForm.tsx`, `AgentDetail.tsx`, `AgentDetail.production.tsx`, `Agents.tsx`, `Agents.production.tsx`, `NewAgentSetup.tsx`, `AgentIconPicker.tsx`, `AgentsUsingSkillDialog.tsx`, `AgentContextualSidebar.tsx`, `AgentActionButtons.tsx`, `ConfigureBuiltInAgentModal.tsx`, `AgentChat.tsx`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `builtInAgentService()` (e.g. with `autoProvisionBundledAgents()` and `ensure()`) actually correct?**
  _`builtInAgentService()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `agentApiKeys`, `agentConfigRevisions`, `agentMemberships` to the rest of the system?**
  _315 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `services/agents.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.07337662337662337 - nodes in this community are weakly interconnected._
- **Should `services/built-in-agents.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.046464646464646465 - nodes in this community are weakly interconnected._