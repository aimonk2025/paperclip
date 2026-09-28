"""SQL: packages/db/src/migrations/0000_mature_masked_marvel.sql"""

def tbl_activity_log():
    """TABLE activity_log — 10 columns, 3 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_actor_type = 'text DEFAULT'
    col_actor_id = 'text NOT NULL'
    col_action = 'text NOT NULL'
    col_entity_type = 'text NOT NULL'
    col_entity_id = 'text NOT NULL'
    col_agent_id = 'uuid'
    col_details = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_heartbeat_runs()  # FK run_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    pass

def tbl_agent_api_keys():
    """TABLE agent_api_keys — 8 columns, 2 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_key_hash = 'text NOT NULL'
    col_last_used_at = 'timestamp with time zone'
    col_revoked_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_agents()  # FK agent_id
    tbl_companies()  # FK company_id
    pass

def tbl_agents():
    """TABLE agents — 17 columns, 3 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_role = 'text DEFAULT'
    col_title = 'text'
    col_status = 'text DEFAULT'
    col_reports_to = 'uuid'
    col_capabilities = 'text'
    col_adapter_type = 'text DEFAULT'
    col_adapter_config = 'jsonb DEFAULT'
    col_context_mode = 'text DEFAULT'
    col_budget_monthly_cents = 'integer DEFAULT 0 NOT NULL'
    col_spent_monthly_cents = 'integer DEFAULT 0 NOT NULL'
    col_last_heartbeat_at = 'timestamp with time zone'
    col_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_environments()  # FK default_environment_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK reports_to
    pass

def tbl_approvals():
    """TABLE approvals — 12 columns, 2 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_type = 'text NOT NULL'
    col_requested_by_agent_id = 'uuid'
    col_requested_by_user_id = 'text'
    col_status = 'text DEFAULT'
    col_payload = 'jsonb NOT NULL'
    col_decision_note = 'text'
    col_decided_by_user_id = 'text'
    col_decided_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK requested_by_agent_id
    pass

def tbl_companies():
    """TABLE companies — 8 columns, 0 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_status = 'text DEFAULT'
    col_budget_monthly_cents = 'integer DEFAULT 0 NOT NULL'
    col_spent_monthly_cents = 'integer DEFAULT 0 NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    pass

def tbl_cost_events():
    """TABLE cost_events — 14 columns, 6 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_issue_id = 'uuid'
    col_project_id = 'uuid'
    col_goal_id = 'uuid'
    col_billing_code = 'text'
    col_provider = 'text NOT NULL'
    col_model = 'text NOT NULL'
    col_input_tokens = 'integer DEFAULT 0 NOT NULL'
    col_output_tokens = 'integer DEFAULT 0 NOT NULL'
    col_cost_cents = 'integer NOT NULL'
    col_occurred_at = 'timestamp with time zone NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_issues()  # FK issue_id
    tbl_heartbeat_runs()  # FK heartbeat_run_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    tbl_projects()  # FK project_id
    tbl_goals()  # FK goal_id
    pass

def tbl_goals():
    """TABLE goals — 10 columns, 3 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_title = 'text NOT NULL'
    col_description = 'text'
    col_level = 'text DEFAULT'
    col_status = 'text DEFAULT'
    col_parent_id = 'uuid'
    col_owner_agent_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_goals()  # FK parent_id
    tbl_agents()  # FK owner_agent_id
    pass

def tbl_heartbeat_runs():
    """TABLE heartbeat_runs — 12 columns, 4 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_invocation_source = 'text DEFAULT'
    col_status = 'text DEFAULT'
    col_started_at = 'timestamp with time zone'
    col_finished_at = 'timestamp with time zone'
    col_error = 'text'
    col_external_run_id = 'text'
    col_context_snapshot = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_agent_wakeup_requests()  # FK wakeup_request_id
    tbl_heartbeat_runs()  # FK retry_of_run_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    pass

def tbl_issue_comments():
    """TABLE issue_comments — 8 columns, 5 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_author_agent_id = 'uuid'
    col_author_user_id = 'text'
    col_body = 'text NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_agents()  # FK deleted_by_agent_id
    tbl_heartbeat_runs()  # FK deleted_by_run_id
    tbl_issues()  # FK issue_id
    tbl_user()  # FK on_behalf_of_user_id
    tbl_companies()  # FK company_id
    pass

def tbl_issues():
    """TABLE issues — 19 columns, 8 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid'
    col_goal_id = 'uuid'
    col_parent_id = 'uuid'
    col_title = 'text NOT NULL'
    col_description = 'text'
    col_status = 'text DEFAULT'
    col_priority = 'text DEFAULT'
    col_assignee_agent_id = 'uuid'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_request_depth = 'integer DEFAULT 0 NOT NULL'
    col_billing_code = 'text'
    col_started_at = 'timestamp with time zone'
    col_completed_at = 'timestamp with time zone'
    col_cancelled_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_project_workspaces()  # FK project_workspace_id
    tbl_execution_workspaces()  # FK execution_workspace_id
    tbl_heartbeat_runs()  # FK execution_run_id
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    tbl_goals()  # FK goal_id
    tbl_issues()  # FK parent_id
    tbl_agents()  # FK assignee_agent_id
    pass

def tbl_projects():
    """TABLE projects — 10 columns, 3 foreign keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_goal_id = 'uuid'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_status = 'text DEFAULT'
    col_lead_agent_id = 'uuid'
    col_target_date = 'date'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_goals()  # FK goal_id
    tbl_agents()  # FK lead_agent_id
    pass

def idx_activity_log_company_created_idx():
    """INDEX on activity_log. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_activity_log()

def idx_agent_api_keys_key_hash_idx():
    """INDEX on agent_api_keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_agent_api_keys()

def idx_agent_api_keys_company_agent_idx():
    """INDEX on agent_api_keys. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_agent_api_keys()

def idx_agents_company_status_idx():
    """INDEX on agents. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_agents()

def idx_agents_company_reports_to_idx():
    """INDEX on agents. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_agents()

def idx_approvals_company_status_type_idx():
    """INDEX on approvals. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_approvals()

def idx_cost_events_company_occurred_idx():
    """INDEX on cost_events. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_cost_events()

def idx_cost_events_company_agent_occurred_idx():
    """INDEX on cost_events. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_cost_events()

def idx_goals_company_idx():
    """INDEX on goals. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_goals()

def idx_heartbeat_runs_company_agent_started_idx():
    """INDEX on heartbeat_runs. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_heartbeat_runs()

def idx_issue_comments_issue_idx():
    """INDEX on issue_comments. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_issue_comments()

def idx_issue_comments_company_idx():
    """INDEX on issue_comments. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_issue_comments()

def idx_issues_company_status_idx():
    """INDEX on issues. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_issues()

def idx_issues_company_assignee_status_idx():
    """INDEX on issues. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_issues()

def idx_issues_company_parent_idx():
    """INDEX on issues. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_issues()

def idx_issues_company_project_idx():
    """INDEX on issues. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_issues()

def idx_projects_company_idx():
    """INDEX on projects. src: packages/db/src/migrations/0000_mature_masked_marvel.sql"""
    tbl_projects()
