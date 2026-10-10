r"""Provenance-bearing symbolic construction grammar for the research preamble.

Categories and axioms are vertices, methods are typed hyperedges, and a
fixed-point computation closes the constructible *types* under operations.
No Sage import, mathematical execution or guesses based on method names.
Unresolved return paths and input constraints are explicit audit findings.

Category declarations and inheritance come from the existing category_graph.
"""

from __future__ import annotations

import argparse
import ast
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dzack_research.utilities import category_graph as graph
from dzack_research.utilities.source_inventory import source_fingerprint


SLOTS = (
    ("Category", "category"),
    ("ParentMethods", "object"),
    ("ElementMethods", "element"),
    ("MorphismMethods", "morphism"),
)
OPERATORS = {
    ast.Add: "__add__", ast.Sub: "__sub__", ast.Mult: "__mul__",
    ast.MatMult: "__matmul__", ast.Div: "__truediv__",
    ast.BitOr: "__or__", ast.BitAnd: "__and__", ast.Pow: "__pow__",
}
MAX_TRACE_DEPTH = 6


def _show(node: ast.AST | None) -> str:
    return ast.unparse(node) if node is not None else "None"


def _returns(function: ast.FunctionDef | ast.AsyncFunctionDef):
    r"""Every lexical return alternative with branch hypotheses, not nested returns."""
    def visit(statements: list[ast.stmt], guards: tuple[str, ...]):
        for stmt in statements:
            match stmt:
                case ast.Return(value=value):
                    yield value, guards, stmt.lineno
                case ast.If(test=test, body=yes, orelse=no):
                    yield from visit(yes, (*guards, _show(test)))
                    yield from visit(no, (*guards, f"not ({_show(test)})"))
                case ast.Match(subject=subject, cases=cases):
                    for branch in cases:
                        condition = f"{_show(subject)} matches {_show(branch.pattern)}"
                        if branch.guard is not None:
                            condition += f" if {_show(branch.guard)}"
                        yield from visit(branch.body, (*guards, condition))
                case ast.Try(body=body, handlers=handlers, orelse=orelse, finalbody=final):
                    yield from visit(body, guards)
                    for handler in handlers:
                        yield from visit(handler.body, (*guards, f"except {_show(handler.type)}"))
                    yield from visit(orelse, guards)
                    yield from visit(final, guards)
                case ast.With(body=body) | ast.AsyncWith(body=body):
                    yield from visit(body, guards)
                case ast.For(body=body, orelse=orelse) | ast.While(body=body, orelse=orelse):
                    yield from visit(body, (*guards, "iteration"))
                    yield from visit(orelse, guards)
                case ast.FunctionDef() | ast.AsyncFunctionDef() | ast.ClassDef():
                    continue
    yield from visit(function.body, ())


def _arguments(function: ast.FunctionDef | ast.AsyncFunctionDef) -> list[dict[str, Any]]:
    args = function.args
    positional = [*args.posonlyargs, *args.args]
    defaults = [None] * (len(positional) - len(args.defaults)) + args.defaults
    result = [
        {"name": arg.arg, "annotation": _show(arg.annotation) if arg.annotation else None,
         "required": default is None, "kind": "positional"}
        for arg, default in zip(positional, defaults, strict=True)
        if arg.arg not in {"self", "cls"}
    ]
    result.extend(
        {"name": arg.arg, "annotation": _show(arg.annotation) if arg.annotation else None,
         "required": default is None, "kind": "keyword"}
        for arg, default in zip(args.kwonlyargs, args.kw_defaults, strict=True)
    )
    for kind, arg in (("varargs", args.vararg), ("kwargs", args.kwarg)):
        if arg:
            result.append({"name": arg.arg, "annotation": _show(arg.annotation)
                           if arg.annotation else None, "required": False, "kind": kind})
    return result


def _port_type(annotation: str | None, categories: set[str]) -> str | None:
    r"""A type obligation explicitly declared by a method parameter.

    Missing annotations remain external obligations, not alleged arguments
    of the category that happens to contain the method.
    """
    if annotation is None:
        return None
    try:
        node = ast.parse(annotation, mode="eval").body
    except SyntaxError:
        return None
    if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
        if node.value.id in categories:
            sort = {"ObjectType": "object", "ParentType": "object",
                    "ElementType": "element"}.get(node.attr)
            if sort:
                return f"{sort}:{node.value.id}"
    if isinstance(node, ast.Name):
        return {
            "Parent": "object:Objects", "ObjectOfCategory": "object:Objects",
            "Element": "element:Objects", "Morphism": "morphism:Objects",
            "Category": "category:Objects",
        }.get(node.id)
    return None


@dataclass
class Method:
    id: str
    owner: str
    slot: str
    name: str
    path: str
    line: int
    node: ast.FunctionDef | ast.AsyncFunctionDef = field(repr=False)
    parameters: list[dict[str, Any]] = field(default_factory=list)
    annotation: str | None = None
    summary: str = ""


@dataclass(frozen=True)
class Result:
    kind: str
    category: str | None
    evidence: str
    expression: str
    guards: tuple[str, ...] = ()
    via: tuple[str, ...] = ()
    placements: tuple[str, ...] = ()

    @property
    def type_id(self) -> str | None:
        if self.kind in {"object", "element", "morphism", "category"} and self.category:
            return f"{self.kind}:{self.category}"
        return None

    def record(self) -> dict[str, Any]:
        return {"kind": self.kind, "category": self.category,
                "type": self.type_id, "evidence": self.evidence,
                "expression": self.expression, "guards": list(self.guards),
                "via": list(self.via), "placements": list(self.placements)}


def _result(kind: str, category: str | None, evidence: str, expr: ast.AST | str,
            *, via: tuple[str, ...] = ()) -> Result:
    return Result(kind, category, evidence,
                  expr if isinstance(expr, str) else _show(expr), via=via)


class Index:
    r"""Source-method and category index, including alias and import resolution."""

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.repo = self.root.parents[2]
        self.trees = {p: ast.parse(p.read_text(encoding="utf-8"), filename=str(p))
                      for p in sorted(self.root.rglob("*.py"))}
        self.declarations = graph.read_tree(self.root)
        self.inclusions = sorted(graph._all_edges(self.declarations))
        self.imports = {p: graph._imported_names(tree) for p, tree in self.trees.items()}
        self.by_module = {
            ".".join(p.relative_to(self.root.parents[1]).with_suffix("").parts): p
            for p in self.trees
        }
        self.methods: dict[str, Method] = {}
        self.by_owner: dict[tuple[str, str, str], str] = {}
        self.functions: dict[tuple[Path, str], str] = {}
        self.session_exports: set[str] = set()
        self.public_catalogues: set[str] = set()
        self.session_bindings: set[str] = set()
        self.module_bindings: dict[Path, dict[str, ast.expr]] = defaultdict(dict)
        self.categories = {d.vertex for d in self.declarations}
        self.categories.update(v for edge in self.inclusions for v in edge)
        self.category_names = {d.name for d in self.declarations}
        self.aliases: dict[tuple[str, str, str], str] = {}
        self.parents: dict[str, set[str]] = defaultdict(set)
        for below, above in self.inclusions:
            self.parents[below].add(above)
        self._collect()
        self._exports()

    def path(self, path: Path) -> str:
        return str(path.relative_to(self.repo))

    def _method(self, node, path: Path, owner: str, slot: str) -> str:
        identifier = f"{self.path(path)}:{node.lineno}:{owner}.{slot}.{node.name}"
        self.methods[identifier] = Method(
            id=identifier, owner=owner, slot=slot, name=node.name,
            path=self.path(path), line=node.lineno, node=node,
            parameters=_arguments(node),
            annotation=_show(node.returns) if node.returns else None,
            summary=(ast.get_docstring(node) or "").strip().split("\n", 1)[0],
        )
        self.by_owner[owner, slot, node.name] = identifier
        return identifier

    def _collect(self) -> None:
        classes = {
            (path, statement.name): statement
            for path, tree in self.trees.items()
            for statement in tree.body
            if isinstance(statement, ast.ClassDef)
        }
        for path, tree in self.trees.items():
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    self.functions[path, node.name] = self._method(
                        node, path, self.path(path), "function")
                elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target in targets:
                        if isinstance(target, ast.Name) and node.value is not None:
                            self.module_bindings[path][target.id] = node.value
                elif isinstance(node, ast.ClassDef):
                    # Lazy class attributes are genuine named mathematical
                    # constructors, especially NamedLattices and its tables.
                    for item in node.body:
                        if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            continue
                        if any("lazy_class_attribute" in _show(decorator)
                               for decorator in item.decorator_list):
                            self._method(item, path, node.name, "catalogue")

        for declaration in self.declarations:
            path = Path(declaration.path)
            tree = self.trees[path]
            category_class = next(
                (item for item in ast.walk(tree)
                 if isinstance(item, ast.ClassDef) and item.lineno == declaration.line),
                None,
            )
            if category_class is None:
                raise ValueError(f"Missing category at {declaration.path}:{declaration.line}")
            for container, slot in SLOTS:
                host = category_class if container == "Category" else next(
                    (item for item in category_class.body
                     if isinstance(item, ast.ClassDef) and item.name == container),
                    None,
                )
                if host is None:
                    continue
                for item in host.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        self._method(item, path, declaration.vertex, slot)
                    if isinstance(item, ast.Assign) and isinstance(item.value, ast.Name):
                        for target in item.targets:
                            if isinstance(target, ast.Name):
                                self.aliases[declaration.vertex, slot, target.id] = item.value.id
            # A Mor category normally specifies its arrow implementation by
            # `ElementMethods = GroupMorphism`, not by a nested
            # `class MorphismMethods`. Those methods are mathematically
            # morphism operations and must not disappear from the survey.
            is_mor = (
                declaration.name.endswith(("Mor", "MorCategory"))
                or any("Mor" in base or "Homset" in base for base in declaration.bases)
            )
            for item in category_class.body:
                if not isinstance(item, ast.Assign) or not isinstance(item.value, ast.Name):
                    continue
                for target in item.targets:
                    if not isinstance(target, ast.Name):
                        continue
                    slot = {
                        "ParentMethods": "object",
                        "ElementMethods": "morphism" if is_mor else "element",
                        "MorphismMethods": "morphism",
                    }.get(target.id)
                    if slot is None:
                        continue
                    source_path, class_name = path, item.value.id
                    if (path, class_name) not in classes and class_name in self.imports[path]:
                        module, original = self.imports[path][class_name]
                        source_path = self.by_module.get(module, path)
                        class_name = original
                    provider = classes.get((source_path, class_name))
                    if provider is None:
                        continue
                    for member in provider.body:
                        if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            if (declaration.vertex, slot, member.name) not in self.by_owner:
                                self._method(member, source_path, declaration.vertex, slot)

    def method(self, owner: str, slot: str, name: str) -> Method | None:
        seen = set()
        while (owner, slot, name) in self.aliases:
            if name in seen:
                break
            seen.add(name)
            name = self.aliases[owner, slot, name]
        identifier = self.by_owner.get((owner, slot, name))
        return self.methods.get(identifier) if identifier else None

    def inherited(self, owner: str, slot: str, name: str) -> list[Method]:
        direct = self.method(owner, slot, name)
        if direct is not None:
            return [direct]
        candidates: list[tuple[int, Method]] = []
        pending: list[tuple[int, str]] = [(0, owner)]
        visited = set()
        while pending:
            distance, vertex = pending.pop(0)
            if vertex in visited:
                continue
            visited.add(vertex)
            if distance and (found := self.method(vertex, slot, name)):
                candidates.append((distance, found))
                continue
            pending.extend((distance + 1, parent) for parent in sorted(self.parents[vertex]))
        minimum = min((distance for distance, _ in candidates), default=None)
        return sorted((m for d, m in candidates if d == minimum), key=lambda m: m.id)

    def helper(self, name: str, path: Path) -> Method | None:
        identifier = self.functions.get((path, name))
        if identifier:
            return self.methods[identifier]
        if name in self.imports[path]:
            module, original = self.imports[path][name]
            destination = self.by_module.get(module)
            if destination:
                identifier = self.functions.get((destination, original))
                if identifier:
                    return self.methods[identifier]
        return None

    def _exports(self) -> None:
        r"""Resolve session function exports through package reexports, without imports."""
        session = self.root / "all.py"
        if session not in self.trees:
            return

        def resolve(module: str, name: str, seen: set[tuple[str, str]]) -> str | None:
            pair = module, name
            if pair in seen:
                return None
            seen.add(pair)
            path = self.by_module.get(module) or self.by_module.get(module + ".__init__")
            if path is None:
                return None
            identity = self.functions.get((path, name))
            if identity:
                return identity
            imported = self.imports[path].get(name)
            if imported:
                # category_graph's ordinary alias resolver intentionally does
                # not expand relative package imports; public `all.py`
                # reexports require that extra source-only resolution step.
                for statement in self.trees[path].body:
                    if not isinstance(statement, ast.ImportFrom):
                        continue
                    if not any((a.asname or a.name) == name for a in statement.names):
                        continue
                    if statement.level:
                        parts = module.split(".")
                        if path.name != "__init__.py":
                            parts.pop()
                        parts = parts[:len(parts) - statement.level + 1]
                        target_module = ".".join([
                            *parts, *(statement.module.split(".") if statement.module else [])
                        ])
                        return resolve(target_module, imported[1], seen)
                return resolve(imported[0], imported[1], seen)
            return None

        for item in self.trees[session].body:
            if isinstance(item, ast.ImportFrom) and item.module:
                for alias in item.names:
                    if (alias.asname or alias.name).startswith("_"):
                        continue
                    self.session_bindings.add(alias.asname or alias.name)
                    identifier = resolve(item.module, alias.name, set())
                    if identifier:
                        self.session_exports.add(identifier)
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not item.name.startswith("_"):
                    self.session_bindings.add(item.name)
                    identifier = self.functions.get((session, item.name))
                    if identifier:
                        self.session_exports.add(identifier)
            if isinstance(item, ast.Expr) and isinstance(item.value, ast.Call):
                call = item.value
                if (isinstance(call.func, ast.Name) and call.func.id == "_lazy_import"
                        and len(call.args) >= 2
                        and isinstance(call.args[1], (ast.Tuple, ast.List))):
                    for name in call.args[1].elts:
                        if isinstance(name, ast.Constant) and isinstance(name.value, str):
                            self.session_bindings.add(name.value)
        self.public_catalogues = {
            method.owner for method in self.methods.values()
            if method.slot == "catalogue" and method.owner in self.session_bindings
        }


class Inference:
    r"""Trace return alternatives through bounded, typed interprocedural paths.

    Each fallback remains unresolved; exceeding a depth bound is *not* a
    negative construction judgment. Runtime observations can subsequently
    corroborate a rule but must never replace a conditional source rule.
    """

    def __init__(self, index: Index, *, depth: int = MAX_TRACE_DEPTH):
        self.index = index
        self.depth = depth
        self.cache: dict[str, tuple[Result, ...]] = {}
        self.calls: dict[str, set[str]] = defaultdict(set)
        self.tree_paths = {str(path): path for path in index.trees}

    def category(self, node: ast.AST, method: Method,
                 assignments: dict[str, list[ast.expr]]) -> str | None:
        if isinstance(node, ast.Name) and node.id in assignments:
            for value in assignments[node.id]:
                found = self.category(value, method, {})
                if found:
                    return found
        if isinstance(node, ast.Name) and node.id not in assignments:
            expression = self.index.module_bindings[
                self.index.repo / method.path
            ].get(node.id)
            if expression is not None and not (
                isinstance(expression, ast.Name) and expression.id == node.id
            ):
                return self.category(expression, method, {})
        # Use the already-owned category name/axiom parser.
        expression = _show(node)
        try:
            base, axioms = graph._axiom_calls(expression)
            head = graph._head(_show(base))
        except (SyntaxError, ValueError):
            return None
        if isinstance(base, ast.Call) and isinstance(base.func, ast.Name):
            binding = self.index.imports.get(self.index.repo / method.path, {}).get(head)
            if binding:
                head = binding[1]
        if head in self.index.category_names:
            return graph._vertex(head, axioms)
        return None

    def _assignments(self, method: Method) -> dict[str, list[ast.expr]]:
        gathered: dict[str, list[ast.expr]] = defaultdict(list)

        def visit(body: list[ast.stmt]) -> None:
            for stmt in body:
                if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    continue
                if isinstance(stmt, (ast.Assign, ast.AnnAssign)):
                    value = stmt.value
                    if value is not None:
                        targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
                        for target in targets:
                            if isinstance(target, ast.Name):
                                gathered[target.id].append(value)
                for field in ("body", "orelse", "finalbody"):
                    child = getattr(stmt, field, None)
                    if isinstance(child, list):
                        visit(child)
                if isinstance(stmt, ast.Try):
                    for handler in stmt.handlers:
                        visit(handler.body)
                if isinstance(stmt, ast.Match):
                    for case in stmt.cases:
                        visit(case.body)

        visit(method.node.body)
        return gathered

    def annotation(self, annotation: str | None) -> Result | None:
        if annotation is None:
            return None
        try:
            tree = ast.parse(annotation, mode="eval").body
        except SyntaxError:
            return None
        if isinstance(tree, ast.Name):
            if tree.id in {"bool", "Predicate"}:
                return _result("value", "Truth", "declared-annotation", annotation)
            if tree.id in {"Parent", "ObjectOfCategory"}:
                return _result("object", "Objects", "broad-annotation", annotation)
            if tree.id in {"Element", "ModuleElement"}:
                return _result("element", "Objects", "broad-annotation", annotation)
            if tree.id in {"Morphism", "Map", "CategoricalMor"}:
                return _result("morphism", "Objects", "broad-annotation", annotation)
            if tree.id in {"Category", "OwnedCategory"}:
                return _result("category", "Objects", "broad-annotation", annotation)
        if isinstance(tree, ast.Attribute):
            if isinstance(tree.value, ast.Name) and tree.value.id in self.index.category_names:
                if tree.attr in {"ObjectType", "ParentType"}:
                    return _result("object", tree.value.id, "declared-annotation", annotation)
                if tree.attr in {"ElementType"}:
                    return _result("element", tree.value.id, "declared-annotation", annotation)
        return None

    def _flow(self, source: Method, target: Method, stack: tuple[str, ...],
              bindings: dict[str, Result]) -> list[Result]:
        self.calls[source.id].add(target.id)
        alternatives = self.trace(target, stack, bindings)
        return [
            Result(item.kind, item.category, "delegated:" + item.evidence,
                   item.expression, item.guards, (target.id, *item.via),
                   item.placements)
            for item in alternatives
        ]

    def _expression(
        self, node: ast.AST | None, method: Method, stack: tuple[str, ...],
        assignments: dict[str, list[ast.expr]],
        bindings: dict[str, Result], local: frozenset[str] = frozenset(),
    ) -> list[Result]:
        if node is None or isinstance(node, ast.Constant) and node.value is None:
            return [_result("none", None, "literal", "None")]
        if isinstance(node, ast.Name):
            if node.id == "self" and method.slot != "function":
                return [_result(method.slot, method.owner, "subject", node)]
            if node.id in bindings:
                got = bindings[node.id]
                return [Result(got.kind, got.category, "argument-flow", got.expression,
                               got.guards, got.via, got.placements)]
            if node.id in assignments and node.id not in local:
                return [
                    item
                    for assigned in assignments[node.id]
                    for item in self._expression(assigned, method, stack, assignments,
                                                 bindings, local | {node.id})
                ]
            return [_result("unknown", None, "unbound-name", node)]
        if isinstance(node, ast.Constant):
            kind = "value" if not isinstance(node.value, bool) else "truth"
            return [_result(kind, type(node.value).__name__, "literal", node)]
        if isinstance(node, (ast.Compare, ast.BoolOp)):
            return [_result("truth", None, "predicate", node)]
        if isinstance(node, ast.IfExp):
            return [
                Result(r.kind, r.category, r.evidence, r.expression,
                       (("" if branch else "not ") + _show(node.test), *r.guards),
                       r.via, r.placements)
                for branch, arm in ((True, node.body), (False, node.orelse))
                for r in self._expression(arm, method, stack, assignments, bindings, local)
            ]
        if isinstance(node, (ast.Tuple, ast.List, ast.Set, ast.Dict,
                             ast.GeneratorExp, ast.ListComp, ast.SetComp, ast.DictComp)):
            return [_result("collection", None, "python-container", node)]
        if isinstance(node, ast.Attribute):
            if (method.slot == "catalogue" and isinstance(node.value, ast.Name)
                    and node.value.id == "cls"):
                target = self.index.method(method.owner, "catalogue", node.attr)
                if target is not None:
                    return self._flow(method, target, stack, {})
            if isinstance(node.value, ast.Name) and node.value.id == "NamedLattices":
                return [_result("object", "Lattices", "named-catalogue", node)]
            return [_result("unknown", None, "attribute-without-call", node)]
        if isinstance(node, ast.BinOp):
            operator = OPERATORS.get(type(node.op))
            if operator:
                obtained = []
                for left in self._expression(node.left, method, stack, assignments, bindings, local):
                    if left.kind in {"object", "element", "morphism"} and left.category:
                        for callee in self.index.inherited(
                            left.category, left.kind, operator
                        ):
                            obtained.extend(self._flow(method, callee, stack, {}))
                if obtained:
                    return obtained
            return [_result("unknown", None, "unresolved-operator", node)]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            return [_result("truth", None, "predicate", node)]
        if isinstance(node, ast.Call):
            function = node.func
            if isinstance(function, ast.Name):
                if function.id in {"bool", "all", "any", "isinstance", "issubclass"}:
                    return [_result("truth", None, "boolean-operation", node)]
                if function.id == "_object_of" and node.args:
                    category = self.category(node.args[0], method, assignments)
                    if category:
                        return [_result("object", category, "owned-constructor", node)]
                binding = self.index.module_bindings[self.index.repo / method.path].get(
                    function.id
                )
                if binding is not None:
                    named_category = self.category(binding, method, {})
                    if named_category:
                        return [_result("object", named_category,
                                        "module-bound-category-constructor", node)]
                category = self.category(node, method, assignments)
                if category:
                    return [_result("category", category, "category-instantiation", node)]
                callee = self.index.helper(function.id, self.index.repo / method.path)
                if callee:
                    values = {}
                    formal = [a["name"] for a in callee.parameters if a["kind"] == "positional"]
                    for arg, name in zip(node.args, formal):
                        possibilities = self._expression(arg, method, stack,
                                                         assignments, bindings, local)
                        if len(possibilities) == 1 and possibilities[0].kind != "unknown":
                            values[name] = possibilities[0]
                    return self._flow(method, callee, stack, values)
                return [_result("unknown", None, "unresolved-function", node)]

            if isinstance(function, ast.Call):
                receivers = self._expression(function, method, stack,
                                             assignments, bindings, local)
                constructed = []
                for item in receivers:
                    if item.kind != "category" or not item.category:
                        continue
                    if item.category.startswith("Mor("):
                        constructed.append(_result("morphism", item.category[4:-1],
                                                   "typed-constructor-application", node))
                        continue
                    placements = [item.category]
                    dynamic_extra = False
                    for keyword in node.keywords:
                        if keyword.arg not in {"_extra_categories", "categories"}:
                            continue
                        if isinstance(keyword.value, (ast.Tuple, ast.List)):
                            for extra in keyword.value.elts:
                                found = self.category(extra, method, assignments)
                                if found:
                                    placements.append(found)
                                else:
                                    dynamic_extra = True
                        else:
                            dynamic_extra = True
                    alternatives = tuple(sorted(set(placements)))
                    target = (f"Join({', '.join(alternatives)})"
                              if len(alternatives) > 1 else item.category)
                    constructed.append(Result(
                        "object", target,
                        ("category-application-with-dynamic-placements"
                         if dynamic_extra else "typed-constructor-application"),
                        _show(node), (), (), alternatives,
                    ))
                return constructed or [_result("unknown", None, "unresolved-callable", node)]

            if isinstance(function, ast.Attribute):
                name = function.attr
                if isinstance(function.value, ast.Name) and function.value.id == "self":
                    candidates = self.index.inherited(method.owner, method.slot, name)
                    if candidates:
                        return [
                            item for candidate in candidates
                            for item in self._flow(method, candidate, stack, {})
                        ]
                receiver_category = self.category(function.value, method, assignments)
                if receiver_category:
                    direct = self.index.inherited(receiver_category, "category", name)
                    if direct:
                        return [item for target in direct
                                for item in self._flow(method, target, stack, {})]
                    if name in {"an_object", "object", "_object_of"}:
                        return [_result("object", receiver_category, "category-constructor", node)]
                    if name in {"Mor", "End", "Iso", "Aut"}:
                        return [_result("category", f"Mor({receiver_category})",
                                        "fixed-mor-construction", node)]
                    # A category's other named methods can construct arbitrary
                    # mathematical objects; no name-based placement is valid.

                receivers = self._expression(function.value, method, stack,
                                             assignments, bindings, local)
                discovered = []
                for receiver in receivers:
                    if not receiver.category or receiver.kind not in {
                        "category", "object", "element", "morphism"
                    }:
                        continue
                    if receiver.kind == "category" and receiver.category.startswith("Mor("):
                        if name in {"identity"}:
                            discovered.append(_result("morphism", receiver.category[4:-1],
                                                      "fixed-mor-identity", node))
                            continue
                    if receiver.kind == "object" and name in {"an_element"}:
                        discovered.append(_result("element", receiver.category,
                                                  "object-element-construction", node))
                        continue
                    if receiver.kind == "object" and name == "__call__":
                        discovered.append(_result("element", receiver.category,
                                                  "object-element-construction", node))
                        continue
                    matches = self.index.inherited(receiver.category, receiver.kind, name)
                    for target in matches:
                        discovered.extend(self._flow(method, target, stack, {}))
                if discovered:
                    return discovered
                return [_result("unknown", None, "unresolved-method-dispatch", node)]

        return [_result("unknown", None, "unresolved-expression", node)]

    def trace(self, method: Method, stack: tuple[str, ...] = (),
              bindings: dict[str, Result] | None = None) -> tuple[Result, ...]:
        bindings = bindings or {}
        if method.id in stack:
            return (_result("unknown", None, "recursive-call", method.name),)
        if len(stack) >= self.depth:
            return (_result("unknown", None, "trace-depth-limit", method.name),)
        if not bindings and method.id in self.cache:
            return self.cache[method.id]
        assignments = self._assignments(method)
        alternatives = []
        for value, guards, _ in _returns(method.node):
            for found in self._expression(value, method, (*stack, method.id),
                                          assignments, bindings):
                alternatives.append(Result(
                    found.kind, found.category, found.evidence,
                    found.expression, (*guards, *found.guards), found.via,
                    found.placements,
                ))
        if not alternatives:
            hint = self.annotation(method.annotation)
            alternatives.append(
                hint or _result(
                    "collection" if any(isinstance(n, (ast.Yield, ast.YieldFrom))
                                        for n in ast.walk(method.node)) else "none",
                    None, "generator" if any(isinstance(n, (ast.Yield, ast.YieldFrom))
                                             for n in ast.walk(method.node))
                    else "implicit-none-or-raises",
                    method.annotation or method.name,
                )
            )
        if all(item.kind == "unknown" for item in alternatives):
            hint = self.annotation(method.annotation)
            if hint:
                alternatives.append(hint)
        unique = tuple({(item.kind, item.category, item.evidence, item.expression,
                         item.guards, item.via, item.placements): item
                        for item in alternatives}.values())
        if not bindings:
            self.cache[method.id] = unique
        return unique


def _closure(categories: list[dict[str, Any]], rules: list[dict[str, Any]],
             inclusions: list[tuple[str, str]]) -> dict[str, Any]:
    r"""Least fixed point of symbolic type *families*, never concrete instances.

    Every seed and rule witness is retained. Required untyped arguments are
    existential parameters, so such a rule is marked conditional and cannot
    be taken as proof that a particular tuple of inputs constructs its output.
    Subcategory propagation is one-way; there is no unjustified
    `Obj(Sets) => Obj(Lattices)` inference.
    """
    known = {row["id"] for row in categories}
    category_parents: dict[str, set[str]] = defaultdict(set)
    for child, parent in inclusions:
        category_parents[child].add(parent)

    witnessed: dict[str, dict[str, Any]] = {}

    def admit(kind: str, category: str, *, proof: str, conditional: bool) -> bool:
        if kind not in {"object", "category", "element", "morphism"} or not category:
            return False
        target = f"{kind}:{category}"
        previous = witnessed.get(target)
        if previous is not None:
            if not previous["conditional"] or conditional:
                return False
        witnessed[target] = {"type": target, "kind": kind, "category": category,
                             "witness": proof, "conditional": conditional}
        return True

    # The source declares the category *families* themselves, not every
    # instance of every parameterized category.
    for category in sorted(known):
        admit("category", category, proof="declared category family", conditional=False)

    # A concrete an_object is a construction witness. It may depend on the
    # category's parameters, which stay symbolic.
    for rule in rules:
        if (rule["slot"] == "category" and rule["name"] == "an_object"
                and rule["owner"] in known):
            admit("object", rule["owner"], proof=rule["id"],
                  conditional=True)

    # A constructor `C(data)` is a possible object of C, with data still a
    # symbolic input. It is not a claim that C is inhabited over every base.
    for rule in rules:
        if (rule["slot"] == "category"
                and rule["name"] in {"__call__", "_element_constructor_", "object"}
                and rule["owner"] in known):
            admit("object", rule["owner"], proof=rule["id"], conditional=True)

    rounds = 0
    while True:
        rounds += 1
        changed = False
        for item in list(witnessed.values()):
            kind, category = item["kind"], item["category"]
            if kind in {"object", "element", "morphism"}:
                for parent in category_parents.get(category, ()):
                    changed |= admit(kind, parent,
                                     proof=f"inherits from {kind}:{category}",
                                     conditional=item["conditional"])
            if kind == "object":
                changed |= admit("element", category,
                                 proof=f"element of constructible object:{category}",
                                 conditional=item["conditional"])
                changed |= admit("morphism", category,
                                 proof=f"identity in selected Mor({category})",
                                 conditional=item["conditional"])
        for rule in rules:
            if rule["slot"] in {"function", "catalogue"} and not rule["exported"]:
                # Private module helpers are recorded as delegates but are
                # not independent public constructors.
                continue
            input_type = f'{rule["slot"]}:{rule["owner"]}'
            witness = witnessed.get(input_type) if rule["slot"] not in {
                "function", "catalogue"
            } else {
                "conditional": False
            }
            if witness is None:
                continue
            requires_data = any(p["required"] for p in rule["parameters"])
            typed = [p["expected_type"] for p in rule["parameters"]
                     if p["required"] and p["expected_type"]]
            if any(req not in witnessed for req in typed):
                continue
            for result in rule["results"]:
                if result["type"] is None:
                    continue
                kind, _, category = result["type"].partition(":")
                if category.startswith("Mor(") and category.endswith(")"):
                    continue
                changed |= admit(
                    kind, category, proof=rule["id"],
                    conditional=(witness["conditional"] or requires_data
                                 or any(witnessed[req]["conditional"] for req in typed)
                                 or bool(result["guards"])
                                 or result["evidence"].startswith("broad-")),
                )
        if not changed:
            break
        if rounds > (len(categories) * 4 + 20):
            raise RuntimeError("symbolic closure did not stabilize over the finite type set")

    return {"rounds": rounds, "types": sorted(witnessed.values(),
                                             key=lambda x: x["type"])}


def build_manifest(root: Path, *, depth: int = MAX_TRACE_DEPTH,
                   observations: dict[str, Any] | None = None) -> dict[str, Any]:
    r"""Inventory every method and return branch, then close typed result edges."""
    index = Index(root)
    inference = Inference(index, depth=depth)
    categories: list[dict[str, Any]] = []
    declarations_by_vertex = defaultdict(list)
    for d in index.declarations:
        declarations_by_vertex[d.vertex].append(d)
    for name in sorted(index.categories):
        records = declarations_by_vertex[name]
        constructor = index.method(name, "category", "__init__")
        categories.append({
            "id": name,
            "declared": bool(records),
            "sources": [
                {"path": index.path(Path(d.path)), "line": d.line,
                 "summary": d.summary, "qualified_name": d.qualified_name,
                 "bases": list(d.bases), "abstract": d.abstract}
                for d in records
            ],
            "parents": sorted(index.parents[name]),
            "constructor_parameters": constructor.parameters if constructor else [],
            "parameterization": (
                "base ring" if any("OwnedCategoryOverBaseRing" in d.bases for d in records)
                else "dependent / source-declared" if any("OwnedParameterizedCategory" in d.bases
                                                         for d in records)
                else "axiom or parameter expression" if not records or "." in name
                else "see constructor signature"
            ),
        })

    rules: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    for below, above in index.inclusions:
        edges.append({"source": f"category:{below}", "target": f"category:{above}",
                      "relation": "subcategory"})
    for method in sorted(index.methods.values(), key=lambda m: m.id):
        inferred = [r.record() for r in inference.trace(method)]
        # Runtime specimens are an independent, explicitly non-generalizing
        # observation. They never replace missing source alternatives.
        observed = (observations or {}).get(method.owner, {}).get(
            {"object": "ParentMethods", "element": "ElementMethods",
             "morphism": "MorphismMethods"}.get(method.slot, ""), {}
        ).get(method.name)
        parameters = [
            {**argument,
             "expected_type": _port_type(argument["annotation"], index.categories)}
            for argument in method.parameters
        ]
        rule = {
            "id": method.id, "owner": method.owner, "slot": method.slot,
            "name": method.name, "source": f"{method.path}:{method.line}",
            "path": method.path, "line": method.line,
            "summary": method.summary, "parameters": parameters,
            "annotation": method.annotation, "public": not method.name.startswith("_"),
            "exported": method.id in index.session_exports or (
                method.slot == "catalogue" and method.owner in index.public_catalogues
            ),
            "operator": method.name.startswith("__") and method.name.endswith("__"),
            "results": inferred, "observed_result": observed,
            "result_status": (
                "unresolved" if all(row["kind"] == "unknown" for row in inferred)
                else "partial" if any(row["kind"] == "unknown" for row in inferred)
                else "classified"
            ),
            "resolved": all(row["kind"] != "unknown" for row in inferred),
            "constructs_object": any(row["kind"] == "object" for row in inferred),
            "contract": (
                f"object:{method.owner}" if method.slot == "category"
                and method.name in {"an_object", "__call__", "_element_constructor_", "object"}
                else f"element:{method.owner}" if method.slot == "object"
                and method.name in {"__call__", "_element_constructor_"}
                else None
            ),
        }
        rules.append(rule)
        if method.slot in {"function", "catalogue"}:
            # Files and helpers remain inspectable and traceable, but are not
            # all declared public session entrypoints.
            if method.slot == "catalogue":
                edges.append({"source": f"catalogue:{method.owner}",
                              "target": "operation:" + method.id,
                              "relation": "catalogue-entry"})
                for alternative in inferred:
                    if alternative["type"]:
                        edges.append({"source": "operation:" + method.id,
                                      "target": alternative["type"],
                                      "relation": "result",
                                      "evidence": alternative["evidence"],
                                      "guards": alternative["guards"]})
            continue
        operation = "operation:" + method.id
        edges.append({"source": f"category:{method.owner}", "target": operation,
                      "relation": "declares-method", "slot": method.slot})
        edges.append({"source": f"{method.slot}:{method.owner}", "target": operation,
                      "relation": "subject-input"})
        for index_arg, argument in enumerate(parameters):
            if argument["required"]:
                edges.append({"source": argument["expected_type"]
                              or f"parameter:{method.id}:{index_arg}",
                              "target": operation, "relation": "argument-input",
                              "label": argument["name"], "annotation": argument["annotation"],
                              "typed": bool(argument["expected_type"])})
        for alternative in inferred:
            if alternative["type"]:
                edges.append({"source": operation, "target": alternative["type"],
                              "relation": "result", "evidence": alternative["evidence"],
                              "guards": alternative["guards"]})
    for caller, callees in sorted(inference.calls.items()):
        for callee in sorted(callees):
            edges.append({"source": "operation:" + caller, "target": "operation:" + callee,
                          "relation": "delegates"})

    # A categorical join is a SINGLE more-structured output, not several
    # mutually exclusive return alternatives. Include its projections into
    # each category the construction states, even for joins first met in a
    # method result rather than declared by a named class.
    extra_edges: set[tuple[str, str]] = set()
    join_categories: dict[str, tuple[str, ...]] = {}
    for rule in rules:
        for outcome in rule["results"]:
            if len(outcome["placements"]) < 2 or not outcome["category"]:
                continue
            join = outcome["category"]
            placements = tuple(outcome["placements"])
            join_categories[join] = placements
            for placed in placements:
                extra_edges.add((join, placed))
    for join, placements in sorted(join_categories.items()):
        categories.append({
            "id": join, "declared": False, "sources": [],
            "parents": list(placements), "constructor_parameters": [],
            "parameterization": "constructed join (all placements hold simultaneously)",
        })
    for a, b in sorted(extra_edges):
        edges.append({"source": f"category:{a}", "target": f"category:{b}",
                      "relation": "constructed-join-projection"})
    inclusions = sorted(set(index.inclusions) | extra_edges)
    closure = _closure(categories, rules, inclusions)
    summary = Counter(
        row["result_status"]
        for row in rules
    )
    public = [r for r in rules if r["public"] and r["slot"] != "function"]
    return {
        "schema": "construction-universe/1",
        "basis": "static source, conditional typed hypergraph; no Sage executions",
        "source_sha256": source_fingerprint(index.root),
        "scope": str(index.root.relative_to(index.repo)),
        "summary": {
            "category_vertices": len(categories),
            "declared_categories": len(index.declarations),
            "constructed_join_vertices": len(join_categories),
            "method_rules": len(rules),
            "session_function_exports": len(index.session_exports),
            "public_catalogue_entries": sum(r["slot"] == "catalogue" and r["exported"]
                                            for r in rules),
            "public_category_methods": len(public),
            "resolved_methods": summary["classified"],
            "partially_resolved_methods": summary["partial"],
            "unresolved_methods": summary["unresolved"] + summary["partial"],
            "public_unresolved": sum(r["result_status"] != "classified" for r in public),
            "object_result_rules": sum(r["constructs_object"] for r in rules),
            "construction_edges": len(edges),
            "typed_argument_ports": sum(
                bool(argument["expected_type"]) for rule in rules
                for argument in rule["parameters"] if argument["required"]
            ),
            "reachable_type_families": len(closure["types"]),
            "closure_rounds": closure["rounds"],
            "by_slot": dict(sorted(Counter(r["slot"] for r in rules).items())),
            "by_evidence": dict(sorted(Counter(
                result["evidence"].removeprefix("delegated:").split("delegated:")[-1]
                for row in rules for result in row["results"]
            ).items())),
        },
        "categories": categories, "rules": rules,
        "inclusions": [list(e) for e in inclusions],
        "edges": edges, "closure": closure,
        "unresolved": [
            {"id": r["id"], "owner": r["owner"], "name": r["name"],
             "slot": r["slot"], "source": r["source"],
             "return_expressions": [
                 {"expression": x["expression"], "reason": x["evidence"],
                  "guards": x["guards"]}
                 for x in r["results"] if x["kind"] == "unknown"
             ]}
            for r in rules if any(x["kind"] == "unknown" for x in r["results"])
        ],
    }


def render_html(manifest: dict[str, Any]) -> str:
    r"""Standalone interactive audit; no third-party JavaScript or network."""
    template = Path(__file__).with_name("construction_universe_view.html").read_text(
        encoding="utf-8"
    )
    # The JSON is data inside a script tag, not executable JavaScript.
    encoded = json.dumps(manifest, ensure_ascii=False, separators=(",", ":"))
    encoded = encoded.replace("<", "\\u003c").replace("&", "\\u0026")
    return template.replace("<!--CONSTRUCTION_UNIVERSE_DATA-->", encoded)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1] / "preamble")
    parser.add_argument("--json", type=Path, required=True, help="machine-readable complete audit")
    parser.add_argument("--html", type=Path, required=True, help="standalone interactive browser")
    parser.add_argument("--depth", type=int, default=MAX_TRACE_DEPTH)
    parser.add_argument("--inferred", type=Path, help="optional existing category_inference observations")
    options = parser.parse_args(argv)
    if options.depth < 1:
        parser.error("--depth must be positive")
    observations = json.loads(options.inferred.read_text()) if options.inferred else None
    report = build_manifest(options.root, depth=options.depth, observations=observations)
    options.json.parent.mkdir(parents=True, exist_ok=True)
    options.html.parent.mkdir(parents=True, exist_ok=True)
    options.json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    options.html.write_text(render_html(report), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
