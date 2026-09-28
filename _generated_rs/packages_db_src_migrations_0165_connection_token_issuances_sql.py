"""SQL: packages/db/src/migrations/0165_connection_token_issuances.sql"""

def tbl_connection_token_issuances():
    """TABLE connection_token_issuances — 19 columns, 7 foreign keys. src: packages/db/src/migrations/0165_connection_token_issuances.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_application_id = 'uuid'
    col_connection_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_run_id = 'uuid'
    col_issue_id = 'uuid'
    col_project_id = 'uuid'
    col_responsible_user_id = 'text'
    col_path = 'text NOT NULL'
    col_requested_scope = 'jsonb DEFAULT'
    col_issued_scope = 'jsonb DEFAULT'
    col_ttl_seconds = 'integer'
    col_expires_at = 'timestamp with time zone'
    col_token_hash = 'text'
    col_outcome = 'text NOT NULL'
    col_error_code = 'text'
    col_metadata = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_applications()  # FK application_id
    tbl_tool_connections()  # FK connection_id
    tbl_agents()  # FK agent_id
    tbl_heartbeat_runs()  # FK run_id
    tbl_issues()  # FK issue_id
    tbl_projects()  # FK project_id
    pass
