"""SQL: packages/db/src/migrations/0106_external_object_references.sql"""

def tbl_external_objects():
    """TABLE external_objects — 26 columns, 2 foreign keys. src: packages/db/src/migrations/0106_external_object_references.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_provider_key = 'text NOT NULL'
    col_plugin_id = 'uuid'
    col_object_type = 'text NOT NULL'
    col_external_id = 'text NOT NULL'
    col_sanitized_canonical_url = 'text'
    col_canonical_identity_hash = 'text'
    col_display_title = 'text'
    col_status_key = 'text'
    col_status_label = 'text'
    col_status_category = 'text DEFAULT'
    col_status_tone = 'text DEFAULT'
    col_liveness = 'text DEFAULT'
    col_is_terminal = 'boolean DEFAULT false NOT NULL'
    col_data = 'jsonb DEFAULT'
    col_remote_version = 'text'
    col_etag = 'text'
    col_last_resolved_at = 'timestamp with time zone'
    col_last_changed_at = 'timestamp with time zone'
    col_last_error_at = 'timestamp with time zone'
    col_next_refresh_at = 'timestamp with time zone'
    col_last_error_code = 'text'
    col_last_error_message = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_plugins()  # FK plugin_id
    pass

def tbl_external_object_mentions():
    """TABLE external_object_mentions — 19 columns, 4 foreign keys. src: packages/db/src/migrations/0106_external_object_references.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_source_issue_id = 'uuid NOT NULL'
    col_source_kind = 'text NOT NULL'
    col_source_record_id = 'uuid'
    col_document_key = 'text'
    col_property_key = 'text'
    col_matched_text_redacted = 'text'
    col_sanitized_display_url = 'text'
    col_canonical_identity_hash = 'text'
    col_canonical_identity = 'jsonb'
    col_object_id = 'uuid'
    col_provider_key = 'text'
    col_detector_key = 'text'
    col_object_type = 'text'
    col_confidence = 'text DEFAULT'
    col_created_by_plugin_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK source_issue_id
    tbl_external_objects()  # FK object_id
    tbl_plugins()  # FK created_by_plugin_id
    pass
