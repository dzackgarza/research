r"""Tier-4 internal consistency: executable graph isomorphism and contraction axioms."""

from __future__ import annotations

from dm_moduli_spike import StableGraph, StableGraphTypes
from dm_moduli_spike.objects.contractions import contract_edge, contract_edges
from dm_moduli_spike.objects.edge_orbits import _elementary_contraction_data
from dm_moduli_spike.objects.isomorphisms import StableGraphIsomorphism, canonicalize, identity_isomorphism


def test_identity_isomorphism_passes_post_init():
    types = StableGraphTypes(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    graph = gamma.canonical_representative()
    iso = identity_isomorphism(graph)
    assert iso.source == graph
    assert iso.target == graph


def test_canonicalization_certificate_is_valid_isomorphism():
    types = StableGraphTypes(1, 2)
    gamma = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    graph = gamma.canonical_representative()
    cert = canonicalize(graph)
    assert isinstance(cert, StableGraphIsomorphism)
    assert cert.source == graph


def test_contraction_witnesses_from_orbit_data_validate():
    types = StableGraphTypes(1, 2)
    gamma = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    for _target, witness, orbit_size in _elementary_contraction_data(gamma):
        assert witness.num_contracted_edges() == 1
        assert orbit_size >= 1
        assert witness.target_type().num_edges() == gamma.num_edges() - 1


def test_multi_edge_contraction_validates():
    types = StableGraphTypes(0, 5)
    gamma = types.from_vertices(
        genera=(0, 0, 0),
        markings=((1, 2), (3,), (4, 5)),
        edges=((0, 1), (1, 2)),
    )
    graph = gamma.canonical_representative()
    _, composite = contract_edges(graph, graph.internal_edges())
    assert composite.num_contracted_edges() == 2
    assert composite.is_identity() is False
