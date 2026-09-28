"""SQL: packages/db/src/migrations/0139_skill_studio_run_templates.sql"""

def tbl_company_skill_test_run_templates():
    """TABLE company_skill_test_run_templates — 12 columns, 2 foreign keys. src: packages/db/src/migrations/0139_skill_studio_run_templates.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_body = 'text NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_updated_by_agent_id = 'uuid'
    col_updated_by_user_id = 'text'
    col_deleted_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass
