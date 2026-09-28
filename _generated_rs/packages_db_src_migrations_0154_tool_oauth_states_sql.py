"""SQL: packages/db/src/migrations/0154_tool_oauth_states.sql"""

def tbl_tool_oauth_states():
    """TABLE tool_oauth_states — 6 columns, 2 foreign keys. src: packages/db/src/migrations/0154_tool_oauth_states.sql"""
    col_state = 'text PRIMARY KEY NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_connection_id = 'uuid NOT NULL'
    col_code_verifier = 'text NOT NULL'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_connections()  # FK connection_id
    pass
