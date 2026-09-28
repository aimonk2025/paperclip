"""SQL: packages/db/src/migrations/0101_plugin_company_id_tenant_isolation.sql"""

def idx_plugin_entities_company_idx():
    """INDEX on plugin_entities. src: packages/db/src/migrations/0101_plugin_company_id_tenant_isolation.sql"""
    tbl_plugin_entities()

def idx_plugin_job_runs_company_idx():
    """INDEX on plugin_job_runs. src: packages/db/src/migrations/0101_plugin_company_id_tenant_isolation.sql"""
    tbl_plugin_job_runs()

def idx_plugin_logs_company_idx():
    """INDEX on plugin_logs. src: packages/db/src/migrations/0101_plugin_company_id_tenant_isolation.sql"""
    tbl_plugin_logs()

def idx_plugin_webhook_deliveries_company_idx():
    """INDEX on plugin_webhook_deliveries. src: packages/db/src/migrations/0101_plugin_company_id_tenant_isolation.sql"""
    tbl_plugin_webhook_deliveries()
