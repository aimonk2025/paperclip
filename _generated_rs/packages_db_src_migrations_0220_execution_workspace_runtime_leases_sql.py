"""SQL: packages/db/src/migrations/0220_execution_workspace_runtime_leases.sql"""

def tbl_execution_workspace_runtime_leases():
    """TABLE execution_workspace_runtime_leases — 14 columns, 5 foreign keys. src: packages/db/src/migrations/0220_execution_workspace_runtime_leases.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_execution_workspace_id = 'uuid NOT NULL'
    col_owner_key = 'text NOT NULL'
    col_owner_issue_id = 'uuid'
    col_owner_run_id = 'uuid'
    col_owner_agent_id = 'uuid'
    col_last_action = 'text NOT NULL'
    col_claimed_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_renewed_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_execution_workspaces()  # FK execution_workspace_id
    tbl_issues()  # FK owner_issue_id
    tbl_heartbeat_runs()  # FK owner_run_id
    tbl_agents()  # FK owner_agent_id
    pass

def idx_execution_workspace_runtime_leases_company_workspace_idx():
    """INDEX on execution_workspace_runtime_leases. src: packages/db/src/migrations/0220_execution_workspace_runtime_leases.sql"""
    tbl_execution_workspace_runtime_leases()

def idx_execution_workspace_runtime_leases_company_owner_idx():
    """INDEX on execution_workspace_runtime_leases. src: packages/db/src/migrations/0220_execution_workspace_runtime_leases.sql"""
    tbl_execution_workspace_runtime_leases()

def idx_execution_workspace_runtime_leases_expires_at_idx():
    """INDEX on execution_workspace_runtime_leases. src: packages/db/src/migrations/0220_execution_workspace_runtime_leases.sql"""
    tbl_execution_workspace_runtime_leases()
