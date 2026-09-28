# Capability census — lib

**173 files · 25,512 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 42 |
| validates input | 16 |
| parses JSON events | 13 |
| caches | 11 |
| retries | 10 |
| buffers partial lines | 8 |
| streams incrementally | 7 |
| enforces a timeout | 5 |
| classifies errors | 5 |
| spawns a process | 5 |
| tracks token usage | 4 |
| captures a session id | 2 |
| handles cancellation | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `inbox.ts` | 1318 | RECENT_ISSUES_LIMIT, FAILED_RUN_STATUSES, ACTIONABLE_APPROVAL_STATUSES, DISMISSED_KEY, READ_ITEMS_KEY +79 |
| `issue-chat-messages.ts` | 1171 | IssueChatComment, IssueChatLinkedRun, IssueChatTranscriptEntry, StableThreadMessageCacheEntry, preserveReadableStreamingRetraction +7 |
| `attention.ts` | 916 | AttentionListOptions, INLINE_RESOLVABLE_SOURCE_KINDS, isInlineResolvable, sourceMeta, severityStyle +55 |
| `cross-tab-poll.ts` | 829 | LeaseRecord, LeaderRole, LeaseStore, LeaderElectionEnv, LeaderElectionOptions +18 |
| `skill-studio.ts` | 555 | TERMINAL_RUN_STATUSES, DEFAULT_TEST_RUN_TEMPLATE_ID, NO_TEST_RUN_TEMPLATE_STORAGE_VALUE, isTerminalRunStatus, shouldPollRun +43 |
| `activity-format.ts` | 496 | formatActivityVerb, formatIssueActivityAction |
| `queryKeys.ts` | 478 | queryKeys |
| `interrupt-handoff.ts` | 439 | isOperatorInterruptedRun, runStatusClassName, RunStatusPresentation, resolveRunStatusPresentation, extractAgentMentionIds +20 |
| `search-query-parser.ts` | 428 | SearchOperatorKey, SearchOperatorPill, SearchOperatorSuggestion, SEARCH_OPERATOR_QUICK_FILTERS, SEARCH_OPERATOR_SUGGESTIONS +11 |
| `timeline/layout.ts` | 415 | LayoutOptions, PositionedBar, PositionedMarker, ActorRow, Connector +14 |
| `status-colors.ts` | 395 | issueStatusIcon, issueStatusIconDefault, issueStatusText, issueStatusTextDefault, BrandChipColor +31 |
| `pipeline-item-detail.ts` | 389 | INTERNAL_FIELD_KEYS, PipelineChildRow, humanizePipelineItemStatus, formatFieldValue, displayPipelineItemFields +10 |
| `optimistic-issue-comments.ts` | 386 | ISSUE_COMMENT_PAGE_SIZE, IssueCommentReassignment, OptimisticIssueComment, IssueTimelineComment, LocallyQueuedIssueComment +17 |
| `issue-thread-interactions.ts` | 386 | SuggestedTaskTreeNode, isIssueThreadInteraction, ItemVerdictProgress, getItemVerdictProgress, buildItemVerdictsSummary +11 |
| `zip.ts` | 375 | readZipArchive, createZipArchive, estimateZipArchiveSize |
| `issue-output.ts` | 312 | OutputFileTone, OutputFileGlyph, formatBytes, formatDuration, normalizeOutputContentType +10 |
| `transcriptPresentation.ts` | 281 | ToolInputDetail, formatToolPayload, parseToolPayload, isCommandTool, displayToolName +6 |
| `blockedInbox.ts` | 275 | BlockedReasonVariant, BLOCKED_REASON_VARIANT_ORDER, BLOCKED_VARIANT_LABELS, BlockedInboxBadgeTone, blockedReasonVariant +17 |
| `issue-filters.ts` | 274 | IssueFilterWorkspaceLookup, IssueFilterWorkspaceContext, IssueFilterState, defaultIssueFilterState, externalObjectFilterOrder +12 |
| `workspace-access-state.ts` | 272 | WorkspaceAccessActionKind, WorkspaceAccessAction, WorkspaceAccessNotice, WorkspaceAccessState, WorkspaceLoginHandoffFailureInfo +2 |
| `company-export-selection.ts` | 272 | ExportCategoryKey, ExportCategorySelection, ExportSelectionIssue, ExportSelectionEmbeddedAsset, EXPORT_CATEGORY_ORDER +6 |
| `issueDetailBreadcrumb.ts` | 272 | IssueDetailHeaderSeed, withIssueDetailHeaderSeed, readIssueDetailHeaderSeed, createIssueDetailLocationState, armIssueDetailInboxQuickArchive +6 |
| `cron-fires.ts` | 272 | parseCronExpression, nextCronFires, FireDisposition, FirePreviewEntry, previewFirePolicies |
| `interaction-audience.ts` | 267 | DEFAULT_RESOLVER_POLICY, resolverPolicyLabel, resolverPolicyEffect, RESOLVER_POLICY_CHOICES, InteractionAudienceNarrowing +5 |
| `issue-monitor.ts` | 266 | MonitorIssueLike, MonitorDisplayState, DerivedMonitorState, MonitorDateTimeFormatOptions, formatMonitorEta +6 |

## Contract members — each is a capability

**IssueChatTranscriptEntry** (19 members)

```
kind, ts, text, delta, name, input, toolUseId, toolName, content, isError, subtype, errors, model, sessionId, inputTokens, outputTokens, cachedTokens, costUsd, changeType
```

**ProjectWorkspaceSummary** (17 members)

```
key, kind, workspaceId, workspaceName, cwd, branchName, lastUpdatedAt, projectWorkspaceId, executionWorkspaceId, executionWorkspaceStatus, serviceCount, runningServiceCount, primaryServiceUrl, primaryServiceUrlRunning, hasRuntimeConfig, linkedIssueCount, issues
```

**IssueChatLinkedRun** (12 members)

```
runId, status, agentId, adapterType, agentName, createdAt, startedAt, finishedAt, hasStoredOutput, logBytes, errorCode, resultJson
```

**BlockedReasonVariant** (12 members)

```
pending_board_decision, pending_user_decision, missing_successful_run_disposition, blocked_chain_stalled, blocked_by_unassigned_issue, blocked_by_assigned_backlog_issue, blocked_by_cancelled_issue, in_review_without_action_path, invalid_review_participant, open_recovery_issue, external_owner_action, blocked_by_uninvokable_assignee
```

**LivenessBannerView** (11 members)

```
reason, tone, title, body, blockerLink, automationLink, permissionKey, showRetry, retryKind, retryLabel, helperNote
```

**SourceResolvedWatchdogFold** (11 members)

```
sourceIssueId, sourceIssueIdentifier, sourceIssueStatus, sameRunEvidenceKind, sameRunEvidenceId, sameRunEvidenceAt, silenceStartedAt, silenceAgeMs, evaluationIssueId, evaluationIssueIdentifier, cleanup
```

**SkillCreateDraft** (11 members)

```
name, slug, tagline, description, color, categories, markdown, sharingScope, forkedFromSkillId, forkedFromName, folderId
```

**WorkModeMeta** (10 members)

```
value, label, shortLabel, icon, tone, classes, chip, container, menuItem, badge
```

## Case sets — each arm is a case you must handle or drop

- **IssueChatTranscriptEntry** (11): assistant, thinking, user, tool_call, tool_result, init, result, stderr, system, stdout, diff
- **StatusCardLifecycle** (8): compiling, fresh, stale, updating, error, paused_budget, paused_hours, archived
- **ParsedSearchQuery** (8): status, priority, assigneeAgentId, assigneeUserId, projectId, labelId, updatedWithin, updatedAfter
- **ComposerHandoffPreviewKind** (7): interrupt_handoff_agent, wake_agent, user_handoff, clear_assignee, notify_agent, plain_text_only, none
- **MonitorDisplayState** (6): scheduled, retrying, due-now, overdue, cleared, none
- **InboxCategoryFilter** (6): everything, issues_i_touched, join_requests, approvals, failed_runs, alerts
- **ExportCategoryKey** (6): agents, projects, skills, routines, tasks, attachments
- **SourceResolvedFoldCleanupOutcome** (6): terminated, termination_sent_still_running, failed, not_running, no_process_metadata, skipped_non_local_adapter

## Decision ledger — fill this in, leave nothing blank

| Capability | KEEP / DROP | Reason |
|---|---|---|
| authenticates | | |
| buffers partial lines | | |
| caches | | |
| captures a session id | | |
| classifies errors | | |
| enforces a timeout | | |
| handles cancellation | | |
| parses JSON events | | |
| retries | | |
| spawns a process | | |
| streams incrementally | | |
| tracks token usage | | |
| validates input | | |
| IssueChatTranscriptEntry.kind | | |
| IssueChatTranscriptEntry.ts | | |
| IssueChatTranscriptEntry.text | | |
| IssueChatTranscriptEntry.delta | | |
| IssueChatTranscriptEntry.name | | |
| IssueChatTranscriptEntry.input | | |
| IssueChatTranscriptEntry.toolUseId | | |
| IssueChatTranscriptEntry.toolName | | |
| IssueChatTranscriptEntry.content | | |
| IssueChatTranscriptEntry.isError | | |
| IssueChatTranscriptEntry.subtype | | |
| IssueChatTranscriptEntry.errors | | |
| IssueChatTranscriptEntry.model | | |
| IssueChatTranscriptEntry.sessionId | | |
| IssueChatTranscriptEntry.inputTokens | | |
| IssueChatTranscriptEntry.outputTokens | | |
| IssueChatTranscriptEntry.cachedTokens | | |
| IssueChatTranscriptEntry.costUsd | | |
| IssueChatTranscriptEntry.changeType | | |
| ProjectWorkspaceSummary.key | | |
| ProjectWorkspaceSummary.kind | | |
| ProjectWorkspaceSummary.workspaceId | | |
| ProjectWorkspaceSummary.workspaceName | | |
| ProjectWorkspaceSummary.cwd | | |
| ProjectWorkspaceSummary.branchName | | |
| ProjectWorkspaceSummary.lastUpdatedAt | | |
| ProjectWorkspaceSummary.projectWorkspaceId | | |
| ProjectWorkspaceSummary.executionWorkspaceId | | |
| ProjectWorkspaceSummary.executionWorkspaceStatus | | |
| ProjectWorkspaceSummary.serviceCount | | |
| ProjectWorkspaceSummary.runningServiceCount | | |
| ProjectWorkspaceSummary.primaryServiceUrl | | |
| ProjectWorkspaceSummary.primaryServiceUrlRunning | | |
| ProjectWorkspaceSummary.hasRuntimeConfig | | |
| ProjectWorkspaceSummary.linkedIssueCount | | |
| ProjectWorkspaceSummary.issues | | |
| IssueChatLinkedRun.runId | | |
| IssueChatLinkedRun.status | | |
| IssueChatLinkedRun.agentId | | |
| IssueChatLinkedRun.adapterType | | |
| IssueChatLinkedRun.agentName | | |
| IssueChatLinkedRun.createdAt | | |
| IssueChatLinkedRun.startedAt | | |
| IssueChatLinkedRun.finishedAt | | |
| IssueChatLinkedRun.hasStoredOutput | | |
| IssueChatLinkedRun.logBytes | | |
| IssueChatLinkedRun.errorCode | | |
| IssueChatLinkedRun.resultJson | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
