"""SQL: packages/db/src/migrations/0026_lying_pete_wisdom.sql"""

def tbl_workspace_runtime_services():
    """TABLE workspace_runtime_services — 26 columns, 7 foreign keys. src: packages/db/src/migrations/0026_lying_pete_wisdom.sql"""
    col_id = 'uuid PRIMARY KEY NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid'
    col_project_workspace_id = 'uuid'
    col_issue_id = 'uuid'
    col_scope_type = 'text NOT NULL'
    col_scope_id = 'text'
    col_service_name = 'text NOT NULL'
    col_status = 'text NOT NULL'
    col_lifecycle = 'text NOT NULL'
    col_reuse_key = 'text'
    col_command = 'text'
    col_cwd = 'text'
    col_port = 'integer'
    col_url = 'text'
    col_provider = 'text NOT NULL'
    col_provider_ref = 'text'
    col_owner_agent_id = 'uuid'
    col_started_by_run_id = 'uuid'
    col_last_used_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_started_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_stopped_at = 'timestamp with time zone'
    col_stop_policy = 'jsonb'
    col_health_status = 'text DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    tbl_project_workspaces()  # FK project_workspace_id
    tbl_issues()  # FK issue_id
    tbl_agents()  # FK owner_agent_id
    tbl_heartbeat_runs()  # FK started_by_run_id
    tbl_execution_workspaces()  # FK execution_workspace_id
    pass

def idx_workspace_runtime_services_company_workspace_status_idx():
    """INDEX on workspace_runtime_services. src: packages/db/src/migrations/0026_lying_pete_wisdom.sql"""
    tbl_workspace_runtime_services()

def idx_workspace_runtime_services_company_project_status_idx():
    """INDEX on workspace_runtime_services. src: packages/db/src/migrations/0026_lying_pete_wisdom.sql"""
    tbl_workspace_runtime_services()

def idx_workspace_runtime_services_run_idx():
    """INDEX on workspace_runtime_services. src: packages/db/src/migrations/0026_lying_pete_wisdom.sql"""
    tbl_workspace_runtime_services()

def idx_workspace_runtime_services_company_updated_idx():
    """INDEX on workspace_runtime_services. src: packages/db/src/migrations/0026_lying_pete_wisdom.sql"""
    tbl_workspace_runtime_services()
