# Domain view — Domain › Flow › Step

**9 domains · 60 flows** from 3574 entry points.

Structure computed from the call graph: an entry point is a flow, its
call chain is the steps. Names are mechanical until a model labels them —
every step still points at a real file and line.

## packages · plugins

`packages/plugins` · 24 flows · 309 steps · event, http

**worker.ts** *(event)* — `packages/plugins/examples/plugin-authoring-smoke-example/src/worker.ts:1`
  → `definePlugin` — `packages/plugins/sdk/src/define-plugin.ts:520`
  → `info` — `cli/src/onboard-service.ts:19`
  → `register` — `server/src/routes/openapi.ts:462`
  → `runWorker` — `packages/plugins/sdk/src/worker-rpc-host.ts:273`
    → `zodToOpenApiSchema` — `server/src/routes/openapi.ts:313`
    → `startWorkerRpcHost` — `packages/plugins/sdk/src/worker-rpc-host.ts:315`
    → `isWorkerEntrypoint` — `packages/plugins/sdk/src/worker-rpc-host.ts:236`
      → `unwrapSchema` — `server/src/routes/openapi.ts:260`

**execLeaseUtility** *(http)* — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:93`
  → `executeInSandbox` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:87`
    → `randomToken` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:23`
    → `writeFile` — `packages/plugins/create-paperclip-plugin/src/index.ts:51`
    → `resolveExecutionTarget` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/sessions.ts:58`
    → `buildLoginShellScript` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:29`
    → `shellQuote` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/helpers.ts:37`
    → `coerceExecuteResult` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:67`
    → `isTimeoutError` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/helpers.ts:27`

**worker.ts** *(event)* — `packages/plugins/examples/plugin-file-browser-example/src/worker.ts:1`
  → `definePlugin` — `packages/plugins/sdk/src/define-plugin.ts:520`
  → `info` — `cli/src/onboard-service.ts:19`
  → `register` — `server/src/routes/openapi.ts:462`
  → `listComments` — `ui/src/api/approvals.ts:20`
  → `extractFilePaths` — `packages/plugins/examples/plugin-file-browser-example/src/worker.ts:48`
  → `warn` — `packages/shared/src/telemetry/client.ts:440`
  → `listWorkspaces` — `ui/src/api/projects.ts:32`
  → `sanitizeWorkspacePath` — `packages/plugins/examples/plugin-file-browser-example/src/worker.ts:16`

**ensureWorkspace** *(http)* — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:127`
  → `execLeaseUtility` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:93`
  → `requireZeroExit` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:116`
    → `executeInSandbox` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:87`
      → `randomToken` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:23`
      → `writeFile` — `packages/plugins/create-paperclip-plugin/src/index.ts:51`
      → `resolveExecutionTarget` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/sessions.ts:58`
      → `buildLoginShellScript` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:29`
      → `shellQuote` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/helpers.ts:37`

**worker.ts** *(event)* — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:1`
  → `definePlugin` — `packages/plugins/sdk/src/define-plugin.ts:520`
  → `register` — `server/src/routes/openapi.ts:462`
  → `pushRecord` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:84`
  → `registerEventHandlers` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:912`
  → `registerJobs` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:941`
  → `registerDataHandlers` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:257`
  → `registerActionHandlers` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:398`
  → `registerToolHandlers` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:828`

**writeSentinel** *(http)* — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:140`
  → `buildSentinelPath` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/helpers.ts:23`
  → `execLeaseUtility` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:93`
  → `shellQuote` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/helpers.ts:37`
  → `requireZeroExit` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:116`
    → `executeInSandbox` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:87`
      → `randomToken` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:23`
      → `writeFile` — `packages/plugins/create-paperclip-plugin/src/index.ts:51`
      → `resolveExecutionTarget` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/sessions.ts:58`

**registerDataHandlers** *(event)* — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:257`
  → `register` — `server/src/routes/openapi.ts:462`
  → `getConfig` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:95`
  → `list` — `packages/kv-demo-mcp-server/src/store.ts:47`
  → `listIssuesForCompany` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:241`
  → `listGoalsForCompany` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:245`
  → `readInstanceState` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:113`
  → `runtimeLaunchersSnapshot` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:253`
  → `recentRecordsSnapshot` — `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts:249`

**verifySentinel** *(http)* — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:180`
  → `execLeaseUtility` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts:93`
  → `shellQuote` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/helpers.ts:37`
  → `buildSentinelPath` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/helpers.ts:23`
    → `executeInSandbox` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:87`
      → `randomToken` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:23`
      → `writeFile` — `packages/plugins/create-paperclip-plugin/src/index.ts:51`
      → `resolveExecutionTarget` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/sessions.ts:58`
      → `buildLoginShellScript` — `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/exec.ts:29`

## routes · access.ts

`routes/access.ts` · 13 flows · 182 steps · http

**normalizeHeaderValue** *(http)* — `server/src/routes/access.ts:356`
  → `nonEmptyTrimmedString` — `server/src/routes/access.ts:474`
  → `isPlainObject` — `server/src/routes/access.ts:306`
  → `call` — `server/src/secrets/aws-secrets-manager-provider.ts:962`
    → `loadAwsCredentials` — `server/src/secrets/aws-secrets-manager-provider.ts:217`
    → `signAwsSecretsManagerRequest` — `server/src/secrets/aws-secrets-manager-provider.ts:163`
    → `classifyAwsProviderError` — `server/src/secrets/aws-secrets-manager-provider.ts:840`
    → `awsProviderSafeMessage` — `server/src/secrets/aws-secrets-manager-provider.ts:852`
    → `SecretProviderClientError` — `server/src/secrets/types.ts:77`

**extractHeaderEntries** *(http)* — `server/src/routes/access.ts:409`
  → `isPlainObject` — `server/src/routes/access.ts:306`
  → `nonEmptyTrimmedString` — `server/src/routes/access.ts:474`
  → `call` — `server/src/secrets/aws-secrets-manager-provider.ts:962`
    → `loadAwsCredentials` — `server/src/secrets/aws-secrets-manager-provider.ts:217`
    → `signAwsSecretsManagerRequest` — `server/src/secrets/aws-secrets-manager-provider.ts:163`
    → `classifyAwsProviderError` — `server/src/secrets/aws-secrets-manager-provider.ts:840`
    → `awsProviderSafeMessage` — `server/src/secrets/aws-secrets-manager-provider.ts:852`
    → `SecretProviderClientError` — `server/src/secrets/types.ts:77`

**normalizeHeaderMap** *(http)* — `server/src/routes/access.ts:456`
  → `extractHeaderEntries` — `server/src/routes/access.ts:409`
  → `normalizeHeaderValue` — `server/src/routes/access.ts:356`
    → `isPlainObject` — `server/src/routes/access.ts:306`
    → `nonEmptyTrimmedString` — `server/src/routes/access.ts:474`
    → `call` — `server/src/secrets/aws-secrets-manager-provider.ts:962`
      → `loadAwsCredentials` — `server/src/secrets/aws-secrets-manager-provider.ts:217`
      → `signAwsSecretsManagerRequest` — `server/src/secrets/aws-secrets-manager-provider.ts:163`
      → `classifyAwsProviderError` — `server/src/secrets/aws-secrets-manager-provider.ts:840`

**buildJoinDefaultsPayloadForAccept** *(http)* — `server/src/routes/access.ts:529`
  → `isPlainObject` — `server/src/routes/access.ts:306`
  → `nonEmptyTrimmedString` — `server/src/routes/access.ts:474`
  → `normalizeHeaderMap` — `server/src/routes/access.ts:456`
  → `headerMapHasKeyIgnoreCase` — `server/src/routes/access.ts:480`
  → `headerMapGetIgnoreCase` — `server/src/routes/access.ts:490`
  → `tokenFromAuthorizationHeader` — `server/src/routes/access.ts:503`
    → `extractHeaderEntries` — `server/src/routes/access.ts:409`
    → `normalizeHeaderValue` — `server/src/routes/access.ts:356`

**mergeJoinDefaultsPayloadForReplay** *(http)* — `server/src/routes/access.ts:591`
  → `isPlainObject` — `server/src/routes/access.ts:306`
  → `normalizeHeaderMap` — `server/src/routes/access.ts:456`
  → `call` — `server/src/secrets/aws-secrets-manager-provider.ts:962`
    → `extractHeaderEntries` — `server/src/routes/access.ts:409`
    → `normalizeHeaderValue` — `server/src/routes/access.ts:356`
    → `loadAwsCredentials` — `server/src/secrets/aws-secrets-manager-provider.ts:217`
    → `signAwsSecretsManagerRequest` — `server/src/secrets/aws-secrets-manager-provider.ts:163`
    → `classifyAwsProviderError` — `server/src/secrets/aws-secrets-manager-provider.ts:840`

**summarizeOpenClawGatewayDefaultsForLog** *(http)* — `server/src/routes/access.ts:672`
  → `isPlainObject` — `server/src/routes/access.ts:306`
  → `normalizeHeaderMap` — `server/src/routes/access.ts:456`
  → `headerMapGetIgnoreCase` — `server/src/routes/access.ts:490`
  → `tokenFromAuthorizationHeader` — `server/src/routes/access.ts:503`
  → `nonEmptyTrimmedString` — `server/src/routes/access.ts:474`
  → `parseBooleanLike` — `server/src/routes/access.ts:513`
  → `summarizeSecretForLog` — `server/src/routes/access.ts:660`
    → `extractHeaderEntries` — `server/src/routes/access.ts:409`

**normalizeAgentDefaultsForJoin** *(http)* — `server/src/routes/access.ts:709`
  → `isPlainObject` — `server/src/routes/access.ts:306`
  → `nonEmptyTrimmedString` — `server/src/routes/access.ts:474`
  → `isDefaultHermesDashboardRoot` — `server/src/routes/access.ts:333`
  → `normalizeHermesGatewayApiBaseUrl` — `server/src/routes/access.ts:321`
  → `isLoopbackHost` — `server/src/routes/access.ts:310`
  → `parseBooleanLike` — `server/src/routes/access.ts:513`
  → `normalizeHeaderMap` — `server/src/routes/access.ts:456`
  → `headerMapGetIgnoreCase` — `server/src/routes/access.ts:490`

**prepareAgentDefaultsPayloadForJoinPersistence** *(http)* — `server/src/routes/access.ts:1057`
  → `secretService` — `server/src/services/secrets.ts:921`
    → `authorizationService` — `server/src/services/authorization.ts:527`
    → `listSecretProviders` — `server/src/secrets/provider-registry.ts:28`
    → `checkSecretProviders` — `server/src/secrets/provider-registry.ts:32`
    → `unprocessable` — `server/src/errors.ts:32`
    → `getSecretProvider` — `server/src/secrets/provider-registry.ts:22`
    → `toDraftProviderVaultRuntimeConfig` — `server/src/services/secrets.ts:1231`
    → `remoteProviderHttpError` — `server/src/services/secrets.ts:282`

## commands · client

`commands/client` · 7 flows · 98 steps · cli

**registerAccessCommands** *(cli)* — `cli/src/commands/client/access.ts:26`
  → `addWhoamiCommand` — `cli/src/commands/client/access.ts:367`
  → `addCommonClientOptions` — `cli/src/commands/client/common.ts:30`
  → `action` — `cli/src/commands/worktree-merge-history-lib.ts:44`
  → `description` — `cli/src/commands/pipelines.ts:30`
  → `resolveCommandContext` — `cli/src/commands/client/common.ts:48`
  → `printOutput` — `cli/src/commands/client/common.ts:193`
  → `handleCommandError` — `cli/src/commands/client/common.ts:288`
  → `addSimpleGet` — `cli/src/commands/client/access.ts:388`

**addWhoamiCommand** *(cli)* — `cli/src/commands/client/access.ts:367`
  → `addCommonClientOptions` — `cli/src/commands/client/common.ts:30`
  → `action` — `cli/src/commands/worktree-merge-history-lib.ts:44`
  → `description` — `cli/src/commands/pipelines.ts:30`
  → `resolveCommandContext` — `cli/src/commands/client/common.ts:48`
  → `printOutput` — `cli/src/commands/client/common.ts:193`
  → `handleCommandError` — `cli/src/commands/client/common.ts:288`
    → `resolveProfile` — `cli/src/client/context.ts:208`
    → `resolveApiBase` — `cli/src/commands/client/common.ts:111`

**addSimpleGet** *(cli)* — `cli/src/commands/client/access.ts:388`
  → `addCommonClientOptions` — `cli/src/commands/client/common.ts:30`
  → `action` — `cli/src/commands/worktree-merge-history-lib.ts:44`
  → `description` — `cli/src/commands/pipelines.ts:30`
  → `resolveCommandContext` — `cli/src/commands/client/common.ts:48`
  → `printOutput` — `cli/src/commands/client/common.ts:193`
  → `handleCommandError` — `cli/src/commands/client/common.ts:288`
    → `resolveProfile` — `cli/src/client/context.ts:208`
    → `resolveApiBase` — `cli/src/commands/client/common.ts:111`

**addJsonPatch** *(cli)* — `cli/src/commands/client/access.ts:399`
  → `addCommonClientOptions` — `cli/src/commands/client/common.ts:30`
  → `action` — `cli/src/commands/worktree-merge-history-lib.ts:44`
  → `description` — `cli/src/commands/pipelines.ts:30`
  → `resolveCommandContext` — `cli/src/commands/client/common.ts:48`
  → `printOutput` — `cli/src/commands/client/common.ts:193`
  → `patch` — `cli/src/client/http.ts:77`
  → `parseJson` — `cli/src/commands/client/access.ts:517`
  → `handleCommandError` — `cli/src/commands/client/common.ts:288`

**addJsonPut** *(cli)* — `cli/src/commands/client/access.ts:410`
  → `addCommonClientOptions` — `cli/src/commands/client/common.ts:30`
  → `action` — `cli/src/commands/worktree-merge-history-lib.ts:44`
  → `description` — `cli/src/commands/pipelines.ts:30`
  → `resolveCommandContext` — `cli/src/commands/client/common.ts:48`
  → `printOutput` — `cli/src/commands/client/common.ts:193`
  → `parseJson` — `cli/src/commands/client/access.ts:517`
  → `handleCommandError` — `cli/src/commands/client/common.ts:288`
    → `resolveProfile` — `cli/src/client/context.ts:208`

**addCompanyList** *(cli)* — `cli/src/commands/client/access.ts:421`
  → `addCommonClientOptions` — `cli/src/commands/client/common.ts:30`
  → `action` — `cli/src/commands/worktree-merge-history-lib.ts:44`
  → `description` — `cli/src/commands/pipelines.ts:30`
  → `resolveCommandContext` — `cli/src/commands/client/common.ts:48`
  → `printOutput` — `cli/src/commands/client/common.ts:193`
  → `apiPath` — `cli/src/commands/client/common.ts:124`
  → `handleCommandError` — `cli/src/commands/client/common.ts:288`
    → `resolveProfile` — `cli/src/client/context.ts:208`

**addCompanyPut** *(cli)* — `cli/src/commands/client/access.ts:435`
  → `addCommonClientOptions` — `cli/src/commands/client/common.ts:30`
  → `action` — `cli/src/commands/worktree-merge-history-lib.ts:44`
  → `description` — `cli/src/commands/pipelines.ts:30`
  → `resolveCommandContext` — `cli/src/commands/client/common.ts:48`
  → `printOutput` — `cli/src/commands/client/common.ts:193`
  → `apiPath` — `cli/src/commands/client/common.ts:124`
  → `parseJson` — `cli/src/commands/client/access.ts:517`
  → `handleCommandError` — `cli/src/commands/client/common.ts:288`

## cli · client

`cli/client` · 6 flows · 84 steps · cli

**readBoardAuthStore** *(cli)* — `cli/src/client/board-auth.ts:74`
  → `resolveBoardAuthStorePath` — `cli/src/client/board-auth.ts:68`
  → `defaultBoardAuthStore` — `cli/src/client/board-auth.ts:48`
  → `toStringOrNull` — `cli/src/client/board-auth.ts:55`
  → `normalizeApiBase` — `cli/src/client/board-auth.ts:59`
    → `resolveDefaultCliAuthPath` — `cli/src/config/home.ts:35`
    → `replace` — `server/src/services/company-skill-policy.ts:189`
      → `resolvePaperclipHomeDir` — `packages/shared/src/home-paths.ts:16`
      → `conflict` — `server/src/errors.ts:28`

**getStoredBoardCredential** *(cli)* — `cli/src/client/board-auth.ts:111`
  → `readBoardAuthStore` — `cli/src/client/board-auth.ts:74`
  → `normalizeApiBase` — `cli/src/client/board-auth.ts:59`
    → `resolveBoardAuthStorePath` — `cli/src/client/board-auth.ts:68`
    → `defaultBoardAuthStore` — `cli/src/client/board-auth.ts:48`
    → `toStringOrNull` — `cli/src/client/board-auth.ts:55`
    → `replace` — `server/src/services/company-skill-policy.ts:189`
      → `resolveDefaultCliAuthPath` — `cli/src/config/home.ts:35`
      → `conflict` — `server/src/errors.ts:28`

**setStoredBoardCredential** *(cli)* — `cli/src/client/board-auth.ts:116`
  → `normalizeApiBase` — `cli/src/client/board-auth.ts:59`
  → `readBoardAuthStore` — `cli/src/client/board-auth.ts:74`
  → `writeBoardAuthStore` — `cli/src/client/board-auth.ts:105`
    → `replace` — `server/src/services/company-skill-policy.ts:189`
    → `resolveBoardAuthStorePath` — `cli/src/client/board-auth.ts:68`
    → `defaultBoardAuthStore` — `cli/src/client/board-auth.ts:48`
    → `toStringOrNull` — `cli/src/client/board-auth.ts:55`
      → `conflict` — `server/src/errors.ts:28`

**removeStoredBoardCredential** *(cli)* — `cli/src/client/board-auth.ts:138`
  → `normalizeApiBase` — `cli/src/client/board-auth.ts:59`
  → `readBoardAuthStore` — `cli/src/client/board-auth.ts:74`
  → `writeBoardAuthStore` — `cli/src/client/board-auth.ts:105`
    → `replace` — `server/src/services/company-skill-policy.ts:189`
    → `resolveBoardAuthStorePath` — `cli/src/client/board-auth.ts:68`
    → `defaultBoardAuthStore` — `cli/src/client/board-auth.ts:48`
    → `toStringOrNull` — `cli/src/client/board-auth.ts:55`
      → `conflict` — `server/src/errors.ts:28`

**loginBoardCli** *(cli)* — `cli/src/client/board-auth.ts:201`
  → `normalizeApiBase` — `cli/src/client/board-auth.ts:59`
  → `buildCliCommandLabel` — `cli/src/client/command-label.ts:1`
  → `isTruthyEnv` — `cli/src/client/board-auth.ts:63`
  → `openUrl` — `cli/src/client/board-auth.ts:177`
  → `setStoredBoardCredential` — `cli/src/client/board-auth.ts:116`
  → `sleep` — `cli/src/client/board-auth.ts:147`
    → `replace` — `server/src/services/company-skill-policy.ts:189`
    → `resolve` — `ui/src/api/file-resources.ts:85`

**buildConnectionErrorMessage** *(cli)* — `cli/src/client/http.ts:216`
  → `buildHealthCheckUrl` — `cli/src/client/http.ts:243`
  → `replace` — `server/src/services/company-skill-policy.ts:189`
    → `conflict` — `server/src/errors.ts:28`
    → `update` — `ui/storybook/.storybook/node-crypto-browser-shim.ts:14`
    → `insert` — `server/src/services/batch-insert.ts:22`
    → `logActivity` — `server/src/services/activity-log.ts:217`
      → `HttpError` — `server/src/errors.ts:1`
      → `persistActivity` — `server/src/services/activity-log.ts:160`

## services · cron.ts

`services/cron.ts` · 4 flows · 13 steps · cron

**nextCronTickFromExpression** *(cron)* — `server/src/services/cron.ts:329`
  → `parseCron` — `server/src/services/cron.ts:204`
  → `nextCronTick` — `server/src/services/cron.ts:253`
    → `parseField` — `server/src/services/cron.ts:70`
    → `advanceToNextMonth` — `server/src/services/cron.ts:356`
    → `findNext` — `server/src/services/cron.ts:345`
      → `validateBounds` — `server/src/services/cron.ts:178`

**validateCron** *(cron)* — `server/src/services/cron.ts:233`
  → `parseCron` — `server/src/services/cron.ts:204`
    → `parseField` — `server/src/services/cron.ts:70`
      → `validateBounds` — `server/src/services/cron.ts:178`

**parseCron** *(cron)* — `server/src/services/cron.ts:204`
  → `parseField` — `server/src/services/cron.ts:70`
    → `validateBounds` — `server/src/services/cron.ts:178`

**nextCronTick** *(cron)* — `server/src/services/cron.ts:253`
  → `advanceToNextMonth` — `server/src/services/cron.ts:356`
  → `findNext` — `server/src/services/cron.ts:345`

## commands · auth-bootstrap-ceo.ts

`commands/auth-bootstrap-ceo.ts` · 2 flows · 28 steps · cli

**resolveBaseUrl** *(cli)* — `cli/src/commands/auth-bootstrap-ceo.ts:32`
  → `replace` — `server/src/services/company-skill-policy.ts:189`
  → `readConfig` — `cli/src/config/store.ts:91`
  → `inferBindModeFromHost` — `packages/shared/src/network-bind.ts:21`
    → `conflict` — `server/src/errors.ts:28`
    → `update` — `ui/storybook/.storybook/node-crypto-browser-shim.ts:14`
    → `insert` — `server/src/services/batch-insert.ts:22`
    → `logActivity` — `server/src/services/activity-log.ts:217`
    → `resolveConfigPath` — `cli/src/config/store.ts:34`

**bootstrapCeoInvite** *(cli)* — `cli/src/commands/auth-bootstrap-ceo.ts:54`
  → `resolveConfigPath` — `cli/src/config/store.ts:34`
  → `loadPaperclipEnvFile` — `cli/src/config/env.ts:51`
  → `readConfig` — `cli/src/config/store.ts:91`
  → `error` — `cli/src/commands/service.ts:11`
  → `info` — `cli/src/onboard-service.ts:19`
  → `resolveDbUrl` — `cli/src/commands/auth-bootstrap-ceo.ts:18`
  → `createDb` — `packages/db/src/client.ts:118`
  → `update` — `ui/storybook/.storybook/node-crypto-browser-shim.ts:14`

## commands · channels.ts

`commands/channels.ts` · 2 flows · 28 steps · cli

**collectChannelState** *(cli)* — `cli/src/commands/channels.ts:63`
  → `resolvePublishedVersion` — `cli/src/commands/install.ts:120`
    → `runCommand` — `cli/src/commands/run.ts:39`
    → `parseResolvedVersion` — `cli/src/commands/install.ts:108`
      → `resolvePaperclipInstanceId` — `packages/shared/src/home-paths.ts:22`
      → `assertForegroundRunAllowed` — `cli/src/services/service-manager.ts:305`
      → `resolvePaperclipHomeDir` — `packages/shared/src/home-paths.ts:16`
      → `describeLocalInstancePaths` — `cli/src/config/home.ts:59`
      → `resolveConfigPath` — `cli/src/config/store.ts:34`

**channelsCommand** *(cli)* — `cli/src/commands/channels.ts:80`
  → `collectChannelState` — `cli/src/commands/channels.ts:63`
  → `channelForVersion` — `cli/src/commands/channels.ts:54`
    → `resolvePublishedVersion` — `cli/src/commands/install.ts:120`
      → `runCommand` — `cli/src/commands/run.ts:39`
      → `parseResolvedVersion` — `cli/src/commands/install.ts:108`
        → `resolvePaperclipInstanceId` — `packages/shared/src/home-paths.ts:22`
        → `assertForegroundRunAllowed` — `cli/src/services/service-manager.ts:305`
        → `resolvePaperclipHomeDir` — `packages/shared/src/home-paths.ts:16`

## cli · checks

`cli/checks` · 1 flows · 14 steps · cli

**agentJwtSecretCheck** *(cli)* — `cli/src/checks/agent-jwt-secret-check.ts:9`
  → `readAgentJwtSecretFromEnv` — `cli/src/config/env.ts:63`
  → `resolveAgentJwtEnvFile` — `cli/src/config/env.ts:47`
  → `readAgentJwtSecretFromEnvFile` — `cli/src/config/env.ts:69`
  → `ensureAgentJwtSecret` — `cli/src/config/env.ts:78`
    → `loadAgentJwtEnvFile` — `cli/src/config/env.ts:55`
    → `resolveEnvFilePath` — `cli/src/config/env.ts:10`
    → `isNonEmpty` — `cli/src/config/env.ts:15`
    → `parseEnvFile` — `cli/src/config/env.ts:19`

## commands · allowed-hostname.ts

`commands/allowed-hostname.ts` · 1 flows · 14 steps · cli

**addAllowedHostname** *(cli)* — `cli/src/commands/allowed-hostname.ts:6`
  → `resolveConfigPath` — `cli/src/config/store.ts:34`
  → `readConfig` — `cli/src/config/store.ts:91`
  → `error` — `cli/src/commands/service.ts:11`
  → `normalizeHostnameInput` — `cli/src/config/hostnames.ts:1`
  → `writeConfig` — `cli/src/config/store.ts:186`
  → `info` — `cli/src/onboard-service.ts:19`
  → `success` — `cli/src/onboard-service.ts:20`
  → `message` — `packages/db/src/check-migration-safety.ts:29`
