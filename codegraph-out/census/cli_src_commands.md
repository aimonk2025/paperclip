# Capability census — commands

**48 files · 23,494 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| validates input | 34 |
| authenticates | 27 |
| parses JSON events | 21 |
| reads config | 18 |
| reads from disk | 15 |
| writes to disk | 11 |
| retries | 6 |
| buffers partial lines | 6 |
| handles cancellation | 4 |
| caches | 4 |
| enforces a timeout | 4 |
| classifies errors | 4 |
| emits telemetry | 4 |
| streams incrementally | 2 |
| tracks token usage | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `worktree.ts` | 4399 | WorktreeSeedValidationSummary, EnsureWorktreeSeededResult, SeededWorktreeExecutionQuarantineSummary, isMissingStorageObjectError, readSourceAttachmentBody +29 |
| `client/company.ts` | 2083 | buildImportSelectionCatalog, buildDefaultImportSelectionState, buildSelectedFilesFromImportSelection, buildDefaultImportAdapterOverrides, renderCompanyImportPreview +22 |
| `client/issue.ts` | 1450 | registerIssueCommands |
| `client/skills.ts` | 1024 | CompanySkillCheckRow, CompanySkillUpdateRow, registerSkillsCommands, resolveCompanySkillReference |
| `client/plugin.ts` | 998 | buildPluginInstallRequest, renderLocalPluginInstallHint, probeTargetDiagnostics, formatTargetDiagnostics, buildPluginInitScaffoldOptions +4 |
| `client/agent.ts` | 878 | registerAgentCommands |
| `pipelines.ts` | 846 | registerPipelineCommands |
| `worktree-merge-history-lib.ts` | 764 | WORKTREE_MERGE_SCOPES, WorktreeMergeScope, ImportAdjustment, IssueMergeAction, CommentMergeAction +17 |
| `onboard.ts` | 756 | isEphemeralNpxExecution, onboard |
| `client/secrets.ts` | 726 | InlineSecretMigrationCandidate, parseSecretsInclude, isSensitiveEnvKey, toPlainEnvValue, buildInlineMigrationSecretName +3 |
| `client/teams.ts` | 720 | registerTeamCommands |
| `client/feedback.ts` | 676 | FeedbackTraceQueryOptions, registerFeedbackCommands, resolveFeedbackCompanyId, buildFeedbackTraceQuery, normalizeFeedbackTraceExportFormat +7 |
| `client/access.ts` | 519 | registerAccessCommands |
| `install.ts` | 420 | PUBLIC_NPM_REGISTRY, InstallOptions, CommandRunner, runCommandWithDiagnostics, resolveGitInstallWorkspacePackages +8 |
| `env.ts` | 411 | envCommand |
| `routines.ts` | 354 | disableAllRoutinesInConfig, disableAllRoutinesCommand, registerRoutineCommands |
| `heartbeat-run.ts` | 344 | heartbeatRun |
| `worktree-lib.ts` | 336 | DEFAULT_WORKTREE_HOME, WORKTREE_SEED_MODES, WORKTREE_SEED_MANIFEST, WORKTREE_SEED_PENDING_MARKER, WORKTREE_SEED_COMPLETE_MARKER +21 |
| `client/workspace.ts` | 327 | registerWorkspaceCommands |
| `client/run.ts` | 321 | registerRunCommands |
| `client/common.ts` | 298 | BaseClientOptions, ResolvedClientContext, addCommonClientOptions, resolveCommandContext, resolveApiBase +7 |
| `client/prompt.ts` | 276 | registerPromptCommands, runAgentPrompt, runBoardPrompt |
| `update.ts` | 268 | InstallMode, UpdateOptions, detectInstallMode, compareVersions, resolveUpdateRequest +2 |
| `client/connect.ts` | 265 | registerConnectCommand |
| `client/approval.ts` | 260 | registerApprovalCommands |

## Contract members — each is a capability

**WorktreeMergePlan** (27 members)

```
companyId, companyName, issuePrefix, previewIssueCounterStart, scopes, projectImports, issuePlans, commentPlans, documentPlans, attachmentPlans, counts, projectsToImport, issuesToInsert, issuesExisting, issueDrift, commentsToInsert, commentsExisting, commentsMissingParent, documentsToInsert, documentsToMerge, documentsExisting, documentsConflictingKey, documentsMissingParent, documentRevisionsToInsert, attachmentsToInsert, attachmentsExisting, attachmentsMissingParent
```

**IssueDocumentRow** (18 members)

```
id, companyId, issueId, documentId, key, linkCreatedAt, linkUpdatedAt, title, format, latestBody, latestRevisionId, latestRevisionNumber, createdByAgentId, createdByUserId, updatedByAgentId, updatedByUserId, documentCreatedAt, documentUpdatedAt
```

**IssueAttachmentRow** (17 members)

```
id, companyId, issueId, issueCommentId, assetId, provider, objectKey, contentType, byteSize, sha256, originalFilename, createdByAgentId, createdByUserId, assetCreatedAt, assetUpdatedAt, attachmentCreatedAt, attachmentUpdatedAt
```

**PlannedIssueInsert** (13 members)

```
source, action, previewIssueNumber, previewIdentifier, targetStatus, targetAssigneeAgentId, targetCreatedByAgentId, targetProjectId, targetProjectWorkspaceId, targetGoalId, projectResolution, mappedProjectName, adjustments
```

**WorktreeLocalPaths** (13 members)

```
cwd, repoConfigDir, configPath, envPath, homeDir, instanceId, instanceRoot, contextPath, embeddedPostgresDataDir, backupDir, logDir, secretsKeyFilePath, storageDir
```

**DocumentRevisionRow** (9 members)

```
id, companyId, documentId, revisionNumber, body, changeSummary, createdByAgentId, createdByUserId, createdAt
```

**WorktreeSeedValidationSummary** (9 members)

```
authUserCount, credentialAccountCount, instanceAdminCount, activeMembershipCount, companyCount, issueCount, representativeCompanyId, representativeIssueId, migrationRevision
```

**BaseClientOptions** (9 members)

```
config, dataDir, context, profile, apiBase, apiKey, runId, companyId, json
```

## Case sets — each arm is a case you must handle or drop

- **ImportAdjustment** (9): clear_assignee_agent, clear_project, clear_project_workspace, clear_goal, clear_author_agent, coerce_in_progress_to_todo, clear_document_agent, clear_document_revision_agent, clear_attachment_agent

## Structural duplication — the reduction lever

Identical logic across N files. This is where a rebuild gets smaller
WITHOUT losing features — unlike dropping capabilities.

| Repeated in | Shape |
|---|---|
| **4 files** | `try { const ctx = resolveCommandContext(opts, { requireCompany: true }…` |
| **3 files** | `} function buildApiUrl(apiBase: string, path: string): string { const …` |
| **3 files** | `const ctx = resolveCommandContext(opts, { requireCompany: true }); pri…` |

## Decision ledger — fill this in, leave nothing blank

| Capability | KEEP / DROP | Reason |
|---|---|---|
| authenticates | | |
| buffers partial lines | | |
| caches | | |
| classifies errors | | |
| emits telemetry | | |
| enforces a timeout | | |
| handles cancellation | | |
| parses JSON events | | |
| reads config | | |
| reads from disk | | |
| retries | | |
| streams incrementally | | |
| tracks token usage | | |
| validates input | | |
| writes to disk | | |
| WorktreeMergePlan.companyId | | |
| WorktreeMergePlan.companyName | | |
| WorktreeMergePlan.issuePrefix | | |
| WorktreeMergePlan.previewIssueCounterStart | | |
| WorktreeMergePlan.scopes | | |
| WorktreeMergePlan.projectImports | | |
| WorktreeMergePlan.issuePlans | | |
| WorktreeMergePlan.commentPlans | | |
| WorktreeMergePlan.documentPlans | | |
| WorktreeMergePlan.attachmentPlans | | |
| WorktreeMergePlan.counts | | |
| WorktreeMergePlan.projectsToImport | | |
| WorktreeMergePlan.issuesToInsert | | |
| WorktreeMergePlan.issuesExisting | | |
| WorktreeMergePlan.issueDrift | | |
| WorktreeMergePlan.commentsToInsert | | |
| WorktreeMergePlan.commentsExisting | | |
| WorktreeMergePlan.commentsMissingParent | | |
| WorktreeMergePlan.documentsToInsert | | |
| WorktreeMergePlan.documentsToMerge | | |
| WorktreeMergePlan.documentsExisting | | |
| WorktreeMergePlan.documentsConflictingKey | | |
| WorktreeMergePlan.documentsMissingParent | | |
| WorktreeMergePlan.documentRevisionsToInsert | | |
| WorktreeMergePlan.attachmentsToInsert | | |
| WorktreeMergePlan.attachmentsExisting | | |
| WorktreeMergePlan.attachmentsMissingParent | | |
| IssueDocumentRow.id | | |
| IssueDocumentRow.companyId | | |
| IssueDocumentRow.issueId | | |
| IssueDocumentRow.documentId | | |
| IssueDocumentRow.key | | |
| IssueDocumentRow.linkCreatedAt | | |
| IssueDocumentRow.linkUpdatedAt | | |
| IssueDocumentRow.title | | |
| IssueDocumentRow.format | | |
| IssueDocumentRow.latestBody | | |
| IssueDocumentRow.latestRevisionId | | |
| IssueDocumentRow.latestRevisionNumber | | |
| IssueDocumentRow.createdByAgentId | | |
| IssueDocumentRow.createdByUserId | | |
| IssueDocumentRow.updatedByAgentId | | |
| IssueDocumentRow.updatedByUserId | | |
| IssueDocumentRow.documentCreatedAt | | |
| IssueDocumentRow.documentUpdatedAt | | |
| IssueAttachmentRow.id | | |
| IssueAttachmentRow.companyId | | |
| IssueAttachmentRow.issueId | | |
| IssueAttachmentRow.issueCommentId | | |
| IssueAttachmentRow.assetId | | |
| IssueAttachmentRow.provider | | |
| IssueAttachmentRow.objectKey | | |
| IssueAttachmentRow.contentType | | |
| IssueAttachmentRow.byteSize | | |
| IssueAttachmentRow.sha256 | | |
| IssueAttachmentRow.originalFilename | | |
| IssueAttachmentRow.createdByAgentId | | |
| IssueAttachmentRow.createdByUserId | | |
| IssueAttachmentRow.assetCreatedAt | | |
| IssueAttachmentRow.assetUpdatedAt | | |
| IssueAttachmentRow.attachmentCreatedAt | | |
| IssueAttachmentRow.attachmentUpdatedAt | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
