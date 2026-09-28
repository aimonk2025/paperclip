"""SQL: packages/db/src/migrations/0104_issue_watchdogs.sql"""

def tbl_issue_watchdogs():
    """TABLE issue_watchdogs — 20 columns, 4 foreign keys. src: packages/db/src/migrations/0104_issue_watchdogs.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_watchdog_agent_id = 'uuid NOT NULL'
    col_instructions = 'text'
    col_status = 'text DEFAULT'
    col_watchdog_issue_id = 'uuid'
    col_last_observed_fingerprint = 'text'
    col_last_reviewed_fingerprint = 'text'
    col_last_triggered_at = 'timestamp with time zone'
    col_last_completed_at = 'timestamp with time zone'
    col_trigger_count = 'integer DEFAULT 0 NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_by_run_id = 'uuid'
    col_updated_by_agent_id = 'uuid'
    col_updated_by_user_id = 'text'
    col_updated_by_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    tbl_agents()  # FK watchdog_agent_id
    tbl_heartbeat_runs()  # FK created_by_run_id
    pass
