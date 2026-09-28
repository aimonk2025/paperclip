"""SHELL: scripts/kill-dev.sh"""

def sh_is_pid_running():
    """shell fn is_pid_running() — src: scripts/kill-dev.sh"""
    pass

def sh_read_pidfile_pid():
    """shell fn read_pidfile_pid() — src: scripts/kill-dev.sh"""
    pass

def sh_command_for_pid():
    """shell fn command_for_pid() — src: scripts/kill-dev.sh"""
    pass

def sh_append_postgres_from_pidfile():
    """shell fn append_postgres_from_pidfile() — src: scripts/kill-dev.sh"""
    sh_is_pid_running()
    sh_read_pidfile_pid()
    sh_command_for_pid()
    pass

def sh_wait_for_pid_exit():
    """shell fn wait_for_pid_exit() — src: scripts/kill-dev.sh"""
    sh_is_pid_running()
    pass
