"""SQL: packages/db/src/migrations/0151_tool_gateway_sessions.sql"""

def tbl_tool_gateway_sessions():
    """TABLE tool_gateway_sessions — 12 columns, 7 foreign keys. src: packages/db/src/migrations/0151_tool_gateway_sessions.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_run_id = 'uuid NOT NULL'
    col_issue_id = 'uuid'
    col_project_id = 'uuid'
    col_token_hash = 'text NOT NULL'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_last_used_at = 'timestamp with time zone'
    col_revoked_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    tbl_heartbeat_runs()  # FK run_id
    tbl_issues()  # FK issue_id
    tbl_projects()  # FK project_id
    tbl_tool_mcp_gateways()  # FK gateway_id
    tbl_tool_mcp_gateway_tokens()  # FK gateway_token_id
    pass
