from . import Command
from ..api import Environment
from ..models import BaseModel

class Populate(Command):
    def run(self, cmdargs) -> None: ...
    @classmethod
    def populate(cls, env: Environment, size, model_patterns: bool = ..., profiling_enabled: bool = ...,
                 commit: bool = ...) -> dict: ...
    @classmethod
    def _get_ordered_models(cls, env: Environment, model_patterns: bool = ...) -> list[BaseModel]: ...
