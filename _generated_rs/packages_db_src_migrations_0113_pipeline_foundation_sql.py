"""SQL: packages/db/src/migrations/0113_pipeline_foundation.sql"""

def tbl_pipeline_automation_executions():
    """TABLE pipeline_automation_executions — 11 columns, 4 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_automation_id = 'text NOT NULL'
    col_triggering_event_id = 'uuid NOT NULL'
    col_routine_id = 'uuid NOT NULL'
    col_status = 'text NOT NULL'
    col_execution_issue_id = 'uuid'
    col_error = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_pipeline_cases()  # FK case_id
    tbl_routines()  # FK routine_id
    tbl_issues()  # FK execution_issue_id
    pass

def tbl_pipeline_case_blockers():
    """TABLE pipeline_case_blockers — 6 columns, 2 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_blocked_by_case_id = 'uuid NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_pipeline_cases()  # FK case_id
    pass

def tbl_pipeline_case_events():
    """TABLE pipeline_case_events — 13 columns, 4 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_type = 'text NOT NULL'
    col_actor_type = 'text NOT NULL'
    col_actor_user_id = 'text'
    col_actor_agent_id = 'uuid'
    col_run_id = 'uuid'
    col_from_stage_id = 'uuid'
    col_to_stage_id = 'uuid'
    col_payload = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_pipeline_cases()  # FK case_id
    tbl_agents()  # FK actor_agent_id
    tbl_pipeline_stages()  # FK from_stage_id
    pass

def tbl_pipeline_case_issue_links():
    """TABLE pipeline_case_issue_links — 8 columns, 3 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_role = 'text NOT NULL'
    col_created_by_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_pipeline_cases()  # FK case_id
    tbl_issues()  # FK issue_id
    pass

def tbl_pipeline_cases():
    """TABLE pipeline_cases — 26 columns, 5 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_pipeline_id = 'uuid NOT NULL'
    col_stage_id = 'uuid NOT NULL'
    col_case_key = 'text NOT NULL'
    col_title = 'text NOT NULL'
    col_summary = 'text'
    col_fields = 'jsonb DEFAULT'
    col_workspace_ref = 'jsonb'
    col_parent_case_id = 'uuid'
    col_version = 'integer DEFAULT 1 NOT NULL'
    col_pending_suggestion = 'jsonb'
    col_lease_owner_type = 'text'
    col_lease_agent_id = 'uuid'
    col_lease_user_id = 'text'
    col_lease_token = 'uuid'
    col_lease_expires_at = 'timestamp with time zone'
    col_terminal_kind = 'text'
    col_terminal_at = 'timestamp with time zone'
    col_child_count = 'integer DEFAULT 0 NOT NULL'
    col_terminal_child_count = 'integer DEFAULT 0 NOT NULL'
    col_created_by_user_id = 'text'
    col_created_by_agent_id = 'uuid'
    col_origin_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_pipelines()  # FK pipeline_id
    tbl_pipeline_stages()  # FK stage_id
    tbl_pipeline_cases()  # FK parent_case_id
    tbl_agents()  # FK lease_agent_id
    pass

def tbl_pipeline_documents():
    """TABLE pipeline_documents — 7 columns, 3 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_pipeline_id = 'uuid NOT NULL'
    col_document_id = 'uuid NOT NULL'
    col_key = 'text NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_pipelines()  # FK pipeline_id
    tbl_documents()  # FK document_id
    pass

def tbl_pipeline_stages():
    """TABLE pipeline_stages — 9 columns, 1 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_pipeline_id = 'uuid NOT NULL'
    col_key = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_kind = 'text NOT NULL'
    col_position = 'integer NOT NULL'
    col_config = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_pipelines()  # FK pipeline_id
    pass

def tbl_pipeline_transitions():
    """TABLE pipeline_transitions — 7 columns, 2 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_pipeline_id = 'uuid NOT NULL'
    col_from_stage_id = 'uuid NOT NULL'
    col_to_stage_id = 'uuid NOT NULL'
    col_label = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_pipelines()  # FK pipeline_id
    tbl_pipeline_stages()  # FK from_stage_id
    pass

def tbl_pipelines():
    """TABLE pipelines — 12 columns, 3 foreign keys. src: packages/db/src/migrations/0113_pipeline_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid'
    col_key = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_enforce_transitions = 'boolean DEFAULT false NOT NULL'
    col_created_by_user_id = 'text'
    col_created_by_agent_id = 'uuid'
    col_archived_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    tbl_agents()  # FK created_by_agent_id
    pass
