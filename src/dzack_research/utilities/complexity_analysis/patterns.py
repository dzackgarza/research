"""Inventories of architectural and maintainability patterns worth reviewing."""

from __future__ import annotations

import ast
import hashlib
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Location:
    path: str
    line: int
    symbol: str
    detail: str = ""


@dataclass(frozen=True)
class DuplicateBody:
    occurrences: tuple[Location, ...]
    statement_count: int


@dataclass(frozen=True)
class PatternAnalysis:
    asserts: tuple[Location, ...]
    tuple_calls: tuple[Location, ...]
    list_calls: tuple[Location, ...]
    hasattr_calls: tuple[Location, ...]
    getattr_calls: tuple[Location, ...]
    isinstance_calls: tuple[Location, ...]
    attribute_error_probes: tuple[Location, ...]
    preamble_attribute_mentions: tuple[Location, ...]
    preamble_attribute_assignments: tuple[Location, ...]
    global_dict_caches: tuple[Location, ...]
    public_top_level_functions: tuple[Location, ...]
    session_exported_top_level_functions: tuple[Location, ...]
    method_grafts: tuple[Location, ...]
    mathematical_collection_materializations: tuple[Location, ...]
    exhaustive_mathematical_collection_loops: tuple[Location, ...]
    raw_matrix_coordinate_peeks: tuple[Location, ...]
    variadic_positional_signatures: tuple[Location, ...]
    variadic_keyword_signatures: tuple[Location, ...]
    none_default_signatures: tuple[Location, ...]
    pass_statements: tuple[Location, ...]
    duplicate_function_bodies: tuple[DuplicateBody, ...]

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def _call_name(node: ast.Call) -> str | None:
    return node.func.id if isinstance(node.func, ast.Name) else None


def _location(path: Path, root: Path, node: ast.AST, symbol: str, detail: str = "") -> Location:
    return Location(str(path.relative_to(root)), getattr(node, "lineno", 0), symbol, detail)


def _module_name(path: Path, root: Path, package_prefix: str) -> str:
    rel = path.relative_to(root)
    if path.name == "__init__.py":
        suffix = ".".join(rel.parts[:-1])
    else:
        suffix = ".".join([*rel.parts[:-1], path.stem])
    return package_prefix if not suffix else f"{package_prefix}.{suffix}"


def _resolve_from(source_module: str, is_package: bool, module: str | None, level: int) -> str:
    if level == 0:
        return module or ""
    source_package = source_module if is_package else source_module.rpartition(".")[0]
    package_parts = source_package.split(".")
    ascend = level - 1
    base = package_parts[: len(package_parts) - ascend] if ascend else package_parts.copy()
    if module:
        base.extend(module.split("."))
    return ".".join(base)


def _session_exported_function_defs(root: Path, package_prefix: str) -> set[tuple[str, str]]:
    definitions: set[tuple[str, str]] = set()
    reexports: dict[tuple[str, str], tuple[str, str]] = {}

    for path in sorted(root.rglob("*.py")):
        if "__pycache__" in path.parts:
            continue
        module_name = _module_name(path, root, package_prefix)
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError:
            continue
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                definitions.add((module_name, node.name))
            elif isinstance(node, ast.ImportFrom):
                target_module = _resolve_from(module_name, path.name == "__init__.py", node.module, node.level)
                if not target_module:
                    continue
                for alias in node.names:
                    if alias.name == "*":
                        continue
                    local_name = alias.asname or alias.name
                    reexports[(module_name, local_name)] = (target_module, alias.name)

    exported: set[tuple[str, str]] = set()
    all_module = f"{package_prefix}.all"

    def resolve(key: tuple[str, str]) -> tuple[str, str] | None:
        seen: set[tuple[str, str]] = set()
        while key not in seen:
            seen.add(key)
            if key in definitions:
                return key
            target = reexports.get(key)
            if target is None:
                return None
            key = target
        return None

    for key in reexports:
        if key[0] != all_module:
            continue
        definition = resolve(key)
        if definition is not None:
            exported.add(definition)
    return exported


def analyze_patterns(
    root: Path,
    *,
    package_prefix: str,
    duplicate_min_statements: int = 3,
) -> PatternAnalysis:
    root = root.resolve()
    session_exports = _session_exported_function_defs(root, package_prefix)
    asserts: list[Location] = []
    tuple_calls: list[Location] = []
    list_calls: list[Location] = []
    hasattr_calls: list[Location] = []
    getattr_calls: list[Location] = []
    isinstance_calls: list[Location] = []
    attribute_error_probes: list[Location] = []
    preamble_mentions: list[Location] = []
    preamble_assignments: list[Location] = []
    caches: list[Location] = []
    globals_: list[Location] = []
    session_globals: list[Location] = []
    grafts: list[Location] = []
    collection_materializations: list[Location] = []
    exhaustive_collection_loops: list[Location] = []
    matrix_peeks: list[Location] = []
    variadic_positional: list[Location] = []
    variadic_keyword: list[Location] = []
    none_defaults: list[Location] = []
    pass_statements: list[Location] = []
    bodies: dict[str, tuple[int, list[Location]]] = {}

    mathematical_collection_methods = {
        "module_generating_set",
        "module_generators",
        "group_generators",
        "algebra_generating_set",
        "algebra_generators",
        "monoid_generators",
        "elements",
        "vertices",
        "factors",
        "summands",
        "biproduct_factors",
        "irreducible_characters",
        "conjugacy_classes_representatives",
        "ideal_generators",
        "representatives",
        "roots",
    }
    matrix_coordinate_methods = {
        "rows",
        "columns",
        "row",
        "column",
        "list",
        "basis_matrix",
        "row_module",
        "right_kernel",
        "left_kernel",
    }

    for path in sorted(root.rglob("*.py")):
        if "__pycache__" in path.parts:
            continue
        source = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(source, filename=str(path))
        except SyntaxError:
            continue

        module_name = _module_name(path, root, package_prefix)
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"):
                location = _location(path, root, node, node.name)
                globals_.append(location)
                if (module_name, node.name) in session_exports:
                    session_globals.append(location)
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                value = node.value
                for target in targets:
                    if isinstance(target, ast.Name) and "CACHE" in target.id.upper():
                        if isinstance(value, ast.Dict) or (
                            isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id == "dict"
                        ):
                            caches.append(_location(path, root, node, target.id))

        class Visitor(ast.NodeVisitor):
            def __init__(self) -> None:
                self.stack: list[str] = []

            @property
            def symbol(self) -> str:
                return ".".join(self.stack) or "<module>"

            def visit_Assert(self, node: ast.Assert) -> None:
                asserts.append(_location(path, root, node, self.symbol, ast.unparse(node.test)))
                self.generic_visit(node)

            def visit_Pass(self, node: ast.Pass) -> None:
                pass_statements.append(_location(path, root, node, self.symbol, "pass"))

            def visit_Call(self, node: ast.Call) -> None:
                name = _call_name(node)
                target = {
                    "tuple": tuple_calls,
                    "list": list_calls,
                    "hasattr": hasattr_calls,
                    "getattr": getattr_calls,
                    "isinstance": isinstance_calls,
                }.get(name or "")
                if target is not None:
                    target.append(_location(path, root, node, self.symbol, ast.unparse(node)[:160]))

                if name in {"tuple", "list"} and node.args:
                    source = node.args[0]
                    if isinstance(source, ast.Call) and isinstance(source.func, ast.Attribute):
                        if source.func.attr in mathematical_collection_methods:
                            collection_materializations.append(
                                _location(path, root, node, self.symbol, ast.unparse(node)[:160])
                            )

                if isinstance(node.func, ast.Attribute) and node.func.attr in matrix_coordinate_methods:
                    matrix_peeks.append(
                        _location(path, root, node, self.symbol, ast.unparse(node)[:160])
                    )
                self.generic_visit(node)

            def visit_For(self, node: ast.For) -> None:
                rendered = ast.unparse(node.iter)
                if any(f".{name}(" in rendered for name in mathematical_collection_methods):
                    exhaustive_collection_loops.append(
                        _location(path, root, node, self.symbol, rendered[:160])
                    )
                self.generic_visit(node)

            def visit_Try(self, node: ast.Try) -> None:
                for handler in node.handlers:
                    if isinstance(handler.type, ast.Name) and handler.type.id == "AttributeError":
                        attribute_error_probes.append(
                            _location(path, root, node, self.symbol, "except AttributeError")
                        )
                self.generic_visit(node)

            def visit_Attribute(self, node: ast.Attribute) -> None:
                if node.attr.startswith("_preamble_"):
                    preamble_mentions.append(_location(path, root, node, self.symbol, node.attr))
                    if isinstance(node.ctx, ast.Store):
                        preamble_assignments.append(_location(path, root, node, self.symbol, node.attr))
                self.generic_visit(node)

            def _function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
                self.stack.append(node.name)
                if node.args.vararg is not None:
                    variadic_positional.append(
                        _location(path, root, node, self.symbol, f"*{node.args.vararg.arg}")
                    )
                if node.args.kwarg is not None:
                    variadic_keyword.append(
                        _location(path, root, node, self.symbol, f"**{node.args.kwarg.arg}")
                    )
                defaults = [*node.args.defaults, *(default for default in node.args.kw_defaults if default is not None)]
                if any(isinstance(default, ast.Constant) and default.value is None for default in defaults):
                    none_defaults.append(
                        _location(path, root, node, self.symbol, ast.unparse(node.args)[:160])
                    )
                statement_count = len(node.body)
                if statement_count >= duplicate_min_statements:
                    body_dump = ast.dump(ast.Module(body=node.body, type_ignores=[]), include_attributes=False)
                    digest = hashlib.sha256(body_dump.encode()).hexdigest()
                    _, locations = bodies.setdefault(digest, (statement_count, []))
                    locations.append(_location(path, root, node, self.symbol))
                self.generic_visit(node)
                self.stack.pop()

            def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
                self._function(node)

            def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
                self._function(node)

            def visit_ClassDef(self, node: ast.ClassDef) -> None:
                self.stack.append(node.name)
                for item in node.body:
                    if not isinstance(item, ast.Assign) or len(item.targets) != 1:
                        continue
                    target = item.targets[0]
                    value = item.value
                    if isinstance(target, ast.Name) and isinstance(value, ast.Attribute) and isinstance(value.value, ast.Name):
                        grafts.append(
                            _location(path, root, item, self.symbol, f"{target.id} = {value.value.id}.{value.attr}")
                        )
                self.generic_visit(node)
                self.stack.pop()

        Visitor().visit(tree)

    duplicate_groups = tuple(
        DuplicateBody(tuple(locations), statement_count)
        for statement_count, locations in bodies.values()
        if len(locations) > 1
    )
    duplicate_groups = tuple(sorted(duplicate_groups, key=lambda group: (len(group.occurrences), group.statement_count), reverse=True))

    return PatternAnalysis(
        asserts=tuple(asserts),
        tuple_calls=tuple(tuple_calls),
        list_calls=tuple(list_calls),
        hasattr_calls=tuple(hasattr_calls),
        getattr_calls=tuple(getattr_calls),
        isinstance_calls=tuple(isinstance_calls),
        attribute_error_probes=tuple(attribute_error_probes),
        preamble_attribute_mentions=tuple(preamble_mentions),
        preamble_attribute_assignments=tuple(preamble_assignments),
        global_dict_caches=tuple(caches),
        public_top_level_functions=tuple(globals_),
        session_exported_top_level_functions=tuple(session_globals),
        method_grafts=tuple(grafts),
        mathematical_collection_materializations=tuple(collection_materializations),
        exhaustive_mathematical_collection_loops=tuple(exhaustive_collection_loops),
        raw_matrix_coordinate_peeks=tuple(matrix_peeks),
        variadic_positional_signatures=tuple(variadic_positional),
        variadic_keyword_signatures=tuple(variadic_keyword),
        none_default_signatures=tuple(none_defaults),
        pass_statements=tuple(pass_statements),
        duplicate_function_bodies=duplicate_groups,
    )
