"""Inspect operation definitions, construction routes and private accesses.

This is source evidence, not a resolved runtime call graph. Attribute calls
retain their receiver expression; matching names are leads for review.
Python files are parsed without importing the preamble. Parse errors remain
errors. JSON records keep source locations and the exact inspected population.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from collections import Counter
from dataclasses import asdict, dataclass, field
from fnmatch import fnmatchcase
from pathlib import Path

from dzack_research.utilities.complexity_analysis.patterns import DuplicateBody, analyze_patterns

DEFAULT_ROOTS = ("src", "tests")
CONSTRUCTORS = ("__init__", "__new__", "__call__", "_call_", "_element_constructor_", "__classcall*")
type Function = ast.FunctionDef | ast.AsyncFunctionDef


@dataclass(frozen=True)
class Reference:
    path: str
    line: int
    owner: str
    name: str
    receiver: str
    expression: str
    shape: str


@dataclass
class Definition:
    path: str
    line: int
    owner: str
    name: str
    signature: str
    visibility: str
    summary: str
    returns: list[str] = field(default_factory=list)
    tuple_arities: list[int] = field(default_factory=list)
    calls: list[Reference] = field(default_factory=list)
    private_accesses: list[Reference] = field(default_factory=list)


@dataclass(frozen=True)
class Survey:
    roots: list[str]
    files: list[str]
    source_digest: str
    patterns: list[str]
    definitions: list[Definition]
    call_sites: list[Reference]
    duplicate_bodies: list[DuplicateBody]
    boundary: str = (
        "Python source only; attribute-call targets and receiver types are unresolved. "
        "A spelling or identical body is not proof of common mathematical meaning. "
        "Private access requires review of the declaration-side protected contract."
    )


def _classify(parent: ast.AST | None) -> str:
    match parent:
        case ast.Compare():
            return "compared"
        case ast.Subscript():
            return "indexed"
        case ast.Assign(targets=[ast.Tuple() | ast.List(), *_]):
            return "unpacked"
        case ast.Assign():
            return "bound"
        case ast.Return():
            return "returned"
        case ast.Call():
            return "argument"
        case ast.For():
            return "iterated"
        case _:
            return "expression"


def _visibility(name: str) -> str:
    if name.startswith("__") and name.endswith("__"):
        return "protocol"
    return "private" if name.startswith("_") else "public"


class SourceVisitor(ast.NodeVisitor):
    """Record lexical ownership using Python's documented AST visitor protocol.

    Reference: https://docs.python.org/3/library/ast.html#ast.NodeVisitor
    Function bodies are visited in their own scope, including nested functions.
    This supplies source relations only, without inventing dynamic dispatch.
    """

    def __init__(self, path: Path) -> None:
        self.path = str(path)
        self.scope: list[str] = []
        self.functions: list[Definition] = []
        self.definitions: list[Definition] = []
        self.calls: list[Reference] = []
        self.parents: dict[ast.AST, ast.AST] = {}

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.scope.append(node.name)
        self.generic_visit(node)
        self.scope.pop()

    def _function(self, node: Function) -> None:
        self.scope.append(node.name)
        definition = Definition(
            self.path, node.lineno, ".".join(self.scope), node.name,
            f"({ast.unparse(node.args)})"
            + (f" -> {ast.unparse(node.returns)}" if node.returns else ""),
            _visibility(node.name), (ast.get_docstring(node) or "").split("\n", 1)[0],
        )
        self.definitions.append(definition)
        self.functions.append(definition)
        for statement in node.body:
            self.visit(statement)
        self.functions.pop()
        self.scope.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._function(node)

    def visit_Return(self, node: ast.Return) -> None:
        if self.functions and node.value is not None:
            self.functions[-1].returns.append(ast.unparse(node.value))
            if isinstance(node.value, ast.Tuple):
                self.functions[-1].tuple_arities.append(len(node.value.elts))
        self.generic_visit(node)

    def _reference(self, node: ast.Call | ast.Attribute, name: str, receiver: str) -> Reference:
        return Reference(
            self.path, node.lineno, ".".join(self.scope) or "<module>",
            name, receiver, ast.unparse(node), _classify(self.parents.get(node)),
        )

    def visit_Call(self, node: ast.Call) -> None:
        match node.func:
            case ast.Attribute(value=value, attr=name):
                reference = self._reference(node, name, ast.unparse(value))
            case ast.Name(id=name):
                reference = self._reference(node, name, "")
            case _:
                # Retain chained constructors such as Subgroups(G)(generators).
                reference = self._reference(node, ast.unparse(node.func), "")
        self.calls.append(reference)
        if self.functions:
            self.functions[-1].calls.append(reference)
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if self.functions and _visibility(node.attr) == "private":
            receiver = ast.unparse(node.value)
            if receiver not in {"self", "cls", "super()"}:
                self.functions[-1].private_accesses.append(self._reference(node, node.attr, receiver))
        self.generic_visit(node)


def survey(patterns: list[str], roots: list[str], view: str = "operation", visibility: str = "all") -> Survey:
    assert all(Path(root).is_dir() for root in roots), f"Source roots must be directories: {roots!r}"
    paths = sorted({p for root in roots for p in Path(root).rglob("*.py")})
    assert paths, f"No Python source files in {roots!r}"
    definitions: list[Definition] = []
    calls: list[Reference] = []
    digest = hashlib.sha256()
    for path in paths:
        source = path.read_bytes()
        digest.update(str(path).encode() + b"\0" + source + b"\0")
        tree = ast.parse(source, filename=str(path))
        visitor = SourceVisitor(path)
        visitor.parents = {child: parent for parent in ast.walk(tree) for child in ast.iter_child_nodes(parent)}
        visitor.visit(tree)
        definitions.extend(visitor.definitions)
        calls.extend(visitor.calls)

    def selected(definition: Definition) -> bool:
        if patterns and not any(fnmatchcase(definition.name, p) or fnmatchcase(definition.owner, p) for p in patterns):
            return False
        if visibility != "all" and definition.visibility != visibility:
            return False
        match view:
            case "constructors":
                return any(fnmatchcase(definition.name, p) for p in CONSTRUCTORS)
            case "private":
                return bool(definition.private_accesses)
            case _:
                return True

    selected_definitions = [d for d in definitions if selected(d)]
    names = {d.name for d in selected_definitions}
    duplicate_bodies: list[DuplicateBody] = []
    if view == "duplicates":
        # Reuse the repository's AST-body inventory rather than a second clone detector.
        for root in roots:
            duplicate_bodies.extend(analyze_patterns(Path(root), package_prefix="").duplicate_function_bodies)
        sites = {(d.path, d.line) for d in selected_definitions}
        duplicate_bodies = [
            group for group in duplicate_bodies
            if any(
                (str(Path(root) / location.path), location.line) in sites
                for root in roots for location in group.occurrences
            )
        ]
    call_sites = [
        call for call in calls
        if call.name in names or any(fnmatchcase(call.name, p) for p in patterns)
    ]
    return Survey(roots, [str(p) for p in paths], digest.hexdigest(), patterns,
                  selected_definitions, call_sites, duplicate_bodies)


def render(result: Survey, view: str) -> str:
    lines = [
        "# Source inspection", "", result.boundary, "",
        f"Source digest: {result.source_digest}", f"Roots: {', '.join(result.roots)}", "",
    ]
    if view == "duplicates":
        for group in result.duplicate_bodies:
            lines += ["## Identical AST bodies", ""]
            lines.extend(f"- {s.path}:{s.line}  {s.symbol}" for s in group.occurrences)
        return "\n".join(lines)
    return_shapes: dict[str, set[int]] = {}
    for definition in result.definitions:
        return_shapes.setdefault(definition.name, set()).update(definition.tuple_arities)
    for name, arities in sorted(return_shapes.items()):
        if len(arities) > 1:
            lines.append(f"Review codomain differences for {name}: tuple-display arities {sorted(arities)}")
    for definition in result.definitions:
        lines += [
            f"## {definition.owner}{definition.signature} [{definition.visibility}]",
            f"{definition.path}:{definition.line}", definition.summary,
        ]
        lines.extend(f"  returns: {value}" for value in definition.returns)
        references = definition.private_accesses if view == "private" else definition.calls
        lines.extend(f"  {r.path}:{r.line}  {r.expression}" for r in references)
        if len(set(definition.tuple_arities)) > 1:
            lines.append(f"  Review return shapes: {sorted(set(definition.tuple_arities))}")
        lines.append("")
    lines += ["## Call sites matching the selected spellings", ""]
    lines.extend(f"- {c.path}:{c.line} {c.owner} [{c.shape}]  {c.expression}" for c in result.call_sites)
    lines += ["", "## Call-site shapes", "", "| Shape | Count |", "| --- | ---: |"]
    lines.extend(f"| {shape} | {count} |" for shape, count in Counter(c.shape for c in result.call_sites).most_common())
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("names", nargs="*", help="operation or qualified-owner glob patterns")
    parser.add_argument("--root", action="append", dest="roots", help="Python source tree; repeatable")
    parser.add_argument("--view", choices=("operation", "constructors", "private", "duplicates"), default="operation")
    parser.add_argument("--visibility", choices=("all", "public", "private", "protocol"), default="all")
    parser.add_argument("--json", action="store_true", help="emit evidence and source population as JSON")
    args = parser.parse_args()
    if not args.names and args.view == "operation":
        parser.error("provide operation patterns, or choose --view constructors/private/duplicates")
    result = survey(args.names, args.roots or list(DEFAULT_ROOTS), args.view, args.visibility)
    print(json.dumps(asdict(result), indent=2) if args.json else render(result, args.view))


if __name__ == "__main__":
    main()
