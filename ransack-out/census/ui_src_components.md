# Capability census — components

**20 files · 3,782 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 12 |
| streams incrementally | 4 |
| validates input | 4 |
| buffers partial lines | 3 |
| tracks token usage | 3 |
| retries | 2 |
| caches | 2 |
| spawns a process | 2 |
| parses JSON events | 1 |
| enforces a timeout | 1 |
| classifies errors | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `task-chat/transcript-adapter.ts` | 731 | isTerminalRunStatus, isNestableLiveChild, flattenSelfTalk, summarizeToolInput, toolDisplayName +14 |
| `transcript/useLiveRunTranscripts.ts` | 526 | RunTranscriptSource, resolveInitialLogOffset, useLiveRunTranscripts |
| `task-chat/task-chat-fixtures.ts` | 318 | TaskChatScenario, buildScenario |
| `task-chat/task-chat-model.ts` | 308 | TaskChatAuthorKind, TaskChatToolStatus, TaskChatApprovalOptionKind, TaskChatPlanEntryStatus, TaskChatPlanEntryPriority +17 |
| `environment-variables-editor/model.ts` | 306 | RowSource, EnvRow, nextRowId, emptyRow, rowsFromValue +15 |
| `folders/skill-folder-tree.ts` | 202 | FolderTreeNode, ReservedRootKey, SkillFolderTreeModel, isReservedRootSystemKey, isBundledFolder +9 |
| `task-chat/task-chat-states.ts` | 181 | TASK_CHAT_STATES, TaskChatStateId, TaskChatStateTier, TaskChatStateSurface, TaskChatStateMeta +2 |
| `useSummaryDraftStream.ts` | 180 | SummaryDraftStream, useSummaryDraftStream |
| `task-chat/task-chat-attachments.ts` | 174 | FileKind, isImageFilename, fileKindForName, formatFileSize, AttachmentRef +3 |
| `issue-properties/helpers.ts` | 129 | defaultProjectWorkspaceIdForProject, defaultExecutionWorkspaceModeForProject, isMainIssueWorkspace, toDateTimeLocalValue, ISSUE_THINKING_EFFORT_OPTIONS +7 |
| `task-chat/tool-taxonomy.ts` | 123 | ToolIcon, ToolFamily, ToolTaxonomyEntry, isGenericToolName, mcpToolSegment +2 |
| `task-chat/task-chat-adapter.ts` | 106 | TaskChatAdapterContext, formatTaskChatTimestamp, commentsToTaskChatItems |
| `task-chat/status-whimsy.ts` | 97 | ANALOG_OFFICE_WORDS, CLAUDE_CODE_WORDS, WHIMSY_WORDS, WHIMSY_ROTATE_MS, isGenericStatusLabel +1 |
| `task-chat/motion-tokens.ts` | 92 | MotionTokenKind, MotionTokenDef, MOTION_TOKENS, EASING_PRESETS, MOTION_TOKEN_GROUPS +2 |
| `task-chat/interaction-thread-order.ts` | 85 | isSuppressedThreadInteraction, interactionThreadAnchorMs |
| `environment-variables-editor/parse-dotenv.ts` | 64 | ParsedEnvPair, parseDotenv, looksLikeDotenv |
| `task-chat/useWindowAutoFollow.ts` | 63 | useWindowAutoFollow |
| `agent-config-defaults.ts` | 46 | defaultCreateValues |
| `environment-variables-editor/sensitive.ts` | 46 | SENSITIVE_ENV_KEY_RE, isSensitiveEnv |
| `issue-properties/index.ts` | 5 | — |

## Contract members — each is a capability

**TaskChatMessageItem** (18 members)

```
id, kind, author, authorName, text, timestamp, streaming, optimistic, queueTargetRunId, agentIcon, onBehalfOfUserName, interstitial, atMs, attachedTurn, presentation, metadata, runAgentId, createdAtIso
```

**TaskChatTurnItem** (13 members)

```
id, kind, items, settled, liveStatus, animateFold, summary, durationLabel, toolCount, added, removed, tokensLabel, failed
```

**TaskChatStatusItem** (11 members)

```
id, kind, status, label, detail, toolName, selfTalk, elapsedMs, startedAtMs, tokens, approval
```

**TaskChatToolItem** (10 members)

```
id, kind, name, rawName, toolKind, status, target, detail, diff, decision
```

**EnvRow** (9 members)

```
id, name, source, textValue, secretId, userSecretKey, required, version, sensitiveDismissed
```

**SkillFolderTreeModel** (7 members)

```
my, company, projects, bundled, byId, childrenById, roots
```

**RunTranscriptSource** (6 members)

```
id, status, adapterType, hasStoredOutput, logBytes, lastOutputBytes
```

**TaskChatThinkingItem** (6 members)

```
id, kind, lines, streaming, collapsed, summaryLabel
```

## Case sets — each arm is a case you must handle or drop

- **ToolFamily** (9): terminal, grep, search, read, edit, web, agent, mcp, other
- **TaskChatStatusItem** (6): running, working, awaiting_approval, interrupted, refused, truncated
- **TaskChatApprovalOptionKind** (4): allow_once, allow_always, reject_once, reject_always

## Decision ledger — fill this in, leave nothing blank

| Capability | KEEP / DROP | Reason |
|---|---|---|
| authenticates | | |
| buffers partial lines | | |
| caches | | |
| classifies errors | | |
| enforces a timeout | | |
| parses JSON events | | |
| retries | | |
| spawns a process | | |
| streams incrementally | | |
| tracks token usage | | |
| validates input | | |
| TaskChatMessageItem.id | | |
| TaskChatMessageItem.kind | | |
| TaskChatMessageItem.author | | |
| TaskChatMessageItem.authorName | | |
| TaskChatMessageItem.text | | |
| TaskChatMessageItem.timestamp | | |
| TaskChatMessageItem.streaming | | |
| TaskChatMessageItem.optimistic | | |
| TaskChatMessageItem.queueTargetRunId | | |
| TaskChatMessageItem.agentIcon | | |
| TaskChatMessageItem.onBehalfOfUserName | | |
| TaskChatMessageItem.interstitial | | |
| TaskChatMessageItem.atMs | | |
| TaskChatMessageItem.attachedTurn | | |
| TaskChatMessageItem.presentation | | |
| TaskChatMessageItem.metadata | | |
| TaskChatMessageItem.runAgentId | | |
| TaskChatMessageItem.createdAtIso | | |
| TaskChatTurnItem.id | | |
| TaskChatTurnItem.kind | | |
| TaskChatTurnItem.items | | |
| TaskChatTurnItem.settled | | |
| TaskChatTurnItem.liveStatus | | |
| TaskChatTurnItem.animateFold | | |
| TaskChatTurnItem.summary | | |
| TaskChatTurnItem.durationLabel | | |
| TaskChatTurnItem.toolCount | | |
| TaskChatTurnItem.added | | |
| TaskChatTurnItem.removed | | |
| TaskChatTurnItem.tokensLabel | | |
| TaskChatTurnItem.failed | | |
| TaskChatStatusItem.id | | |
| TaskChatStatusItem.kind | | |
| TaskChatStatusItem.status | | |
| TaskChatStatusItem.label | | |
| TaskChatStatusItem.detail | | |
| TaskChatStatusItem.toolName | | |
| TaskChatStatusItem.selfTalk | | |
| TaskChatStatusItem.elapsedMs | | |
| TaskChatStatusItem.startedAtMs | | |
| TaskChatStatusItem.tokens | | |
| TaskChatStatusItem.approval | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
