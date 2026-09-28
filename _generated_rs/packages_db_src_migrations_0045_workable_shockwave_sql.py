"""SQL: packages/db/src/migrations/0045_workable_shockwave.sql"""

def tbl_issue_inbox_archives():
    """TABLE issue_inbox_archives — 7 columns, 4 foreign keys. src: packages/db/src/migrations/0045_workable_shockwave.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_user_id = 'text NOT NULL'
    col_archived_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_agents()  # FK archived_by_agent_id
    tbl_heartbeat_runs()  # FK archived_by_run_id
    tbl_issues()  # FK issue_id
    tbl_companies()  # FK company_id
    pass

def idx_issue_inbox_archives_company_issue_idx():
    """INDEX on issue_inbox_archives. src: packages/db/src/migrations/0045_workable_shockwave.sql"""
    tbl_issue_inbox_archives()

def idx_issue_inbox_archives_company_user_idx():
    """INDEX on issue_inbox_archives. src: packages/db/src/migrations/0045_workable_shockwave.sql"""
    tbl_issue_inbox_archives()

def idx_issue_inbox_archives_company_issue_user_idx():
    """INDEX on issue_inbox_archives. src: packages/db/src/migrations/0045_workable_shockwave.sql"""
    tbl_issue_inbox_archives()

def idx_board_api_keys_key_hash_idx():
    """INDEX on board_api_keys. src: packages/db/src/migrations/0045_workable_shockwave.sql"""
    tbl_board_api_keys()
