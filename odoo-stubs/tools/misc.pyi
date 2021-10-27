from cache import *
import threading
import xlsxwriter
import xlwt
from collections import Mapping, MutableSet, defaultdict
from itertools import repeat as repeat
from odoo.loglevels import exception_to_unicode as exception_to_unicode, get_encodings as get_encodings
from threading import local
from typing import Any

_logger: Any
SKIPPED_ELEMENT_TYPES: Any

def find_in_path(name): ...
def _exec_pipe(prog, args, env: Any | None = ...): ...
def exec_command_pipe(name, *args): ...
def find_pg_tool(name): ...
def exec_pg_environ(): ...
def exec_pg_command(name, *args) -> None: ...
def exec_pg_command_pipe(name, *args): ...
def file_open(name, mode: str = ..., subdir: str = ..., pathinfo: bool = ...): ...
def _fileopen(path, mode, basedir, pathinfo, basename: Any | None = ...): ...
def flatten(list): ...
def reverse_enumerate(l): ...
def partition(pred, elems): ...
def topological_sort(elems): ...

class PatchedWorkbook(xlwt.Workbook):
    def add_sheet(self, name, cell_overwrite_ok: bool = ...): ...

class PatchedXlsxWorkbook(xlsxwriter.Workbook):
    def add_worksheet(self, name: Any | None = ..., **kw): ...

class UpdateableStr(local):
    string: Any
    def __init__(self, string: str = ...) -> None: ...
    def __str__(self): ...
    def __repr__(self): ...
    def __nonzero__(self): ...

class UpdateableDict(local):
    dict: Any
    def __init__(self, dict: Any | None = ...) -> None: ...
    def __str__(self): ...
    def __repr__(self): ...
    def clear(self): ...
    def keys(self): ...
    def __setitem__(self, i, y) -> None: ...
    def __getitem__(self, i): ...
    def copy(self): ...
    def iteritems(self): ...
    def iterkeys(self): ...
    def itervalues(self): ...
    def pop(self, k, d: Any | None = ...): ...
    def popitem(self): ...
    def setdefault(self, k, d: Any | None = ...): ...
    def update(self, E, **F): ...
    def values(self): ...
    def get(self, k, d: Any | None = ...): ...
    def has_key(self, k): ...
    def items(self): ...
    def __cmp__(self, y): ...
    def __contains__(self, k): ...
    def __delitem__(self, y): ...
    def __eq__(self, y): ...
    def __ge__(self, y): ...
    def __gt__(self, y): ...
    def __hash__(self): ...
    def __iter__(self): ...
    def __le__(self, y): ...
    def __len__(self): ...
    def __lt__(self, y): ...
    def __ne__(self, y): ...

def to_xml(s): ...
def get_iso_codes(lang): ...
def scan_languages(): ...
def get_user_companies(cr, user): ...
def mod10r(number): ...
def str2bool(s, default: Any | None = ...): ...
def human_size(sz): ...
def logged(f): ...

class profile:
    fname: Any
    def __init__(self, fname: Any | None = ...) -> None: ...
    def __call__(self, f): ...

def detect_ip_addr(): ...

DEFAULT_SERVER_DATE_FORMAT: str
DEFAULT_SERVER_TIME_FORMAT: str
DEFAULT_SERVER_DATETIME_FORMAT: Any
DATETIME_FORMATS_MAP: Any
POSIX_TO_LDML: Any

def posix_to_ldml(fmt, locale): ...
def split_every(n, iterable, piece_maker=...) -> None: ...

class upload_data_thread(threading.Thread):
    args: Any
    def __init__(self, email, data, type) -> None: ...
    def run(self) -> None: ...

def upload_data(email, data, type: str = ...): ...
def get_and_group_by_field(cr, uid, obj, ids, field, context: Any | None = ...): ...
def get_and_group_by_company(cr, uid, obj, ids, context: Any | None = ...): ...
def resolve_attr(obj, attr): ...
def attrgetter(*items): ...

class unquote(str):
    def __repr__(self): ...

class UnquoteEvalContext(defaultdict):
    def __init__(self, *args, **kwargs) -> None: ...
    def __missing__(self, key): ...

class mute_logger:
    loggers: Any
    def __init__(self, *loggers) -> None: ...
    def filter(self, record): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any | None = ..., exc_val: Any | None = ..., exc_tb: Any | None = ...) -> None: ...
    def __call__(self, func): ...

_ph: Any

class CountingStream:
    stream: Any
    index: Any
    stopped: bool
    def __init__(self, stream, start: int = ...) -> None: ...
    def __iter__(self): ...
    def next(self): ...

def stripped_sys_argv(*strip_args): ...

class ConstantMapping(Mapping):
    __slots__: Any
    _value: Any
    def __init__(self, val) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, item): ...

def dumpstacks(sig: Any | None = ..., frame: Any | None = ...) -> None: ...
def freehash(arg): ...

class frozendict(dict):
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, val) -> None: ...
    def clear(self) -> None: ...
    def pop(self, key, default: Any | None = ...) -> None: ...
    def popitem(self) -> None: ...
    def setdefault(self, key, default: Any | None = ...) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def __hash__(self): ...

class Collector(Mapping):
    __slots__: Any
    _map: Any
    def __init__(self) -> None: ...
    def add(self, key, val) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self): ...

class OrderedSet(MutableSet):
    __slots__: Any
    _map: Any
    def __init__(self, elems=...) -> None: ...
    def __contains__(self, elem): ...
    def __iter__(self): ...
    def __len__(self): ...
    def add(self, elem) -> None: ...
    def discard(self, elem) -> None: ...

class LastOrderedSet(OrderedSet):
    def add(self, elem) -> None: ...

def ignore(*exc) -> None: ...
def html_escape(text): ...
def formatLang(env, value, digits: Any | None = ..., grouping: bool = ..., monetary: bool = ..., dp: bool = ..., currency_obj: bool = ...): ...
def _consteq(str1, str2): ...

consteq: Any

class Pickle:
    @classmethod
    def load(cls, stream, errors: bool = ...): ...
    @classmethod
    def loads(cls, text): ...
    dumps: Any
    dump: Any
pickle = Pickle

def wrap_module(module, attr_list): ...
