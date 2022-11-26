from collections import defaultdict
from typing import Iterable, Literal

from ..models import BaseModel
from ..sql_db import Cursor

_CONFDELTYPES: dict[str, str]

def existing_tables(cr: Cursor, tablenames: Iterable[str]) -> list[str]: ...
def table_exists(cr: Cursor, tablename: str) -> bool: ...
def table_kind(cr: Cursor, tablename: str) -> str | None: ...

SQL_ORDER_BY_TYPE: defaultdict

def create_model_table(cr: Cursor, tablename: str, comment: str | None = ..., columns: Iterable = ...) -> None: ...
def table_columns(cr: Cursor, tablename: str) -> dict: ...
def column_exists(cr: Cursor, tablename: str, columnname: str) -> int: ...
def create_column(cr: Cursor, tablename: str, columnname: str, columntype: str, comment: str | None = ...) -> None: ...
def rename_column(cr: Cursor, tablename: str, columnname1: str, columnname2: str) -> None: ...
def convert_column(cr: Cursor, tablename: str, columnname: str, columntype: str) -> None: ...
def convert_column_translatable(cr: Cursor, tablename: str, columnname: str, columntype: str) -> None: ...
def _convert_column(cr: Cursor, tablename: str, columnname: str, columntype: str, using: str) -> None: ...
def drop_depending_views(cr: Cursor, table: str, column: str) -> None: ...
def get_depending_views(cr: Cursor, table: str, column: str): ...
def set_not_null(cr: Cursor, tablename: str, columnname: str) -> None: ...
def drop_not_null(cr: Cursor, tablename: str, columnname: str) -> None: ...
def constraint_definition(cr: Cursor, tablename: str, constraintname: str) -> str | None: ...
def add_constraint(cr: Cursor, tablename: str, constraintname: str, definition: str) -> None: ...
def drop_constraint(cr: Cursor, tablename: str, constraintname: str) -> None: ...
def add_foreign_key(cr: Cursor, tablename1: str, columnname1: str, tablename2: str, columnname2: str, ondelete) -> Literal[True]: ...
def get_foreign_keys(cr: Cursor, tablename1: str, columnname1: str, tablename2: str, columnname2: str, ondelete) -> list[str]: ...
def fix_foreign_key(cr: Cursor, tablename1: str, columnname1: str, tablename2: str, columnname2: str, ondelete) -> list[str]: ...
def index_exists(cr: Cursor, indexname: str) -> int: ...
def check_index_exist(cr: Cursor, indexname: str) -> None: ...
def create_index(cr: Cursor, indexname: str, tablename: str, expressions: Iterable[str], method: str = ..., where: str = ...) -> None: ...
def create_unique_index(cr: Cursor, indexname: str, tablename: str, expressions: Iterable[str]) -> None: ...
def drop_index(cr: Cursor, indexname: str, tablename: str) -> None: ...
def drop_view_if_exists(cr: Cursor, viewname: str) -> None: ...
def escape_psql(to_escape: str) -> str: ...
def pg_varchar(size: int = ...) -> str: ...
def reverse_order(order: str) -> str: ...
def increment_fields_skiplock(records: BaseModel, *fields: str) -> bool: ...
def value_to_translated_trigram_pattern(value: str) -> str: ...
def pattern_to_translated_trigram_pattern(pattern: str) -> str: ...
def make_identifier(identifier: str) -> str: ...
def make_index_name(table_name: str, column_name: str) -> str: ...
