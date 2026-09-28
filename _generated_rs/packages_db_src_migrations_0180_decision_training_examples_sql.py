"""SQL: packages/db/src/migrations/0180_decision_training_examples.sql"""

def tbl_decision_training_examples():
    """TABLE decision_training_examples — 13 columns, 2 foreign keys. src: packages/db/src/migrations/0180_decision_training_examples.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL REFERENCES'
    col_source_kind = 'text NOT NULL'
    col_source_id = 'uuid NOT NULL'
    col_issue_id = 'uuid NOT NULL REFERENCES'
    col_cutoff_at = 'timestamp with time zone NOT NULL'
    col_notes = 'text DEFAULT'
    col_notes_history = 'jsonb DEFAULT'
    col_decision_outcome = 'text'
    col_snapshot = 'jsonb NOT NULL'
    col_created_by_user_id = 'text NOT NULL'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_issues()  # FK issue_id
    pass
