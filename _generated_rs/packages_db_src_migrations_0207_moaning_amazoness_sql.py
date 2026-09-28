"""SQL: packages/db/src/migrations/0207_moaning_amazoness.sql"""

def tbl_company_secret_proposals():
    """TABLE company_secret_proposals — 32 columns, 7 foreign keys. src: packages/db/src/migrations/0207_moaning_amazoness.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_kind = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_proposed_name = 'text'
    col_proposed_key = 'text'
    col_proposed_description = 'text'
    col_justification = 'text NOT NULL'
    col_value_ciphertext = 'jsonb'
    col_value_fingerprint_sha256 = 'text'
    col_value_length = 'integer'
    col_secret_id = 'uuid'
    col_secret_proposal_id = 'uuid'
    col_target_type = 'text'
    col_target_id = 'uuid'
    col_config_path = 'text'
    col_projection_class = 'text DEFAULT'
    col_binding_target_policy_snapshot = 'text'
    col_proposer_ancestor_ids_snapshot = 'jsonb'
    col_target_ancestor_ids_snapshot = 'jsonb'
    col_proposed_by_agent_id = 'uuid NOT NULL'
    col_origin_issue_id = 'uuid'
    col_origin_run_id = 'uuid NOT NULL'
    col_resolved_by_user_id = 'text'
    col_resolved_at = 'timestamp with time zone'
    col_resolution_reason = 'text'
    col_created_secret_id = 'uuid'
    col_applied_binding_config_path = 'text'
    col_ciphertext_scrubbed_at = 'timestamp with time zone'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_company_secrets()  # FK secret_id
    tbl_company_secret_proposals()  # FK secret_proposal_id
    tbl_agents()  # FK target_id
    tbl_issues()  # FK origin_issue_id
    tbl_heartbeat_runs()  # FK origin_run_id
    tbl_issue_thread_interactions()  # FK interaction_id
    pass
