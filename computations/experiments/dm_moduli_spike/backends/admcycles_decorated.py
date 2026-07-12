r"""Adapter over ``admcycles.decorated_graph``.

``admcycles.decorated_graph.stable_graphs`` enumerates stable graphs up to
isomorphism with explicit contraction morphisms.  Results are converted to the
spike's owned :class:`~dm_moduli_spike.objects.graph_types.StableGraphType`;
``DecoratedGraph`` is never exposed in the public API.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterator
from typing import TYPE_CHECKING

from ..objects.records import StableGraph

if TYPE_CHECKING:
    from ..objects.contractions import StableGraphContraction
    from ..objects.curve_types import StableCurveType, StableCurveTypes


def _require_decorated_module() -> object:
    try:
        import admcycles.decorated_graph as decorated_graph  # type: ignore[import-not-found]
    except ImportError as error:
        raise ImportError(
            "the admcycles-decorated backend requires admcycles with the "
            "'admcycles.decorated_graph' module (install admcycles from "
            "https://gitlab.com/modulispaces/admcycles)"
        ) from error
    if not hasattr(decorated_graph, "stable_graphs"):  # pragma: no cover - version dependent
        raise ImportError(
            "admcycles.decorated_graph is present but lacks 'stable_graphs'; "
            "upgrade admcycles from https://gitlab.com/modulispaces/admcycles"
        )
    return decorated_graph


def _decorated_genera(decorated: object, num_vertices: int) -> tuple[int, ...]:
    genus = getattr(decorated, "genus", None)
    if callable(genus):
        return tuple(int(genus(vertex)) for vertex in range(num_vertices))
    genera = getattr(decorated, "_genera", None)
    if genera is None:
        raise TypeError(f"DecoratedGraph lacks vertex genera: {decorated!r}")
    return tuple(int(genera[vertex]) for vertex in range(num_vertices))


def _record_from_decorated_graph(decorated: object, g: int, n: int) -> StableGraph:
    r"""Convert an ``admcycles`` ``DecoratedGraph`` to a half-edge record."""
    num_vertices = int(decorated.num_verts())  # type: ignore[attr-defined]
    genera = _decorated_genera(decorated, num_vertices)
    markings = tuple(
        tuple(int(m) for m in decorated.markings(vertex))  # type: ignore[attr-defined]
        for vertex in range(num_vertices)
    )
    edges: list[tuple[int, int]] = []
    for u, v, multiplicity in decorated.edges(multiplicities=True, loops=True):  # type: ignore[attr-defined]
        for _ in range(int(multiplicity)):
            edges.append((int(u), int(v)))

    labels = sorted(marking for vertex_markings in markings for marking in vertex_markings)
    assert labels == list(range(1, n + 1)), f"decorated graph markings {labels} are not exactly 1, ..., {n}"

    flag_vertex: list[int] = []
    flag_involution: list[int] = []
    marking_to_flag_by_label: dict[int, int] = {}

    for vertex, vertex_markings in enumerate(markings):
        for label in vertex_markings:
            flag = len(flag_vertex)
            flag_vertex.append(vertex)
            flag_involution.append(flag)
            marking_to_flag_by_label[label] = flag

    for u, v in edges:
        flag_u = len(flag_vertex)
        flag_vertex.append(u)
        flag_involution.append(flag_u + 1)
        flag_vertex.append(v)
        flag_involution.append(flag_u)

    marking_to_flag = tuple(marking_to_flag_by_label[label] for label in range(1, n + 1))
    record = StableGraph(
        vertex_genera=genera,
        flag_vertex=tuple(flag_vertex),
        flag_involution=tuple(flag_involution),
        marking_to_flag=marking_to_flag,
    )
    assert record.genus() == g, f"converted record genus {record.genus()} != ambient genus {g}"
    return record


def _iter_decorated_graphs(decorated_graph: object, g: int, n: int, cap: int) -> Iterator[tuple[object, int]]:
    r"""Flatten ``stable_graphs(g, n, rmax)`` buckets (list-of-lists by codimension)."""
    buckets = decorated_graph.stable_graphs(g, n, cap)  # type: ignore[attr-defined]
    if not buckets:
        return
    assert isinstance(buckets[0], list), (
        f"expected stable_graphs({g}, {n}, {cap}) to return dimension buckets; got {type(buckets[0])}"
    )
    for codim, bucket in enumerate(buckets):
        if codim > cap:
            continue
        for decorated in bucket:
            yield decorated, codim


def _edge_flag_pairs(record: StableGraph) -> dict[tuple[int, int], list[tuple[int, int]]]:
    r"""Undirected vertex edge ``(min, max)`` to ordered flag pairs (in insertion order)."""
    buckets: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for flag, partner in record.internal_edges():
        u = record.flag_vertex[flag]
        v = record.flag_vertex[partner]
        key = (u, v) if u <= v else (v, u)
        pair = (flag, partner) if flag < partner else (partner, flag)
        buckets.setdefault(key, []).append(pair)
    return buckets


def _contracted_flags_for_vertex_edge(
    record: StableGraph,
    u: int,
    v: int,
    multiplicity: int = 1,
) -> frozenset[int]:
    r"""Flag set for contracting ``multiplicity`` units of the undirected edge ``(u, v)``."""
    key = (int(u), int(v)) if int(u) <= int(v) else (int(v), int(u))
    pairs = _edge_flag_pairs(record)[key]
    contracted: set[int] = set()
    for flag, partner in pairs[: int(multiplicity)]:
        contracted.add(flag)
        contracted.add(partner)
    return frozenset(contracted)


def contraction_from_decorated_morphism(
    morphism: object,
    g: int,
    n: int,
    *,
    domain_graph: StableGraph | None = None,
) -> StableGraphContraction:
    r"""Convert an ``admcycles`` ``DecoratedGraphMorphism`` to :class:`StableGraphContraction`."""
    from ..objects.contractions import _contract_flag_set

    if domain_graph is None:
        domain = _record_from_decorated_graph(morphism.domain(), g, n)  # type: ignore[attr-defined]
    else:
        domain = domain_graph
    contracted: set[int] = set()
    for u, v, multiplicity in morphism.contracted_edges():  # type: ignore[attr-defined]
        contracted.update(_contracted_flags_for_vertex_edge(domain, int(u), int(v), int(multiplicity)))
    return _contract_flag_set(domain, frozenset(contracted))


def _record_to_decorated_graph(record: StableGraph, g: int, n: int) -> object:
    r"""Convert a half-edge :class:`StableGraph` to an ``admcycles`` ``DecoratedGraph``."""
    decorated_graph = _require_decorated_module()
    DecoratedGraph = decorated_graph.DecoratedGraph  # type: ignore[attr-defined]
    genera = list(record.vertex_genera)
    markings = [list(record.markings_at(vertex)) for vertex in range(record.num_vertices())]
    multiplicities: dict[tuple[int, int], int] = defaultdict(int)
    for flag, partner in record.internal_edges():
        u = record.flag_vertex[flag]
        v = record.flag_vertex[partner]
        key = (u, v) if u <= v else (v, u)
        multiplicities[key] += 1
    edges = [(u, v, multiplicity) for (u, v), multiplicity in sorted(multiplicities.items())]
    decorated = DecoratedGraph(genera, markings, edges)
    converted = _record_from_decorated_graph(decorated, g, n)
    assert converted.genus() == g, f"round-trip genus {converted.genus()} != ambient {g}"
    assert converted.num_markings() == n, f"round-trip markings {converted.num_markings()} != ambient {n}"
    assert converted.num_edges() == record.num_edges(), (
        f"round-trip edge count {converted.num_edges()} != {record.num_edges()}"
    )
    return decorated


def edge_orbit_sizes(decorated: object) -> tuple[tuple[tuple[int, int], int], ...]:
    r"""Proxy ``DecoratedGraph.edge_orbit_representatives`` as ``((u, v), size)`` pairs."""
    return tuple(
        ((int(u), int(v)), int(size))
        for u, v, size in decorated.edge_orbit_representatives()  # type: ignore[attr-defined]
    )


class AdmcyclesDecoratedGraphBackend:
    r"""Enumerator via ``admcycles.decorated_graph.stable_graphs``."""

    def stable_curve_types(self, curve_types: StableCurveTypes, max_codim: int | None = None) -> tuple[StableCurveType, ...]:
        decorated_graph = _require_decorated_module()
        g = curve_types.genus()
        n = curve_types.number_of_markings()
        dimension = curve_types.dimension()
        cap = dimension if max_codim is None else min(int(max_codim), dimension)
        result: dict[object, StableCurveType] = {}
        for decorated, bucket_codim in _iter_decorated_graphs(decorated_graph, g, n, cap):
            record = _record_from_decorated_graph(decorated, g, n)
            assert record.num_edges() == bucket_codim, (
                f"decorated_graph bucket codim {bucket_codim} disagrees with {record.num_edges()} edges"
            )
            if record.num_edges() > cap:
                continue
            curve_type = curve_types.from_record(record)
            result[curve_type.canonical_key()] = curve_type
        return tuple(result.values())
