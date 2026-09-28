"""SQL: packages/db/src/migrations/0153_tool_stdio_command_templates.sql"""

def tbl_tool_stdio_command_templates():
    """TABLE tool_stdio_command_templates — 15 columns, 2 foreign keys. src: packages/db/src/migrations/0153_tool_stdio_command_templates.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_template_key = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_status = 'text DEFAULT'
    col_command = 'text NOT NULL'
    col_args = 'jsonb DEFAULT'
    col_env_keys = 'jsonb DEFAULT'
    col_tools = 'jsonb DEFAULT'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_disabled_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass
