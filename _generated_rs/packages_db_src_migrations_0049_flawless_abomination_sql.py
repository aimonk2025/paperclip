"""SQL: packages/db/src/migrations/0049_flawless_abomination.sql"""

def tbl_issue_relations():
    """TABLE issue_relations — 9 columns, 3 foreign keys. src: packages/db/src/migrations/0049_flawless_abomination.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_related_issue_id = 'uuid NOT NULL'
    col_type = 'text NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    tbl_agents()  # FK created_by_agent_id
    pass

def idx_issue_relations_company_issue_idx():
    """INDEX on issue_relations. src: packages/db/src/migrations/0049_flawless_abomination.sql"""
    tbl_issue_relations()

def idx_issue_relations_company_related_issue_idx():
    """INDEX on issue_relations. src: packages/db/src/migrations/0049_flawless_abomination.sql"""
    tbl_issue_relations()

def idx_issue_relations_company_type_idx():
    """INDEX on issue_relations. src: packages/db/src/migrations/0049_flawless_abomination.sql"""
    tbl_issue_relations()

def idx_issue_relations_company_edge_uq():
    """INDEX on issue_relations. src: packages/db/src/migrations/0049_flawless_abomination.sql"""
    tbl_issue_relations()
