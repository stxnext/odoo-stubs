import unittest
import urllib2
from typing import Any

from odoo.api import Environment
from odoo.modules.registry import Registry
from odoo.sql_db import Cursor

_logger: Any
ADDONS_PATH: Any
HOST: str
PORT: Any
ADMIN_USER_ID: Any

def get_db_name(): ...

DB: Any

def at_install(flag): ...
def post_install(flag): ...

class BaseCase(unittest.TestCase):
    longMessage: bool
    env: Environment
    registry: Registry
    def cursor(self) -> Cursor: ...
    def ref(self, xid): ...
    def browse_ref(self, xid): ...
    def _assertRaises(self, exception) -> None: ...
    def assertRaises(self, exception, func: Any | None = ..., *args, **kwargs): ...
    def shortDescription(self): ...

class TransactionCase(BaseCase):
    registry: Registry
    cr: Cursor
    uid: int
    env: Environment
    def setUp(self): ...
    def patch(self, obj, key, val) -> None: ...
    def patch_order(self, model, order) -> None: ...

class SingleTransactionCase(BaseCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...

savepoint_seq: Any

class SavepointCase(SingleTransactionCase):
    _savepoint_id: Any
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...

class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_response(self, request, response): ...
    https_response: Any

class HttpCase(TransactionCase):
    xmlrpc_url: Any
    xmlrpc_common: Any
    xmlrpc_db: Any
    xmlrpc_object: Any
    def __init__(self, methodName: str = ...) -> None: ...
    session: Any
    session_id: Any
    opener: Any
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def url_open(self, url, data: Any | None = ..., timeout: int = ...): ...
    def authenticate(self, user, password) -> None: ...
    def phantom_poll(self, phantom, timeout): ...
    def phantom_run(self, cmd, timeout) -> None: ...
    def _wait_remaining_requests(self) -> None: ...
    def phantom_js(self, url_path, code, ready: str = ..., login: Any | None = ..., timeout: int = ..., **kw) -> None: ...

def can_import(module): ...
