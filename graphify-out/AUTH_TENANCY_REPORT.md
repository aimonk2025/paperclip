# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 58 files · ~153,133 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1591 nodes · 3042 edges · 78 communities (61 shown, 17 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 103 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- validators/tool-access.ts
- types/tool-access.ts
- authorization.ts
- toolAccessRoutes
- middleware/auth.ts
- toolAccessService
- tool-access-policy.ts
- services/tool-access.ts
- validators/access.ts
- device-login-service.ts
- routes/access.ts
- completeOAuthCallback
- PaperclipRunnerToolAuthority
- refreshCatalog
- asRecord
- accessRoutes
- tool_access.ts
- better-auth.ts
- discoverOAuthEndpoints
- accessService
- oauthConfig
- login-command.ts
- createDeviceLoginService
- tool-oauth-legacy-backfill.ts
- types/access.ts
- workspace-login-handoff.ts
- normalizeAgentDefaultsForJoin
- device-login-reaper.ts
- refreshOAuthGrantCredentials
- buildInviteOnboardingManifest
- PaperclipRunnerSemanticAuthority
- services/resource-memberships.ts
- oauth-endpoint-url.ts
- validators/adapter-auth-session.ts
- workspace-login-handoff-issuer.ts
- normalizeHumanRole
- connectGalleryApp
- types/resource-memberships.ts
- workspace-command-authz.ts
- runLogin
- runtime-request-resolution-authority.ts
- workspace-login-handoff-exchange.ts
- loginHome
- buildProfileDetails
- workspace-login-handoff-plugin.ts
- observeSandboxDelete
- registerOAuthClient
- schema/auth.ts
- codex-auth-reconciliation.ts
- invite-rate-limit.ts
- src/adapter-auth-session.ts
- runtimeHealth
- toCatalogEntryForConnection
- adapter_auth_sessions.ts
- createCompanyInviteForCompany
- adapter-login-lease.ts
- loadGitHubGrantMetadata
- adapter-login-route-spine.ts
- classifyRisk
- stableHash
- connectToolAppSchema
- routes/auth.ts
- agent_memberships.ts
- company_memberships.ts
- document_memberships.ts
- instance_user_roles.ts
- invites.ts
- project_memberships.ts
- secret_access_events.ts
- adapter-auth-check-code.ts
- ToolMcpGateway
- ToolMcpGatewayToken
- ToolProfile
- VercelConnectGrantReference
- assertSameOAuthActor
- isGoogleWorkspaceToolAllowed
- toConnectionGrant

## God Nodes (most connected - your core abstractions)
1. `toolAccessService()` - 250 edges
2. `asRecord()` - 55 edges
3. `accessRoutes()` - 54 edges
4. `toolAccessRoutes()` - 44 edges
5. `authorizationService()` - 39 edges
6. `decideBase()` - 33 edges
7. `connectGalleryApp()` - 33 edges
8. `accessService()` - 29 edges
9. `oauthConfig()` - 29 edges
10. `refreshCatalog()` - 28 edges
11. `toolAccessPolicyService()` - 27 edges
12. `completeOAuthCallback()` - 26 edges
13. `checkConnectionHealth()` - 25 edges
14. `refreshOAuthGrantCredentials()` - 25 edges
15. `getConnectionRow()` - 23 edges

## Surprising Connections (you probably didn't know these)
- `resolveWorkspaceHandoffIdentity()` --calls--> `normalizeWorkspaceHandoffOrigin()`  [EXTRACTED]
  server/src/auth/better-auth.ts → server/src/auth/workspace-login-handoff.ts
- `createBetterAuthInstance()` --calls--> `workspaceLoginHandoffPlugin()`  [EXTRACTED]
  server/src/auth/better-auth.ts → server/src/auth/workspace-login-handoff-plugin.ts
- `workspaceLoginHandoffPlugin()` --calls--> `exchangeWorkspaceHandoffTicket()`  [EXTRACTED]
  server/src/auth/workspace-login-handoff-plugin.ts → server/src/auth/workspace-login-handoff-exchange.ts
- `issueWorkspaceLoginHandoff()` --calls--> `sanitizeWorkspaceHandoffRedirectPath()`  [EXTRACTED]
  server/src/services/workspace-login-handoff-issuer.ts → server/src/auth/workspace-login-handoff.ts
- `loadCompanyAccessSummary()` --calls--> `normalizeHumanRole()`  [EXTRACTED]
  server/src/routes/access.ts → server/src/services/company-member-roles.ts

## Import Cycles
- None detected.

## Communities (78 total, 17 thin omitted)

### Community 0 - "validators/tool-access.ts"
Cohesion: 0.01
Nodes (156): actorConditionSchema, argumentConditionSchema, connectionGrantKindSchema, connectionGrantSchema, connectionGrantStatusSchema, connectionTokenIssuancePathSchema, ConnectionTokenRequestInput, connectionTokenRequestSchema (+148 more)

### Community 1 - "types/tool-access.ts"
Cohesion: 0.02
Nodes (130): CONNECTION_RECOVERABLE_ERROR_CODES, ConnectionAudienceMember, ConnectionGrant, ConnectionGrantCapabilities, ConnectionGrantDelegation, ConnectionGrantKind, ConnectionGrantMember, ConnectionGrantMemberSubjectType (+122 more)

### Community 2 - "authorization.ts"
Cohesion: 0.05
Nodes (87): GrantInput, MemberArchiveInput, MembershipRow, activeActorMembership(), activeResponsibleUserCanAuthorizeAgentGrantedSkillChange(), activeResponsibleUserCanAuthorizeIssueAction(), AgentAuthorizationRow, AgentHierarchyRow (+79 more)

### Community 3 - "toolAccessRoutes"
Cohesion: 0.05
Nodes (58): ActorSecretContext, assertBoard(), assertBoardOrAgent(), assertBoardOrgAccess(), assertInstanceAdmin(), buildActorSecretContext(), getAccessibleResource(), getActorInfo() (+50 more)

### Community 4 - "middleware/auth.ts"
Cohesion: 0.05
Nodes (60): BetterAuthSessionResult, actorMiddleware(), ActorMiddlewareOptions, auditAgentJwtRunHeaderMismatch(), auditAgentKeyMissingResponsibleUser(), CloudActorHeaderSource, cloudTenantCompanyId(), cloudTenantWriteDebounceFor() (+52 more)

### Community 5 - "toolAccessService"
Cohesion: 0.05
Nodes (53): builtInStdioTemplate(), normalizeToolDescriptor(), readStdioTemplateId(), toConnectionInstall(), toolAccessService(), assertAgentsInCompany(), assertApplication(), assertCatalogEntriesForConnection() (+45 more)

### Community 6 - "tool-access-policy.ts"
Cohesion: 0.07
Nodes (64): argumentConditionMatches(), argumentFiltersMatch(), assertGenericPolicyType(), assertSupportedGenericPolicyShape(), assertSupportedPolicyConditions(), asToolRiskLevel(), auditOutcome(), boolCondition() (+56 more)

### Community 7 - "services/tool-access.ts"
Cohesion: 0.05
Nodes (43): RFC-6749, RFC-7591, RFC-8414, RFC-9207, RFC-9728, ACTIVE_BROKER_RUN_STATUSES, ActorInfo, APPROVED_STDIO_TEMPLATES (+35 more)

### Community 8 - "validators/access.ts"
Cohesion: 0.05
Nodes (40): AcceptInvite, acceptInviteSchema, ArchiveCompanyMember, archiveCompanyMemberSchema, AuthSession, authSessionSchema, BoardCliAuthAccessLevel, boardCliAuthAccessLevelSchema (+32 more)

### Community 9 - "device-login-service.ts"
Cohesion: 0.05
Nodes (33): AcquireLoginLeaseInput, ADAPTER_AUTH_PROMOTION_CLAIM_MS, AdapterAuthSessionConflictError, AdapterAuthSessionRow, adapterLoginPromotionLockKey(), CompareAndSetAdapterAuthSessionStatusInput, CredentialPromotionContext, DEVICE_LOGIN_PROVIDER_UNSUPPORTED (+25 more)

### Community 10 - "routes/access.ts"
Cohesion: 0.09
Nodes (30): agentJoinGrantsFromDefaults(), AvailableSkill, CompanyMemberRecord, defaultInviteResolutionNetwork, grantsFromDefaults(), HERMES_DASHBOARD_API_PATHS, hostnameForResolution(), humanRoleRank (+22 more)

### Community 11 - "completeOAuthCallback"
Cohesion: 0.11
Nodes (32): actorBinding(), connectionMethodForConnection(), managedConnectorProfile(), normalizeConnectionMethodConfig(), normalizeOAuthProviderError(), oauthProviderErrorMessage(), originOf(), projectedConnectionHeaders() (+24 more)

### Community 12 - "PaperclipRunnerToolAuthority"
Cohesion: 0.17
Nodes (12): Binding, boundedLimit(), canonicalJson(), IMPLEMENTED_OPERATIONS, nullableProviderId(), PaperclipRunnerToolAuthority, record(), redactedActor() (+4 more)

### Community 13 - "refreshCatalog"
Cohesion: 0.14
Nodes (31): healthFailureHttpStatus(), toConnection(), assertComposioConnectedAccountActive(), audit(), auditConnectionTokenIssuance(), checkConnectionHealth(), classifyConnectionSecrets(), composioClientForParent() (+23 more)

### Community 14 - "asRecord"
Cohesion: 0.13
Nodes (28): asRecord(), isOAuthEndpointRejection(), mergeManagedToolArguments(), projectConnectionMethodToolArguments(), projectedConnectionToolArguments(), sanitizeHttpFailure(), accessContextForBroker(), annotateGitHubAuthorization() (+20 more)

### Community 15 - "accessRoutes"
Cohesion: 0.12
Nodes (27): accessRoutes(), assertCanGenerateOpenClawInvitePrompt(), assertCompanyPermission(), assertInstanceAdmin(), getInviteCompanyBranding(), getInviteLogoAsset(), actorHasActiveUserMembership(), assertAccessAdminVisible() (+19 more)

### Community 16 - "tool_access.ts"
Cohesion: 0.08
Nodes (25): connectionGrantDelegations, connectionGrantMembers, connectionGrants, connectionTokenIssuances, toolAccessAuditEvents, toolActionRequests, toolApplications, toolCallEvents (+17 more)

### Community 17 - "better-auth.ts"
Cohesion: 0.13
Nodes (23): BetterAuthGetSessionApi, BetterAuthHandlerTarget, BetterAuthInstance, BetterAuthSessionResolver, BetterAuthSessionUser, buildBetterAuthAdvancedOptions(), buildBetterAuthRateLimitOptions(), createBetterAuthInstance() (+15 more)

### Community 18 - "discoverOAuthEndpoints"
Cohesion: 0.12
Nodes (26): connectionMethodFor(), credentialFieldsFor(), protectedResourceMetadataUrls(), remoteEndpoint(), allowPrivateRemoteEndpoints(), assertConfiguredTokenBrokerEndpointsAllowed(), assertOAuthEndpointUrl(), assertRemoteConnectionEndpointsAllowed() (+18 more)

### Community 19 - "accessService"
Cohesion: 0.13
Nodes (19): accessService(), archiveMember(), assertAssignableArchiveTarget(), assertCanRemoveActiveOwner(), canUser(), copyActiveUserMemberships(), decide(), ensureMembership() (+11 more)

### Community 20 - "oauthConfig"
Cohesion: 0.18
Nodes (23): credentialRefConfigPath(), sameOAuthIssuer(), singleFlight(), acquireOAuthRefreshLease(), adoptClientIdMetadataDocument(), assertOAuthCallbackIssuer(), clearOAuthRefreshLease(), configuredOAuthClientForConnection() (+15 more)

### Community 21 - "login-command.ts"
Cohesion: 0.11
Nodes (17): AUTH_JSON_FILE_NAME, decodeAuthReadOutput(), DescriptorBoundAuthReadDeps, DEVICE_LOGIN_AUTH_READ_ERROR, DEVICE_LOGIN_AUTH_READ_SCRIPT, MAX_AUTH_JSON_BYTES, runDescriptorBoundAuthRead(), createWorkerBoundLoginPtyOpener() (+9 more)

### Community 22 - "createDeviceLoginService"
Cohesion: 0.13
Nodes (12): AdapterAuthSessionStore, buildFailure(), createDeviceLoginService(), buildOwnerResponse(), cancelOwnerSession(), readActiveOwnerSession(), readOwnerSession(), resolveProfile() (+4 more)

### Community 23 - "tool-oauth-legacy-backfill.ts"
Cohesion: 0.17
Nodes (21): asRecord(), backfillLegacyToolOAuthTokens(), configPath(), DbTransaction, hasRawOauthTokenKeys(), LegacyOAuthToken, OAuthTokenKind, RAW_OAUTH_TOKEN_KEYS (+13 more)

### Community 24 - "types/access.ts"
Cohesion: 0.14
Nodes (17): AccessUserProfile, AdminUserDirectoryEntry, ArchiveCompanyMemberResponse, CompanyInviteListResponse, CompanyInviteRecord, CompanyMemberRecord, CompanyMembership, CompanyMembersResponse (+9 more)

### Community 25 - "workspace-login-handoff.ts"
Cohesion: 0.12
Nodes (12): base64UrlDecode(), base64UrlEncode(), WORKSPACE_EXECUTION_WORKSPACE_COMPANY_ID_ENV_KEY, WORKSPACE_EXECUTION_WORKSPACE_ID_ENV_KEY, WORKSPACE_HANDOFF_CLOCK_SKEW_SECONDS, WORKSPACE_HANDOFF_KEY_ENV_KEY, WORKSPACE_HANDOFF_TICKET_VERSION, WORKSPACE_READINESS_TOKEN_ENV_KEY (+4 more)

### Community 26 - "normalizeAgentDefaultsForJoin"
Cohesion: 0.22
Nodes (18): buildJoinDefaultsPayloadForAccept(), extractHeaderEntries(), generateEd25519PrivateKeyPem(), hashToken(), headerMapGetIgnoreCase(), headerMapHasKeyIgnoreCase(), isDefaultHermesDashboardRoot(), isPlainObject() (+10 more)

### Community 27 - "device-login-reaper.ts"
Cohesion: 0.12
Nodes (11): DeviceLoginReaper, DeviceLoginReaperDeps, LoginLeaseRef, ProductionLoginSessionReaperRuntimeDeps, ReaperSweepResult, TaggedLease, ADAPTER_AUTH_ACTIVE_STATUSES, AdapterAuthReaperStore (+3 more)

### Community 28 - "refreshOAuthGrantCredentials"
Cohesion: 0.25
Nodes (18): acquireOAuthGrantRefreshLease(), clearOAuthGrantRefreshLease(), connectionReconnectUrl(), connectionSetupUrl(), getOAuthGrantRow(), oauthGrantConfig(), oauthGrantExpiresAtMs(), refreshManagedGitHubGrantAccessOnce() (+10 more)

### Community 29 - "buildInviteOnboardingManifest"
Cohesion: 0.16
Nodes (17): buildInviteOnboardingManifest(), buildInviteOnboardingTextDocument(), buildOnboardingConnectionCandidates(), buildOnboardingDiscoveryDiagnostics(), extractInviteHumanRole(), extractInviteMessage(), inviteExpired(), inviteState() (+9 more)

### Community 30 - "PaperclipRunnerSemanticAuthority"
Cohesion: 0.20
Nodes (8): activeAgentStatus(), BoundContext, boundedLimit(), jsonValue(), PaperclipRunnerSemanticAuthority, PaperclipRunnerSemanticBinding, READ_OPERATION_IDS, requiredString()

### Community 31 - "services/resource-memberships.ts"
Cohesion: 0.15
Nodes (10): assertBoardSelfMembershipAccess(), BoardActor, evaluatePolicy(), MembershipChangeKind, MembershipUpdateResult, PolicyDecision, ResourceMembershipPolicyHook, resourceMembershipService() (+2 more)

### Community 32 - "oauth-endpoint-url.ts"
Cohesion: 0.20
Nodes (11): checkOAuthEndpointUrl(), insecureTransportAllowed(), isLoopbackHost(), isLoopbackIpv4(), isSafeOAuthEndpointUrl(), KIND_LABELS, normalizedOrigin(), OAuthEndpointKind (+3 more)

### Community 33 - "validators/adapter-auth-session.ts"
Cohesion: 0.14
Nodes (13): AdapterAuthSessionFailure, adapterAuthSessionFailureSchema, AdapterAuthSessionOwnerResponse, adapterAuthSessionOwnerResponseSchema, AdapterAuthSessionPrompt, adapterAuthSessionPromptSchema, AdapterAuthSessionResponse, adapterAuthSessionResponseSchema (+5 more)

### Community 34 - "workspace-login-handoff-issuer.ts"
Cohesion: 0.22
Nodes (12): buildWorkspaceHandoffExchangeUrl(), issueWorkspaceHandoffTicket(), normalizeWorkspaceHandoffOrigin(), sign(), WORKSPACE_HANDOFF_TICKET_TTL_SECONDS, issueWorkspaceLoginHandoff(), resolveLiveWorkspaceRuntimeOrigin(), resolveWorkspaceHandoffBoardIdentity() (+4 more)

### Community 35 - "normalizeHumanRole"
Cohesion: 0.23
Nodes (12): approveHumanJoinRequestFromInvite(), addCompanyMemberRemovalAccess(), assertCanManageCompanyMember(), getProtectedMemberReason(), resolveActorHumanRole(), grantsForHumanRole(), HUMAN_COMPANY_MEMBERSHIP_ROLES, normalizeHumanRole() (+4 more)

### Community 36 - "connectGalleryApp"
Cohesion: 0.19
Nodes (14): connectionUid(), googleSheetsAllowedSpreadsheetIds(), isGoogleSheetsConnectionConfig(), normalizeGoogleSheetsConnectionConfig(), normalizeKey(), appForConnectionSetup(), assertGoogleSheetsSpreadsheetOwnership(), assertSecretRefs() (+6 more)

### Community 37 - "types/resource-memberships.ts"
Cohesion: 0.17
Nodes (11): RESOURCE_MEMBERSHIP_STATES, ResourceMembershipResourceType, ResourceMemberships, ResourceMembershipState, ResourceMembershipUpdateResult, UpdateResourceMembership, resourceMembershipStateSchema, UpdateDocumentResourceMembership (+3 more)

### Community 38 - "workspace-command-authz.ts"
Cohesion: 0.47
Nodes (11): collectAgentAdapterWorkspaceCommandPaths(), collectExecutionWorkspaceCommandPaths(), collectExecutionWorkspaceConfigCommandPaths(), collectIssueWorkspaceCommandPaths(), collectProjectExecutionWorkspaceCommandPaths(), collectProjectWorkspaceCommandPaths(), collectWorkspaceRuntimeCommandPaths(), collectWorkspaceStrategyCommandPaths() (+3 more)

### Community 39 - "runLogin"
Cohesion: 0.19
Nodes (7): abandonAfterLostClaim(), runLogin(), conditionalTransition(), terminate(), CredentialPromotion, DisplayedCodeLoginProfile, LoginSessionLease

### Community 40 - "runtime-request-resolution-authority.ts"
Cohesion: 0.18
Nodes (10): APPROVAL_REQUEST_KINDS, canonicalPendingRequest(), NativeRuntimeRequestKind, NativeRuntimeRequestResolutionAuthorizationError, NativeRuntimeRequestResolver, PendingNativeRuntimeRequest, readPendingNativeRuntimeRequest(), record() (+2 more)

### Community 41 - "workspace-login-handoff-exchange.ts"
Cohesion: 0.21
Nodes (10): constantTimeMatches(), exchangeWorkspaceHandoffTicket(), WorkspaceHandoffClonedIdentity, WorkspaceHandoffExchangeDeps, WorkspaceHandoffExchangeResult, isPayloadShape(), sanitizeWorkspaceHandoffRedirectPath(), verifyWorkspaceHandoffTicket() (+2 more)

### Community 42 - "loginHome"
Cohesion: 0.38
Nodes (11): localAiLoginService(), cancel(), check(), complete(), reapExpired(), start(), loginHome(), prepareHome() (+3 more)

### Community 43 - "buildProfileDetails"
Cohesion: 0.24
Nodes (12): buildProfileDetails(), pendingNewToolsForProfile(), profileCoversCatalogScope(), profileEntryMatchesCatalog(), summarizeProfile(), getProfileRow(), listProfileNewTools(), profileDetails() (+4 more)

### Community 44 - "workspace-login-handoff-plugin.ts"
Cohesion: 0.27
Nodes (9): isWorkspaceHandoffRepairReason(), WorkspaceHandoffExchangeFailureReason, buildFallbackRedirect(), WorkspaceHandoffEndpointContext, WorkspaceHandoffExpectedIdentity, workspaceLoginHandoffPlugin(), WORKSPACE_HANDOFF_EXCHANGE_PATH, WORKSPACE_HANDOFF_TICKET_QUERY_PARAM (+1 more)

### Community 45 - "observeSandboxDelete"
Cohesion: 0.38
Nodes (8): createDeviceLoginReaper(), sweep(), sweepCleanupPending(), sweepExpiredSessions(), sweepOrphanLeases(), LoginSessionCleanupRuntime, isConfirmedDelete(), observeSandboxDelete()

### Community 46 - "registerOAuthClient"
Cohesion: 0.33
Nodes (9): actorForSecret(), assertOAuthDcrArray(), createOrRotateOAuthSecret(), invalidOAuthDcrResponse(), oauthSecretRef(), parseOAuthDcrString(), parseOAuthDcrTimestamp(), registerOAuthClient() (+1 more)

### Community 47 - "schema/auth.ts"
Cohesion: 0.33
Nodes (5): authAccounts, authSessions, authUsers, authVerifications, cliAuthChallenges

### Community 48 - "codex-auth-reconciliation.ts"
Cohesion: 0.57
Nodes (6): ApiKeyBinding, asRecord(), classifyApiKeyBinding(), CodexAuthReconciliationSummary, readPlainEnvValue(), reconcileCodexLocalManagedHomesOnStartup()

### Community 49 - "invite-rate-limit.ts"
Cohesion: 0.29
Nodes (5): createInviteRateLimiter(), INVITE_RATE_LIMIT_MAX_REQUESTS, INVITE_RATE_LIMIT_WINDOW_MS, InviteRateLimiter, InviteRateLimitResult

### Community 50 - "src/adapter-auth-session.ts"
Cohesion: 0.33
Nodes (3): ACTIVE_STATUS_SET, ADAPTER_AUTH_SESSION_ACTIVE_STATUSES, AdapterAuthSessionActiveStatus

### Community 51 - "runtimeHealth"
Cohesion: 0.33
Nodes (6): numberValue(), percent(), percentile(), buildRuntimeAlerts(), runtimeAlert(), runtimeHealth()

### Community 52 - "toCatalogEntryForConnection"
Cohesion: 0.33
Nodes (6): projectConnectionMethodToolInputSchema(), projectedConnectionToolInputSchema(), schemaHasInputProperties(), stripManagedToolArgumentSchema(), toCatalogEntry(), toCatalogEntryForConnection()

### Community 53 - "adapter_auth_sessions.ts"
Cohesion: 0.40
Nodes (3): ADAPTER_AUTH_SESSION_ACTIVE_STATES, adapterAuthSessions, AdapterAuthSessionState

### Community 54 - "createCompanyInviteForCompany"
Cohesion: 0.40
Nodes (5): createCompanyInviteForCompany(), companyInviteExpiresAt(), createInviteToken(), isInviteTokenHashCollisionError(), mergeInviteDefaults()

### Community 55 - "adapter-login-lease.ts"
Cohesion: 0.40
Nodes (4): AcquireLoginLeaseArgs, buildLoginLeaseAcquireArgs(), BuildLoginLeaseAcquireArgsOptions, LoginLeaseMetadata

### Community 56 - "loadGitHubGrantMetadata"
Cohesion: 0.50
Nodes (5): githubId(), githubInstallationManagementUrl(), loadGitHubGrantMetadata(), loadGitHubTokenRepositories(), recordValue()

### Community 58 - "classifyRisk"
Cohesion: 0.83
Nodes (4): classifyRisk(), isGmailToolPermanentlyBlocked(), normalizedProviderToolName(), verbMatches()

### Community 59 - "stableHash"
Cohesion: 0.50
Nodes (4): connectionSetupMutationFingerprint(), descriptorHash(), flattenKeys(), stableHash()

### Community 60 - "connectToolAppSchema"
Cohesion: 0.67
Nodes (3): connectToolAppSchema, rejectSensitiveConfigKeys(), rejectUnsafeHeaderCredentials()

## Knowledge Gaps
- **572 isolated node(s):** `AdapterAuthSessionState`, `ADAPTER_AUTH_SESSION_ACTIVE_STATES`, `adapterAuthSessions`, `agentMemberships`, `authSessions` (+567 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `toolAccessService()` connect `toolAccessService` to `toolAccessRoutes`, `connectGalleryApp`, `tool-access-policy.ts`, `services/tool-access.ts`, `completeOAuthCallback`, `buildProfileDetails`, `refreshCatalog`, `asRecord`, `toConnectionGrant`, `registerOAuthClient`, `discoverOAuthEndpoints`, `runtimeHealth`, `oauthConfig`, `toCatalogEntryForConnection`, `loadGitHubGrantMetadata`, `refreshOAuthGrantCredentials`?**
  _High betweenness centrality (0.147) - this node is a cross-community bridge._
- **Why does `toolAccessRoutes()` connect `toolAccessRoutes` to `toolAccessService`, `accessRoutes`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Why does `assertCompanyAccess()` connect `accessRoutes` to `routes/access.ts`, `toolAccessRoutes`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `toolAccessService()` (e.g. with `toCatalogEntry()` and `checkConnectionHealth()`) actually correct?**
  _`toolAccessService()` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `authorizationService()` (e.g. with `decide()` and `decidePrincipalGrant()`) actually correct?**
  _`authorizationService()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `AdapterAuthSessionState`, `ADAPTER_AUTH_SESSION_ACTIVE_STATES`, `adapterAuthSessions` to the rest of the system?**
  _572 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `validators/tool-access.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.012738853503184714 - nodes in this community are weakly interconnected._