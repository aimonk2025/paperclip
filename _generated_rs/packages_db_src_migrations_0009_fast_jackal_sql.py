"""SQL: packages/db/src/migrations/0009_fast_jackal.sql"""

def tbl_company_secret_versions():
    """TABLE company_secret_versions — 9 columns, 2 foreign keys. src: packages/db/src/migrations/0009_fast_jackal.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_secret_id = 'uuid NOT NULL'
    col_version = 'integer NOT NULL'
    col_material = 'jsonb NOT NULL'
    col_value_sha256 = 'text NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_revoked_at = 'timestamp with time zone'
    tbl_company_secrets()  # FK secret_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_company_secrets():
    """TABLE company_secrets — 11 columns, 4 foreign keys. src: packages/db/src/migrations/0009_fast_jackal.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_provider = 'text DEFAULT'
    col_external_ref = 'text'
    col_latest_version = 'integer DEFAULT 1 NOT NULL'
    col_description = 'text'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_user_secret_definitions()  # FK user_secret_definition_id
    tbl_company_secret_provider_configs()  # FK provider_config_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass

def idx_company_secret_versions_secret_idx():
    """INDEX on company_secret_versions. src: packages/db/src/migrations/0009_fast_jackal.sql"""
    tbl_company_secret_versions()

def idx_company_secret_versions_value_sha256_idx():
    """INDEX on company_secret_versions. src: packages/db/src/migrations/0009_fast_jackal.sql"""
    tbl_company_secret_versions()

def idx_company_secret_versions_secret_version_uq():
    """INDEX on company_secret_versions. src: packages/db/src/migrations/0009_fast_jackal.sql"""
    tbl_company_secret_versions()

def idx_company_secrets_company_idx():
    """INDEX on company_secrets. src: packages/db/src/migrations/0009_fast_jackal.sql"""
    tbl_company_secrets()

def idx_company_secrets_company_provider_idx():
    """INDEX on company_secrets. src: packages/db/src/migrations/0009_fast_jackal.sql"""
    tbl_company_secrets()

def idx_company_secrets_company_name_uq():
    """INDEX on company_secrets. src: packages/db/src/migrations/0009_fast_jackal.sql"""
    tbl_company_secrets()
