import datetime
from typing import Any

DATE_LENGTH: Any
DATETIME_LENGTH: Any
EMPTY_DICT: Any
RENAMED_ATTRS: Any
_logger: Any
_schema: Any
Default: Any

class SpecialValue:
    value: Any
    def __init__(self, value) -> None: ...
    def get(self): ...

class FailedValue(SpecialValue):
    exception: Any
    def __init__(self, exception) -> None: ...
    def get(self) -> None: ...

def _check_value(value): ...
def copy_cache(records, env) -> None: ...
def first(records): ...
def resolve_mro(model, name, predicate): ...

class MetaField(type):
    by_type: Any
    def __new__(meta, name, bases, attrs): ...
    def __init__(cls, name, bases, attrs) -> None: ...

class Field:
    __metaclass__: MetaField
    type: Any
    relational: bool
    translate: bool
    column_type: Any
    column_format: str
    _slots: Any
    args: Any
    _setup_done: Any
    def __init__(self, string=..., **kwargs) -> None: ...
    def new(self, **kwargs): ...
    def __getattr__(self, name): ...
    _attrs: Any
    def __setattr__(self, name, value) -> None: ...
    def set_all_attrs(self, attrs) -> None: ...
    def __delattr__(self, name) -> None: ...
    def __str__(self): ...
    def __repr__(self): ...
    def setup_base(self, model, name) -> None: ...
    def _can_setup_from(self, field): ...
    prefetch: bool
    string: Any
    default: Any
    def _setup_attrs(self, model, name): ...
    def setup_full(self, model) -> None: ...
    depends: Any
    def _setup_regular_base(self, model): ...
    def _setup_regular_full(self, model) -> None: ...
    related: Any
    related_field: Any
    compute: Any
    inverse: Any
    search: Any
    states: Any
    required: bool
    def _setup_related_full(self, model) -> None: ...
    def traverse_related(self, record): ...
    def _compute_related(self, records) -> None: ...
    def _inverse_related(self, records) -> None: ...
    def _search_related(self, records, operator, value): ...
    _related_comodel_name: Any
    _related_string: Any
    _related_help: Any
    _related_readonly: Any
    _related_groups: Any
    _related_group_operator: Any
    @property
    def base_field(self): ...
    def _default_company_dependent(self, model): ...
    def _compute_company_dependent(self, records) -> None: ...
    def _inverse_company_dependent(self, records) -> None: ...
    def _search_company_dependent(self, records, operator, value): ...
    def _compute_sparse(self, records) -> None: ...
    def _inverse_sparse(self, records) -> None: ...
    def resolve_deps(self, model, path0=..., seen=...): ...
    recursive: bool
    def setup_triggers(self, model) -> None: ...
    def get_description(self, env): ...
    _description_store: Any
    _description_manual: Any
    _description_depends: Any
    _description_related: Any
    _description_company_dependent: Any
    _description_readonly: Any
    _description_required: Any
    _description_states: Any
    _description_groups: Any
    _description_change_default: Any
    _description_deprecated: Any
    @property
    def _description_searchable(self): ...
    @property
    def _description_sortable(self): ...
    def _description_string(self, env): ...
    def _description_help(self, env): ...
    def null(self, record): ...
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_record(self, value, record): ...
    def convert_to_read(self, value, record, use_name_get: bool = ...): ...
    def convert_to_write(self, value, record): ...
    def convert_to_onchange(self, value, record, fnames=...): ...
    def convert_to_export(self, value, record): ...
    def convert_to_display_name(self, value, record): ...
    def check_schema(self, model) -> None: ...
    def read(self, records): ...
    def write(self, records, value): ...
    # def __get__(self, record, owner): ...
    def __set__(self, record, value) -> None: ...
    def _compute_value(self, records) -> None: ...
    def compute_value(self, records) -> None: ...
    def determine_value(self, record) -> None: ...
    def determine_draft_value(self, record) -> None: ...
    def determine_inverse(self, records) -> None: ...
    def determine_domain(self, records, operator, value): ...
    def modified(self, records): ...
    def modified_draft(self, records): ...

class Boolean(Field):
    type: str
    column_type: Any
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_export(self, value, record): ...

class Integer(Field):
    type: str
    column_type: Any
    _slots: Any
    _description_group_operator: Any
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_read(self, value, record, use_name_get: bool = ...): ...
    def _update(self, records, value) -> None: ...
    def convert_to_export(self, value, record): ...

class Float(Field):
    type: str
    _slots: Any
    def __init__(self, string=..., digits=..., **kwargs) -> None: ...
    @property
    def column_type(self): ...
    @property
    def digits(self): ...
    _related__digits: Any
    _description_digits: Any
    _description_group_operator: Any
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_export(self, value, record): ...

class Monetary(Field):
    type: str
    column_type: Any
    _slots: Any
    def __init__(self, string=..., currency_field=..., **kwargs) -> None: ...
    _related_currency_field: Any
    _description_currency_field: Any
    _description_group_operator: Any
    currency_field: str
    def _setup_regular_full(self, model) -> None: ...
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_read(self, value, record, use_name_get: bool = ...): ...
    def convert_to_write(self, value, record): ...

class _String(Field):
    _slots: Any
    def __init__(self, string=..., **kwargs) -> None: ...
    _related_translate: Any
    def _description_translate(self, env): ...
    def get_trans_terms(self, value): ...
    def get_trans_func(self, records): ...
    def check_trans_value(self, value): ...

class Char(_String):
    type: str
    _slots: Any
    @property
    def column_type(self): ...
    _related_size: Any
    _description_size: Any
    def _setup_regular_base(self, model) -> None: ...
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...

class Text(_String):
    type: str
    column_type: Any
    def convert_to_cache(self, value, record, validate: bool = ...): ...

class Html(_String):
    type: str
    column_type: Any
    _slots: Any
    translate: Any
    def _setup_attrs(self, model, name) -> None: ...
    _related_sanitize: Any
    _related_sanitize_tags: Any
    _related_sanitize_attributes: Any
    _related_sanitize_style: Any
    _related_strip_style: Any
    _related_strip_classes: Any
    _description_sanitize: Any
    _description_sanitize_tags: Any
    _description_sanitize_attributes: Any
    _description_sanitize_style: Any
    _description_strip_style: Any
    _description_strip_classes: Any
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...

class Date(Field):
    type: str
    column_type: Any
    @staticmethod
    def today(*args) -> str: ...
    @staticmethod
    def context_today(record, timestamp: Any | None = ...) -> str: ...
    @staticmethod
    def from_string(value) -> datetime.date: ...
    @staticmethod
    def to_string(value) -> str: ...
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_export(self, value, record): ...

class Datetime(Field):
    type: str
    column_type: Any
    @staticmethod
    def now(*args) -> str: ...
    @staticmethod
    def context_timestamp(record, timestamp): ...
    @staticmethod
    def from_string(value) -> datetime.datetime: ...
    @staticmethod
    def to_string(value) -> str: ...
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_export(self, value, record): ...
    def convert_to_display_name(self, value, record): ...

class Binary(Field):
    type: str
    _slots: Any
    @property
    def column_type(self): ...
    _description_attachment: Any
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def read(self, records) -> None: ...
    def write(self, records, value) -> None: ...

class Selection(Field):
    type: str
    _slots: Any
    def __init__(self, selection=..., string=..., **kwargs) -> None: ...
    @property
    def column_type(self): ...
    def _setup_regular_base(self, model) -> None: ...
    selection: Any
    def _setup_related_full(self, model): ...
    def _setup_attrs(self, model, name) -> None: ...
    def _description_selection(self, env): ...
    def get_values(self, env): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_export(self, value, record): ...
    def convert_to_column(self, value, record): ...

class Reference(Selection):
    type: str
    @property
    def column_type(self): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_record(self, value, record): ...
    def convert_to_read(self, value, record, use_name_get: bool = ...): ...
    def convert_to_export(self, value, record): ...
    def convert_to_display_name(self, value, record): ...

class _Relational(Field):
    relational: bool
    _slots: Any
    comodel_name: str
    def _setup_regular_base(self, model) -> None: ...
    @property
    def _related_domain(self): ...
    _related_context: Any
    _description_relation: Any
    _description_context: Any
    def _description_domain(self, env): ...
    def null(self, record): ...
    def modified(self, records): ...

class Many2one(_Relational):
    type: str
    column_type: Any
    _slots: Any
    def __init__(self, comodel_name=..., string=..., **kwargs) -> None: ...
    delegate: Any
    def _setup_attrs(self, model, name) -> None: ...
    def _update(self, records, value) -> None: ...
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_record(self, value, record): ...
    def convert_to_read(self, value, record, use_name_get: bool = ...): ...
    def convert_to_write(self, value, record): ...
    def convert_to_export(self, value, record): ...
    def convert_to_display_name(self, value, record): ...
    def convert_to_onchange(self, value, record, fnames=...): ...

class UnionUpdate(SpecialValue):
    args: Any
    def __init__(self, field, record, value) -> None: ...
    def get(self): ...

class _RelationalMulti(_Relational):
    def _update(self, records, value) -> None: ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...
    def convert_to_record(self, value, record): ...
    def convert_to_read(self, value, record, use_name_get: bool = ...): ...
    def convert_to_write(self, value, record): ...
    def convert_to_onchange(self, value, record, fnames=...): ...
    def convert_to_export(self, value, record): ...
    def convert_to_display_name(self, value, record) -> None: ...
    def _compute_related(self, records): ...
    def _setup_regular_base(self, model) -> None: ...

class One2many(_RelationalMulti):
    type: str
    _slots: Any
    def __init__(self, comodel_name=..., inverse_name=..., string=..., **kwargs) -> None: ...
    def _setup_regular_full(self, model) -> None: ...
    _description_relation_field: Any
    def convert_to_onchange(self, value, record, fnames=...): ...
    def check_schema(self, model) -> None: ...
    def read(self, records) -> None: ...
    def write(self, records, value) -> None: ...

class Many2many(_RelationalMulti):
    type: str
    _slots: Any
    def __init__(self, comodel_name=..., relation=..., column1=..., column2=..., string=..., **kwargs) -> None: ...
    relation: Any
    column1: Any
    column2: Any
    def _setup_regular_base(self, model) -> None: ...
    def _setup_regular_full(self, model) -> None: ...
    def check_schema(self, model): ...
    def read(self, records) -> None: ...
    def write(self, records, value): ...

class Serialized(Field):
    type: str
    _slots: Any
    column_type: Any
    def convert_to_column(self, value, record): ...
    def convert_to_cache(self, value, record, validate: bool = ...): ...

class Id(Field):
    type: str
    column_type: Any
    _slots: Any
    def __get__(self, record, owner): ...
    def __set__(self, record, value) -> None: ...
