"""SQL: packages/db/src/migrations/0172_inbox_archive_agent_policies.sql"""

def tbl_user_inbox_agent_policies():
    """TABLE user_inbox_agent_policies — 7 columns, 1 foreign keys. src: packages/db/src/migrations/0172_inbox_archive_agent_policies.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_user_id = 'text NOT NULL'
    col_mode = 'text DEFAULT'
    col_allowed_agent_ids = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass
