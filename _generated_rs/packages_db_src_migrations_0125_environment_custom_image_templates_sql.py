"""SQL: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""

def tbl_environment_custom_image_templates():
    """TABLE environment_custom_image_templates — 17 columns, 4 foreign keys. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_environment_id = 'uuid NOT NULL'
    col_provider = 'text NOT NULL'
    col_template_kind = 'text DEFAULT'
    col_template_ref = 'text NOT NULL'
    col_source_template_ref = 'text'
    col_source_environment_config_fingerprint = 'text'
    col_status = 'text DEFAULT'
    col_created_by_user_id = 'text'
    col_created_by_agent_id = 'uuid'
    col_captured_at = 'timestamp with time zone'
    col_last_used_at = 'timestamp with time zone'
    col_superseded_by_template_id = 'uuid'
    col_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_environments()  # FK environment_id
    tbl_agents()  # FK created_by_agent_id
    tbl_environment_custom_image_templates()  # FK superseded_by_template_id
    pass

def tbl_environment_custom_image_setup_sessions():
    """TABLE environment_custom_image_setup_sessions — 20 columns, 5 foreign keys. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_environment_id = 'uuid NOT NULL'
    col_template_id = 'uuid'
    col_promoted_template_id = 'uuid'
    col_provider = 'text NOT NULL'
    col_provider_lease_id = 'text'
    col_environment_lease_id = 'uuid'
    col_status = 'text DEFAULT'
    col_started_by_user_id = 'text'
    col_started_by_agent_id = 'uuid'
    col_base_template_ref = 'text'
    col_expires_at = 'timestamp with time zone'
    col_finished_at = 'timestamp with time zone'
    col_failure_reason = 'text'
    col_connection_summary = 'jsonb'
    col_connection_secret_ref = 'text'
    col_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_environments()  # FK environment_id
    tbl_environment_custom_image_templates()  # FK template_id
    tbl_environment_leases()  # FK environment_lease_id
    tbl_agents()  # FK started_by_agent_id
    pass

def idx_environment_custom_image_templates_company_environment_status_idx():
    """INDEX on environment_custom_image_templates. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_templates()

def idx_environment_custom_image_templates_company_provider_status_idx():
    """INDEX on environment_custom_image_templates. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_templates()

def idx_environment_custom_image_templates_company_environment_active_uq():
    """INDEX on environment_custom_image_templates. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_templates()

def idx_environment_custom_image_templates_superseded_by_idx():
    """INDEX on environment_custom_image_templates. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_templates()

def idx_environment_custom_image_templates_company_last_used_idx():
    """INDEX on environment_custom_image_templates. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_templates()

def idx_environment_custom_image_setup_sessions_company_environment_status_idx():
    """INDEX on environment_custom_image_setup_sessions. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_setup_sessions()

def idx_environment_custom_image_setup_sessions_company_environment_active_uq():
    """INDEX on environment_custom_image_setup_sessions. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_setup_sessions()

def idx_environment_custom_image_setup_sessions_company_template_idx():
    """INDEX on environment_custom_image_setup_sessions. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_setup_sessions()

def idx_environment_custom_image_setup_sessions_company_promoted_template_idx():
    """INDEX on environment_custom_image_setup_sessions. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_setup_sessions()

def idx_environment_custom_image_setup_sessions_company_expires_idx():
    """INDEX on environment_custom_image_setup_sessions. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_setup_sessions()

def idx_environment_custom_image_setup_sessions_provider_lease_idx():
    """INDEX on environment_custom_image_setup_sessions. src: packages/db/src/migrations/0125_environment_custom_image_templates.sql"""
    tbl_environment_custom_image_setup_sessions()
