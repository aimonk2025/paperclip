# Structural inventory

**Enumerated, not clustered.** Community detection finds where code is
dense; this counts the things. Parity is the default — if they ship 12
adapters and you build 5, that is an unfinished port.

## Families — sibling implementations

| where | kind | count | members |
|---|---|---|---|
| `ui/src/adapters` | adapter | **13** | `claude-local`, `codex-local`, `cursor`, `cursor-cloud`, `gemini-local`, `grok-local`, `hermes-gateway`, `hermes-local`, `http`, `openclaw-gateway` +3 |
| `packages/adapters` | adapter | **11** | `claude-local`, `codex-local`, `cursor-cloud`, `cursor-local`, `gemini-local`, `grok-local`, `hermes`, `hermes-gateway`, `openclaw-gateway`, `opencode-local` +1 |
| `packages` | package | **9** | `adapter-utils`, `db`, `google-sheets-mcp-server`, `kv-demo-mcp-server`, `mcp-server`, `shared`, `skills-catalog`, `tailscale-https-broker`, `teams-catalog` |
| `packages/plugins/sandbox-providers` | plugin | **7** | `cloudflare`, `daytona`, `e2b`, `exe-dev`, `kubernetes`, `modal`, `novita` |
| `packages/plugins/plugin-llm-wiki/skills` | plugin | **6** | `index-refresh`, `paperclip-distill`, `wiki-ingest`, `wiki-lint`, `wiki-maintainer`, `wiki-query` |
| `server/src` | sibling-group | **5** | `adapters`, `middleware`, `routes`, `services`, `storage` |
| `packages/plugins` | plugin | **5** | `create-paperclip-plugin`, `paperclip-plugin-fake-sandbox`, `plugin-llm-wiki`, `plugin-workspace-diff`, `sdk` |
| `packages/plugins/examples` | plugin | **5** | `plugin-authoring-smoke-example`, `plugin-file-browser-example`, `plugin-hello-world-example`, `plugin-kitchen-sink-example`, `plugin-orchestration-smoke-example` |
| `packages/skills-catalog/catalog/bundled/paperclip-operations` | skill | **5** | `issue-triage`, `reflection-coach`, `status-card-query`, `summarize-status`, `task-planning` |
| `skills` | skill | **5** | `paperclip`, `paperclip-board`, `paperclip-converting-plans-to-tasks`, `paperclip-create-agent`, `para-memory-files` |
| `packages/adapters/hermes/src` | adapter | **4** | `cli`, `gateway`, `server`, `ui` |
| `<root>` | sibling-group | **3** | `cli`, `server`, `ui` |
| `ui/src` | sibling-group | **3** | `adapters`, `api`, `i18n` |
| `packages/shared/src` | package | **3** | `telemetry`, `types`, `validators` |
| `packages/adapters/hermes-gateway/src` | adapter | **3** | `cli`, `server`, `ui` |
| `packages/adapters/cursor-local/src` | adapter | **3** | `cli`, `server`, `ui` |
| `packages/adapters/opencode-local/src` | adapter | **3** | `cli`, `server`, `ui` |
| `packages/adapters/cursor-cloud/src` | adapter | **3** | `cli`, `server`, `ui` |
| `packages/adapters/gemini-local/src` | adapter | **3** | `cli`, `server`, `ui` |
| `packages/adapters/grok-local/src` | adapter | **3** | `cli`, `server`, `ui` |

> **This is the count to match.**

## Packages — 43

| name | eco | path |
|---|---|---|
| `paperclip` | npm | `.` |
| `paperclipai` | npm | `cli` |
| `@paperclipai/adapter-utils` | npm | `packages/adapter-utils` |
| `@paperclipai/adapter-claude-local` | npm | `packages/adapters/claude-local` |
| `@paperclipai/adapter-codex-local` | npm | `packages/adapters/codex-local` |
| `@paperclipai/adapter-cursor-cloud` | npm | `packages/adapters/cursor-cloud` |
| `@paperclipai/adapter-cursor-local` | npm | `packages/adapters/cursor-local` |
| `@paperclipai/adapter-gemini-local` | npm | `packages/adapters/gemini-local` |
| `@paperclipai/adapter-grok-local` | npm | `packages/adapters/grok-local` |
| `@paperclipai/hermes-paperclip-adapter` | npm | `packages/adapters/hermes` |
| `@paperclipai/adapter-hermes-gateway` | npm | `packages/adapters/hermes-gateway` |
| `@paperclipai/adapter-openclaw-gateway` | npm | `packages/adapters/openclaw-gateway` |
| `@paperclipai/adapter-opencode-local` | npm | `packages/adapters/opencode-local` |
| `@paperclipai/adapter-pi-local` | npm | `packages/adapters/pi-local` |
| `@paperclipai/db` | npm | `packages/db` |
| `@paperclipai/google-sheets-mcp-server` | npm | `packages/google-sheets-mcp-server` |
| `@paperclipai/kv-demo-mcp-server` | npm | `packages/kv-demo-mcp-server` |
| `@paperclipai/mcp-server` | npm | `packages/mcp-server` |
| `@paperclipai/create-paperclip-plugin` | npm | `packages/plugins/create-paperclip-plugin` |
| `@paperclipai/plugin-authoring-smoke-example` | npm | `packages/plugins/examples/plugin-authoring-smoke-example` |
| `@paperclipai/plugin-file-browser-example` | npm | `packages/plugins/examples/plugin-file-browser-example` |
| `@paperclipai/plugin-hello-world-example` | npm | `packages/plugins/examples/plugin-hello-world-example` |
| `@paperclipai/plugin-kitchen-sink-example` | npm | `packages/plugins/examples/plugin-kitchen-sink-example` |
| `@paperclipai/plugin-orchestration-smoke-example` | npm | `packages/plugins/examples/plugin-orchestration-smoke-example` |
| `@paperclipai/plugin-fake-sandbox` | npm | `packages/plugins/paperclip-plugin-fake-sandbox` |
| `@paperclipai/plugin-llm-wiki` | npm | `packages/plugins/plugin-llm-wiki` |
| `@paperclipai/plugin-workspace-diff` | npm | `packages/plugins/plugin-workspace-diff` |
| `@paperclipai/plugin-cloudflare-sandbox` | npm | `packages/plugins/sandbox-providers/cloudflare` |
| `paperclip-cloudflare-sandbox-bridge-template` | npm | `packages/plugins/sandbox-providers/cloudflare/bridge-template` |
| `@paperclipai/plugin-daytona` | npm | `packages/plugins/sandbox-providers/daytona` |

## Entrypoints — what actually runs

| kind | count | examples |
|---|---|---|
| cli | 40 | `cli/esbuild.config.mjs`, `cli/src/index.ts`, `cli/src/commands/pipelines.ts` |
| migration | 40 | `packages/plugins/examples/plugin-orchestration-smoke-example/migrations/001_orchestration_smoke.sql`, `packages/plugins/plugin-llm-wiki/migrations/002_paperclip_distillation.sql`, `packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql` |
| http server | 19 | `server/src/app.ts`, `server/src/index.ts`, `server/src/services/smoke-lab.ts` |
| mcp server | 16 | `ui/src/pages/tools/PasteConfigTab.tsx`, `server/src/adapters/index.ts`, `server/src/services/heartbeat.ts` |
| websocket | 7 | `ui/src/components/transcript/useLiveRunTranscripts.ts`, `ui/src/pages/CompanyEnvironments.tsx`, `server/src/index.ts` |
| worker/queue | 4 | `ui/src/adapters/sandboxed-parser-worker.ts`, `ui/src/hooks/useWorkspaceFileAvailability.ts`, `ui/src/pages/JoinRequestQueue.tsx` |
| cron/schedule | 2 | `ui/src/hooks/useSecondTick.ts`, `packages/kv-demo-mcp-server/src/render.ts` |

## Variants — every case the system handles

| union | arms | values |
|---|---|---|
| `ToolAccessReasonCode` | **16** | `allow_trust_rule`, `allow_profile`, `allow_explicit_grant`, `allow_policy`, `requires_review_changed_tool`, `requires_approval_policy`, `deny_default`, `deny_company_boundary`, `deny_disabled_connection`, `deny_disabled_application`, `deny_archived_application`, `deny_missing_tool` |
| `ProjectConfigFieldKey` | **15** | `name`, `description`, `status`, `goals`, `env`, `execution_workspace_enabled`, `execution_workspace_default_mode`, `execution_workspace_shared_concurrency`, `execution_workspace_environment`, `execution_workspace_base_ref`, `execution_workspace_branch_template`, `execution_workspace_worktree_parent_dir` |
| `PaperclipEventName` | **14** | `agent.created`, `agent.first_heartbeat`, `agent.task_completed`, `company.imported`, `error.handler_crash`, `goal.created`, `install.completed`, `install.started`, `interaction.created`, `interaction.resolved`, `project.created`, `routine.created` |
| `PipelineHealthWarningCode` | **13** | `paused_agent`, `stage_no_automation`, `automation_no_instructions`, `automation_no_agent`, `automation_failed`, `review_no_approver`, `missing_pipeline_reference`, `missing_stage_reference`, `breakdown_target_missing`, `breakdown_no_wait`, `breakdown_target_not_entry_safe`, `breakdown_field_mismatch` |
| `IssueBlockedInboxReason` | **12** | `blocked_by_unassigned_issue`, `blocked_by_assigned_backlog_issue`, `blocked_by_uninvokable_assignee`, `blocked_by_cancelled_issue`, `blocked_chain_stalled`, `invalid_review_participant`, `in_review_without_action_path`, `missing_successful_run_disposition`, `pending_board_decision`, `pending_user_decision`, `external_owner_action`, `open_recovery_issue` |
| `CatalogTeamFileKind` | **12** | `team`, `agent`, `project`, `task`, `skill`, `extension`, `readme`, `reference`, `script`, `asset`, `markdown`, `other` |
| `CatalogTeamFileKind` | **12** | `team`, `agent`, `project`, `task`, `skill`, `extension`, `readme`, `reference`, `script`, `asset`, `markdown`, `other` |
| `CaseEventKind` | **11** | `created`, `updated`, `fields_changed`, `status_changed`, `issue_linked`, `issue_unlinked`, `document_revised`, `child_linked`, `attachment_added`, `label_added`, `label_removed` |
| `SecretResolutionErrorCode` | **11** | `binding_missing`, `secret_deleted`, `secret_inactive`, `secret_scope_invalid`, `responsible_user_missing`, `user_secret_definition_missing`, `user_secret_definition_inactive`, `user_secret_missing`, `version_missing`, `version_inactive`, `provider_error` |
| `LoginSessionActivityPhase` | **11** | `session_created`, `lease_acquired`, `lease_released`, `prompt_surfaced`, `promoting`, `sandbox_deleted`, `cleanup_pending`, `authenticated`, `failed`, `timed_out`, `cancelled` |
| `ResourceStatusVariant` | **10** | `ready`, `needs_setup`, `missing`, `error`, `update_available`, `drifted`, `schedule_off`, `schedule_on`, `pending_approval`, `proposal_pending` |
| `WorkspaceHandoffVerificationFailure` | **10** | `not_configured`, `malformed`, `unsupported_version`, `bad_signature`, `expired`, `not_yet_valid`, `origin_mismatch`, `instance_mismatch`, `workspace_mismatch`, `company_mismatch` |
| `AgentInvokabilityBlockReason` | **10** | `missing`, `paused`, `terminated`, `pending_approval`, `unknown_status`, `manager_missing`, `manager_company_mismatch`, `manager_terminated`, `reporting_cycle`, `reporting_chain_too_deep` |
| `EnvironmentErrorCode` | **10** | `environment_not_found`, `environment_inactive`, `unsupported_environment`, `unsupported_adapter_environment`, `probe_failed`, `lease_acquire_failed`, `workspace_realization_failed`, `transport_resolution_failed`, `lease_release_failed`, `lease_cleanup_failed` |
| `HeartbeatRunStopReason` | **10** | `completed`, `interrupted`, `timeout`, `cancelled`, `budget_paused`, `paused`, `max_turns_exhausted`, `process_lost`, `unmanaged_background_task_stopped`, `adapter_failed` |
| `Tone` | **10** | `todo`, `in_progress`, `in_review`, `done`, `blocked`, `running`, `paused`, `failed`, `queued`, `default` |
| `ToolFamily` | **9** | `terminal`, `grep`, `search`, `read`, `edit`, `web`, `agent`, `mcp`, `other` |
| `AgentDetailView` | **9** | `dashboard`, `instructions`, `configuration`, `secrets`, `skills`, `tools`, `runs`, `audit`, `budget` |
| `CaseColumn` | **9** | `id`, `key`, `title`, `status`, `updated`, `created`, `type`, `project`, `parent` |
| `ImportAdjustment` | **9** | `clear_assignee_agent`, `clear_project`, `clear_project_workspace`, `clear_goal`, `clear_author_agent`, `coerce_in_progress_to_todo`, `clear_document_agent`, `clear_document_revision_agent`, `clear_attachment_agent` |

> Each arm is a case. Dropping one silently narrows behaviour.
