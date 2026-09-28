"""SQL: packages/db/src/migrations/0007_new_quentin_quire.sql"""

def tbl_agent_task_sessions():
    """TABLE agent_task_sessions — 11 columns, 3 foreign keys. src: packages/db/src/migrations/0007_new_quentin_quire.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_agent_id = 'uuid NOT NULL'
    col_adapter_type = 'text NOT NULL'
    col_task_key = 'text NOT NULL'
    col_session_params_json = 'jsonb'
    col_session_display_id = 'text'
    col_last_run_id = 'uuid'
    col_last_error = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK agent_id
    tbl_heartbeat_runs()  # FK last_run_id
    pass

def idx_agent_task_sessions_company_agent_adapter_task_uniq():
    """INDEX on agent_task_sessions. src: packages/db/src/migrations/0007_new_quentin_quire.sql"""
    tbl_agent_task_sessions()

def idx_agent_task_sessions_company_agent_updated_idx():
    """INDEX on agent_task_sessions. src: packages/db/src/migrations/0007_new_quentin_quire.sql"""
    tbl_agent_task_sessions()

def idx_agent_task_sessions_company_task_updated_idx():
    """INDEX on agent_task_sessions. src: packages/db/src/migrations/0007_new_quentin_quire.sql"""
    tbl_agent_task_sessions()
