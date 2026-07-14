r"""Tier-4 internal consistency: contraction morphisms and cover witnesses."""

from __future__ import annotations

from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.objects.contractions import contract_edges


def test_loop_contraction_adds_one_to_genus():
    types = StableGraphs(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    graph = loop.canonical_representative()
    edge = graph.internal_edges()[0]
    image, contraction = graph.contract(edge)
    assert image.is_smooth()
    assert image.total_genus() == 1
    assert image.vertex_genera() == (1,)
    assert contraction.domain() == graph
    assert contraction.codomain() == image.canonical_representative()
    assert contraction.num_contracted_edges() == 1


def test_nonloop_contraction_merges_and_sums_genera():
    types = StableGraphs(1, 2)
    gamma = types.from_vertices(genera=(1, 0), markings=((), (1, 2)), edges=((0, 1),))
    graph = gamma.canonical_representative()
    edge = graph.internal_edges()[0]
    image, contraction = graph.contract(edge)
    assert image.is_smooth()
    assert image.total_genus() == 1
    assert image.vertex_genera() == (1,)
    assert len(contraction.vertex_fibres()) == 1
    assert contraction.vertex_fibres()[0] == frozenset({0, 1})


def test_every_contraction_preserves_total_genus_and_stability():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        for gamma in StableGraphs(g, n):
                graph = gamma.canonical_representative()
                for edge in graph.internal_edges():
                    image, _ = graph.contract(edge)
                    assert image.total_genus() == gamma.total_genus()
                    assert image.is_stable()
                    assert image.num_edges() == gamma.num_edges() - 1


def test_contraction_composition_contracts_the_union_of_edges():
    types = StableGraphs(0, 5)
    # A chain of two edges: three genus-0 vertices in a path.
    gamma = types.from_vertices(
        genera=(0, 0, 0),
        markings=((1, 2), (3,), (4, 5)),
        edges=((0, 1), (1, 2)),
    )
    graph = gamma.canonical_representative()
    edges = graph.internal_edges()
    _, first = graph.contract(edges[0])
    # contract the surviving edge of the intermediate graph
    intermediate = first.codomain()
    second_edge = intermediate.internal_edges()[0]
    _, second = intermediate.contract(second_edge)
    composite = first.compose(second)
    assert composite.domain() == graph
    assert composite.num_contracted_edges() == 2
    assert composite.codomain().graph_type().is_smooth()
    # contracting both edges directly agrees with the composite
    direct, _ = contract_edges(graph, edges)
    assert direct.canonical_representative() == composite.codomain()
