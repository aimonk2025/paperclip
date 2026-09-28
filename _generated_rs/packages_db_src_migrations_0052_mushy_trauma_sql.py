"""SQL: packages/db/src/migrations/0052_mushy_trauma.sql"""

def tbl_issue_execution_decisions():
    """TABLE issue_execution_decisions — 12 columns, 4 foreign keys. src: packages/db/src/migrations/0052_mushy_trauma.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_stage_id = 'uuid NOT NULL'
    col_stage_type = 'text NOT NULL'
    col_actor_agent_id = 'uuid'
    col_actor_user_id = 'text'
    col_outcome = 'text NOT NULL'
    col_body = 'text NOT NULL'
    col_created_by_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    tbl_agents()  # FK actor_agent_id
    tbl_heartbeat_runs()  # FK created_by_run_id
    pass

def idx_issue_execution_decisions_company_issue_idx():
    """INDEX on issue_execution_decisions. src: packages/db/src/migrations/0052_mushy_trauma.sql"""
    tbl_issue_execution_decisions()

def idx_issue_execution_decisions_stage_idx():
    """INDEX on issue_execution_decisions. src: packages/db/src/migrations/0052_mushy_trauma.sql"""
    tbl_issue_execution_decisions()
