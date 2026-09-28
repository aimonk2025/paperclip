# Capability census — stories

**75 files · 27,382 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 38 |
| retries | 17 |
| validates input | 10 |
| enforces a timeout | 9 |
| caches | 7 |
| classifies errors | 5 |
| captures a session id | 3 |
| emits telemetry | 3 |
| tracks token usage | 3 |
| streams incrementally | 1 |
| spawns a process | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `issue-thread-interactions.stories.tsx` | 1377 | SuggestedTasksPending, SuggestedTasksAccepted, SuggestedTasksRejected, AskUserQuestionsPending, AskUserQuestionsAnswered +45 |
| `chat-comments.stories.tsx` | 1070 | FullSurfaceMatrix, CommentThreads, LiveRunChat, IssueChatWithTimeline, IssueThreadNotices +1 |
| `dialogs-modals.stories.tsx` | 1069 | NewIssueEmpty, NewIssuePrefilled, NewIssueValidationError, NewIssueCheapLanePrimary, NewIssueCheapLaneCheap +14 |
| `issue-management.stories.tsx` | 1005 | FullSurfaceMatrix, IssuePropertiesLongValuesDesktop, IssuePropertiesLongValuesMobile, IssuePropertiesModelOverride, IssuePropertiesMobileBlockerActions +1 |
| `agent-management.stories.tsx` | 923 | ManagementMatrix, ForcedKubernetesExecution, ForcedKubernetesMissingEnvironment |
| `forms-editors.stories.tsx` | 820 | AllFormsAndEditors, RoutineRunVariablesDialogOpen, FoldCurtainShowcase |
| `search.stories.tsx` | 783 | SearchSurfaces |
| `budget-finance.stories.tsx` | 774 | FullMatrix |
| `data-viz-misc.stories.tsx` | 766 | ActivityChartsPopulated, ActivityChartsEmpty, KanbanBoardPopulated, KanbanBoardEmpty, FilterBarPopulated +16 |
| `external-objects.stories.tsx` | 721 | FullSurface, PropertiesRowDesktop, PropertiesRowMobileSheet, RelatedWorkEmpty, SidebarMobile +3 |
| `status-language.stories.tsx` | 721 | FullMatrix |
| `access-profiles.stories.tsx` | 693 | IndexPopulated, IndexNewToolsChip, IndexLongProfileName, AccessCheckerSheet, IndexEmpty +13 |
| `artifacts.stories.tsx` | 658 | Grid, GroupedByTask, GroupedByParentTask, SelectedStack, MobileGrouping +1 |
| `what-needs-me.stories.tsx` | 624 | DateGrouping, GroupedByType, GroupedByProject, GroupedBySeverity, WithCurtains +8 |
| `decisions-desk.stories.tsx` | 591 | TodaysDesk, DeskClearToday, AgingShelf, QueuePage, CollapsedInteractionAudience +1 |
| `document-annotations.stories.tsx` | 573 | IntegratedDesktopOpen, IntegratedDesktopZeroComments, IntegratedDesktopEditMode, IntegratedDesktopDirtyDraft, IntegratedMobileBottomSheet +4 |
| `file-viewer.stories.tsx` | 523 | FileViewerSheetProps, FileViewerSheet, TextContentWithHighlightedLine, TextContentLongPathTruncation, OpenFilePrompt +10 |
| `projects-goals-workspaces.stories.tsx` | 516 | SurfaceMatrix |
| `source-issue-recovery.stories.tsx` | 469 | RecoveryActionCardStates, InboxRowChips, BlockerNoticeRecoveryIndicators, ActiveRunPanelRecoveryChips |
| `routine-detail-c.stories.tsx` | 464 | Overview, OverviewDescriptionAnnotations, Triggers, Variables, Secrets +3 |
| `summary-slot-card.stories.tsx` | 436 | Disabled, SetupCta, Empty, Generating, GeneratingWithStatusLine +10 |
| `built-in-agents.stories.tsx` | 398 | SurfaceGallery, ConfigureModal, PauseConfirmDialog, BundleStatusPanel |
| `test-tab.stories.tsx` | 395 | Default, AllowedResult, AskFirstResult, ErrorResult, RunningState +3 |
| `navigation-layout.stories.tsx` | 390 | BoardChromeMatrix, SidebarIconAlignment |
| `team-catalog.stories.tsx` | 368 | BrowseList, DetailPane, InstalledStates, InstallTargetManager, InstallSourcePolicy +7 |

## Contract members — each is a capability

**FileViewerSheetProps** (3 members)

```
issueId, open, onOpenChange
```

## Structural duplication — the reduction lever

Identical logic across N files. This is where a rebuild gets smaller
WITHOUT losing features — unlike dropping capabilities.

| Repeated in | Shape |
|---|---|
| **9 files** | `}) { return ( <section className="paperclip-story__frame overflow-hidd…` |
| **9 files** | `return ( <section className="paperclip-story__frame overflow-hidden"> …` |
| **9 files** | `<section className="paperclip-story__frame overflow-hidden"> <div clas…` |
| **9 files** | `<div className="border-b border-border px-5 py-4"> <div className="pap…` |
| **9 files** | `<div className="paperclip-story__label">{eyebrow}</div> <h2 className=…` |
| **8 files** | `import { T } from "@/components/T"; import { T } from "@/components/T"…` |

## Decision ledger — fill this in, leave nothing blank

| Capability | KEEP / DROP | Reason |
|---|---|---|
| authenticates | | |
| caches | | |
| captures a session id | | |
| classifies errors | | |
| emits telemetry | | |
| enforces a timeout | | |
| retries | | |
| spawns a process | | |
| streams incrementally | | |
| tracks token usage | | |
| validates input | | |
| FileViewerSheetProps.issueId | | |
| FileViewerSheetProps.open | | |
| FileViewerSheetProps.onOpenChange | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
