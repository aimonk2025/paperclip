"""SQL: packages/db/src/migrations/0077_unusual_karnak.sql"""

def tbl_routine_revisions():
    """TABLE routine_revisions — 13 columns, 5 foreign keys. src: packages/db/src/migrations/0077_unusual_karnak.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_routine_id = 'uuid NOT NULL'
    col_revision_number = 'integer NOT NULL'
    col_title = 'text NOT NULL'
    col_description = 'text'
    col_snapshot = 'jsonb NOT NULL'
    col_change_summary = 'text'
    col_restored_from_revision_id = 'uuid'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_by_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_routines()  # FK routine_id
    tbl_routine_revisions()  # FK restored_from_revision_id
    tbl_agents()  # FK created_by_agent_id
    tbl_heartbeat_runs()  # FK created_by_run_id
    pass
