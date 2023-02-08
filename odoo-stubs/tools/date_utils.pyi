import datetime
from typing import Tuple, Iterator, TypeVar

from dateutil.relativedelta import relativedelta

_DateTimeT = TypeVar('_DateTimeT', datetime.date, datetime.datetime)

def get_month(date: _DateTimeT) -> Tuple[_DateTimeT, _DateTimeT]: ...
def get_quarter_number(date: _DateTimeT) -> int: ...
def get_quarter(date: _DateTimeT) -> Tuple[_DateTimeT, _DateTimeT]: ...
def get_fiscal_year(date: _DateTimeT, day: int = ..., month: int = ...) -> Tuple[_DateTimeT, _DateTimeT]: ...
def get_timedelta(qty: int, granularity: str) -> relativedelta: ...
def start_of(value: _DateTimeT, granularity: str) -> _DateTimeT: ...
def end_of(value: _DateTimeT, granularity: str) -> _DateTimeT: ...
def add(value: _DateTimeT, *args, **kwargs) -> _DateTimeT: ...
def subtract(value: _DateTimeT, *args, **kwargs) -> _DateTimeT: ...
def json_default(obj) -> str: ...
def date_range(start: datetime.datetime, end: datetime.datetime, step: relativedelta = ...) -> Iterator[datetime.datetime]: ...
