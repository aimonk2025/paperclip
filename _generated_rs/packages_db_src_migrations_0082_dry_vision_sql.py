"""SQL: packages/db/src/migrations/0082_dry_vision.sql"""

def tbl_company_secret_bindings():
    """TABLE company_secret_bindings — 11 columns, 2 foreign keys. src: packages/db/src/migrations/0082_dry_vision.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_secret_id = 'uuid NOT NULL'
    col_target_type = 'text NOT NULL'
    col_target_id = 'text NOT NULL'
    col_config_path = 'text NOT NULL'
    col_version_selector = 'text DEFAULT'
    col_required = 'boolean DEFAULT true NOT NULL'
    col_label = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_company_secrets()  # FK secret_id
    pass

def tbl_secret_access_events():
    """TABLE secret_access_events — 16 columns, 6 foreign keys. src: packages/db/src/migrations/0082_dry_vision.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_secret_id = 'uuid NOT NULL'
    col_version = 'integer'
    col_provider = 'text NOT NULL'
    col_actor_type = 'text NOT NULL'
    col_actor_id = 'text'
    col_consumer_type = 'text NOT NULL'
    col_consumer_id = 'text NOT NULL'
    col_config_path = 'text'
    col_issue_id = 'uuid'
    col_heartbeat_run_id = 'uuid'
    col_plugin_id = 'uuid'
    col_outcome = 'text NOT NULL'
    col_error_code = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_user_secret_definitions()  # FK user_secret_definition_id
    tbl_companies()  # FK company_id
    tbl_company_secrets()  # FK secret_id
    tbl_issues()  # FK issue_id
    tbl_heartbeat_runs()  # FK heartbeat_run_id
    tbl_plugins()  # FK plugin_id
    pass
