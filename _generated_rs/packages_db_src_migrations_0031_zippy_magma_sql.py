"""SQL: packages/db/src/migrations/0031_zippy_magma.sql"""

def tbl_finance_events():
    """TABLE finance_events — 27 columns, 7 foreign keys. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_agent_id = 'uuid'
    col_issue_id = 'uuid'
    col_project_id = 'uuid'
    col_goal_id = 'uuid'
    col_heartbeat_run_id = 'uuid'
    col_cost_event_id = 'uuid'
    col_billing_code = 'text'
    col_description = 'text'
    col_event_kind = 'text NOT NULL'
    col_direction = 'text DEFAULT'
    col_biller = 'text NOT NULL'
    col_provider = 'text'
    col_execution_adapter_type = 'text'
    col_pricing_tier = 'text'
    col_region = 'text'
    col_model = 'text'
    col_quantity = 'integer'
    col_unit = 'text'
    col_amount_cents = 'integer NOT NULL'
    col_currency = 'text DEFAULT'
    col_estimated = 'boolean DEFAULT false NOT NULL'
    col_external_invoice_id = 'text'
    col_metadata_json = 'jsonb'
    col_occurred_at = 'timestamp with time zone NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_issues()  # FK issue_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    tbl_projects()  # FK project_id
    tbl_goals()  # FK goal_id
    tbl_heartbeat_runs()  # FK heartbeat_run_id
    tbl_cost_events()  # FK cost_event_id
    pass

def idx_finance_events_company_occurred_idx():
    """INDEX on finance_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_finance_events()

def idx_finance_events_company_biller_occurred_idx():
    """INDEX on finance_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_finance_events()

def idx_finance_events_company_kind_occurred_idx():
    """INDEX on finance_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_finance_events()

def idx_finance_events_company_direction_occurred_idx():
    """INDEX on finance_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_finance_events()

def idx_finance_events_company_heartbeat_run_idx():
    """INDEX on finance_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_finance_events()

def idx_finance_events_company_cost_event_idx():
    """INDEX on finance_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_finance_events()

def idx_cost_events_company_provider_occurred_idx():
    """INDEX on cost_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_cost_events()

def idx_cost_events_company_biller_occurred_idx():
    """INDEX on cost_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_cost_events()

def idx_cost_events_company_heartbeat_run_idx():
    """INDEX on cost_events. src: packages/db/src/migrations/0031_zippy_magma.sql"""
    tbl_cost_events()
