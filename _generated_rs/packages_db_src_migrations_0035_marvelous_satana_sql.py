"""SQL: packages/db/src/migrations/0035_marvelous_satana.sql"""

def tbl_execution_workspaces():
    """TABLE execution_workspaces — 24 columns, 5 foreign keys. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid NOT NULL'
    col_project_workspace_id = 'uuid'
    col_source_issue_id = 'uuid'
    col_mode = 'text NOT NULL'
    col_strategy_type = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_cwd = 'text'
    col_repo_url = 'text'
    col_base_ref = 'text'
    col_branch_name = 'text'
    col_provider_type = 'text DEFAULT'
    col_provider_ref = 'text'
    col_derived_from_execution_workspace_id = 'uuid'
    col_last_used_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_opened_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_closed_at = 'timestamp with time zone'
    col_cleanup_eligible_at = 'timestamp with time zone'
    col_cleanup_reason = 'text'
    col_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    tbl_project_workspaces()  # FK project_workspace_id
    tbl_issues()  # FK source_issue_id
    tbl_execution_workspaces()  # FK derived_from_execution_workspace_id
    pass

def tbl_issue_work_products():
    """TABLE issue_work_products — 20 columns, 6 foreign keys. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid'
    col_issue_id = 'uuid NOT NULL'
    col_execution_workspace_id = 'uuid'
    col_runtime_service_id = 'uuid'
    col_type = 'text NOT NULL'
    col_provider = 'text NOT NULL'
    col_external_id = 'text'
    col_title = 'text NOT NULL'
    col_url = 'text'
    col_status = 'text NOT NULL'
    col_review_state = 'text DEFAULT'
    col_is_primary = 'boolean DEFAULT false NOT NULL'
    col_health_status = 'text DEFAULT'
    col_summary = 'text'
    col_metadata = 'jsonb'
    col_created_by_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    tbl_issues()  # FK issue_id
    tbl_execution_workspaces()  # FK execution_workspace_id
    tbl_workspace_runtime_services()  # FK runtime_service_id
    tbl_heartbeat_runs()  # FK created_by_run_id
    pass

def idx_execution_workspaces_company_project_status_idx():
    """INDEX on execution_workspaces. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_execution_workspaces()

def idx_execution_workspaces_company_project_workspace_status_idx():
    """INDEX on execution_workspaces. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_execution_workspaces()

def idx_execution_workspaces_company_source_issue_idx():
    """INDEX on execution_workspaces. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_execution_workspaces()

def idx_execution_workspaces_company_last_used_idx():
    """INDEX on execution_workspaces. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_execution_workspaces()

def idx_execution_workspaces_company_branch_idx():
    """INDEX on execution_workspaces. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_execution_workspaces()

def idx_issue_work_products_company_issue_type_idx():
    """INDEX on issue_work_products. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_issue_work_products()

def idx_issue_work_products_company_execution_workspace_type_idx():
    """INDEX on issue_work_products. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_issue_work_products()

def idx_issue_work_products_company_provider_external_id_idx():
    """INDEX on issue_work_products. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_issue_work_products()

def idx_issue_work_products_company_updated_idx():
    """INDEX on issue_work_products. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_issue_work_products()

def idx_issues_company_project_workspace_idx():
    """INDEX on issues. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_issues()

def idx_issues_company_execution_workspace_idx():
    """INDEX on issues. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_issues()

def idx_project_workspaces_project_source_type_idx():
    """INDEX on project_workspaces. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_project_workspaces()

def idx_project_workspaces_company_shared_key_idx():
    """INDEX on project_workspaces. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_project_workspaces()

def idx_project_workspaces_project_remote_ref_idx():
    """INDEX on project_workspaces. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_project_workspaces()

def idx_workspace_runtime_services_company_execution_workspace_status_idx():
    """INDEX on workspace_runtime_services. src: packages/db/src/migrations/0035_marvelous_satana.sql"""
    tbl_workspace_runtime_services()
