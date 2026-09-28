# Graph Report - paperclip  (2026-09-14)

## Corpus Check
- 21 files · ~34,003 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 436 nodes · 700 edges · 19 communities (15 shown, 4 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 20 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9e3bb7c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- environment-custom-image-terminal-ws.ts
- startup-timing.ts
- index.ts
- TelemetryClient
- Sentry Error Monitoring
- instrumentation.ts
- duplex-observability.ts
- live-events-ws.ts
- paperclip-telemetry.ts
- runner-prp-outbound.ts
- Run-Log Events
- recovery-observability.ts
- runner-prp-ws.ts
- duplex-observability-recorder.ts
- createDuplexObservability
- DuplexObservability
- DuplexObservabilityDimensions
- DuplexChannelOpenAttempt
- heartbeat_run_events.ts

## God Nodes (most connected - your core abstractions)
1. `TelemetryClient` - 33 edges
2. `setupEnvironmentCustomImageTerminalWebSocketServer()` - 25 edges
3. `setupLiveEventsWebSocketServer()` - 13 edges
4. `asEventDimension()` - 12 edges
5. `measureStartupStep()` - 10 edges
6. `Sentry Error Monitoring` - 10 edges
7. `Run-Log Events` - 10 edges
8. `TelemetryEvent` - 9 edges
9. `Ssh2Shell` - 9 edges
10. `Telemetry Data Contract` - 9 edges
11. `EnvironmentCustomImageSshShell` - 8 edges
12. `TelemetryState` - 7 edges
13. `bootstrapOtel()` - 7 edges
14. `handleClientFrame()` - 7 edges
15. `WsJsonWireConnection` - 7 edges

## Surprising Connections (you probably didn't know these)
- `PendingBatch` --references--> `TelemetryEvent`  [EXTRACTED]
  packages/shared/src/telemetry/client.ts → packages/shared/src/telemetry/types.ts
- `TelemetryClient` --references--> `ResolvedTelemetryCaps`  [EXTRACTED]
  packages/shared/src/telemetry/client.ts → packages/shared/src/telemetry/config.ts
- `TelemetryClient` --references--> `TelemetryConfig`  [EXTRACTED]
  packages/shared/src/telemetry/client.ts → packages/shared/src/telemetry/types.ts
- `TelemetryClient` --references--> `TelemetryEvent`  [EXTRACTED]
  packages/shared/src/telemetry/client.ts → packages/shared/src/telemetry/types.ts
- `TelemetryClient` --references--> `TelemetryState`  [EXTRACTED]
  packages/shared/src/telemetry/client.ts → packages/shared/src/telemetry/types.ts

## Import Cycles
- None detected.

## Communities (19 total, 4 thin omitted)

### Community 0 - "environment-custom-image-terminal-ws.ts"
Cohesion: 0.06
Nodes (34): AuthenticatedTerminalContext, clientSafeErrorMessage(), closeClient(), closeUpgradeSocket(), createSsh2EnvironmentCustomImageSshConnector(), CUSTOM_IMAGE_TERMINAL_UTF8_ENV, CustomImageTerminalService, decodeClientMessage() (+26 more)

### Community 1 - "startup-timing.ts"
Cohesion: 0.07
Nodes (38): ActiveStepContext, activeStepContextStorage, buildActiveStepContext(), buildStepEvent(), BUILT_IN_PROVIDER_FAMILIES, clampSpanLabel(), createRuntimeSpanRunner(), emitSkippedStartupStep() (+30 more)

### Community 2 - "index.ts"
Cohesion: 0.12
Nodes (35): CI_ENV_VARS, isCI(), resolveCaps(), ResolvedTelemetryCaps, resolveTelemetryConfig(), TELEMETRY_DEFAULTS, TelemetryConfigOverrides, asEventDimension() (+27 more)

### Community 3 - "TelemetryClient"
Cohesion: 0.12
Nodes (12): DEFAULT_ENDPOINTS, parseRetryAfterMs(), PendingBatch, stableStringify(), TelemetryClient, TrackArgs, PAPERCLIP_EVENTS, TelemetryConfig (+4 more)

### Community 4 - "Sentry Error Monitoring"
Cohesion: 0.07
Nodes (31): 1. Install the OTel peer dependencies, 1. Install the Sentry peer dependency, 2. Set the environment, Browser data, Counters, Default capture set, Dimension keys, DSN delivery to the browser (+23 more)

### Community 5 - "instrumentation.ts"
Cohesion: 0.08
Nodes (17): bootstrapOtel(), ExporterProtocol, importExporter(), instrumentationReady, NOOP_SPAN, NOOP_TRACE_CONTEXT, NOOP_TRACER, OTEL_COMMON_PACKAGES (+9 more)

### Community 6 - "duplex-observability.ts"
Cohesion: 0.07
Nodes (24): APPROVED_PROVIDERS, DUPLEX_APPROVED_PROVIDER, DUPLEX_COUNTER_CHANNEL_OPEN_TOTAL, DUPLEX_COUNTER_FALLBACK_TOTAL, DUPLEX_COUNTER_LOSS_TOTAL, DUPLEX_COUNTER_SESSION_LEAK_TOTAL, DUPLEX_LOSS_REASONS, DUPLEX_PROVIDER_OTHER (+16 more)

### Community 7 - "live-events-ws.ts"
Cohesion: 0.14
Nodes (16): authorizeUpgrade(), closeUpgradeSocket(), CloudUpgradeActor, hashToken(), headersFromIncomingMessage(), IncomingMessageWithContext, isWritableUpgradeSocket(), parseBearerToken() (+8 more)

### Community 8 - "paperclip-telemetry.ts"
Cohesion: 0.09
Nodes (20): AnyPaperclipTelemetryEvent, PAPERCLIP_ENUM_DESCRIPTIONS, PaperclipAgentCreatedDimensions, PaperclipAgentFirstHeartbeatDimensions, PaperclipAgentTaskCompletedDimensions, PaperclipAgentTaskRunDimensions, PaperclipCompanyImportedDimensions, PaperclipErrorHandlerCrashDimensions (+12 more)

### Community 9 - "runner-prp-outbound.ts"
Cohesion: 0.14
Nodes (14): awaitWithinDeadline(), connectRunnerPrpIngress(), delay(), endpointHeaders(), openEndpoint(), RECONNECT_DELAYS_MS, RunnerIngressConnectionError, RunnerIngressFailureCode (+6 more)

### Community 10 - "Run-Log Events"
Cohesion: 0.09
Nodes (20): Codex resume usage snapshot, Execution recovery, Native Local Process Stop Evidence, Native PRP Run-Log Events, Native Restart Recovery Run-Log Event, Related instrumentation, Run-Log Events, Run Phase Timing Run-Log Event (+12 more)

### Community 11 - "recovery-observability.ts"
Cohesion: 0.13
Nodes (18): ACTIVE_STATUSES, classifyRecoveryHandoff(), DEFAULT_RECOVERY_RATE_THRESHOLD_PERCENT, evaluateRecoveryRateAlert(), HandoffClass, MAX_WINDOW_WEEKS, RecoveryActionFacts, RecoveryCauseGroup (+10 more)

### Community 12 - "runner-prp-ws.ts"
Cohesion: 0.16
Nodes (12): currentLiveAuthorities, CurrentLiveAuthority, liveAuthorityKey(), queueLiveRunnerPrpCommand(), RegisteredAuthority, registerRunnerPrpAuthority(), registrations, rejectUpgrade() (+4 more)

### Community 13 - "duplex-observability-recorder.ts"
Cohesion: 0.15
Nodes (9): getActiveStepContext(), DUPLEX_DIMENSION_KEYS, DUPLEX_SPAN_REQUEST, DuplexObservabilityCounterRecord, DuplexObservabilityEventRecord, DuplexObservabilitySpanRecord, createHostDuplexObservabilityRecorder(), DuplexObservabilitySpan (+1 more)

### Community 14 - "createDuplexObservability"
Cohesion: 0.47
Nodes (3): createDuplexObservability(), DuplexObservabilityRecorder, normalizeDuplexProvider()

## Knowledge Gaps
- **151 isolated node(s):** `RUN_STARTUP_STEP_EVENT_TYPE`, `BUILT_IN_PROVIDER_FAMILIES`, `SANDBOX_STARTUP_SPAN_ATTR_PREFIX`, `SANDBOX_STARTUP_SPAN_ATTRS`, `SANDBOX_STARTUP_OUTCOME` (+146 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TelemetryClient` connect `TelemetryClient` to `index.ts`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Why does `Observability` connect `Sentry Error Monitoring` to `Run-Log Events`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **Why does `DuplexObservability` connect `DuplexObservability` to `duplex-observability.ts`?**
  _High betweenness centrality (0.005) - this node is a cross-community bridge._
- **What connects `RUN_STARTUP_STEP_EVENT_TYPE`, `BUILT_IN_PROVIDER_FAMILIES`, `SANDBOX_STARTUP_SPAN_ATTR_PREFIX` to the rest of the system?**
  _151 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `environment-custom-image-terminal-ws.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.05961426066627703 - nodes in this community are weakly interconnected._
- **Should `startup-timing.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.06859903381642513 - nodes in this community are weakly interconnected._
- **Should `index.ts` be split into smaller, more focused modules?**
  _Cohesion score 0.11738648947951273 - nodes in this community are weakly interconnected._