"""SQL: packages/db/src/migrations/0185_status_cards.sql"""

def tbl_status_cards():
    """TABLE status_cards — 31 columns, 4 foreign keys. src: packages/db/src/migrations/0185_status_cards.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_created_by_user_id = 'text'
    col_created_by_agent_id = 'uuid'
    col_title = 'text'
    col_title_pinned = 'boolean DEFAULT false NOT NULL'
    col_interest_prompt = 'text NOT NULL'
    col_queries = 'jsonb DEFAULT'
    col_query_version = 'integer DEFAULT 0 NOT NULL'
    col_query_compiled_at = 'timestamp with time zone'
    col_query_compiled_by_agent_id = 'uuid'
    col_instructions_mode = 'text DEFAULT'
    col_instructions = 'text'
    col_refresh_policy = 'jsonb NOT NULL'
    col_state = 'text DEFAULT'
    col_pending_change_count = 'integer DEFAULT 0 NOT NULL'
    col_last_change_at = 'timestamp with time zone'
    col_fingerprint = 'jsonb'
    col_fingerprint_at = 'timestamp with time zone'
    col_document_id = 'uuid'
    col_last_update_run_kind = 'text'
    col_last_generated_at = 'timestamp with time zone'
    col_last_model = 'text'
    col_generating_issue_id = 'uuid'
    col_failure_reason = 'text'
    col_next_eval_at = 'timestamp with time zone'
    col_archived_at = 'timestamp with time zone'
    col_archived_by_user_id = 'text'
    col_archived_by_agent_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_agents()  # FK agent_id
    tbl_companies()  # FK company_id
    tbl_documents()  # FK document_id
    tbl_issues()  # FK generating_issue_id
    pass

def tbl_status_card_updates():
    """TABLE status_card_updates — 15 columns, 3 foreign keys. src: packages/db/src/migrations/0185_status_cards.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_card_id = 'uuid NOT NULL'
    col_kind = 'text NOT NULL'
    col_trigger = 'text NOT NULL'
    col_generation_issue_id = 'uuid'
    col_run_id = 'uuid'
    col_changes = 'jsonb DEFAULT'
    col_input_tokens = 'integer DEFAULT 0 NOT NULL'
    col_output_tokens = 'integer DEFAULT 0 NOT NULL'
    col_cost_cents = 'integer DEFAULT 0 NOT NULL'
    col_model = 'text'
    col_started_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_finished_at = 'timestamp with time zone'
    col_status = 'text NOT NULL'
    col_error = 'text'
    tbl_status_cards()  # FK card_id
    tbl_issues()  # FK generation_issue_id
    tbl_heartbeat_runs()  # FK run_id
    pass
