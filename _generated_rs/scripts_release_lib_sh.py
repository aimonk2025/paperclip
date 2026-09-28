"""SHELL: scripts/release-lib.sh"""

def sh_release_info():
    """shell fn release_info() — src: scripts/release-lib.sh"""
    pass

def sh_release_warn():
    """shell fn release_warn() — src: scripts/release-lib.sh"""
    pass

def sh_release_fail():
    """shell fn release_fail() — src: scripts/release-lib.sh"""
    pass

def sh_git_remote_exists():
    """shell fn git_remote_exists() — src: scripts/release-lib.sh"""
    pass

def sh_github_repo_from_remote():
    """shell fn github_repo_from_remote() — src: scripts/release-lib.sh"""
    pass

def sh_resolve_release_remote():
    """shell fn resolve_release_remote() — src: scripts/release-lib.sh"""
    sh_release_fail()
    sh_git_remote_exists()
    pass

def sh_fetch_release_remote():
    """shell fn fetch_release_remote() — src: scripts/release-lib.sh"""
    pass

def sh_git_current_branch():
    """shell fn git_current_branch() — src: scripts/release-lib.sh"""
    pass

def sh_git_local_tag_exists():
    """shell fn git_local_tag_exists() — src: scripts/release-lib.sh"""
    pass

def sh_git_remote_tag_exists():
    """shell fn git_remote_tag_exists() — src: scripts/release-lib.sh"""
    pass

def sh_get_last_stable_tag():
    """shell fn get_last_stable_tag() — src: scripts/release-lib.sh"""
    pass

def sh_get_current_stable_version():
    """shell fn get_current_stable_version() — src: scripts/release-lib.sh"""
    sh_get_last_stable_tag()
    pass

def sh_stable_version_slot_for_date():
    """shell fn stable_version_slot_for_date() — src: scripts/release-lib.sh"""
    pass

def sh_utc_date_iso():
    """shell fn utc_date_iso() — src: scripts/release-lib.sh"""
    pass

def sh_next_stable_version():
    """shell fn next_stable_version() — src: scripts/release-lib.sh"""
    pass

def sh_require_prerelease_channel():
    """shell fn require_prerelease_channel() — src: scripts/release-lib.sh"""
    sh_release_fail()
    pass

def sh_next_prerelease_version():
    """shell fn next_prerelease_version() — src: scripts/release-lib.sh"""
    sh_require_prerelease_channel()
    pass

def sh_next_canary_version():
    """shell fn next_canary_version() — src: scripts/release-lib.sh"""
    sh_next_prerelease_version()
    pass

def sh_release_notes_file():
    """shell fn release_notes_file() — src: scripts/release-lib.sh"""
    pass

def sh_stable_tag_name():
    """shell fn stable_tag_name() — src: scripts/release-lib.sh"""
    pass

def sh_prerelease_tag_name():
    """shell fn prerelease_tag_name() — src: scripts/release-lib.sh"""
    sh_require_prerelease_channel()
    pass

def sh_canary_tag_name():
    """shell fn canary_tag_name() — src: scripts/release-lib.sh"""
    sh_prerelease_tag_name()
    pass

def sh_npm_package_version_exists():
    """shell fn npm_package_version_exists() — src: scripts/release-lib.sh"""
    pass

def sh_wait_for_npm_package_version():
    """shell fn wait_for_npm_package_version() — src: scripts/release-lib.sh"""
    sh_npm_package_version_exists()
    pass

def sh_is_npm_tlog_duplicate_error():
    """shell fn is_npm_tlog_duplicate_error() — src: scripts/release-lib.sh"""
    pass

def sh_package_publish_tool():
    """shell fn package_publish_tool() — src: scripts/release-lib.sh"""
    pass

def sh_run_bundled_npm_pack():
    """shell fn run_bundled_npm_pack() — src: scripts/release-lib.sh"""
    pass

def sh_run_bundled_npm_publish():
    """shell fn run_bundled_npm_publish() — src: scripts/release-lib.sh"""
    pass

def sh_run_package_publish():
    """shell fn run_package_publish() — src: scripts/release-lib.sh"""
    sh_run_bundled_npm_publish()
    pass

def sh_publish_package_to_npm():
    """shell fn publish_package_to_npm() — src: scripts/release-lib.sh"""
    sh_release_warn()
    sh_npm_package_version_exists()
    sh_is_npm_tlog_duplicate_error()
    sh_run_package_publish()
    pass

def sh_publish_package_to_npm_and_wait():
    """shell fn publish_package_to_npm_and_wait() — src: scripts/release-lib.sh"""
    sh_release_warn()
    sh_wait_for_npm_package_version()
    sh_publish_package_to_npm()
    pass

def sh_verify_npm_installable():
    """shell fn verify_npm_installable() — src: scripts/release-lib.sh"""
    pass

def sh_wait_for_release_registry_state():
    """shell fn wait_for_release_registry_state() — src: scripts/release-lib.sh"""
    sh_release_warn()
    pass

def sh_require_clean_worktree():
    """shell fn require_clean_worktree() — src: scripts/release-lib.sh"""
    sh_release_fail()
    pass

def sh_require_on_master_branch():
    """shell fn require_on_master_branch() — src: scripts/release-lib.sh"""
    sh_release_fail()
    sh_git_current_branch()
    pass

def sh_require_channel_tag_at_head():
    """shell fn require_channel_tag_at_head() — src: scripts/release-lib.sh"""
    sh_release_fail()
    sh_require_prerelease_channel()
    pass

def sh_require_channel_tag_absent_at_head():
    """shell fn require_channel_tag_absent_at_head() — src: scripts/release-lib.sh"""
    sh_release_fail()
    sh_require_prerelease_channel()
    pass

def sh_require_npm_publish_auth():
    """shell fn require_npm_publish_auth() — src: scripts/release-lib.sh"""
    sh_release_info()
    sh_release_fail()
    pass

def sh_list_public_package_info():
    """shell fn list_public_package_info() — src: scripts/release-lib.sh"""
    pass

def sh_set_public_package_version():
    """shell fn set_public_package_version() — src: scripts/release-lib.sh"""
    pass
