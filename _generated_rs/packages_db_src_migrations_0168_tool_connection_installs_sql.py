"""SQL: packages/db/src/migrations/0168_tool_connection_installs.sql"""

def tbl_tool_connection_installs():
    """TABLE tool_connection_installs — 8 columns, 3 foreign keys. src: packages/db/src/migrations/0168_tool_connection_installs.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_connection_id = 'uuid NOT NULL'
    col_target_type = 'text NOT NULL'
    col_target_id = 'text NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_connections()  # FK connection_id
    tbl_agents()  # FK created_by_agent_id
    pass
