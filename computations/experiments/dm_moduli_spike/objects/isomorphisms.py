r"""Isomorphisms and canonicalization certificates between labeled stable graphs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .canonical import _flag_node, _incidence_graph
from .records import StableGraph, intern_graph

if TYPE_CHECKING:
    from .contractions import StableGraphContraction


@dataclass(frozen=True, slots=True)
class StableGraphIsomorphism:
    r"""Isomorphism ``source -> target`` on vertices and half-edges."""

    source: StableGraph
    target: StableGraph
    vertex_map: tuple[int, ...]
    flag_map: tuple[int, ...]


StableGraphCanonicalization = StableGraphIsomorphism


def canonicalize(record: StableGraph) -> StableGraphIsomorphism:
    r"""Canonicalize ``record``; certificate maps ``record -> canonical representative``."""
    graph, partition, color_of = _incidence_graph(record)
    _, relabelling = graph.canonical_label(partition=partition, certificate=True)

    vertex_nodes = sorted(
        (node for node in color_of if node[0] == "V"),
        key=lambda node: relabelling[node],
    )
    old_vertices = [node[1] for node in vertex_nodes]
    vertex_map = tuple(old_vertices.index(vertex) for vertex in range(record.num_vertices()))

    old_flags = list(range(record.num_flags()))
    old_flags.sort(key=lambda flag: relabelling[_flag_node(record, flag)])
    flag_map = tuple(old_flags.index(flag) for flag in range(record.num_flags()))

    target = intern_graph(
        StableGraph(
            vertex_genera=tuple(record.vertex_genera[vertex] for vertex in old_vertices),
            flag_vertex=tuple(old_vertices.index(record.flag_vertex[old_flag]) for old_flag in old_flags),
            flag_involution=tuple(flag_map[record.flag_involution[old_flag]] for old_flag in old_flags),
            marking_to_flag=tuple(flag_map[flag] for flag in record.marking_to_flag),
        )
    )
    return StableGraphIsomorphism(
        source=record,
        target=target,
        vertex_map=vertex_map,
        flag_map=flag_map,
    )


def identity_isomorphism(record: StableGraph) -> StableGraphIsomorphism:
    size_v = record.num_vertices()
    size_h = record.num_flags()
    return StableGraphIsomorphism(
        source=record,
        target=record,
        vertex_map=tuple(range(size_v)),
        flag_map=tuple(range(size_h)),
    )


def inverse_vertex_map(vertex_map: tuple[int, ...]) -> tuple[int, ...]:
    inverse = [0] * len(vertex_map)
    for source, target in enumerate(vertex_map):
        inverse[target] = source
    return tuple(inverse)


def inverse_flag_map(flag_map: tuple[int, ...]) -> tuple[int, ...]:
    inverse = [0] * len(flag_map)
    for source, target in enumerate(flag_map):
        inverse[target] = source
    return tuple(inverse)


def isomorphism_between(source: StableGraph, target: StableGraph) -> StableGraphIsomorphism:
    r"""The unique isomorphism when ``source`` and ``target`` have the same canonical type."""
    src = canonicalize(source)
    dst = canonicalize(target)
    assert src.target == dst.target, "graphs are not isomorphic"
    inverse_dst_vertices = inverse_vertex_map(dst.vertex_map)
    inverse_dst_flags = inverse_flag_map(dst.flag_map)
    vertex_map = tuple(inverse_dst_vertices[src.vertex_map[vertex]] for vertex in range(source.num_vertices()))
    flag_map = tuple(inverse_dst_flags[src.flag_map[flag]] for flag in range(source.num_flags()))
    return StableGraphIsomorphism(source=source, target=target, vertex_map=vertex_map, flag_map=flag_map)


def apply_isomorphism(graph: StableGraph, iso: StableGraphIsomorphism) -> StableGraph:
    r"""Push ``graph`` forward along ``iso`` to its ``target`` labeling."""
    assert iso.source == graph
    inverse_vertices = inverse_vertex_map(iso.vertex_map)
    inverse_flags = inverse_flag_map(iso.flag_map)
    return StableGraph(
        vertex_genera=tuple(graph.vertex_genera[inverse_vertices[vertex]] for vertex in range(iso.target.num_vertices())),
        flag_vertex=tuple(iso.vertex_map[graph.flag_vertex[inverse_flags[flag]]] for flag in range(iso.target.num_flags())),
        flag_involution=tuple(
            iso.flag_map[graph.flag_involution[inverse_flags[flag]]] for flag in range(iso.target.num_flags())
        ),
        marking_to_flag=tuple(iso.flag_map[graph.marking_to_flag[label - 1]] for label in range(1, graph.num_markings() + 1)),
    )


def remap_vertex_fibres(
    vertex_fibres: tuple[frozenset[int], ...],
    codomain_vertex_map: tuple[int, ...],
    domain_vertex_map: tuple[int, ...],
) -> tuple[frozenset[int], ...]:
    r"""Transport vertex fibres under ``q' = beta o q o alpha^{-1}``."""
    grouped: list[set[int]] = [set() for _ in range(len(codomain_vertex_map))]
    for old_codomain_vertex, fibre in enumerate(vertex_fibres):
        new_codomain_vertex = codomain_vertex_map[old_codomain_vertex]
        grouped[new_codomain_vertex].update(domain_vertex_map[vertex] for vertex in fibre)
    return tuple(frozenset(fibre) for fibre in grouped)


def transport_contraction(
    contraction: StableGraphContraction,
    *,
    domain: StableGraph | None = None,
    codomain: StableGraph | None = None,
) -> StableGraphContraction:
    r"""Transport ``q`` along isomorphisms ``alpha: domain -> domain'``, ``beta: codomain -> codomain'``."""
    from .contractions import StableGraphContraction

    if domain is None:
        domain = contraction.domain()
    if codomain is None:
        codomain = contraction.codomain()
    if domain is contraction.domain() and codomain is contraction.codomain():
        return contraction

    alpha = (
        isomorphism_between(contraction.domain(), domain)
        if domain is not contraction.domain()
        else identity_isomorphism(domain)
    )
    beta = (
        isomorphism_between(contraction.codomain(), codomain)
        if codomain is not contraction.codomain()
        else identity_isomorphism(codomain)
    )

    contracted_flags = frozenset(alpha.flag_map[flag] for flag in contraction.contracted_flags())
    domain_flag_of_codomain_flag = tuple(
        sorted(
            (beta.flag_map[codomain_flag], alpha.flag_map[domain_flag])
            for codomain_flag, domain_flag in contraction.domain_flag_of_codomain_flag().items()
        )
    )
    vertex_fibres = remap_vertex_fibres(
        contraction.vertex_fibres(),
        beta.vertex_map,
        alpha.vertex_map,
    )
    return StableGraphContraction(
        domain=domain,
        codomain=codomain,
        target_type=contraction.target_type(),
        contracted_flags=contracted_flags,
        vertex_fibres=vertex_fibres,
        domain_flag_of_codomain_flag=domain_flag_of_codomain_flag,
    )
