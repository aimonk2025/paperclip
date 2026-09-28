"""SQL: packages/db/src/migrations/0059_plugin_database_namespaces.sql"""

def tbl_plugin_database_namespaces():
    """TABLE plugin_database_namespaces — 8 columns, 1 foreign keys. src: packages/db/src/migrations/0059_plugin_database_namespaces.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_plugin_key = 'text NOT NULL'
    col_namespace_name = 'text NOT NULL'
    col_namespace_mode = 'text DEFAULT'
    col_status = 'text DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_plugins()  # FK plugin_id
    pass

def tbl_plugin_migrations():
    """TABLE plugin_migrations — 11 columns, 1 foreign keys. src: packages/db/src/migrations/0059_plugin_database_namespaces.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_plugin_id = 'uuid NOT NULL'
    col_plugin_key = 'text NOT NULL'
    col_namespace_name = 'text NOT NULL'
    col_migration_key = 'text NOT NULL'
    col_checksum = 'text NOT NULL'
    col_plugin_version = 'text NOT NULL'
    col_status = 'text NOT NULL'
    col_started_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_applied_at = 'timestamp with time zone'
    col_error_message = 'text'
    tbl_plugins()  # FK plugin_id
    pass
