"""SQL: packages/db/src/migrations/0042_spotty_the_renegades.sql"""

def tbl_company_skills():
    """TABLE company_skills — 16 columns, 4 foreign keys. src: packages/db/src/migrations/0042_spotty_the_renegades.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_key = 'text NOT NULL'
    col_slug = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_description = 'text'
    col_markdown = 'text NOT NULL'
    col_source_type = 'text DEFAULT'
    col_source_locator = 'text'
    col_source_ref = 'text'
    col_trust_level = 'text DEFAULT'
    col_compatibility = 'text DEFAULT'
    col_file_inventory = 'jsonb DEFAULT'
    col_metadata = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_company_skills()  # FK forked_from_skill_id
    tbl_companies()  # FK forked_from_company_id
    tbl_company_skill_versions()  # FK current_version_id
    tbl_folders()  # FK folder_id
    pass
