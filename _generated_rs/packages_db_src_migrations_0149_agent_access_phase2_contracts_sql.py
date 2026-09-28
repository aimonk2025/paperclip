"""SQL: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""

def tbl_tool_profiles():
    """TABLE tool_profiles — 10 columns, 1 foreign keys. src: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_profile_key = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_status = 'text DEFAULT'
    col_default_action = 'text DEFAULT'
    col_metadata = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def tbl_tool_profile_entries():
    """TABLE tool_profile_entries — 13 columns, 5 foreign keys. src: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_profile_id = 'uuid NOT NULL'
    col_selector_type = 'text NOT NULL'
    col_effect = 'text DEFAULT'
    col_application_id = 'uuid'
    col_connection_id = 'uuid'
    col_catalog_entry_id = 'uuid'
    col_tool_name = 'text'
    col_risk_level = 'text'
    col_conditions = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_profiles()  # FK profile_id
    tbl_tool_applications()  # FK application_id
    tbl_tool_connections()  # FK connection_id
    tbl_tool_catalog_entries()  # FK catalog_entry_id
    pass

def tbl_tool_profile_bindings():
    """TABLE tool_profile_bindings — 11 columns, 3 foreign keys. src: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_profile_id = 'uuid NOT NULL'
    col_target_type = 'text NOT NULL'
    col_target_id = 'text NOT NULL'
    col_priority = 'integer DEFAULT 100 NOT NULL'
    col_metadata = 'jsonb DEFAULT'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_profiles()  # FK profile_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_tool_policies():
    """TABLE tool_policies — 14 columns, 2 foreign keys. src: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_policy_type = 'text NOT NULL'
    col_priority = 'integer DEFAULT 100 NOT NULL'
    col_enabled = 'boolean DEFAULT true NOT NULL'
    col_selectors = 'jsonb DEFAULT'
    col_conditions = 'jsonb'
    col_config = 'jsonb'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_tool_invocations():
    """TABLE tool_invocations — 29 columns, 9 foreign keys. src: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_idempotency_key = 'text'
    col_actor_type = 'text DEFAULT'
    col_actor_id = 'text'
    col_agent_id = 'uuid'
    col_issue_id = 'uuid'
    col_run_id = 'uuid'
    col_application_id = 'uuid'
    col_connection_id = 'uuid'
    col_catalog_entry_id = 'uuid'
    col_tool_name = 'text NOT NULL'
    col_arguments_hash = 'text'
    col_arguments_summary = 'jsonb'
    col_policy_decision = 'text'
    col_matched_policy_ids = 'jsonb DEFAULT'
    col_approval_state = 'text DEFAULT'
    col_status = 'text DEFAULT'
    col_upstream_request_id = 'text'
    col_result_hash = 'text'
    col_result_summary = 'jsonb'
    col_result_size_bytes = 'integer'
    col_result_artifact_id = 'uuid'
    col_error_code = 'text'
    col_error_message = 'text'
    col_started_at = 'timestamp with time zone'
    col_completed_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_tool_mcp_gateways()  # FK gateway_id
    tbl_tool_mcp_gateway_tokens()  # FK gateway_token_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    tbl_issues()  # FK issue_id
    tbl_heartbeat_runs()  # FK run_id
    tbl_tool_applications()  # FK application_id
    tbl_tool_connections()  # FK connection_id
    tbl_tool_catalog_entries()  # FK catalog_entry_id
    pass

def tbl_tool_action_requests():
    """TABLE tool_action_requests — 22 columns, 6 foreign keys. src: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_invocation_id = 'uuid NOT NULL'
    col_issue_id = 'uuid'
    col_interaction_id = 'uuid'
    col_approval_id = 'uuid'
    col_status = 'text DEFAULT'
    col_canonical_arguments_hash = 'text NOT NULL'
    col_canonical_arguments_summary = 'jsonb NOT NULL'
    col_signed_arguments = 'text'
    col_preview_markdown = 'text'
    col_requested_by_agent_id = 'uuid'
    col_requested_by_user_id = 'text'
    col_resolved_by_agent_id = 'uuid'
    col_resolved_by_user_id = 'text'
    col_decided_by_agent_id = 'uuid'
    col_decided_by_user_id = 'text'
    col_decided_at = 'timestamp with time zone'
    col_expires_at = 'timestamp with time zone'
    col_resolved_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_invocations()  # FK invocation_id
    tbl_issues()  # FK issue_id
    tbl_issue_thread_interactions()  # FK interaction_id
    tbl_approvals()  # FK approval_id
    tbl_agents()  # FK requested_by_agent_id
    pass

def tbl_tool_call_events():
    """TABLE tool_call_events — 32 columns, 12 foreign keys. src: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_event_type = 'text NOT NULL'
    col_actor_type = 'text DEFAULT'
    col_actor_id = 'text'
    col_agent_id = 'uuid'
    col_run_id = 'uuid'
    col_issue_id = 'uuid'
    col_application_id = 'uuid'
    col_connection_id = 'uuid'
    col_catalog_entry_id = 'uuid'
    col_invocation_id = 'uuid'
    col_action_request_id = 'uuid'
    col_runtime_slot_id = 'uuid'
    col_tool_name = 'text'
    col_decision = 'text'
    col_matched_policy_ids = 'jsonb DEFAULT'
    col_reason_code = 'text'
    col_outcome = 'text DEFAULT'
    col_latency_ms = 'integer'
    col_arguments_summary = 'jsonb'
    col_request_hash = 'text'
    col_request_summary = 'jsonb'
    col_result_hash = 'text'
    col_result_summary = 'jsonb'
    col_result_size_bytes = 'integer'
    col_redaction_plan = 'jsonb'
    col_rate_limit_state = 'jsonb'
    col_metadata = 'jsonb'
    col_error_code = 'text'
    col_error_message = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_tool_mcp_gateways()  # FK gateway_id
    tbl_tool_mcp_gateway_tokens()  # FK gateway_token_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    tbl_heartbeat_runs()  # FK run_id
    tbl_issues()  # FK issue_id
    tbl_tool_applications()  # FK application_id
    tbl_tool_connections()  # FK connection_id
    tbl_tool_catalog_entries()  # FK catalog_entry_id
    tbl_tool_invocations()  # FK invocation_id
    tbl_tool_action_requests()  # FK action_request_id
    tbl_tool_runtime_slots()  # FK runtime_slot_id
    pass

def tbl_tool_rate_limit_counters():
    """TABLE tool_rate_limit_counters — 13 columns, 2 foreign keys. src: packages/db/src/migrations/0149_agent_access_phase2_contracts.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_policy_id = 'uuid NOT NULL'
    col_counter_key = 'text NOT NULL'
    col_scope_type = 'text NOT NULL'
    col_scope_id = 'text NOT NULL'
    col_window_kind = 'text NOT NULL'
    col_window_start_at = 'timestamp with time zone NOT NULL'
    col_limit = 'integer NOT NULL'
    col_remaining = 'integer NOT NULL'
    col_reset_at = 'timestamp with time zone NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_policies()  # FK policy_id
    pass
