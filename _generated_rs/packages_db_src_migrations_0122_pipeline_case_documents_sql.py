"""SQL: packages/db/src/migrations/0122_pipeline_case_documents.sql"""

def tbl_pipeline_case_documents():
    """TABLE pipeline_case_documents — 7 columns, 3 foreign keys. src: packages/db/src/migrations/0122_pipeline_case_documents.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_document_id = 'uuid NOT NULL'
    col_key = 'text NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_pipeline_cases()  # FK case_id
    tbl_documents()  # FK document_id
    pass
