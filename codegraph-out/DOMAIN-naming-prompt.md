# Name these domains and flows

The structure below was computed from the call graph — entry points and
their real call chains. **Do not change it.** Your job is naming only.

Return JSON:
```json
{"domains":{"<domain-id>":{"name":"Order Management","summary":"2 sentences","entities":["Order","Payment"]}},
 "flows":{"<flow-id>":{"name":"Create Order","summary":"one sentence"}}}
```

Rules:
- Use the vocabulary a person in this business would say, not the code's.
- If a group is plumbing, not business (config, logging, health checks),
  name it plainly as infrastructure. Do not invent a business meaning.
- Never rename an id. Keys must match exactly.

---

## `domain:packages-plugins`  (24 flows · 309 steps · event, http)
directory: `packages/plugins`
- `flow:worker-ts` — entry `worker.ts` (event) in `packages/plugins/examples/plugin-authoring-smoke-example/src/worker.ts`
  steps: definePlugin → info → register → runWorker → zodToOpenApiSchema → startWorkerRpcHost → isWorkerEntrypoint
- `flow:execleaseutility` — entry `execLeaseUtility` (http) in `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts`
  steps: executeInSandbox → randomToken → writeFile → resolveExecutionTarget → buildLoginShellScript → shellQuote → coerceExecuteResult
- `flow:worker-ts` — entry `worker.ts` (event) in `packages/plugins/examples/plugin-file-browser-example/src/worker.ts`
  steps: definePlugin → info → register → listComments → extractFilePaths → warn → listWorkspaces
- `flow:ensureworkspace` — entry `ensureWorkspace` (http) in `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts`
  steps: execLeaseUtility → requireZeroExit → executeInSandbox → randomToken → writeFile → resolveExecutionTarget → buildLoginShellScript
- `flow:worker-ts` — entry `worker.ts` (event) in `packages/plugins/examples/plugin-kitchen-sink-example/src/worker.ts`
  steps: definePlugin → register → pushRecord → registerEventHandlers → registerJobs → registerDataHandlers → registerActionHandlers
- `flow:writesentinel` — entry `writeSentinel` (http) in `packages/plugins/sandbox-providers/cloudflare/bridge-template/src/routes.ts`
  steps: buildSentinelPath → execLeaseUtility → shellQuote → requireZeroExit → executeInSandbox → randomToken → writeFile

## `domain:routes-access-ts`  (13 flows · 182 steps · http)
directory: `routes/access.ts`
- `flow:normalizeheadervalue` — entry `normalizeHeaderValue` (http) in `server/src/routes/access.ts`
  steps: nonEmptyTrimmedString → isPlainObject → call → loadAwsCredentials → signAwsSecretsManagerRequest → classifyAwsProviderError → awsProviderSafeMessage
- `flow:extractheaderentries` — entry `extractHeaderEntries` (http) in `server/src/routes/access.ts`
  steps: isPlainObject → nonEmptyTrimmedString → call → loadAwsCredentials → signAwsSecretsManagerRequest → classifyAwsProviderError → awsProviderSafeMessage
- `flow:normalizeheadermap` — entry `normalizeHeaderMap` (http) in `server/src/routes/access.ts`
  steps: extractHeaderEntries → normalizeHeaderValue → isPlainObject → nonEmptyTrimmedString → call → loadAwsCredentials → signAwsSecretsManagerRequest
- `flow:buildjoindefaultspayloadforaccept` — entry `buildJoinDefaultsPayloadForAccept` (http) in `server/src/routes/access.ts`
  steps: isPlainObject → nonEmptyTrimmedString → normalizeHeaderMap → headerMapHasKeyIgnoreCase → headerMapGetIgnoreCase → tokenFromAuthorizationHeader → extractHeaderEntries
- `flow:mergejoindefaultspayloadforreplay` — entry `mergeJoinDefaultsPayloadForReplay` (http) in `server/src/routes/access.ts`
  steps: isPlainObject → normalizeHeaderMap → call → extractHeaderEntries → normalizeHeaderValue → loadAwsCredentials → signAwsSecretsManagerRequest
- `flow:summarizeopenclawgatewaydefaultsforlog` — entry `summarizeOpenClawGatewayDefaultsForLog` (http) in `server/src/routes/access.ts`
  steps: isPlainObject → normalizeHeaderMap → headerMapGetIgnoreCase → tokenFromAuthorizationHeader → nonEmptyTrimmedString → parseBooleanLike → summarizeSecretForLog

## `domain:commands-client`  (7 flows · 98 steps · cli)
directory: `commands/client`
- `flow:registeraccesscommands` — entry `registerAccessCommands` (cli) in `cli/src/commands/client/access.ts`
  steps: addWhoamiCommand → addCommonClientOptions → action → description → resolveCommandContext → printOutput → handleCommandError
- `flow:addwhoamicommand` — entry `addWhoamiCommand` (cli) in `cli/src/commands/client/access.ts`
  steps: addCommonClientOptions → action → description → resolveCommandContext → printOutput → handleCommandError → resolveProfile
- `flow:addsimpleget` — entry `addSimpleGet` (cli) in `cli/src/commands/client/access.ts`
  steps: addCommonClientOptions → action → description → resolveCommandContext → printOutput → handleCommandError → resolveProfile
- `flow:addjsonpatch` — entry `addJsonPatch` (cli) in `cli/src/commands/client/access.ts`
  steps: addCommonClientOptions → action → description → resolveCommandContext → printOutput → patch → parseJson
- `flow:addjsonput` — entry `addJsonPut` (cli) in `cli/src/commands/client/access.ts`
  steps: addCommonClientOptions → action → description → resolveCommandContext → printOutput → parseJson → handleCommandError
- `flow:addcompanylist` — entry `addCompanyList` (cli) in `cli/src/commands/client/access.ts`
  steps: addCommonClientOptions → action → description → resolveCommandContext → printOutput → apiPath → handleCommandError

## `domain:cli-client`  (6 flows · 84 steps · cli)
directory: `cli/client`
- `flow:readboardauthstore` — entry `readBoardAuthStore` (cli) in `cli/src/client/board-auth.ts`
  steps: resolveBoardAuthStorePath → defaultBoardAuthStore → toStringOrNull → normalizeApiBase → resolveDefaultCliAuthPath → replace → resolvePaperclipHomeDir
- `flow:getstoredboardcredential` — entry `getStoredBoardCredential` (cli) in `cli/src/client/board-auth.ts`
  steps: readBoardAuthStore → normalizeApiBase → resolveBoardAuthStorePath → defaultBoardAuthStore → toStringOrNull → replace → resolveDefaultCliAuthPath
- `flow:setstoredboardcredential` — entry `setStoredBoardCredential` (cli) in `cli/src/client/board-auth.ts`
  steps: normalizeApiBase → readBoardAuthStore → writeBoardAuthStore → replace → resolveBoardAuthStorePath → defaultBoardAuthStore → toStringOrNull
- `flow:removestoredboardcredential` — entry `removeStoredBoardCredential` (cli) in `cli/src/client/board-auth.ts`
  steps: normalizeApiBase → readBoardAuthStore → writeBoardAuthStore → replace → resolveBoardAuthStorePath → defaultBoardAuthStore → toStringOrNull
- `flow:loginboardcli` — entry `loginBoardCli` (cli) in `cli/src/client/board-auth.ts`
  steps: normalizeApiBase → buildCliCommandLabel → isTruthyEnv → openUrl → setStoredBoardCredential → sleep → replace
- `flow:buildconnectionerrormessage` — entry `buildConnectionErrorMessage` (cli) in `cli/src/client/http.ts`
  steps: buildHealthCheckUrl → replace → conflict → update → insert → logActivity → HttpError

## `domain:services-cron-ts`  (4 flows · 13 steps · cron)
directory: `services/cron.ts`
- `flow:nextcrontickfromexpression` — entry `nextCronTickFromExpression` (cron) in `server/src/services/cron.ts`
  steps: parseCron → nextCronTick → parseField → advanceToNextMonth → findNext → validateBounds
- `flow:validatecron` — entry `validateCron` (cron) in `server/src/services/cron.ts`
  steps: parseCron → parseField → validateBounds
- `flow:parsecron` — entry `parseCron` (cron) in `server/src/services/cron.ts`
  steps: parseField → validateBounds
- `flow:nextcrontick` — entry `nextCronTick` (cron) in `server/src/services/cron.ts`
  steps: advanceToNextMonth → findNext

## `domain:commands-auth-bootstrap-ceo-ts`  (2 flows · 28 steps · cli)
directory: `commands/auth-bootstrap-ceo.ts`
- `flow:resolvebaseurl` — entry `resolveBaseUrl` (cli) in `cli/src/commands/auth-bootstrap-ceo.ts`
  steps: replace → readConfig → inferBindModeFromHost → conflict → update → insert → logActivity
- `flow:bootstrapceoinvite` — entry `bootstrapCeoInvite` (cli) in `cli/src/commands/auth-bootstrap-ceo.ts`
  steps: resolveConfigPath → loadPaperclipEnvFile → readConfig → error → info → resolveDbUrl → createDb

## `domain:commands-channels-ts`  (2 flows · 28 steps · cli)
directory: `commands/channels.ts`
- `flow:collectchannelstate` — entry `collectChannelState` (cli) in `cli/src/commands/channels.ts`
  steps: resolvePublishedVersion → runCommand → parseResolvedVersion → resolvePaperclipInstanceId → assertForegroundRunAllowed → resolvePaperclipHomeDir → describeLocalInstancePaths
- `flow:channelscommand` — entry `channelsCommand` (cli) in `cli/src/commands/channels.ts`
  steps: collectChannelState → channelForVersion → resolvePublishedVersion → runCommand → parseResolvedVersion → resolvePaperclipInstanceId → assertForegroundRunAllowed

## `domain:cli-checks`  (1 flows · 14 steps · cli)
directory: `cli/checks`
- `flow:agentjwtsecretcheck` — entry `agentJwtSecretCheck` (cli) in `cli/src/checks/agent-jwt-secret-check.ts`
  steps: readAgentJwtSecretFromEnv → resolveAgentJwtEnvFile → readAgentJwtSecretFromEnvFile → ensureAgentJwtSecret → loadAgentJwtEnvFile → resolveEnvFilePath → isNonEmpty

## `domain:commands-allowed-hostname-ts`  (1 flows · 14 steps · cli)
directory: `commands/allowed-hostname.ts`
- `flow:addallowedhostname` — entry `addAllowedHostname` (cli) in `cli/src/commands/allowed-hostname.ts`
  steps: resolveConfigPath → readConfig → error → normalizeHostnameInput → writeConfig → info → success
