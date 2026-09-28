"""SQL: packages/db/src/migrations/0001_fast_northstar.sql"""

def tbl_agent_runtime_state():
    """TABLE agent_runtime_state — 14 columns, 2 foreign keys. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    col_agent_id = 'uuid PRIMARY KEY NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_adapter_type = 'text NOT NULL'
    col_session_id = 'text'
    col_state_json = 'jsonb DEFAULT'
    col_last_run_id = 'uuid'
    col_last_run_status = 'text'
    col_total_input_tokens = 'bigint DEFAULT 0 NOT NULL'
    col_total_output_tokens = 'bigint DEFAULT 0 NOT NULL'
    col_total_cached_input_tokens = 'bigint DEFAULT 0 NOT NULL'
    col_total_cost_cents = 'bigint DEFAULT 0 NOT NULL'
    col_last_error = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_agents()  # FK agent_id
    tbl_companies()  # FK company_id
    pass

def tbl_agent_wakeup_requests():
    """TABLE agent_wakeup_requests — 19 columns, 2 foreign keys. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_source = 'text NOT NULL'
    col_trigger_detail = 'text'
    col_reason = 'text'
    col_payload = 'jsonb'
    col_status = 'text DEFAULT'
    col_coalesced_count = 'integer DEFAULT 0 NOT NULL'
    col_requested_by_actor_type = 'text'
    col_requested_by_actor_id = 'text'
    col_idempotency_key = 'text'
    col_run_id = 'uuid'
    col_requested_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_claimed_at = 'timestamp with time zone'
    col_finished_at = 'timestamp with time zone'
    col_error = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    pass

def tbl_heartbeat_run_events():
    """TABLE heartbeat_run_events — 12 columns, 3 foreign keys. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    col_id = 'bigserial PRIMARY KEY NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_run_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_seq = 'integer NOT NULL'
    col_event_type = 'text NOT NULL'
    col_stream = 'text'
    col_level = 'text'
    col_color = 'text'
    col_message = 'text'
    col_payload = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_heartbeat_runs()  # FK run_id
    tbl_agents()  # FK agent_id
    pass

def idx_agent_runtime_state_company_agent_idx():
    """INDEX on agent_runtime_state. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    tbl_agent_runtime_state()

def idx_agent_runtime_state_company_updated_idx():
    """INDEX on agent_runtime_state. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    tbl_agent_runtime_state()

def idx_agent_wakeup_requests_company_agent_status_idx():
    """INDEX on agent_wakeup_requests. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    tbl_agent_wakeup_requests()

def idx_agent_wakeup_requests_company_requested_idx():
    """INDEX on agent_wakeup_requests. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    tbl_agent_wakeup_requests()

def idx_agent_wakeup_requests_agent_requested_idx():
    """INDEX on agent_wakeup_requests. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    tbl_agent_wakeup_requests()

def idx_heartbeat_run_events_run_seq_idx():
    """INDEX on heartbeat_run_events. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    tbl_heartbeat_run_events()

def idx_heartbeat_run_events_company_run_idx():
    """INDEX on heartbeat_run_events. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    tbl_heartbeat_run_events()

def idx_heartbeat_run_events_company_created_idx():
    """INDEX on heartbeat_run_events. src: packages/db/src/migrations/0001_fast_northstar.sql"""
    tbl_heartbeat_run_events()
