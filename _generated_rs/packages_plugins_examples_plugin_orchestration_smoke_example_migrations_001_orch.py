"""SQL: packages/plugins/examples/plugin-orchestration-smoke-example/migrations/001_orchestration_smoke.sql"""

def tbl_smoke_runs():
    """TABLE smoke_runs — 8 columns, 2 foreign keys. src: packages/plugins/examples/plugin-orchestration-smoke-example/migrations/001_orchestration_smoke.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_root_issue_id = 'uuid NOT NULL REFERENCES public'
    col_child_issue_id = 'uuid REFERENCES public'
    col_blocker_issue_id = 'uuid REFERENCES public'
    col_billing_code = 'text NOT NULL'
    col_last_summary = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK root_issue_id
    tbl_companies()  # FK company_id
    pass
