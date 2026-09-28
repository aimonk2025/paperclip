"""SQL: packages/db/src/migrations/0076_useful_elektra.sql"""

def tbl_plugin_managed_resources():
    """TABLE plugin_managed_resources — 10 columns, 2 foreign keys. src: packages/db/src/migrations/0076_useful_elektra.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_plugin_key = 'text NOT NULL'
    col_resource_kind = 'text NOT NULL'
    col_resource_key = 'text NOT NULL'
    col_resource_id = 'uuid NOT NULL'
    col_defaults_json = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_plugins()  # FK plugin_id
    pass
