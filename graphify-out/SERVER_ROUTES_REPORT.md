# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 97 files · ~258,786 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1624 nodes · 4195 edges · 76 communities (68 shown, 8 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 17 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- issues.ts
- issueRoutes
- pipelines.ts
- openapi.ts
- badRequest
- cases.ts
- plugins.ts
- logger.ts
- projectRoutes
- agentRoutes
- getActorInfo
- org-chart-svg.ts
- middleware/auth.ts
- access.ts
- environmentRoutes
- toolAccessRoutes
- validate
- accessRoutes
- app.ts
- forbidden
- better-auth.ts
- assertCompanyAccess
- activity.ts
- unprocessable
- hasCompanyAccess
- file-resources.ts
- workspace-login-handoff.ts
- decisions.ts
- assertAgentIssueMutationAllowed
- buildIssueSubtreeDiagnosticsResponse
- workspace-login-handoff-plugin.ts
- agents.ts
- readNonEmptyString
- api-compression.ts
- adapters.ts
- chat-webhook-body.ts
- normalizeAgentDefaultsForJoin
- secretRoutes
- tool-gateway.ts
- conflict
- user-profiles.ts
- authz.ts
- health.ts
- chat-channels.ts
- asNonEmptyString
- companySkillRoutes
- routes/index.ts
- logger
- buildOpenApiDocument
- asRecord
- isLocalImplicit
- connection-intents.ts
- runtime-api.ts
- zodToOpenApiSchema
- board-mutation-guard.ts
- built-in-agents.ts
- trust-proxy.ts
- createCompanyInviteForCompany
- summary-slots.ts
- Runner API escape hatch
- private-hostname-guard.ts
- boardChatRoutes
- issueListRequestKey
- applyDocumentFixups
- isClosedIssueStatus
- llms.ts
- buildOnboardingConnectionCandidates
- api.ts
- privateJsonEtag
- dashboard.ts
- experimental-api-paths.ts
- issues-checkout-wakeup.ts
- assertInReviewReviewPath
- sidebar-badges.ts
- experimental-api-metadata.ts
- canonicalizePaperclipArtifactMetadata

## God Nodes (most connected - your core abstractions)
1. `issueRoutes()` - 186 edges
2. `forbidden()` - 148 edges
3. `assertCompanyAccess()` - 147 edges
4. `agentRoutes()` - 122 edges
5. `getActorInfo()` - 105 edges
6. `createApp()` - 83 edges
7. `unprocessable()` - 80 edges
8. `validate()` - 76 edges
9. `assertBoard()` - 76 edges
10. `accessRoutes()` - 61 edges
11. `notFound()` - 59 edges
12. `badRequest()` - 56 edges
13. `toolAccessRoutes()` - 50 edges
14. `caseRoutes()` - 41 edges
15. `getAccessibleResource()` - 39 edges

## Surprising Connections (you probably didn't know these)
- `createApp()` --indirect_call--> `chatWebhookBodyParser()`  [INFERRED]
  server/src/app.ts → server/src/middleware/chat-webhook-body.ts
- `createApp()` --indirect_call--> `errorHandler()`  [INFERRED]
  server/src/app.ts → server/src/middleware/error-handler.ts
- `assertCanResumeAgent()` --calls--> `forbidden()`  [EXTRACTED]
  server/src/routes/agents.ts → server/src/errors.ts
- `assertSecretCatalogReadAllowed()` --calls--> `forbidden()`  [EXTRACTED]
  server/src/routes/secrets.ts → server/src/errors.ts
- `assertCanTestAsAgent()` --calls--> `forbidden()`  [EXTRACTED]
  server/src/routes/tool-access.ts → server/src/errors.ts

## Import Cycles
- None detected.

## Communities (76 total, 8 thin omitted)

### Community 0 - "issues.ts"
Cohesion: 0.03
Nodes (85): ACTIVE_REVIEW_APPROVAL_STATUSES, ActivityExecutionParticipant, activityExecutionParticipantKey(), ActivityIssueRelationSummary, actorMatchesExecutionParticipant(), applyActorMonitorScheduledBy(), attachmentArtifactMetadataInputSchema, auditAgentIssueCommentAttributionSpoof() (+77 more)

### Community 1 - "issueRoutes"
Cohesion: 0.03
Nodes (55): applyCreateIssueStatusDefault(), assertCanManageIssueMonitor(), buildCreateIssueActivityStatusDetails(), buildRequestItemVerdictsWakeIdempotencyKey(), compactIssueListEtag(), companySearchRateLimitActor(), emptyWorkspaceNameMaps(), isApprovalReviewComment() (+47 more)

### Community 2 - "pipelines.ts"
Cohesion: 0.05
Nodes (79): notFound(), assertBuiltInAgentsEnabled(), activityActorForPipelineRoute(), assertCaseAccess(), assertCurrentStageAutomationTargetWriteAccess(), assertPipelineAccess(), assertPipelineCompanyAccess(), assertPipelineWriteAccess() (+71 more)

### Community 3 - "openapi.ts"
Cohesion: 0.03
Nodes (68): ACCEPTED_OPERATIONS, AgentSecretListResponseSchema, approveSecretProposalSchema, AUTHENTICATED_SECURITY, BOARD_ONLY_OPERATIONS, BOARD_ONLY_PREFIXES, BOARD_SECURITY, buildOpenApiSpec (+60 more)

### Community 4 - "badRequest"
Cohesion: 0.07
Nodes (52): badRequest(), assertExternalInstructionsAdmin(), attentionRoutes(), optionalQueryString(), assertInstanceAdmin(), cleanupTerminalImportJobs(), cloudTenantRequestKey(), CompanyImportResult (+44 more)

### Community 5 - "cases.ts"
Cohesion: 0.07
Nodes (52): annotationActorInput(), assertCaseAccess(), assertCasesEnabled(), assertLabelsBelongToCompany(), assertParentCaseBelongsToCompany(), assertProjectBelongsToCompany(), autoLinkRunIssue(), buildCasePatchUpdateValues() (+44 more)

### Community 6 - "plugins.ts"
Cohesion: 0.05
Nodes (37): assertPluginManagementVisible(), AvailableBundledPlugin, bundledPluginMetadata(), __dirname, discoverBundledPlugins(), DiscoveredBundledPlugin, EXPERIMENTAL_BUNDLED_PLUGIN_PACKAGE_NAMES, fileExists() (+29 more)

### Community 7 - "logger.ts"
Cohesion: 0.08
Nodes (39): attachErrorContext(), ErrorContext, errorHandler(), getPaperclipDb(), isRedactedSkillPolicyDenial(), readZodIssues(), recordResponsibleUserDenialFromHttpError(), reportCrash() (+31 more)

### Community 8 - "projectRoutes"
Cohesion: 0.09
Nodes (37): assertNoAgentAdapterConfigMutation(), assertNoAgentInstructionsConfigMutation(), executionWorkspaceRoutes(), assertRuntimeManageAllowed(), handleExecutionWorkspaceRuntimeCommand(), isReadableFile(), resolveFallbackSeedSourceConfigPath(), projectRoutes() (+29 more)

### Community 9 - "agentRoutes"
Cohesion: 0.06
Nodes (26): agentRoutes(), actorCanReadConfigurationsForCompany(), assertAdapterTestEnvironmentForCompany(), assertAgentReadAllowed(), assertCanApplyAgentProfileChange(), assertCanApplyProtectedAgentChange(), assertCanManageInstructionsPath(), assertCanResumeAgent() (+18 more)

### Community 10 - "getActorInfo"
Cohesion: 0.10
Nodes (25): ALLOWED_COMPANY_LOGO_CONTENT_TYPES, assetRoutes(), sanitizeSvgBuffer(), getAccessibleResource(), getActorInfo(), costRoutes(), parseCostDateRange(), parseCostLimit() (+17 more)

### Community 11 - "org-chart-svg.ts"
Cohesion: 0.10
Nodes (34): avatarGridHeight(), avatarGridRows(), avatarGridWidth(), cardHeight(), cardWidth(), collapseToAvatars(), countNodes(), defaultRenderCard() (+26 more)

### Community 12 - "middleware/auth.ts"
Cohesion: 0.11
Nodes (31): BetterAuthSessionResult, actorMiddleware(), ActorMiddlewareOptions, auditAgentJwtRunHeaderMismatch(), auditAgentKeyMissingResponsibleUser(), CloudActorHeaderSource, cloudTenantCompanyId(), cloudTenantWriteDebounceFor() (+23 more)

### Community 13 - "access.ts"
Cohesion: 0.08
Nodes (31): agentJoinGrantsFromDefaults(), AvailableSkill, buildCliAuthApprovalPath(), CompanyMemberRecord, defaultInviteResolutionNetwork, grantsFromDefaults(), HERMES_DASHBOARD_API_PATHS, hostnameForResolution() (+23 more)

### Community 14 - "environmentRoutes"
Cohesion: 0.11
Nodes (25): applyPlatformProvisionedEnvironmentFloor(), assertNoClientPlatformProvisionedMarkers(), assertPlatformProvisionedEnvironmentWritable(), environmentRoutes(), assertCanAccessInstanceEnvironments(), assertCanReadSecretsForDraftProbe(), assertCustomImageCompanyAccess(), canReadFullInstanceEnvironment() (+17 more)

### Community 15 - "toolAccessRoutes"
Cohesion: 0.09
Nodes (28): agentOrgDepths(), allowlistIds(), classifyConnectionUpdate(), cloudConnectorEnrollmentOutcomeHtml(), cloudConnectorEnrollmentReturnPath(), connectionIntentOAuthOutcomeHtml(), filterVisibleToolConnections(), normalizeCloudConnectorEnrollmentReturnTo() (+20 more)

### Community 16 - "validate"
Cohesion: 0.11
Nodes (24): unauthorized(), EXISTING_BRANCH_SETTINGS_PATH, isExistingBranchSemanticsZodIssue(), validate(), validateIssueMutationBody(), assertCanGenerateOpenClawInvitePrompt(), assertCompanyPermission(), authRoutes() (+16 more)

### Community 17 - "accessRoutes"
Cohesion: 0.11
Nodes (30): accessRoutes(), getInviteCompanyBranding(), getInviteLogoAsset(), actorHasActiveUserMembership(), assertAccessAdminVisible(), assertLegacyAgentInviteAdapterType(), buildInviteOnboardingManifest(), buildInviteOnboardingTextDocument() (+22 more)

### Community 18 - "app.ts"
Cohesion: 0.12
Nodes (23): ChatReconciliationLane, createApp(), createChatReconciliationCoordinator(), createManagedBundledPluginWorkerRecovery(), isDatabaseConnectionUnavailableError(), listenViteHmrServer(), resolveViteHmrHost(), resolveViteHmrPort() (+15 more)

### Community 19 - "forbidden"
Cohesion: 0.12
Nodes (26): forbidden(), assertCanCreateAgentsForCompany(), assertCanReadAgent(), assertCanReadConfigurations(), assertSameCompanyCeoAgentOrBoard(), companySkillPolicyRoutes(), assertCanAdministerPolicy(), assertSkillPolicyCompanyAccess() (+18 more)

### Community 20 - "better-auth.ts"
Cohesion: 0.13
Nodes (23): BetterAuthGetSessionApi, BetterAuthHandlerTarget, BetterAuthInstance, BetterAuthSessionResolver, BetterAuthSessionUser, buildBetterAuthAdvancedOptions(), buildBetterAuthRateLimitOptions(), createBetterAuthInstance() (+15 more)

### Community 21 - "assertCompanyAccess"
Cohesion: 0.17
Nodes (21): assertBoardCanManageAgentsForCompany(), assertBoardCanWakeAgent(), assertCanManageAdapterLogin(), aiConnectionRoutes(), assertLocalOperator(), assertAiConnectionCreateAccess(), canInstallSharedAiConnectionForNewAgent(), validateAiApiKey() (+13 more)

### Community 22 - "activity.ts"
Cohesion: 0.11
Nodes (16): activityRoutes(), assertAgentAuditPermission(), hasAgentAuditPermission(), agentActionAuditActorScopeSchema, agentActionAuditQuerySchema, AUDIT_CSV_COLUMNS, AuditCsvRow, auditRowsToCsv() (+8 more)

### Community 23 - "unprocessable"
Cohesion: 0.11
Nodes (22): unprocessable(), allowedEnvironmentDriversForAgent(), assertAdapterConfigConstraints(), assertAgentDefaultEnvironmentSelection(), assertAgentEnvironmentSelection(), assertCodexLoginProviderCapability(), assertFreshPaperclipRunnerProvider(), assertKnownAdapterType() (+14 more)

### Community 24 - "hasCompanyAccess"
Cohesion: 0.12
Nodes (19): assertCanUpdateAgent(), approvalRoutes(), approvalReviewPathContext(), assertApprovalMutationAllowedByRunContext(), queueAdditionalApprovalReviewPathWakes(), requireApprovalAccess(), isStatusOnlyRecoveryContext(), redactApprovalPayload() (+11 more)

### Community 25 - "file-resources.ts"
Cohesion: 0.17
Nodes (22): activityDetails(), availabilityActivityDetails(), createFileResourceAvailabilityLimiter(), createFileResourceLimiter(), createFileResourceListLimiter(), denialReasonFromError(), FileResourceLimiter, fileResourceRoutes() (+14 more)

### Community 26 - "workspace-login-handoff.ts"
Cohesion: 0.13
Nodes (17): base64UrlDecode(), base64UrlEncode(), buildWorkspaceHandoffExchangeUrl(), constantTimeMatches(), isPayloadShape(), issueWorkspaceHandoffTicket(), normalizeWorkspaceHandoffOrigin(), sign() (+9 more)

### Community 27 - "decisions.ts"
Cohesion: 0.15
Nodes (18): assertBoardOrAgent(), assertDecisionAccess(), decisionQueueRoutes(), mutationActor(), sourceParams(), agentContext(), boardUserId(), bundleSchema (+10 more)

### Community 28 - "assertAgentIssueMutationAllowed"
Cohesion: 0.13
Nodes (22): assertAgentInteractionRunAttribution(), assertAgentIssueCommentAllowed(), assertAgentIssueMutationAllowed(), assertCrossIssueInfluenceWithinRunCap(), assertFreshTaskWatchdogSourceMutation(), assertIssueReadAllowed(), assertIssueThreadInteractionContainmentAllowed(), assertIssueThreadInteractionResolutionAllowed() (+14 more)

### Community 29 - "buildIssueSubtreeDiagnosticsResponse"
Cohesion: 0.13
Nodes (21): blockerDiagnosticLabel(), buildIssueBlockerDiagnosis(), buildIssueBlockerDiagnosticsResponse(), buildIssueSubtreeDiagnosis(), buildIssueSubtreeDiagnosticsResponse(), buildIssueWakeDiagnosis(), buildIssueWakeDiagnosticsResponse(), dateToIso() (+13 more)

### Community 30 - "workspace-login-handoff-plugin.ts"
Cohesion: 0.15
Nodes (16): exchangeWorkspaceHandoffTicket(), isWorkspaceHandoffRepairReason(), WorkspaceHandoffClonedIdentity, WorkspaceHandoffExchangeDeps, WorkspaceHandoffExchangeFailureReason, WorkspaceHandoffExchangeResult, buildFallbackRedirect(), WorkspaceHandoffEndpointContext (+8 more)

### Community 31 - "agents.ts"
Cohesion: 0.11
Nodes (15): AdapterLoginStartResolution, AdapterLoginStartSpineInput, runAdapterLoginStartSpine(), AGENT_SKILL_ASSIGNMENT_MODES, buildRuntimeSkillConfig(), resolveAgentSelfTrustPreset(), resolveDesiredSkillAssignment(), shouldMaterializeRuntimeSkillsForAdapter() (+7 more)

### Community 32 - "readNonEmptyString"
Cohesion: 0.20
Nodes (19): buildQueuedCommentQueue(), cancelScheduledRetrySupersededByComment(), findQueuedCommentWake(), lockQueuedCommentState(), queueCommentsForWake(), readObject(), resolveRunIssueWorkspaceInheritanceSource(), listSuccessfulRunHandoffStates() (+11 more)

### Community 33 - "api-compression.ts"
Cohesion: 0.22
Nodes (17): API_COMPRESSION_THRESHOLD_BYTES, apiCompression(), ApiCompressionOptions, deflateAsync, EncodingPreference, gzipAsync, isJsonContentType(), normalizeEndArgs() (+9 more)

### Community 34 - "adapters.ts"
Cohesion: 0.22
Nodes (14): AdapterCapabilities, AdapterInfo, AdapterInstallRequest, AdapterLoginProjection, adapterRoutes(), assertAdapterCodeInstallAllowed(), assertAdapterManagementVisible(), buildAdapterCapabilities() (+6 more)

### Community 35 - "chat-webhook-body.ts"
Cohesion: 0.18
Nodes (14): payloadTooLarge(), unsupportedMediaType(), CHAT_WEBHOOK_BODY_LIMIT, CHAT_WEBHOOK_BODY_LIMIT_BYTES, DEFAULT_JSON_BODY_LIMIT, PORTABLE_JSON_BODY_LIMIT, PORTABLE_JSON_BODY_LIMIT_BYTES, PORTABLE_ZIP_UPLOAD_LIMIT_BYTES (+6 more)

### Community 36 - "normalizeAgentDefaultsForJoin"
Cohesion: 0.26
Nodes (16): buildJoinDefaultsPayloadForAccept(), extractHeaderEntries(), generateEd25519PrivateKeyPem(), headerMapGetIgnoreCase(), headerMapHasKeyIgnoreCase(), isDefaultHermesDashboardRoot(), isPlainObject(), mergeJoinDefaultsPayloadForReplay() (+8 more)

### Community 37 - "secretRoutes"
Cohesion: 0.22
Nodes (14): assertCompanySecretWrite(), assertSecretDefinitionAdmin(), boardActorUser(), currentUserId(), hasSecretDefinitionAdminAccess(), isCompanyScopedSecret(), proposalListPage(), secretRoutes() (+6 more)

### Community 38 - "tool-gateway.ts"
Cohesion: 0.23
Nodes (14): bearerToken(), callerHeaders(), decodeAuditCursor(), encodeAuditCursor(), gatewayToken(), handleMcpGatewayProtocol(), mcpGatewayProtocolRoutes(), normalizedAuditOutcome() (+6 more)

### Community 39 - "conflict"
Cohesion: 0.13
Nodes (15): conflict(), isExplicitResumeCapableStatus(), activeExecutionParticipantAgentId(), assertExplicitResumeIntentAllowed(), assertNoAgentDelegationCycle(), assertQueueMutationTarget(), assertSafeRecoveryHandBackGates(), hasActiveCheckoutManagementOverride() (+7 more)

### Community 40 - "user-profiles.ts"
Cohesion: 0.30
Nodes (14): CompanyUserRow, dayKeyExpr(), isoDay(), loadDailyStats(), loadWindowStats(), PROFILE_WINDOWS, resolveCompanyUser(), slugifyUserPart() (+6 more)

### Community 41 - "authz.ts"
Cohesion: 0.23
Nodes (7): HttpError, ActorSecretContext, assertBoardOrgAccess(), hasBoardOrgAccess(), throwOrShadowResponsibleUserCompanyAccessDeny(), assertCanReadInstanceEnvironments(), Heartbeat

### Community 42 - "health.ts"
Cohesion: 0.27
Nodes (12): resolveWorkspaceReadinessLocalToken(), WORKSPACE_READINESS_TOKEN_HEADER, WORKSPACE_READINESS_USER_EMAIL_HEADER, WORKSPACE_READINESS_USER_ID_HEADER, getCloudHealthStatus(), hasDevServerStatusToken(), hasWorkspaceReadinessToken(), healthRoutes() (+4 more)

### Community 43 - "chat-channels.ts"
Cohesion: 0.28
Nodes (12): tooManyRequests(), actorUserId(), assertEndpointAccess(), ChatChannelRouteOptions, chatChannelRoutes(), assertConnectionManager(), assertEndpointManagementAccess(), ChatWebhookRouteOptions (+4 more)

### Community 44 - "asNonEmptyString"
Cohesion: 0.18
Nodes (13): adapterSupportsInstructionsBundle(), applyCreateDefaultsByAdapterType(), asNonEmptyString(), assertNoNewAgentLegacyPromptTemplate(), codexLocalAgentHome(), ensureGatewayDeviceKey(), evaluateClaudeAuthSignal(), evaluateCodexAuthSignal() (+5 more)

### Community 45 - "companySkillRoutes"
Cohesion: 0.22
Nodes (9): companySkillRoutes(), assertCanMutateCompanySkills(), asString(), deriveTrackedSkillRef(), firstQueryString(), optionalQueryBoolean(), skillPolicyPrincipal(), skillPolicyResource() (+1 more)

### Community 46 - "routes/index.ts"
Cohesion: 0.26
Nodes (8): folderRoutes(), inboxDismissalRoutes(), inboxDismissalSchema, requireBoardUser(), onboardingSeedRoutes(), profileInput(), remoteAgentProfileRoutes(), remoteAgentService()

### Community 47 - "logger"
Cohesion: 0.20
Nodes (9): ACTION_BY_METHOD, cloudControlMiddleware(), cloudRuntimeIdentityMiddleware(), logger, computeETag(), MIME_TYPES, PluginUiStaticRouteOptions, pluginUiStaticRoutes() (+1 more)

### Community 48 - "buildOpenApiDocument"
Cohesion: 0.20
Nodes (8): buildOpenApiDocument(), isZodSchema(), jsonBody(), normalizeContent(), normalizeResponses(), OpenAPIRegistry, paramsSchemaFromPath(), registerCurrentRoute()

### Community 49 - "asRecord"
Cohesion: 0.25
Nodes (11): applyCodexLocalKeyIsolation(), asEnvBindingString(), asRecord(), assertProviderTraceSettingTransition(), codexLocalEnvKeyConfigured(), normalizeNewAgentRuntimeConfig(), parseBooleanLike(), parseNumberLike() (+3 more)

### Community 50 - "isLocalImplicit"
Cohesion: 0.24
Nodes (10): approveHumanJoinRequestFromInvite(), assertInstanceAdmin(), addCompanyMemberRemovalAccess(), assertCanManageCompanyMember(), getProtectedMemberReason(), isLocalImplicit(), loadCompanyAccessSummary(), resolveAcceptedInviteJoinRequest() (+2 more)

### Community 51 - "connection-intents.ts"
Cohesion: 0.31
Nodes (8): bearer(), connectionIntentBoardRoutes(), bypassCurrentMembershipCheck(), canManageCompanyConnections(), Heartbeat, resultContent(), runtimeClaims(), runtimeConnectionIntentRoutes()

### Community 52 - "runtime-api.ts"
Cohesion: 0.60
Nodes (9): buildRuntimeApiCandidateUrls(), choosePrimaryRuntimeApiUrl(), collectReachableInterfaceHosts(), formatOrigin(), isLinkLocalHost(), isLoopbackHost(), isWildcardHost(), normalizeHost() (+1 more)

### Community 53 - "zodToOpenApiSchema"
Cohesion: 0.42
Nodes (9): applyNumberChecks(), applyStringChecks(), checkDef(), isOptionalSchema(), parametersFromSchema(), unwrapSchema(), zodDef(), zodToOpenApiSchema() (+1 more)

### Community 54 - "board-mutation-guard.ts"
Cohesion: 0.43
Nodes (7): boardMutationGuard(), DEFAULT_DEV_ORIGINS, parseOrigin(), requestHost(), SAFE_METHODS, trustedBoardMutationOrigin(), trustedOriginsForRequest()

### Community 55 - "built-in-agents.ts"
Cohesion: 0.32
Nodes (7): builtInAgentRoutes(), assertCanControlBuiltInRoutine(), assertCanProvisionBuiltInAgents(), logBuiltInAgentMutation(), formatScheduleLabel(), redactBuiltInAgentListState(), WEEKDAY_LABELS

### Community 56 - "trust-proxy.ts"
Cohesion: 0.33
Nodes (6): RFC-4291, applyTrustProxy(), isValidSubnetToken(), NAMED_SUBNETS, parseTrustProxyEnv(), TrustProxyValue

### Community 57 - "createCompanyInviteForCompany"
Cohesion: 0.29
Nodes (7): createCompanyInviteForCompany(), companyInviteExpiresAt(), createInviteToken(), hashToken(), isInviteTokenHashCollisionError(), mergeInviteDefaults(), summarizeSecretForLog()

### Community 58 - "summary-slots.ts"
Cohesion: 0.38
Nodes (6): readScopeId(), summarySlotRoutes(), assertCanGenerateSummary(), assertSummariesEnabled(), logSummaryMutation(), summarySlotSessionTaskKey()

### Community 59 - "Runner API escape hatch"
Cohesion: 0.29
Nodes (6): Authority and replay, Catalog maintenance, Controlled rollout, Discovery and requests, Runner API escape hatch, Verification and paid evals

### Community 60 - "private-hostname-guard.ts"
Cohesion: 0.60
Nodes (5): extractHostname(), isLoopbackHostname(), normalizeAllowedHostnames(), privateHostnameGuard(), resolvePrivateHostnameAllowSet()

### Community 61 - "boardChatRoutes"
Cohesion: 0.53
Nodes (4): boardChatRoutes(), isConciergeReply(), serializeTurn(), stripActionSignals()

### Community 62 - "issueListRequestKey"
Cohesion: 0.53
Nodes (6): issueListActorIdentity(), issueListClientIdentity(), issueListRequestKey(), normalizeIssueListCacheValue(), shortHash(), stableJson()

### Community 63 - "applyDocumentFixups"
Cohesion: 0.47
Nodes (6): applyDocumentFixups(), applyOperationStatusOverride(), isBoardOnlyOperation(), operationKey(), resolveOperationAuthLevel(), securityRequirement()

### Community 64 - "isClosedIssueStatus"
Cohesion: 0.40
Nodes (5): isAssigneeSelfCommentOnTerminalIssue(), isClosedIssueStatus(), clearReopenPendingConsumptionWithRetry(), guardReopenedWorkspaceConsumption(), shouldImplicitlyMoveCommentedIssueToTodo()

### Community 65 - "llms.ts"
Cohesion: 0.50
Nodes (4): hasCreatePermission(), llmRoutes(), assertCanRead(), pluginOnlyAdapterDocs

### Community 66 - "buildOnboardingConnectionCandidates"
Cohesion: 0.67
Nodes (4): buildOnboardingConnectionCandidates(), buildOnboardingDiscoveryDiagnostics(), isLoopbackHost(), normalizeHostname()

### Community 72 - "assertInReviewReviewPath"
Cohesion: 0.67
Nodes (3): hasExecutionParticipant(), hasScheduledMonitor(), assertInReviewReviewPath()

## Knowledge Gaps
- **276 isolated node(s):** `API_PREFIX`, `API`, `UiMode`, `VITE_DEV_ASSET_PREFIXES`, `VITE_DEV_STATIC_PATHS` (+271 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `agentRoutes()` connect `agentRoutes` to `pipelines.ts`, `badRequest`, `conflict`, `projectRoutes`, `getActorInfo`, `org-chart-svg.ts`, `asNonEmptyString`, `routes/index.ts`, `validate`, `asRecord`, `app.ts`, `forbidden`, `assertCompanyAccess`, `activity.ts`, `unprocessable`, `hasCompanyAccess`, `agents.ts`?**
  _High betweenness centrality (0.133) - this node is a cross-community bridge._
- **Why does `issueRoutes()` connect `issueRoutes` to `issues.ts`, `pipelines.ts`, `badRequest`, `projectRoutes`, `getActorInfo`, `validate`, `app.ts`, `forbidden`, `assertCompanyAccess`, `unprocessable`, `assertAgentIssueMutationAllowed`, `buildIssueSubtreeDiagnosticsResponse`, `readNonEmptyString`, `conflict`, `routes/index.ts`, `issueListRequestKey`, `isClosedIssueStatus`, `privateJsonEtag`, `issues-checkout-wakeup.ts`, `assertInReviewReviewPath`, `canonicalizePaperclipArtifactMetadata`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Why does `forbidden()` connect `forbidden` to `issues.ts`, `issueRoutes`, `pipelines.ts`, `badRequest`, `cases.ts`, `plugins.ts`, `projectRoutes`, `agentRoutes`, `getActorInfo`, `middleware/auth.ts`, `access.ts`, `environmentRoutes`, `toolAccessRoutes`, `validate`, `accessRoutes`, `app.ts`, `assertCompanyAccess`, `activity.ts`, `unprocessable`, `hasCompanyAccess`, `decisions.ts`, `assertAgentIssueMutationAllowed`, `agents.ts`, `adapters.ts`, `secretRoutes`, `tool-gateway.ts`, `conflict`, `authz.ts`, `chat-channels.ts`, `companySkillRoutes`, `routes/index.ts`, `isLocalImplicit`, `connection-intents.ts`, `built-in-agents.ts`, `summary-slots.ts`, `llms.ts`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `issueRoutes()` (e.g. with `applyCreateIssueStatusDefault()` and `summarizeIssueRelationForActivity()`) actually correct?**
  _`issueRoutes()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `API_PREFIX`, `API`, `UiMode` to the rest of the system?**
  _276 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `issues.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.026373626373626374 - nodes in this community are weakly interconnected._
- **Should `issueRoutes` be split into smaller, more focused modules?**
  _Cohesion score 0.030473135525260625 - nodes in this community are weakly interconnected._