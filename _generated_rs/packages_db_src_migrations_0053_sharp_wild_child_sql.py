"""SQL: packages/db/src/migrations/0053_sharp_wild_child.sql"""

def tbl_inbox_dismissals():
    """TABLE inbox_dismissals — 7 columns, 1 foreign keys. src: packages/db/src/migrations/0053_sharp_wild_child.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_user_id = 'text NOT NULL'
    col_item_key = 'text NOT NULL'
    col_dismissed_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass
