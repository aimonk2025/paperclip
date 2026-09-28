"""SQL: packages/db/src/migrations/0099_skills_store_foundation.sql"""

def tbl_company_skill_versions():
    """TABLE company_skill_versions — 9 columns, 3 foreign keys. src: packages/db/src/migrations/0099_skills_store_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_company_skill_id = 'uuid NOT NULL'
    col_revision_number = 'integer NOT NULL'
    col_label = 'text'
    col_file_inventory = 'jsonb DEFAULT'
    col_author_agent_id = 'uuid'
    col_author_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_company_skills()  # FK company_skill_id
    tbl_agents()  # FK author_agent_id
    pass

def tbl_company_skill_stars():
    """TABLE company_skill_stars — 6 columns, 3 foreign keys. src: packages/db/src/migrations/0099_skills_store_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_company_skill_id = 'uuid NOT NULL'
    col_agent_id = 'uuid'
    col_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_company_skills()  # FK company_skill_id
    tbl_agents()  # FK agent_id
    pass

def tbl_company_skill_comments():
    """TABLE company_skill_comments — 10 columns, 4 foreign keys. src: packages/db/src/migrations/0099_skills_store_foundation.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_company_skill_id = 'uuid NOT NULL'
    col_parent_comment_id = 'uuid'
    col_author_agent_id = 'uuid'
    col_author_user_id = 'text'
    col_body = 'text NOT NULL'
    col_deleted_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    tbl_company_skills()  # FK company_skill_id
    tbl_company_skill_comments()  # FK parent_comment_id
    tbl_agents()  # FK author_agent_id
    pass
