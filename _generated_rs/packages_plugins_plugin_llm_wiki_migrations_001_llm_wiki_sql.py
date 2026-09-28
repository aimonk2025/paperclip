"""SQL: packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql"""

def tbl_wiki_instances():
    """TABLE wiki_instances — 11 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_root_folder_key = 'text NOT NULL DEFAULT'
    col_configured_root_path = 'text'
    col_schema_version = 'integer NOT NULL DEFAULT 1'
    col_settings = 'jsonb NOT NULL DEFAULT'
    col_managed_agent_key = 'text'
    col_managed_project_key = 'text'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass

def tbl_wiki_sources():
    """TABLE wiki_sources — 12 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_source_type = 'text NOT NULL'
    col_title = 'text'
    col_url = 'text'
    col_raw_path = 'text NOT NULL'
    col_content_hash = 'text NOT NULL'
    col_status = 'text NOT NULL DEFAULT'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass

def tbl_wiki_pages():
    """TABLE wiki_pages — 13 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_path = 'text NOT NULL'
    col_title = 'text'
    col_page_type = 'text'
    col_frontmatter = 'jsonb NOT NULL DEFAULT'
    col_source_refs = 'jsonb NOT NULL DEFAULT'
    col_backlinks = 'jsonb NOT NULL DEFAULT'
    col_content_hash = 'text'
    col_current_revision_id = 'uuid'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass

def tbl_wiki_page_revisions():
    """TABLE wiki_page_revisions — 10 columns, 2 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_page_id = 'uuid REFERENCES plugin_llm_wiki_8f50da974f'
    col_operation_id = 'uuid'
    col_path = 'text NOT NULL'
    col_content_hash = 'text NOT NULL'
    col_summary = 'text'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    tbl_plugin_llm_wiki_8f50da974f()  # FK page_id
    pass

def tbl_wiki_operations():
    """TABLE wiki_operations — 14 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_operation_type = 'text NOT NULL'
    col_status = 'text NOT NULL'
    col_hidden_issue_id = 'uuid REFERENCES public'
    col_project_id = 'uuid REFERENCES public'
    col_run_ids = 'jsonb NOT NULL DEFAULT'
    col_cost_cents = 'integer NOT NULL DEFAULT 0'
    col_warnings = 'jsonb NOT NULL DEFAULT'
    col_affected_pages = 'jsonb NOT NULL DEFAULT'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass

def tbl_wiki_query_sessions():
    """TABLE wiki_query_sessions — 9 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_hidden_issue_id = 'uuid REFERENCES public'
    col_agent_session_id = 'text'
    col_status = 'text NOT NULL DEFAULT'
    col_filed_outputs = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass

def tbl_wiki_resource_bindings():
    """TABLE wiki_resource_bindings — 9 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/001_llm_wiki.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL'
    col_resource_kind = 'text NOT NULL'
    col_resource_key = 'text NOT NULL'
    col_resolved_id = 'uuid'
    col_metadata = 'jsonb NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass
