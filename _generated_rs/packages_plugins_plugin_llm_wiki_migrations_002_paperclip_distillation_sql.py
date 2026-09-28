"""SQL: packages/plugins/plugin-llm-wiki/migrations/002_paperclip_distillation.sql"""

def tbl_paperclip_distillation_cursors():
    """TABLE paperclip_distillation_cursors — 16 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/002_paperclip_distillation.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_source_scope = 'text NOT NULL'
    col_scope_key = 'text NOT NULL'
    col_project_id = 'uuid REFERENCES public'
    col_root_issue_id = 'uuid REFERENCES public'
    col_source_kind = 'text NOT NULL DEFAULT'
    col_last_processed_at = 'timestamptz'
    col_last_observed_at = 'timestamptz'
    col_pending_event_count = 'integer NOT NULL DEFAULT 0'
    col_last_successful_run_id = 'uuid'
    col_last_source_hash = 'text'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass

def tbl_paperclip_distillation_work_items():
    """TABLE paperclip_distillation_work_items — 13 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/002_paperclip_distillation.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_work_item_kind = 'text NOT NULL'
    col_status = 'text NOT NULL DEFAULT'
    col_priority = 'text NOT NULL DEFAULT'
    col_project_id = 'uuid REFERENCES public'
    col_root_issue_id = 'uuid REFERENCES public'
    col_requested_by_issue_id = 'uuid REFERENCES public'
    col_idempotency_key = 'text'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass

def tbl_paperclip_distillation_runs():
    """TABLE paperclip_distillation_runs — 18 columns, 2 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/002_paperclip_distillation.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_cursor_id = 'uuid REFERENCES plugin_llm_wiki_8f50da974f'
    col_work_item_id = 'uuid REFERENCES plugin_llm_wiki_8f50da974f'
    col_project_id = 'uuid REFERENCES public'
    col_root_issue_id = 'uuid REFERENCES public'
    col_source_window_start = 'timestamptz'
    col_source_window_end = 'timestamptz'
    col_source_hash = 'text'
    col_status = 'text NOT NULL'
    col_operation_issue_id = 'uuid REFERENCES public'
    col_retry_count = 'integer NOT NULL DEFAULT 0'
    col_cost_cents = 'integer NOT NULL DEFAULT 0'
    col_warnings = 'jsonb NOT NULL DEFAULT'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    tbl_plugin_llm_wiki_8f50da974f()  # FK cursor_id
    pass

def tbl_paperclip_source_snapshots():
    """TABLE paperclip_source_snapshots — 13 columns, 2 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/002_paperclip_distillation.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_distillation_run_id = 'uuid REFERENCES plugin_llm_wiki_8f50da974f'
    col_project_id = 'uuid REFERENCES public'
    col_root_issue_id = 'uuid REFERENCES public'
    col_source_hash = 'text NOT NULL'
    col_max_characters = 'integer NOT NULL'
    col_clipped = 'boolean NOT NULL DEFAULT false'
    col_source_refs = 'jsonb NOT NULL DEFAULT'
    col_bundle_markdown = 'text NOT NULL'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    tbl_plugin_llm_wiki_8f50da974f()  # FK distillation_run_id
    pass

def tbl_paperclip_page_bindings():
    """TABLE paperclip_page_bindings — 11 columns, 2 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/002_paperclip_distillation.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_project_id = 'uuid REFERENCES public'
    col_root_issue_id = 'uuid REFERENCES public'
    col_page_path = 'text NOT NULL'
    col_last_applied_source_hash = 'text'
    col_last_distillation_run_id = 'uuid REFERENCES plugin_llm_wiki_8f50da974f'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    tbl_plugin_llm_wiki_8f50da974f()  # FK last_distillation_run_id
    pass
