"""SQL: packages/db/src/migrations/0166_smoke_lab_results.sql"""

def tbl_smoke_runs():
    """TABLE smoke_runs — 9 columns, 1 foreign keys. src: packages/db/src/migrations/0166_smoke_lab_results.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_trigger = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_started_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_finished_at = 'timestamp with time zone'
    col_summary = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def tbl_smoke_run_steps():
    """TABLE smoke_run_steps — 11 columns, 2 foreign keys. src: packages/db/src/migrations/0166_smoke_lab_results.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_run_id = 'uuid NOT NULL'
    col_path = 'text NOT NULL'
    col_scenario_step = 'text NOT NULL'
    col_status = 'text NOT NULL'
    col_detail = 'text'
    col_screenshot_artifact_ref = 'jsonb'
    col_duration_ms = 'integer'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_smoke_runs()  # FK run_id
    pass
