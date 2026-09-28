"""SQL: packages/db/src/migrations/0056_spooky_ultragirl.sql"""

def tbl_company_user_sidebar_preferences():
    """TABLE company_user_sidebar_preferences — 6 columns, 1 foreign keys. src: packages/db/src/migrations/0056_spooky_ultragirl.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_user_id = 'text NOT NULL'
    col_project_order = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def tbl_user_sidebar_preferences():
    """TABLE user_sidebar_preferences — 5 columns, 0 foreign keys. src: packages/db/src/migrations/0056_spooky_ultragirl.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_user_id = 'text NOT NULL'
    col_company_order = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    pass

def idx_company_user_sidebar_preferences_company_idx():
    """INDEX on company_user_sidebar_preferences. src: packages/db/src/migrations/0056_spooky_ultragirl.sql"""
    tbl_company_user_sidebar_preferences()

def idx_company_user_sidebar_preferences_user_idx():
    """INDEX on company_user_sidebar_preferences. src: packages/db/src/migrations/0056_spooky_ultragirl.sql"""
    tbl_company_user_sidebar_preferences()

def idx_company_user_sidebar_preferences_company_user_uq():
    """INDEX on company_user_sidebar_preferences. src: packages/db/src/migrations/0056_spooky_ultragirl.sql"""
    tbl_company_user_sidebar_preferences()

def idx_user_sidebar_preferences_user_uq():
    """INDEX on user_sidebar_preferences. src: packages/db/src/migrations/0056_spooky_ultragirl.sql"""
    tbl_user_sidebar_preferences()
