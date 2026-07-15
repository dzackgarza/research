r"""Tier-4: isomorphism certificates and contraction morphisms on StableGraph."""

from __future__ import annotations

from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.objects.stable_graphs import StableGraphs


def test_identity_morphism_is_isomorphism():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    morph = StableGraphCategory(0, 4).identity(gamma)
    assert morph.domain() == gamma
    assert morph.codomain() == gamma
    assert morph.is_isomorphism()
    assert morph.num_contracted_edges() == 0


def test_from_vertices_returns_canonical_stable_graph():
    types = StableGraphs(1, 2)
    gamma = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    again = types.from_vertices(genera=(0, 0), markings=((2,), (1,)), edges=((0, 1), (0, 1)))
    assert gamma == again
    assert gamma.parent() is types


def test_contraction_witnesses_from_orbit_data_validate():
    types = StableGraphs(1, 2)
    gamma = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    for target, witness, orbit_size in gamma.elementary_contractions():
        assert witness.num_contracted_edges() == 1
        assert orbit_size >= 1
        assert witness.codomain() == target
        assert witness.codomain().num_edges() == gamma.num_edges() - 1
        assert witness.is_contraction()


def test_multi_edge_contraction_validates():
    types = StableGraphs(0, 5)
    gamma = types.from_vertices(
        genera=(0, 0, 0),
        markings=((1, 2), (3,), (4, 5)),
        edges=((0, 1), (1, 2)),
    )
    morph = StableGraphCategory(0, 5).contract(gamma, gamma.internal_edges())
    assert morph.num_contracted_edges() == 2
    assert morph.is_isomorphism() is False
    assert morph.is_contraction()
