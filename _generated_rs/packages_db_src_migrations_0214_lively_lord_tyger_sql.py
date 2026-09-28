"""SQL: packages/db/src/migrations/0214_lively_lord_tyger.sql"""

def tbl_adapter_auth_sessions():
    """TABLE adapter_auth_sessions — 12 columns, 2 foreign keys. src: packages/db/src/migrations/0214_lively_lord_tyger.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_environment_id = 'uuid NOT NULL'
    col_adapter_type = 'text NOT NULL'
    col_started_by_user_id = 'text NOT NULL'
    col_provider_lease_id = 'text'
    col_status = 'text DEFAULT'
    col_expires_at = 'timestamp with time zone'
    col_finished_at = 'timestamp with time zone'
    col_failure_reason = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_environments()  # FK environment_id
    pass

def idx_adapter_auth_sessions_company_status_idx():
    """INDEX on adapter_auth_sessions. src: packages/db/src/migrations/0214_lively_lord_tyger.sql"""
    tbl_adapter_auth_sessions()

def idx_adapter_auth_sessions_company_adapter_active_uq():
    """INDEX on adapter_auth_sessions. src: packages/db/src/migrations/0214_lively_lord_tyger.sql"""
    tbl_adapter_auth_sessions()

def idx_adapter_auth_sessions_environment_idx():
    """INDEX on adapter_auth_sessions. src: packages/db/src/migrations/0214_lively_lord_tyger.sql"""
    tbl_adapter_auth_sessions()

def idx_adapter_auth_sessions_expires_idx():
    """INDEX on adapter_auth_sessions. src: packages/db/src/migrations/0214_lively_lord_tyger.sql"""
    tbl_adapter_auth_sessions()

def idx_adapter_auth_sessions_provider_lease_idx():
    """INDEX on adapter_auth_sessions. src: packages/db/src/migrations/0214_lively_lord_tyger.sql"""
    tbl_adapter_auth_sessions()
