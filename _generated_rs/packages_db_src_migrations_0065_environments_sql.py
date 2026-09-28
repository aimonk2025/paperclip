"""SQL: packages/db/src/migrations/0065_environments.sql"""

def tbl_environments():
    """TABLE environments — 10 columns, 1 foreign keys. src: packages/db/src/migrations/0065_environments.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_driver = 'text DEFAULT'
    col_status = 'text DEFAULT'
    col_config = 'jsonb DEFAULT'
    col_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def tbl_environment_leases():
    """TABLE environment_leases — 19 columns, 5 foreign keys. src: packages/db/src/migrations/0065_environments.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_environment_id = 'uuid NOT NULL'
    col_execution_workspace_id = 'uuid'
    col_issue_id = 'uuid'
    col_heartbeat_run_id = 'uuid'
    col_status = 'text DEFAULT'
    col_lease_policy = 'text DEFAULT'
    col_provider = 'text'
    col_provider_lease_id = 'text'
    col_acquired_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_last_used_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_expires_at = 'timestamp with time zone'
    col_released_at = 'timestamp with time zone'
    col_failure_reason = 'text'
    col_cleanup_status = 'text'
    col_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_environments()  # FK environment_id
    tbl_companies()  # FK company_id
    tbl_execution_workspaces()  # FK execution_workspace_id
    tbl_issues()  # FK issue_id
    tbl_heartbeat_runs()  # FK heartbeat_run_id
    pass

def idx_environments_company_status_idx():
    """INDEX on environments. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environments()

def idx_environments_company_driver_idx():
    """INDEX on environments. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environments()

def idx_environments_company_name_idx():
    """INDEX on environments. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environments()

def idx_environment_leases_company_environment_status_idx():
    """INDEX on environment_leases. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environment_leases()

def idx_environment_leases_company_execution_workspace_idx():
    """INDEX on environment_leases. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environment_leases()

def idx_environment_leases_company_issue_idx():
    """INDEX on environment_leases. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environment_leases()

def idx_environment_leases_heartbeat_run_idx():
    """INDEX on environment_leases. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environment_leases()

def idx_environment_leases_company_last_used_idx():
    """INDEX on environment_leases. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environment_leases()

def idx_environment_leases_provider_lease_idx():
    """INDEX on environment_leases. src: packages/db/src/migrations/0065_environments.sql"""
    tbl_environment_leases()
