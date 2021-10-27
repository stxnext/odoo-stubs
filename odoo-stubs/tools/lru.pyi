from typing import Any

__all__: Any

class LRUNode:
    __slots__: Any
    prev: Any
    me: Any
    next: Any
    def __init__(self, prev, me) -> None: ...

class LRU:
    _lock: Any
    count: Any
    d: Any
    first: Any
    last: Any
    def __init__(self, count, pairs=...) -> None: ...
    def __contains__(self, obj): ...
    def get(self, obj, val: Any | None = ...): ...
    def __getitem__(self, obj): ...
    def __setitem__(self, obj, val) -> None: ...
    def __delitem__(self, obj) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def iteritems(self) -> None: ...
    def iterkeys(self): ...
    def itervalues(self) -> None: ...
    def keys(self): ...
    def pop(self, key): ...
    def clear(self) -> None: ...
