"""SHELL: scripts/provision-worktree-runtime.sh"""

def sh_base_cli_files_present():
    """shell fn base_cli_files_present() — src: scripts/provision-worktree-runtime.sh"""
    pass

def sh_base_cli_healthy():
    """shell fn base_cli_healthy() — src: scripts/provision-worktree-runtime.sh"""
    sh_base_cli_files_present()
    pass

def sh_repair_base_workspace_install():
    """shell fn repair_base_workspace_install() — src: scripts/provision-worktree-runtime.sh"""
    sh_base_cli_healthy()
    pass

def sh_ensure_base_cli_healthy():
    """shell fn ensure_base_cli_healthy() — src: scripts/provision-worktree-runtime.sh"""
    sh_base_cli_files_present()
    sh_base_cli_healthy()
    sh_repair_base_workspace_install()
    pass

def sh_run_ensure_seeded():
    """shell fn run_ensure_seeded() — src: scripts/provision-worktree-runtime.sh"""
    sh_ensure_base_cli_healthy()
    pass
