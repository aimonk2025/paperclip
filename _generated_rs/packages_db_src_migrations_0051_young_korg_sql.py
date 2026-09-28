"""SQL: packages/db/src/migrations/0051_young_korg.sql"""

def idx_issue_comments_body_search_idx():
    """INDEX on issue_comments. src: packages/db/src/migrations/0051_young_korg.sql"""
    tbl_issue_comments()

def idx_issues_title_search_idx():
    """INDEX on issues. src: packages/db/src/migrations/0051_young_korg.sql"""
    tbl_issues()

def idx_issues_identifier_search_idx():
    """INDEX on issues. src: packages/db/src/migrations/0051_young_korg.sql"""
    tbl_issues()

def idx_issues_description_search_idx():
    """INDEX on issues. src: packages/db/src/migrations/0051_young_korg.sql"""
    tbl_issues()
