"""SQL: packages/db/src/migrations/0206_review_path_recovery_idempotency_index.sql"""

def idx_agent_wakeup_requests_review_path_recovery_idempotency_uq():
    """INDEX on agent_wakeup_requests. src: packages/db/src/migrations/0206_review_path_recovery_idempotency_index.sql"""
    tbl_agent_wakeup_requests()
