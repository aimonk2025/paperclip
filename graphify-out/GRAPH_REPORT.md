# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 500 files · ~255,322 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2860 nodes · 5713 edges · 335 communities (287 shown, 48 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 125 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- constants.ts
- schema/index.ts
- check-migration-safety.ts
- toolAccessService
- tool-access.ts
- tool-access-policy.ts
- test-embedded-postgres.ts
- worktree.ts
- client.ts
- backup-lib.ts
- wake-queue/adapters/postgres.ts
- "tool_call_events"
- companies.ts
- company-portability.ts
- completeOAuthCallback
- oauthConfig
- authorization.ts
- 0255_previous_captain_america.sql
- issues.ts
- refreshCatalog
- runWorktreeInit
- types/access.ts
- worktree-lib.ts
- services/access.ts
- plugin-database.ts
- asRecord
- applyPendingMigrations
- plugins
- Database
- runWorktreeReseed
- authorizationService
- accessService
- document_annotation_threads.ts
- better-auth.ts
- src/index.ts
- migration-runtime.ts
- discoverOAuthEndpoints
- chat_channels.ts
- 0000_mature_masked_marvel.sql
- decideBase
- connectGalleryApp
- runtime-config.ts
- active-run-watchdog/adapters/postgres.ts
- pipeline_cases.ts
- companies
- SeedWorktreeDatabase
- cases.ts
- boardAuthService
- 0014_many_mikhail_rasputin.sql
- "public"."issues"
- 0029_plugin_tables.sql
- board-auth.ts
- company_secrets.ts
- ensureWorktreeSeeded
- embedded-postgres-supervisor.ts
- adapter_auth_sessions.ts
- ensurePostgresDatabase
- environment_custom_image_setup_sessions.ts
- "decision_triage_events"
- "issues"
- native_run_finalizations.ts
- "document_revisions"
- "execution_workspaces"
- 0113_pipeline_foundation.sql
- "tool_mcp_gateways"
- check-migration-numbering.ts
- "issue_attachments"
- "finance_events"
- "environment_leases"
- 0227_modern_pandemic.sql
- authUsers
- registerOAuthClient
- auth-bootstrap-ceo.ts
- issue-comment-derived-attribution-migration.test.ts
- "workspace_runtime_services"
- "issue_plan_decompositions"
- "environment_custom_image_setup_sessions"
- "connection_grants"
- "chat_teams_file_transfers"
- run-event-payload.ts
- queued-comment-postgres.ts
- agent-permissions.ts
- configure.ts
- client.test.ts
- "heartbeat_run_events"
- "issue_approvals"
- 0143_cases_foundation.sql
- "execution_workspace_runtime_leases"
- "connection_grant_delegations"
- migration-snapshot-drift.test.ts
- "company_secret_versions"
- "issue_labels"
- "budget_incidents"
- "workspace_operations"
- "issue_execution_decisions"
- "decision_retention"
- decision-queue-migrations.test.ts
- "approval_comments"
- "agent_task_sessions"
- "project_goals"
- "issue_relations"
- 0197_decisions_v1.sql
- "managed_agent_profiles"
- registerSeedInterruptHandler
- "project_workspaces"
- "company_logos"
- 0039_fat_magneto.sql
- 0056_spooky_ultragirl.sql
- 0091_old_swarm.sql
- 0099_skills_store_foundation.sql
- "adapter_auth_sessions"
- "claude_setup_token_sessions"
- 0272_light_kate_bishop.sql
- 0277_uneven_lady_deathstrike.sql
- "instance_settings"
- 0044_illegal_toad.sql
- 0059_plugin_database_namespaces.sql
- 0066_issue_tree_holds.sql
- 0082_dry_vision.sql
- 0089_cloud_upstreams.sql
- 0090_resource_memberships.sql
- 0106_external_object_references.sql
- 0128_user_specific_secrets.sql
- 0137_skill_studio_server_foundation.sql
- "tool_stdio_command_templates"
- 0166_smoke_lab_results.sql
- 0173_inbox_policy_agent_cleanup.sql
- 0185_status_cards.sql
- "company_transfer_runs"
- "connection_event_deliveries"
- "run_identity_contexts"
- connection-grants-phase2-migration.test.ts
- 0042_spotty_the_renegades.sql
- 0053_sharp_wild_child.sql
- 0060_orange_annihilus.sql
- 0070_active_run_output_watchdog.sql
- 0076_useful_elektra.sql
- 0077_unusual_karnak.sql
- 0083_company_secret_provider_configs.sql
- 0084_issue_recovery_actions.sql
- 0104_issue_watchdogs.sql
- 0109_routine_description_annotations.sql
- 0122_pipeline_case_documents.sql
- 0135_repair_run_responsible_user_updated_at_sweep.sql
- 0139_skill_studio_run_templates.sql
- 0140_built_in_managed_resources.sql
- 0162_tool_runtime_metric_counters.sql
- 0165_connection_token_issuances.sql
- 0168_tool_connection_installs.sql
- 0169_tool_gateway_protocol_rate_limit_counters.sql
- 0172_inbox_archive_agent_policies.sql
- 0174_folders.sql
- 0178_summary_slots.sql
- 0207_moaning_amazoness.sql
- 0216_company_onboarding_seeds.sql
- 0228_nasty_grim_reaper.sql
- 0234_provider_trace_records.sql
- 0246_nostalgic_medusa.sql
- 0248_small_manta.sql
- 0249_fast_silverclaw.sql
- 0267_warm_wild_child.sql
- 0276_hard_mandroid.sql

## God Nodes (most connected - your core abstractions)
1. `toolAccessService()` - 249 edges
2. `companies` - 126 edges
3. `agents` - 69 edges
4. `issues` - 66 edges
5. `asRecord()` - 55 edges
6. `heartbeatRuns` - 45 edges
7. `authorizationService()` - 39 edges
8. `startEmbeddedPostgresTestDatabase()` - 38 edges
9. `connectGalleryApp()` - 34 edges
10. `decideBase()` - 33 edges
11. `accessService()` - 29 edges
12. `oauthConfig()` - 29 edges
13. `getEmbeddedPostgresTestSupport()` - 28 edges
14. `refreshCatalog()` - 28 edges
15. `toolAccessPolicyService()` - 27 edges

## Surprising Connections (you probably didn't know these)
- `bootstrapCeoInvite()` --calls--> `createDb()`  [EXTRACTED]
  cli/src/commands/auth-bootstrap-ceo.ts → packages/db/src/client.ts
- `SeedWorktreeDatabase` --calls--> `formatDatabaseBackupResult()`  [EXTRACTED]
  cli/src/commands/worktree.ts → packages/db/src/backup-lib.ts
- `SeedWorktreeDatabase` --calls--> `runDatabaseBackup()`  [EXTRACTED]
  cli/src/commands/worktree.ts → packages/db/src/backup-lib.ts
- `SeedWorktreeDatabase` --calls--> `runDatabaseRestore()`  [EXTRACTED]
  cli/src/commands/worktree.ts → packages/db/src/backup-lib.ts
- `SeedWorktreeDatabase` --calls--> `applyPendingMigrations()`  [EXTRACTED]
  cli/src/commands/worktree.ts → packages/db/src/client.ts

## Import Cycles
- None detected.

## Communities (335 total, 48 thin omitted)

### Community 0 - "constants.ts"
Cohesion: 0.01
Nodes (377): ADAPTER_AGNOSTIC_KEYS, AdapterAgnosticKey, AGENT_ADAPTER_TYPES, AGENT_DEFAULT_MAX_CONCURRENT_RUNS, AGENT_ICON_NAMES, AGENT_ROLE_LABELS, AGENT_ROLES, AGENT_STATUSES (+369 more)

### Community 1 - "schema/index.ts"
Cohesion: 0.03
Nodes (71): agentApiKeys, agentConfigRevisions, agentMemberships, agentRuntimeState, agentSessionGoalActions, agentTaskSessions, aiConnectionDefaults, aiProviderDefaults (+63 more)

### Community 2 - "check-migration-safety.ts"
Cohesion: 0.05
Nodes (78): addFindingOnce(), analyzeMigrationSafety(), batchWhereClausesBeforeOrderBy(), CreateIndexInfo, dollarQuoteTagAt(), estimatesByTable(), estimateSuffix(), findingId() (+70 more)

### Community 3 - "toolAccessService"
Cohesion: 0.04
Nodes (65): builtInStdioTemplate(), normalizeToolDescriptor(), readStdioTemplateId(), toConnectionInstall(), toolAccessService(), assertAgentsInCompany(), assertApplication(), assertCatalogEntriesForConnection() (+57 more)

### Community 4 - "tool-access.ts"
Cohesion: 0.04
Nodes (71): RFC-6749, RFC-7591, RFC-8414, RFC-8707, RFC-9207, RFC-9728, isUniqueViolation(), ACTIVE_BROKER_RUN_STATUSES (+63 more)

### Community 5 - "tool-access-policy.ts"
Cohesion: 0.06
Nodes (70): toolActionRequests, toolApplications, toolMcpGateways, toolProfileBindings, toolProfiles, toolRateLimitCounters, argumentConditionMatches(), argumentFiltersMatch() (+62 more)

### Community 6 - "test-embedded-postgres.ts"
Cohesion: 0.05
Nodes (40): cleanups, cleanups, cleanups, cleanups, cleanups, cleanups, cleanups, createTempDatabase() (+32 more)

### Community 7 - "worktree.ts"
Cohesion: 0.04
Nodes (55): activeSeedInterruptHandlers, applyMergePlan(), ClosableDb, collectClaimedWorktreePorts(), ConfiguredStorage, CopiedGitHooksResult, copyDirectoryContents(), copyGitHooksToWorktreeGitDir() (+47 more)

### Community 8 - "client.ts"
Cohesion: 0.07
Nodes (53): applyPendingMigrationsManually(), clientFinalizer, clientsByHostPort, closeRegisteredClients(), columnExists(), columnHasDataType(), constraintExists(), createDb() (+45 more)

### Community 9 - "backup-lib.ts"
Cohesion: 0.07
Nodes (49): dbBackupCommand(), DbBackupOptions, normalizeRetentionDays(), resolveBackupDir(), resolveConnectionString(), backupWorktreeReseedTarget(), asPositiveInt(), appendCapturedStderr() (+41 more)

### Community 10 - "wake-queue/adapters/postgres.ts"
Cohesion: 0.06
Nodes (34): issueApprovals, issueRecoveryActions, issueRelations, nativeRunFinalizations, buildReviewParticipantFacts(), CancelSuppressedRetryInput, CancelSuppressedRetryResult, classifyRetryReasonKind() (+26 more)

### Community 11 - ""tool_call_events""
Cohesion: 0.08
Nodes (41): "public"."companies", "public"."tool_applications", "public"."tool_catalog_entries", "public"."tool_connections", "tool_access_audit_events", "tool_applications", "tool_catalog_entries", "tool_connections" (+33 more)

### Community 12 - "companies.ts"
Cohesion: 0.18
Nodes (11): activityLog, agentWakeupRequests, agents, decisionBundles, decisionEffectExecutions, decisions, decisionTargetIssues, heartbeatRuns (+3 more)

### Community 13 - "company-portability.ts"
Cohesion: 0.06
Nodes (37): IssueCommentAuthorType, CompanyPortabilityAdapterOverride, CompanyPortabilityAgentSelection, CompanyPortabilityBlobManifestEntry, CompanyPortabilityCollisionStrategy, CompanyPortabilityCompanyManifestEntry, CompanyPortabilityEmbeddedAssetManifestEntry, CompanyPortabilityEnvInput (+29 more)

### Community 14 - "completeOAuthCallback"
Cohesion: 0.10
Nodes (37): connectionMethodForConnection(), managedConnectorProfile(), normalizeConnectionMethodConfig(), normalizeOAuthProviderError(), oauthProviderErrorMessage(), originOf(), projectedConnectionHeaders(), toApplication() (+29 more)

### Community 15 - "oauthConfig"
Cohesion: 0.14
Nodes (37): credentialRefConfigPath(), resolveOAuthClientIdMetadataDocumentUrl(), singleFlight(), acquireOAuthGrantRefreshLease(), acquireOAuthRefreshLease(), adoptClientIdMetadataDocument(), clearOAuthGrantRefreshLease(), clearOAuthRefreshLease() (+29 more)

### Community 16 - "authorization.ts"
Cohesion: 0.08
Nodes (35): userInboxAgentPolicies, activeActorMembership(), activeResponsibleUserCanAuthorizeAgentGrantedSkillChange(), activeResponsibleUserCanAuthorizeIssueAction(), AgentAuthorizationRow, AgentHierarchyRow, agentIsInSubtree(), AssignmentPolicyEffect (+27 more)

### Community 17 - "0255_previous_captain_america.sql"
Cohesion: 0.10
Nodes (34): "chat_actions", "chat_agent_routes", "chat_conversations", "chat_deliveries", "chat_endpoint_leases", "chat_endpoint_resources", "chat_endpoints", "chat_external_principals" (+26 more)

### Community 18 - "issues.ts"
Cohesion: 0.18
Nodes (15): companyOnboardingSeeds, costEvents, decisionTrainingExamples, executionWorkspaces, feedbackExports, feedbackVotes, financeEvents, goals (+7 more)

### Community 19 - "refreshCatalog"
Cohesion: 0.13
Nodes (34): actorBinding(), descriptorHash(), flattenKeys(), healthFailureHttpStatus(), stableHash(), toConnection(), assertComposioConnectedAccountActive(), audit() (+26 more)

### Community 20 - "runWorktreeInit"
Cohesion: 0.14
Nodes (30): branchExistsOnAnyRemote(), branchHasUniqueCommits(), detectGitBranchName(), ensureRepairTargetWorktree(), extractExecSyncErrorMessage(), installDependenciesBestEffort(), isPrimaryGitWorktree(), isWorktreeSeedMode() (+22 more)

### Community 21 - "types/access.ts"
Cohesion: 0.12
Nodes (29): AgentAdapterType, CompanyStatus, HumanCompanyMembershipRole, InstanceUserRole, InviteJoinType, InviteType, JoinRequestStatus, JoinRequestType (+21 more)

### Community 22 - "worktree-lib.ts"
Cohesion: 0.08
Nodes (28): buildWorktreeConfig(), buildWorktreeEnvEntries(), DEFAULT_WORKTREE_HOME, formatShellExports(), generateWorktreeColor(), hslComponentToHex(), hslToHex(), MINIMAL_WORKTREE_EXCLUDED_TABLES (+20 more)

### Community 23 - "services/access.ts"
Cohesion: 0.10
Nodes (25): Db, companySecretBindings, principalPermissionGrants, connectionGrantDelegations, connectionGrantMembers, toolAccessAuditEvents, userSecretDeclarations, ensureRoleDefaultGrants() (+17 more)

### Community 24 - "plugin-database.ts"
Cohesion: 0.12
Nodes (23): ApplyPluginMigrationsOptions, assertAllowedPublicRead(), assertIdentifier(), assertNoBannedSql(), derivePluginDatabaseNamespace(), extractQualifiedRefs(), normaliseSql(), PluginDatabaseClient (+15 more)

### Community 25 - "asRecord"
Cohesion: 0.12
Nodes (29): asRecord(), isOAuthEndpointRejection(), mergeManagedToolArguments(), projectConnectionMethodToolArguments(), projectedConnectionToolArguments(), sanitizeHttpFailure(), accessContextForBroker(), annotateGitHubAuthorization() (+21 more)

### Community 26 - "applyPendingMigrations"
Cohesion: 0.12
Nodes (18): cleanups, migrationHash, applyPendingMigrations(), createUtilitySql(), discoverMigrationTableSchema(), inspectMigrations(), listMigrationFiles(), migratePostgresIfEmpty() (+10 more)

### Community 27 - "plugins"
Cohesion: 0.11
Nodes (14): externalObjectMentions, externalObjects, pluginCompanySettings, pluginConfig, pluginDatabaseNamespaces, pluginMigrations, pluginEntities, pluginJobRuns (+6 more)

### Community 28 - "Database"
Cohesion: 0.07
Nodes (26): 1. Embedded PostgreSQL — zero config, 2. Local PostgreSQL (Docker), 3. Hosted PostgreSQL (Supabase), Attachment upload provenance, Backups, Client tuning (optional), Cloud runtime identity singleton, Configure (+18 more)

### Community 29 - "runWorktreeReseed"
Cohesion: 0.12
Nodes (26): collectMergePlan(), createConfiguredStorageFromPaperclipConfig(), getS3Client(), dynamicImport, formatSeededWorktreeExecutionQuarantineSummary(), normalizeS3Prefix(), openConfiguredStorage(), parseGitWorktreeList() (+18 more)

### Community 30 - "authorizationService"
Cohesion: 0.16
Nodes (26): authorizationService(), agentHasMentionGrantOnIssue(), agentWithinLowTrustBoundary(), allowIssueMentionGrant(), assignmentPolicyEffect(), commentAuthorCanGrantIssueMention(), decideLowTrustAccess(), decideTaskBridgeAccess() (+18 more)

### Community 31 - "accessService"
Cohesion: 0.13
Nodes (19): accessService(), archiveMember(), assertAssignableArchiveTarget(), assertCanRemoveActiveOwner(), canUser(), copyActiveUserMemberships(), decide(), ensureMembership() (+11 more)

### Community 32 - "document_annotation_threads.ts"
Cohesion: 0.13
Nodes (12): documentAnnotationAnchorSnapshots, documentAnnotationThreads, documentMemberships, documentRevisions, documents, routineDocuments, routines, StatusCardFingerprint (+4 more)

### Community 33 - "better-auth.ts"
Cohesion: 0.14
Nodes (21): BetterAuthGetSessionApi, BetterAuthHandlerTarget, BetterAuthInstance, BetterAuthSessionResolver, BetterAuthSessionResult, BetterAuthSessionUser, buildBetterAuthAdvancedOptions(), buildBetterAuthRateLimitOptions() (+13 more)

### Community 34 - "src/index.ts"
Cohesion: 0.13
Nodes (16): databaseCheck(), isInsideOsTmpDir(), MigrationBootstrapResult, MigrationHistoryReconcileResult, MigrationState, EMBEDDED_POSTGRES_EXIT_EVENTS, EmbeddedPostgresExitTarget, loadWithoutEmbeddedPostgresExitHooks() (+8 more)

### Community 35 - "migration-runtime.ts"
Cohesion: 0.16
Nodes (18): ensureEmbeddedPostgres(), inspectLegacyWorktreeDatabase(), readPidFilePort(), getPostgresDataDirectory(), createEmbeddedPostgresLogBuffer(), detectEmbeddedPostgresHint(), formatEmbeddedPostgresError(), summarizeRecentLogs() (+10 more)

### Community 36 - "discoverOAuthEndpoints"
Cohesion: 0.15
Nodes (21): canonicalResourceIndicator(), protectedResourceMetadataUrls(), remoteEndpoint(), sameOAuthIssuer(), allowPrivateRemoteEndpoints(), assertOAuthCallbackIssuer(), assertRemoteEndpointAllowed(), assertRemoteHttpUrlAllowed() (+13 more)

### Community 37 - "chat_channels.ts"
Cohesion: 0.14
Nodes (17): chatActions, chatAgentRoutes, chatConversations, chatDeliveries, chatEndpointLeases, chatEndpointResources, chatEndpoints, chatExternalPrincipals (+9 more)

### Community 38 - "0000_mature_masked_marvel.sql"
Cohesion: 0.22
Nodes (18): "activity_log", "agent_api_keys", "agents", "approvals", "cost_events", "goals", "heartbeat_runs", "issue_comments" (+10 more)

### Community 39 - "decideBase"
Cohesion: 0.22
Nodes (19): allow(), assignmentTargetIsInCompany(), decideBase(), decideVisibleIssueWrite(), decideWithAgentConfigReadGrant(), decideWithProtectedChangeGrants(), decideWithTaskAssignmentGrants(), denyForAssignmentPolicyIfNeeded() (+11 more)

### Community 40 - "connectGalleryApp"
Cohesion: 0.13
Nodes (19): assertClass3ToolCredentialRefAllowed(), connectionMethodFor(), connectionSetupMutationFingerprint(), connectionUid(), credentialFieldsFor(), googleSheetsAllowedSpreadsheetIds(), googleSheetsRobotEmailFromEnv(), isGoogleSheetsConnectionConfig() (+11 more)

### Community 41 - "runtime-config.ts"
Cohesion: 0.18
Nodes (14): asPositiveInt(), findConfigFileFromAncestors(), migrateLegacyConfig(), parseEnvFile(), PartialConfig, readConfig(), readEnvEntries(), resolveDatabaseTarget() (+6 more)

### Community 42 - "active-run-watchdog/adapters/postgres.ts"
Cohesion: 0.15
Nodes (12): heartbeatRunWatchdogDecisions, createPostgresWatchdogAdapter(), findCandidateSilentRuns(), findEvaluationIssueById(), findOpenStaleRunEvaluation(), findRunForCompany(), findSourceIssue(), selectEvaluationIssueSnapshot() (+4 more)

### Community 43 - "pipeline_cases.ts"
Cohesion: 0.21
Nodes (12): pipelineCaseEvents, pipelineAutomationExecutions, pipelineCaseBlockers, pipelineCaseDocuments, pipelineCaseIssueLinks, PipelineCasePendingSuggestion, pipelineCases, PipelineCaseWorkspaceRef (+4 more)

### Community 44 - "companies"
Cohesion: 0.19
Nodes (7): approvalComments, approvals, budgetIncidents, budgetPolicies, companies, invites, joinRequests

### Community 45 - "SeedWorktreeDatabase"
Cohesion: 0.13
Nodes (16): closeDb(), copySeededSecretsKey(), isCurrentSourceConfigPath(), isEnabledValue(), isRecord(), resolveWorktreeSeedPlan(), normalizeWorktreeRuntimeConfig(), openConfiguredDb() (+8 more)

### Community 46 - "cases.ts"
Cohesion: 0.17
Nodes (10): assets, caseAttachments, caseDocuments, caseEvents, caseIssueLinks, caseLabels, cases, companyLogos (+2 more)

### Community 47 - "boardAuthService"
Cohesion: 0.19
Nodes (11): boardAuthService(), cancelCliAuthChallenge(), describeCliAuthChallenge(), getCliAuthChallenge(), getCliAuthChallengeBySecret(), pruneTouchedBoardApiKeys(), resolveBoardAccess(), resolveBoardActivityCompanyIds() (+3 more)

### Community 48 - "0014_many_mikhail_rasputin.sql"
Cohesion: 0.19
Nodes (13): "account", "company_memberships", "instance_user_roles", "invites", "join_requests", "principal_permission_grants", "session", "public"."agents" (+5 more)

### Community 49 - ""public"."issues""
Cohesion: 0.14
Nodes (10): "issue_read_states", "public"."companies", "public"."issues", "issue_inbox_archives", "public"."companies", "public"."issues", "feedback_exports", "feedback_votes" (+2 more)

### Community 50 - "0029_plugin_tables.sql"
Cohesion: 0.25
Nodes (13): "plugin_company_settings", "plugin_config", "plugin_entities", "plugin_job_runs", "plugin_jobs", "plugin_logs", "plugin_state", "plugin_webhook_deliveries" (+5 more)

### Community 51 - "board-auth.ts"
Cohesion: 0.21
Nodes (13): companyMemberships, BOARD_API_KEY_TTL_MS, boardApiKeyExpiresAt(), approveCliAuthChallenge(), createCliAuthChallenge(), createNamedBoardApiKey(), findBoardApiKeyByToken(), CLI_AUTH_CHALLENGE_TTL_MS (+5 more)

### Community 52 - "company_secrets.ts"
Cohesion: 0.26
Nodes (6): companySecretProviderConfigs, companySecretVersions, companySecrets, managedAgentProfiles, secretAccessEvents, userSecretDefinitions

### Community 53 - "ensureWorktreeSeeded"
Cohesion: 0.29
Nodes (13): acquireWorktreeSeedLock(), ensureWorktreeSeeded(), formatWorktreeSeedFailureDiagnostic(), resolveWorktreeSeedMarkerPaths(), markWorktreeSeedPending(), parseWorktreeSeedLockOwner(), processIsAlive(), readLegacyWorktreeSeedPendingMarker() (+5 more)

### Community 54 - "embedded-postgres-supervisor.ts"
Cohesion: 0.19
Nodes (6): createEmbeddedPostgresSupervisor(), EmbeddedPostgresExitListener, EmbeddedPostgresSupervisor, once(), Options, SupervisedEmbeddedPostgres

### Community 55 - "adapter_auth_sessions.ts"
Cohesion: 0.23
Nodes (8): column(), columnIsNotNull(), findIndex(), indexColumns(), PgTable, ADAPTER_AUTH_SESSION_ACTIVE_STATES, adapterAuthSessions, AdapterAuthSessionState

### Community 56 - "ensurePostgresDatabase"
Cohesion: 0.18
Nodes (7): createBufferedTextFileWriter(), cleanups, createSiblingDatabase(), createTempDatabase(), chatMigrations, identityMigrations, ensurePostgresDatabase()

### Community 57 - "environment_custom_image_setup_sessions.ts"
Cohesion: 0.29
Nodes (5): environmentCustomImageSetupSessions, environmentCustomImageTemplates, environmentLeases, environments, instanceSettings

### Community 58 - ""decision_triage_events""
Cohesion: 0.35
Nodes (10): "decision_queues", "decision_triage_events", "decision_queue_items", "decision_triage", "public"."agents", "public"."companies", "public"."decision_queues", "public"."heartbeat_runs" (+2 more)

### Community 59 - ""issues""
Cohesion: 0.20
Nodes (8): "companies", "issues", "public"."projects", "public"."heartbeat_runs", "public"."heartbeat_runs", "company_skill_policies", "issue_create_idempotency_keys", "decision_training_examples"

### Community 60 - "native_run_finalizations.ts"
Cohesion: 0.38
Nodes (5): completionContracts, nativeRunResults, statusDecisionEffects, statusDecisions, workAssessments

### Community 61 - ""document_revisions""
Cohesion: 0.29
Nodes (8): "document_revisions", "documents", "issue_documents", "public"."agents", "public"."companies", "public"."issues", "document_memberships", "public"."documents"

### Community 62 - ""execution_workspaces""
Cohesion: 0.29
Nodes (9): "execution_workspaces", "issue_work_products", "public"."companies", "public"."execution_workspaces", "public"."heartbeat_runs", "public"."issues", "public"."project_workspaces", "public"."projects" (+1 more)

### Community 63 - "0113_pipeline_foundation.sql"
Cohesion: 0.20
Nodes (9): "pipeline_automation_executions", "pipeline_case_blockers", "pipeline_case_events", "pipeline_case_issue_links", "pipeline_cases", "pipeline_documents", "pipeline_stages", "pipeline_transitions" (+1 more)

### Community 64 - ""tool_mcp_gateways""
Cohesion: 0.20
Nodes (9): "public"."agents", "public"."companies", "public"."issues", "public"."projects", "public"."tool_mcp_gateways", "public"."tool_profiles", "tool_mcp_gateway_tokens", "tool_mcp_gateways" (+1 more)

### Community 65 - "check-migration-numbering.ts"
Cohesion: 0.33
Nodes (8): ensureJournalMatchesFiles(), ensureNoDuplicates(), ensureStrictlyOrdered(), JournalFile, journalPath, main(), migrationNumber(), migrationsDir

### Community 66 - ""issue_attachments""
Cohesion: 0.25
Nodes (8): "assets", "issue_attachments", "public"."agents", "public"."assets", "public"."companies", "public"."issue_comments", "public"."issues", "public"."heartbeat_runs"

### Community 67 - ""finance_events""
Cohesion: 0.22
Nodes (8): "finance_events", "public"."agents", "public"."companies", "public"."goals", "public"."heartbeat_runs", "public"."issues", "public"."projects", "public"."cost_events"

### Community 68 - ""environment_leases""
Cohesion: 0.25
Nodes (8): "environment_leases", "environments", "public"."companies", "public"."environments", "public"."execution_workspaces", "public"."heartbeat_runs", "public"."issues", "public"."environments"

### Community 69 - "0227_modern_pandemic.sql"
Cohesion: 0.25
Nodes (8): "completion_contracts", "native_run_finalizations", "native_run_results", paperclip_bump_issue_status_version(), paperclip_issue_status_version_trigger, "status_decision_effects", "status_decisions", "work_assessments"

### Community 70 - "authUsers"
Cohesion: 0.33
Nodes (6): authAccounts, authSessions, authUsers, authVerifications, boardApiKeys, cliAuthChallenges

### Community 71 - "registerOAuthClient"
Cohesion: 0.33
Nodes (9): actorForSecret(), assertOAuthDcrArray(), createOrRotateOAuthSecret(), invalidOAuthDcrResponse(), oauthSecretRef(), parseOAuthDcrString(), parseOAuthDcrTimestamp(), registerOAuthClient() (+1 more)

### Community 72 - "auth-bootstrap-ceo.ts"
Cohesion: 0.39
Nodes (6): bootstrapCeoInvite(), createInviteToken(), hashToken(), resolveBaseUrl(), resolveDbUrl(), instanceUserRoles

### Community 73 - "issue-comment-derived-attribution-migration.test.ts"
Cohesion: 0.29
Nodes (4): cleanups, createTempDatabase(), makeDerivedAttributionMigrationPending(), migrationHash()

### Community 74 - ""workspace_runtime_services""
Cohesion: 0.25
Nodes (7): "public"."agents", "public"."companies", "public"."heartbeat_runs", "public"."issues", "public"."project_workspaces", "public"."projects", "workspace_runtime_services"

### Community 75 - ""issue_plan_decompositions""
Cohesion: 0.25
Nodes (7): "issue_plan_decompositions", "public"."agents", "public"."companies", "public"."heartbeat_runs", "public"."issue_thread_interactions", "public"."issues", "public"."document_revisions"

### Community 76 - ""environment_custom_image_setup_sessions""
Cohesion: 0.39
Nodes (7): "environment_custom_image_setup_sessions", "environment_custom_image_templates", "public"."agents", "public"."companies", "public"."environments", "public"."environment_custom_image_templates", "public"."environment_leases"

### Community 77 - ""connection_grants""
Cohesion: 0.25
Nodes (6): "tool_oauth_states", "connection_grants", "public"."agents", "public"."companies", "public"."tool_connections", "public"."agents"

### Community 78 - ""chat_teams_file_transfers""
Cohesion: 0.25
Nodes (7): "chat_teams_file_transfers", "public"."chat_conversations", "public"."chat_endpoints", "public"."chat_external_principals", "public"."chat_publications", "public"."companies", "public"."issues"

### Community 79 - "run-event-payload.ts"
Cohesion: 0.36
Nodes (5): decodeRunEventPayload(), encodeRunEventPayload(), project(), projectString(), runEventPayload

### Community 80 - "queued-comment-postgres.ts"
Cohesion: 0.25
Nodes (3): QueuedCommentQueuePostgresAdapterDeps, RunRow, WakeRow

### Community 81 - "agent-permissions.ts"
Cohesion: 0.39
Nodes (7): AgentPermissionsContext, asRecord(), defaultAgentPermissions(), normalizeAgentPermissions(), NormalizedAgentPermissions, permissionsImplyLowTrust(), canCreateAgentsLegacy()

### Community 82 - "configure.ts"
Cohesion: 0.43
Nodes (5): configure(), defaultConfig(), Section, SECTION_LABELS, promptDatabase()

### Community 83 - "client.test.ts"
Cohesion: 0.29
Nodes (4): cleanups, createTempDatabase(), migrationUpdatedAtUpdateAllowlist, userVisibleUpdatedAtTables

### Community 84 - ""heartbeat_run_events""
Cohesion: 0.48
Nodes (6): "agent_runtime_state", "agent_wakeup_requests", "heartbeat_run_events", "public"."agents", "public"."companies", "public"."heartbeat_runs"

### Community 85 - ""issue_approvals""
Cohesion: 0.38
Nodes (6): "agent_config_revisions", "issue_approvals", "public"."agents", "public"."approvals", "public"."companies", "public"."issues"

### Community 86 - "0143_cases_foundation.sql"
Cohesion: 0.29
Nodes (6): "case_attachments", "case_documents", "case_events", "case_issue_links", "case_labels", "cases"

### Community 87 - ""execution_workspace_runtime_leases""
Cohesion: 0.29
Nodes (6): "execution_workspace_runtime_leases", "public"."agents", "public"."companies", "public"."execution_workspaces", "public"."heartbeat_runs", "public"."issues"

### Community 88 - ""connection_grant_delegations""
Cohesion: 0.38
Nodes (6): "connection_grant_delegations", "connection_grant_members", "phase4_ambiguous_personal_secrets", "public"."agents", "public"."companies", "public"."connection_grants"

### Community 89 - "migration-snapshot-drift.test.ts"
Cohesion: 0.33
Nodes (3): JournalEntry, migrationsDir, schemaDir

### Community 90 - ""company_secret_versions""
Cohesion: 0.40
Nodes (5): "company_secret_versions", "company_secrets", "public"."agents", "public"."companies", "public"."company_secrets"

### Community 91 - ""issue_labels""
Cohesion: 0.40
Nodes (5): "issue_labels", "labels", "public"."companies", "public"."issues", "public"."labels"

### Community 92 - ""budget_incidents""
Cohesion: 0.40
Nodes (5): "budget_incidents", "budget_policies", "public"."approvals", "public"."companies", "public"."budget_policies"

### Community 93 - ""workspace_operations""
Cohesion: 0.33
Nodes (5): "public"."companies", "public"."execution_workspaces", "public"."heartbeat_runs", "workspace_operations", "public"."companies"

### Community 94 - ""issue_execution_decisions""
Cohesion: 0.33
Nodes (5): "issue_execution_decisions", "public"."agents", "public"."companies", "public"."heartbeat_runs", "public"."issues"

### Community 95 - ""decision_retention""
Cohesion: 0.33
Nodes (5): "decision_archive_notification_outbox", "decision_retention", "public"."agents", "public"."companies", "public"."heartbeat_runs"

### Community 96 - "decision-queue-migrations.test.ts"
Cohesion: 0.50
Nodes (4): cleanups, DECISION_QUEUE_MIGRATIONS, readMigration(), reapplyDecisionQueueMigrations()

### Community 97 - ""approval_comments""
Cohesion: 0.40
Nodes (4): "approval_comments", "public"."agents", "public"."approvals", "public"."companies"

### Community 98 - ""agent_task_sessions""
Cohesion: 0.40
Nodes (4): "agent_task_sessions", "public"."agents", "public"."companies", "public"."heartbeat_runs"

### Community 99 - ""project_goals""
Cohesion: 0.40
Nodes (4): "project_goals", "public"."companies", "public"."goals", "public"."projects"

### Community 100 - ""issue_relations""
Cohesion: 0.40
Nodes (4): "issue_relations", "public"."agents", "public"."companies", "public"."issues"

### Community 101 - "0197_decisions_v1.sql"
Cohesion: 0.40
Nodes (4): "decision_bundles", "decision_effect_executions", "decision_target_issues", "decisions"

### Community 102 - ""managed_agent_profiles""
Cohesion: 0.50
Nodes (4): "managed_agent_profiles", "remote_agent_profiles", "public"."companies", "public"."company_secrets"

### Community 103 - "registerSeedInterruptHandler"
Cohesion: 0.67
Nodes (4): dispatchSeedInterruption(), dispatchSeedSigint(), dispatchSeedSigterm(), registerSeedInterruptHandler()

### Community 104 - ""project_workspaces""
Cohesion: 0.50
Nodes (3): "project_workspaces", "public"."companies", "public"."projects"

### Community 105 - ""company_logos""
Cohesion: 0.50
Nodes (3): "company_logos", "public"."assets", "public"."companies"

### Community 106 - "0039_fat_magneto.sql"
Cohesion: 0.50
Nodes (3): "routine_runs", "routine_triggers", "routines"

### Community 107 - "0056_spooky_ultragirl.sql"
Cohesion: 0.50
Nodes (3): "company_user_sidebar_preferences", "public"."companies", "user_sidebar_preferences"

### Community 108 - "0091_old_swarm.sql"
Cohesion: 0.50
Nodes (3): "document_annotation_anchor_snapshots", "document_annotation_comments", "document_annotation_threads"

### Community 109 - "0099_skills_store_foundation.sql"
Cohesion: 0.50
Nodes (3): "company_skill_comments", "company_skill_stars", "company_skill_versions"

### Community 110 - ""adapter_auth_sessions""
Cohesion: 0.50
Nodes (3): "adapter_auth_sessions", "public"."companies", "public"."environments"

### Community 111 - ""claude_setup_token_sessions""
Cohesion: 0.50
Nodes (3): "claude_setup_token_sessions", "public"."companies", "public"."environments"

### Community 112 - "0272_light_kate_bishop.sql"
Cohesion: 0.50
Nodes (3): "email_endpoints", "email_messages", "email_sends"

### Community 113 - "0277_uneven_lady_deathstrike.sql"
Cohesion: 0.67
Nodes (3): ai_connection_defaults_sync_provider, "ai_provider_defaults", sync_ai_provider_default()

## Knowledge Gaps
- **767 isolated node(s):** `Section`, `SECTION_LABELS`, `DbBackupOptions`, `WORKTREE_SEED_MODES`, `WORKTREE_SEED_MANIFEST` (+762 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **48 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `toolAccessService()` connect `toolAccessService` to `tool-access.ts`, `tool-access-policy.ts`, `discoverOAuthEndpoints`, `registerOAuthClient`, `connectGalleryApp`, `completeOAuthCallback`, `oauthConfig`, `refreshCatalog`, `asRecord`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Why does `agents` connect `companies.ts` to `document_annotation_threads.ts`, `schema/index.ts`, `tool-access.ts`, `chat_channels.ts`, `tool-access-policy.ts`, `worktree.ts`, `active-run-watchdog/adapters/postgres.ts`, `pipeline_cases.ts`, `companies`, `wake-queue/adapters/postgres.ts`, `cases.ts`, `queued-comment-postgres.ts`, `authorization.ts`, `issues.ts`, `company_secrets.ts`, `services/access.ts`, `environment_custom_image_setup_sessions.ts`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Why does `companies` connect `companies` to `document_annotation_threads.ts`, `schema/index.ts`, `tool-access.ts`, `chat_channels.ts`, `authUsers`, `worktree.ts`, `pipeline_cases.ts`, `companies.ts`, `cases.ts`, `issues.ts`, `board-auth.ts`, `company_secrets.ts`, `adapter_auth_sessions.ts`, `plugins`, `native_run_finalizations.ts`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `toolAccessService()` (e.g. with `toCatalogEntry()` and `checkConnectionHealth()`) actually correct?**
  _`toolAccessService()` has 29 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Section`, `SECTION_LABELS`, `DbBackupOptions` to the rest of the system?**
  _767 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `constants.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.005194805194805195 - nodes in this community are weakly interconnected._
- **Should `schema/index.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.03404255319148936 - nodes in this community are weakly interconnected._