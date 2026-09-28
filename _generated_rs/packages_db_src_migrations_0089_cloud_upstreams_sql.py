"""SQL: packages/db/src/migrations/0089_cloud_upstreams.sql"""

def tbl_cloud_upstream_connections():
    """TABLE cloud_upstream_connections — 29 columns, 1 foreign keys. src: packages/db/src/migrations/0089_cloud_upstreams.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_remote_url = 'text NOT NULL'
    col_source_instance_id = 'text NOT NULL'
    col_source_instance_fingerprint = 'text NOT NULL'
    col_source_public_key = 'text NOT NULL'
    col_private_key_pem = 'text NOT NULL'
    col_token_status = 'text NOT NULL'
    col_scopes = 'text[] DEFAULT'
    col_authorized_global_user_id = 'text'
    col_access_token = 'text'
    col_token_id = 'text'
    col_token_expires_at = 'timestamp with time zone'
    col_target_stack_id = 'text NOT NULL'
    col_target_stack_slug = 'text'
    col_target_stack_display_name = 'text'
    col_target_company_id = 'text NOT NULL'
    col_target_origin = 'text NOT NULL'
    col_target_primary_host = 'text NOT NULL'
    col_target_product = 'text NOT NULL'
    col_target_schema_major = 'integer NOT NULL'
    col_target_max_chunk_bytes = 'integer NOT NULL'
    col_pending_state = 'text'
    col_pending_code_verifier = 'text'
    col_pending_redirect_uri = 'text'
    col_pending_token_url = 'text'
    col_last_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def tbl_cloud_upstream_runs():
    """TABLE cloud_upstream_runs — 20 columns, 2 foreign keys. src: packages/db/src/migrations/0089_cloud_upstreams.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_connection_id = 'uuid NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_remote_run_id = 'text'
    col_status = 'text NOT NULL'
    col_active_step = 'text NOT NULL'
    col_progress_percent = 'integer DEFAULT 0 NOT NULL'
    col_dry_run = 'boolean DEFAULT false NOT NULL'
    col_retry_of_run_id = 'uuid'
    col_summary = 'jsonb DEFAULT'
    col_warnings = 'jsonb DEFAULT'
    col_conflicts = 'jsonb DEFAULT'
    col_events = 'jsonb DEFAULT'
    col_report = 'jsonb DEFAULT'
    col_idempotency_key = 'text NOT NULL'
    col_manifest_hash = 'text NOT NULL'
    col_target_url = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_completed_at = 'timestamp with time zone'
    tbl_cloud_upstream_connections()  # FK connection_id
    tbl_companies()  # FK company_id
    pass
