"""SQL: packages/db/src/migrations/0029_plugin_tables.sql"""

def tbl_plugins():
    """TABLE plugins — 13 columns, 0 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_plugin_key = 'text NOT NULL'
    col_package_name = 'text NOT NULL'
    col_package_path = 'text'
    col_version = 'text NOT NULL'
    col_api_version = 'integer DEFAULT 1 NOT NULL'
    col_categories = 'jsonb DEFAULT'
    col_manifest_json = 'jsonb NOT NULL'
    col_status = 'text DEFAULT'
    col_install_order = 'integer'
    col_last_error = 'text'
    col_installed_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    pass

def tbl_plugin_config():
    """TABLE plugin_config — 6 columns, 2 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_config_json = 'jsonb DEFAULT'
    col_last_error = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_plugins()  # FK plugin_id
    pass

def tbl_plugin_state():
    """TABLE plugin_state — 8 columns, 1 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_scope_kind = 'text NOT NULL'
    col_scope_id = 'text'
    col_namespace = 'text DEFAULT'
    col_state_key = 'text NOT NULL'
    col_value_json = 'jsonb NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_plugins()  # FK plugin_id
    pass

def tbl_plugin_entities():
    """TABLE plugin_entities — 11 columns, 2 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_entity_type = 'text NOT NULL'
    col_scope_kind = 'text NOT NULL'
    col_scope_id = 'text'
    col_external_id = 'text'
    col_title = 'text'
    col_status = 'text'
    col_data = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_plugins()  # FK plugin_id
    tbl_companies()  # FK company_id
    pass

def tbl_plugin_jobs():
    """TABLE plugin_jobs — 9 columns, 1 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_job_key = 'text NOT NULL'
    col_schedule = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_last_run_at = 'timestamp with time zone'
    col_next_run_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_plugins()  # FK plugin_id
    pass

def tbl_plugin_job_runs():
    """TABLE plugin_job_runs — 11 columns, 3 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_job_id = 'uuid NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_trigger = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_duration_ms = 'integer'
    col_error = 'text'
    col_logs = 'jsonb DEFAULT'
    col_started_at = 'timestamp with time zone'
    col_finished_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_plugin_jobs()  # FK job_id
    tbl_plugins()  # FK plugin_id
    tbl_companies()  # FK company_id
    pass

def tbl_plugin_webhook_deliveries():
    """TABLE plugin_webhook_deliveries — 12 columns, 2 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_webhook_key = 'text NOT NULL'
    col_external_id = 'text'
    col_status = 'text DEFAULT'
    col_duration_ms = 'integer'
    col_error = 'text'
    col_payload = 'jsonb NOT NULL'
    col_headers = 'jsonb DEFAULT'
    col_started_at = 'timestamp with time zone'
    col_finished_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_plugins()  # FK plugin_id
    tbl_companies()  # FK company_id
    pass

def tbl_plugin_company_settings():
    """TABLE plugin_company_settings — 8 columns, 2 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_settings_json = 'jsonb DEFAULT'
    col_last_error = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_enabled = 'boolean DEFAULT true NOT NULL'
    tbl_companies()  # FK company_id
    tbl_plugins()  # FK plugin_id
    pass

def tbl_plugin_logs():
    """TABLE plugin_logs — 6 columns, 2 foreign keys. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid()'
    col_plugin_id = 'uuid NOT NULL'
    col_level = 'text NOT NULL DEFAULT'
    col_message = 'text NOT NULL'
    col_meta = 'jsonb'
    col_created_at = 'timestamp with time zone NOT NULL DEFAULT now()'
    tbl_plugins()  # FK plugin_id
    tbl_companies()  # FK company_id
    pass

def idx_plugins_plugin_key_idx():
    """INDEX on plugins. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugins()

def idx_plugins_status_idx():
    """INDEX on plugins. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugins()

def idx_plugin_config_plugin_id_idx():
    """INDEX on plugin_config. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_config()

def idx_plugin_state_plugin_scope_idx():
    """INDEX on plugin_state. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_state()

def idx_plugin_entities_plugin_idx():
    """INDEX on plugin_entities. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_entities()

def idx_plugin_entities_type_idx():
    """INDEX on plugin_entities. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_entities()

def idx_plugin_entities_scope_idx():
    """INDEX on plugin_entities. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_entities()

def idx_plugin_entities_external_idx():
    """INDEX on plugin_entities. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_entities()

def idx_plugin_jobs_plugin_idx():
    """INDEX on plugin_jobs. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_jobs()

def idx_plugin_jobs_next_run_idx():
    """INDEX on plugin_jobs. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_jobs()

def idx_plugin_jobs_unique_idx():
    """INDEX on plugin_jobs. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_jobs()

def idx_plugin_job_runs_job_idx():
    """INDEX on plugin_job_runs. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_job_runs()

def idx_plugin_job_runs_plugin_idx():
    """INDEX on plugin_job_runs. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_job_runs()

def idx_plugin_job_runs_status_idx():
    """INDEX on plugin_job_runs. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_job_runs()

def idx_plugin_webhook_deliveries_plugin_idx():
    """INDEX on plugin_webhook_deliveries. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_webhook_deliveries()

def idx_plugin_webhook_deliveries_status_idx():
    """INDEX on plugin_webhook_deliveries. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_webhook_deliveries()

def idx_plugin_webhook_deliveries_key_idx():
    """INDEX on plugin_webhook_deliveries. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_webhook_deliveries()

def idx_plugin_company_settings_company_idx():
    """INDEX on plugin_company_settings. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_company_settings()

def idx_plugin_company_settings_plugin_idx():
    """INDEX on plugin_company_settings. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_company_settings()

def idx_plugin_company_settings_company_plugin_uq():
    """INDEX on plugin_company_settings. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_company_settings()

def idx_plugin_logs_plugin_time_idx():
    """INDEX on plugin_logs. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_logs()

def idx_plugin_logs_level_idx():
    """INDEX on plugin_logs. src: packages/db/src/migrations/0029_plugin_tables.sql"""
    tbl_plugin_logs()
