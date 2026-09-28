"""SQL: packages/db/src/migrations/0091_old_swarm.sql"""

def tbl_document_annotation_threads():
    """TABLE document_annotation_threads — 27 columns, 7 foreign keys. src: packages/db/src/migrations/0091_old_swarm.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_document_id = 'uuid NOT NULL'
    col_document_key = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_anchor_state = 'text DEFAULT'
    col_original_revision_id = 'uuid'
    col_original_revision_number = 'integer NOT NULL'
    col_current_revision_id = 'uuid'
    col_current_revision_number = 'integer NOT NULL'
    col_selected_text = 'text NOT NULL'
    col_prefix_text = 'text DEFAULT'
    col_suffix_text = 'text DEFAULT'
    col_normalized_start = 'integer NOT NULL'
    col_normalized_end = 'integer NOT NULL'
    col_markdown_start = 'integer NOT NULL'
    col_markdown_end = 'integer NOT NULL'
    col_anchor_confidence = 'text DEFAULT'
    col_anchor_selector = 'jsonb NOT NULL'
    col_created_by_agent_id = 'uuid'
    col_created_by_user_id = 'text'
    col_resolved_by_agent_id = 'uuid'
    col_resolved_by_user_id = 'text'
    col_resolved_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_cases()  # FK case_id
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    tbl_documents()  # FK document_id
    tbl_document_revisions()  # FK original_revision_id
    tbl_agents()  # FK created_by_agent_id
    tbl_routines()  # FK routine_id
    pass

def tbl_document_annotation_comments():
    """TABLE document_annotation_comments — 12 columns, 9 foreign keys. src: packages/db/src/migrations/0091_old_swarm.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_thread_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL'
    col_document_id = 'uuid NOT NULL'
    col_body = 'text NOT NULL'
    col_author_type = 'text NOT NULL'
    col_author_agent_id = 'uuid'
    col_author_user_id = 'text'
    col_created_by_run_id = 'uuid'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_issue_comments()  # FK issue_comment_id
    tbl_cases()  # FK case_id
    tbl_companies()  # FK company_id
    tbl_document_annotation_threads()  # FK thread_id
    tbl_issues()  # FK issue_id
    tbl_documents()  # FK document_id
    tbl_agents()  # FK author_agent_id
    tbl_heartbeat_runs()  # FK created_by_run_id
    tbl_routines()  # FK routine_id
    pass

def tbl_document_annotation_anchor_snapshots():
    """TABLE document_annotation_anchor_snapshots — 14 columns, 4 foreign keys. src: packages/db/src/migrations/0091_old_swarm.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_thread_id = 'uuid NOT NULL'
    col_document_id = 'uuid NOT NULL'
    col_from_revision_id = 'uuid'
    col_from_revision_number = 'integer'
    col_to_revision_id = 'uuid'
    col_to_revision_number = 'integer NOT NULL'
    col_previous_anchor = 'jsonb NOT NULL'
    col_next_anchor = 'jsonb'
    col_anchor_state = 'text NOT NULL'
    col_anchor_confidence = 'text NOT NULL'
    col_failure_reason = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_document_annotation_threads()  # FK thread_id
    tbl_documents()  # FK document_id
    tbl_document_revisions()  # FK from_revision_id
    pass
