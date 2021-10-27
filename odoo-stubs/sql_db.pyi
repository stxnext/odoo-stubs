import psycopg2.extensions
from typing import Any

_logger: Any
types_mapping: Any

def unbuffer(symb, cr): ...
def undecimalize(symb, cr): ...
def adapt_string(adapted): ...

re_from: Any
re_into: Any
sql_counter: int

class Cursor:
    IN_MAX: int
    def check(f): ...
    sql_from_log: Any
    sql_into_log: Any
    sql_log: Any
    sql_log_count: int
    _closed: bool
    __pool: Any
    dbname: Any
    _serialized: Any
    _cnx: Any
    _obj: Any
    __caller: Any
    __closer: bool
    _default_log_exceptions: bool
    cache: Any
    _event_handlers: Any
    def __init__(self, pool, dbname, dsn, serialized: bool = ...) -> None: ...
    def __build_dict(self, row): ...
    def dictfetchone(self): ...
    def dictfetchmany(self, size): ...
    def dictfetchall(self): ...
    def __del__(self) -> None: ...
    def execute(self, query, params: Any | None = ..., log_exceptions: Any | None = ...): ...
    def split_for_in_conditions(self, ids, size: Any | None = ...): ...
    def print_log(self): ...
    def close(self): ...
    def _close(self, leak: bool = ...) -> None: ...
    def autocommit(self, on) -> None: ...
    def after(self, event, func) -> None: ...
    def _pop_event_handlers(self): ...
    def commit(self): ...
    def rollback(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def savepoint(self) -> None: ...
    def __getattr__(self, name): ...
    @property
    def closed(self): ...

class TestCursor(Cursor):
    _lock: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def force_close(self) -> None: ...
    def close(self) -> None: ...
    def autocommit(self, on) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...

class LazyCursor:
    _dbname: Any
    _cursor: Any
    _depth: int
    def __init__(self, dbname: Any | None = ...) -> None: ...
    @property
    def dbname(self): ...
    def __getattr__(self, name): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class PsycoConnection(psycopg2.extensions.connection): ...

class ConnectionPool:
    def locked(fun): ...
    _connections: Any
    _maxconn: Any
    _lock: Any
    def __init__(self, maxconn: int = ...) -> None: ...
    def __repr__(self): ...
    def _debug(self, msg, *args) -> None: ...
    def borrow(self, connection_info): ...
    def give_back(self, connection, keep_in_pool: bool = ...) -> None: ...
    def close_all(self, dsn: Any | None = ...) -> None: ...

class Connection:
    dbname: Any
    dsn: Any
    __pool: Any
    def __init__(self, pool, dbname, dsn) -> None: ...
    def cursor(self, serialized: bool = ...): ...
    def test_cursor(self, serialized: bool = ...): ...
    serialized_cursor: Any
    def __nonzero__(self): ...

def connection_info_for(db_or_uri): ...

_Pool: Any

def db_connect(to, allow_uri: bool = ...): ...
def close_db(db_name) -> None: ...
def close_all() -> None: ...
