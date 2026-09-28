"""SQL: packages/db/src/migrations/0083_company_secret_provider_configs.sql"""

def tbl_company_secret_provider_configs():
    """TABLE company_secret_provider_configs — 16 columns, 2 foreign keys. src: packages/db/src/migrations/0083_company_secret_provider_configs.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_provider = 'text NOT NULL'
    col_display_name = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_is_default = 'boolean DEFAULT false NOT NULL'
    col_config = 'jsonb DEFAULT'
    col_health_status = 'text'
    col_health_checked_at = 'timestamp with time zone'
    col_health_message = 'text'
    col_health_details = 'jsonb'
    col_disabled_at = 'timestamp with time zone'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass
