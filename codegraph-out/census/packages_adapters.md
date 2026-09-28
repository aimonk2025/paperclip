# Capability census — adapters

**177 files · 33,153 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 80 |
| validates input | 44 |
| captures a session id | 42 |
| reads config | 37 |
| buffers partial lines | 35 |
| parses JSON events | 33 |
| tracks token usage | 33 |
| reads from disk | 27 |
| writes to disk | 26 |
| caches | 25 |
| retries | 24 |
| handles cancellation | 23 |
| classifies errors | 22 |
| streams incrementally | 17 |
| enforces a timeout | 12 |
| spawns a process | 7 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `codex-local/src/server/execute.ts` | 1582 | firstMeaningfulStderrLine, assertCodexCredentialsLaunchable, ensureCodexSkillsInjected, execute |
| `openclaw-gateway/src/server/execute.ts` | 1492 | resolveSessionKey, resolveClaimedApiKeyPath, buildAgentParams, execute |
| `claude-local/src/server/execute.ts` | 1271 | claudeSessionCwdMatchesExecutionTarget, runClaudeLogin, execute |
| `hermes/src/gateway/server/execute.ts` | 959 | resolveSessionKey, parseSseFramesForTest, mapFinalResultForTest, execute |
| `codex-local/src/server/codex-home.ts` | 860 | CODEX_SYNC_ALLOWLIST, ManagedCodexMcpGateway, mergeManagedCodexMcpGateways, pathExists, resolveSharedCodexHomeDir +18 |
| `pi-local/src/server/execute.ts` | 847 | execute |
| `claude-local/src/server/acp.ts` | 782 | ClaudeExecutionEngine, ClaudeEngineSelection, resolveClaudeExecutionEngine, resolveClaudeExecutionEngineForRun, formatClaudeAcpFallbackMessage +7 |
| `cursor-local/src/server/execute.ts` | 763 | ensureCursorSkillsInjected, execute |
| `gemini-local/src/server/execute.ts` | 759 | execute |
| `opencode-local/src/server/execute.ts` | 730 | ensureRemoteOpenCodeModelConfiguredAndAvailable, execute |
| `codex-local/src/server/acp.ts` | 655 | CodexExecutionEngine, CodexEngineSelection, resolveCodexExecutionEngine, resolveCodexExecutionEngineForRun, formatCodexAcpFallbackMessage +5 |
| `codex-local/src/server/quota.ts` | 651 | codexHomeDir, CodexAuthInfo, readCodexAuthInfo, readCodexToken, secondsToWindowLabel +7 |
| `cursor-cloud/src/server/execute.ts` | 625 | execute |
| `hermes/src/server/execute.ts` | 598 | resolveHermesCommand, buildPrompt, execute |
| `grok-local/src/server/execute.ts` | 594 | execute |
| `claude-local/src/server/parse.ts` | 560 | claudeModelUsageTotals, parseClaudeStreamJson, extractClaudeLoginUrl, detectClaudeLoginRequired, describeClaudeFailure +9 |
| `claude-local/src/server/quota.ts` | 541 | claudeConfigDir, readClaudeAuthStatus, readClaudeToken, toPercent, fetchWithTimeout +5 |
| `claude-local/src/server/setup-token-parse.ts` | 518 | SetupTokenPrompt, SETUP_TOKEN_PROMPT, SETUP_TOKEN_AUTH_URLS, SETUP_TOKEN_REDIRECT_URI, SETUP_TOKEN_URL_QUERY_KEYS +5 |
| `gemini-local/src/server/acp.ts` | 514 | GeminiExecutionEngine, GeminiEngineSelection, resolveGeminiExecutionEngine, resolveGeminiExecutionEngineForRun, formatGeminiAcpFallbackMessage +4 |
| `codex-local/src/server/test.ts` | 459 | testEnvironment |
| `claude-local/src/server/test.ts` | 453 | testEnvironment |
| `claude-local/src/server/setup-token-runner.ts` | 449 | CLAUDE_SETUP_TOKEN_COMMAND, CODE_SUBMISSION_TERMINATOR, CODE_SUBMIT_SETTLE_MS, CLAUDE_SETUP_TOKEN_MAX_BUFFER_CHARS, SetupTokenPtyDriver +7 |
| `opencode-local/src/server/test.ts` | 441 | testEnvironment |
| `codex-local/src/server/runtime-config.ts` | 430 | stripManagedCodexProviderBlocks, prepareCodexRuntimeConfig |
| `cursor-local/src/ui/parse-stdout.ts` | 412 | parseCursorStdoutLine |

## Contract members — each is a capability

**ParsedGrokJsonl** (10 members)

```
sessionId, summary, thought, errorMessage, stopReason, requestId, inputTokens, outputTokens, cachedInputTokens, costUsd
```

**PromoteDeviceLoginCredentialInput** (8 members)

```
authBytes, companyId, userInitiated, checkReadiness, authBytes, isSoleActiveOwner, log, env
```

**CodexOutputInactivityMonitorState** (8 members)

```
fired, spawnedAt, lastEventAt, firedAt, outputChunkCount, outputBytes, parsedEventCount, processActivityCount
```

**WriteCredentialSeedOrNewerInput** (8 members)

```
sourceBytes, destinationPath, seedIfDestAbsent, log, writtenLine, keptLine, tempPrefix, errorLabel
```

**RunSetupTokenLoginOptions** (8 members)

```
command, onPrompt, provideCode, onCredential, codeSubmitSettleMs, timeoutMs, signal, log
```

**CodexProcessActivityMonitorOptions** (7 members)

```
pid, processGroupId, onActivity, intervalMs, sample, setTimer, clearTimer
```

**RunDeviceLoginOptions** (7 members)

```
command, onPrompt, onCredential, authPath, timeoutMs, signal, log
```

**CodexAuthInfo** (7 members)

```
accessToken, accountId, refreshToken, idToken, email, planType, lastRefresh
```

## Case sets — each arm is a case you must handle or drop

- **PromoteDeviceLoginCredentialOutcome** (5): promoted, kept, kept_foreign_identity, not_sole_owner, background_skipped
- **ReconcileManagedCodexHomeStatus** (5): no_managed_home, external_override, already_seeded, source_auth_missing, seeded
- **CodexAuthPrecedenceWinner** (4): configured_api_key, host_auth_json, sandbox_auth_json, none
- **CodexAuthRefreshFailureClass** (3): refresh_token_reused, refresh_token_expired, refresh_token_invalidated

## Structural duplication — the reduction lever

Identical logic across N files. This is where a rebuild gets smaller
WITHOUT losing features — unlike dropping capabilities.

| Repeated in | Shape |
|---|---|
| **14 files** | `function firstNonEmptyLine(text: string): string { return ( text .spli…` |
| **13 files** | `function asRecord(value: unknown): T<string, unknown> | null { if (typ…` |
| **13 files** | `if (typeof value !== "object" || value === null || T.isArray(value)) r…` |
| **11 files** | `} catch { return null; } } function asRecord(value: unknown): T<string…` |
| **11 files** | `return null; } } function asRecord(value: unknown): T<string, unknown>…` |
| **11 files** | `} } function asRecord(value: unknown): T<string, unknown> | null { if …` |

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
| reads config | | |
| reads from disk | | |
| retries | | |
| spawns a process | | |
| streams incrementally | | |
| tracks token usage | | |
| validates input | | |
| writes to disk | | |
| ParsedGrokJsonl.sessionId | | |
| ParsedGrokJsonl.summary | | |
| ParsedGrokJsonl.thought | | |
| ParsedGrokJsonl.errorMessage | | |
| ParsedGrokJsonl.stopReason | | |
| ParsedGrokJsonl.requestId | | |
| ParsedGrokJsonl.inputTokens | | |
| ParsedGrokJsonl.outputTokens | | |
| ParsedGrokJsonl.cachedInputTokens | | |
| ParsedGrokJsonl.costUsd | | |
| PromoteDeviceLoginCredentialInput.authBytes | | |
| PromoteDeviceLoginCredentialInput.companyId | | |
| PromoteDeviceLoginCredentialInput.userInitiated | | |
| PromoteDeviceLoginCredentialInput.checkReadiness | | |
| PromoteDeviceLoginCredentialInput.authBytes | | |
| PromoteDeviceLoginCredentialInput.isSoleActiveOwner | | |
| PromoteDeviceLoginCredentialInput.log | | |
| PromoteDeviceLoginCredentialInput.env | | |
| CodexOutputInactivityMonitorState.fired | | |
| CodexOutputInactivityMonitorState.spawnedAt | | |
| CodexOutputInactivityMonitorState.lastEventAt | | |
| CodexOutputInactivityMonitorState.firedAt | | |
| CodexOutputInactivityMonitorState.outputChunkCount | | |
| CodexOutputInactivityMonitorState.outputBytes | | |
| CodexOutputInactivityMonitorState.parsedEventCount | | |
| CodexOutputInactivityMonitorState.processActivityCount | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
