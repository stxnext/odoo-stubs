from typing import Any

class render:
    done: bool
    bin_datas: Any
    path: Any
    def __init__(self, bin_datas: Any | None = ..., path: str = ...) -> None: ...
    def _render(self) -> None: ...
    _result: Any
    def render(self): ...
    def is_done(self): ...
    def get(self): ...
