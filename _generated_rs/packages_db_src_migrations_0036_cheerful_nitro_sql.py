"""SQL: packages/db/src/migrations/0036_cheerful_nitro.sql"""

def tbl_instance_settings():
    """TABLE instance_settings — 5 columns, 1 foreign keys. src: packages/db/src/migrations/0036_cheerful_nitro.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_singleton_key = 'text DEFAULT'
    col_experimental = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_environments()  # FK default_environment_id
    pass

def idx_instance_settings_singleton_key_idx():
    """INDEX on instance_settings. src: packages/db/src/migrations/0036_cheerful_nitro.sql"""
    tbl_instance_settings()
