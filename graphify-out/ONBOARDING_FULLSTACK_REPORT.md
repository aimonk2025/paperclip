# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 28 files · ~38,710 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 252 nodes · 413 edges · 14 communities (12 shown, 2 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- onboarding-motion.ts
- OnboardingWizard.tsx
- onboard.ts
- OnboardingWizardInner
- ConnectModelPreview.tsx
- onboardingSeedService
- onboarding-first-task-assets.ts
- onboarding-route.ts
- OnboardingChat.tsx
- validators/onboarding-seed.ts
- SleepingZs.tsx
- agent-onboarding-prompt.ts
- onboarding-auto-open.ts
- company_onboarding_seeds.ts

## God Nodes (most connected - your core abstractions)
1. `OnboardingWizardInner()` - 32 edges
2. `onboardingSeedService()` - 10 edges
3. `applyWithin()` - 10 edges
4. `handleGiveHeartbeat()` - 10 edges
5. `onboard()` - 9 edges
6. `handleLaunchToDashboard()` - 8 edges
7. `quickstartDefaultsFromEnv()` - 6 edges
8. `loadFirstTaskAsset()` - 6 edges
9. `buildAdapterConfig()` - 6 edges
10. `handoffToOnboardedService()` - 5 edges
11. `renderOnboardingFirstTaskGreeting()` - 5 edges
12. `apiKeyEnvKeyFor()` - 5 edges
13. `managedBindingForStep()` - 5 edges
14. `runAdapterEnvironmentTest()` - 5 edges
15. `selectDefaultCompanyGoalId()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `onboardingSeedRoutes()` --calls--> `onboardingSeedService()`  [EXTRACTED]
  server/src/routes/onboarding-seed.ts → server/src/services/onboarding-seed.ts
- `renderOnboardingGreeting()` --calls--> `renderOnboardingFirstTaskGreeting()`  [EXTRACTED]
  server/src/services/onboarding-greeting.ts → server/src/services/onboarding-first-task-assets.ts
- `OnboardingWizardInner()` --calls--> `beatDelay()`  [EXTRACTED]
  ui/src/components/OnboardingWizard.tsx → ui/src/components/onboarding/onboarding-motion.ts
- `OnboardingWizardInner()` --calls--> `useSavedProviderKeys()`  [EXTRACTED]
  ui/src/components/OnboardingWizard.tsx → ui/src/components/onboarding/SavedProviderKeySelect.tsx
- `OnboardingWizardInner()` --calls--> `agentArcStepFor()`  [EXTRACTED]
  ui/src/components/OnboardingWizard.tsx → ui/src/components/onboarding/Stepper.tsx

## Import Cycles
- None detected.

## Communities (14 total, 2 thin omitted)

### Community 0 - "onboarding-motion.ts"
Cohesion: 0.06
Nodes (37): AgentPreview(), FooterNav(), FooterPrimaryIcon, beatDelay(), CANVAS_CONTENT_ENTER, CANVAS_CONTENT_EXIT, CANVAS_CONTENT_TRAVEL, CANVAS_EASE (+29 more)

### Community 1 - "OnboardingWizard.tsx"
Cohesion: 0.08
Nodes (24): SavedProviderKeySelect(), useSavedProviderKeys(), AGENT_ARC_STEP_LABELS, AGENT_ARC_TOTAL_STEPS, AGENT_ARC_WIZARD_STEPS, agentArcStepFor(), ONBOARDING_STEP_LABELS, ONBOARDING_WIZARD_STEPS (+16 more)

### Community 2 - "onboard.ts"
Cohesion: 0.10
Nodes (27): canCreateBootstrapInviteImmediately(), describeServerBinding(), isEphemeralNpxExecution(), onboard(), ONBOARD_ENV_KEYS, OnboardDefaults, OnboardOptions, parseBooleanFromEnv() (+19 more)

### Community 3 - "OnboardingWizardInner"
Cohesion: 0.13
Nodes (27): adapterConfigHasAnthropicApiKey(), apiKeyEnvKeyFor(), blocksAgentCreate(), isEnvRecord(), OnboardingWizardInner(), buildAdapterConfig(), canCommitCreatedCompany(), handleClose() (+19 more)

### Community 4 - "ConnectModelPreview.tsx"
Cohesion: 0.09
Nodes (18): CredentialControl, MODEL_SOURCES, CredentialModeLink(), LINK_LABEL, OTHER_MODE, CREDENTIAL_TAG_LABEL, CredentialMode, ModelSource (+10 more)

### Community 5 - "onboardingSeedService"
Cohesion: 0.20
Nodes (15): onboardingSeedRoutes(), ONBOARDING_SEED_PROJECT_NAME, OnboardingSeedApplication, OnboardingSeedAuditActor, onboardingSeedService(), apply(), applyWithin(), goalStillExists() (+7 more)

### Community 6 - "onboarding-first-task-assets.ts"
Cohesion: 0.19
Nodes (15): buildOnboardingFirstAgentInstructionsBundle(), buildOnboardingFirstTaskBrief(), buildOnboardingFirstTaskOpeningQuestion(), fillFirstTaskPlaceholders(), loadFirstTaskAsset(), ONBOARDING_FIRST_TASK_OPENING_INTERVIEW_OPTION_ID, ONBOARDING_FIRST_TASK_OPENING_QUESTION_ID, ONBOARDING_FIRST_TASK_OPENING_TASK_OPTION_ID (+7 more)

### Community 7 - "onboarding-route.ts"
Cohesion: 0.19
Nodes (12): canGoBackFromOnboardingStep(), canJumpToOnboardingStep(), companyPrefixFromOnboardingPath(), ExistingCompanyOnboardingStep, isOnboardingPath(), ONBOARDING_AGENT_STEP, ONBOARDING_MISSION_STEP, OnboardingRouteCompany (+4 more)

### Community 8 - "OnboardingChat.tsx"
Cohesion: 0.29
Nodes (8): detectHiringPlan(), getCyclingMessage(), getRunStatusMessage(), OnboardingChat(), OnboardingChatProps, QUEUED_MESSAGES, RUNNING_MESSAGES, WAITING_MESSAGES

### Community 9 - "validators/onboarding-seed.ts"
Cohesion: 0.25
Nodes (7): AGENT_NAME_MAX_LENGTH, AGENT_ROLE_MAX_LENGTH, ApplyOnboardingSeed, applyOnboardingSeedSchema, FIRST_TASK_DETAILS_MAX_LENGTH, FIRST_TASK_TITLE_MAX_LENGTH, MISSION_MAX_LENGTH

### Community 10 - "SleepingZs.tsx"
Cohesion: 0.32
Nodes (7): nextFlight(), randomBetween(), SleepingZs(), SleepyZ(), Z_TIERS, ZFlight, ZTier

### Community 11 - "agent-onboarding-prompt.ts"
Cohesion: 0.60
Nodes (4): AgentOnboardingPromptInput, buildAgentOnboardingPrompt(), buildCandidateOnboardingUrls(), buildResolutionTestUrl()

## Knowledge Gaps
- **80 isolated node(s):** `SetupMode`, `OnboardOptions`, `OnboardDefaults`, `ONBOARD_ENV_KEYS`, `OnboardServiceOptions` (+75 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `OnboardingWizardInner()` connect `OnboardingWizardInner` to `onboarding-motion.ts`, `OnboardingWizard.tsx`, `onboarding-route.ts`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Why does `beatDelay()` connect `onboarding-motion.ts` to `OnboardingWizard.tsx`, `OnboardingWizardInner`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **Why does `resolveRouteOnboardingOptions()` connect `onboarding-route.ts` to `OnboardingWizard.tsx`, `OnboardingWizardInner`?**
  _High betweenness centrality (0.006) - this node is a cross-community bridge._
- **What connects `SetupMode`, `OnboardOptions`, `OnboardDefaults` to the rest of the system?**
  _80 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `onboarding-motion.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.05512820512820513 - nodes in this community are weakly interconnected._
- **Should `OnboardingWizard.tsx` be split into smaller, more focused modules?**
  _Cohesion score 0.0773109243697479 - nodes in this community are weakly interconnected._
- **Should `onboard.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.10080645161290322 - nodes in this community are weakly interconnected._