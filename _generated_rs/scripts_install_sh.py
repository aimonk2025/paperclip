"""SHELL: scripts/install.sh"""

def sh_usage():
    """shell fn usage() — src: scripts/install.sh"""
    pass

def sh_log():
    """shell fn log() — src: scripts/install.sh"""
    pass

def sh_fail():
    """shell fn fail() — src: scripts/install.sh"""
    pass

def sh_parse_bool():
    """shell fn parse_bool() — src: scripts/install.sh"""
    sh_fail()
    pass

def sh_require_value():
    """shell fn require_value() — src: scripts/install.sh"""
    sh_fail()
    pass

def sh_cleanup():
    """shell fn cleanup() — src: scripts/install.sh"""
    pass

def sh_node_major():
    """shell fn node_major() — src: scripts/install.sh"""
    pass

def sh_has_supported_node():
    """shell fn has_supported_node() — src: scripts/install.sh"""
    sh_node_major()
    pass

def sh_print_command():
    """shell fn print_command() — src: scripts/install.sh"""
    pass

def sh_confirm_command():
    """shell fn confirm_command() — src: scripts/install.sh"""
    sh_fail()
    sh_print_command()
    pass

def sh_run_command():
    """shell fn run_command() — src: scripts/install.sh"""
    sh_confirm_command()
    pass

def sh_run_privileged():
    """shell fn run_privileged() — src: scripts/install.sh"""
    sh_fail()
    sh_run_command()
    pass

def sh_ensure_temp_dir():
    """shell fn ensure_temp_dir() — src: scripts/install.sh"""
    pass

def sh_download_checked_script():
    """shell fn download_checked_script() — src: scripts/install.sh"""
    sh_fail()
    pass

def sh_check_version_manager():
    """shell fn check_version_manager() — src: scripts/install.sh"""
    sh_fail()
    pass

def sh_install_node_macos():
    """shell fn install_node_macos() — src: scripts/install.sh"""
    sh_log()
    sh_fail()
    sh_run_command()
    sh_ensure_temp_dir()
    sh_download_checked_script()
    pass

def sh_install_node_apt():
    """shell fn install_node_apt() — src: scripts/install.sh"""
    sh_run_privileged()
    sh_ensure_temp_dir()
    sh_download_checked_script()
    pass

def sh_install_node_dnf():
    """shell fn install_node_dnf() — src: scripts/install.sh"""
    sh_run_privileged()
    sh_ensure_temp_dir()
    sh_download_checked_script()
    pass

def sh_install_node_linux():
    """shell fn install_node_linux() — src: scripts/install.sh"""
    sh_fail()
    sh_run_privileged()
    sh_install_node_apt()
    sh_install_node_dnf()
    pass
