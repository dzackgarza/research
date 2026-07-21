"""Observability and audits for the category parent DOT graph and stubs.

Large-scale questions this module answers:

1. What are all axioms, and where is each *first* defined?
2. What axioms are *attached* to a category (declared on it)?
3. What axioms are *available* on a category (attached + inherited from
   less-structured solid ancestors)?
4. What are all solid forgetful paths from a category down to bedrock
   (vertices with no solid parents — typically ``CatObject``)?

Also: per-axiom lower-host candidates, named joins, Hasse defects,
Sage ↪ 𝒢 embedding (``embed`` / ``ledger``), three-layer naming (``naming``).

Usage::

    just audit axioms
    just audit axiom Finite
    just audit category Rings
    just audit paths Fields
    just audit summary
    just audit json
    just audit hasse
    just audit embed
    just audit ledger
    just audit naming
    just audit layers
    just audit design
"""

from __future__ import annotations

import json
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass

from .dot_parse import DotGraph, Edge, parse_dot
from .slugs import axiom_method_name, short_name

#══════════════════════════════════════════════════════════════════════════════
# Graph primitives
#══════════════════════════════════════════════════════════════════════════════


def _solid_parent_map(graph: DotGraph) -> dict[str, tuple[str, ...]]:
    parents: dict[str, list[str]] = defaultdict(list)
    for edge in graph.solid_edges:
        parents[edge.src].append(edge.tgt)
    return {node: tuple(dict.fromkeys(ps)) for node, ps in parents.items()}


def resolve_vertex(node: str, graph: DotGraph | None = None) -> str:
    """Map a short name / alias to a solid DOT vertex when unambiguous."""
    graph = graph or parse_dot()
    if node in graph.solid_nodes or node in graph.named_joins:
        return node
    matches = sorted(
        (
            n
            for n in set(graph.solid_nodes) | set(graph.named_joins)
            if short_name(n) == short_name(node) or short_name(n) == node
        ),
        key=str,
    )
    if len(matches) == 1:
        return matches[0]
    if node in matches:
        return node
    return node


def solid_ancestors(node: str, graph: DotGraph | None = None) -> tuple[str, ...]:
    """Categories strictly less structured than ``node`` (solid-parent closure)."""
    graph = graph or parse_dot()
    node = resolve_vertex(node, graph)
    parents = _solid_parent_map(graph)
    seen: set[str] = set()
    stack = list(parents.get(node, ()))
    order: list[str] = []
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        order.append(cur)
        stack.extend(parents.get(cur, ()))
    return tuple(order)


def solid_ancestry_depth(
    node: str, graph: DotGraph | None = None
) -> dict[str, int]:
    """Ancestor → shortest solid-path length from ``node`` (1 = immediate parent)."""
    graph = graph or parse_dot()
    node = resolve_vertex(node, graph)
    parents = _solid_parent_map(graph)
    depth: dict[str, int] = {}
    queue: list[tuple[str, int]] = [(p, 1) for p in parents.get(node, ())]
    while queue:
        cur, d = queue.pop(0)
        if cur in depth and depth[cur] <= d:
            continue
        depth[cur] = d
        for p in parents.get(cur, ()):
            queue.append((p, d + 1))
    return depth


def bedrock_vertices(graph: DotGraph | None = None) -> tuple[str, ...]:
    """Forgetful sinks: solid vertices with no solid parent, excluding axiom nodes.

    ``Sets.Finite`` / ``Magmas.Additive`` / ``ax.Domain`` attach by dotted edges, so
    they have no *solid* parent and would otherwise look like bedrock. Real bedrock
    is typically ``CatObject`` (and any other plain root).
    """
    graph = graph or parse_dot()
    parents = _solid_parent_map(graph)
    axiomish = set(graph.axiom_labels) | {e.src for e in graph.declared_axiom_edges}
    # Host.Axiom solid ids (Sets.Countable, Lat.Definite, …)
    for node in graph.solid_nodes:
        if " = " in node or node.count(".") != 1:
            continue
        _host, ax = node.split(".", 1)
        if axiom_method_name(ax) in declared_axiom_hosts(graph):
            axiomish.add(node)
    return tuple(
        sorted(
            (n for n in graph.solid_nodes if not parents.get(n) and n not in axiomish),
            key=str,
        )
    )


def _forgetful_parents(
    node: str, graph: DotGraph, parents: dict[str, tuple[str, ...]]
) -> tuple[str, ...]:
    """Solid parents, plus the host of an axiom-refinement node (dotted attachment)."""
    out: list[str] = list(parents.get(node, ()))
    for edge in graph.declared_axiom_edges:
        if edge.src == node and edge.tgt not in out:
            out.append(edge.tgt)
    # Host.Axiom ids whose host edge may be classified only as legacy-dotted
    if " = " not in node and node.count(".") == 1:
        host, _ax = node.split(".", 1)
        # resolve Schemes / Lat aliases appearing as edge targets
        for edge in graph.edges:
            if edge.src == node and edge.tgt not in out:
                # prefer host-looking targets
                if edge.tgt == host or short_name(edge.tgt) == host or edge.style_dotted:
                    out.append(edge.tgt)
    return tuple(dict.fromkeys(out))


def paths_to_bedrock(
    node: str, graph: DotGraph | None = None, *, limit: int = 256
) -> tuple[tuple[str, ...], ...]:
    """All simple forgetful paths from ``node`` down to a bedrock vertex.

    Follows solid child→parent edges; when a Host.Axiom refinement has no solid
    parent, continues through its dotted host attachment (``Magmas.Additive`` →
    ``Magmas`` → … → ``CatObject``).
    """
    graph = graph or parse_dot()
    node = resolve_vertex(node, graph)
    parents = _solid_parent_map(graph)
    beds = set(bedrock_vertices(graph))
    if node in beds:
        return ((node,),)

    paths: list[tuple[str, ...]] = []
    stack: list[tuple[str, ...]] = [(node,)]
    while stack and len(paths) < limit:
        path = stack.pop()
        cur = path[-1]
        nexts = _forgetful_parents(cur, graph, parents)
        if not nexts:
            if cur in beds:
                paths.append(path)
            continue
        for parent in reversed(nexts):
            if parent in path:
                continue
            stack.append(path + (parent,))
    # keep only paths that terminate at bedrock
    paths = [p for p in paths if p[-1] in beds]
    paths.sort(key=lambda p: (len(p), p))
    return tuple(paths)


#══════════════════════════════════════════════════════════════════════════════
# Axiom catalog
#══════════════════════════════════════════════════════════════════════════════


def _axiom_label(edge: Edge, graph: DotGraph) -> str:
    raw = graph.axiom_labels.get(edge.src, edge.src.rsplit(".", 1)[-1])
    return axiom_method_name(raw)


def declared_axiom_hosts(
    graph: DotGraph | None = None,
) -> dict[str, tuple[str, ...]]:
    """Axiom name → hosts of explicit ``style=dotted`` attachments."""
    graph = graph or parse_dot()
    hosts: dict[str, list[str]] = defaultdict(list)
    for edge in graph.declared_axiom_edges:
        hosts[_axiom_label(edge, graph)].append(edge.tgt)
    return {
        ax: tuple(sorted(dict.fromkeys(hs), key=str)) for ax, hs in hosts.items()
    }


def all_axioms(graph: DotGraph | None = None) -> tuple[str, ...]:
    """Every axiom name declared by a ``style=dotted`` edge, sorted."""
    return tuple(sorted(declared_axiom_hosts(graph)))


def axiom_node_ids_for(
    axiom: str, graph: DotGraph | None = None
) -> tuple[str, ...]:
    graph = graph or parse_dot()
    ax = axiom_method_name(axiom)
    nodes: list[str] = []
    for edge in graph.declared_axiom_edges:
        if _axiom_label(edge, graph) == ax:
            nodes.append(edge.src)
    for node_id, label in graph.axiom_labels.items():
        if axiom_method_name(label) == ax and node_id not in nodes:
            nodes.append(node_id)
    return tuple(sorted(dict.fromkeys(nodes), key=str))


def named_joins_using_axiom(
    axiom: str, graph: DotGraph | None = None
) -> tuple[str, ...]:
    graph = graph or parse_dot()
    ax = axiom_method_name(axiom)
    return tuple(
        sorted(
            (
                join
                for join, (_host, path) in graph.named_joins.items()
                if ax in {axiom_method_name(p) for p in path}
            ),
            key=str,
        )
    )


def first_defined_hosts(
    axiom: str, graph: DotGraph | None = None
) -> tuple[str, ...]:
    """Declared hosts that do not sit above another declared host of the same name.

    If ``Finite`` is declared on both ``Sets`` and ``Schemes(S)``, and ``Sets``
    is a solid ancestor of ``Schemes(S)``, then ``Sets`` is first-defined and
    ``Schemes(S)`` is a higher re-declaration (often a *different* meaning —
    see ``redeclared_hosts``).
    """
    graph = graph or parse_dot()
    hosts = declared_axiom_hosts(graph).get(axiom_method_name(axiom), ())
    first: list[str] = []
    for host in hosts:
        ancestors = set(solid_ancestors(host, graph))
        if any(other in ancestors for other in hosts if other != host):
            continue
        first.append(host)
    return tuple(first)


def redeclared_hosts(
    axiom: str, graph: DotGraph | None = None
) -> tuple[tuple[str, tuple[str, ...]], ...]:
    """Hosts that re-declare ``axiom`` above a lower declared host of the same name.

    Each entry is ``(host, lower_declared_hosts_in_ancestry)``.
    """
    graph = graph or parse_dot()
    hosts = declared_axiom_hosts(graph).get(axiom_method_name(axiom), ())
    out: list[tuple[str, tuple[str, ...]]] = []
    for host in hosts:
        ancestors = set(solid_ancestors(host, graph))
        below = tuple(sorted((h for h in hosts if h != host and h in ancestors), key=str))
        if below:
            out.append((host, below))
    return tuple(out)


@dataclass(frozen=True)
class AxiomSiting:
    """Where an axiom sits, first definition sites, and lower candidates."""

    axiom: str
    declared_hosts: tuple[str, ...]
    first_defined_on: tuple[str, ...]
    redeclared_on: tuple[tuple[str, tuple[str, ...]], ...]
    lower_by_host: tuple[tuple[str, tuple[str, ...]], ...]
    named_joins: tuple[str, ...]
    axiom_node_ids: tuple[str, ...]

    @property
    def possible_lower_hosts(self) -> tuple[str, ...]:
        seen: set[str] = set()
        out: list[str] = []
        for _host, lowers in self.lower_by_host:
            for node in lowers:
                if node not in seen:
                    seen.add(node)
                    out.append(node)
        return tuple(out)


def axiom_siting(axiom: str, graph: DotGraph | None = None) -> AxiomSiting:
    graph = graph or parse_dot()
    ax = axiom_method_name(axiom)
    hosts = declared_axiom_hosts(graph).get(ax, ())
    lower_by_host: list[tuple[str, tuple[str, ...]]] = []
    for host in hosts:
        depths = solid_ancestry_depth(host, graph)
        ordered = tuple(
            anc for anc, _d in sorted(depths.items(), key=lambda kv: (kv[1], str(kv[0])))
        )
        lower_by_host.append((host, ordered))
    return AxiomSiting(
        axiom=ax,
        declared_hosts=hosts,
        first_defined_on=first_defined_hosts(ax, graph),
        redeclared_on=redeclared_hosts(ax, graph),
        lower_by_host=tuple(lower_by_host),
        named_joins=named_joins_using_axiom(ax, graph),
        axiom_node_ids=axiom_node_ids_for(ax, graph),
    )


def all_axiom_sitings(graph: DotGraph | None = None) -> dict[str, AxiomSiting]:
    graph = graph or parse_dot()
    return {ax: axiom_siting(ax, graph) for ax in all_axioms(graph)}


def multi_hosted_axioms(graph: DotGraph | None = None) -> dict[str, tuple[str, ...]]:
    return {
        ax: hosts
        for ax, hosts in declared_axiom_hosts(graph).items()
        if len(hosts) > 1
    }


#══════════════════════════════════════════════════════════════════════════════
# Per-category axiom views
#══════════════════════════════════════════════════════════════════════════════


@dataclass(frozen=True)
class AxiomSource:
    axiom: str
    origin: str
    """``attached`` | ``inherited`` | ``named_join``."""
    via: str
    """Host or named-join vertex that contributes the axiom."""


@dataclass(frozen=True)
class CategoryAxiomView:
    """Attached vs available axioms on one category vertex."""

    category: str
    attached: tuple[str, ...]
    """Declared on this vertex by ``style=dotted``."""

    named_join_axioms: tuple[str, ...]
    """If this vertex is a named join, axioms in its path."""

    inherited: tuple[str, ...]
    """Declared on a solid ancestor (available by forgetful inheritance)."""

    available: tuple[str, ...]
    """``attached ∪ named_join_axioms ∪ inherited``."""

    sources: tuple[AxiomSource, ...]
    """Provenance for each available axiom (may list several origins)."""


def axioms_attached(category: str, graph: DotGraph | None = None) -> tuple[str, ...]:
    graph = graph or parse_dot()
    cat = resolve_vertex(category, graph)
    return tuple(
        sorted(
            {
                _axiom_label(e, graph)
                for e in graph.declared_axiom_edges
                if e.tgt == cat
            },
            key=str,
        )
    )


def axioms_from_named_join(
    category: str, graph: DotGraph | None = None
) -> tuple[str, ...]:
    graph = graph or parse_dot()
    cat = resolve_vertex(category, graph)
    if cat not in graph.named_joins:
        return ()
    _host, path = graph.named_joins[cat]
    return tuple(dict.fromkeys(axiom_method_name(p) for p in path))


def axioms_inherited(category: str, graph: DotGraph | None = None) -> tuple[str, ...]:
    """Axioms declared on solid ancestors of ``category``."""
    graph = graph or parse_dot()
    cat = resolve_vertex(category, graph)
    hosts = declared_axiom_hosts(graph)
    # invert: host → axioms
    on_host: dict[str, set[str]] = defaultdict(set)
    for ax, hs in hosts.items():
        for h in hs:
            on_host[h].add(ax)
    inherited: set[str] = set()
    for anc in solid_ancestors(cat, graph):
        inherited |= on_host.get(anc, set())
    # do not count axioms also attached here as "inherited"
    inherited -= set(axioms_attached(cat, graph))
    return tuple(sorted(inherited, key=str))


def category_axiom_view(
    category: str, graph: DotGraph | None = None
) -> CategoryAxiomView:
    graph = graph or parse_dot()
    cat = resolve_vertex(category, graph)
    attached = axioms_attached(cat, graph)
    join_axs = axioms_from_named_join(cat, graph)
    inherited = axioms_inherited(cat, graph)
    available = tuple(
        sorted(set(attached) | set(join_axs) | set(inherited), key=str)
    )

    hosts = declared_axiom_hosts(graph)
    on_host: dict[str, set[str]] = defaultdict(set)
    for ax, hs in hosts.items():
        for h in hs:
            on_host[h].add(ax)

    sources: list[AxiomSource] = []
    for ax in attached:
        sources.append(AxiomSource(axiom=ax, origin="attached", via=cat))
    for ax in join_axs:
        sources.append(AxiomSource(axiom=ax, origin="named_join", via=cat))
    for anc in solid_ancestors(cat, graph):
        for ax in sorted(on_host.get(anc, ()), key=str):
            if ax in attached:
                continue
            sources.append(AxiomSource(axiom=ax, origin="inherited", via=anc))
    sources.sort(key=lambda s: (s.axiom, s.origin, s.via))

    return CategoryAxiomView(
        category=cat,
        attached=attached,
        named_join_axioms=join_axs,
        inherited=inherited,
        available=available,
        sources=tuple(sources),
    )


# Back-compat alias used by earlier CLI / tests
def axioms_on_host(host: str, graph: DotGraph | None = None) -> CategoryAxiomView:
    return category_axiom_view(host, graph)


#══════════════════════════════════════════════════════════════════════════════
# Hasse
#══════════════════════════════════════════════════════════════════════════════


def hasse_nonminimal_edges(graph: DotGraph | None = None) -> tuple[Edge, ...]:
    """Solid edges ``A → C`` for which a longer solid path ``A ↝ C`` also exists."""
    graph = graph or parse_dot()
    parents = _solid_parent_map(graph)
    out: list[Edge] = []
    for edge in graph.solid_edges:
        stack = [p for p in parents.get(edge.src, ()) if p != edge.tgt]
        seen: set[str] = set()
        found = False
        while stack and not found:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            if cur == edge.tgt:
                found = True
                break
            stack.extend(parents.get(cur, ()))
        if found:
            out.append(edge)
    return tuple(out)


#══════════════════════════════════════════════════════════════════════════════
# Machine-readable dump
#══════════════════════════════════════════════════════════════════════════════


def audit_catalog(graph: DotGraph | None = None) -> dict[str, object]:
    """Full JSON-serializable catalog for large-scale inspection."""
    graph = graph or parse_dot()
    sitings = all_axiom_sitings(graph)
    categories = sorted(set(graph.solid_nodes) | set(graph.named_joins), key=str)
    return {
        "bedrock": list(bedrock_vertices(graph)),
        "counts": {
            "solid_nodes": len(graph.solid_nodes),
            "solid_edges": len(graph.solid_edges),
            "named_joins": len(graph.named_joins),
            "axioms": len(sitings),
            "multi_hosted_axioms": len(multi_hosted_axioms(graph)),
            "non_hasse_edges": len(hasse_nonminimal_edges(graph)),
        },
        "axioms": {
            ax: {
                "first_defined_on": list(s.first_defined_on),
                "declared_hosts": list(s.declared_hosts),
                "redeclared_on": [
                    {"host": h, "above": list(below)} for h, below in s.redeclared_on
                ],
                "named_joins": list(s.named_joins),
                "axiom_nodes": list(s.axiom_node_ids),
            }
            for ax, s in sitings.items()
        },
        "categories": {
            cat: {
                "attached": list(v.attached),
                "named_join_axioms": list(v.named_join_axioms),
                "inherited": list(v.inherited),
                "available": list(v.available),
                "bedrock_path_count": len(paths_to_bedrock(cat, graph)),
            }
            for cat, v in (
                (c, category_axiom_view(c, graph)) for c in categories
            )
        },
    }


#══════════════════════════════════════════════════════════════════════════════
# Formatting
#══════════════════════════════════════════════════════════════════════════════


def format_axioms_catalog(graph: DotGraph | None = None) -> str:
    graph = graph or parse_dot()
    sitings = all_axiom_sitings(graph)
    lines = [
        f"all axioms ({len(sitings)}):",
        f"{'axiom':28} {'first defined on':40} declared",
        "-" * 90,
    ]
    for ax, s in sitings.items():
        first = ",".join(s.first_defined_on) or "?"
        decl = ",".join(s.declared_hosts)
        extra = ""
        if s.redeclared_on:
            extra = f"  redeclared↑ {','.join(h for h, _ in s.redeclared_on)}"
        lines.append(f"{ax:28} {first:40} {decl}{extra}")
    return "\n".join(lines)


def format_axiom_siting(siting: AxiomSiting) -> str:
    lines = [
        f"axiom: {siting.axiom}",
        f"  first defined on: {', '.join(siting.first_defined_on) or '(none)'}",
        f"  declared on: {', '.join(siting.declared_hosts) or '(none)'}",
        f"  axiom nodes: {', '.join(siting.axiom_node_ids) or '(none)'}",
    ]
    if siting.redeclared_on:
        lines.append("  redeclared above a lower host of the same name:")
        for host, below in siting.redeclared_on:
            lines.append(f"    - {host}  (above {', '.join(below)})")
    lines.append("  possible lower hosts by declaration site:")
    if not siting.lower_by_host:
        lines.append("    (no declared hosts)")
    for host, lowers in siting.lower_by_host:
        lines.append(f"    on {host}:")
        if lowers:
            for node in lowers:
                lines.append(f"      - {node}")
        else:
            lines.append("      (none — already maximal-forgetful among solid parents)")
    lines.append("  named joins packaging this axiom:")
    if siting.named_joins:
        for join in siting.named_joins:
            lines.append(f"    - {join}")
    else:
        lines.append("    (none)")
    return "\n".join(lines)


def format_category_view(view: CategoryAxiomView) -> str:
    lines = [
        f"category: {view.category}",
        f"  attached ({len(view.attached)}):",
    ]
    for ax in view.attached or ("(none)",):
        lines.append(f"    - {ax}")
    if view.named_join_axioms:
        lines.append(f"  named-join path axioms ({len(view.named_join_axioms)}):")
        for ax in view.named_join_axioms:
            lines.append(f"    - {ax}")
    lines.append(f"  inherited from ancestors ({len(view.inherited)}):")
    for ax in view.inherited or ("(none)",):
        lines.append(f"    - {ax}")
    lines.append(f"  available total ({len(view.available)}):")
    for ax in view.available or ("(none)",):
        lines.append(f"    - {ax}")
    lines.append("  provenance:")
    if not view.sources:
        lines.append("    (none)")
    else:
        for src in view.sources:
            lines.append(f"    - {src.axiom:28} [{src.origin}] via {src.via}")
    return "\n".join(lines)


def format_paths(node: str, graph: DotGraph | None = None) -> str:
    graph = graph or parse_dot()
    node = resolve_vertex(node, graph)
    beds = bedrock_vertices(graph)
    paths = paths_to_bedrock(node, graph)
    lines = [
        f"paths to bedrock from {node}",
        f"  bedrock sinks: {', '.join(beds)}",
        f"  path count: {len(paths)}",
    ]
    for i, path in enumerate(paths, 1):
        lines.append(f"  [{i}] " + " → ".join(path))
    return "\n".join(lines)


def format_summary(graph: DotGraph | None = None) -> str:
    graph = graph or parse_dot()
    sitings = all_axiom_sitings(graph)
    multi = multi_hosted_axioms(graph)
    nonmin = hasse_nonminimal_edges(graph)
    beds = bedrock_vertices(graph)
    lines = [
        f"solid nodes: {len(graph.solid_nodes)}",
        f"solid edges: {len(graph.solid_edges)}",
        f"named joins: {len(graph.named_joins)}",
        f"axioms: {len(sitings)}",
        f"bedrock: {', '.join(beds)}",
        f"multi-hosted axioms: {len(multi)}",
        f"non-Hasse solid edges: {len(nonmin)}",
        "",
        format_axioms_catalog(graph),
    ]
    if multi:
        lines.append("")
        lines.append("multi-hosted (inspect meanings — often not the same axiom):")
        for ax, hosts in sorted(multi.items()):
            lines.append(f"  {ax}: {', '.join(hosts)}")
    return "\n".join(lines)


def format_hasse(graph: DotGraph | None = None) -> str:
    edges = hasse_nonminimal_edges(graph)
    if not edges:
        return "no non-Hasse solid edges"
    lines = ["non-Hasse solid edges (A→C also reachable by a longer path):"]
    for edge in edges:
        lines.append(f"  {edge.src} -> {edge.tgt}")
    return "\n".join(lines)


def format_ancestry(node: str, graph: DotGraph | None = None) -> str:
    graph = graph or parse_dot()
    node = resolve_vertex(node, graph)
    depths = solid_ancestry_depth(node, graph)
    if not depths:
        return f"{node}: no solid parents in graph (bedrock or unknown)"
    lines = [f"solid ancestry of {node} (depth = forgetful steps):"]
    for anc, d in sorted(depths.items(), key=lambda kv: (kv[1], str(kv[0]))):
        lines.append(f"  {d}: {anc}")
    return "\n".join(lines)


#══════════════════════════════════════════════════════════════════════════════
# CLI
#══════════════════════════════════════════════════════════════════════════════


_COMMANDS = (
    "axioms | axiom <Name> | category <Vertex> | host <Vertex> | "
    "paths <Vertex> | ancestry <Vertex> | summary | hasse | json | "
    "embed | embed-json | ledger | naming | naming-json | layers | design | "
    "seed | manifests | manifests-parity"
)


def _cli(argv: Iterable[str] | None = None) -> int:
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help", "help"}:
        print(__doc__)
        print(f"commands: {_COMMANDS}")
        return 0
    cmd = args[0]
    graph = parse_dot()
    if cmd == "summary":
        print(format_summary(graph))
        return 0
    if cmd == "axioms":
        print(format_axioms_catalog(graph))
        return 0
    if cmd == "axiom":
        if len(args) < 2:
            print("usage: audit axiom <AxiomName>", file=sys.stderr)
            return 2
        print(format_axiom_siting(axiom_siting(args[1], graph)))
        return 0
    if cmd in {"category", "host"}:
        if len(args) < 2:
            print(f"usage: audit {cmd} <Vertex>", file=sys.stderr)
            return 2
        print(format_category_view(category_axiom_view(args[1], graph)))
        return 0
    if cmd == "paths":
        if len(args) < 2:
            print("usage: audit paths <Vertex>", file=sys.stderr)
            return 2
        print(format_paths(args[1], graph))
        return 0
    if cmd == "ancestry":
        if len(args) < 2:
            print("usage: audit ancestry <Vertex>", file=sys.stderr)
            return 2
        print(format_ancestry(args[1], graph))
        return 0
    if cmd == "hasse":
        print(format_hasse(graph))
        return 0
    if cmd == "json":
        print(json.dumps(audit_catalog(graph), indent=2, sort_keys=True))
        return 0
    if cmd == "embed":
        from .sage_embed import format_embedding_report, full_embedding_report

        print(format_embedding_report(full_embedding_report(graph)))
        return 0
    if cmd == "embed-json":
        from .sage_embed import full_embedding_report

        print(json.dumps(full_embedding_report(graph).to_dict(), indent=2, sort_keys=True))
        return 0
    if cmd == "ledger":
        from .exceptions import EMBED_EXCEPTIONS

        for row in EMBED_EXCEPTIONS:
            print(
                f"{row.kind}\t{row.sage_name}\talias_of={row.alias_of}\t"
                f"parent={row.sage_parent}\tstub={row.stub_vertex}\t{row.detail}"
            )
        return 0
    if cmd == "naming":
        from .naming import format_naming_report, naming_report

        print(format_naming_report(naming_report(graph)))
        return 0
    if cmd == "naming-json":
        from .naming import naming_report

        print(json.dumps(naming_report(graph).to_dict(), indent=2, sort_keys=True))
        return 0
    if cmd == "layers":
        from .architecture import pipeline_summary
        from .sage_correspondence import current_sage_correspondence

        corr = current_sage_correspondence()
        print(pipeline_summary())
        print()
        print(f"sage_correspondence.version: {corr.version}")
        print(f"sage→𝒢 map size: {len(corr.sage_to_graph)}")
        print(f"research-only vertices: {len(corr.research_only)}")
        print(f"exception ledger rows: {len(corr.exceptions)}")
        return 0
    if cmd == "design":
        from .design_sources import (
            assert_design_sources_present,
            design_paths,
            load_correspondence,
            load_sage_nodes,
        )

        assert_design_sources_present()
        paths = design_paths()
        sage = load_sage_nodes()
        corr_json = load_correspondence()
        print("design/ — three static sources (+ semantic seed under 𝒢)")
        for key in (
            "sage_category_graph",
            "normalized_category_graph",
            "sage_to_normalized_map",
            "semantic_seed",
        ):
            print(f"  {key}: {paths[key]}")
        print(f"sage nodes (inventory extract): {sage['node_count']}")
        print(f"correspondence sage→𝒢: {len(corr_json['sage_to_graph'])}")
        print(f"normalized DOT (presentation): {paths['normalized_dot']}")
        print(f"semantic seed (authoritative):  {paths['semantic_seed']}")
        return 0
    if cmd == "seed":
        from .semantic_seed import format_seed_report

        print(format_seed_report())
        return 0
    if cmd == "manifests":
        from .manifests import format_manifests_report, validate_three_manifests

        parity = "parity" in args[1:]
        print(format_manifests_report(require_full_parity=parity))
        return 0 if not validate_three_manifests(require_full_parity=parity) else 1
    if cmd == "manifests-parity":
        from .manifests import format_manifests_report, validate_three_manifests

        print(format_manifests_report(require_full_parity=True))
        return 0 if not validate_three_manifests(require_full_parity=True) else 1
    print(f"unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(_cli())
