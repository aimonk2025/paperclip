"""SQL: packages/db/src/migrations/0148_tool_access_mcp_connections.sql"""

def tbl_tool_applications():
    """TABLE tool_applications — 8 columns, 3 foreign keys. src: packages/db/src/migrations/0148_tool_access_mcp_connections.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_type = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_metadata = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_plugins()  # FK plugin_id
    tbl_agents()  # FK owner_agent_id
    pass

def tbl_tool_connections():
    """TABLE tool_connections — 15 columns, 3 foreign keys. src: packages/db/src/migrations/0148_tool_access_mcp_connections.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_application_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_transport = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_enabled = 'boolean DEFAULT false NOT NULL'
    col_config = 'jsonb DEFAULT'
    col_credential_refs = 'jsonb DEFAULT'
    col_health_status = 'text DEFAULT'
    col_health_message = 'text'
    col_last_health_at = 'timestamp with time zone'
    col_last_catalog_refresh_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_tool_applications()  # FK application_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_by_agent_id
    pass

def tbl_tool_catalog_entries():
    """TABLE tool_catalog_entries — 17 columns, 4 foreign keys. src: packages/db/src/migrations/0148_tool_access_mcp_connections.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_connection_id = 'uuid NOT NULL'
    col_name = 'text NOT NULL'
    col_title = 'text'
    col_description = 'text'
    col_input_schema = 'jsonb DEFAULT'
    col_annotations = 'jsonb DEFAULT'
    col_risk_level = 'text DEFAULT'
    col_status = 'text DEFAULT'
    col_version_hash = 'text NOT NULL'
    col_first_seen_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_last_seen_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_quarantined_at = 'timestamp with time zone'
    col_quarantine_reason = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_connections()  # FK connection_id
    tbl_tool_applications()  # FK application_id
    tbl_agents()  # FK reviewed_by_agent_id
    pass

def tbl_tool_runtime_slots():
    """TABLE tool_runtime_slots — 14 columns, 6 foreign keys. src: packages/db/src/migrations/0148_tool_access_mcp_connections.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_connection_id = 'uuid NOT NULL'
    col_slot_key = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_provider_ref = 'text'
    col_health_status = 'text DEFAULT'
    col_health_message = 'text'
    col_last_started_at = 'timestamp with time zone'
    col_last_used_at = 'timestamp with time zone'
    col_idle_deadline_at = 'timestamp with time zone'
    col_metadata = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_tool_connections()  # FK connection_id
    tbl_tool_applications()  # FK application_id
    tbl_project_workspaces()  # FK project_workspace_id
    tbl_execution_workspaces()  # FK execution_workspace_id
    tbl_issues()  # FK issue_id
    pass

def tbl_tool_access_audit_events():
    """TABLE tool_access_audit_events — 11 columns, 5 foreign keys. src: packages/db/src/migrations/0148_tool_access_mcp_connections.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_connection_id = 'uuid'
    col_catalog_entry_id = 'uuid'
    col_actor_type = 'text DEFAULT'
    col_actor_id = 'text'
    col_action = 'text NOT NULL'
    col_outcome = 'text NOT NULL'
    col_reason_code = 'text'
    col_details = 'jsonb DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_tool_mcp_gateways()  # FK gateway_id
    tbl_tool_mcp_gateway_tokens()  # FK gateway_token_id
    tbl_companies()  # FK company_id
    tbl_tool_connections()  # FK connection_id
    tbl_tool_catalog_entries()  # FK catalog_entry_id
    pass
