"""SQL: packages/db/src/migrations/0039_fat_magneto.sql"""

def tbl_routine_runs():
    """TABLE routine_runs — 15 columns, 5 foreign keys. src: packages/db/src/migrations/0039_fat_magneto.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_routine_id = 'uuid NOT NULL'
    col_trigger_id = 'uuid'
    col_source = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_triggered_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_idempotency_key = 'text'
    col_trigger_payload = 'jsonb'
    col_linked_issue_id = 'uuid'
    col_coalesced_into_run_id = 'uuid'
    col_failure_reason = 'text'
    col_completed_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_routine_revisions()  # FK routine_revision_id
    tbl_companies()  # FK company_id
    tbl_routines()  # FK routine_id
    tbl_routine_triggers()  # FK trigger_id
    tbl_issues()  # FK linked_issue_id
    pass

def tbl_routine_triggers():
    """TABLE routine_triggers — 22 columns, 4 foreign keys. src: packages/db/src/migrations/0039_fat_magneto.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_routine_id = 'uuid NOT NULL'
    col_kind = 'text NOT NULL'
    col_label = 'text'
    col_enabled = 'boolean DEFAULT true NOT NULL'
    col_cron_expression = 'text'
    col_timezone = 'text'
    col_next_run_at = 'timestamp with time zone'
    col_last_fired_at = 'timestamp with time zone'
    col_public_id = 'text'
    col_secret_id = 'uuid'
    col_signing_mode = 'text'
    col_replay_window_sec = 'integer'
    col_last_rotated_at = 'timestamp with time zone'
    col_last_result = 'text'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_updated_by_agent_id = 'uuid'
    col_updated_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_routines()  # FK routine_id
    tbl_company_secrets()  # FK secret_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_routines():
    """TABLE routines — 20 columns, 6 foreign keys. src: packages/db/src/migrations/0039_fat_magneto.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid NOT NULL'
    col_goal_id = 'uuid'
    col_parent_issue_id = 'uuid'
    col_title = 'text NOT NULL'
    col_description = 'text'
    col_assignee_agent_id = 'uuid NOT NULL'
    col_priority = 'text DEFAULT'
    col_status = 'text DEFAULT'
    col_concurrency_policy = 'text DEFAULT'
    col_catch_up_policy = 'text DEFAULT'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_updated_by_agent_id = 'uuid'
    col_updated_by_user_id = 'text'
    col_last_triggered_at = 'timestamp with time zone'
    col_last_enqueued_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    tbl_goals()  # FK goal_id
    tbl_issues()  # FK parent_issue_id
    tbl_agents()  # FK assignee_agent_id
    tbl_folders()  # FK folder_id
    pass
