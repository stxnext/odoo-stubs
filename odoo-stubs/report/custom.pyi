from . import render
from .interface import report_int
from typing import Any

class external_pdf(render.render):
    pdf: Any
    output_type: str
    def __init__(self, pdf) -> None: ...
    def _render(self): ...

class report_custom(report_int):
    def __init__(self, name) -> None: ...
    def _row_get(self, cr, uid, objs, fields, conditions, row_canvas: Any | None = ..., group_by: Any | None = ...): ...
    def create(self, cr, uid, ids, datas, context: Any | None = ...): ...
    obj: Any
    def _create_tree(self, uid, ids, report, fields, level, results, context): ...
    def _create_lines(self, cr, uid, ids, report, fields, results, context): ...
    def _create_bars(self, cr, uid, ids, report, fields, results, context): ...
    def _create_pie(self, cr, uid, ids, report, fields, results, context): ...
    def _create_table(self, uid, ids, report, fields, tree, results, context): ...
