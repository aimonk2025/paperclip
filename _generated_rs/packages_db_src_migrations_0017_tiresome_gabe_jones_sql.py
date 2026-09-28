"""SQL: packages/db/src/migrations/0017_tiresome_gabe_jones.sql"""

def idx_companies_issue_prefix_idx():
    """INDEX on companies. src: packages/db/src/migrations/0017_tiresome_gabe_jones.sql"""
    tbl_companies()

def idx_issues_identifier_idx():
    """INDEX on issues. src: packages/db/src/migrations/0017_tiresome_gabe_jones.sql"""
    tbl_issues()
