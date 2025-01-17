from collections import defaultdict
from typing import Any, Callable, Collection, Generator, Iterable, Iterator, KeysView, Literal, Mapping, Optional, Sequence, TypeVar, Union
from weakref import WeakSet

from .fields import Field
from .models import BaseModel
from .modules.registry import Registry
from .sql_db import Cursor
from .tools import OrderedSet, frozendict, StackMap

_T = TypeVar('_T')
_ModelT = TypeVar('_ModelT', bound=BaseModel)
_CallableT = TypeVar('_CallableT', bound=Callable)

INHERITED_ATTRS: tuple[str, ...]

class Params:
    args: tuple
    kwargs: dict
    def __init__(self, args: tuple, kwargs: dict) -> None: ...
    def __str__(self) -> str: ...

class Meta(type):
    def __new__(meta, name: str, bases: tuple, attrs: dict): ...

def attrsetter(attr, value) -> Callable[[_T], _T]: ...
def propagate(method1: Callable, method2: _CallableT) -> _CallableT: ...
def constrains(*args: str | Callable[[_ModelT], Sequence[str]]) -> Callable[[_T], _T]: ...
def ondelete(*, at_uninstall: bool) -> Callable[[_T], _T]: ...
def onchange(*args: str) -> Callable[[_T], _T]: ...
def depends(*args: str | Callable[[_ModelT], Sequence[str]]) -> Callable[[_T], _T]: ...
def depends_context(*args: str) -> Callable[[_T], _T]: ...
def returns(model: str | None, downgrade: Callable | None = ..., upgrade: Callable | None = ...) -> Callable[[_T], _T]: ...
def downgrade(method: Callable, value, self, args, kwargs): ...
def split_context(method: Callable, args, kwargs) -> tuple: ...
def autovacuum(method: _CallableT) -> _CallableT: ...
def model(method: _CallableT) -> _CallableT: ...

def _model_create_single(create: Callable[..., _ModelT], self: _ModelT, arg) -> _ModelT: ...
def model_create_single(method: _CallableT) -> _CallableT: ...
def _model_create_multi(create: Callable[..., _ModelT], self: _ModelT, arg) -> _ModelT: ...
def model_create_multi(method: _CallableT) -> _CallableT: ...
def _call_kw_model(method: Callable[..., _ModelT], self: _ModelT, args, kwargs): ...
def _call_kw_model_create(method: Callable[..., _ModelT], self: _ModelT, args, kwargs) -> list[int] | int | Literal[False]: ...
def _call_kw_multi(method: Callable[..., _ModelT], self: _ModelT, args, kwargs): ...
def call_kw(model: BaseModel, name: str, args, kwargs): ...

class Environment(Mapping[str, BaseModel]):
    cr: Cursor = ...
    uid: int = ...
    context: dict[str, Any] = ...
    su: bool = ...
    envs: None
    args: tuple[Cursor, int, dict, bool]
    @classmethod
    def manage(cls) -> Generator[None, None, None]: ...
    def reset(self) -> None: ...
    all: Transaction
    transaction: Transaction
    registry: Registry
    cache: Cache
    _cache_key: dict[Field, Any]
    _protected: StackMap[Field, set[int]]
    def __new__(cls, cr: Cursor, uid: int | None, context: dict, su: bool = ...) -> Environment: ...
    def __contains__(self, model_name: str) -> bool: ...
    def __getitem__(self, model_name: str) -> BaseModel: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __call__(self, cr: Cursor | None = ..., user: Union['odoo.model.res_users', int, None] = ..., context: dict | None = ..., su: bool | None = ...) -> Environment: ...
    def ref(self, xml_id: str, raise_if_not_found: bool = ...) -> Optional[BaseModel]: ...
    def is_superuser(self) -> bool: ...
    def is_admin(self) -> bool: ...
    def is_system(self) -> bool: ...
    @property
    def user(self) -> 'odoo.model.res_users': ...
    @property
    def company(self) -> 'odoo.model.res_company': ...
    @property
    def companies(self) -> 'odoo.model.res_company': ...
    @property
    def lang(self) -> str: ...
    def clear(self) -> None: ...
    def clear_upon_failure(self): ...
    def invalidate_all(self, flush: bool = ...) -> None: ...
    def _recompute_all(self) -> None: ...
    def flush_all(self) -> None: ...
    def is_protected(self, field: Field, record: BaseModel) -> bool: ...
    def protected(self, field: Field) -> BaseModel: ...
    def protecting(self, what, records: Optional[BaseModel] = ...) -> Generator[None, None, None]: ...
    def fields_to_compute(self) -> KeysView[Field]: ...
    def records_to_compute(self, field: Field) -> BaseModel: ...
    def is_to_compute(self, field: Field, record: BaseModel) -> bool: ...
    def not_to_compute(self, field: Field, records: _ModelT) -> _ModelT: ...
    def add_to_compute(self, field: Field, records: BaseModel): ...
    def remove_to_compute(self, field: Field, records: BaseModel) -> None: ...
    def norecompute(self) -> Generator[None, None, None]: ...
    def cache_key(self, field: Field): ...

class Transaction:
    registry: Registry
    envs: WeakSet[Environment]
    cache: Cache
    protected: StackMap[Field, set[int]]
    tocompute: defaultdict[Field, set[int]]
    def __init__(self, registry: Registry) -> None: ...
    def flush(self) -> None: ...
    def clear(self) -> None: ...
    def reset(self) -> None: ...

NOTHING: object
EMPTY_DICT: frozendict

class Cache:
    _data: defaultdict[Field, dict]
    _dirty: defaultdict[Field, OrderedSet[int]]
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def _get_field_cache(self, model: BaseModel, field: Field) -> dict: ...
    def _set_field_cache(self, model: BaseModel, field: Field): ...
    def contains(self, record: BaseModel, field: Field) -> bool: ...
    def contains_field(self, field: Field) -> bool: ...
    def get(self, record: BaseModel, field: Field, default=...): ...
    def set(self, record: BaseModel, field: Field, value, dirty: bool = ..., check_dirty: bool = ...) -> None: ...
    def update(self, records: BaseModel, field: Field, values, dirty: bool = ..., check_dirty: bool = ...) -> None: ...
    def update_raw(self, records: BaseModel, field: Field, values, dirty: bool = ..., check_dirty: bool = ...) -> None: ...
    def insert_missing(self, records: BaseModel, field: Field, values) -> None: ...
    def remove(self, record: BaseModel, field: Field) -> None: ...
    def get_values(self, records: BaseModel, field: Field) -> Iterator: ...
    def get_until_miss(self, records: BaseModel, field: Field) -> list: ...
    def get_records_different_from(self, records: _ModelT, field: Field, value) -> _ModelT: ...
    def get_fields(self, record: BaseModel) -> Iterator[Field]: ...
    def get_records(self, model: _ModelT, field: Field) -> _ModelT: ...
    def get_missing_ids(self, records: BaseModel, field: Field) -> Iterator[int]: ...
    def get_dirty_fields(self) -> 'set[Field]': ...
    def get_dirty_records(self, model: _ModelT, field: Field) -> _ModelT: ...
    def has_dirty_fields(self, records: BaseModel, fields: Iterable[Field] | None = ...) -> bool: ...
    def clear_dirty_field(self, field: Field) -> Collection[int]: ...
    def invalidate(self, spec: list[tuple[Field, Iterable | None]] | None = ...) -> None: ...
    def clear(self) -> None: ...
    def check(self, env: Environment) -> None: ...

class Starred:
    __slots__ = ['value']
    value: Any
    def __init__(self, value) -> None: ...
    def __repr__(self) -> str: ...
