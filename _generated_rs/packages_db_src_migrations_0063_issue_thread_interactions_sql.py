"""SQL: packages/db/src/migrations/0063_issue_thread_interactions.sql"""

def tbl_issue_thread_interactions():
    """TABLE issue_thread_interactions — 19 columns, 5 foreign keys. src: packages/db/src/migrations/0063_issue_thread_interactions.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_kind = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_continuation_policy = 'text DEFAULT'
    col_source_comment_id = 'uuid'
    col_source_run_id = 'uuid'
    col_title = 'text'
    col_summary = 'text'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_resolved_by_agent_id = 'uuid'
    col_resolved_by_user_id = 'text'
    col_payload = 'jsonb NOT NULL'
    col_result = 'jsonb'
    col_resolved_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_issues()  # FK issue_id
    tbl_companies()  # FK company_id
    tbl_issue_comments()  # FK source_comment_id
    tbl_heartbeat_runs()  # FK source_run_id
    tbl_agents()  # FK created_by_agent_id
    pass
