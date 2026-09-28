"""SQL: packages/db/src/migrations/0018_flat_sleepwalker.sql"""

def tbl_issue_labels():
    """TABLE issue_labels — 4 columns, 3 foreign keys. src: packages/db/src/migrations/0018_flat_sleepwalker.sql"""
    col_issue_id = 'uuid NOT NULL'
    col_label_id = 'uuid NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_issues()  # FK issue_id
    tbl_labels()  # FK label_id
    tbl_companies()  # FK company_id
    pass

def tbl_labels():
    """TABLE labels — 6 columns, 1 foreign keys. src: packages/db/src/migrations/0018_flat_sleepwalker.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_color = 'text NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def idx_issue_labels_issue_idx():
    """INDEX on issue_labels. src: packages/db/src/migrations/0018_flat_sleepwalker.sql"""
    tbl_issue_labels()

def idx_issue_labels_label_idx():
    """INDEX on issue_labels. src: packages/db/src/migrations/0018_flat_sleepwalker.sql"""
    tbl_issue_labels()

def idx_issue_labels_company_idx():
    """INDEX on issue_labels. src: packages/db/src/migrations/0018_flat_sleepwalker.sql"""
    tbl_issue_labels()

def idx_labels_company_idx():
    """INDEX on labels. src: packages/db/src/migrations/0018_flat_sleepwalker.sql"""
    tbl_labels()

def idx_labels_company_name_idx():
    """INDEX on labels. src: packages/db/src/migrations/0018_flat_sleepwalker.sql"""
    tbl_labels()
