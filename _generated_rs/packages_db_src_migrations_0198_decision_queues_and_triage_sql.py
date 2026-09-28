"""SQL: packages/db/src/migrations/0198_decision_queues_and_triage.sql"""

def tbl_decision_queue_items():
    """TABLE decision_queue_items — 14 columns, 5 foreign keys. src: packages/db/src/migrations/0198_decision_queues_and_triage.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_queue_id = 'uuid NOT NULL'
    col_source_kind = 'text NOT NULL'
    col_source_id = 'text NOT NULL'
    col_added_by_type = 'text NOT NULL'
    col_added_by_agent_id = 'uuid'
    col_added_by_user_id = 'text'
    col_added_by_run_id = 'uuid'
    col_added_by_agent_api_key_id = 'uuid'
    col_responsible_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_or = '('
    col_or = '('
    tbl_decision_queues()  # FK queue_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK added_by_agent_id
    tbl_heartbeat_runs()  # FK added_by_run_id
    tbl_agent_api_keys()  # FK added_by_agent_api_key_id
    pass

def tbl_decision_queues():
    """TABLE decision_queues — 17 columns, 4 foreign keys. src: packages/db/src/migrations/0198_decision_queues_and_triage.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_key = 'text NOT NULL'
    col_title = 'text NOT NULL'
    col_description = 'text'
    col_created_by_type = 'text NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_created_by_run_id = 'uuid'
    col_created_by_agent_api_key_id = 'uuid'
    col_retention_days = 'integer'
    col_seed_rules = 'jsonb DEFAULT'
    col_seed_rules_enabled = 'boolean DEFAULT false NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_or = '('
    col_or = '('
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    tbl_heartbeat_runs()  # FK created_by_run_id
    tbl_agent_api_keys()  # FK created_by_agent_api_key_id
    pass

def tbl_decision_triage():
    """TABLE decision_triage — 19 columns, 4 foreign keys. src: packages/db/src/migrations/0198_decision_queues_and_triage.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_source_kind = 'text NOT NULL'
    col_source_id = 'text NOT NULL'
    col_decide_by = 'text'
    col_decide_by_date = 'date'
    col_snoozed_until = 'timestamp with time zone'
    col_set_by_type = 'text NOT NULL'
    col_set_by_agent_id = 'uuid'
    col_set_by_user_id = 'text'
    col_set_by_run_id = 'uuid'
    col_set_by_agent_api_key_id = 'uuid'
    col_responsible_user_id = 'text'
    col_version = 'integer DEFAULT 1 NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_or = '('
    col_or = '('
    col_or = '('
    tbl_companies()  # FK company_id
    tbl_agents()  # FK set_by_agent_id
    tbl_heartbeat_runs()  # FK set_by_run_id
    tbl_agent_api_keys()  # FK set_by_agent_api_key_id
    pass

def tbl_decision_triage_events():
    """TABLE decision_triage_events — 16 columns, 5 foreign keys. src: packages/db/src/migrations/0198_decision_queues_and_triage.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_queue_id = 'uuid'
    col_source_kind = 'text'
    col_source_id = 'text'
    col_action = 'text NOT NULL'
    col_actor_type = 'text NOT NULL'
    col_actor_agent_id = 'uuid'
    col_actor_user_id = 'text'
    col_actor_run_id = 'uuid'
    col_agent_api_key_id = 'uuid'
    col_responsible_user_id = 'text'
    col_details = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_or = '('
    col_or = '('
    tbl_companies()  # FK company_id
    tbl_decision_queues()  # FK queue_id
    tbl_agents()  # FK actor_agent_id
    tbl_heartbeat_runs()  # FK actor_run_id
    tbl_agent_api_keys()  # FK agent_api_key_id
    pass
