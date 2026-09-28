"""SQL: packages/db/src/migrations/0178_summary_slots.sql"""

def tbl_summary_slots():
    """TABLE summary_slots — 13 columns, 4 foreign keys. src: packages/db/src/migrations/0178_summary_slots.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_scope_kind = 'text NOT NULL'
    col_scope_id = 'uuid'
    col_slot_key = 'text NOT NULL'
    col_document_id = 'uuid'
    col_status = 'text DEFAULT'
    col_generating_issue_id = 'uuid'
    col_last_generated_at = 'timestamp with time zone'
    col_last_generated_by_agent_id = 'uuid'
    col_last_model = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_documents()  # FK document_id
    tbl_issues()  # FK generating_issue_id
    tbl_agents()  # FK last_generated_by_agent_id
    pass
