"""SQL: packages/db/src/migrations/0025_nasty_salo.sql"""

def tbl_issue_read_states():
    """TABLE issue_read_states — 7 columns, 2 foreign keys. src: packages/db/src/migrations/0025_nasty_salo.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_user_id = 'text NOT NULL'
    col_last_read_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    pass

def idx_issue_read_states_company_issue_idx():
    """INDEX on issue_read_states. src: packages/db/src/migrations/0025_nasty_salo.sql"""
    tbl_issue_read_states()

def idx_issue_read_states_company_user_idx():
    """INDEX on issue_read_states. src: packages/db/src/migrations/0025_nasty_salo.sql"""
    tbl_issue_read_states()

def idx_issue_read_states_company_issue_user_idx():
    """INDEX on issue_read_states. src: packages/db/src/migrations/0025_nasty_salo.sql"""
    tbl_issue_read_states()
