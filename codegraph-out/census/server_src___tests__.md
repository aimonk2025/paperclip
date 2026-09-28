# Capability census — __tests__

**5 files · 250 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 1 |
| reads config | 1 |
| writes to disk | 1 |
| enforces a timeout | 1 |
| retries | 1 |
| parses JSON events | 1 |
| validates input | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `helpers/route-test-harness.ts` | 141 | describeEmbeddedPostgres, EmbeddedPostgresContext, useEmbeddedPostgres, BoardActor, SeededCompany +3 |
| `setup-supertest.ts` | 64 | — |
| `helpers/drain-heartbeat-runs.ts` | 26 | drainHeartbeatRunsToQuiescence |
| `helpers/wake-message.ts` | 13 | parseWakePayloadFromMessage |
| `helpers/embedded-postgres.ts` | 6 | — |

## Contract members — each is a capability

**BoardActor** (6 members)

```
type, source, userId, companyIds, memberships, isInstanceAdmin
```

## Decision ledger — fill this in, leave nothing blank

| Capability | KEEP / DROP | Reason |
|---|---|---|
| authenticates | | |
| enforces a timeout | | |
| parses JSON events | | |
| reads config | | |
| retries | | |
| validates input | | |
| writes to disk | | |
| BoardActor.type | | |
| BoardActor.source | | |
| BoardActor.userId | | |
| BoardActor.companyIds | | |
| BoardActor.memberships | | |
| BoardActor.isInstanceAdmin | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
