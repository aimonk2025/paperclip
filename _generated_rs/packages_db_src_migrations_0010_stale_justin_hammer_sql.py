"""SQL: packages/db/src/migrations/0010_stale_justin_hammer.sql"""

def tbl_assets():
    """TABLE assets — 12 columns, 2 foreign keys. src: packages/db/src/migrations/0010_stale_justin_hammer.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_provider = 'text NOT NULL'
    col_object_key = 'text NOT NULL'
    col_content_type = 'text NOT NULL'
    col_byte_size = 'integer NOT NULL'
    col_sha256 = 'text NOT NULL'
    col_original_filename = 'text'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_issue_attachments():
    """TABLE issue_attachments — 7 columns, 4 foreign keys. src: packages/db/src/migrations/0010_stale_justin_hammer.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_asset_id = 'uuid NOT NULL'
    col_issue_comment_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    tbl_assets()  # FK asset_id
    tbl_issue_comments()  # FK issue_comment_id
    pass

def idx_assets_company_created_idx():
    """INDEX on assets. src: packages/db/src/migrations/0010_stale_justin_hammer.sql"""
    tbl_assets()

def idx_assets_company_provider_idx():
    """INDEX on assets. src: packages/db/src/migrations/0010_stale_justin_hammer.sql"""
    tbl_assets()

def idx_assets_company_object_key_uq():
    """INDEX on assets. src: packages/db/src/migrations/0010_stale_justin_hammer.sql"""
    tbl_assets()

def idx_issue_attachments_company_issue_idx():
    """INDEX on issue_attachments. src: packages/db/src/migrations/0010_stale_justin_hammer.sql"""
    tbl_issue_attachments()

def idx_issue_attachments_issue_comment_idx():
    """INDEX on issue_attachments. src: packages/db/src/migrations/0010_stale_justin_hammer.sql"""
    tbl_issue_attachments()

def idx_issue_attachments_asset_uq():
    """INDEX on issue_attachments. src: packages/db/src/migrations/0010_stale_justin_hammer.sql"""
    tbl_issue_attachments()
