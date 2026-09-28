"""SQL: packages/db/src/migrations/0047_overjoyed_groot.sql"""

def tbl_feedback_exports():
    """TABLE feedback_exports — 26 columns, 4 foreign keys. src: packages/db/src/migrations/0047_overjoyed_groot.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_feedback_vote_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_project_id = 'uuid'
    col_author_user_id = 'text NOT NULL'
    col_target_type = 'text NOT NULL'
    col_target_id = 'text NOT NULL'
    col_vote = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_destination = 'text'
    col_export_id = 'text'
    col_consent_version = 'text'
    col_schema_version = 'text DEFAULT'
    col_bundle_version = 'text DEFAULT'
    col_payload_version = 'text DEFAULT'
    col_payload_digest = 'text'
    col_payload_snapshot = 'jsonb'
    col_target_summary = 'jsonb NOT NULL'
    col_redaction_summary = 'jsonb'
    col_attempt_count = 'integer DEFAULT 0 NOT NULL'
    col_last_attempted_at = 'timestamp with time zone'
    col_exported_at = 'timestamp with time zone'
    col_failure_reason = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_feedback_votes()  # FK feedback_vote_id
    tbl_issues()  # FK issue_id
    tbl_projects()  # FK project_id
    pass

def tbl_feedback_votes():
    """TABLE feedback_votes — 14 columns, 2 foreign keys. src: packages/db/src/migrations/0047_overjoyed_groot.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_target_type = 'text NOT NULL'
    col_target_id = 'text NOT NULL'
    col_author_user_id = 'text NOT NULL'
    col_vote = 'text NOT NULL'
    col_reason = 'text'
    col_shared_with_labs = 'boolean DEFAULT false NOT NULL'
    col_shared_at = 'timestamp with time zone'
    col_consent_version = 'text'
    col_redaction_summary = 'jsonb'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    pass
