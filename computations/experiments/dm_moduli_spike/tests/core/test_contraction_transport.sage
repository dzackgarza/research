from tests.support.fixtures import flag_generator_images
r"""Tier-4 internal consistency: transport of contractions along isomorphisms."""

from __future__ import annotations

from dm_moduli_spike.objects.graph_types import StableGraphTypes
from dm_moduli_spike.objects.records import StableGraph
from dm_moduli_spike.objects.contractions import contract_edge
from dm_moduli_spike.objects.isomorphisms import (
    identity_isomorphism,
    isomorphism_between,
    transport_contraction,
    transport_contraction_via_canonical_relabeling,
)


def _swap_vertices(graph: StableGraph) -> StableGraph:
    r"""Relabel vertices ``0 <-> 1`` while keeping flag indices fixed."""
    swap = (1, 0)
    return StableGraph(
        vertex_genera=tuple(graph.vertex_genera[swap[vertex]] for vertex in range(graph.num_vertices())),
        flag_vertex=tuple(swap[graph.flag_vertex[flag]] for flag in range(graph.num_flags())),
        flag_involution=graph.flag_involution,
        marking_to_flag=graph.marking_to_flag,
    )


def test_transport_square_preserves_flag_and_fibre_data():
    types = StableGraphTypes(1, 2)
    gamma = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    domain = gamma.canonical_representative()
    loop_edge = next(
        edge
        for edge in domain.internal_edges()
        if domain.flag_vertex[edge[0]] == domain.flag_vertex[edge[1]]
    )
    _, contraction = contract_edge(domain, loop_edge)

    domain_alt = _swap_vertices(domain)
    codomain_alt = _swap_vertices(contraction.codomain())
    alpha = isomorphism_between(domain, domain_alt)
    beta = isomorphism_between(contraction.codomain(), codomain_alt)
    assert alpha.vertex_map == (1, 0)
    assert beta.vertex_map == (1, 0)

    transported = transport_contraction(contraction, alpha, beta)
    assert transported.domain() == domain_alt
    assert transported.codomain() == codomain_alt

    for codomain_flag, domain_flag in contraction.domain_flag_of_codomain_flag().items():
        new_codomain = beta.flag_map[codomain_flag]
        new_domain = alpha.flag_map[domain_flag]
        assert transported.domain_flag_of_codomain_flag()[new_codomain] == new_domain

    for codomain_vertex, fibre in enumerate(contraction.vertex_fibres()):
        new_vertex = beta.vertex_map[codomain_vertex]
        expected = frozenset(alpha.vertex_map[vertex] for vertex in fibre)
        assert transported.vertex_fibres()[new_vertex] == expected


def test_transport_composes_with_native_contraction():
    types = StableGraphTypes(1, 2)
    gamma = types.from_vertices(genera=(1, 0), markings=((), (1, 2)), edges=((0, 1),))
    domain = gamma.canonical_representative()
    domain_alt = _swap_vertices(domain)
    edge = domain.internal_edges()[0]
    _, contraction = contract_edge(domain, edge)
    alpha = isomorphism_between(domain, domain_alt)
    beta = identity_isomorphism(contraction.codomain())
    transported = transport_contraction(contraction, alpha, beta)
    edge_alt = transported.contracted_edges()[0]
    image, native = contract_edge(domain_alt, edge_alt)
    assert image.canonical_representative() == transported.codomain()


def test_banana_parallel_edge_transport_swaps_contracted_edge():
    r"""Mbar(1,2) banana: Aut swaps parallel edges; transport moves edge-1 -> edge-2."""
    from dm_moduli_spike.objects.isomorphisms import StableGraphIsomorphism

    types = StableGraphTypes(1, 2)
    banana = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    graph = banana.canonical_representative()
    edges = graph.internal_edges()
    assert len(edges) == 2
    assert banana.automorphism_number() == 2

    _, q_edge0 = contract_edge(graph, edges[0])
    flag_perm = flag_generator_images(graph)[0]
    assert flag_perm[edges[0][0]] == edges[1][0]
    alpha = StableGraphIsomorphism(
        source=graph,
        target=graph,
        vertex_map=tuple(range(graph.num_vertices())),
        flag_map=flag_perm,
    )
    beta = identity_isomorphism(q_edge0.codomain())
    transported = transport_contraction(q_edge0, alpha, beta)
    assert transported.contracted_flags() == contract_edge(graph, edges[1])[1].contracted_flags()


def test_canonical_relabeling_convenience_matches_explicit_isomorphisms():
    types = StableGraphTypes(1, 2)
    gamma = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    domain = gamma.canonical_representative()
    loop_edge = next(
        edge
        for edge in domain.internal_edges()
        if domain.flag_vertex[edge[0]] == domain.flag_vertex[edge[1]]
    )
    _, contraction = contract_edge(domain, loop_edge)
    domain_alt = _swap_vertices(domain)
    codomain_alt = _swap_vertices(contraction.codomain())
    alpha = isomorphism_between(domain, domain_alt)
    beta = isomorphism_between(contraction.codomain(), codomain_alt)
    explicit = transport_contraction(contraction, alpha, beta)
    via_canonical = transport_contraction_via_canonical_relabeling(
        contraction,
        domain=domain_alt,
        codomain=codomain_alt,
    )
    assert explicit == via_canonical
