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

    def __post_init__(self) -> None:
        source = self.source
        target = self.target
        vertex_map = self.vertex_map
        flag_map = self.flag_map

        num_vertices = source.num_vertices()
        num_flags = source.num_flags()
        assert len(vertex_map) == num_vertices, f"vertex_map length {len(vertex_map)} != |V|={num_vertices}"
        assert len(flag_map) == num_flags, f"flag_map length {len(flag_map)} != |H|={num_flags}"
        assert target.num_vertices() == num_vertices
        assert target.num_flags() == num_flags

        assert sorted(vertex_map) == list(range(num_vertices)), f"vertex_map {vertex_map} is not a bijection on V"
        assert sorted(flag_map) == list(range(num_flags)), f"flag_map {flag_map} is not a bijection on H"

        for vertex in range(num_vertices):
            image = vertex_map[vertex]
            assert source.vertex_genera[vertex] == target.vertex_genera[image], (
                f"vertex genus not preserved at {vertex}: {source.vertex_genera[vertex]} != {target.vertex_genera[image]}"
            )

        for flag in range(num_flags):
            image = flag_map[flag]
            assert vertex_map[source.flag_vertex[flag]] == target.flag_vertex[image], (
                f"incidence not preserved at flag {flag}: d({flag})={source.flag_vertex[flag]} maps to "
                f"{vertex_map[source.flag_vertex[flag]]}, but flag {image} attaches to {target.flag_vertex[image]}"
            )
            partner = source.flag_involution[flag]
            image_partner = flag_map[partner]
            assert target.flag_involution[image] == image_partner, f"involution not preserved at flag {flag}: iota({image})={target.flag_involution[image]} != {image_partner}"

        for label in range(1, source.num_markings() + 1):
            source_flag = source.marking_to_flag[label - 1]
            target_flag = target.marking_to_flag[label - 1]
            assert flag_map[source_flag] == target_flag, f"marking {label} not preserved: {source_flag} -> {flag_map[source_flag]}, expected {target_flag}"


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
    r"""An isomorphism when ``source`` and ``target`` share a canonical type.

    When ``Aut(\Gamma) \neq 1`` on a common representative, this choice is
    determined by the canonical labelling pipeline and need not be unique.
    """
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
        flag_involution=tuple(iso.flag_map[graph.flag_involution[inverse_flags[flag]]] for flag in range(iso.target.num_flags())),
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
    q: StableGraphContraction,
    alpha: StableGraphIsomorphism,
    beta: StableGraphIsomorphism,
) -> StableGraphContraction:
    r"""Transport ``q`` along ``alpha: domain' -> domain`` and ``beta: codomain' -> codomain``.

    Returns the contraction ``beta o q o alpha^{-1}`` with domain ``alpha.target``
    and codomain ``beta.target``.
    """
    from .contractions import StableGraphContraction

    assert alpha.source == q.domain(), "alpha.source must equal q.domain()"
    assert beta.source == q.codomain(), "beta.source must equal q.codomain()"

    contracted_flags = frozenset(alpha.flag_map[flag] for flag in q.contracted_flags())
    domain_flag_of_codomain_flag = tuple(
        sorted((beta.flag_map[codomain_flag], alpha.flag_map[domain_flag]) for codomain_flag, domain_flag in q.domain_flag_of_codomain_flag().items())
    )
    vertex_fibres = remap_vertex_fibres(
        q.vertex_fibres(),
        beta.vertex_map,
        alpha.vertex_map,
    )
    return StableGraphContraction(
        domain=alpha.target,
        codomain=beta.target,
        target_type=q.target_type(),
        contracted_flags=contracted_flags,
        vertex_fibres=vertex_fibres,
        domain_flag_of_codomain_flag=domain_flag_of_codomain_flag,
    )


def transport_contraction_via_canonical_relabeling(
    q: StableGraphContraction,
    *,
    domain: StableGraph,
    codomain: StableGraph,
) -> StableGraphContraction:
    r"""Transport ``q`` to new labeled endpoints via :func:`isomorphism_between`.

    This is a convenience wrapper around :func:`transport_contraction`.  The
    isomorphisms are **not** unique when the endpoint graphs admit nontrivial
    automorphisms (``Aut(\Gamma) \neq 1``): the choice follows the canonical
    labelling pipeline, not a gauge-invariant contract.
    """
    alpha = isomorphism_between(q.domain(), domain)
    beta = isomorphism_between(q.codomain(), codomain)
    return transport_contraction(q, alpha, beta)
