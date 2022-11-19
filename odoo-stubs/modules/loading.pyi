from typing import Any, Iterable

from .graph import Graph, Node
from .registry import Registry
from ..sql_db import Cursor
from ..tools.assertion_report import assertion_report

def load_data(cr: Cursor, idref: dict, mode: str, kind: str, package: Node, report: assertion_report) -> bool: ...
def load_demo(cr: Cursor, package: Node, idref: dict, mode: str, report: assertion_report | None = ...) -> bool: ...
def force_demo(cr: Cursor) -> None: ...
def load_module_graph(cr: Cursor, graph: Graph, status: Any | None = ..., perform_checks: Any = ..., skip_modules: list[str] | None = ...,
                      report: assertion_report | None = ..., models_to_check: set[str] | None = ...) -> tuple[list[str], list[str]]: ...
def _check_module_names(cr: Cursor, module_names: Iterable[str]) -> None: ...
def load_marked_modules(cr: Cursor, graph: Graph, states: list[str], force: list[str], progressdict, report: assertion_report,
                        loaded_modules: list[str], perform_checks: Any, models_to_check: set[str] | None = ...) -> list[str]: ...
def load_modules(db: Registry, force_demo: bool = ..., status: Any | None = ..., update_module: Any = ...) -> Registry | None: ...
def reset_modules_state(db_name: str) -> None: ...
