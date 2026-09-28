"""SQL: packages/db/src/migrations/0011_windy_corsair.sql"""

def tbl_project_goals():
    """TABLE project_goals — 5 columns, 3 foreign keys. src: packages/db/src/migrations/0011_windy_corsair.sql"""
    col_project_id = 'uuid NOT NULL'
    col_goal_id = 'uuid NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_projects()  # FK project_id
    tbl_goals()  # FK goal_id
    tbl_companies()  # FK company_id
    pass

def idx_project_goals_project_idx():
    """INDEX on project_goals. src: packages/db/src/migrations/0011_windy_corsair.sql"""
    tbl_project_goals()

def idx_project_goals_goal_idx():
    """INDEX on project_goals. src: packages/db/src/migrations/0011_windy_corsair.sql"""
    tbl_project_goals()

def idx_project_goals_company_idx():
    """INDEX on project_goals. src: packages/db/src/migrations/0011_windy_corsair.sql"""
    tbl_project_goals()
