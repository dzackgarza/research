r"""Isomorphisms and canonicalization certificates between labeled stable graphs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .canonical import _flag_node, _incidence_graph
from .records import StableGraph, intern_graph

if TYPE_CHECKING:
    from .contractions import StableGraphContraction


@dataclass(frozen=True, slots=True)
class StableGraphCanonicalization:
    r"""Certificate from a labeled graph to its canonical representative."""

    source: StableGraph
    target: StableGraph
    vertex_map: tuple[int, ...]
    flag_map: tuple[int, ...]


def canonicalize(record: StableGraph) -> StableGraphCanonicalization:
    r"""Canonicalize ``record`` and retain Sage's relabelling certificate."""
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
    return StableGraphCanonicalization(
        source=record,
        target=target,
        vertex_map=vertex_map,
        flag_map=flag_map,
    )


def inverse_flag_map(flag_map: tuple[int, ...]) -> tuple[int, ...]:
    inverse = [0] * len(flag_map)
    for source, target in enumerate(flag_map):
        inverse[target] = source
    return tuple(inverse)


def compose_flag_maps(inner: tuple[int, ...], outer: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(outer[inner[flag]] for flag in range(len(inner)))


def vertex_transport_map(source: StableGraph, target: StableGraph) -> tuple[int, ...]:
    r"""Map vertex indices on ``source`` to matching indices on ``target``."""
    src = canonicalize(source)
    dst = canonicalize(target)
    assert src.target == dst.target, "graphs are not isomorphic"
    inverse_dst = [0] * len(dst.vertex_map)
    for source_index, target_index in enumerate(dst.vertex_map):
        inverse_dst[target_index] = source_index
    return tuple(inverse_dst[src.vertex_map[vertex]] for vertex in range(source.num_vertices()))


def remap_vertex_fibres(
    vertex_fibres: tuple[frozenset[int], ...],
    vertex_map: tuple[int, ...],
) -> tuple[frozenset[int], ...]:
    grouped: list[set[int]] = [set() for _ in range(len(vertex_map))]
    for source_index, fibre in enumerate(vertex_fibres):
        grouped[vertex_map[source_index]].update(fibre)
    return tuple(frozenset(fibre) for fibre in grouped)


def transport_contraction(
    contraction: StableGraphContraction,
    *,
    domain: StableGraph | None = None,
    codomain: StableGraph | None = None,
) -> StableGraphContraction:
    r"""Transport a contraction to new labeled endpoint representatives."""
    from .contractions import StableGraphContraction

    if domain is None:
        domain = contraction.domain()
    if codomain is None:
        codomain = contraction.codomain()
    if domain is contraction.domain() and codomain is contraction.codomain():
        return contraction

    if domain is not contraction.domain():
        domain_flag_map = compose_flag_maps(
            inverse_flag_map(canonicalize(contraction.domain()).flag_map),
            canonicalize(domain).flag_map,
        )
    else:
        domain_flag_map = tuple(range(domain.num_flags()))

    if codomain is not contraction.codomain():
        codomain_flag_map = compose_flag_maps(
            canonicalize(contraction.codomain()).flag_map,
            inverse_flag_map(canonicalize(codomain).flag_map),
        )
        vertex_transport = vertex_transport_map(contraction.codomain(), codomain)
        vertex_fibres = remap_vertex_fibres(contraction.vertex_fibres(), vertex_transport)
    else:
        codomain_flag_map = tuple(range(codomain.num_flags()))
        vertex_fibres = contraction.vertex_fibres()

    contracted_flags = frozenset(domain_flag_map[flag] for flag in contraction.contracted_flags())
    domain_flag_of_codomain_flag = tuple(
        sorted(
            (domain_flag_map[domain_flag], codomain_flag_map[codomain_flag])
            for codomain_flag, domain_flag in contraction.domain_flag_of_codomain_flag().items()
        )
    )
    return StableGraphContraction(
        domain=domain,
        codomain=codomain,
        target_type=contraction.target_type(),
        contracted_flags=contracted_flags,
        vertex_fibres=vertex_fibres,
        domain_flag_of_codomain_flag=domain_flag_of_codomain_flag,
    )
