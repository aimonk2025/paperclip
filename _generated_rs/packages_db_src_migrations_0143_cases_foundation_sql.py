"""SQL: packages/db/src/migrations/0143_cases_foundation.sql"""

def tbl_cases():
    """TABLE cases — 17 columns, 4 foreign keys. src: packages/db/src/migrations/0143_cases_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_project_id = 'uuid'
    col_case_number = 'integer NOT NULL'
    col_identifier = 'text NOT NULL'
    col_case_type = 'text NOT NULL'
    col_key = 'text'
    col_title = 'text NOT NULL'
    col_summary = 'text'
    col_status = 'text DEFAULT'
    col_fields = 'jsonb DEFAULT'
    col_parent_case_id = 'uuid'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_completed_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_projects()  # FK project_id
    tbl_cases()  # FK parent_case_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_case_issue_links():
    """TABLE case_issue_links — 8 columns, 3 foreign keys. src: packages/db/src/migrations/0143_cases_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_role = 'text NOT NULL'
    col_created_by_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_cases()  # FK case_id
    tbl_issues()  # FK issue_id
    pass

def tbl_case_events():
    """TABLE case_events — 11 columns, 3 foreign keys. src: packages/db/src/migrations/0143_cases_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_kind = 'text NOT NULL'
    col_actor_type = 'text NOT NULL'
    col_actor_user_id = 'text'
    col_actor_agent_id = 'uuid'
    col_run_id = 'uuid'
    col_payload = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_cases()  # FK case_id
    tbl_agents()  # FK actor_agent_id
    pass

def tbl_case_documents():
    """TABLE case_documents — 7 columns, 3 foreign keys. src: packages/db/src/migrations/0143_cases_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_document_id = 'uuid NOT NULL'
    col_key = 'text NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_cases()  # FK case_id
    tbl_documents()  # FK document_id
    pass

def tbl_case_labels():
    """TABLE case_labels — 6 columns, 3 foreign keys. src: packages/db/src/migrations/0143_cases_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_label_id = 'uuid NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_cases()  # FK case_id
    tbl_labels()  # FK label_id
    pass

def tbl_case_attachments():
    """TABLE case_attachments — 6 columns, 3 foreign keys. src: packages/db/src/migrations/0143_cases_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_case_id = 'uuid NOT NULL'
    col_asset_id = 'uuid NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_cases()  # FK case_id
    tbl_assets()  # FK asset_id
    pass
