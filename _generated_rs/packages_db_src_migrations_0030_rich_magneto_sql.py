"""SQL: packages/db/src/migrations/0030_rich_magneto.sql"""

def tbl_company_logos():
    """TABLE company_logos — 5 columns, 2 foreign keys. src: packages/db/src/migrations/0030_rich_magneto.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_asset_id = 'uuid NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_assets()  # FK asset_id
    pass

def idx_company_logos_company_uq():
    """INDEX on company_logos. src: packages/db/src/migrations/0030_rich_magneto.sql"""
    tbl_company_logos()

def idx_company_logos_asset_uq():
    """INDEX on company_logos. src: packages/db/src/migrations/0030_rich_magneto.sql"""
    tbl_company_logos()
