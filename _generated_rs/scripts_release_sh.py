"""SHELL: scripts/release.sh"""

def sh_usage():
    """shell fn usage() — src: scripts/release.sh"""
    pass

def sh_restore_publish_artifacts():
    """shell fn restore_publish_artifacts() — src: scripts/release.sh"""
    pass

def sh_cleanup_release_state():
    """shell fn cleanup_release_state() — src: scripts/release.sh"""
    sh_restore_publish_artifacts()
    pass

def sh_set_cleanup_trap():
    """shell fn set_cleanup_trap() — src: scripts/release.sh"""
    sh_cleanup_release_state()
    pass
