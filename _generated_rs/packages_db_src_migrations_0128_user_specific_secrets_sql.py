"""SQL: packages/db/src/migrations/0128_user_specific_secrets.sql"""

def tbl_user_secret_definitions():
    """TABLE user_secret_definitions — 18 columns, 3 foreign keys. src: packages/db/src/migrations/0128_user_specific_secrets.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_key = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_status = 'text DEFAULT'
    col_provider = 'text DEFAULT'
    col_managed_mode = 'text DEFAULT'
    col_provider_config_id = 'uuid'
    col_provider_metadata = 'jsonb'
    col_usage_guidance = 'text'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_updated_by_agent_id = 'uuid'
    col_updated_by_user_id = 'text'
    col_deleted_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_company_secret_provider_configs()  # FK provider_config_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_user_secret_declarations():
    """TABLE user_secret_declarations — 13 columns, 2 foreign keys. src: packages/db/src/migrations/0128_user_specific_secrets.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_user_secret_definition_id = 'uuid NOT NULL'
    col_target_type = 'text NOT NULL'
    col_target_id = 'text NOT NULL'
    col_config_path = 'text NOT NULL'
    col_env_key = 'text NOT NULL'
    col_version_selector = 'text DEFAULT'
    col_required = 'boolean DEFAULT true NOT NULL'
    col_allow_missing_override = 'boolean DEFAULT false NOT NULL'
    col_label = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_user_secret_definitions()  # FK user_secret_definition_id
    pass
