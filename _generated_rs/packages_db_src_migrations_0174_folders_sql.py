"""SQL: packages/db/src/migrations/0174_folders.sql"""

def tbl_folders():
    """TABLE folders — 8 columns, 2 foreign keys. src: packages/db/src/migrations/0174_folders.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_kind = 'text NOT NULL'
    col_name = 'text NOT NULL'
    col_color = 'text'
    col_position = 'integer DEFAULT 0 NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_folders()  # FK parent_id
    tbl_companies()  # FK company_id
    pass
