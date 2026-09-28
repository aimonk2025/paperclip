"""SQL: packages/db/src/migrations/0170_company_skill_policies.sql"""

def tbl_company_skill_policies():
    """TABLE company_skill_policies — 7 columns, 1 foreign keys. src: packages/db/src/migrations/0170_company_skill_policies.sql"""
    col_company_id = 'uuid PRIMARY KEY NOT NULL REFERENCES'
    col_schema_version = 'integer DEFAULT 1 NOT NULL'
    col_revision = 'integer NOT NULL'
    col_default_effect = 'text NOT NULL'
    col_rules = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass
