from typing import Any

def transpile_javascript(url, content): ...

URL_RE: Any

def url_to_module_path(url): ...
def wrap_with_odoo_define(module_path, content): ...

EXPORT_FCT_OR_CLASS_RE: Any

def convert_export_function_or_class(content): ...

EXPORT_FCT_OR_CLASS_DEFAULT_RE: Any

def convert_export_function_or_class_default(content): ...

EXPORT_VAR_RE: Any

def convert_variable_export(content): ...

EXPORT_DEFAULT_VAR_RE: Any

def convert_variable_export_default(content): ...

EXPORT_OBJECT_RE: Any

def convert_object_export(content): ...

EXPORT_FROM_RE: Any

def convert_from_export(content): ...

EXPORT_STAR_FROM_RE: Any

def convert_star_from_export(content): ...

EXPORT_DEFAULT_RE: Any

def convert_default_export(content): ...

IMPORT_BASIC_RE: Any

def convert_basic_import(content): ...

IMPORT_LEGACY_DEFAULT_RE: Any

def convert_legacy_default_import(content): ...

IMPORT_DEFAULT: Any

def convert_default_import(content): ...

RELATIVE_REQUIRE_RE: Any

def convert_relative_require(url, content): ...

IMPORT_STAR: Any

def convert_star_import(content): ...

IMPORT_UNNAMED_RELATIVE_RE: Any

def convert_unnamed_relative_import(content): ...

URL_INDEX_RE: Any

def remove_index(content): ...
def relative_path_to_module_path(url, path_rel): ...

ODOO_MODULE_RE: Any

def is_odoo_module(content): ...
def get_aliased_odoo_define_content(module_path, content): ...
def convert_as(val): ...
def remove_as(val): ...