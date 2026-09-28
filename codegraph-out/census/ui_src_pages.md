# Capability census — pages

**21 files · 1,808 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 7 |
| validates input | 2 |
| retries | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `tools/profiles/profile-model.ts` | 399 | ToolCapability, toolCapability, CAPABILITY_LABEL, AppGroup, groupCatalogByApp +18 |
| `apps/gateways/gateway-helpers.ts` | 209 | TOKEN_EXPIRING_WINDOW_DAYS, TokenStatus, toDate, maskedTokenLabel, tokenStatus +13 |
| `TeamCatalog.fixtures.ts` | 166 | sampleTeam, optionalTeam, warnTeam, outOfDateInstalledState, currentInstalledState +2 |
| `StatusCards/format.ts` | 156 | formatTokens, formatCents, StatusCardRollup, rollupUpdates, rollupUpdatesToday +4 |
| `agent-skills/agent-skill-source.ts` | 118 | AgentSkillSourceMeta, buildAgentSkillSourceMeta |
| `secrets/secret-path.ts` | 112 | SecretPathRow, SecretPathFolder, SecretPathBreadcrumb, SecretPathListing, getSecretPathRowName +5 |
| `tools/smoke-lab-matrix.ts` | 108 | SMOKE_PATH_LABELS, LifecycleStage, LIFECYCLE_STAGES, matchLifecycleStage, CellStatus +6 |
| `tools/profiles/useProfilesData.ts` | 83 | useProfilesData |
| `tools/tool-tabs.ts` | 55 | ADVANCED_TOOLS_BASE, advancedTabHref, ADVANCED_TABS, DEVELOPER_TABS, TOOL_TABS +3 |
| `tools/profiles/profile-summary.ts` | 55 | allowsLabel, AssignedLabel, assignedLabel, STATUS_LABEL, isDraft |
| `tools/profiles/wizard-draft.ts` | 45 | WizardStep, WizardMeta, readWizardMeta, withWizardMeta, resumeStep |
| `agent-skills/agent-skill-filter.ts` | 44 | AgentSkillSearchFields, buildAgentSkillHaystack, agentSkillMatchesSearch, filterAgentSkills |
| `apps/app-detail/types.ts` | 41 | AccessDraft, AppDetailSectionProps, ActivityPanelProps |
| `apps/google-sheets.ts` | 37 | parseGoogleSheetIds, googleSheetsConfigWithAllowlist |
| `apps/app-definition-display.ts` | 36 | AppGalleryDisplayEntry, appDefinitionSlug, appDefinitionName, appDefinitionDescription, appDefinitionLogoUrl +1 |
| `apps/app-tabs.ts` | 35 | APP_TABS, AppTabKey, CONNECTED_ONLY_APP_TABS, appTabHref, appApplicationTabHref +2 |
| `apps/gateways/gateway-tabs.ts` | 28 | GATEWAY_TABS, GatewayTabKey, gatewayTabHref, isGatewayTabKey, gatewayTabLabel |
| `StatusCards/types.ts` | 25 | StatusCardView |
| `apps/useReviewCount.ts` | 22 | useReviewCount |
| `secrets/my-value-state.ts` | 20 | myValueState |
| `apps/app-connect-policy.ts` | 14 | MCP_DIRECT_OAUTH_CONNECT_SLUGS, isMcpDirectOAuthConnectSlug, appSourceConnectHref, canEnterAppsConnect |

## Contract members — each is a capability

**AppDetailSectionProps** (14 members)

```
connectionId, connection, appName, galleryEntry, catalog, active, readOnly, canChange, quarantined, enabledIds, askFirstIds, access, agents, pending
```

**ActivityPanelProps** (9 members)

```
events, lifecycleEvents, issues, actionRequests, loading, agents, connectionId, appName, userLabelById
```

**AgentSkillSearchFields** (6 members)

```
name, slug, author, tagline, description, categories
```

**GatewayAppRow** (5 members)

```
application, connection, toolCount, needsAttention, attentionReason
```

**AppGroup** (5 members)

```
appKey, applicationId, connectionId, name, tools
```

**AdvancedRule** (5 members)

```
id, kind, value, riskLevel, effect
```

**StatusCardView** (4 members)

```
summaryBody, watchedIssueCount, todayTokens, todayCostCents
```

**SecretPathFolder** (4 members)

```
name, path, secretCount, folderCount
```

## Decision ledger — fill this in, leave nothing blank

| Capability | KEEP / DROP | Reason |
|---|---|---|
| authenticates | | |
| retries | | |
| validates input | | |
| AppDetailSectionProps.connectionId | | |
| AppDetailSectionProps.connection | | |
| AppDetailSectionProps.appName | | |
| AppDetailSectionProps.galleryEntry | | |
| AppDetailSectionProps.catalog | | |
| AppDetailSectionProps.active | | |
| AppDetailSectionProps.readOnly | | |
| AppDetailSectionProps.canChange | | |
| AppDetailSectionProps.quarantined | | |
| AppDetailSectionProps.enabledIds | | |
| AppDetailSectionProps.askFirstIds | | |
| AppDetailSectionProps.access | | |
| AppDetailSectionProps.agents | | |
| AppDetailSectionProps.pending | | |
| ActivityPanelProps.events | | |
| ActivityPanelProps.lifecycleEvents | | |
| ActivityPanelProps.issues | | |
| ActivityPanelProps.actionRequests | | |
| ActivityPanelProps.loading | | |
| ActivityPanelProps.agents | | |
| ActivityPanelProps.connectionId | | |
| ActivityPanelProps.appName | | |
| ActivityPanelProps.userLabelById | | |
| AgentSkillSearchFields.name | | |
| AgentSkillSearchFields.slug | | |
| AgentSkillSearchFields.author | | |
| AgentSkillSearchFields.tagline | | |
| AgentSkillSearchFields.description | | |
| AgentSkillSearchFields.categories | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
