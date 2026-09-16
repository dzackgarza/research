"""The declared category graph, read from source without importing it.

The live survey in :mod:`dzack_research.utilities.megadoc` answers what a
session *does*.  This module answers what the source *says*: which categories
exist, and what each one declares as its supercategories.  It parses the tree
with :mod:`ast`, so it reports on a preamble that does not currently import,
which is exactly when the declarations most need reading.

A ``super_categories()`` return value is a mathematical claim -- that every
object of this category is an object of those -- and this is the surface that
makes each claim legible beside every other one.
"""

from __future__ import annotations

import argparse
import ast
import json
from dataclasses import dataclass, field
from pathlib import Path

CATEGORY_BASES: frozenset[str] = frozenset(
    {
        "Category",
        "CategoryWithAxiom",
        "CategoricalHomset",
        "HomCategoryConstruction",
        "OwnedCategory",
        "OwnedCategoryBase",
        "OwnedCategoryOverBaseRing",
        "OwnedParameterizedCategory",
        "_SchemePropertyCategory",
    }
)

DECLARATION = "super_categories"


@dataclass(frozen=True)
class Supercategory:
    """One declared supercategory, and where its name comes from."""

    expression: str
    head: str
    resolved: str  # the head with any import alias followed back to its name
    origin: str  # "owned", "sage", or "expression"


@dataclass(frozen=True)
class CategoryDeclaration:
    """One category class and the supercategories its source declares."""

    name: str
    qualified_name: str
    path: str
    line: int
    bases: tuple[str, ...]
    summary: str
    declares: bool
    abstract: bool
    supercategories: tuple[Supercategory, ...] = field(default_factory=tuple)

    @property
    def heads(self) -> tuple[str, ...]:
        """The category names alone, with each declaration's arguments dropped."""
        return tuple(declared.head for declared in self.supercategories)

    @property
    def sage_supercategories(self) -> tuple[Supercategory, ...]:
        """The declared supercategories whose names are Sage's, not this tree's."""
        return tuple(d for d in self.supercategories if d.origin == "sage")


def _head(expression: str) -> str:
    """Return the name a supercategory expression applies or refers to."""
    stripped = expression.split("(", 1)[0]
    return stripped.rsplit(".", 1)[-1].strip()


def _summary(node: ast.ClassDef) -> str:
    text = ast.get_docstring(node) or ""
    return text.strip().split("\n", 1)[0]


def _is_abstract(node: ast.FunctionDef) -> bool:
    for decorator in node.decorator_list:
        if _head(ast.unparse(decorator)) == "abstract_method":
            return True
    return False


def _returned_supercategories(node: ast.FunctionDef) -> tuple[str, ...]:
    """Collect every expression this declaration returns as a supercategory."""
    found: list[str] = []
    for statement in ast.walk(node):
        if not isinstance(statement, ast.Return) or statement.value is None:
            continue
        value = statement.value
        if isinstance(value, (ast.List, ast.Tuple, ast.Set)):
            found.extend(ast.unparse(item) for item in value.elts)
        else:
            found.append(ast.unparse(value))
    return tuple(found)


def _imported_names(tree: ast.Module) -> dict[str, tuple[str, str]]:
    """Map each imported name to the module and the name it was imported as.

    A name bound by ``import X as Y`` is the same category as ``X``; resolving
    ``Y`` back to ``X`` is what keeps an alias from reading as a category that
    nothing defines.
    """
    origins: dict[str, tuple[str, str]] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                origins[alias.asname or alias.name] = (node.module, alias.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                bound = alias.asname or alias.name.split(".")[0]
                origins[bound] = (alias.name, alias.name.split(".")[-1])
    return origins


def _module_level_names(tree: ast.Module) -> set[str]:
    """Names a module binds besides its classes: factories and rebindings.

    ``def FiniteSets()`` returning a category, and ``OwnedAbelianGroups =
    AbelianGroups``, both define a category name as surely as a ``class``
    statement does.
    """
    bound: set[str] = set()
    for statement in tree.body:
        if isinstance(statement, ast.FunctionDef):
            bound.add(statement.name)
        elif isinstance(statement, ast.Assign):
            for target in statement.targets:
                if isinstance(target, ast.Name):
                    bound.add(target.id)
    return bound


def _declaration(node: ast.ClassDef) -> ast.FunctionDef | None:
    for statement in node.body:
        if isinstance(statement, ast.FunctionDef) and statement.name == DECLARATION:
            return statement
    return None


def _is_category(node: ast.ClassDef, known: set[str]) -> bool:
    for base in node.bases:
        if _head(ast.unparse(base)) in CATEGORY_BASES | known:
            return True
    return False


def _resolved(head: str, imported: dict[str, tuple[str, str]]) -> str:
    """Follow ``import X as Y`` back, so an alias names the category it aliases."""
    binding = imported.get(head)
    return binding[1] if binding is not None else head


def _origin(
    head: str, imported: dict[str, tuple[str, str]], known: set[str]
) -> str:
    """Say where a declared supercategory's name comes from."""
    binding = imported.get(head)
    if binding is not None and binding[0].split(".")[0] == "sage":
        return "sage"
    if head in known or (binding is not None and binding[1] in known):
        return "owned"
    if binding is not None:
        return "owned"
    return "expression"


def read_tree(root: Path) -> list[CategoryDeclaration]:
    """Read every category declared under ``root``, in source order per file."""
    sources = sorted(root.rglob("*.py"))
    parsed: list[tuple[Path, ast.Module]] = []
    for path in sources:
        try:
            parsed.append((path, ast.parse(path.read_text(encoding="utf-8"))))
        except SyntaxError:
            continue

    known: set[str] = set()
    # Two passes: a category declared through another category's name is only
    # recognisable once that name is known, and files are read in path order.
    for _ in range(2):
        for _, tree in parsed:
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and _is_category(node, known):
                    known.add(node.name)
    # A category name is also bound by a factory function or a rebinding, so
    # those count as defined when a declaration names them.
    for _, tree in parsed:
        known |= _module_level_names(tree)

    declarations: list[CategoryDeclaration] = []
    for path, tree in parsed:
        imported = _imported_names(tree)
        for scope, node in _classes(tree):
            if not _is_category(node, known):
                continue
            declaration = _declaration(node)
            declarations.append(
                CategoryDeclaration(
                    name=node.name,
                    qualified_name=".".join((*scope, node.name)),
                    path=str(path),
                    line=node.lineno,
                    bases=tuple(_head(ast.unparse(base)) for base in node.bases),
                    summary=_summary(node),
                    declares=declaration is not None,
                    abstract=declaration is not None and _is_abstract(declaration),
                    supercategories=tuple(
                        Supercategory(
                            expression=expression,
                            head=_head(expression),
                            resolved=_resolved(_head(expression), imported),
                            origin=_origin(_head(expression), imported, known),
                        )
                        for expression in (
                            _returned_supercategories(declaration) if declaration else ()
                        )
                    ),
                )
            )
    return declarations


def _classes(
    tree: ast.Module,
) -> list[tuple[tuple[str, ...], ast.ClassDef]]:
    """Every class in the module, each with the class names enclosing it."""
    found: list[tuple[tuple[str, ...], ast.ClassDef]] = []

    def walk(body: list[ast.stmt], scope: tuple[str, ...]) -> None:
        for statement in body:
            if isinstance(statement, ast.ClassDef):
                found.append((scope, statement))
                walk(statement.body, (*scope, statement.name))

    walk(tree.body, ())
    return found


def render_table(declarations: list[CategoryDeclaration]) -> str:
    lines = [
        f"{len(declarations)} categories declared under the parsed tree.",
        "",
        "Each row is what the source says: the category, and the supercategories",
        "its `super_categories()` returns.  A row with no declaration inherits",
        "one; a row marked `abstract` requires its subcategories to supply one.",
        "",
    ]
    width = max((len(d.qualified_name) for d in declarations), default=0)
    for declaration in sorted(declarations, key=lambda d: d.qualified_name):
        if declaration.abstract:
            stated = "<abstract>"
        elif not declaration.declares:
            stated = "<inherited>"
        elif not declaration.supercategories:
            stated = "<none returned>"
        else:
            stated = ", ".join(d.expression for d in declaration.supercategories)
        lines.append(f"{declaration.qualified_name:<{width}}  {stated}")
    return "\n".join(lines) + "\n"


def render_by_supercategory(declarations: list[CategoryDeclaration]) -> str:
    """Group the tree the other way round: each supercategory, and who claims it."""
    claimants: dict[str, list[str]] = {}
    for declaration in declarations:
        for head in declaration.heads:
            claimants.setdefault(head, []).append(declaration.qualified_name)
    lines = [
        "Every declared supercategory, and the categories declaring it.",
        "",
        "Read a large group as one mathematical claim made many times: each",
        "member asserts that its objects are objects of the heading.",
        "",
    ]
    for head in sorted(claimants, key=lambda h: (-len(claimants[h]), h)):
        members = sorted(claimants[head])
        lines.append(f"{head}  ({len(members)})")
        for member in members:
            lines.append(f"    {member}")
        lines.append("")
    return "\n".join(lines)


def render_foreign(declarations: list[CategoryDeclaration]) -> str:
    """Owned categories that declare a Sage category as a supercategory.

    The preamble owns its categories outright, so each row places an owned
    category's objects inside a category this tree does not define, and the
    claim can only be read in Sage's source.
    """
    rows = [d for d in declarations if d.sage_supercategories]
    lines = [
        f"{len(rows)} owned categories declare a supercategory whose name is Sage's.",
        "",
    ]
    for declaration in sorted(rows, key=lambda d: d.qualified_name):
        foreign = ", ".join(s.expression for s in declaration.sage_supercategories)
        lines.append(f"{declaration.qualified_name}")
        lines.append(f"    declares  {foreign}")
        lines.append(f"    at        {declaration.path}:{declaration.line}")
        lines.append("")
    return "\n".join(lines)


def _defined_names(declarations: list[CategoryDeclaration]) -> set[str]:
    """Every category name the parsed tree binds, aliases and factories included."""
    roots = {Path(d.path).parent for d in declarations}
    bound: set[str] = set()
    for root in roots:
        for path in root.glob("*.py"):
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except (SyntaxError, OSError):
                continue
            bound |= _module_level_names(tree)
    return bound


def render_audit(declarations: list[CategoryDeclaration]) -> str:
    """The mechanically checkable defects in the declared graph.

    None of these needs a reading of what the objects are.  A name declared as
    a supercategory that nothing defines is a missing category; a declaration
    computed from a local variable is an edge this graph cannot state; a cycle
    is a contradiction outright.  What a declaration *means* is read by a
    mathematician against the category's own definition, not decided here.
    """
    declared = (
        {d.name for d in declarations}
        | {d.qualified_name for d in declarations}
        | _defined_names(declarations)
    )

    missing: dict[str, list[str]] = {}
    unstated: dict[str, list[str]] = {}
    for declaration in declarations:
        for supercategory in declaration.supercategories:
            if supercategory.origin == "expression":
                if supercategory.resolved not in declared:
                    unstated.setdefault(supercategory.expression, []).append(
                        declaration.qualified_name
                    )
            elif (
                supercategory.origin == "owned"
                and supercategory.resolved not in declared
            ):
                missing.setdefault(supercategory.resolved, []).append(
                    declaration.qualified_name
                )

    # A category may legitimately declare itself on other data: `Modules(R)`
    # declares `Modules(S)` for a restriction base ring.  That is a loop on the
    # name and not on the objects, so it is reported apart from real cycles.
    recursive = sorted(
        {d.name for d in declarations if d.name in d.heads}
    )
    edges = {d.name: set(d.heads) - {d.name} for d in declarations}
    cycles: list[str] = []
    for start in sorted(edges):
        seen: set[str] = set()
        stack = [(start, (start,))]
        while stack:
            node, path = stack.pop()
            for head in sorted(edges.get(node, ())):
                if head == start:
                    cycles.append(" -> ".join((*path, head)))
                elif head not in seen and head in edges:
                    seen.add(head)
                    stack.append((head, (*path, head)))

    lines = [
        "Mechanically checkable defects in the declared category graph.",
        "",
        f"## Named as a supercategory, defined nowhere ({len(missing)})",
        "",
    ]
    for head in sorted(missing, key=lambda h: (-len(missing[h]), h)):
        lines.append(f"{head}  <- {', '.join(sorted(missing[head]))}")
    lines += [
        "",
        f"## Declared from a local expression, so the edge is not stated ({len(unstated)})",
        "",
    ]
    for expression in sorted(unstated):
        lines.append(f"{expression}  <- {', '.join(sorted(unstated[expression]))}")
    lines += [
        "",
        f"## Declared on its own name, with other data ({len(recursive)})",
        "",
        "Legitimate where the parameter differs -- restriction of scalars, a",
        "smaller base -- and a contradiction where it does not.  Read the body.",
        "",
    ]
    lines.extend(recursive or ["none"])
    lines += ["", f"## Cycles among distinct categories ({len(cycles)})", ""]
    lines.extend(cycles or ["none"])
    return "\n".join(lines) + "\n"


def render_dot(declarations: list[CategoryDeclaration]) -> str:
    """The literal declared graph, one edge per declared supercategory."""
    declared = {d.qualified_name for d in declarations} | {d.name for d in declarations}
    lines = [
        "digraph declared_categories {",
        "  rankdir=BT;",
        '  node [shape=box, fontname="Inter"];',
    ]
    for declaration in sorted(declarations, key=lambda d: d.qualified_name):
        for head in declaration.heads:
            style = "" if head in declared else ' [style=dashed, color="#b45309"]'
            lines.append(f'  "{declaration.qualified_name}" -> "{head}"{style};')
    lines.append("}")
    return "\n".join(lines) + "\n"


def render_json(declarations: list[CategoryDeclaration]) -> str:
    payload = [
        {
            "name": d.name,
            "qualified_name": d.qualified_name,
            "source": f"{d.path}:{d.line}",
            "bases": list(d.bases),
            "summary": d.summary,
            "declares": d.declares,
            "abstract": d.abstract,
            "supercategories": [
                {"expression": s.expression, "head": s.head, "resolved": s.resolved, "origin": s.origin}
                for s in d.supercategories
            ],
            "heads": list(d.heads),
        }
        for d in sorted(declarations, key=lambda d: d.qualified_name)
    ]
    return json.dumps(payload, indent=1) + "\n"


def _default_root() -> Path:
    return Path(__file__).resolve().parents[1] / "preamble"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List every declared category and its declared supercategories, without importing the tree."
    )
    parser.add_argument("root", nargs="?", type=Path, default=_default_root())
    parser.add_argument(
        "--format",
        choices=("table", "by-supercategory", "foreign", "audit", "dot", "json"),
        default="table",
    )
    parser.add_argument("-o", "--output", type=Path)
    arguments = parser.parse_args()

    declarations = read_tree(arguments.root)
    rendered = {
        "table": render_table,
        "by-supercategory": render_by_supercategory,
        "foreign": render_foreign,
        "audit": render_audit,
        "dot": render_dot,
        "json": render_json,
    }[arguments.format](declarations)

    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
