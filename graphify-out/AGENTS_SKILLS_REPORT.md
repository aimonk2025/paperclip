# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 150 files · ~184,653 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2304 nodes · 3905 edges · 158 communities (138 shown, 20 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 118 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- validators/company-skill.ts
- skills-catalog/src/catalog-builder.ts
- types/company-skill.ts
- services/company-skills.ts
- services/agents.ts
- services/teams-catalog.ts
- companySkillService
- agentRoutes
- Inputs
- validators/agent.ts
- services/built-in-agents.ts
- types/agent.ts
- agent-instructions.ts
- chat-teams-file-consent.ts
- skill-policy.ts
- pluginManagedAgentService
- Agent Instruction Templates
- teams-catalog/src/catalog-builder.ts
- asString
- installFromCatalog
- company_skills.ts
- ensureSkillInventoryCurrent
- isPlainRecord
- resolveManagedSkillsRoot
- Paperclip Skill
- process
- plugin-managed-skills.ts
- skills-catalog.ts
- Paperclip Board Skill
- types/teams-catalog.ts
- teams-catalog/src/index.ts
- buildCatalogTeam
- builtInAgentService
- chat-teams-file-transfers.ts
- chat-teams-personal-recipient.ts
- agent-eligibility.ts
- validators/teams-catalog.ts
- services/managed-agent-profiles.ts
- Procedure
- routes/agents.ts
- services/remote-agent-profiles.ts
- agentmail-api.ts
- digest
- runtime-skill-cache.ts
- services/company-skill-policy.ts
- agent-conversations.ts
- ensure
- findSingleAgent
- Release Announcement
- Paperclip Routines
- companySkillRoutes
- Paperclip API Reference
- Company Skills Workflow
- visit
- agent-invokability.ts
- chat-teams-inline-image-intake.ts
- Wireframe
- Workflow
- Grid, palette, and type scale
- Section outline
- Draft-Review Checklist
- PARA Memory Files
- asRecord
- Cases
- validators/adapter-skills.ts
- teams-catalog/src/frontmatter.ts
- bindTeamsFileConsent
- chat-teams-inline-images.ts
- Hero Capsule Bank
- GitHub Pull Request Workflow
- Agent Browser
- Prepare MCP Integration
- routes/built-in-agents.ts
- agent-assignability.ts
- Identicon Prototyper
- Paperclip Capsules
- QA Acceptance
- Response Schemas
- Full API Reference
- types/adapter-skills.ts
- materializeDefaultInstructionsBundleForNewAgent
- chat-teams-file-publication.ts
- Doc Maintenance
- Issue Triage
- Task Planning
- Generator Workflows
- Governance and Approvals
- asNonEmptyString
- agent-action-audit.ts
- getCatalogManifest
- Status card query
- Individual and Status Capsules
- Ramp
- Product Design Critique
- Teams Catalog Migration Notes
- routes/company-skills.ts
- agent-task-run-telemetry.ts
- TeamsFileTransferOptions
- Summarize status
- Worked examples
- Paperclip Workflow Playbooks
- validateManagedAgentBinding
- inboxAgentPolicyRoutes
- Paperclip — Converting Plans to Tasks
- Paperclip Create Agent API Reference
- Issue Workspace Runtime Controls
- buildAgentDetail
- companySkillPolicyRoutes
- agentmail.ts
- Example: Research and Gate a Notion MCP Connection
- ceo/AGENTS.md
- ux-designer/AGENTS.md
- Product Design
- Product Engineering
- The Heartbeat Procedure
- agent-url-key.ts
- types/inbox-agent-policy.ts
- validators/inbox-agent-policy.ts
- assertSetupTokenLoginProviderCapability
- agent-start-lock.ts
- ensureBuiltInAgentDefaultGrants
- chat-teams-credentials.ts
- inboxAgentPolicyService
- Simplified English
- core-exec-team/agents/cto/AGENTS.md
- core-exec-team/agents/qa/AGENTS.md
- Core Exec Team
- product-engineering/agents/cto/AGENTS.md
- product-engineering/agents/qa/AGENTS.md
- senior-coder/AGENTS.md
- Worked Example: IC Heartbeat
- Content Machine
- AgentMail
- Project Setup (Create + Workspace)
- Generated Artifacts and Work Products
- chat_teams_file_transfers.ts
- company_skill_policies.ts
- managed_agent_profiles.ts
- remote_agent_profiles.ts
- user_inbox_agent_policies.ts
- CompanySkill
- CompanySkillFileInventoryEntry
- CompanySkillForkSummary
- CompanySkillTestRun
- requireBuiltInAgent
- findMarkedRows
- Content Calendar

## God Nodes (most connected - your core abstractions)
1. `companySkillService()` - 110 edges
2. `agentRoutes()` - 103 edges
3. `builtInAgentService()` - 50 edges
4. `asString()` - 39 edges
5. `agentService()` - 37 edges
6. `isPlainRecord()` - 31 edges
7. `getById()` - 28 edges
8. `ensureSkillInventoryCurrent()` - 24 edges
9. `Paperclip Skill` - 24 edges
10. `reconcileLocalPathSkillSources()` - 21 edges
11. `installUpdate()` - 21 edges
12. `installFromCatalog()` - 21 edges
13. `process()` - 20 edges
14. `upsertImportedSkills()` - 20 edges
15. `buildCatalogTeam()` - 19 edges

## Surprising Connections (you probably didn't know these)
- `assertExternalInstructionsAdmin()` --calls--> `agentInstructionsBundleMode()`  [EXTRACTED]
  server/src/routes/agents.ts → server/src/services/agent-instructions.ts
- `readPackageJson()` --calls--> `asString()`  [EXTRACTED]
  packages/teams-catalog/src/catalog-builder.ts → packages/teams-catalog/src/frontmatter.ts
- `buildCatalogTeam()` --calls--> `asBoolean()`  [EXTRACTED]
  packages/teams-catalog/src/catalog-builder.ts → packages/teams-catalog/src/frontmatter.ts
- `buildCatalogTeam()` --calls--> `parseFrontmatterMarkdown()`  [EXTRACTED]
  packages/teams-catalog/src/catalog-builder.ts → packages/teams-catalog/src/frontmatter.ts
- `visit()` --calls--> `parseFrontmatterMarkdown()`  [EXTRACTED]
  packages/teams-catalog/src/catalog-builder.ts → packages/teams-catalog/src/frontmatter.ts

## Import Cycles
- None detected.

## Communities (158 total, 20 thin omitted)

### Community 0 - "validators/company-skill.ts"
Cohesion: 0.02
Nodes (92): catalogSkillFileDetailSchema, catalogSkillFileSchema, catalogSkillGitHubSourceSchema, catalogSkillKindSchema, CatalogSkillListQuery, catalogSkillListQuerySchema, catalogSkillSchema, catalogSkillSourceSchema (+84 more)

### Community 1 - "skills-catalog/src/catalog-builder.ts"
Cohesion: 0.06
Nodes (68): packageDir, packageDir, BaseSkillCandidate, buildCatalogManifest(), BuildCatalogManifestOptions, BuildCatalogManifestResult, buildCatalogSkill(), buildCatalogSkillSource() (+60 more)

### Community 2 - "types/company-skill.ts"
Cohesion: 0.03
Nodes (72): CatalogSkill, CatalogSkillFile, CatalogSkillFileDetail, CatalogSkillFileKind, CatalogSkillGitHubSource, CatalogSkillKind, CatalogSkillListQuery, CatalogSkillSource (+64 more)

### Community 3 - "services/company-skills.ts"
Cohesion: 0.04
Nodes (69): ALLOWED_SKILL_TEST_TEMPLATE_PLACEHOLDERS, assertNoSymlinksInLocalTree(), assertVersionMatchesSkill(), BUILT_IN_SKILL_TEST_RUN_TEMPLATE_BODY, BUILT_IN_SKILL_TEST_RUN_TEMPLATE_DATE, BundledSkillReleaseManifestEntry, categoryLookupKey(), CompanySkillCommentRow (+61 more)

### Community 4 - "services/agents.ts"
Cohesion: 0.06
Nodes (63): AgentPermissionsContext, asRecord(), defaultAgentPermissions(), normalizeAgentPermissions(), NormalizedAgentPermissions, permissionsImplyLowTrust(), AgentSecretBindingSyncService, asRecord() (+55 more)

### Community 5 - "services/teams-catalog.ts"
Cohesion: 0.06
Nodes (63): teamsCatalogRoutes(), assertCanInstallCatalogTeam(), canCreateAgents(), buildPortabilityInput(), CatalogManifestFile, catalogManifestPath, catalogPackageRootCandidates, catalogProvenance() (+55 more)

### Community 6 - "companySkillService"
Cohesion: 0.07
Nodes (58): buildHarnessIssueDescription(), builtInSkillTestRunTemplate(), companySkillService(), actorStarClause(), assertCanMutateComment(), cancelTestRun(), categoryCounts(), completeTestRunForIssue() (+50 more)

### Community 7 - "agentRoutes"
Cohesion: 0.05
Nodes (27): agentRoutes(), allowedEnvironmentDriversForAgent(), assertAdapterConfigConstraints(), assertAgentEnvironmentSelection(), assertAgentReadAllowed(), assertBoardCanManageAgentsForCompany(), assertCanApplyAgentProfileChange(), assertCanApplyProtectedAgentChange() (+19 more)

### Community 8 - "Inputs"
Cohesion: 0.04
Nodes (46): Annotation layer, Arrow connector (between two screens), Avatar (circular, with cross), Breadcrumb, Button (filled), Button (icon-only square), Button (outlined / secondary), Card (+38 more)

### Community 9 - "validators/agent.ts"
Cohesion: 0.05
Nodes (41): adapterConfigSchema, agentApiKeyScopeSchema, agentInstructionsBundleModeSchema, AgentMineInboxQuery, agentMineInboxQuerySchema, agentPermissionsSchema, agentRuntimeConfigSchema, BuiltInAgentEmptyMutation (+33 more)

### Community 10 - "services/built-in-agents.ts"
Cohesion: 0.05
Nodes (40): AUTO_PROVISION_ON_COMPANY_CREATE_KEYS, BUILT_IN_AGENT_DEFAULT_GRANTS, BUILT_INS_DIR, BuiltInAgentBundleDefinition, BuiltInAgentDefinition, BuiltInAgentProvisionActor, BuiltInAgentProvisionInput, BuiltInAgentProvisionResult (+32 more)

### Community 11 - "types/agent.ts"
Cohesion: 0.05
Nodes (41): AgentOrgChainHealth, ADAPTER_AUTH_PANEL_MODES, ADAPTER_AUTH_SESSION_INTERNAL_STATUSES, ADAPTER_AUTH_SESSION_STATUSES, AdapterAuthPanelMode, AdapterAuthSessionFailure, AdapterAuthSessionInternalStatus, AdapterAuthSessionOwnerResponse (+33 more)

### Community 12 - "agent-instructions.ts"
Cohesion: 0.16
Nodes (40): AgentInstructionsBundle, agentInstructionsBundleMode(), AgentInstructionsFileDetail, AgentInstructionsFileSummary, agentInstructionsService(), deleteFile(), ensureWritableBundle(), exportFiles() (+32 more)

### Community 13 - "chat-teams-file-consent.ts"
Cohesion: 0.07
Nodes (26): activitySchema, bindingSchema, buildTeamsFileConsentCard(), contextSchema, filename, INSTALLED_HOOK, installTeamsFileConsentHook(), opaqueId (+18 more)

### Community 14 - "skill-policy.ts"
Cohesion: 0.07
Nodes (27): EffectiveSkillPolicy, EvaluateSkillPolicy, evaluateSkillPolicySchema, nonEmptyUniqueStrings, ReplaceSkillPolicy, replaceSkillPolicySchema, SKILL_POLICY_ACTIONS, SKILL_POLICY_SOURCE_TYPES (+19 more)

### Community 15 - "pluginManagedAgentService"
Cohesion: 0.18
Nodes (29): adapterPreference(), applyInstructionTemplateVariables(), bindingExternalId(), declarationPatch(), declaredInstructionFiles(), fallbackAdapterType(), managedAgentPauseReason(), managedMetadata() (+21 more)

### Community 16 - "Agent Instruction Templates"
Cohesion: 0.07
Nodes (25): Agent Instruction Templates, Decision flow, Example 1 — lens-heavy adjacent template: "Backend Performance Engineer", Example 2 — focused lens subset for a narrow role: "Dependency Auditor", Example 3 — no lenses needed: "Release Coordinator", Example 4 — UX-adjacent template with trimmed lenses: "Content Designer", How to apply an adjacent template, How to apply an exact template (+17 more)

### Community 17 - "teams-catalog/src/catalog-builder.ts"
Cohesion: 0.11
Nodes (26): packageDir, packageDir, buildCatalogManifest(), BuildCatalogManifestOptions, buildExpectedCatalogManifest(), CATALOG_KINDS, CatalogSkillSummary, collectCandidateUniquenessErrors() (+18 more)

### Community 18 - "asString"
Cohesion: 0.17
Nodes (29): assertImportedSkillKeyAllowed(), assertImportedSkillSourceAllowed(), asString(), classifyInventoryKind(), collectLocalSkillInventory(), cleanupFailedFork(), ensureBundledSkills(), forkSkill() (+21 more)

### Community 19 - "installFromCatalog"
Cohesion: 0.13
Nodes (29): auditInstalledSkillBytes(), collectSkillFileBytes(), visit(), assertCatalogSkillInstallable(), auditCatalogSkillSnapshot(), auditSkill(), buildCatalogSkillMetadata(), copySkillDirectory() (+21 more)

### Community 20 - "company_skills.ts"
Cohesion: 0.11
Nodes (16): agentApiKeys, agentConfigRevisions, agentMemberships, agentRuntimeState, agentSessionGoalActions, agentTaskSessions, agentWakeupRequests, agents (+8 more)

### Community 21 - "ensureSkillInventoryCurrent"
Cohesion: 0.14
Nodes (24): buildInventoryContentHash(), collectVersionFileInventory(), collectVersionFileInventoryFromDirectory(), createVersion(), deleteFile(), ensureBundledSkillReleases(), ensureRunSkillVersion(), ensureSkillInventoryCurrent() (+16 more)

### Community 22 - "isPlainRecord"
Cohesion: 0.14
Nodes (24): buildMissingLocalSourceMarker(), buildMissingRuntimeSourceDetail(), bundledFolderLabel(), reconcileLocalPathSkillSources(), reconcilePaperclipSkillFolders(), findMissingLocalSkillIds(), getMissingSourceMarker(), importedSkillMetadataEqual() (+16 more)

### Community 23 - "resolveManagedSkillsRoot"
Cohesion: 0.15
Nodes (23): buildSkillRuntimeName(), applySkillReassignments(), assertLocalImportSourceAllowed(), deleteSkill(), listMaterializedFiles(), listReferenceTargets(), listRuntimeSkillEntries(), materializeCatalogManifestSkillFiles() (+15 more)

### Community 24 - "Paperclip Skill"
Cohesion: 0.08
Nodes (24): Authentication, Cases, Comment Style (Required), Company Skills Workflow, Conversation tasks, Critical Rules, Full Reference, Issue Dependencies (Blockers) (+16 more)

### Community 25 - "process"
Cohesion: 0.34
Nodes (23): authority(), authorityHash(), context(), fail(), summary(), teamsFileTransferService(), applyResponse(), bounded() (+15 more)

### Community 26 - "plugin-managed-skills.ts"
Cohesion: 0.21
Nodes (22): buildDeclaredSkillFiles(), buildDefaultMarkdown(), buildPackageFiles(), buildSkillDefaults(), canonicalSkillKey(), pluginKeySlug(), pluginManagedSkillService(), declarationFor() (+14 more)

### Community 27 - "skills-catalog.ts"
Cohesion: 0.14
Nodes (21): CatalogManifestFile, CatalogManifestUnavailableError, copyCatalogSkillFile(), devCatalogManifestPath, devCatalogPackageRoot, fetchCatalogSourceFile(), getCatalogSkillOrThrow(), inferLanguageFromPath() (+13 more)

### Community 28 - "Paperclip Board Skill"
Cohesion: 0.09
Nodes (22): Agent Hiring, Agent Monitoring, Agent System Prompt Template, Approvals, Authentication & Environment, Cost Monitoring, Cross-Agent Escalation Path Updates, Decision Log (+14 more)

### Community 29 - "types/teams-catalog.ts"
Cohesion: 0.10
Nodes (21): CatalogManifest, CatalogTeam, CatalogTeamCompatibility, CatalogTeamEnvInputSummary, CatalogTeamFile, CatalogTeamFileDetail, CatalogTeamFileKind, CatalogTeamImportOptions (+13 more)

### Community 30 - "teams-catalog/src/index.ts"
Cohesion: 0.14
Nodes (18): BuildCatalogManifestResult, TeamCandidate, catalogManifest, catalogTeams, teamsById, teamsByKey, CatalogManifest, CatalogTeam (+10 more)

### Community 31 - "buildCatalogTeam"
Cohesion: 0.16
Nodes (22): buildCatalogTeam(), collectEnvInputs(), collectRequiredSkills(), upsert(), collectSlugs(), collectSourceRefs(), isExternalRef(), isSkillRequirementType() (+14 more)

### Community 32 - "builtInAgentService"
Cohesion: 0.24
Nodes (22): builtInAgentService(), bundleResourceStates(), createOrResetRoutine(), currentInstructionFiles(), getCurrentSkillFiles(), getManagedResourceBinding(), getRoutineByBinding(), importBundledSkill() (+14 more)

### Community 33 - "chat-teams-file-transfers.ts"
Cohesion: 0.09
Nodes (21): createTeamsFileConsentBinding(), TeamsFileConsentBinding, TeamsFileConsentEvent, TeamsFilePrivateContext, TeamsFileUploadCapability, authoritySchema, closed, expiryRecoveryCursors (+13 more)

### Community 34 - "chat-teams-personal-recipient.ts"
Cohesion: 0.12
Nodes (20): activitySchema, admissionSchema, bindingFields, bindingSchema, bindingScopeSchema, bindTeamsPersonalRecipient(), canonicalEventId(), conversationFromThread() (+12 more)

### Community 35 - "agent-eligibility.ts"
Cohesion: 0.15
Nodes (19): AgentEligibilityAgent, AgentEligibilityLifecycleReason, AgentInvalidOrgChainAncestor, AgentOrgChainEntry, AgentOrgChainInvalidReason, AgentWorkEligibility, ASSIGNABLE_AGENT_STATUSES, buildRepairGuidance() (+11 more)

### Community 36 - "validators/teams-catalog.ts"
Cohesion: 0.10
Nodes (19): catalogTeamCompatibilitySchema, catalogTeamEnvInputSummarySchema, catalogTeamFileDetailSchema, catalogTeamFileKindSchema, catalogTeamFileSchema, CatalogTeamInstall, catalogTeamInstallSchema, catalogTeamKindSchema (+11 more)

### Community 37 - "services/managed-agent-profiles.ts"
Cohesion: 0.20
Nodes (16): managedAgentProfileRoutes(), profileInput(), assertQualifiedRevisionUnchanged(), CLAUDE_MANAGED_BETA_VERSION, computeManagedAgentProfileRevision(), ManagedAgentProfileInput, ManagedAgentProfileRevisionInput, managedAgentProfileService() (+8 more)

### Community 38 - "Procedure"
Cohesion: 0.11
Nodes (18): 10) Apply only after acceptance, in a follow-up run, 1) Confirm target and scope, 2) Pull the recent record, 3) Read the target's current guardrails, 4) Cluster the failures, 5) Route each cluster to a target surface, 6) Draft the proposal document, 7) Write the actual drafts (files, not just prose) (+10 more)

### Community 39 - "routes/agents.ts"
Cohesion: 0.13
Nodes (14): AGENT_SKILL_ASSIGNMENT_MODES, buildRuntimeSkillConfig(), resolveAgentSelfTrustPreset(), resolveDesiredSkillAssignment(), shouldMaterializeRuntimeSkillsForAdapter(), hireRunLocks, mergeDesiredSkillEntries(), readLiveRunsQueryInt() (+6 more)

### Community 40 - "services/remote-agent-profiles.ts"
Cohesion: 0.22
Nodes (15): profileInput(), remoteAgentProfileRoutes(), remoteAgentService(), AGENTCORE_CONFIGURATION_KEYS, assertQualifiedRevisionUnchanged(), computeRemoteAgentProfileRevision(), RemoteAgentProfileInput, remoteAgentProfileService() (+7 more)

### Community 41 - "agentmail-api.ts"
Cohesion: 0.12
Nodes (8): AGENTMAIL_EVENTS, agentmailApi(), AgentmailApiError, AgentmailInbox, AgentmailMessage, agentmailMessageSchema, AgentmailScope, strings

### Community 42 - "digest"
Cohesion: 0.19
Nodes (10): abortable(), classifyTeamsUploadResponse(), digest(), exchangeTeamsFileUpload(), openPrivate(), restoreTeamsFileConsentBinding(), restoreTeamsFileConsentEvent(), restoreTeamsFileUpload() (+2 more)

### Community 43 - "runtime-skill-cache.ts"
Cohesion: 0.26
Nodes (16): assertDirectories(), CacheSpec, digest(), filePath(), FileRecord, inFlight, inventory(), matches() (+8 more)

### Community 44 - "services/company-skill-policy.ts"
Cohesion: 0.20
Nodes (11): companySkillPolicyService(), evaluate(), get(), hasLegacyBroadMutationGrant(), decision(), effectivePolicyFromRow(), normalizeRole(), OPEN_DEFAULT_POLICY (+3 more)

### Community 45 - "agent-conversations.ts"
Cohesion: 0.23
Nodes (13): AGENT_CHAT_DIRECTIVE, ConversationIdentity, conversationReplay(), deliverConversationComments(), isConversation(), isConversationExecutionWake(), isConversationReset(), isSupersededConversationRun() (+5 more)

### Community 46 - "ensure"
Cohesion: 0.22
Nodes (16): assertAdapterAllowed(), assertKnownBuiltInAgentModel(), defaultProvisionInput(), ensure(), findSingleRootManager(), provision(), builtInMetadata(), defaultAdapterType() (+8 more)

### Community 47 - "findSingleAgent"
Cohesion: 0.25
Nodes (16): autoProvisionBundledAgents(), ensureBuiltInAgentAssignable(), ensureCompany(), findSingleAgent(), get(), list(), reconcileDefinitionDefaults(), requireBundleRoutine() (+8 more)

### Community 48 - "Release Announcement"
Cohesion: 0.12
Nodes (15): Avoid, Changelog entry (terse), Channel templates, Determine the audience and channel first, Dev blog post (300–800 words), In-app note, Paperclip Cases output, Post-publish checklist (+7 more)

### Community 49 - "Paperclip Routines"
Cohesion: 0.12
Nodes (15): Activity-Gated Scheduled Runs, Adding Triggers, API (manual only), Catch-Up Policies, Concurrency Policies, Creating a Routine, Example: skip quiet nights, Lifecycle (+7 more)

### Community 50 - "companySkillRoutes"
Cohesion: 0.19
Nodes (11): companySkillRoutes(), assertCanMutateCompanySkills(), asString(), deriveTrackedSkillRef(), firstQueryString(), optionalQueryBoolean(), skillImportPolicyResource(), skillPolicyPrincipal() (+3 more)

### Community 51 - "Paperclip API Reference"
Cohesion: 0.13
Nodes (13): Comments and @-mentions, Common Mistakes, Company Branding (CEO / Board), Company Context, Cross-Team Work and Delegation, Error Handling, Escalation, Issue Lifecycle (+5 more)

### Community 52 - "Company Skills Workflow"
Cohesion: 0.13
Nodes (14): App-shipped catalog, Assign Skills To An Existing Agent, Company Skills Workflow, Core Endpoints, Example: GitHub import, Example: skills.sh import (preferred), External source import, Include Skills During Hire Or Create (+6 more)

### Community 53 - "visit"
Cohesion: 0.24
Nodes (14): buildContentHash(), classifyCatalogFile(), collectMisplacedTeamFiles(), visit(), collectTeamFiles(), visit(), discoverTeamCandidates(), graphBucketForFile() (+6 more)

### Community 54 - "agent-invokability.ts"
Cohesion: 0.20
Nodes (12): AgentInvokability, AgentInvokabilityBlockReason, AgentOrgRow, AgentStatus, blocked(), DIRECT_NON_INVOKABLE_STATUSES, evaluateAgentInvokability(), evaluateAgentInvokabilityFromDb() (+4 more)

### Community 55 - "chat-teams-inline-image-intake.ts"
Cohesion: 0.22
Nodes (12): canonicalThread(), deriveTeamsInlineImageLocator(), locatorSchema, mime, officialHost(), opaque, parseTeamsInlineImageLocator(), record() (+4 more)

### Community 56 - "Wireframe"
Cohesion: 0.14
Nodes (13): Bundled assets, Grid, palette, and type scale, House style — non-negotiable, If the user asks to deploy / publish / host the wireframes, If the user requests a website / viewer page, Output convention, Primitive library, Quick start — minimal SVG (+5 more)

### Community 57 - "Workflow"
Cohesion: 0.14
Nodes (13): 1. Confirm identity and company context, 2. Discover adapter configuration for this Paperclip instance, 3. Compare existing agent configurations, 4. Choose the instruction source (required), 5. Discover allowed agent icons, 6. Draft the new hire config, 7. Review the draft against the quality checklist, 8. Submit hire request (+5 more)

### Community 58 - "Grid, palette, and type scale"
Cohesion: 0.15
Nodes (12): Canvas presets, Coordinate conventions, Desktop 12-column grid, Grid, Grid, palette, and type scale, Link convention, Mobile single column, Negative space (+4 more)

### Community 59 - "Section outline"
Cohesion: 0.15
Nodes (12): 1. Identity and reporting line, 2. Role charter, 3. Operating workflow, 4. Domain lenses, 5. Output / review bar, 6. Collaboration and handoffs, 7. Safety and permissions, 8. Done criteria (+4 more)

### Community 60 - "Draft-Review Checklist"
Cohesion: 0.15
Nodes (12): A. Identity and framing, B. Role clarity, C. Operating workflow, D. Domain lenses and judgment, Draft-Review Checklist, E. Output / review bar, F. Collaboration routing, Failure modes to watch for (+4 more)

### Community 61 - "PARA Memory Files"
Cohesion: 0.15
Nodes (11): Atomic Fact Schema (items.yaml), Memory Decay, Schemas and Memory Decay, Layer 1: Knowledge Graph (`$AGENT_HOME/life/` -- PARA), Layer 2: Daily Notes (`$AGENT_HOME/memory/YYYY-MM-DD.md`), Layer 3: Tacit Knowledge (`$AGENT_HOME/MEMORY.md`), Memory Recall -- Use qmd, PARA Memory Files (+3 more)

### Community 62 - "asRecord"
Cohesion: 0.23
Nodes (12): applyCodexLocalKeyIsolation(), asEnvBindingString(), asRecord(), assertProviderTraceSettingTransition(), codexLocalAgentHome(), codexLocalEnvKeyConfigured(), normalizeNewAgentRuntimeConfig(), parseBooleanLike() (+4 more)

### Community 63 - "Cases"
Cohesion: 0.17
Nodes (11): Attachments, Cases, Child Cases, Core Model, Documents, Fields, Issue Links, Lifecycle (+3 more)

### Community 64 - "validators/adapter-skills.ts"
Cohesion: 0.18
Nodes (10): agentDesiredSkillEntrySchema, agentDesiredSkillSelectionSchema, agentSkillAssignmentModeSchema, agentSkillEntrySchema, agentSkillOriginSchema, agentSkillSnapshotSchema, agentSkillStateSchema, AgentSkillSync (+2 more)

### Community 65 - "teams-catalog/src/frontmatter.ts"
Cohesion: 0.27
Nodes (10): readEnvInputs(), readTeamPackageGraph(), asBoolean(), isPlainRecord(), MarkdownDoc, parseFrontmatterMarkdown(), parseYamlBlock(), parseYamlFrontmatter() (+2 more)

### Community 66 - "bindTeamsFileConsent"
Cohesion: 0.24
Nodes (6): bindEarlyTeamsFileConsent(), bindTeamsFileConsent(), ConsentEvent, consentEventMatches(), sealTeamsFileConsentEvent(), sealTeamsFileUpload()

### Community 67 - "chat-teams-inline-images.ts"
Cohesion: 0.31
Nodes (10): dimensions(), gif(), isTeamsInlineImageContentType(), jpeg(), png(), PNG_SIGNATURE, prepareTeamsInlineImage(), TEAMS_INLINE_IMAGE_MAX_BYTES (+2 more)

### Community 68 - "Hero Capsule Bank"
Cohesion: 0.18
Nodes (10): Capsule Shape, Coordinate System, Gradient Palette, Grain Overlay, Hero Capsule Bank, Layout, Optional Wave Motion, Per-Column Gradient Sequences (+2 more)

### Community 69 - "GitHub Pull Request Workflow"
Cohesion: 0.18
Nodes (10): Anti-patterns, Branch hygiene before opening, GitHub Pull Request Workflow, Merge checklist, PR body, PR title, Replying to review comments, Verification evidence (+2 more)

### Community 70 - "Agent Browser"
Cohesion: 0.18
Nodes (10): Agent Browser, Anti-patterns, Before launching the browser, Common failure modes, Driving the browser, Login-gated pages, Performance and politeness, What evidence to record (+2 more)

### Community 71 - "Prepare MCP Integration"
Cohesion: 0.18
Nodes (10): Default Connection Experience, Feed New Rules Upstream, Finish, Gate Research Before Building, Keep The Run Resumable, Phase A: Research In paperclip-content, Phase B: Implement In Paperclip App, Preflight (+2 more)

### Community 72 - "routes/built-in-agents.ts"
Cohesion: 0.24
Nodes (5): builtInAgentRoutes(), formatScheduleLabel(), redactBuiltInAgentListState(), WEEKDAY_LABELS, BuiltInAgentState

### Community 73 - "agent-assignability.ts"
Cohesion: 0.31
Nodes (9): AgentAssignmentConflictReason, AgentAssignmentKind, assertAssignableAgent(), AssignabilityAgent, assignmentMessage(), assignmentReasonFromHealth(), conflictDetails(), getAgent() (+1 more)

### Community 74 - "Identicon Prototyper"
Cohesion: 0.20
Nodes (9): Color Systems, Density And Dither Behavior, Determinism Contract, Export And Share, Identicon Prototyper, Recommended Combinations, Smoke Checks, Themes, Motion, And Randomization (+1 more)

### Community 75 - "Paperclip Capsules"
Cohesion: 0.20
Nodes (9): Choose the Right Capsule Surface, Implementation Workflow, Non-Negotiable Rules, Output Expectations, Paperclip Capsules, References, Validation Checklist, When Not to Use (+1 more)

### Community 76 - "QA Acceptance"
Cohesion: 0.20
Nodes (9): Acceptance criteria format, Anti-patterns, Evidence, Handoff back to the author, QA Acceptance, Quarantine and follow-up, What every plan must cover, When not to use (+1 more)

### Community 77 - "Response Schemas"
Cohesion: 0.20
Nodes (10): Agent Record (`GET /api/agents/me` or `GET /api/agents/:agentId`), Blocker Diagnostics (`GET /api/issues/:issueId/diagnostics/blockers`), Company Portability, Cross-Agent Review Gates, Execution Policy Fields On An Issue, Issue Update Response (`PATCH /api/issues/:issueId`), Issue with Ancestors (`GET /api/issues/:issueId`), Response Schemas (+2 more)

### Community 78 - "Full API Reference"
Cohesion: 0.20
Nodes (10): Agent secret access, Agent secret proposals, Agents, Approvals, Costs, Activity, Dashboard, Companies, Projects, Goals, Full API Reference, Issues (Tasks), Re-bind an existing secret under a new path (no secret ID) (+2 more)

### Community 79 - "types/adapter-skills.ts"
Cohesion: 0.22
Nodes (8): AgentDesiredSkillEntry, AgentSkillAssignmentMode, AgentSkillEntry, AgentSkillOrigin, AgentSkillSnapshot, AgentSkillState, AgentSkillSyncMode, AgentSkillSyncRequest

### Community 80 - "materializeDefaultInstructionsBundleForNewAgent"
Cohesion: 0.28
Nodes (8): adapterSupportsInstructionsBundle(), assertNoNewAgentLegacyPromptTemplate(), materializeDefaultInstructionsBundleForNewAgent(), DEFAULT_AGENT_BUNDLE_FILES, DefaultAgentBundleRole, loadDefaultAgentInstructionsBundle(), resolveDefaultAgentBundleUrl(), resolveDefaultAgentInstructionsBundleRole()

### Community 81 - "chat-teams-file-publication.ts"
Cohesion: 0.25
Nodes (8): effectStage, fail(), opaque, projectTeamsFilePublication(), reasons, summarySchema, Tx, TeamsFileTransferSummary

### Community 82 - "Doc Maintenance"
Cohesion: 0.22
Nodes (8): Anti-patterns, Doc Maintenance, Drift detection, Release-note rules, Style baseline, The pass, When not to use, When to use

### Community 83 - "Issue Triage"
Cohesion: 0.22
Nodes (8): Don't-do list, Inputs, Issue Triage, Output of a triage pass, Per-issue triage decision, Stuck-state heuristics, When not to use, When to use

### Community 84 - "Task Planning"
Cohesion: 0.22
Nodes (8): Anti-patterns, Filing the plan, Outputs, Plan structure, Rules of thumb for splitting, Task Planning, When not to use, When to use

### Community 85 - "Generator Workflows"
Cohesion: 0.22
Nodes (8): Artifact Record Template, Choose a Workflow, Deterministic Identicon / Profile Pill, Generator Workflows, Mirrored Graphic Generator Contract, Review Checklist, Source Precedence, Website Embedded Generator

### Community 86 - "Governance and Approvals"
Cohesion: 0.22
Nodes (9): Approval follow-up (requesting agent), CEO strategy approval, Checkbox confirmations, Checking approval status, Governance and Approvals, Issue-thread confirmations, Item verdict requests, Questions and waiting for human input (+1 more)

### Community 87 - "asNonEmptyString"
Cohesion: 0.29
Nodes (8): applyCreateDefaultsByAdapterType(), asNonEmptyString(), ensureGatewayDeviceKey(), evaluateClaudeAuthSignal(), evaluateCodexAuthSignal(), generateEd25519PrivateKeyPem(), resolveInstructionsFilePath(), resolvePaperclipRunnerAdapterTransition()

### Community 88 - "agent-action-audit.ts"
Cohesion: 0.36
Nodes (7): AgentActionAuditFilters, agentActionAuditService(), CursorValue, cursorValueSchema, decodeCursor(), encodeCursor(), excerpt()

### Community 89 - "getCatalogManifest"
Cohesion: 0.32
Nodes (8): getCatalogManifest(), getCatalogSkills(), isMissingFileError(), listCatalogSkills(), loadCatalogManifest(), manifestUnavailableMessage(), resolveCatalogSkillReference(), searchText()

### Community 90 - "Status card query"
Cohesion: 0.25
Nodes (7): Agent-authored card recipe, CompanySearchQuery, Compilation guidance, Exact write-back sequence, Status card query, Summarizer compilation, Update assignments

### Community 91 - "Individual and Status Capsules"
Cohesion: 0.25
Nodes (7): App Agent Gradient Tokens, Common Mistakes, Heartbeat Status Capsule, Individual Agent Capsule, Individual and Status Capsules, Source Precedence, Website Marketing Capsule Palette

### Community 92 - "Ramp"
Cohesion: 0.25
Nodes (7): Before fetching, Design note, Mandatory Paperclip approval gates, Ramp, Safety rules while following Ramp, Source model, Typical flow

### Community 93 - "Product Design Critique"
Cohesion: 0.25
Nodes (7): Anti-patterns, Output format, Pre-critique context, Product Design Critique, The pass (in order), When not to use, When to use

### Community 94 - "Teams Catalog Migration Notes"
Cohesion: 0.25
Nodes (7): Bundled entries shipped in Phase H, Compatibility tests required before deleting legacy sources, Coordination, Intentionally deferred, Optional entries shipped in Phase H, Status, Teams Catalog Migration Notes

### Community 95 - "routes/company-skills.ts"
Cohesion: 0.29
Nodes (6): SkillPolicyDenialResponse, SkillPolicyResourceInput, SkillTelemetryInput, SkillTestRunAssignmentAuthorizationScope, isCatalogManifestUnavailableError(), listCatalogSkillsOrEmpty()

### Community 96 - "agent-task-run-telemetry.ts"
Cohesion: 0.48
Nodes (6): emitAgentTaskRun(), emitAgentTaskRunById(), HeartbeatRun, readNonEmptyString(), readUsageToken(), resolveDurationSeconds()

### Community 98 - "Summarize status"
Cohesion: 0.29
Nodes (6): API quick reference, Inputs, Procedure, Summarize status, When not to use, When to use

### Community 99 - "Worked examples"
Cohesion: 0.29
Nodes (6): 1. Login screen (mobile, 375×812), 2. Admin dashboard (desktop, 1280×800), 3. Settings page with form (desktop, 1280×800), 4. Modal confirmation overlay (desktop, 1280×800), Multi-screen flow, Worked examples

### Community 100 - "Paperclip Workflow Playbooks"
Cohesion: 0.29
Nodes (6): Company Import / Export, OpenClaw Invite (CEO), Paperclip Workflow Playbooks, Project Setup (CEO/Manager), Self-Test Playbook (App-Level), Setting Agent Instructions Path

### Community 101 - "validateManagedAgentBinding"
Cohesion: 0.33
Nodes (6): assertAdapterTestEnvironmentForCompany(), buildSandboxIdentityCheck(), readMetadataString(), resolveAdapterTestExecutionContext(), testManagedEnvironment(), validateManagedAgentBinding()

### Community 103 - "Paperclip — Converting Plans to Tasks"
Cohesion: 0.33
Nodes (5): Paperclip — Converting Plans to Tasks, Quick checklist before you publish a plan, What this skill is not, When converting an accepted plan into tasks, When you're asked to plan

### Community 104 - "Paperclip Create Agent API Reference"
Cohesion: 0.33
Nodes (5): Approval Lifecycle, Core Endpoints, Paperclip Create Agent API Reference, `POST /api/companies/:companyId/agent-hires`, Safety Notes

### Community 105 - "Issue Workspace Runtime Controls"
Cohesion: 0.33
Nodes (5): Control Services, Discover the Workspace, Issue Workspace Runtime Controls, MCP Tools, Read the URL

### Community 106 - "buildAgentDetail"
Cohesion: 0.40
Nodes (5): buildAgentAccessState(), buildAgentDetail(), canCreateAgents(), redactAgentRowForResponse(), redactForRestrictedAgentView()

### Community 107 - "companySkillPolicyRoutes"
Cohesion: 0.50
Nodes (3): companySkillPolicyRoutes(), assertCanAdministerPolicy(), assertSkillPolicyCompanyAccess()

### Community 108 - "agentmail.ts"
Cohesion: 0.40
Nodes (3): AGENTMAIL_EMAIL_CONTRACT, AGENTMAIL_TOOLS, schema

### Community 109 - "Example: Research and Gate a Notion MCP Connection"
Cohesion: 0.40
Nodes (4): Application, Example: Research and Gate a Notion MCP Connection, Gate Output, Input

### Community 110 - "ceo/AGENTS.md"
Cohesion: 0.40
Nodes (4): Delegation, Keeping work moving, Safety, What you do personally

### Community 111 - "ux-designer/AGENTS.md"
Cohesion: 0.40
Nodes (4): Responsibilities, Safety, Visual-truth gate, Working rules

### Community 112 - "Product Design"
Cohesion: 0.40
Nodes (4): Contents, Migration notes, Product Design, Skill rationale

### Community 113 - "Product Engineering"
Cohesion: 0.40
Nodes (4): Contents, Migration notes, Product Engineering, Skill rationale

### Community 114 - "The Heartbeat Procedure"
Cohesion: 0.40
Nodes (5): Delegating review tasks, Generated Artifacts and Work Products, Monitors and Watchers (say only what you actually scheduled), Status Quick Guide, The Heartbeat Procedure

### Community 116 - "types/inbox-agent-policy.ts"
Cohesion: 0.50
Nodes (3): INBOX_AGENT_POLICY_MODES, InboxAgentPolicy, InboxAgentPolicyMode

### Community 117 - "validators/inbox-agent-policy.ts"
Cohesion: 0.50
Nodes (3): inboxAgentPolicyModeSchema, UpdateInboxAgentPolicy, updateInboxAgentPolicySchema

### Community 118 - "assertSetupTokenLoginProviderCapability"
Cohesion: 0.50
Nodes (4): assertCodexLoginProviderCapability(), assertSandboxLoginEnvironment(), assertSetupTokenLoginProviderCapability(), resolveProviderSupportsLoginPty()

### Community 119 - "agent-start-lock.ts"
Cohesion: 0.67
Nodes (3): startLocksByAgent, waitForAgentStartLock(), withAgentStartLock()

### Community 120 - "ensureBuiltInAgentDefaultGrants"
Cohesion: 0.67
Nodes (4): ensureAgentDefaultGrants(), ensureBuiltInAgentDefaultGrants(), ensureCompanyDefaultAgentGrants(), ensureRootAgentDefaultChangeGrants()

### Community 123 - "Simplified English"
Cohesion: 0.50
Nodes (3): Approved words, Core rules, Simplified English

### Community 124 - "core-exec-team/agents/cto/AGENTS.md"
Cohesion: 0.50
Nodes (3): Responsibilities, Safety, Working rules

### Community 125 - "core-exec-team/agents/qa/AGENTS.md"
Cohesion: 0.50
Nodes (3): Browser flow, Responsibilities, Safety

### Community 126 - "Core Exec Team"
Cohesion: 0.50
Nodes (3): Contents, Core Exec Team, Migration notes

### Community 127 - "product-engineering/agents/cto/AGENTS.md"
Cohesion: 0.50
Nodes (3): Responsibilities, Safety, Working rules

### Community 128 - "product-engineering/agents/qa/AGENTS.md"
Cohesion: 0.50
Nodes (3): Browser flow, Responsibilities, Safety

### Community 129 - "senior-coder/AGENTS.md"
Cohesion: 0.50
Nodes (3): Responsibilities, Safety, Working rules

### Community 130 - "Worked Example: IC Heartbeat"
Cohesion: 0.50
Nodes (4): Worked Example: Archive A Resolved Inbox Item, Worked Example: IC Heartbeat, Worked Example: Report A Board User's Mine Inbox, Worked Example: Reviewer / Approver Heartbeat

### Community 133 - "Project Setup (Create + Workspace)"
Cohesion: 0.67
Nodes (3): Option A: One-call create with workspace, Option B: Two calls (project first, then workspace), Project Setup (Create + Workspace)

## Knowledge Gaps
- **1047 isolated node(s):** `agentApiKeys`, `agentConfigRevisions`, `agentMemberships`, `agentRuntimeState`, `agentTaskSessions` (+1042 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `companySkillService()` connect `companySkillService` to `builtInAgentService`, `services/company-skills.ts`, `services/agents.ts`, `services/teams-catalog.ts`, `agentRoutes`, `services/built-in-agents.ts`, `companySkillRoutes`, `installFromCatalog`, `asString`, `ensureSkillInventoryCurrent`, `isPlainRecord`, `resolveManagedSkillsRoot`, `plugin-managed-skills.ts`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Why does `agentRoutes()` connect `agentRoutes` to `validateManagedAgentBinding`, `companySkillService`, `routes/agents.ts`, `buildAgentDetail`, `agent-instructions.ts`, `materializeDefaultInstructionsBundleForNewAgent`, `assertSetupTokenLoginProviderCapability`, `asNonEmptyString`, `agent-invokability.ts`, `asRecord`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `agentService()` connect `services/agents.ts` to `builtInAgentService`, `services/company-skills.ts`, `services/teams-catalog.ts`, `companySkillService`, `services/built-in-agents.ts`, `pluginManagedAgentService`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `companySkillService()` (e.g. with `auditSkill()` and `browseProjectWorkspace()`) actually correct?**
  _`companySkillService()` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `builtInAgentService()` (e.g. with `autoProvisionBundledAgents()` and `ensure()`) actually correct?**
  _`builtInAgentService()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `agentApiKeys`, `agentConfigRevisions`, `agentMemberships` to the rest of the system?**
  _1047 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `validators/company-skill.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.021505376344086023 - nodes in this community are weakly interconnected._