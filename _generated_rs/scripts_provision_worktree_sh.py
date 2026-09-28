"""SHELL: scripts/provision-worktree.sh"""

def sh_base_cli_files_present():
    """shell fn base_cli_files_present() — src: scripts/provision-worktree.sh"""
    pass

def sh_base_cli_healthy():
    """shell fn base_cli_healthy() — src: scripts/provision-worktree.sh"""
    sh_base_cli_files_present()
    pass

def sh_repair_base_workspace_install():
    """shell fn repair_base_workspace_install() — src: scripts/provision-worktree.sh"""
    sh_base_cli_healthy()
    pass

def sh_ensure_base_cli_healthy():
    """shell fn ensure_base_cli_healthy() — src: scripts/provision-worktree.sh"""
    sh_base_cli_files_present()
    sh_base_cli_healthy()
    sh_repair_base_workspace_install()
    pass

def sh_run_isolated_worktree_init():
    """shell fn run_isolated_worktree_init() — src: scripts/provision-worktree.sh"""
    sh_ensure_base_cli_healthy()
    pass

def sh_paperclipai_command_available():
    """shell fn paperclipai_command_available() — src: scripts/provision-worktree.sh"""
    sh_base_cli_files_present()
    pass

def sh_existing_worktree_config_is_usable():
    """shell fn existing_worktree_config_is_usable() — src: scripts/provision-worktree.sh"""
    pass

def sh_write_seed_pending_manifest():
    """shell fn write_seed_pending_manifest() — src: scripts/provision-worktree.sh"""
    pass

def sh_write_fallback_worktree_config():
    """shell fn write_fallback_worktree_config() — src: scripts/provision-worktree.sh"""
    pass

def sh_list_base_node_modules_paths():
    """shell fn list_base_node_modules_paths() — src: scripts/provision-worktree.sh"""
    pass

def sh_compute_pnpm_install_fingerprint():
    """shell fn compute_pnpm_install_fingerprint() — src: scripts/provision-worktree.sh"""
    pass

def sh_restore_moved_symlinks():
    """shell fn restore_moved_symlinks() — src: scripts/provision-worktree.sh"""
    pass

def sh_cleanup_moved_symlinks():
    """shell fn cleanup_moved_symlinks() — src: scripts/provision-worktree.sh"""
    pass

def sh_run_pnpm_install():
    """shell fn run_pnpm_install() — src: scripts/provision-worktree.sh"""
    pass
