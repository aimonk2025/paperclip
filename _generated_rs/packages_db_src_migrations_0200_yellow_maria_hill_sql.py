"""SQL: packages/db/src/migrations/0200_yellow_maria_hill.sql"""

def tbl_decision_archive_notification_outbox():
    """TABLE decision_archive_notification_outbox — 13 columns, 2 foreign keys. src: packages/db/src/migrations/0200_yellow_maria_hill.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_source_kind = 'text NOT NULL'
    col_source_id = 'text NOT NULL'
    col_archive_version = 'integer NOT NULL'
    col_origin_agent_id = 'uuid NOT NULL'
    col_origin_issue_id = 'uuid NOT NULL'
    col_status = 'text DEFAULT'
    col_attempt_count = 'integer DEFAULT 0 NOT NULL'
    col_last_attempt_at = 'timestamp with time zone'
    col_delivered_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_agents()  # FK origin_agent_id
    pass

def tbl_decision_retention():
    """TABLE decision_retention — 19 columns, 3 foreign keys. src: packages/db/src/migrations/0200_yellow_maria_hill.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_source_kind = 'text NOT NULL'
    col_source_id = 'text NOT NULL'
    col_source_activity_at = 'timestamp with time zone NOT NULL'
    col_keep = 'boolean DEFAULT false NOT NULL'
    col_archived_at = 'timestamp with time zone'
    col_archived_reason = 'text'
    col_archived_by_type = 'text'
    col_archived_by_agent_id = 'uuid'
    col_archived_by_user_id = 'text'
    col_archived_by_run_id = 'uuid'
    col_version = 'integer DEFAULT 1 NOT NULL'
    col_archive_version = 'integer DEFAULT 0 NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_or = '('
    col_or = '('
    col_or = '('
    tbl_companies()  # FK company_id
    tbl_agents()  # FK archived_by_agent_id
    tbl_heartbeat_runs()  # FK archived_by_run_id
    pass
