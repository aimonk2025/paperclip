"""SQL: packages/db/src/migrations/0197_decisions_v1.sql"""

def tbl_decision_bundles():
    """TABLE decision_bundles — 8 columns, 4 foreign keys. src: packages/db/src/migrations/0197_decisions_v1.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_title = 'text NOT NULL'
    col_summary = 'text NOT NULL'
    col_origin_agent_id = 'uuid NOT NULL'
    col_origin_issue_id = 'uuid NOT NULL'
    col_origin_run_id = 'uuid NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK origin_agent_id
    tbl_issues()  # FK origin_issue_id
    tbl_heartbeat_runs()  # FK origin_run_id
    pass

def tbl_decisions():
    """TABLE decisions — 25 columns, 5 foreign keys. src: packages/db/src/migrations/0197_decisions_v1.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_bundle_id = 'uuid'
    col_origin_agent_id = 'uuid NOT NULL'
    col_origin_issue_id = 'uuid NOT NULL'
    col_origin_run_id = 'uuid NOT NULL'
    col_rule_key = 'text'
    col_title = 'text NOT NULL'
    col_body = 'text NOT NULL'
    col_options = 'jsonb NOT NULL'
    col_inputs = 'jsonb'
    col_status = 'text DEFAULT'
    col_execution_status = 'text'
    col_chosen_option_id = 'text'
    col_input_values = 'jsonb'
    col_decided_by_user_id = 'text'
    col_decided_at = 'timestamp with time zone'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_idempotency_key = 'text'
    col_signed_spec = 'text NOT NULL'
    col_target_snapshots = 'jsonb NOT NULL'
    col_continuation_policy = 'text DEFAULT'
    col_metadata = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_decision_bundles()  # FK bundle_id
    tbl_agents()  # FK origin_agent_id
    tbl_issues()  # FK origin_issue_id
    tbl_heartbeat_runs()  # FK origin_run_id
    pass

def tbl_decision_target_issues():
    """TABLE decision_target_issues — 3 columns, 3 foreign keys. src: packages/db/src/migrations/0197_decisions_v1.sql"""
    col_decision_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_company_id = 'uuid NOT NULL'
    tbl_decisions()  # FK decision_id
    tbl_issues()  # FK issue_id
    tbl_companies()  # FK company_id
    pass

def tbl_decision_effect_executions():
    """TABLE decision_effect_executions — 10 columns, 3 foreign keys. src: packages/db/src/migrations/0197_decisions_v1.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_decision_id = 'uuid NOT NULL'
    col_effect_index = 'integer NOT NULL'
    col_effect_type = 'text NOT NULL'
    col_target_issue_id = 'uuid NOT NULL'
    col_status = 'text DEFAULT'
    col_result = 'jsonb'
    col_error = 'text'
    col_activity_log_id = 'uuid'
    col_executed_at = 'timestamp with time zone'
    tbl_decisions()  # FK decision_id
    tbl_issues()  # FK target_issue_id
    tbl_activity_log()  # FK activity_log_id
    pass
