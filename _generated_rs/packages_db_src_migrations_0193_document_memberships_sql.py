"""SQL: packages/db/src/migrations/0193_document_memberships.sql"""

def tbl_document_memberships():
    """TABLE document_memberships — 7 columns, 2 foreign keys. src: packages/db/src/migrations/0193_document_memberships.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL REFERENCES'
    col_document_id = 'uuid NOT NULL REFERENCES'
    col_user_id = 'text NOT NULL'
    col_starred_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_documents()  # FK document_id
    pass
