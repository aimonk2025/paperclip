"""SQL: packages/db/src/migrations/0044_illegal_toad.sql"""

def tbl_board_api_keys():
    """TABLE board_api_keys — 8 columns, 1 foreign keys. src: packages/db/src/migrations/0044_illegal_toad.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_user_id = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_key_hash = 'text NOT NULL'
    col_last_used_at = 'timestamp with time zone'
    col_revoked_at = 'timestamp with time zone'
    col_expires_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_user()  # FK user_id
    pass

def tbl_cli_auth_challenges():
    """TABLE cli_auth_challenges — 15 columns, 3 foreign keys. src: packages/db/src/migrations/0044_illegal_toad.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_secret_hash = 'text NOT NULL'
    col_command = 'text NOT NULL'
    col_client_name = 'text'
    col_requested_access = 'text DEFAULT'
    col_requested_company_id = 'uuid'
    col_pending_key_hash = 'text NOT NULL'
    col_pending_key_name = 'text NOT NULL'
    col_approved_by_user_id = 'text'
    col_board_api_key_id = 'uuid'
    col_approved_at = 'timestamp with time zone'
    col_cancelled_at = 'timestamp with time zone'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK requested_company_id
    tbl_user()  # FK approved_by_user_id
    tbl_board_api_keys()  # FK board_api_key_id
    pass
