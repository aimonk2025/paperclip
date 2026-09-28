"""SQL: packages/db/src/migrations/0092_mighty_puma.sql"""

def tbl_issue_plan_decompositions():
    """TABLE issue_plan_decompositions — 16 columns, 6 foreign keys. src: packages/db/src/migrations/0092_mighty_puma.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_source_issue_id = 'uuid NOT NULL'
    col_accepted_plan_revision_id = 'uuid NOT NULL'
    col_accepted_interaction_id = 'uuid'
    col_status = 'text DEFAULT'
    col_request_fingerprint = 'text NOT NULL'
    col_requested_child_count = 'integer DEFAULT 0 NOT NULL'
    col_requested_children = 'jsonb DEFAULT'
    col_child_issue_ids = 'jsonb DEFAULT'
    col_owner_agent_id = 'uuid'
    col_owner_user_id = 'text'
    col_owner_run_id = 'uuid'
    col_completed_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK source_issue_id
    tbl_document_revisions()  # FK accepted_plan_revision_id
    tbl_issue_thread_interactions()  # FK accepted_interaction_id
    tbl_agents()  # FK owner_agent_id
    tbl_heartbeat_runs()  # FK owner_run_id
    pass

def idx_issue_plan_decompositions_company_source_status_idx():
    """INDEX on issue_plan_decompositions. src: packages/db/src/migrations/0092_mighty_puma.sql"""
    tbl_issue_plan_decompositions()

def idx_issue_plan_decompositions_active_owner_idx():
    """INDEX on issue_plan_decompositions. src: packages/db/src/migrations/0092_mighty_puma.sql"""
    tbl_issue_plan_decompositions()

def idx_issue_plan_decompositions_source_revision_uq():
    """INDEX on issue_plan_decompositions. src: packages/db/src/migrations/0092_mighty_puma.sql"""
    tbl_issue_plan_decompositions()
