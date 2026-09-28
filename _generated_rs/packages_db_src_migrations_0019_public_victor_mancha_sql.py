"""SQL: packages/db/src/migrations/0019_public_victor_mancha.sql"""

def tbl_project_workspaces():
    """TABLE project_workspaces — 11 columns, 2 foreign keys. src: packages/db/src/migrations/0019_public_victor_mancha.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_cwd = 'text NOT NULL'
    col_repo_url = 'text'
    col_repo_ref = 'text'
    col_metadata = 'jsonb'
    col_is_primary = 'boolean DEFAULT false NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    pass

def idx_project_workspaces_company_project_idx():
    """INDEX on project_workspaces. src: packages/db/src/migrations/0019_public_victor_mancha.sql"""
    tbl_project_workspaces()

def idx_project_workspaces_project_primary_idx():
    """INDEX on project_workspaces. src: packages/db/src/migrations/0019_public_victor_mancha.sql"""
    tbl_project_workspaces()
