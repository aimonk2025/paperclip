"""DOC: docs/deploy/aws-ecs.md"""

def doc_prerequisites():
    """H2: Prerequisites — src: docs/deploy/aws-ecs.md"""
    pass

def doc__1_create_ecr_repository():
    """H2: 1. Create ECR Repository — src: docs/deploy/aws-ecs.md"""
    pass

def doc__2_build_and_push_docker_image():
    """H2: 2. Build and Push Docker Image — src: docs/deploy/aws-ecs.md"""
    pass

def doc_authenticate_docker_to_ecr():
    """H1: Authenticate Docker to ECR — src: docs/deploy/aws-ecs.md"""
    pass

def doc_build():
    """H1: Build — src: docs/deploy/aws-ecs.md"""
    pass

def doc_tag_and_push():
    """H1: Tag and push — src: docs/deploy/aws-ecs.md"""
    pass

def doc__3_networking_vpc_subnets_security_groups():
    """H2: 3. Networking (VPC, Subnets, Security Groups) — src: docs/deploy/aws-ecs.md"""
    pass

def doc_get_default_vpc():
    """H1: Get default VPC — src: docs/deploy/aws-ecs.md"""
    pass

def doc_get_two_public_subnets_for_alb():
    """H1: Get two public subnets (for ALB) — src: docs/deploy/aws-ecs.md"""
    pass

def doc_alb_security_group_inbound_https():
    """H1: ALB security group — inbound HTTPS — src: docs/deploy/aws-ecs.md"""
    pass

def doc_also_open_port_80_so_the_alb_can_accept_http_and_redirect_to_https():
    """H1: Also open port 80 so the ALB can accept HTTP and redirect to HTTPS — src: docs/deploy/aws-ecs.md"""
    pass

def doc_ecs_task_security_group_inbound_from_alb_only():
    """H1: ECS task security group — inbound from ALB only — src: docs/deploy/aws-ecs.md"""
    pass

def doc_rds_security_group_inbound_from_ecs_only():
    """H1: RDS security group — inbound from ECS only — src: docs/deploy/aws-ecs.md"""
    pass

def doc_efs_security_group_inbound_nfs_from_ecs_only():
    """H1: EFS security group — inbound NFS from ECS only — src: docs/deploy/aws-ecs.md"""
    pass

def doc__4_create_rds_postgres_instance():
    """H2: 4. Create RDS Postgres Instance — src: docs/deploy/aws-ecs.md"""
    pass

def doc_custom_vpcs_don_t_come_with_a_default_db_subnet_group_create_one():
    """H1: Custom VPCs don't come with a default DB subnet group — create one — src: docs/deploy/aws-ecs.md"""
    pass

def doc_that_spans_our_two_subnets_so_rds_can_place_the_instance():
    """H1: that spans our two subnets so RDS can place the instance. — src: docs/deploy/aws-ecs.md"""
    pass

def doc_wait_for_it_to_become_available_takes_5_10_min():
    """H1: Wait for it to become available (takes 5-10 min) — src: docs/deploy/aws-ecs.md"""
    pass

def doc_get_the_endpoint():
    """H1: Get the endpoint — src: docs/deploy/aws-ecs.md"""
    pass

def doc__5_create_efs_filesystem():
    """H2: 5. Create EFS Filesystem — src: docs/deploy/aws-ecs.md"""
    pass

def doc_create_mount_targets_in_each_subnet():
    """H1: Create mount targets in each subnet — src: docs/deploy/aws-ecs.md"""
    pass

def doc_wait_for_mount_targets():
    """H1: Wait for mount targets — src: docs/deploy/aws-ecs.md"""
    pass

def doc__6_store_secrets():
    """H2: 6. Store Secrets — src: docs/deploy/aws-ecs.md"""
    pass

def doc__7_iam_roles():
    """H2: 7. IAM Roles — src: docs/deploy/aws-ecs.md"""
    pass

def doc_task_execution_role():
    """H1: Task execution role — src: docs/deploy/aws-ecs.md"""
    pass

def doc_allow_reading_secrets():
    """H1: Allow reading secrets — src: docs/deploy/aws-ecs.md"""
    pass

def doc_task_role_application_add_permissions_as_needed():
    """H1: Task role (application — add permissions as needed) — src: docs/deploy/aws-ecs.md"""
    pass

def doc__8_ecs_cluster_and_task_definition():
    """H2: 8. ECS Cluster and Task Definition — src: docs/deploy/aws-ecs.md"""
    pass

def doc__9_alb_and_tls_certificate():
    """H2: 9. ALB and TLS Certificate — src: docs/deploy/aws-ecs.md"""
    pass

def doc_get_the_cname_record_to_add_to_your_dns():
    """H1: Get the CNAME record to add to your DNS — src: docs/deploy/aws-ecs.md"""
    pass

def doc_target_group():
    """H1: Target group — src: docs/deploy/aws-ecs.md"""
    pass

def doc_https_listener():
    """H1: HTTPS listener — src: docs/deploy/aws-ecs.md"""
    pass

def doc_http_listener_redirect_all_80_traffic_to_443():
    """H1: HTTP listener — redirect all :80 traffic to :443 — src: docs/deploy/aws-ecs.md"""
    pass

def doc__10_create_ecs_service():
    """H2: 10. Create ECS Service — src: docs/deploy/aws-ecs.md"""
    pass

def doc__11_verify_deployment():
    """H2: 11. Verify Deployment — src: docs/deploy/aws-ecs.md"""
    pass

def doc_watch_task_come_up():
    """H1: Watch task come up — src: docs/deploy/aws-ecs.md"""
    pass

def doc_check_task_health():
    """H1: Check task health — src: docs/deploy/aws-ecs.md"""
    pass

def doc_check_logs():
    """H1: Check logs — src: docs/deploy/aws-ecs.md"""
    pass

def doc_hit_the_health_endpoint():
    """H1: Hit the health endpoint — src: docs/deploy/aws-ecs.md"""
    pass

def doc_post_deploy_security_hardening():
    """H2: Post-Deploy Security Hardening — src: docs/deploy/aws-ecs.md"""
    pass

def doc_disable_public_sign_up_prevents_unauthorized_users_from_creating_accounts():
    """H1: Disable public sign-up (prevents unauthorized users from creating accounts) — src: docs/deploy/aws-ecs.md"""
    pass

def doc_add_to_the_task_definition_environment_section_then_redeploy():
    """H1: Add to the task definition environment section, then redeploy: — src: docs/deploy/aws-ecs.md"""
    pass

def doc_name_paperclip_auth_disable_sign_up_value_true():
    """H1: { "name": "PAPERCLIP_AUTH_DISABLE_SIGN_UP", "value": "true" } — src: docs/deploy/aws-ecs.md"""
    pass

def doc_or_update_via_secrets_manager_task_def_override_then_force_new_deployment():
    """H1: Or update via Secrets Manager / task def override, then force new deployment — src: docs/deploy/aws-ecs.md"""
    pass

def doc_deploying_updates():
    """H2: Deploying Updates — src: docs/deploy/aws-ecs.md"""
    pass

def doc_build_and_push_new_image():
    """H1: Build and push new image — src: docs/deploy/aws-ecs.md"""
    pass

def doc_roll_out():
    """H1: Roll out — src: docs/deploy/aws-ecs.md"""
    pass

def doc_watch_the_deployment():
    """H1: Watch the deployment — src: docs/deploy/aws-ecs.md"""
    pass

def doc_rollback():
    """H2: Rollback — src: docs/deploy/aws-ecs.md"""
    pass

def doc_ecs_automatically_rolls_back_if_the_new_task_fails_health_checks():
    """H1: ECS automatically rolls back if the new task fails health checks — src: docs/deploy/aws-ecs.md"""
    pass

def doc_circuit_breaker_is_enabled_in_the_service_configuration_above():
    """H1: (circuit breaker is enabled in the service configuration above). — src: docs/deploy/aws-ecs.md"""
    pass

def doc_to_force_rollback_manually():
    """H1: To force rollback manually: — src: docs/deploy/aws-ecs.md"""
    pass

def doc__1_find_the_previous_task_definition_revision():
    """H1: 1. Find the previous task definition revision — src: docs/deploy/aws-ecs.md"""
    pass

def doc__2_update_service_to_the_previous_revision():
    """H1: 2. Update service to the previous revision — src: docs/deploy/aws-ecs.md"""
    pass

def doc_scaling_to_zero_cost_savings():
    """H2: Scaling to Zero (Cost Savings) — src: docs/deploy/aws-ecs.md"""
    pass

def doc_stop():
    """H1: Stop — src: docs/deploy/aws-ecs.md"""
    pass

def doc_start():
    """H1: Start — src: docs/deploy/aws-ecs.md"""
    pass

def doc_teardown():
    """H2: Teardown — src: docs/deploy/aws-ecs.md"""
    pass

def doc__1_ecs_service_and_cluster():
    """H1: 1. ECS service and cluster — src: docs/deploy/aws-ecs.md"""
    pass

def doc__2_alb_and_acm_cert():
    """H1: 2. ALB and ACM cert — src: docs/deploy/aws-ecs.md"""
    pass

def doc__3_rds_creates_final_snapshot():
    """H1: 3. RDS (creates final snapshot) — src: docs/deploy/aws-ecs.md"""
    pass

def doc__4_efs_mount_targets_must_be_deleted_first():
    """H1: 4. EFS (mount targets must be deleted first) — src: docs/deploy/aws-ecs.md"""
    pass

def doc_mount_target_deletion_is_async_poll_until_none_remain_before_deleting():
    """H1: Mount-target deletion is async; poll until none remain before deleting — src: docs/deploy/aws-ecs.md"""
    pass

def doc_the_filesystem_otherwise_delete_file_system_fails_with_filesysteminuse():
    """H1: the filesystem, otherwise delete-file-system fails with FileSystemInUse. — src: docs/deploy/aws-ecs.md"""
    pass

def doc__5_secrets():
    """H1: 5. Secrets — src: docs/deploy/aws-ecs.md"""
    pass

def doc__6_security_groups_after_all_dependents_are_gone():
    """H1: 6. Security groups (after all dependents are gone) — src: docs/deploy/aws-ecs.md"""
    pass

def doc__7_ecr():
    """H1: 7. ECR — src: docs/deploy/aws-ecs.md"""
    pass

def doc__8_iam_roles():
    """H1: 8. IAM roles — src: docs/deploy/aws-ecs.md"""
    pass

def doc__9_log_group():
    """H1: 9. Log group — src: docs/deploy/aws-ecs.md"""
    pass

def doc_cost_reference():
    """H2: Cost Reference — src: docs/deploy/aws-ecs.md"""
    pass
