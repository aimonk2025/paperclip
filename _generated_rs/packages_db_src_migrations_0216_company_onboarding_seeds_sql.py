"""SQL: packages/db/src/migrations/0216_company_onboarding_seeds.sql"""

def tbl_company_onboarding_seeds():
    """TABLE company_onboarding_seeds — 14 columns, 4 foreign keys. src: packages/db/src/migrations/0216_company_onboarding_seeds.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_revision = 'text NOT NULL'
    col_mission = 'text'
    col_agent_name = 'text'
    col_agent_role = 'text'
    col_first_task_title = 'text'
    col_first_task_details = 'text'
    col_goal_id = 'uuid'
    col_agent_id = 'uuid'
    col_issue_id = 'uuid'
    col_applied_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_goals()  # FK goal_id
    tbl_agents()  # FK agent_id
    tbl_issues()  # FK issue_id
    pass
