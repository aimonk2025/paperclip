"""SQL: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""

def tbl_account():
    """TABLE account — 13 columns, 1 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'text PRIMARY KEY NOT NULL'
    col_account_id = 'text NOT NULL'
    col_provider_id = 'text NOT NULL'
    col_user_id = 'text NOT NULL'
    col_access_token = 'text'
    col_refresh_token = 'text'
    col_id_token = 'text'
    col_access_token_expires_at = 'timestamp with time zone'
    col_refresh_token_expires_at = 'timestamp with time zone'
    col_scope = 'text'
    col_password = 'text'
    col_created_at = 'timestamp with time zone NOT NULL'
    col_updated_at = 'timestamp with time zone NOT NULL'
    tbl_user()  # FK user_id
    pass

def tbl_session():
    """TABLE session — 8 columns, 1 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'text PRIMARY KEY NOT NULL'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_token = 'text NOT NULL'
    col_created_at = 'timestamp with time zone NOT NULL'
    col_updated_at = 'timestamp with time zone NOT NULL'
    col_ip_address = 'text'
    col_user_agent = 'text'
    col_user_id = 'text NOT NULL'
    tbl_user()  # FK user_id
    pass

def tbl_user():
    """TABLE user — 7 columns, 0 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'text PRIMARY KEY NOT NULL'
    col_name = 'text NOT NULL'
    col_email = 'text NOT NULL'
    col_email_verified = 'boolean DEFAULT false NOT NULL'
    col_image = 'text'
    col_created_at = 'timestamp with time zone NOT NULL'
    col_updated_at = 'timestamp with time zone NOT NULL'
    pass

def tbl_verification():
    """TABLE verification — 6 columns, 0 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'text PRIMARY KEY NOT NULL'
    col_identifier = 'text NOT NULL'
    col_value = 'text NOT NULL'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_created_at = 'timestamp with time zone'
    col_updated_at = 'timestamp with time zone'
    pass

def tbl_company_memberships():
    """TABLE company_memberships — 8 columns, 1 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_principal_type = 'text NOT NULL'
    col_principal_id = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_membership_role = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def tbl_instance_user_roles():
    """TABLE instance_user_roles — 5 columns, 0 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_user_id = 'text NOT NULL'
    col_role = 'text DEFAULT'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    pass

def tbl_invites():
    """TABLE invites — 12 columns, 1 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid'
    col_invite_type = 'text DEFAULT'
    col_token_hash = 'text NOT NULL'
    col_allowed_join_types = 'text DEFAULT'
    col_defaults_payload = 'jsonb'
    col_expires_at = 'timestamp with time zone NOT NULL'
    col_invited_by_user_id = 'text'
    col_revoked_at = 'timestamp with time zone'
    col_accepted_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def tbl_join_requests():
    """TABLE join_requests — 19 columns, 3 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_invite_id = 'uuid NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_request_type = 'text NOT NULL'
    col_status = 'text DEFAULT'
    col_request_ip = 'text NOT NULL'
    col_requesting_user_id = 'text'
    col_request_email_snapshot = 'text'
    col_agent_name = 'text'
    col_adapter_type = 'text'
    col_capabilities = 'text'
    col_agent_defaults_payload = 'jsonb'
    col_created_agent_id = 'uuid'
    col_approved_by_user_id = 'text'
    col_approved_at = 'timestamp with time zone'
    col_rejected_by_user_id = 'text'
    col_rejected_at = 'timestamp with time zone'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_invites()  # FK invite_id
    tbl_companies()  # FK company_id
    tbl_agents()  # FK created_agent_id
    pass

def tbl_principal_permission_grants():
    """TABLE principal_permission_grants — 9 columns, 1 foreign keys. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    col_id = 'uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL'
    col_company_id = 'uuid NOT NULL'
    col_principal_type = 'text NOT NULL'
    col_principal_id = 'text NOT NULL'
    col_permission_key = 'text NOT NULL'
    col_scope = 'jsonb'
    col_granted_by_user_id = 'text'
    col_created_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    col_updated_at = 'timestamp with time zone DEFAULT now() NOT NULL'
    tbl_companies()  # FK company_id
    pass

def idx_company_memberships_company_principal_unique_idx():
    """INDEX on company_memberships. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_company_memberships()

def idx_company_memberships_principal_status_idx():
    """INDEX on company_memberships. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_company_memberships()

def idx_company_memberships_company_status_idx():
    """INDEX on company_memberships. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_company_memberships()

def idx_instance_user_roles_user_role_unique_idx():
    """INDEX on instance_user_roles. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_instance_user_roles()

def idx_instance_user_roles_role_idx():
    """INDEX on instance_user_roles. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_instance_user_roles()

def idx_invites_token_hash_unique_idx():
    """INDEX on invites. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_invites()

def idx_invites_company_invite_state_idx():
    """INDEX on invites. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_invites()

def idx_join_requests_invite_unique_idx():
    """INDEX on join_requests. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_join_requests()

def idx_join_requests_company_status_type_created_idx():
    """INDEX on join_requests. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_join_requests()

def idx_principal_permission_grants_unique_idx():
    """INDEX on principal_permission_grants. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_principal_permission_grants()

def idx_principal_permission_grants_company_permission_idx():
    """INDEX on principal_permission_grants. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_principal_permission_grants()

def idx_issues_company_assignee_user_status_idx():
    """INDEX on issues. src: packages/db/src/migrations/0014_many_mikhail_rasputin.sql"""
    tbl_issues()
