"""Build Sage ``DiGraph`` / ``MultiDiGraph`` objects from DOT and from categories."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from sage.graphs.digraph import DiGraph

from .dot_parse import DotGraph, parse_dot
from .factory import factory
from .slugs import axiom_method_name

if TYPE_CHECKING:
    from sage.categories.category import Category


def dot_vertices(graph: DotGraph | None = None) -> tuple[str, ...]:
    graph = graph or parse_dot()
    return tuple(sorted(set(graph.solid_nodes) | set(graph.named_joins), key=str))


def dot_solid_digraph(graph: DotGraph | None = None) -> DiGraph:
    """Solid parent edges from the DOT file (child → parent = supercategory)."""
    graph = graph or parse_dot()
    G = DiGraph(multiedges=True)
    verts = dot_vertices(graph)
    G.add_vertices(verts)
    for edge in graph.solid_edges:
        if edge.src in G and edge.tgt in G:
            G.add_edge(edge.src, edge.tgt)
    return G


def dot_axiom_digraph(graph: DotGraph | None = None) -> DiGraph:
    """Axiom attachment edges (dotted in DOT): source → host, edge label = axiom name."""
    graph = graph or parse_dot()
    G = DiGraph(multiedges=True)
    G.add_vertices(dot_vertices(graph))
    for edge in graph.axiom_edges:
        label = graph.axiom_labels.get(edge.src, edge.src.rsplit(".", 1)[-1])
        host = edge.tgt
        if host not in G:
            continue
        axiom_vertex = edge.src if edge.src in G else f"{host}.{axiom_method_name(label)}"
        if axiom_vertex not in G:
            G.add_vertex(axiom_vertex)
        G.add_edge(axiom_vertex, host, axiom_method_name(label))
    return G


def _stub_instances(graph: DotGraph | None = None) -> dict[str, Category]:
    fac = factory()
    graph = graph or fac.graph
    return {vertex: fac.instance(vertex) for vertex in dot_vertices(graph)}


def _resolve_vertex(cat: Category, instances: dict[str, Category]) -> str | None:
    vertex = getattr(cat, "_dot_vertex", None)
    if isinstance(vertex, str) and vertex in instances:
        return vertex
    for node, inst in instances.items():
        if inst is cat:
            return node
    return None


def _category_digraph(
    instances: dict[str, Category],
    *,
    edge_builder: Callable[[DiGraph, str, Category, dict[str, Category]], None],
) -> DiGraph:
    G = DiGraph(multiedges=True)
    G.add_vertices(list(instances.keys()))
    for child, cat in instances.items():
        edge_builder(G, child, cat, instances)
    return G


def sage_solid_digraph(
    graph: DotGraph | None = None,
    *,
    instances: dict[str, Category] | None = None,
) -> DiGraph:
    """Direct ``super_categories()`` among DOT vertices (stub factory)."""

    def add_edges(G: DiGraph, child: str, cat: Category, inst: dict[str, Category]) -> None:
        for parent_cat in cat.super_categories():
            parent = _resolve_vertex(parent_cat, inst)
            if parent is not None:
                G.add_edge(child, parent)

    instances = instances or _stub_instances(graph)
    return _category_digraph(instances, edge_builder=add_edges)


def sage_axiom_digraph(
    graph: DotGraph | None = None,
    *,
    instances: dict[str, Category] | None = None,
) -> DiGraph:
    """Axiom attachments declared in the DOT, verified against stub instances."""
    fac = factory()
    graph = graph or fac.graph
    instances = instances or _stub_instances(graph)
    G = DiGraph(multiedges=True)
    G.add_vertices(list(instances.keys()))

    for edge in graph.axiom_edges:
        raw_label = graph.axiom_labels.get(edge.src, edge.src.rsplit(".", 1)[-1])
        label = axiom_method_name(raw_label)
        host = edge.tgt if edge.tgt in instances else None
        if host is None:
            continue

        if edge.src in instances:
            child = instances[edge.src]
            if label in child.axioms():
                G.add_edge(edge.src, host, label)
            continue

        try:
            refined = fac.axiom_instance(host, label)
        except (AttributeError, KeyError):
            continue
        if label not in refined.axioms():
            continue
        axiom_vertex = f"__axiom__:{host}:{label}"
        G.add_vertex(axiom_vertex)
        G.add_edge(axiom_vertex, host, label)

    return G


def native_solid_digraph(
    graph: DotGraph | None = None,
    *,
    instances: dict[str, Category] | None = None,
) -> DiGraph:
    """Direct ``super_categories()`` among mapped native ``sage.categories`` instances."""
    from .native_map import mapped_native_instances

    def add_edges(G: DiGraph, child: str, cat: Category, inst: dict[str, Category]) -> None:
        for parent_cat in cat.super_categories():
            parent = _resolve_vertex(parent_cat, inst)
            if parent is not None:
                G.add_edge(child, parent)

    instances = instances or mapped_native_instances(graph)
    return _category_digraph(instances, edge_builder=add_edges)


def native_axiom_digraph(
    graph: DotGraph | None = None,
    *,
    instances: dict[str, Category] | None = None,
) -> DiGraph:
    """Axiom attachments from native instances on the mapped vertex subset."""
    graph = graph or parse_dot()
    from .native_map import mapped_native_instances

    instances = instances or mapped_native_instances(graph)
    G = DiGraph(multiedges=True)
    G.add_vertices(list(instances.keys()))

    for edge in graph.axiom_edges:
        raw_label = graph.axiom_labels.get(edge.src, edge.src.rsplit(".", 1)[-1])
        label = axiom_method_name(raw_label)
        host = edge.tgt if edge.tgt in instances else None
        if host is None:
            continue

        if edge.src in instances:
            child = instances[edge.src]
            if label in child.axioms():
                G.add_edge(edge.src, host, label)
            continue

        host_cat = instances[host]
        method = getattr(host_cat, label, None)
        if method is None:
            continue
        refined = method()
        if label not in refined.axioms():
            continue
        axiom_vertex = f"__axiom__:{host}:{label}"
        G.add_vertex(axiom_vertex)
        G.add_edge(axiom_vertex, host, label)

    return G


def edge_set(G: DiGraph, *, labels: bool = False) -> set[tuple]:
    if labels:
        return set(G.edges(sort=True))
    return {(u, v) for u, v, _ in G.edges(sort=True)}


def compare_solid_graphs(
    left: DiGraph | None = None,
    right: DiGraph | None = None,
    *,
    left_name: str = "dot",
    right_name: str = "stub",
) -> dict[str, object]:
    """Compare two solid multidigraphs on their shared vertex set."""
    left = left or dot_solid_digraph()
    right = right or sage_solid_digraph()
    shared = set(left.vertices(sort=True)) & set(right.vertices(sort=True))
    left_edges = {
        (u, v)
        for u, v, _ in left.edges(sort=True)
        if u in shared and v in shared
    }
    right_edges = {
        (u, v)
        for u, v, _ in right.edges(sort=True)
        if u in shared and v in shared
    }
    left_sub = left.subgraph(shared)
    right_sub = right.subgraph(shared)
    return {
        "shared_vertices": tuple(sorted(shared, key=str)),
        "left_vertices": set(left.vertices(sort=True)),
        "right_vertices": set(right.vertices(sort=True)),
        "vertices_equal": set(left.vertices(sort=True)) == set(right.vertices(sort=True)),
        f"only_in_{left_name}": left_edges - right_edges,
        f"only_in_{right_name}": right_edges - left_edges,
        f"{left_name}_is_subgraph_of_{right_name}": left_edges <= right_edges,
        f"{right_name}_is_subgraph_of_{left_name}": right_edges <= left_edges,
        "isomorphic_on_shared": left_sub.is_isomorphic(right_sub),
        "isomorphic": (
            left.is_isomorphic(right)
            if set(left.vertices(sort=True)) == set(right.vertices(sort=True))
            else left_sub.is_isomorphic(right_sub)
        ),
        "only_in_dot": left_edges - right_edges,
        "only_in_sage": right_edges - left_edges,
    }


def compare_axiom_graphs(
    left: DiGraph | None = None,
    right: DiGraph | None = None,
    *,
    left_name: str = "dot",
    right_name: str = "stub",
) -> dict[str, object]:
    """Compare two axiom multidigraphs on incoming (host, label) pairs."""
    left = left or dot_axiom_digraph()
    right = right or sage_axiom_digraph()

    def labeled_incoming(G: DiGraph) -> set[tuple[str, object]]:
        return {
            (v, edge[2])
            for v in G.vertices(sort=True)
            for edge in G.incoming_edges(v, labels=True)
        }

    left_labeled = labeled_incoming(left)
    right_labeled = labeled_incoming(right)
    shared_hosts = set(left.vertices(sort=True)) & set(right.vertices(sort=True))
    left_on_shared = {(h, lab) for h, lab in left_labeled if h in shared_hosts}
    right_on_shared = {(h, lab) for h, lab in right_labeled if h in shared_hosts}
    return {
        "shared_vertices": tuple(sorted(shared_hosts, key=str)),
        f"only_in_{left_name}": left_on_shared - right_on_shared,
        f"only_in_{right_name}": right_on_shared - left_on_shared,
        f"{left_name}_is_subgraph_of_{right_name}": left_on_shared <= right_on_shared,
        "isomorphic": left.subgraph(shared_hosts).is_isomorphic(right.subgraph(shared_hosts)),
        "only_in_dot": left_on_shared - right_on_shared,
        "only_in_sage": right_on_shared - left_on_shared,
    }


def compare_dot_vs_stub_solid() -> dict[str, object]:
    return compare_solid_graphs(
        dot_solid_digraph(),
        sage_solid_digraph(),
        left_name="dot",
        right_name="stub",
    )


def compare_dot_vs_stub_axiom() -> dict[str, object]:
    return compare_axiom_graphs(
        dot_axiom_digraph(),
        sage_axiom_digraph(),
        left_name="dot",
        right_name="stub",
    )


def compare_stub_vs_native_solid() -> dict[str, object]:
    return compare_solid_graphs(
        sage_solid_digraph(),
        native_solid_digraph(),
        left_name="stub",
        right_name="native",
    )


def compare_stub_vs_native_axiom() -> dict[str, object]:
    return compare_axiom_graphs(
        sage_axiom_digraph(),
        native_axiom_digraph(),
        left_name="stub",
        right_name="native",
    )


def compare_dot_vs_native_solid() -> dict[str, object]:
    return compare_solid_graphs(
        dot_solid_digraph(),
        native_solid_digraph(),
        left_name="dot",
        right_name="native",
    )


def compare_dot_vs_native_axiom() -> dict[str, object]:
    return compare_axiom_graphs(
        dot_axiom_digraph(),
        native_axiom_digraph(),
        left_name="dot",
        right_name="native",
    )


def graph_comparison_report() -> dict[str, object]:
    """Run all solid/axiom comparisons; same machinery as tests/diagnostics."""
    from .native_map import mapped_native_instances, unmapped_native_vertices

    mapped = mapped_native_instances()
    return {
        "mapped_native_count": len(mapped),
        "unmapped_native_vertices": unmapped_native_vertices(),
        "dot_vs_stub_solid": compare_dot_vs_stub_solid(),
        "dot_vs_stub_axiom": compare_dot_vs_stub_axiom(),
        "stub_vs_native_solid": compare_stub_vs_native_solid(),
        "stub_vs_native_axiom": compare_stub_vs_native_axiom(),
        "dot_vs_native_solid": compare_dot_vs_native_solid(),
        "dot_vs_native_axiom": compare_dot_vs_native_axiom(),
    }
