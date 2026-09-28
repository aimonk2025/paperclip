"""SQL: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""

def tbl_budget_incidents():
    """TABLE budget_incidents — 17 columns, 3 foreign keys. src: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_policy_id = 'uuid NOT NULL'
    col_scope_type = 'text NOT NULL'
    col_scope_id = 'uuid NOT NULL'
    col_metric = 'text NOT NULL'
    col_window_kind = 'text NOT NULL'
    col_window_start = 'timestamp with time zone NOT NULL'
    col_window_end = 'timestamp with time zone NOT NULL'
    col_threshold_type = 'text NOT NULL'
    col_amount_limit = 'integer NOT NULL'
    col_amount_observed = 'integer NOT NULL'
    col_status = 'text DEFAULT'
    col_approval_id = 'uuid'
    col_resolved_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_budget_policies()  # FK policy_id
    tbl_approvals()  # FK approval_id
    pass

def tbl_budget_policies():
    """TABLE budget_policies — 15 columns, 1 foreign keys. src: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_scope_type = 'text NOT NULL'
    col_scope_id = 'uuid NOT NULL'
    col_metric = 'text DEFAULT'
    col_window_kind = 'text NOT NULL'
    col_amount = 'integer DEFAULT 0 NOT NULL'
    col_warn_percent = 'integer DEFAULT 80 NOT NULL'
    col_hard_stop_enabled = 'boolean DEFAULT true NOT NULL'
    col_notify_enabled = 'boolean DEFAULT true NOT NULL'
    col_is_active = 'boolean DEFAULT true NOT NULL'
    col_created_by_user_id = 'text'
    col_updated_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def idx_budget_incidents_company_status_idx():
    """INDEX on budget_incidents. src: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""
    tbl_budget_incidents()

def idx_budget_incidents_company_scope_idx():
    """INDEX on budget_incidents. src: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""
    tbl_budget_incidents()

def idx_budget_incidents_policy_window_threshold_idx():
    """INDEX on budget_incidents. src: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""
    tbl_budget_incidents()

def idx_budget_policies_company_scope_active_idx():
    """INDEX on budget_policies. src: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""
    tbl_budget_policies()

def idx_budget_policies_company_window_idx():
    """INDEX on budget_policies. src: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""
    tbl_budget_policies()

def idx_budget_policies_company_scope_metric_unique_idx():
    """INDEX on budget_policies. src: packages/db/src/migrations/0032_pretty_doctor_octopus.sql"""
    tbl_budget_policies()
