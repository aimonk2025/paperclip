"""SQL: packages/db/src/migrations/0221_swift_justin_hammer.sql"""

def tbl_claude_setup_token_sessions():
    """TABLE claude_setup_token_sessions — 12 columns, 2 foreign keys. src: packages/db/src/migrations/0221_swift_justin_hammer.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_session_id = 'text NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_owner_user_id = 'text NOT NULL'
    col_adapter_type = 'text NOT NULL'
    col_environment_id = 'uuid NOT NULL'
    col_lease_id = 'text'
    col_state = 'text DEFAULT'
    col_deadline_at = 'timestamp with time zone NOT NULL'
    col_bound_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_environments()  # FK environment_id
    pass

def idx_claude_setup_token_sessions_active_uq():
    """INDEX on claude_setup_token_sessions. src: packages/db/src/migrations/0221_swift_justin_hammer.sql"""
    tbl_claude_setup_token_sessions()

def idx_claude_setup_token_sessions_session_id_uq():
    """INDEX on claude_setup_token_sessions. src: packages/db/src/migrations/0221_swift_justin_hammer.sql"""
    tbl_claude_setup_token_sessions()

def idx_claude_setup_token_sessions_deadline_idx():
    """INDEX on claude_setup_token_sessions. src: packages/db/src/migrations/0221_swift_justin_hammer.sql"""
    tbl_claude_setup_token_sessions()
