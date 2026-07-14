r"""Tier-4: StableGraphCategory (Gamma_{g,n}) core API and combinatorial oracles."""

from __future__ import annotations

import pytest
from sage.combinat.posets.posets import FinitePoset

from dm_moduli_spike import StableGraphCategory
from dm_moduli_spike.objects.model import _enumerate_stable_graph_levels
from dm_moduli_spike.testing_support.support.poset_oracle import expected_M0n_specialization_poset


def test_gamma_objects_and_homsets_M11():
    Gamma = StableGraphCategory(1, 1)
    objects = Gamma.objects()
    assert len(objects) == 2
    smooth, special = objects
    assert smooth.num_edges() == 0
    assert special.num_edges() == 1
    assert len(Gamma.hom(special, smooth)) >= 1
    assert len(Gamma.hom(smooth, special)) == 0
    ident = Gamma.identity(smooth)
    assert ident.is_isomorphism()


def test_gamma_specialization_poset_matches_enumerator_M11():
    Gamma = StableGraphCategory(1, 1)
    P = Gamma.specialization_poset()
    assert isinstance(P, FinitePoset)
    legacy = _enumerate_stable_graph_levels(1, 1).specialization_poset()
    assert P.cardinality() == legacy.cardinality()
    assert P.is_isomorphic(legacy)


def test_morphism_factors_as_contraction_then_isomorphism_M11():
    Gamma = StableGraphCategory(1, 1)
    smooth, special = Gamma.objects()
    morph = Gamma.hom(special, smooth).an_element()
    assert morph.contracted_edges()
    # Surviving half-edge injection is bijective onto codomain flags when |E_c|=|E(dom)|-|E(cod)|
    injection = morph.surviving_half_edge_injection()
    assert sorted(injection.keys()) == list(range(smooth.num_flags()))
    assert morph.codomain() == smooth


def test_aut_equals_end_units_M11():
    Gamma = StableGraphCategory(1, 1)
    for graph in Gamma.objects():
        units = [m for m in Gamma.end(graph) if m.is_isomorphism()]
        autos = Gamma.automorphism_morphisms(graph)
        assert len(units) == len(autos)
        assert set(units) == set(autos)
        assert Gamma.identity(graph) in units


def test_he_functors_contravariant_on_contraction_M11():
    Gamma = StableGraphCategory(1, 1)
    smooth, special = Gamma.objects()
    morph = Gamma.hom(special, smooth).an_element()
    h_map = Gamma.half_edge_map(morph)
    assert len(h_map) == smooth.num_flags()
    e_map = Gamma.edge_map(morph)
    assert e_map == {}  # smooth has no edges


def test_boundary_terms_are_distinct_M12():
    Gamma = StableGraphCategory(1, 2)
    divisors = Gamma.boundary_divisors()
    boundary = Gamma.strata_in_boundary()
    deepest = Gamma.deepest_strata()
    assert all(g.num_edges() == 1 for g in divisors)
    assert set(divisors).issubset(set(boundary))
    assert all(g.num_edges() >= 1 for g in boundary)
    max_e = max(g.num_edges() for g in Gamma.objects())
    assert all(g.num_edges() == max_e for g in deepest)
    assert set(deepest).issubset(set(boundary))


def test_clutching_source_and_node_pairings_M11():
    Gamma = StableGraphCategory(1, 1)
    special = next(g for g in Gamma.objects() if g.num_edges() == 1)
    factors = Gamma.clutching_source(special)
    assert len(factors) == special.num_vertices()
    genus, flags = factors[0]
    assert genus == 0
    assert len(flags) == 3  # two half-edges of the node + one marking
    pairings = Gamma.node_pairings(special)
    assert len(pairings) == 1


def test_codimension_equals_num_edges():
    Gamma = StableGraphCategory(1, 2)
    for graph in Gamma.objects():
        assert Gamma.codimension(graph) == graph.num_edges()
        assert Gamma.stratum_dimension(graph) == Gamma.dimension() - graph.num_edges()


def test_truncation_is_induced_subposet_by_edge_count():
    Gamma = StableGraphCategory(1, 2)
    full = Gamma.specialization_poset()
    truncated = Gamma.truncate(1)
    assert isinstance(truncated, FinitePoset)
    assert all(g.num_edges() <= 1 for g in truncated)
    assert truncated.cardinality() < full.cardinality() or all(g.num_edges() <= 1 for g in Gamma.objects())


def test_closure_poset_is_dual():
    Gamma = StableGraphCategory(1, 1)
    assert Gamma.closure_poset() == Gamma.specialization_poset().dual()


def test_native_automorphism_group_api_M12_banana():
    from dm_moduli_spike.testing_support.support.fixtures import m12_types

    Gamma = StableGraphCategory(1, 2)
    banana = m12_types()["E"].canonical_representative()
    edge_aut = banana.automorphism_group(on="edges")
    assert edge_aut.order() == 2
    flag_aut = Gamma.automorphism_group(banana, on="half_edges")
    assert flag_aut.order() >= 2


@pytest.mark.ci
def test_thinification_matches_legacy_enumerator_small():
    for g, n in [(1, 1), (1, 2), (2, 0), (0, 4)]:
        Gamma = StableGraphCategory(g, n)
        P = Gamma.specialization_poset()
        legacy = _enumerate_stable_graph_levels(g, n, backend="pure-sage").specialization_poset()
        assert P.cardinality() == legacy.cardinality()
        assert P.is_isomorphic(legacy)


@pytest.mark.ci
def test_M0n_thinification_matches_split_oracle():
    Gamma = StableGraphCategory(0, 4)
    P = Gamma.specialization_poset()
    expected = expected_M0n_specialization_poset(4)
    assert P.cardinality() == expected.cardinality()
    assert P.is_isomorphic(expected)


def test_symmetric_delta_complex_M04_and_refuses_g_positive_dm_claim():
    from sage.rings.rational_field import QQ

    from dm_moduli_spike import SymmetricDeltaComplex

    Delta0 = SymmetricDeltaComplex(StableGraphCategory(0, 4))
    assert Delta0.as_dm_boundary_complex() == Delta0.order_complex()
    homology = Delta0.as_dm_boundary_complex().homology(base_ring=QQ)
    nonzero = {d: g.dimension() for d, g in homology.items() if g.dimension() != 0}
    assert nonzero == {0: 2}  # n-4=0, (n-2)! = 2 for n=4

    Delta1 = StableGraphCategory(1, 1).symmetric_delta_complex()
    assert Delta1.cone_dimension(Delta1.category().objects()[1]) == 1
    try:
        Delta1.as_dm_boundary_complex()
        assert False, "expected ValueError for g>0"
    except ValueError as err:
        assert "g>0" in str(err)
