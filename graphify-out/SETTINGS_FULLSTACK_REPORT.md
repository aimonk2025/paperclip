# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 28 files · ~30,495 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 257 nodes · 378 edges · 25 communities (18 shown, 7 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PipelineSettings.tsx
- services/instance-settings.ts
- useHiddenSettings
- src/settings-visibility.ts
- PipelineSettings
- PluginSettings.tsx
- InstanceExperimentalSettings.tsx
- routes/instance-settings.ts
- src/setting-defaults.ts
- StatusCardSettingsForm.tsx
- buildIncomingCarryOverFieldGroups
- buildCarryOverFieldGroups
- stageAutomation
- ProfileSettings
- validators/sidebar-preferences.ts
- GeneralSettingsContext.tsx
- services/sidebar-preferences.ts
- computeStageForm
- routes/sidebar-preferences.ts
- savedStageVariables
- instance_settings.ts
- plugin_company_settings.ts
- types/sidebar-preferences.ts
- buildAutomationVariableGroups

## God Nodes (most connected - your core abstractions)
1. `PipelineSettings()` - 35 edges
2. `useHiddenSettings()` - 11 edges
3. `instanceSettingsService()` - 9 edges
4. `stageAutomation()` - 7 edges
5. `computeStageForm()` - 7 edges
6. `instanceSettingsRoutes()` - 6 edges
7. `applyExperimentalSettingsPatch()` - 6 edges
8. `buildCarryOverFieldGroups()` - 6 edges
9. `buildIncomingCarryOverFieldGroups()` - 6 edges
10. `resolveWorktreeRunExecutionActivationState()` - 5 edges
11. `toExperimentalView()` - 5 edges
12. `CompanySettings()` - 5 edges
13. `selectedCarryOverFieldKeys()` - 5 edges
14. `carryOverPolicyForSave()` - 5 edges
15. `PluginSettings()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `ExperimentalToggleCard()` --calls--> `useHiddenSettings()`  [EXTRACTED]
  ui/src/pages/InstanceExperimentalSettings.tsx → ui/src/hooks/useHiddenSettings.ts
- `HiddenSettingsPageGate()` --calls--> `useHiddenSettings()`  [EXTRACTED]
  ui/src/components/HiddenSettingsPageGate.tsx → ui/src/hooks/useHiddenSettings.ts
- `instanceSettingsRoutes()` --calls--> `getHiddenSettings()`  [EXTRACTED]
  server/src/routes/instance-settings.ts → server/src/services/settings-visibility.ts
- `instanceSettingsService()` --calls--> `getOperatorSettingDefaults()`  [EXTRACTED]
  server/src/services/instance-settings.ts → server/src/services/setting-defaults.ts
- `CompanySettingsSidebar()` --calls--> `useHiddenSettings()`  [EXTRACTED]
  ui/src/components/CompanySettingsSidebar.production.tsx → ui/src/hooks/useHiddenSettings.ts

## Import Cycles
- None detected.

## Communities (25 total, 7 thin omitted)

### Community 0 - "PipelineSettings.tsx"
Cohesion: 0.07
Nodes (28): ApproverKind, AUTOMATION_ITEM_BUILTIN_KEYS, AutomationVariableGroup, automationVariableKind(), AutomationVariableOption, automationVariablePreviewTitle(), AutomationVariableTokenHelper(), CarryOverFieldGroup (+20 more)

### Community 1 - "services/instance-settings.ts"
Cohesion: 0.11
Nodes (27): applyCloudCatalogDefaults(), applyExperimentalSettingsPatch(), applyManagedExperimentalOverlay(), getRuntimeInstanceId(), instanceExperimentalSettingsStorageSchema, instanceGeneralSettingsStorageSchema, instanceSettingsService(), toExperimentalView() (+19 more)

### Community 2 - "useHiddenSettings"
Cohesion: 0.15
Nodes (18): CompanySettingsNav(), CompanySettingsTab, getCompanySettingsTab(), hiddenSettingKeyByTab, items, CompanySettingsSidebar(), isSandboxProviderOnly(), CompanySettingsSidebar() (+10 more)

### Community 3 - "src/settings-visibility.ts"
Cohesion: 0.10
Nodes (16): experimentalSettingKey(), HIDEABLE_COMPANY_PAGES, HIDEABLE_COMPANY_SECTIONS, HIDEABLE_GENERAL_SECTIONS, HIDEABLE_INSTANCE_PAGES, HIDEABLE_SETTING_KEYS, HideableCompanyPage, HideableCompanySection (+8 more)

### Community 4 - "PipelineSettings"
Cohesion: 0.11
Nodes (19): approverValueFromOption(), dedupeEdges(), defaultReviewTarget(), executionWorkspaceSettingsForPreference(), flattenAutomationVariableKeys(), manualVariableNamesForTemplate(), nextStageByPosition(), nextStageForInsert() (+11 more)

### Community 5 - "PluginSettings.tsx"
Cohesion: 0.14
Nodes (12): FolderRequirements(), formatDuration(), formatRelativeTime(), formatTimestamp(), formatUptime(), isLikelyAbsolutePath(), isRootNotInspected(), PluginConfigFormProps (+4 more)

### Community 6 - "InstanceExperimentalSettings.tsx"
Cohesion: 0.14
Nodes (8): instanceSettingsApi, CompanySettings(), ExperimentalToggleCard(), formatActivationTimestamp(), InstanceExperimentalSettings(), resolveWorktreeRunExecutionDisplayState(), WorktreeRunExecutionDisplayState, InstanceGeneralSettings()

### Community 7 - "routes/instance-settings.ts"
Cohesion: 0.27
Nodes (10): assertCanManageInstanceSettings(), assertNoHiddenSettingChanges(), instanceSettingsRoutes(), publishActivitiesBestEffort(), sameJsonValue(), taskDrainTransitionQueue, withTaskDrainTransition(), getHiddenSettings() (+2 more)

### Community 8 - "src/setting-defaults.ts"
Cohesion: 0.18
Nodes (7): DEFAULTABLE_GENERAL_SETTINGS, defaultableFieldsSchema, DefaultableGeneralSetting, OperatorSettingDefaults, ParsedSettingDefaults, schemaDefaults, SETTING_DEFAULTS_ENV_KEY

### Community 9 - "StatusCardSettingsForm.tsx"
Cohesion: 0.22
Nodes (5): DEBOUNCE_OPTIONS, INTERVAL_OPTIONS, StatusCardSettingsValue, TRIGGER_ROWS, TriggerKey

### Community 10 - "buildIncomingCarryOverFieldGroups"
Cohesion: 0.32
Nodes (8): buildIncomingCarryOverFieldGroups(), carryOverPolicyForCheckedFields(), carryOverPolicyForSave(), copyCarryOverPolicy(), flattenCarryOverFields(), inheritFieldsForSave(), selectedCarryOverFieldKeys(), toggleCarryOverField()

### Community 11 - "buildCarryOverFieldGroups"
Cohesion: 0.40
Nodes (6): buildCarryOverFieldGroups(), fieldOriginLabel(), pipelineBreakdownTargetIds(), pipelineCarryOverFields(), readVariableField(), upstreamPipelineIds()

### Community 12 - "stageAutomation"
Cohesion: 0.40
Nodes (6): buildStageAutomationForSave(), nullableExecutionWorkspaceMode(), nullableExecutionWorkspaceSettings(), nullableString(), pipelineAutomationTitleTemplate(), stageAutomation()

### Community 13 - "ProfileSettings"
Cohesion: 0.47
Nodes (4): deriveInitials(), ProfileSettings(), persistProfile(), syncSessionProfile()

### Community 14 - "validators/sidebar-preferences.ts"
Cohesion: 0.40
Nodes (4): sidebarOrderedIdSchema, sidebarOrderPreferenceSchema, UpsertSidebarOrderPreference, upsertSidebarOrderPreferenceSchema

### Community 17 - "computeStageForm"
Cohesion: 0.50
Nodes (4): approvalValue(), canonicalStageKind(), computeStageForm(), stageNewEntriesDisabled()

### Community 19 - "savedStageVariables"
Cohesion: 0.67
Nodes (3): savedStageVariables(), syncPipelineStageAutomationVariables(), toRoutineVariables()

## Knowledge Gaps
- **75 isolated node(s):** `instanceSettings`, `pluginCompanySettings`, `SETTING_DEFAULTS_ENV_KEY`, `DEFAULTABLE_GENERAL_SETTINGS`, `DefaultableGeneralSetting` (+70 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `instanceSettingsApi` connect `InstanceExperimentalSettings.tsx` to `PipelineSettings.tsx`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Why does `useHiddenSettings()` connect `useHiddenSettings` to `InstanceExperimentalSettings.tsx`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **What connects `instanceSettings`, `pluginCompanySettings`, `SETTING_DEFAULTS_ENV_KEY` to the rest of the system?**
  _75 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PipelineSettings.tsx` be split into smaller, more focused modules?**
  _Cohesion score 0.07459677419354839 - nodes in this community are weakly interconnected._
- **Should `services/instance-settings.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.11264367816091954 - nodes in this community are weakly interconnected._
- **Should `src/settings-visibility.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._
- **Should `PipelineSettings` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._