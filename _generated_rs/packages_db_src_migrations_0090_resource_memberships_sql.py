"""SQL: packages/db/src/migrations/0090_resource_memberships.sql"""

def tbl_agent_memberships():
    """TABLE agent_memberships — 7 columns, 2 foreign keys. src: packages/db/src/migrations/0090_resource_memberships.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_user_id = 'text NOT NULL'
    col_state = 'text DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    pass

def tbl_project_memberships():
    """TABLE project_memberships — 7 columns, 2 foreign keys. src: packages/db/src/migrations/0090_resource_memberships.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid NOT NULL'
    col_user_id = 'text NOT NULL'
    col_state = 'text DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    pass
