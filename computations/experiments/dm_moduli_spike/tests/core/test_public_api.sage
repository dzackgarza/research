r"""Tier-4 internal consistency: user-facing public API surface."""

from __future__ import annotations

import pytest

from dm_moduli_spike import DMCompactificationModel, StableGraphCategory, StableGraphTypes


def test_gamma_is_public_entry_point():
    Gamma = StableGraphCategory(1, 1)
    assert Gamma.genus() == 1
    assert len(Gamma.objects()) == 2
    assert Gamma.specialization_poset().cardinality() == 2


def test_legacy_model_still_importable():
    model = DMCompactificationModel(2, 1)
    assert model.genus() == 2
    assert model.number_of_markings() == 1
    assert model.dimension() == 4
    assert model.is_stable_range()


def test_direct_stable_graph_constructor_and_stratum():
    model = DMCompactificationModel(0, 4)
    types = model.graph_types()
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    assert gamma.total_genus() == 0
    assert gamma.num_edges() == 1
    stratum = model.stratum(gamma)
    assert stratum.codimension() == 1


def test_stable_graph_types_parent_protocol():
    types = StableGraphTypes(0, 4)
    smooth = types.smooth()
    assert smooth.num_edges() == 0
    assert types(smooth) is smooth
