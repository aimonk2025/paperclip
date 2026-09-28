"""SQL: packages/db/src/migrations/0006_overjoyed_mister_sinister.sql"""

def tbl_agent_config_revisions():
    """TABLE agent_config_revisions — 11 columns, 2 foreign keys. src: packages/db/src/migrations/0006_overjoyed_mister_sinister.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_source = 'text DEFAULT'
    col_rolled_back_from_revision_id = 'uuid'
    col_changed_keys = 'jsonb DEFAULT'
    col_before_config = 'jsonb NOT NULL'
    col_after_config = 'jsonb NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    pass

def tbl_issue_approvals():
    """TABLE issue_approvals — 6 columns, 4 foreign keys. src: packages/db/src/migrations/0006_overjoyed_mister_sinister.sql"""
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_approval_id = 'uuid NOT NULL'
    col_linked_by_agent_id = 'uuid'
    col_linked_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    tbl_approvals()  # FK approval_id
    tbl_agents()  # FK linked_by_agent_id
    pass

def idx_agent_config_revisions_company_agent_created_idx():
    """INDEX on agent_config_revisions. src: packages/db/src/migrations/0006_overjoyed_mister_sinister.sql"""
    tbl_agent_config_revisions()

def idx_agent_config_revisions_agent_created_idx():
    """INDEX on agent_config_revisions. src: packages/db/src/migrations/0006_overjoyed_mister_sinister.sql"""
    tbl_agent_config_revisions()

def idx_issue_approvals_issue_idx():
    """INDEX on issue_approvals. src: packages/db/src/migrations/0006_overjoyed_mister_sinister.sql"""
    tbl_issue_approvals()

def idx_issue_approvals_approval_idx():
    """INDEX on issue_approvals. src: packages/db/src/migrations/0006_overjoyed_mister_sinister.sql"""
    tbl_issue_approvals()

def idx_issue_approvals_company_idx():
    """INDEX on issue_approvals. src: packages/db/src/migrations/0006_overjoyed_mister_sinister.sql"""
    tbl_issue_approvals()
