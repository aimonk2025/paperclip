"""SQL: packages/db/src/migrations/0060_orange_annihilus.sql"""

def tbl_issue_reference_mentions():
    """TABLE issue_reference_mentions — 10 columns, 2 foreign keys. src: packages/db/src/migrations/0060_orange_annihilus.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_source_issue_id = 'uuid NOT NULL'
    col_target_issue_id = 'uuid NOT NULL'
    col_source_kind = 'text NOT NULL'
    col_source_record_id = 'uuid'
    col_document_key = 'text'
    col_matched_text = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK source_issue_id
    pass
