r"""Canonical labelling and automorphisms of a stable curve type.

The half-edge record is reduced to a *coloured simple incidence graph*:

* one node for each component vertex, coloured by its genus;
* one node for each internal edge;
* two flag nodes for each internal edge;
* one singleton-coloured node for each labelled marking;

with incidences ``component -- flag -- edge`` and ``component -- marking``.

This encoding faithfully retains parallel edges, the two branches of a loop,
branch swaps, marking labels and vertex genera.  Sage's canonical labelling
relative to a vertex partition then provides:

* a canonical serialisation key (equality / hashing), and
* the automorphism group order, which equals :math:`|\operatorname{Aut}(\Gamma)|`
  for the stack quotient (markings are individually coloured, so every marking is
  fixed; flags attached to the same edge may swap, giving loop branch swaps;
  equal-genus vertices and parallel edges may permute).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from .records import StableGraph

if TYPE_CHECKING:
    from sage.graphs.graph import Graph

# Node color tags. Vertex nodes additionally carry their genus so that only
# equal-genus components may be identified; markings are singletons.
_ColorTag = tuple[object, ...]
CanonicalKey = tuple[tuple[tuple[int, int], ...], tuple[tuple[int, _ColorTag], ...]]


def _partition_sort_key(tag: _ColorTag) -> tuple[int, int]:
    r"""Sort colour tags in a partition-stable, numerically correct order."""
    kind = tag[0]
    if kind == "V":
        return (0, int(cast(int, tag[1])))
    if kind == "M":
        return (1, int(cast(int, tag[1])))
    if kind == "E":
        return (2, 0)
    if kind == "F":
        return (3, 0)
    raise ValueError(f"unknown incidence-graph colour tag {tag!r}")


def _incidence_graph(record: StableGraph) -> tuple[Graph, list[list[tuple[str, int]]], dict[tuple[str, int], _ColorTag]]:
    r"""Return the coloured incidence graph, its colour partition (a list of
    node classes for Sage's ``partition`` argument), and the node -> colour-tag
    map used to build a canonical, colour-aware key."""
    from sage.graphs.graph import Graph

    graph = Graph()
    color_of: dict[tuple[str, int], _ColorTag] = {}

    # Component nodes, coloured by genus.
    for vertex in range(record.num_vertices()):
        node = ("V", vertex)
        graph.add_vertex(node)
        color_of[node] = ("V", record.vertex_genera[vertex])

    # Marking nodes, each its own singleton colour, wired to the carrying vertex.
    for marking, flag in enumerate(record.marking_to_flag, start=1):
        node = ("M", marking)
        graph.add_vertex(node)
        color_of[node] = ("M", marking)
        graph.add_edge(node, ("V", record.flag_vertex[flag]))

    # Edge and flag nodes: component -- flag -- edge, two flags per edge.
    for index, (flag, partner) in enumerate(record.internal_edges()):
        edge_node = ("E", index)
        graph.add_vertex(edge_node)
        color_of[edge_node] = ("E",)
        for branch in (flag, partner):
            flag_node = ("F", branch)
            graph.add_vertex(flag_node)
            color_of[flag_node] = ("F",)
            graph.add_edge(("V", record.flag_vertex[branch]), flag_node)
            graph.add_edge(flag_node, edge_node)

    partition_map: dict[_ColorTag, list[tuple[str, int]]] = {}
    for node, tag in color_of.items():
        if tag not in partition_map:
            partition_map[tag] = []
        partition_map[tag].append(node)
    partition = [partition_map[tag] for tag in sorted(partition_map, key=_partition_sort_key)]
    return graph, partition, color_of


def _flag_node(record: StableGraph, flag: int) -> tuple[str, int]:
    if record.flag_involution[flag] == flag:
        marking = record.marking_to_flag.index(flag) + 1
        return ("M", marking)
    return ("F", flag)


def flag_to_node(record: StableGraph, flag: int) -> tuple[str, int]:
    r"""Incidence-graph node for a half-edge flag index."""
    return _flag_node(record, flag)


def node_to_flag(record: StableGraph, node: object) -> int:
    r"""Half-edge flag index for an incidence-graph ``M``/``F`` node."""
    if not isinstance(node, tuple) or len(node) != 2:
        raise ValueError(f"not a flag node: {node!r}")
    kind, value = node
    if kind == "F":
        return int(value)
    if kind == "M":
        return record.marking_to_flag[int(value) - 1]
    raise ValueError(f"not a flag node: {node!r}")


def canonical_record(record: StableGraph) -> StableGraph:
    r"""The canonical half-edge representative for an isomorphism class.

    Two inputs with the same :func:`canonical_key` yield identical records.
    """
    from .isomorphisms import canonicalize

    return canonicalize(record).target


def canonical_key(record: StableGraph) -> CanonicalKey:
    r"""A hashable, colour-aware canonical form.

    Two records yield the same key iff their coloured incidence graphs are
    isomorphic as coloured graphs, i.e. iff the stable curve types are
    isomorphic (respecting vertex genera and every marking label individually).
    """
    graph, partition, color_of = _incidence_graph(record)
    _, relabelling = graph.canonical_label(partition=partition, certificate=True)
    edges = tuple(sorted((min(relabelling[u], relabelling[v]), max(relabelling[u], relabelling[v])) for u, v, _ in graph.edges()))
    colors = tuple(sorted((relabelling[node], tag) for node, tag in color_of.items()))
    return edges, colors


def automorphism_group(record: StableGraph) -> object:
    r"""The automorphism group of the coloured incidence graph."""
    graph, partition, _ = _incidence_graph(record)
    return graph.automorphism_group(partition=partition)


def automorphism_number(record: StableGraph) -> int:
    r""":math:`|\operatorname{Aut}(\Gamma)|`, the order of the automorphism group
    of the coloured incidence graph.  This is the half-edge automorphism number:
    it counts branch swaps of loops and permutations of parallel edges, and fixes
    every marking."""
    from typing import Any, cast

    group = cast(Any, automorphism_group(record))
    return int(group.order())


def to_labeled_json(record: StableGraph, g: int, n: int, schema: int = 1) -> dict[str, object]:
    r"""A versioned, external JSON representation (vertex/edge oriented).

    This is the shape crossing a process boundary; the in-process canonical key
    additionally retains branch identifiers.  Loops appear as edges with equal
    ends.
    """
    vertices = [
        {
            "id": vertex,
            "genus": record.vertex_genera[vertex],
            "markings": list(record.markings_at(vertex)),
        }
        for vertex in range(record.num_vertices())
    ]
    edges = [
        {
            "id": index,
            "ends": [record.flag_vertex[flag], record.flag_vertex[partner]],
        }
        for index, (flag, partner) in enumerate(record.internal_edges())
    ]
    return {
        "schema": schema,
        "ambient": {"g": g, "n": n},
        "vertices": vertices,
        "edges": edges,
    }


def to_json(record: StableGraph, g: int, n: int, schema: int = 1) -> dict[str, object]:
    r"""JSON for the canonical representative (isomorphism-class invariant)."""
    return to_labeled_json(canonical_record(record), g, n, schema=schema)
