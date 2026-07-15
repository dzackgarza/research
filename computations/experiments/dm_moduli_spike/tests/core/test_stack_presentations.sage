r"""Tier-4: geometric quotient-stack and clutching presentations via Mbar stratification."""

from __future__ import annotations

from sage.rings.integer_ring import ZZ

from dm_moduli_spike import Mbar_gn, ProductStack, QuotientStack, spec
from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.objects.stable_graphs import StableGraphs


def test_open_stack_presentation_factors_and_group_order():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    graph = gamma._canonical_record()
    XSbar = Mbar_gn(0, 4, base=spec(ZZ))
    S = XSbar.stratification().stratum(gamma)
    underlying = S.underlying_stack()
    assert isinstance(underlying, QuotientStack)
    assert int(underlying.group().order()) == gamma.automorphism_number()
    factors = S.clutching_morphism().domain().factors()
    assert sorted((f.genus(), f.number_of_markings()) for f in factors) == [(0, 3), (0, 3)]
    assert [flags for _g, flags in Gamma_clutching_flags(graph)] == [(0, 1, 4), (2, 3, 5)]


def test_closure_normalization_uses_compact_factors():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    graph = gamma._canonical_record()
    XSbar = Mbar_gn(0, 4, base=spec(ZZ))
    S = XSbar.stratification().stratum(gamma)
    factors = S.clutching_morphism().domain().factors()
    assert all(f.is_proper() for f in factors)
    assert sorted((f.genus(), f.number_of_markings()) for f in factors) == [(0, 3), (0, 3)]


def test_clutching_morphism_targets_the_ambient_compactification():
    types = StableGraphs(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    graph = loop._canonical_record()
    XSbar = Mbar_gn(1, 1, base=spec(ZZ))
    S = XSbar.stratification().stratum(loop)
    xi = S.clutching_morphism()
    assert xi in xi.parent()
    assert xi.codomain() is XSbar
    assert isinstance(xi.domain(), ProductStack)
    assert [(f.genus(), f.number_of_markings()) for f in xi.domain().factors()] == [(0, 3)]
    assert int(S.underlying_stack().group().order()) == 2


def test_m04_boundary_clutching_maps_are_pairwise_distinct():
    XSbar = Mbar_gn(0, 4, base=spec(ZZ))
    Sigma = XSbar.stratification()
    boundary = [S for S in Sigma.strata() if S.index().num_edges() == 1]
    assert len(boundary) == 3
    keys = {S.index().canonical_key() for S in boundary}
    assert len(keys) == 3
    assert len({id(S.clutching_morphism()) for S in boundary}) == 3
    assert len({S.index() for S in boundary}) == 3


def test_stable_graphs_rejects_mismatched_ambient():
    wrong = StableGraphs(2, 1).smooth()
    try:
        StableGraphs(0, 4)(wrong)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for mismatched ambient (g, n)")


def test_geometric_stratum_is_distinct_from_indexing_graph_type():
    types = StableGraphs(1, 1)
    smooth = types.smooth()
    XSbar = Mbar_gn(1, 1, base=spec(ZZ))
    S = XSbar.stratification().stratum(smooth)
    assert hasattr(smooth, "automorphism_number")
    assert hasattr(smooth, "one_edge_degenerations")
    assert hasattr(S, "underlying_stack")
    assert hasattr(S, "clutching_morphism")
    assert not hasattr(smooth, "underlying_stack")
    assert not hasattr(S, "one_edge_degenerations")


def Gamma_clutching_flags(graph):
    from dm_moduli_spike.objects.stable_graphs import StableGraph, StableGraphs

    if not isinstance(graph, StableGraph):
        graph = StableGraphs(graph.genus(), graph.num_markings())(graph)
    return StableGraphCategory(graph.genus(), graph.num_markings()).clutching_source(graph)
