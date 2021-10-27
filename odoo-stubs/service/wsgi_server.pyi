from typing import Any

_logger: Any
RPC_FAULT_CODE_CLIENT_ERROR: int
RPC_FAULT_CODE_APPLICATION_ERROR: int
RPC_FAULT_CODE_WARNING: int
RPC_FAULT_CODE_ACCESS_DENIED: int
RPC_FAULT_CODE_ACCESS_ERROR: int

def xmlrpc_return(start_response, service, method, params, string_faultcode: bool = ...): ...
def xmlrpc_handle_exception_int(e): ...
def xmlrpc_handle_exception_string(e): ...
def wsgi_xmlrpc(environ, start_response): ...
def application_unproxied(environ, start_response): ...
def application(environ, start_response): ...
