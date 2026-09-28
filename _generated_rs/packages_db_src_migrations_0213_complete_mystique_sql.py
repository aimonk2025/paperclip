"""SQL: packages/db/src/migrations/0213_complete_mystique.sql"""

def tbl_company_transfer_runs():
    """TABLE company_transfer_runs — 17 columns, 1 foreign keys. src: packages/db/src/migrations/0213_complete_mystique.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid'
    col_direction = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_actor_key = 'text NOT NULL'
    col_container_ref = 'jsonb NOT NULL'
    col_idempotency_key = 'text NOT NULL'
    col_manifest_sha256 = 'text'
    col_manifest = 'jsonb'
    col_chunk_count = 'integer DEFAULT 0 NOT NULL'
    col_blob_count = 'integer DEFAULT 0 NOT NULL'
    col_completed_parts = 'jsonb DEFAULT'
    col_error = 'text'
    col_started_at = 'timestamp with time zone'
    col_finished_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def idx_company_transfer_runs_company_idx():
    """INDEX on company_transfer_runs. src: packages/db/src/migrations/0213_complete_mystique.sql"""
    tbl_company_transfer_runs()

def idx_company_transfer_runs_idempotency_direction_idx():
    """INDEX on company_transfer_runs. src: packages/db/src/migrations/0213_complete_mystique.sql"""
    tbl_company_transfer_runs()

def idx_company_transfer_runs_actor_status_idx():
    """INDEX on company_transfer_runs. src: packages/db/src/migrations/0213_complete_mystique.sql"""
    tbl_company_transfer_runs()
