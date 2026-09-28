# Capability census — tailscale-https-broker

**20 files · 2,788 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| validates input | 10 |
| authenticates | 9 |
| parses JSON events | 4 |
| classifies errors | 4 |
| reads from disk | 3 |
| spawns a process | 2 |
| enforces a timeout | 2 |
| caches | 2 |
| reads config | 1 |
| handles cancellation | 1 |
| buffers partial lines | 1 |
| streams incrementally | 1 |
| tracks token usage | 1 |
| writes to disk | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `src/broker-core.ts` | 827 | CliResult, ListenerOwnership, BrokerDeps, BrokerCoreConfig, BrokerCore |
| `src/socket-server.ts` | 218 | SocketServerConfig, ClientAdmissionConfig, ClientAdmissionController, startSocketServer |
| `src/types.ts` | 215 | BROKER_PROTOCOL_VERSION, PROTECTED_PRIMARY_PORT, PROTECTED_PRIMARY_TARGET, PROTECTED_PRIMARY_PORTS, BrokerOp +16 |
| `src/strict-json.ts` | 194 | parseJsonNoDuplicateKeys |
| `src/serve-config.ts` | 183 | ServeHandler, ServeEntry, ParsedServe, ServeParseError, parseServeStatus +6 |
| `src/protocol.ts` | 182 | MAX_REQUEST_BYTES, MAX_LISTENERS_PER_REQUEST, ProtocolError, decodeRequest |
| `src/registry.ts` | 158 | emptyRegistry, loadRegistry, saveRegistry, registryPathUnsafeReason, nextGeneration +6 |
| `src/proc-listener.ts` | 142 | ProcListenerRow, parseProcNetTable, isLoopbackIpv4Hex, isLoopbackIpv6Hex, isWildcardHex +3 |
| `src/main.ts` | 94 | — |
| `src/audit.ts` | 90 | AuditEvent, sanitizeField, formatAuditLine, AuditSink, FileAuditSink +1 |
| `src/authorization.ts` | 87 | PeerPolicy, AuthorizationError, authorizePeer, generateLeaseHandle, handlesEqual +1 |
| `src/argv.ts` | 76 | loopbackTarget, buildStatusArgv, buildExposeArgv, buildRemoveArgv |
| `src/config.ts` | 61 | BrokerHostConfig, loadHostConfig |
| `src/integers.ts` | 59 | MIN_PORT, MAX_PORT, assertCanonicalPort, parseCanonicalIntegerString |
| `src/tailscale-cli.ts` | 57 | MIN_TAILSCALE_VERSION, createTailscaleRunner, parseTailscaleVersion, isSupportedTailscaleVersion |
| `src/port-policy.ts` | 48 | DEFAULT_APP_PORT_MIN, DEFAULT_APP_PORT_MAX, DEFAULT_HMR_PORT_OFFSET, DEFAULT_HMR_PORT_MIN, DEFAULT_HMR_PORT_MAX +2 |
| `src/peercred.ts` | 37 | PeerResolverConfig, PeerResolutionError, createPeerResolver |
| `src/native-peercred.ts` | 36 | createNativePeerCredentialReader |
| `vitest.config.ts` | 13 | — |
| `src/index.ts` | 11 | — |

## Contract members — each is a capability

**AuditEvent** (13 members)

```
timestampIso, peer, op, runtimeId, ports, requestId, decision, reasonCode, reason, beforeDigest, afterDigest, cliExitCategory, recovery
```

**LeaseRecord** (10 members)

```
handle, runtimeId, peerUid, peerGid, ports, purposes, state, generation, createdAtIso, expiresAtIso
```

**BrokerHostConfig** (9 members)

```
socketPath, registryPath, auditPath, tailscaleBinPath, nodeIdentity, serviceUid, serviceGid, runtimeUid, protectedPorts
```

**BrokerCoreConfig** (8 members)

```
tailscaleBinPath, registryPath, auditSink, peerPolicy, nodeIdentity, isAllowedPort, protectedPorts, deps
```

**SocketServerConfig** (8 members)

```
socketPath, core, resolvePeer, serviceUid, maxClients, maxClientsPerUid, reservedServiceClients, connectionDeadlineMs
```

**ProcListenerRow** (5 members)

```
localAddressHex, localPortHex, state, uid, inode
```

**ReserveResponseOk** (5 members)

```
ok, op, requestId, handle, reservedPorts
```

**ExposeResponseOk** (5 members)

```
ok, op, requestId, handle, publicPorts
```

## Case sets — each arm is a case you must handle or drop

- **BrokerErrorCode** (28): unsupported_version, malformed_request, unknown_operation, unauthorized_peer, invalid_runtime_id, invalid_port, port_not_allowlisted, listener_not_owned, listener_absent, listener_not_loopback, listener_ownership_mismatch, listener_unattributable, listener_substituted, manual_mapping_present, protected_port, protected_entry_violation, reservation_conflict, reservation_expired, primary_route_violation, invalid_handle, serve_parse_error, cli_error, cli_timeout, unexpected_serve_diff, quarantined, rate_limited, too_many_clients, internal_error

## Decision ledger — fill this in, leave nothing blank

| Capability | KEEP / DROP | Reason |
|---|---|---|
| authenticates | | |
| buffers partial lines | | |
| caches | | |
| classifies errors | | |
| enforces a timeout | | |
| handles cancellation | | |
| parses JSON events | | |
| reads config | | |
| reads from disk | | |
| spawns a process | | |
| streams incrementally | | |
| tracks token usage | | |
| validates input | | |
| writes to disk | | |
| AuditEvent.timestampIso | | |
| AuditEvent.peer | | |
| AuditEvent.op | | |
| AuditEvent.runtimeId | | |
| AuditEvent.ports | | |
| AuditEvent.requestId | | |
| AuditEvent.decision | | |
| AuditEvent.reasonCode | | |
| AuditEvent.reason | | |
| AuditEvent.beforeDigest | | |
| AuditEvent.afterDigest | | |
| AuditEvent.cliExitCategory | | |
| AuditEvent.recovery | | |
| LeaseRecord.handle | | |
| LeaseRecord.runtimeId | | |
| LeaseRecord.peerUid | | |
| LeaseRecord.peerGid | | |
| LeaseRecord.ports | | |
| LeaseRecord.purposes | | |
| LeaseRecord.state | | |
| LeaseRecord.generation | | |
| LeaseRecord.createdAtIso | | |
| LeaseRecord.expiresAtIso | | |
| BrokerHostConfig.socketPath | | |
| BrokerHostConfig.registryPath | | |
| BrokerHostConfig.auditPath | | |
| BrokerHostConfig.tailscaleBinPath | | |
| BrokerHostConfig.nodeIdentity | | |
| BrokerHostConfig.serviceUid | | |
| BrokerHostConfig.serviceGid | | |
| BrokerHostConfig.runtimeUid | | |
| BrokerHostConfig.protectedPorts | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
