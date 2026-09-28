"""SQL: packages/db/src/migrations/0171_issue_create_idempotency_keys.sql"""

def tbl_issue_create_idempotency_keys():
    """TABLE issue_create_idempotency_keys — 5 columns, 2 foreign keys. src: packages/db/src/migrations/0171_issue_create_idempotency_keys.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL REFERENCES'
    col_idempotency_key = 'text NOT NULL'
    col_issue_id = 'uuid NOT NULL REFERENCES'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    pass
