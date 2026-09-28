"""SQL: packages/db/src/migrations/0066_issue_tree_holds.sql"""

def tbl_issue_tree_holds():
    """TABLE issue_tree_holds — 20 columns, 4 foreign keys. src: packages/db/src/migrations/0066_issue_tree_holds.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_root_issue_id = 'uuid NOT NULL'
    col_mode = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_reason = 'text'
    col_release_policy = 'jsonb'
    col_created_by_actor_type = 'text DEFAULT'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_by_run_id = 'uuid'
    col_released_at = 'timestamp with time zone'
    col_released_by_actor_type = 'text'
    col_released_by_agent_id = 'uuid'
    col_released_by_user_id = 'text'
    col_released_by_run_id = 'uuid'
    col_release_reason = 'text'
    col_release_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK root_issue_id
    tbl_agents()  # FK created_by_agent_id
    tbl_heartbeat_runs()  # FK created_by_run_id
    pass

def tbl_issue_tree_hold_members():
    """TABLE issue_tree_hold_members — 16 columns, 5 foreign keys. src: packages/db/src/migrations/0066_issue_tree_holds.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_hold_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_parent_issue_id = 'uuid'
    col_depth = 'integer DEFAULT 0 NOT NULL'
    col_issue_identifier = 'text'
    col_issue_title = 'text NOT NULL'
    col_issue_status = 'text NOT NULL'
    col_assignee_agent_id = 'uuid'
    col_assignee_user_id = 'text'
    col_active_run_id = 'uuid'
    col_active_run_status = 'text'
    col_skipped = 'boolean DEFAULT false NOT NULL'
    col_skip_reason = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issue_tree_holds()  # FK hold_id
    tbl_issues()  # FK issue_id
    tbl_agents()  # FK assignee_agent_id
    tbl_heartbeat_runs()  # FK active_run_id
    pass
