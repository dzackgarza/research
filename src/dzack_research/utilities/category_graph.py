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


def _imported_names(tree: ast.Module) -> dict[str, str]:
    """Map each imported name to the module it was imported from."""
    origins: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                origins[alias.asname or alias.name] = node.module
        elif isinstance(node, ast.Import):
            for alias in node.names:
                origins[alias.asname or alias.name.split(".")[0]] = alias.name
    return origins


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


def _origin(head: str, imported: dict[str, str], known: set[str]) -> str:
    """Say where a declared supercategory's name comes from."""
    module = imported.get(head)
    if module is not None and module.split(".")[0] == "sage":
        return "sage"
    if head in known or module is not None:
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
                {"expression": s.expression, "head": s.head, "origin": s.origin}
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
        choices=("table", "by-supercategory", "foreign", "dot", "json"),
        default="table",
    )
    parser.add_argument("-o", "--output", type=Path)
    arguments = parser.parse_args()

    declarations = read_tree(arguments.root)
    rendered = {
        "table": render_table,
        "by-supercategory": render_by_supercategory,
        "foreign": render_foreign,
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
