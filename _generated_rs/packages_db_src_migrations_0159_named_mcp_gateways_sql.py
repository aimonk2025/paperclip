"""SQL: packages/db/src/migrations/0159_named_mcp_gateways.sql"""

def tbl_tool_mcp_gateways():
    """TABLE tool_mcp_gateways — 15 columns, 5 foreign keys. src: packages/db/src/migrations/0159_named_mcp_gateways.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_slug = 'text NOT NULL'
    col_description = 'text'
    col_status = 'text DEFAULT'
    col_profile_id = 'uuid NOT NULL'
    col_agent_id = 'uuid'
    col_project_id = 'uuid'
    col_issue_id = 'uuid'
    col_metadata = 'jsonb DEFAULT'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_profiles()  # FK profile_id
    tbl_agents()  # FK agent_id
    tbl_projects()  # FK project_id
    tbl_issues()  # FK issue_id
    pass

def tbl_tool_mcp_gateway_tokens():
    """TABLE tool_mcp_gateway_tokens — 12 columns, 3 foreign keys. src: packages/db/src/migrations/0159_named_mcp_gateways.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_gateway_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_token_hash = 'text NOT NULL'
    col_expires_at = 'timestamp with time zone'
    col_last_used_at = 'timestamp with time zone'
    col_revoked_at = 'timestamp with time zone'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_mcp_gateways()  # FK gateway_id
    tbl_agents()  # FK expiry_override_by_agent_id
    pass
