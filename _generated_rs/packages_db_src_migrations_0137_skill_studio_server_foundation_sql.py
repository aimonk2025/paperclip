"""SQL: packages/db/src/migrations/0137_skill_studio_server_foundation.sql"""

def tbl_company_skill_test_inputs():
    """TABLE company_skill_test_inputs — 9 columns, 2 foreign keys. src: packages/db/src/migrations/0137_skill_studio_server_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_skill_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_content = 'text NOT NULL'
    col_created_by = 'text'
    col_deleted_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_company_skills()  # FK skill_id
    pass

def tbl_company_skill_test_runs():
    """TABLE company_skill_test_runs — 15 columns, 6 foreign keys. src: packages/db/src/migrations/0137_skill_studio_server_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_skill_id = 'uuid NOT NULL'
    col_input_id = 'uuid'
    col_input_snapshot = 'text NOT NULL'
    col_skill_version_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_agent_config_snapshot = 'jsonb DEFAULT'
    col_issue_id = 'uuid NOT NULL'
    col_status = 'text DEFAULT'
    col_output_document_key = 'text DEFAULT'
    col_output_snapshot = 'text DEFAULT'
    col_error = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_company_skills()  # FK skill_id
    tbl_company_skill_test_inputs()  # FK input_id
    tbl_company_skill_versions()  # FK skill_version_id
    tbl_agents()  # FK agent_id
    tbl_issues()  # FK issue_id
    pass
