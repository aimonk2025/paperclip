"""SQL: packages/db/src/migrations/0037_friendly_eddie_brock.sql"""

def tbl_workspace_operations():
    """TABLE workspace_operations — 21 columns, 4 foreign keys. src: packages/db/src/migrations/0037_friendly_eddie_brock.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_execution_workspace_id = 'uuid'
    col_heartbeat_run_id = 'uuid'
    col_phase = 'text NOT NULL'
    col_command = 'text'
    col_cwd = 'text'
    col_status = 'text DEFAULT'
    col_exit_code = 'integer'
    col_log_store = 'text'
    col_log_ref = 'text'
    col_log_bytes = 'bigint'
    col_log_sha256 = 'text'
    col_log_compressed = 'boolean DEFAULT false NOT NULL'
    col_stdout_excerpt = 'text'
    col_stderr_excerpt = 'text'
    col_metadata = 'jsonb'
    col_started_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_finished_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_issues()  # FK issue_id
    tbl_companies()  # FK company_id
    tbl_execution_workspaces()  # FK execution_workspace_id
    tbl_heartbeat_runs()  # FK heartbeat_run_id
    pass

def idx_workspace_operations_company_run_started_idx():
    """INDEX on workspace_operations. src: packages/db/src/migrations/0037_friendly_eddie_brock.sql"""
    tbl_workspace_operations()

def idx_workspace_operations_company_workspace_started_idx():
    """INDEX on workspace_operations. src: packages/db/src/migrations/0037_friendly_eddie_brock.sql"""
    tbl_workspace_operations()
