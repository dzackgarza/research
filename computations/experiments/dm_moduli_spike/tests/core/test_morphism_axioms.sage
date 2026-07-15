r"""Tier-4 internal consistency: executable graph isomorphism and contraction axioms."""

from __future__ import annotations

from dm_moduli_spike.objects.contractions import _contract_edges
from dm_moduli_spike.objects.isomorphisms import StableGraphIsomorphism, canonicalize, identity_isomorphism
from dm_moduli_spike.objects.stable_graphs import StableGraphs


def test_identity_isomorphism_passes_post_init():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    graph = gamma._canonical_record()
    iso = identity_isomorphism(graph)
    assert iso.source == graph
    assert iso.target == graph


def test_canonicalization_certificate_is_valid_isomorphism():
    types = StableGraphs(1, 2)
    gamma = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    graph = gamma._canonical_record()
    cert = canonicalize(graph)
    assert isinstance(cert, StableGraphIsomorphism)
    assert cert.source == graph


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
    graph = gamma._canonical_record()
    _, composite = _contract_edges(graph, graph.internal_edges())
    assert composite.num_contracted_edges() == 2
    assert composite.is_identity() is False
