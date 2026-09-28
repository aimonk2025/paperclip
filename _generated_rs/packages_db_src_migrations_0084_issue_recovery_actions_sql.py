"""SQL: packages/db/src/migrations/0084_issue_recovery_actions.sql"""

def tbl_issue_recovery_actions():
    """TABLE issue_recovery_actions — 26 columns, 3 foreign keys. src: packages/db/src/migrations/0084_issue_recovery_actions.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_source_issue_id = 'uuid NOT NULL'
    col_recovery_issue_id = 'uuid'
    col_kind = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_owner_type = 'text DEFAULT'
    col_owner_agent_id = 'uuid'
    col_owner_user_id = 'text'
    col_previous_owner_agent_id = 'uuid'
    col_return_owner_agent_id = 'uuid'
    col_cause = 'text NOT NULL'
    col_fingerprint = 'text NOT NULL'
    col_evidence = 'jsonb DEFAULT'
    col_next_action = 'text NOT NULL'
    col_wake_policy = 'jsonb'
    col_monitor_policy = 'jsonb'
    col_attempt_count = 'integer DEFAULT 0 NOT NULL'
    col_max_attempts = 'integer'
    col_timeout_at = 'timestamp with time zone'
    col_last_attempt_at = 'timestamp with time zone'
    col_outcome = 'text'
    col_resolution_note = 'text'
    col_resolved_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK source_issue_id
    tbl_agents()  # FK owner_agent_id
    pass
