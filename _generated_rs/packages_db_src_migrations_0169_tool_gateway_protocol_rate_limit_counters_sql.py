"""SQL: packages/db/src/migrations/0169_tool_gateway_protocol_rate_limit_counters.sql"""

def tbl_tool_gateway_rate_limit_counters():
    """TABLE tool_gateway_rate_limit_counters — 10 columns, 1 foreign keys. src: packages/db/src/migrations/0169_tool_gateway_protocol_rate_limit_counters.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_counter_key = 'text NOT NULL'
    col_window_start_at = 'timestamp with time zone NOT NULL'
    col_window_ms = 'integer NOT NULL'
    col_limit = 'integer NOT NULL'
    col_count = 'integer DEFAULT 0 NOT NULL'
    col_reset_at = 'timestamp with time zone NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass
