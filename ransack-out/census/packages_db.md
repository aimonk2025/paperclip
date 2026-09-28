# Capability census — db

**137 files · 12,330 lines**

Enumerated BEFORE any decision. Every row is a capability that must be
either KEPT (with a rebuild plan) or DROPPED (with a stated reason).

## Behaviours observed

| Capability | Files |
|---|---|
| authenticates | 25 |
| validates input | 15 |
| reads from disk | 10 |
| reads config | 9 |
| retries | 7 |
| parses JSON events | 6 |
| classifies errors | 6 |
| buffers partial lines | 5 |
| captures a session id | 5 |
| tracks token usage | 4 |
| handles cancellation | 3 |
| caches | 1 |
| enforces a timeout | 1 |
| spawns a process | 1 |
| streams incrementally | 1 |
| writes to disk | 1 |

## Public surface

| File | Lines | Exports |
|---|---|---|
| `src/check-migration-safety.ts` | 1052 | MigrationSafetyRule, MigrationSafetySeverity, MigrationSafetyFinding, MigrationSafetyInput, MigrationSafetyResult +1 |
| `src/backup-lib.ts` | 1034 | BackupRetentionPolicy, RunDatabaseBackupOptions, RunDatabaseBackupResult, RunDatabaseRestoreOptions, createBufferedTextFileWriter +3 |
| `src/client.ts` | 880 | MigrationState, DatabaseClientOptions, databaseClientOptionsFromEnv, postgresJsOptions, createDb +10 |
| `src/schema/tool_access.ts` | 869 | toolApplications, toolConnections, connectionGrants, toolConnectionInstalls, toolOauthStates +18 |
| `scripts/clean-poisoned-claude-sessions.ts` | 462 | SessionClassification, ClaudeSessionRowInput, classifyJsonlText, encodeClaudeCwd, resolveClaudeConfigDir +2 |
| `src/test-embedded-postgres.ts` | 295 | EmbeddedPostgresTestSupport, EmbeddedPostgresTestDatabase, __setEmbeddedPostgresCtorProviderForTests, __startEmbeddedPostgresWithRetryForTests, __embeddedPostgresStartMaxAttemptsForTests +2 |
| `src/schema/decision_queues.ts` | 256 | decisionQueues, decisionQueueItems, decisionTriage, decisionTriageEvents, decisionRetention +1 |
| `src/schema/company_skills.ts` | 244 | companySkills, CompanySkillVersionFileInventoryEntry, companySkillVersions, companySkillStars, companySkillComments +3 |
| `src/runtime-config.ts` | 236 | ResolvedDatabaseTarget, resolveDatabaseTarget |
| `src/schema/pipeline_cases.ts` | 213 | PipelineCasePendingSuggestion, PipelineCaseWorkspaceRef, pipelineCases, pipelineCaseIssueLinks, pipelineCaseBlockers +3 |
| `src/migration-runtime.ts` | 196 | MigrationConnection, resolveMigrationConnection |
| `src/schema/issues.ts` | 179 | issues |
| `src/schema/index.ts` | 177 | — |
| `src/table-size-estimates.ts` | 176 | TableSizeBucket, LocalTableRowCount, TableSizeEstimate, TABLE_SIZE_ESTIMATE_SOURCE, TABLE_SIZE_ESTIMATE_FACTOR +7 |
| `src/schema/routines.ts` | 176 | routines, routineRevisions, routineTriggers, routineRuns |
| `src/schema/cases.ts` | 168 | cases, caseIssueLinks, caseEvents, caseDocuments, caseLabels +1 |
| `src/migration-safety-baseline.ts` | 157 | MigrationSafetyBaselineEntry, MIGRATION_SAFETY_BASELINE |
| `src/schema/decisions.ts` | 115 | decisionBundles, decisions, decisionTargetIssues, decisionEffectExecutions |
| `src/schema/heartbeat_runs.ts` | 108 | heartbeatRuns |
| `src/schema/plugin_jobs.ts` | 106 | pluginJobs, pluginJobRuns |
| `src/seed.ts` | 99 | — |
| `src/backup.ts` | 98 | — |
| `src/schema/status_cards.ts` | 97 | statusCards, statusCardUpdates |
| `src/schema/plugin_state.ts` | 90 | pluginState |
| `src/embedded-postgres-error.ts` | 89 | createEmbeddedPostgresLogBuffer, formatEmbeddedPostgresError |

## Contract members — each is a capability

**RunDatabaseBackupOptions** (9 members)

```
connectionString, backupDir, retention, filenamePrefix, connectTimeoutSeconds, includeMigrationJournal, excludeTables, nullifyColumns, backupEngine
```

**PipelineCasePendingSuggestion** (7 members)

```
id, toStageKey, rationale, confidence, suggestedByAgentId, runId, createdAt
```

**MigrationState** (5 members)

```
status, tableCount, availableMigrations, appliedMigrations, journalEntryCount
```

**ResolvedDatabaseTarget** (5 members)

```
mode, connectionString, source, configPath, envPath
```

**DatabaseClientOptions** (4 members)

```
prepare, maxConnections, idleTimeoutSeconds, connectTimeoutSeconds
```

**ClaudeSessionRowInput** (3 members)

```
sessionId, cwd, isRemote
```

**MigrationConnection** (3 members)

```
connectionString, source, stop
```

**Db** (3 members)

```
entries, idx, tag
```

## Case sets — each arm is a case you must handle or drop

- **ClaudeSetupTokenSessionState** (9): starting, awaiting_code, submitting, persisting, stored, completed, failed, timed_out, cancelled
- **MigrationSafetyRule** (4): loop-mutation-large-table, batched-mutation-large-table-missing-index, full-table-mutation-large-table, large-create-index-not-concurrently

## Structural duplication — the reduction lever

Identical logic across N files. This is where a rebuild gets smaller
WITHOUT losing features — unlike dropping capabilities.

| Repeated in | Shape |
|---|---|
| **4 files** | `documentId: uuid("document_id").notNull().references(() => documents.i…` |
| **3 files** | `timestamp, uniqueIndex, uuid, } from "drizzle-orm/pg-core"; import { a…` |
| **3 files** | `createX: uuid("createX").references(() => agents.id, { onDelete: "set …` |
| **3 files** | `{ id: uuid("id").primaryKey().defaultRandom(), pluginId: uuid("plugin_…` |

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
| RunDatabaseBackupOptions.connectionString | | |
| RunDatabaseBackupOptions.backupDir | | |
| RunDatabaseBackupOptions.retention | | |
| RunDatabaseBackupOptions.filenamePrefix | | |
| RunDatabaseBackupOptions.connectTimeoutSeconds | | |
| RunDatabaseBackupOptions.includeMigrationJournal | | |
| RunDatabaseBackupOptions.excludeTables | | |
| RunDatabaseBackupOptions.nullifyColumns | | |
| RunDatabaseBackupOptions.backupEngine | | |
| PipelineCasePendingSuggestion.id | | |
| PipelineCasePendingSuggestion.toStageKey | | |
| PipelineCasePendingSuggestion.rationale | | |
| PipelineCasePendingSuggestion.confidence | | |
| PipelineCasePendingSuggestion.suggestedByAgentId | | |
| PipelineCasePendingSuggestion.runId | | |
| PipelineCasePendingSuggestion.createdAt | | |
| MigrationState.status | | |
| MigrationState.tableCount | | |
| MigrationState.availableMigrations | | |
| MigrationState.appliedMigrations | | |
| MigrationState.journalEntryCount | | |

> A DROP row needs a concept in YOUR system that it maps to nothing in.
> "We don't need it yet" is not a reason — that is scope, not domain.
