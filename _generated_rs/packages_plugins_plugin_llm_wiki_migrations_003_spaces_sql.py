"""SQL: packages/plugins/plugin-llm-wiki/migrations/003_spaces.sql"""

def tbl_wiki_spaces():
    """TABLE wiki_spaces — 18 columns, 1 foreign keys. src: packages/plugins/plugin-llm-wiki/migrations/003_spaces.sql"""
    col_id = 'uuid PRIMARY KEY'
    col_company_id = 'uuid NOT NULL REFERENCES public'
    col_wiki_id = 'text NOT NULL DEFAULT'
    col_slug = 'text NOT NULL'
    col_display_name = 'text NOT NULL'
    col_space_type = 'text NOT NULL DEFAULT'
    col_folder_mode = 'text NOT NULL DEFAULT'
    col_root_folder_key = 'text NOT NULL DEFAULT'
    col_path_prefix = 'text'
    col_configured_root_path = 'text'
    col_access_scope = 'text NOT NULL DEFAULT'
    col_owner_user_id = 'text'
    col_owner_agent_id = 'uuid REFERENCES public'
    col_team_key = 'text'
    col_settings = 'jsonb NOT NULL DEFAULT'
    col_status = 'text NOT NULL DEFAULT'
    col_created_at = 'timestamptz NOT NULL DEFAULT now()'
    col_updated_at = 'timestamptz NOT NULL DEFAULT now()'
    tbl_public()  # FK company_id
    pass
