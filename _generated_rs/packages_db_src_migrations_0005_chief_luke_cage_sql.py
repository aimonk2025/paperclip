"""SQL: packages/db/src/migrations/0005_chief_luke_cage.sql"""

def tbl_approval_comments():
    """TABLE approval_comments — 8 columns, 3 foreign keys. src: packages/db/src/migrations/0005_chief_luke_cage.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_approval_id = 'uuid NOT NULL'
    col_author_agent_id = 'uuid'
    col_author_user_id = 'text'
    col_body = 'text NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_approvals()  # FK approval_id
    tbl_agents()  # FK author_agent_id
    pass

def idx_approval_comments_company_idx():
    """INDEX on approval_comments. src: packages/db/src/migrations/0005_chief_luke_cage.sql"""
    tbl_approval_comments()

def idx_approval_comments_approval_idx():
    """INDEX on approval_comments. src: packages/db/src/migrations/0005_chief_luke_cage.sql"""
    tbl_approval_comments()

def idx_approval_comments_approval_created_idx():
    """INDEX on approval_comments. src: packages/db/src/migrations/0005_chief_luke_cage.sql"""
    tbl_approval_comments()
