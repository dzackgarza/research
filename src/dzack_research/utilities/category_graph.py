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

from sage.graphs.digraph import DiGraph
from sage.graphs.graph import Graph
from sage.topology.simplicial_complex import SimplicialComplex

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
    }
)

DECLARATIONS = ("super_categories", "extra_super_categories")


def _vertex(base: str, axioms: tuple[str, ...]) -> str:
    """The graph vertex of a category with axioms: ``Base.Axiom1.Axiom2``, sorted.

    Sage's ``Base().A().B()`` is the join of ``Base.A`` and ``Base.B``, one
    category whichever order the axioms are applied in.
    """
    return ".".join((base, *sorted(axioms)))


@dataclass(frozen=True)
class Supercategory:
    """One declared supercategory, and where its name comes from."""

    expression: str
    head: str
    resolved: str  # the head with any import alias followed back to its name
    origin: str  # "owned", "sage", or "expression"
    axioms: tuple[str, ...] = ()

    @property
    def vertex(self) -> str:
        return _vertex(self.resolved, self.axioms)


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
    axiom_of: str = ""  # for a nested axiom class, the category it refines

    @property
    def vertex(self) -> str:
        if not self.axiom_of:
            return self.name
        return _vertex(self.axiom_of, tuple(self.qualified_name.split(".")[1:]))

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
    stripped = _without_axioms(expression).split("(", 1)[0]
    return stripped.rsplit(".", 1)[-1].strip()


def _axiom_calls(expression: str) -> tuple[ast.expr, tuple[str, ...]]:
    """Split ``Base(R).A().B()`` into the base expression and its axiom names.

    An axiom is applied as a capitalised zero-argument method (Sage's
    ``with_axiom`` accessors); anything else ends the chain.
    """
    try:
        node: ast.expr = ast.parse(expression, mode="eval").body
    except SyntaxError:
        return ast.Name(id=expression), ()
    axioms: list[str] = []
    while (
        isinstance(node, ast.Call)
        and not node.args
        and not node.keywords
        and isinstance(node.func, ast.Attribute)
        and node.func.attr[:1].isupper()
    ):
        axioms.append(node.func.attr)
        node = node.func.value
    return node, tuple(reversed(axioms))


def _without_axioms(expression: str) -> str:
    base, _ = _axiom_calls(expression)
    return ast.unparse(base)


def _axioms(expression: str) -> tuple[str, ...]:
    _, axioms = _axiom_calls(expression)
    return axioms


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


def _declarations(node: ast.ClassDef) -> list[ast.FunctionDef]:
    """The methods declaring supercategories: ``super_categories`` and, on an
    axiom class, ``extra_super_categories`` (Sage adds the rest itself)."""
    return [
        statement
        for statement in node.body
        if isinstance(statement, ast.FunctionDef) and statement.name in DECLARATIONS
    ]


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
            declaring = _declarations(node)
            declarations.append(
                CategoryDeclaration(
                    name=node.name,
                    qualified_name=".".join((*scope, node.name)),
                    path=str(path),
                    line=node.lineno,
                    bases=tuple(_head(ast.unparse(base)) for base in node.bases),
                    summary=_summary(node),
                    declares=bool(declaring),
                    abstract=any(_is_abstract(d) for d in declaring),
                    supercategories=tuple(
                        Supercategory(
                            expression=expression,
                            head=_head(expression),
                            resolved=_resolved(_head(expression), imported),
                            origin=_origin(_head(expression), imported, known),
                            axioms=_axioms(expression),
                        )
                        for declaration in declaring
                        for expression in _returned_supercategories(declaration)
                    ),
                    # A class nested in a category and based on CategoryWithAxiom
                    # is that category with the axioms the nesting names.
                    axiom_of=scope[0] if scope and scope[0] in known else "",
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

    # A category declaring its own name over other data (`Modules(R)` declaring
    # `Modules(S)`) is a restriction-of-scalars edge, ruled out on 2026-09-16
    # because Sage applies every axiom along it; reported apart from cycles
    # because it is a loop on the name, not on the objects.
    recursive = sorted({d.name for d in declarations if d.name in d.heads})
    # A strongly connected component with more than one category is a set of
    # categories each declared to lie under the others.
    cycles = [
        ", ".join(sorted(component))
        for component in _digraph(_declared_edges(declarations)).strongly_connected_components()
        if len(component) > 1
    ]

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
        "A restriction-of-scalars edge, which Sage applies every axiom along;",
        "restriction is a functor, never a declaration (AGENTS.md, Red flags).",
        "",
    ]
    lines.extend(recursive or ["none"])
    lines += ["", f"## Cycles among distinct categories ({len(cycles)})", ""]
    lines.extend(cycles or ["none"])
    return "\n".join(lines) + "\n"


def _declared_edges(
    declarations: list[CategoryDeclaration],
) -> set[tuple[str, str]]:
    """Edges between categories this tree defines, self-declaration dropped.

    An axiom category ``Base.A.B`` is the join of ``Base.A`` and ``Base.B``
    (Sage's axiom semantics), so every axiom vertex, declared or merely named,
    also declares each vertex with one axiom fewer.
    """
    names = {d.name for d in declarations}
    return {
        (d.vertex, supercategory.vertex)
        for d in declarations
        for supercategory in d.supercategories
        if supercategory.resolved in names and supercategory.vertex != d.vertex
    }


def _axiom_edges(
    declarations: list[CategoryDeclaration], declared: set[tuple[str, str]]
) -> set[tuple[str, str]]:
    """The edges Sage's join supplies: each axiom vertex declares every vertex
    with one axiom fewer, down to the base.  These are computed, not written."""
    pending = {v for edge in declared for v in edge if "." in v} | {
        d.vertex for d in declarations if d.axiom_of
    }
    edges: set[tuple[str, str]] = set()
    while pending:
        vertex = pending.pop()
        base, *axioms = vertex.split(".")
        for dropped in axioms:
            below = _vertex(base, tuple(a for a in axioms if a != dropped))
            if (vertex, below) not in edges:
                edges.add((vertex, below))
                if "." in below:
                    pending.add(below)
    return edges


def _all_edges(declarations: list[CategoryDeclaration]) -> set[tuple[str, str]]:
    declared = _declared_edges(declarations)
    return declared | _axiom_edges(declarations, declared)


def _base_of(vertex: str) -> str:
    return vertex.split(".", 1)[0]


def _graph(edges: set[tuple[str, str]]) -> Graph:
    return Graph(sorted(edges))


def _digraph(edges: set[tuple[str, str]]) -> DiGraph:
    return DiGraph(sorted(edges))


def _shortcuts(declarations: list[CategoryDeclaration]) -> list[tuple[str, str]]:
    """Written declarations a longer path already gives.

    The reduction runs over the written and the computed edges together, so a
    computed edge parallel to a written path is never reported: Sage's join
    drops it itself.
    """
    declared = _declared_edges(declarations)
    reduction = set(_digraph(_all_edges(declarations)).transitive_reduction().edges(labels=False))
    return sorted(declared - reduction)


def _chains_above(directed: DiGraph) -> dict[str, int]:
    """The longest chain of declarations above each category.

    ``level_sets()`` of the reversed graph puts a category in level ``k`` when
    its longest path to a maximal category has ``k`` declarations (Sage's
    ``DiGraph.level_sets``, linear time).  ``longest_path()`` is a MILP by
    default; see ``TRAPS.md``.
    """
    return {
        name: level
        for level, names in enumerate(directed.reverse().level_sets())
        for name in names
    }


def _in_cyclic_order(graph: Graph, cycle: list[str]) -> list[str]:
    """Order a cycle's vertices around it.

    Sage's ``minimum_cycle_basis`` returns each cycle as a vertex set, not in
    cyclic order (``sage.graphs.base.boost_graph.min_cycle_basis``).
    """
    induced = graph.subgraph(cycle).cycle_basis()
    return induced[0] if len(induced) == 1 else sorted(cycle)


def _minimum_cycle_basis(graph: Graph) -> list[list[str]]:
    """Sage's default minimum cycle basis takes integer vertices only; relabel.

    Wall time on the declared graph is in ``TRAPS.md``.
    """
    relabelled = graph.copy()
    names = relabelled.relabel(return_map=True)
    back = {integer: name for name, integer in names.items()}
    return [
        _in_cyclic_order(graph, [back[v] for v in cycle])
        for cycle in relabelled.minimum_cycle_basis()
    ]


def _blocks(graph: Graph) -> list[list[str]]:
    """The 2-connected blocks holding at least one cycle, largest first.

    The cycle space is the direct sum of the blocks' cycle spaces, so every
    generator lies inside one block.  A near-tree has only small blocks.
    """
    blocks, _ = graph.blocks_and_cut_vertices()
    return sorted((sorted(b) for b in blocks if len(b) >= 3), key=len, reverse=True)


def render_shape(declarations: list[CategoryDeclaration]) -> str:
    """Breadth, depth and shortcuts.  The intended shape is deep and narrow."""
    edges = _all_edges(declarations)
    directed = _digraph(edges)
    breadth = directed.in_degree(labels=True)
    depth = _chains_above(directed)

    lines = [
        "The declared graph as numbers.  Intended shape: near-tree, deep and narrow.",
        "",
        (
            f"categories {directed.order()}   "
            f"declarations {directed.size()}   "
            f"pieces {_graph(edges).connected_components_number()}"
        ),
        f"longest chain of declarations = {max(depth.values(), default=0)}",
        "",
        "## Breadth: categories declared directly by the most others",
        "",
        "Each count is the number of unfactored declarations into that node,",
        "unless every claimant's own definition places it one step below.",
        "",
    ]
    for name in sorted(breadth, key=lambda n: (-breadth[n], n))[:15]:
        if breadth[name]:
            lines.append(f"{breadth[name]:5d}  {name}")

    histogram: dict[int, int] = {}
    for value in depth.values():
        histogram[value] = histogram.get(value, 0) + 1
    lines += ["", "## Depth: longest chain above each category", ""]
    for value in sorted(histogram):
        lines.append(f"  depth {value:2d}: {histogram[value]:4d} categories")

    shortcuts = _shortcuts(declarations)
    lines += [
        "",
        f"## Shortcut declarations, dropped by the transitive reduction ({len(shortcuts)})",
        "",
    ]
    lines.extend(f"{below} -> {above}" for below, above in shortcuts)
    return "\n".join(lines) + "\n"


def render_cells(declarations: list[CategoryDeclaration]) -> str:
    r"""Homology of the declaration graph, and the cycles owing a 2-cell.

    Each generator is two routes between the same pair of categories, asserted
    to be the same composite of forgetful functors; nothing in the source
    proves it.  Homology is unreduced (Sage's default is reduced).
    """
    edges = _all_edges(declarations)
    graph = _graph(edges)
    homology = SimplicialComplex([list(edge) for edge in edges]).homology(reduced=False)
    blocks = _blocks(graph)
    shortcuts = _shortcuts(declarations)
    dropped = {frozenset(edge) for edge in shortcuts}

    def through_a_shortcut(cycle: list[str]) -> bool:
        return any(frozenset(pair) in dropped for pair in zip(cycle, cycle[1:] + cycle[:1]))

    def is_axiom_join(cycle: list[str]) -> bool:
        # Every vertex is one base with a subset of its axioms: Sage computes
        # this join, so the two routes are the same functor by construction.
        return len({_base_of(v) for v in cycle}) == 1

    lines = [
        "Homology of the declaration graph.",
        "",
        f"  0-cells {graph.order()}    1-cells {graph.size()}    2-cells 0",
        f"  H_0 = {homology[0]}    H_1 = {homology[1]}    H_n = 0, n >= 2",
        "",
        f"## 2-connected blocks with a cycle ({len(blocks)}), by size",
        "",
        "Every generator lies inside one block.  A near-tree has only small",
        "blocks; a large block is the region where declarations form a mesh.",
        "",
    ]
    lines.extend(f"{len(block):5d}  {', '.join(block)}" for block in blocks)
    lines += ["", f"## Killed by deleting one declaration ({len(shortcuts)})", ""]
    lines.extend(f"{below} -> {above}" for below, above in shortcuts)

    for block in blocks:
        basis = _minimum_cycle_basis(graph.subgraph(block))
        joins = [c for c in basis if is_axiom_join(c)]
        remaining = [c for c in basis if not is_axiom_join(c) and not through_a_shortcut(c)]
        lines += [
            "",
            f"## Computed axiom joins, in the block of {len(block)} ({len(joins)})",
            "",
        ]
        lines.extend(" -> ".join(c + c[:1]) for c in sorted(joins, key=lambda c: (len(c), c)))
        lines += [
            "",
            f"## Owing a real 2-cell, in the block of {len(block)} ({len(remaining)})",
            "",
        ]
        lines.extend(" -> ".join(c + c[:1]) for c in sorted(remaining, key=lambda c: (len(c), c)))
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
        choices=(
            "table",
            "by-supercategory",
            "foreign",
            "audit",
            "shape",
            "cells",
            "dot",
            "json",
        ),
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
        "shape": render_shape,
        "cells": render_cells,
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
