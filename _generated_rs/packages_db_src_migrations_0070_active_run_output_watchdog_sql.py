"""SQL: packages/db/src/migrations/0070_active_run_output_watchdog.sql"""

def tbl_heartbeat_run_watchdog_decisions():
    """TABLE heartbeat_run_watchdog_decisions — 11 columns, 4 foreign keys. src: packages/db/src/migrations/0070_active_run_output_watchdog.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_run_id = 'uuid NOT NULL'
    col_evaluation_issue_id = 'uuid'
    col_decision = 'text NOT NULL'
    col_snoozed_until = 'timestamp with time zone'
    col_reason = 'text'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_by_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_heartbeat_runs()  # FK run_id
    tbl_issues()  # FK evaluation_issue_id
    tbl_agents()  # FK created_by_agent_id
    pass
