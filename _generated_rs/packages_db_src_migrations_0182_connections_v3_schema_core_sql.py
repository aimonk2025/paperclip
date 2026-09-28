"""SQL: packages/db/src/migrations/0182_connections_v3_schema_core.sql"""

def tbl_connection_grants():
    """TABLE connection_grants — 17 columns, 3 foreign keys. src: packages/db/src/migrations/0182_connections_v3_schema_core.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_connection_id = 'uuid NOT NULL'
    col_kind = 'text NOT NULL'
    col_subject_user_id = 'text'
    col_provider_tenant = 'jsonb'
    col_credential_secret_refs = 'jsonb DEFAULT'
    col_status = 'text DEFAULT'
    col_is_default = 'boolean DEFAULT false NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_revoked_at = 'timestamp with time zone'
    col_revoked_by_agent_id = 'uuid'
    col_revoked_by_user_id = 'text'
    col_last_used_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_connections()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass

def idx_tool_connections_company_uid_uq():
    """INDEX on tool_connections. src: packages/db/src/migrations/0182_connections_v3_schema_core.sql"""
    tbl_tool_connections()

def idx_connection_grants_company_connection_idx():
    """INDEX on connection_grants. src: packages/db/src/migrations/0182_connections_v3_schema_core.sql"""
    tbl_connection_grants()

def idx_connection_grants_subject_user_idx():
    """INDEX on connection_grants. src: packages/db/src/migrations/0182_connections_v3_schema_core.sql"""
    tbl_connection_grants()

def idx_connection_grants_user_uq():
    """INDEX on connection_grants. src: packages/db/src/migrations/0182_connections_v3_schema_core.sql"""
    tbl_connection_grants()

def idx_connection_grants_default_uq():
    """INDEX on connection_grants. src: packages/db/src/migrations/0182_connections_v3_schema_core.sql"""
    tbl_connection_grants()
