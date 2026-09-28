"""SHELL: scripts/smoke/hermes-gateway-join.sh"""

def sh_log():
    """shell fn log() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_warn():
    """shell fn warn() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_fail():
    """shell fn fail() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_require_cmd():
    """shell fn require_cmd() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_fail()
    pass

def sh_print_usage():
    """shell fn print_usage() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_hash_prefix():
    """shell fn hash_prefix() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_redact_text():
    """shell fn redact_text() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_print_response_error():
    """shell fn print_response_error() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_redact_text()
    pass

def sh_api_request():
    """shell fn api_request() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_assert_status():
    """shell fn assert_status() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_fail()
    sh_print_response_error()
    pass

def sh_assert_json_has_string():
    """shell fn assert_json_has_string() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_fail()
    sh_print_response_error()
    pass

def sh_fail_board_auth_required():
    """shell fn fail_board_auth_required() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_print_response_error()
    pass

def sh_is_remote_plain_http():
    """shell fn is_remote_plain_http() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_url_host()
    sh_is_loopback_http_host()
    pass

def sh_url_host():
    """shell fn url_host() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_is_loopback_http_host():
    """shell fn is_loopback_http_host() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_strip_trailing_slash():
    """shell fn strip_trailing_slash() — src: scripts/smoke/hermes-gateway-join.sh"""
    pass

def sh_resolve_company_id():
    """shell fn resolve_company_id() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_log()
    sh_fail()
    sh_api_request()
    sh_assert_status()
    sh_fail_board_auth_required()
    pass

def sh_assert_onboarding_contains():
    """shell fn assert_onboarding_contains() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_fail()
    pass

def sh_probe_hermes_gateway():
    """shell fn probe_hermes_gateway() — src: scripts/smoke/hermes-gateway-join.sh"""
    sh_log()
    sh_fail()
    sh_hash_prefix()
    sh_is_remote_plain_http()
    pass
