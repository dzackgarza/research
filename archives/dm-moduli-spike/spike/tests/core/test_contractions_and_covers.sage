r"""Tier-4: contraction morphisms and covers via public Γ / StableGraph APIs."""

from __future__ import annotations

from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.objects.stable_graphs import StableGraphs


def test_loop_contraction_adds_one_to_genus():
    types = StableGraphs(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    Gamma = StableGraphCategory(1, 1)
    edge = loop.internal_edges()[0]
    morph = Gamma.contract(loop, (edge,))
    image = morph.codomain()
    assert image.is_smooth()
    assert image.total_genus() == 1
    assert image.vertex_genera() == (1,)
    assert morph.domain() == loop
    assert morph.num_contracted_edges() == 1
    assert morph.is_contraction()


def test_nonloop_contraction_merges_and_sums_genera():
    types = StableGraphs(1, 2)
    gamma = types.from_vertices(genera=(1, 0), markings=((), (1, 2)), edges=((0, 1),))
    Gamma = StableGraphCategory(1, 2)
    edge = gamma.internal_edges()[0]
    morph = Gamma.contract(gamma, (edge,))
    image = morph.codomain()
    assert image.is_smooth()
    assert image.total_genus() == 1
    assert image.vertex_genera() == (1,)
    assert morph.num_contracted_edges() == 1


def test_every_contraction_preserves_total_genus_and_stability():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        Gamma = StableGraphCategory(g, n)
        for gamma in StableGraphs(g, n):
            for edge in gamma.internal_edges():
                morph = Gamma.contract(gamma, (edge,))
                image = morph.codomain()
                assert image.total_genus() == gamma.total_genus()
                assert image.is_stable()
                assert image.num_edges() == gamma.num_edges() - 1


def test_multi_edge_contraction_agrees_with_elementary_orbit_chain():
    types = StableGraphs(0, 5)
    gamma = types.from_vertices(
        genera=(0, 0, 0),
        markings=((1, 2), (3,), (4, 5)),
        edges=((0, 1), (1, 2)),
    )
    Gamma = StableGraphCategory(0, 5)
    edges = gamma.internal_edges()
    direct = Gamma.contract(gamma, edges)
    assert direct.num_contracted_edges() == 2
    assert direct.domain() == gamma
    assert direct.codomain().is_smooth()
    assert direct.codomain().total_genus() == 0
