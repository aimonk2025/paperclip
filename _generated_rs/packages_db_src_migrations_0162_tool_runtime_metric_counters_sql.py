"""SQL: packages/db/src/migrations/0162_tool_runtime_metric_counters.sql"""

def tbl_tool_runtime_metric_counters():
    """TABLE tool_runtime_metric_counters — 7 columns, 1 foreign keys. src: packages/db/src/migrations/0162_tool_runtime_metric_counters.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_metric = 'text NOT NULL'
    col_bucket_start_at = 'timestamp with time zone NOT NULL'
    col_count = 'integer DEFAULT 0 NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass
