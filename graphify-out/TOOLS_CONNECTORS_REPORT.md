# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 113 files · ~177,280 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1636 nodes · 3122 edges · 79 communities (71 shown, 8 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 65 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- validators/tool-access.ts
- types/tool-access.ts
- tool-access-policy.ts
- paperclip-runner-tool-authority.ts
- toolAccessService
- createToolGatewayService
- connectionIntentService
- services/tool-access.ts
- services/tool-gateway.ts
- paperclip-cloud-connector.ts
- refreshCatalog
- PluginToolRegistry
- completeOAuthCallback
- routes/tool-gateway.ts
- discoverOAuthEndpoints
- createToolRuntimeSupervisor
- Developer Category
- paperclip-cloud-connector-enrollment.ts
- tool_access.ts
- toolAccessRoutes
- Productivity Category
- executeRemoteHttpTool
- oauthConfig
- asRecord
- tool-content-guards.ts
- tool-oauth-legacy-backfill.ts
- Content Category
- Communication Category
- namedGatewaySessionFromBearer
- Commerce Category
- Data Category
- mcp-remote-headers.ts
- routes/tool-access.ts
- Ai Category
- Golden-Path Agent Tutorial
- connectGalleryApp
- startOAuth
- buildProfileDetails
- Appendix: Notion Dry Run (MCP-Direct With DCR)
- Analytics Category
- asRecord
- runTestToolInvocation
- resolveConnectionGrant
- Connection Authoring Runbook
- types/connection-intent.ts
- Detailed Design Checklist
- validators/connection-intent.ts
- refreshOAuthGrantCredentials
- Google Sheets (App)
- buildRemoteHeaders
- Gmail (App)
- Google Calendar (App)
- Google Chat (App)
- Google Docs (App)
- Google Drive (App)
- Google Slides (App)
- google-workspace-connectors.ts
- createPaperclipCloudConnector
- runtimeHealth
- projectedConnectionToolInputSchema
- connectedRemoteApprovalSnapshot
- API key app (App)
- connection-intent-guidance.ts
- github-connectors.ts
- loadGitHubGrantMetadata
- Mental Model: Five Independent Axes
- self-serve-mcp-research.ts
- classifyRisk
- tool-action-delivery.ts
- AppDefinition Field Reference
- MCP-Direct Connections (Hosted MCP + OAuth)
- mcp-config-help-prompt.ts
- projectedConnectionToolArguments
- ToolMcpGateway
- ToolMcpGatewayToken
- ToolProfile
- VercelConnectGrantReference
- assertSecretRefs
- isGoogleWorkspaceToolAllowed

## God Nodes (most connected - your core abstractions)
1. `toolAccessService()` - 261 edges
2. `createToolGatewayService()` - 115 edges
3. `asRecord()` - 55 edges
4. `toolAccessRoutes()` - 46 edges
5. `connectGalleryApp()` - 34 edges
6. `toolAccessPolicyService()` - 31 edges
7. `oauthConfig()` - 29 edges
8. `refreshCatalog()` - 28 edges
9. `executeApprovedAgentInvocation()` - 27 edges
10. `connectionIntentService()` - 26 edges
11. `refreshOAuthGrantCredentials()` - 26 edges
12. `completeOAuthCallback()` - 26 edges
13. `checkConnectionHealth()` - 25 edges
14. `getConnectionRow()` - 23 edges
15. `remoteTools()` - 22 edges

## Surprising Connections (you probably didn't know these)
- `wakeAfterResolution()` --calls--> `connectionIntentDeliveryService()`  [EXTRACTED]
  server/src/routes/connection-intents.ts → server/src/services/connection-intent-delivery.ts
- `toolAccessRoutes()` --calls--> `connectionIntentService()`  [EXTRACTED]
  server/src/routes/tool-access.ts → server/src/services/connection-intents.ts
- `toolAccessRoutes()` --calls--> `appWithPaperclipCloudConnectorAvailability()`  [EXTRACTED]
  server/src/routes/tool-access.ts → server/src/services/paperclip-cloud-connector.ts
- `toolAccessRoutes()` --calls--> `completePaperclipCloudConnectorEnrollment()`  [EXTRACTED]
  server/src/routes/tool-access.ts → server/src/services/paperclip-cloud-connector-enrollment.ts
- `toolAccessRoutes()` --calls--> `loadPaperclipCloudConnectorIdentity()`  [EXTRACTED]
  server/src/routes/tool-access.ts → server/src/services/paperclip-cloud-connector-enrollment.ts

## Import Cycles
- None detected.

## Communities (79 total, 8 thin omitted)

### Community 0 - "validators/tool-access.ts"
Cohesion: 0.01
Nodes (153): actorConditionSchema, argumentConditionSchema, connectionGrantKindSchema, connectionGrantSchema, connectionGrantStatusSchema, connectionTokenIssuancePathSchema, ConnectionTokenRequestInput, connectionTokenRequestSchema (+145 more)

### Community 1 - "types/tool-access.ts"
Cohesion: 0.02
Nodes (129): CONNECTION_RECOVERABLE_ERROR_CODES, ConnectionAudienceMember, ConnectionGrant, ConnectionGrantCapabilities, ConnectionGrantDelegation, ConnectionGrantKind, ConnectionGrantMember, ConnectionGrantMemberSubjectType (+121 more)

### Community 2 - "tool-access-policy.ts"
Cohesion: 0.05
Nodes (79): argumentConditionMatches(), argumentFiltersMatch(), assertGenericPolicyType(), assertSupportedGenericPolicyShape(), assertSupportedPolicyConditions(), asToolRiskLevel(), auditOutcome(), boolCondition() (+71 more)

### Community 3 - "paperclip-runner-tool-authority.ts"
Cohesion: 0.07
Nodes (36): projectToolRoutes(), AgentBinding, annotateConnectorSkills(), applyConnectorSkills(), ConnectorAssignment, ConnectorDefinition, connectors, executeConnectorTool() (+28 more)

### Community 4 - "toolAccessService"
Cohesion: 0.05
Nodes (44): builtInStdioTemplate(), normalizeToolDescriptor(), readStdioTemplateId(), toConnectionInstall(), toolAccessService(), assertApplication(), assertCatalogEntry(), assertConfiguredTokenBrokerEndpointsAllowed() (+36 more)

### Community 5 - "createToolGatewayService"
Cohesion: 0.09
Nodes (45): createToolGatewayService(), allTools(), approvedManagedArgumentsRemainCurrent(), assertAgentInCompany(), assertGatewayContext(), assertGatewayTokenAction(), assertIssueOpenForApprovedAction(), connectedMcpToolsForCompany() (+37 more)

### Community 6 - "connectionIntentService"
Cohesion: 0.10
Nodes (39): bearer(), connectionIntentBoardRoutes(), bypassCurrentMembershipCheck(), canManageCompanyConnections(), wakeAfterResolution(), Heartbeat, resultContent(), runtimeClaims() (+31 more)

### Community 7 - "services/tool-access.ts"
Cohesion: 0.05
Nodes (41): RFC-6749, RFC-7591, RFC-8414, RFC-9207, RFC-9728, ACTIVE_BROKER_RUN_STATUSES, ActorInfo, APPROVED_STDIO_TEMPLATES (+33 more)

### Community 8 - "services/tool-gateway.ts"
Cohesion: 0.06
Nodes (39): AgentToolDescriptor, ACTIVE_GATEWAY_RUN_STATUSES, approvalSnapshotsMatch(), buildHumanizedActionPreview(), BUILTIN_LOCAL_STDIO_RUNTIME_TEMPLATES, BUILTIN_TOOLS, ConnectedCredentialVersionSnapshot, ConnectedMcpGatewayMetadata (+31 more)

### Community 9 - "paperclip-cloud-connector.ts"
Cohesion: 0.08
Nodes (33): badEnvelope(), base64Url(), connectorProfileDefinition(), ConnectorResponse, call(), openCredentials(), decryptEnvelope(), ED25519_PKCS8_PREFIX (+25 more)

### Community 10 - "refreshCatalog"
Cohesion: 0.12
Nodes (39): healthFailureHttpStatus(), sanitizeHttpFailure(), toConnection(), assertComposioConnectedAccountActive(), audit(), auditConnectionTokenIssuance(), checkConnectionHealth(), classifyConnectionSecrets() (+31 more)

### Community 11 - "PluginToolRegistry"
Cohesion: 0.07
Nodes (13): createPluginToolDispatcher(), handlePluginEnabled(), registerFromDb(), PluginToolDispatcher, PluginToolDispatcherOptions, createPluginToolRegistry(), addTool(), buildName() (+5 more)

### Community 12 - "completeOAuthCallback"
Cohesion: 0.10
Nodes (35): connectionMethodForConnection(), managedConnectorProfile(), normalizeOAuthProviderError(), oauthProviderErrorMessage(), toApplication(), actionSummary(), actorForSecret(), assertAgentsInCompany() (+27 more)

### Community 13 - "routes/tool-gateway.ts"
Cohesion: 0.10
Nodes (25): createToolMcpGatewaySchema, createToolMcpGatewayTokenSchema, updateToolMcpGatewaySchema, bearerToken(), callerHeaders(), decodeAuditCursor(), encodeAuditCursor(), gatewayToken() (+17 more)

### Community 14 - "discoverOAuthEndpoints"
Cohesion: 0.11
Nodes (31): canonicalResourceIndicator(), connectionMethodFor(), credentialFieldsFor(), originOf(), protectedResourceMetadataUrls(), remoteEndpoint(), allowPrivateRemoteEndpoints(), assertNotSmokeLabOAuthEndpoints() (+23 more)

### Community 15 - "createToolRuntimeSupervisor"
Cohesion: 0.13
Nodes (26): ACTIVE_SLOT_STATUSES, asRecord(), createToolRuntimeSupervisor(), activeRows(), assertCapacity(), assertLocalStdioAvailable(), assertRestartAllowed(), ensureRunningSlot() (+18 more)

### Community 16 - "Developer Category"
Cohesion: 0.07
Nodes (30): Cloudflare (App), Context7 (App), GitHub (App), Kernel (App), Netlify (App), PagerDuty (App), Postman (App), Sentry (App) (+22 more)

### Community 17 - "paperclip-cloud-connector-enrollment.ts"
Cohesion: 0.16
Nodes (27): completePaperclipCloudConnectorEnrollment(), completePaperclipCloudConnectorEnrollmentUnlocked(), connectorEnvironment(), connectorTarget(), createIdentity(), enrollmentMutationTail, hasManagedConnectorIdentityOverride(), identityMatchesTarget() (+19 more)

### Community 18 - "tool_access.ts"
Cohesion: 0.07
Nodes (26): connectionGrantDelegations, connectionGrantMembers, connectionGrants, connectionTokenIssuances, toolAccessAuditEvents, toolActionRequests, toolApplications, toolCallEvents (+18 more)

### Community 19 - "toolAccessRoutes"
Cohesion: 0.12
Nodes (21): toolAccessRoutes(), activeToolMembership(), assertBoardToolPermission(), assertToolAppMutationAccess(), assertToolConnectionAccess(), assertToolConnectionConfigureAccess(), assertToolsAdmin(), assertToolsRuntimeManage() (+13 more)

### Community 20 - "Productivity Category"
Cohesion: 0.08
Nodes (24): Asana (App), Coda (App), Composio (App), Jira (App), Linear (App), Make (App), Manufact (App), Miro (App) (+16 more)

### Community 21 - "executeRemoteHttpTool"
Cohesion: 0.14
Nodes (22): initializeMcpHttpSession(), looksLikeJsonRpcMessage(), MCP_HTTP_ACCEPT, MCP_PROTOCOL_VERSION, McpHttpInitializationError, mcpHttpRequestHeaders(), parseMcpHttpResponseBody(), projectedConnectionHeaders() (+14 more)

### Community 22 - "oauthConfig"
Cohesion: 0.17
Nodes (24): credentialRefConfigPath(), resolveOAuthClientIdMetadataDocumentUrl(), sameOAuthIssuer(), singleFlight(), acquireOAuthRefreshLease(), adoptClientIdMetadataDocument(), assertOAuthCallbackIssuer(), clearOAuthRefreshLease() (+16 more)

### Community 23 - "asRecord"
Cohesion: 0.16
Nodes (23): asRecord(), accessContextForBroker(), annotateGitHubAuthorization(), configuredTokenBrokerExchangeUrls(), connectionTokenBrokerEnabled(), defaultScopesForConnection(), enforceDefaultConnectionTokenRateLimit(), exchangeTokenUrl() (+15 more)

### Community 24 - "tool-content-guards.ts"
Cohesion: 0.16
Nodes (19): canonicalToolArguments(), hashToolValue(), isPlainObject(), PROMPT_INJECTION_PATTERNS, readSignedToolArguments(), readSignedToolArgumentsPayload(), resolveToolActionSigningSecret(), scanPromptInjection() (+11 more)

### Community 25 - "tool-oauth-legacy-backfill.ts"
Cohesion: 0.17
Nodes (21): asRecord(), backfillLegacyToolOAuthTokens(), configPath(), DbTransaction, hasRawOauthTokenKeys(), LegacyOAuthToken, OAuthTokenKind, RAW_OAUTH_TOKEN_KEYS (+13 more)

### Community 26 - "Content Category"
Cohesion: 0.10
Nodes (21): beehiiv (App), Box (App), Cloudinary (App), Egnyte (App), Notion (App), O'Reilly (App), Sanity (App), Webflow (App) (+13 more)

### Community 27 - "Communication Category"
Cohesion: 0.10
Nodes (20): AgentMail (App), Discord (App), Google People (App), iMessage Photon (App), Microsoft Teams (App), Resend (App), Slack (App), Telegram (App) (+12 more)

### Community 28 - "namedGatewaySessionFromBearer"
Cohesion: 0.16
Nodes (19): assertNamedGatewayProtocolLimit(), assertSessionRunIsActive(), captureSessionIdentity(), consumeProtocolRateLimit(), findGatewayForProtocolLocator(), getActiveSession(), namedGatewaySessionFromBearer(), normalizeGatewayTokenActions() (+11 more)

### Community 29 - "Commerce Category"
Cohesion: 0.11
Nodes (18): Brex (App), Embat (App), Razorpay (App), Shopify (App), Stripe (App), Ticket Tailor (App), Xero (App), Commerce Category (+10 more)

### Community 30 - "Data Category"
Cohesion: 0.12
Nodes (17): Airtable (App), Candid (App), ClickHouse (App), Google Workspace Search (App), PlanetScale (App), Supabase (App), Data Category, Profile: workspace-search.read (+9 more)

### Community 31 - "mcp-remote-headers.ts"
Cohesion: 0.15
Nodes (16): RFC-9110, checkMcpRemoteHeaderName(), checkMcpRemoteHeaderValue(), FORBIDDEN_HEADER_NAMES, FORBIDDEN_HEADER_PREFIXES, isSafeMcpRemoteHeaderName(), isSafeMcpRemoteHeaderValue(), MCP_REMOTE_HEADER_LIMITS (+8 more)

### Community 32 - "routes/tool-access.ts"
Cohesion: 0.15
Nodes (16): agentOrgDepths(), allowlistIds(), classifyConnectionUpdate(), cloudConnectorEnrollmentOutcomeHtml(), cloudConnectorEnrollmentReturnPath(), connectionIntentOAuthOutcomeHtml(), filterVisibleToolConnections(), Heartbeat (+8 more)

### Community 33 - "Ai Category"
Cohesion: 0.12
Nodes (16): Anthropic (App), Hugging Face (App), Mem0 (App), OpenAI (App), OpenRouter (App), Grok (App), Ai Category, Anthropic [ai-api_key / runtime_auth] (+8 more)

### Community 34 - "Golden-Path Agent Tutorial"
Cohesion: 0.12
Nodes (16): Connection UX and user journeys, Connector-provided skills and tools, Golden-Path Agent Tutorial, Phase 0: Establish scope and preserve the worktree, Phase 10: Verify APIs and audit without exposing credentials, Phase 11: Run the PR-ready verification ladder, Phase 12: Prepare and submit the pull request, Phase 1: Research the provider from primary sources (+8 more)

### Community 35 - "connectGalleryApp"
Cohesion: 0.17
Nodes (15): connectionUid(), googleSheetsAllowedSpreadsheetIds(), googleSheetsRobotEmailFromEnv(), isGoogleSheetsConnectionConfig(), isOAuthEndpointRejection(), normalizeConnectionMethodConfig(), normalizeGoogleSheetsConnectionConfig(), normalizeKey() (+7 more)

### Community 36 - "startOAuth"
Cohesion: 0.16
Nodes (14): actorBinding(), connectionSetupMutationFingerprint(), descriptorHash(), flattenKeys(), stableHash(), assertOAuthRedirectConstraints(), base64UrlSha256(), credentialScope() (+6 more)

### Community 37 - "buildProfileDetails"
Cohesion: 0.20
Nodes (14): buildProfileDetails(), pendingNewToolsForProfile(), profileCoversCatalogScope(), profileEntryMatchesCatalog(), summarizeProfile(), getProfileRow(), listProfileNewTools(), profileDetails() (+6 more)

### Community 38 - "Appendix: Notion Dry Run (MCP-Direct With DCR)"
Cohesion: 0.22
Nodes (14): Actions, Administrator Setup (mandatory), AppDefinition catalog authoring, Appendix: Linear Dry Run, Appendix: Notion Dry Run (MCP-Direct With DCR), Connection Flow (mandatory), Dry-Run Request Log (PAP-16649, 2026-08-06/07), Governance Defaults (+6 more)

### Community 39 - "Analytics Category"
Cohesion: 0.15
Nodes (13): Bitly (App), Local Falcon (App), Mixpanel (App), PostHog (App), Similarweb (App), Analytics Category, Bitly [mcp-api-key / mcp_remote], Bitly [mcp-oauth / mcp_remote] (+5 more)

### Community 40 - "asRecord"
Cohesion: 0.23
Nodes (12): asRecord(), elicitationQuestions(), enumOptions(), executeBuiltinTool(), extractMcpElicitationRequest(), malformedRemoteMcpResponse(), normalizeMcpContent(), normalizeMcpToolResult() (+4 more)

### Community 41 - "runTestToolInvocation"
Cohesion: 0.24
Nodes (12): approvalRequiredInstructions(), requestApprovalForRecordedToolCall(), requestElicitationForRecordedToolCall(), runTestToolInvocation(), throwApprovalRequired(), writeAudit(), writeToolCallEvent(), executionAuditFromError() (+4 more)

### Community 42 - "resolveConnectionGrant"
Cohesion: 0.21
Nodes (12): callAssignedConnectionProtocol(), callLocalStdioMcp(), createUserAuthorizationInteraction(), executeLocalStdioTool(), localStdioEnvironment(), localStdioTemplateId(), resolveConnectedLocalStdioTool(), resolveConnectionGrant() (+4 more)

### Community 43 - "Connection Authoring Runbook"
Cohesion: 0.18
Nodes (10): Architecture From Setup To Agent Call, Connection Authoring Runbook, Contents, Current Default Access Policy, Definition Of Done, Output, Secret Storage And Lifecycle, Template (+2 more)

### Community 44 - "types/connection-intent.ts"
Cohesion: 0.20
Nodes (9): CompleteConnectionIntentInput, ConnectionAvailabilityState, ConnectionIntentSetupConnection, ConnectionIntentSetupOptions, ConnectionRequestResult, ConnectionSearchResultItem, ConnectionsSearchResult, DeclineConnectionIntentInput (+1 more)

### Community 45 - "Detailed Design Checklist"
Cohesion: 0.20
Nodes (10): Detailed Design Checklist, Step 1: Confirm It Is A Catalog Entry, Step 2: Classify The Reuse Path, Step 3: Pick Auth And Credential Ownership, Step 4: Author The AppDefinition, Step 5: Model Resource Filters, Step 6: Define The Action Catalog, Step 7: Select The Wizard Path (+2 more)

### Community 46 - "validators/connection-intent.ts"
Cohesion: 0.22
Nodes (8): CompleteConnectionIntent, completeConnectionIntentSchema, ConnectionRequestInput, connectionRequestInputSchema, ConnectionsSearchInput, connectionsSearchInputSchema, DeclineConnectionIntent, declineConnectionIntentSchema

### Community 47 - "refreshOAuthGrantCredentials"
Cohesion: 0.47
Nodes (9): acquireOAuthGrantRefreshLease(), clearOAuthGrantRefreshLease(), getOAuthGrantRow(), oauthGrantConfig(), oauthGrantExpiresAtMs(), refreshManagedGitHubGrantAccessOnce(), refreshOAuthGrantCredentials(), resolveOAuthGrantSecret() (+1 more)

### Community 48 - "Google Sheets (App)"
Cohesion: 0.25
Nodes (8): Google Sheets (App), Profile: sheets.read, Profile: sheets.write, Google Sheets [customer-read-oauth / mcp_remote], Google Sheets [customer-write-oauth / mcp_remote], Google Sheets [local / local_stdio], Google Sheets [paperclip-read / mcp_remote], Google Sheets [paperclip-write / mcp_remote]

### Community 49 - "buildRemoteHeaders"
Cohesion: 0.39
Nodes (8): buildRemoteHeaders(), headerName(), headerValue(), metadataHeadersForSession(), normalizeCallerHeaders(), readHeaderPolicy(), stringArray(), isSensitivePassthroughHeader()

### Community 50 - "Gmail (App)"
Cohesion: 0.29
Nodes (7): Gmail (App), Profile: gmail.draft, Profile: gmail.read, Gmail [customer-draft-oauth / mcp_remote], Gmail [customer-read-oauth / mcp_remote], Gmail [paperclip-draft / mcp_remote], Gmail [paperclip-read / mcp_remote]

### Community 51 - "Google Calendar (App)"
Cohesion: 0.29
Nodes (7): Google Calendar (App), Profile: calendar.read, Profile: calendar.write, Google Calendar [customer-read-oauth / mcp_remote], Google Calendar [customer-write-oauth / mcp_remote], Google Calendar [paperclip-read / mcp_remote], Google Calendar [paperclip-write / mcp_remote]

### Community 52 - "Google Chat (App)"
Cohesion: 0.29
Nodes (7): Google Chat (App), Profile: chat.read, Profile: chat.write, Google Chat [customer-read-oauth / mcp_remote], Google Chat [customer-write-oauth / mcp_remote], Google Chat [paperclip-read / mcp_remote], Google Chat [paperclip-write / mcp_remote]

### Community 53 - "Google Docs (App)"
Cohesion: 0.29
Nodes (7): Google Docs (App), Profile: docs.read, Profile: docs.write, Google Docs [customer-read-oauth / mcp_remote], Google Docs [customer-write-oauth / mcp_remote], Google Docs [paperclip-read / mcp_remote], Google Docs [paperclip-write / mcp_remote]

### Community 54 - "Google Drive (App)"
Cohesion: 0.29
Nodes (7): Google Drive (App), Profile: drive.read, Profile: drive.write, Google Drive [customer-read-oauth / mcp_remote], Google Drive [customer-write-oauth / mcp_remote], Google Drive [paperclip-read / mcp_remote], Google Drive [paperclip-write / mcp_remote]

### Community 55 - "Google Slides (App)"
Cohesion: 0.29
Nodes (7): Google Slides (App), Profile: slides.read, Profile: slides.write, Google Slides [customer-read-oauth / mcp_remote], Google Slides [customer-write-oauth / mcp_remote], Google Slides [paperclip-read / mcp_remote], Google Slides [paperclip-write / mcp_remote]

### Community 56 - "google-workspace-connectors.ts"
Cohesion: 0.29
Nodes (3): GOOGLE_WORKSPACE_CONNECTOR_PROFILE_IDS, GOOGLE_WORKSPACE_CONNECTOR_PROFILES, GoogleWorkspaceConnectorProfileId

### Community 57 - "createPaperclipCloudConnector"
Cohesion: 0.43
Nodes (6): createPaperclipCloudConnector(), isLoopback(), paperclipCloudConnectorCapabilitiesFromEnv(), paperclipCloudConnectorConfigFromEnv(), privateKey(), reconcilePaperclipCloudConnectorEnrollmentStatus()

### Community 58 - "runtimeHealth"
Cohesion: 0.33
Nodes (6): numberValue(), percent(), percentile(), buildRuntimeAlerts(), runtimeAlert(), runtimeHealth()

### Community 59 - "projectedConnectionToolInputSchema"
Cohesion: 0.33
Nodes (6): projectConnectionMethodToolInputSchema(), projectedConnectionToolInputSchema(), schemaHasInputProperties(), stripManagedToolArgumentSchema(), toCatalogEntry(), toCatalogEntryForConnection()

### Community 60 - "connectedRemoteApprovalSnapshot"
Cohesion: 0.40
Nodes (6): connectedCredentialVersionSnapshots(), connectedRemoteApprovalSnapshot(), credentialVersionRefHash(), grantRefForCredential(), resolveConnectedCredentialVersion(), stableHash()

### Community 61 - "API key app (App)"
Cohesion: 0.40
Nodes (5): API key app (App), OAuth app (App), Other Category, API key app [api-key / rest_api], OAuth app [oauth / rest_api]

### Community 62 - "connection-intent-guidance.ts"
Cohesion: 0.40
Nodes (4): CONNECTION_INTENT_AGENT_GUIDANCE, CONNECTION_REQUEST_TOOL_DESCRIPTION, CONNECTION_RUNTIME_TOOL_NAMES, CONNECTIONS_SEARCH_TOOL_DESCRIPTION

### Community 63 - "github-connectors.ts"
Cohesion: 0.40
Nodes (3): GITHUB_CONNECTOR_PROFILE_IDS, GITHUB_CONNECTOR_PROFILES, GitHubConnectorProfileId

### Community 64 - "loadGitHubGrantMetadata"
Cohesion: 0.50
Nodes (5): githubId(), githubInstallationManagementUrl(), loadGitHubGrantMetadata(), loadGitHubTokenRepositories(), recordValue()

### Community 65 - "Mental Model: Five Independent Axes"
Cohesion: 0.40
Nodes (5): Authentication support matrix, Credential source is not OAuth client ownership, Mental Model: Five Independent Axes, OAuth client resolution order, Transport support and boundaries

### Community 66 - "self-serve-mcp-research.ts"
Cohesion: 0.50
Nodes (3): BLOCKED_MCP_PROVIDERS, SELF_SERVE_MCP_CANDIDATES, SELF_SERVE_MCP_RESEARCH

### Community 67 - "classifyRisk"
Cohesion: 0.83
Nodes (4): classifyRisk(), isGmailToolPermanentlyBlocked(), normalizedProviderToolName(), verbMatches()

### Community 69 - "AppDefinition Field Reference"
Cohesion: 0.50
Nodes (4): App-level fields, AppDefinition Field Reference, Field definition rules, Method fields

### Community 70 - "MCP-Direct Connections (Hosted MCP + OAuth)"
Cohesion: 0.50
Nodes (4): Documentation standards for every connection doc, Dynamic client registration (RFC 7591), MCP-Direct Connections (Hosted MCP + OAuth), Redirect-URI constraints

### Community 72 - "projectedConnectionToolArguments"
Cohesion: 0.67
Nodes (3): mergeManagedToolArguments(), projectConnectionMethodToolArguments(), projectedConnectionToolArguments()

## Knowledge Gaps
- **622 isolated node(s):** `toolApplications`, `toolConnections`, `connectionGrants`, `connectionGrantMembers`, `connectionGrantDelegations` (+617 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `toolAccessService()` connect `toolAccessService` to `tool-access-policy.ts`, `connectionIntentService`, `services/tool-access.ts`, `refreshCatalog`, `completeOAuthCallback`, `routes/tool-gateway.ts`, `discoverOAuthEndpoints`, `createToolRuntimeSupervisor`, `toolAccessRoutes`, `oauthConfig`, `asRecord`, `tool-content-guards.ts`, `routes/tool-access.ts`, `connectGalleryApp`, `startOAuth`, `buildProfileDetails`, `refreshOAuthGrantCredentials`, `createPaperclipCloudConnector`, `runtimeHealth`, `projectedConnectionToolInputSchema`, `loadGitHubGrantMetadata`, `assertSecretRefs`?**
  _High betweenness centrality (0.144) - this node is a cross-community bridge._
- **Why does `createToolGatewayService()` connect `createToolGatewayService` to `tool-access-policy.ts`, `services/tool-gateway.ts`, `runTestToolInvocation`, `resolveConnectionGrant`, `asRecord`, `connectedRemoteApprovalSnapshot`, `createToolRuntimeSupervisor`, `buildRemoteHeaders`, `executeRemoteHttpTool`, `tool-content-guards.ts`, `createPaperclipCloudConnector`, `namedGatewaySessionFromBearer`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `listConnectionLifecycleEvents()` connect `routes/tool-gateway.ts` to `toolAccessService`, `services/tool-access.ts`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `toolAccessService()` (e.g. with `toCatalogEntry()` and `checkConnectionHealth()`) actually correct?**
  _`toolAccessService()` has 29 INFERRED edges - model-reasoned connections that need verification._
- **What connects `toolApplications`, `toolConnections`, `connectionGrants` to the rest of the system?**
  _622 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `validators/tool-access.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.012987012987012988 - nodes in this community are weakly interconnected._
- **Should `types/tool-access.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.015384615384615385 - nodes in this community are weakly interconnected._