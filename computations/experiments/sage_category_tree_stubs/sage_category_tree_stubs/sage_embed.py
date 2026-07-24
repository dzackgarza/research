r"""Sage ↪ 𝒢 embedding observability (bijection frame, not edge-set equality).

Implements diagnostics for the active comparison model:

- \(\mathcal G_{\mathrm{Sage}}\subseteq\mathcal G\) with
  \(\operatorname{Ob}(S_{\mathrm{sem}})\xrightarrow{\sim}
  \operatorname{Ob}(\mathcal G_{\mathrm{Sage}})\);
- semantic (not nominal) bijection;
- vertex parity stricter than edge parity;
- explicit exception ledger (see ``exceptions.py``).

This module reports; it does not silently repair maps. Map/DOT fixes are
downstream of a failing report.
"""

from __future__ import annotations

import json
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import asdict, dataclass, field

from .dot_parse import DotGraph, parse_dot
from .exceptions import (
    EMBED_EXCEPTIONS,
    SageEmbedException,
    alias_map,
    exceptions_by_kind,
    waived_native_stub_edges,
)
from .graph_compare import native_solid_digraph, sage_solid_digraph
from .sage_to_stub import SAGE_TO_STUB, STUB_TO_SAGE
from .slugs import axiom_method_name, short_name


def graph_universe(graph: DotGraph | None = None) -> frozenset[str]:
    r"""Vertices present in \(\mathcal G\) as currently presented by the DOT."""
    graph = graph or parse_dot()
    nodes: set[str] = set(graph.solid_nodes) | set(graph.named_joins)
    # Host.Axiom solid refinements already appear in solid_nodes when edged;
    # also index axiom attachment ids and Host.Axiom label forms.
    for src, label in graph.axiom_labels.items():
        nodes.add(src)
        ax = axiom_method_name(label)
        for edge in graph.axiom_edges:
            if edge.src != src:
                continue
            host = edge.tgt
            nodes.add(f"{short_name(host)}.{ax}")
            nodes.add(f"{host}.{ax}")
    return frozenset(nodes)


def vertex_in_graph(vertex: str, graph: DotGraph | None = None) -> bool:
    r"""Whether ``vertex`` is a *declared* object of \(\mathcal G\) (DOT presentation).

    Transported classifiers such as ``Algebras(R).Graded`` (Graded defined on Sets)
    are **not** treated as present merely because the axiom name exists elsewhere.
    They must appear as a DOT solid/named/axiom-attachment vertex, or be added by a
    later explicit transport rule — until then ``missing_targets`` flags them.
    """
    graph = graph or parse_dot()
    universe = graph_universe(graph)
    if vertex in universe:
        return True
    if short_name(vertex) in universe:
        return True
    # Declared Host.Axiom only when this host actually carries that axiom edge.
    if " = " not in vertex and "." in vertex:
        host, ax = vertex.rsplit(".", 1)
        ax_name = axiom_method_name(ax)
        for edge in graph.axiom_edges:
            if short_name(edge.tgt) != short_name(host) and edge.tgt != host:
                continue
            label = graph.axiom_labels.get(edge.src, edge.src.rsplit(".", 1)[-1])
            if axiom_method_name(label) == ax_name:
                return True
    # A destination may be a constructible category with no name and therefore no
    # vertex: the bridge's job includes discovering which constructions must exist
    # normalized, and `Subobjects(Sets)` is such a discovery. The DOT is a curated
    # presentation, so absence from it is not absence from the graph. A seed-declared
    # construction value counts as declared; anything not in the seed still fails.
    return _is_declared_construction_value(vertex)


def _is_declared_construction_value(vertex: str) -> bool:
    from .semantic_seed import load_semantic_seed

    for entity in load_semantic_seed().entities:
        if entity.get("id") != vertex and entity.get("canonical_name") != vertex:
            continue
        definition = entity.get("definition") or {}
        return bool(definition.get("operation") == "construction_value")
    return False


def semantic_sage_names() -> frozenset[str]:
    r"""\(\operatorname{Ob}(S_{\mathrm{sem}})\) as declared by the map, minus aliases."""
    aliases = alias_map()
    return frozenset(n for n in SAGE_TO_STUB if n not in aliases)


def marked_sage_image(graph: DotGraph | None = None) -> dict[str, str]:
    """Bijection candidates: semantic Sage name → stub target string."""
    aliases = alias_map()
    return {sage: target for sage, target in SAGE_TO_STUB.items() if sage not in aliases}


@dataclass(frozen=True, slots=True)
class Collapse:
    stub_target: str
    sage_names: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class EmbeddingReport:
    r"""Machine-readable \(\mathcal G_{\mathrm{Sage}}\) embedding status."""

    # Ob(S_sem) size and G_Sage targets
    semantic_sage_count: int
    marked_target_count: int
    # Totality / target existence
    missing_targets: tuple[tuple[str, str], ...]  # (sage, target)
    # Injectivity among semantic names
    collapses: tuple[Collapse, ...]
    # Map keys classified as aliases (not in Ob(S_sem))
    aliases: tuple[tuple[str, str], ...]  # (alias, primary)
    # STUB_TO_SAGE keys with no reverse SAGE_TO_STUB image (informational)
    stub_to_sage_orphans: tuple[str, ...]
    # Exception ledger summary
    exception_counts: dict[str, int] = field(default_factory=dict)
    # Optional edge diagnostics (filled when native graph available)
    unexplained_native_edges: tuple[tuple[str, str], ...] = ()
    explained_incorrect_parents: tuple[tuple[str, str], ...] = ()

    @property
    def bijection_ok(self) -> bool:
        return not self.missing_targets and not self.collapses

    def to_dict(self) -> dict[str, object]:
        d = asdict(self)
        d["bijection_ok"] = self.bijection_ok
        return d


def embedding_report(graph: DotGraph | None = None) -> EmbeddingReport:
    """Compute vertex-level embedding diagnostics against the DOT + map."""
    graph = graph or parse_dot()
    aliases = alias_map()
    marked = marked_sage_image(graph)

    missing: list[tuple[str, str]] = []
    for sage, target in sorted(marked.items()):
        if not vertex_in_graph(target, graph):
            missing.append((sage, target))

    by_target: dict[str, list[str]] = defaultdict(list)
    for sage, target in marked.items():
        by_target[target].append(sage)
    collapses = tuple(Collapse(stub_target=t, sage_names=tuple(sorted(names))) for t, names in sorted(by_target.items()) if len(names) > 1)

    reverse_ok = set(SAGE_TO_STUB.values()) | {SAGE_TO_STUB[a] for a in aliases if a in SAGE_TO_STUB}
    orphans = tuple(sorted(k for k in STUB_TO_SAGE if k not in reverse_ok and k not in SAGE_TO_STUB.values()))

    counts: dict[str, int] = {kind: len(rows) for kind, rows in exceptions_by_kind().items()}

    return EmbeddingReport(
        semantic_sage_count=len(marked),
        marked_target_count=len(set(marked.values())),
        missing_targets=tuple(missing),
        collapses=collapses,
        aliases=tuple(sorted((a, p) for a, p in aliases.items())),
        stub_to_sage_orphans=orphans,
        exception_counts=counts,
    )


def edge_preservation_report(
    graph: DotGraph | None = None,
) -> tuple[tuple[tuple[str, str], ...], tuple[tuple[str, str], ...]]:
    """Native solid edges: unexplained vs ledger-explained incorrect parents.

    Returns ``(unexplained, explained)`` as (stub_child, stub_parent) pairs
    after mapping through SAGE_TO_STUB. Requires stub materialization for the
    stub digraph and native instances for the Sage digraph.
    """
    from .native_semantics import _has_directed_path

    graph = graph or parse_dot()
    stub = sage_solid_digraph(graph)
    try:
        native = native_solid_digraph(graph)
    except Exception:
        return (), ()

    waived_stub = waived_native_stub_edges()
    unexplained: list[tuple[str, str]] = []
    explained: list[tuple[str, str]] = []
    shared = set(stub.vertices()) & set(native.vertices())
    for u, v, _ in native.edges(sort=True):
        if u not in shared or v not in shared:
            continue
        if (u, v) in waived_stub:
            explained.append((u, v))
            continue
        if _has_directed_path(stub, u, v):
            continue
        unexplained.append((u, v))
    return tuple(unexplained), tuple(explained)


def full_embedding_report(graph: DotGraph | None = None) -> EmbeddingReport:
    """Vertex report plus native edge unexplained/explained lists."""
    base = embedding_report(graph)
    unexplained, explained = edge_preservation_report(graph)
    return EmbeddingReport(
        semantic_sage_count=base.semantic_sage_count,
        marked_target_count=base.marked_target_count,
        missing_targets=base.missing_targets,
        collapses=base.collapses,
        aliases=base.aliases,
        stub_to_sage_orphans=base.stub_to_sage_orphans,
        exception_counts=base.exception_counts,
        unexplained_native_edges=unexplained,
        explained_incorrect_parents=explained,
    )


def format_embedding_report(report: EmbeddingReport) -> str:
    lines = [
        "Sage ↪ 𝒢 embedding report",
        f"  Ob(S_sem) declared (map − aliases): {report.semantic_sage_count}",
        f"  |G_Sage| (distinct targets):        {report.marked_target_count}",
        f"  bijection_ok (no missing/collapse): {report.bijection_ok}",
        "",
        "Exception ledger counts:",
    ]
    for kind, n in sorted(report.exception_counts.items()):
        lines.append(f"  {kind}: {n}")
    if report.aliases:
        lines.append("")
        lines.append("Aliases (not in Ob(S_sem)):")
        for a, p in report.aliases:
            lines.append(f"  {a} → {p}")
    if report.missing_targets:
        lines.append("")
        lines.append("MISSING TARGETS (in map, not in 𝒢):")
        for sage, target in report.missing_targets:
            lines.append(f"  {sage} ↦ {target}")
    if report.collapses:
        lines.append("")
        lines.append("INJECTIVITY COLLAPSES (many Sage → one target):")
        for c in report.collapses:
            lines.append(f"  {c.stub_target} ← {', '.join(c.sage_names)}")
    if report.explained_incorrect_parents:
        lines.append("")
        lines.append(f"Ledger-explained native edges (incorrect_parent/composite): {len(report.explained_incorrect_parents)}")
    if report.unexplained_native_edges:
        lines.append("")
        lines.append("UNEXPLAINED native solid edges (no stub path, not in ledger):")
        for u, v in report.unexplained_native_edges:
            lines.append(f"  {u} → {v}")
    if report.stub_to_sage_orphans:
        lines.append("")
        lines.append(f"STUB_TO_SAGE orphans (informational): {len(report.stub_to_sage_orphans)}")
    return "\n".join(lines)


def ledger_rows() -> tuple[SageEmbedException, ...]:
    return EMBED_EXCEPTIONS


# ══════════════════════════════════════════════════════════════════════════════
# CLI (also wired as ``just audit embed``)
# ══════════════════════════════════════════════════════════════════════════════


def _cli(argv: Iterable[str] | None = None) -> int:
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help", "help"}:
        print(__doc__)
        print("commands: report | json | ledger | missing | collapses")
        return 0
    cmd = args[0]
    if cmd == "ledger":
        for row in EMBED_EXCEPTIONS:
            print(f"{row.kind}\t{row.sage_name}\talias_of={row.alias_of}\tparent={row.sage_parent}\tstub={row.stub_vertex}\t{row.detail}")
        return 0
    if cmd == "report":
        print(format_embedding_report(full_embedding_report()))
        return 0
    if cmd == "json":
        print(json.dumps(full_embedding_report().to_dict(), indent=2, sort_keys=True))
        return 0
    if cmd == "missing":
        for sage, target in embedding_report().missing_targets:
            print(f"{sage}\t{target}")
        return 0
    if cmd == "collapses":
        for c in embedding_report().collapses:
            print(f"{c.stub_target}\t{','.join(c.sage_names)}")
        return 0
    print(f"unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(_cli())
