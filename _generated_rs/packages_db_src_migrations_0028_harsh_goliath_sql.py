"""SQL: packages/db/src/migrations/0028_harsh_goliath.sql"""

def tbl_document_revisions():
    """TABLE document_revisions — 9 columns, 4 foreign keys. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_document_id = 'uuid NOT NULL'
    col_revision_number = 'integer NOT NULL'
    col_body = 'text NOT NULL'
    col_change_summary = 'text'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_heartbeat_runs()  # FK created_by_run_id
    tbl_companies()  # FK company_id
    tbl_documents()  # FK document_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_documents():
    """TABLE documents — 13 columns, 2 foreign keys. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_title = 'text'
    col_format = 'text DEFAULT'
    col_latest_body = 'text NOT NULL'
    col_latest_revision_id = 'uuid'
    col_latest_revision_number = 'integer DEFAULT 1 NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_updated_by_agent_id = 'uuid'
    col_updated_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_issue_documents():
    """TABLE issue_documents — 7 columns, 3 foreign keys. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_document_id = 'uuid NOT NULL'
    col_key = 'text NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    tbl_documents()  # FK document_id
    pass

def idx_document_revisions_document_revision_uq():
    """INDEX on document_revisions. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    tbl_document_revisions()

def idx_document_revisions_company_document_created_idx():
    """INDEX on document_revisions. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    tbl_document_revisions()

def idx_documents_company_updated_idx():
    """INDEX on documents. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    tbl_documents()

def idx_documents_company_created_idx():
    """INDEX on documents. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    tbl_documents()

def idx_issue_documents_company_issue_key_uq():
    """INDEX on issue_documents. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    tbl_issue_documents()

def idx_issue_documents_document_uq():
    """INDEX on issue_documents. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    tbl_issue_documents()

def idx_issue_documents_company_issue_updated_idx():
    """INDEX on issue_documents. src: packages/db/src/migrations/0028_harsh_goliath.sql"""
    tbl_issue_documents()
