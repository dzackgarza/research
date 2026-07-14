r"""Induced subposets from arbitrary stable-type subsets."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import _enumerate_stable_graph_levels
from dm_moduli_spike.objects.stable_graphs import StableGraphs

from dm_moduli_spike.objects.stratification import _build_stratification_from_types

pytestmark = pytest.mark.ci


def test_intermediate_deletion_adds_direct_cover():
    full = _enumerate_stable_graph_levels(2, 1)
    smooth = StableGraphs(2, 1).smooth()
    codim_two = full.curve_type_levels()[2][0]
    subset = _build_stratification_from_types(
        StableGraphs(2, 1),
        (smooth, codim_two),
        induced_order=True,
    )
    assert subset.is_induced_subposet()
    assert len(subset.covers()) == 1
    generic, special = subset.covers()[0]
    assert generic == smooth
    assert special == codim_two
    poset = subset.specialization_poset()
    assert poset.is_lequal(generic, special)
    assert poset.cover_relations() == [[generic, special]]


def test_induced_subposet_rank_differs_from_ambient_codimension():
    full = _enumerate_stable_graph_levels(2, 1)
    smooth = StableGraphs(2, 1).smooth()
    codim_two = full.curve_type_levels()[2][0]
    subset = _build_stratification_from_types(
        StableGraphs(2, 1),
        (smooth, codim_two),
        induced_order=True,
    )
    poset = subset.specialization_poset()
    _, special = subset.covers()[0]
    assert special.codimension() == 2
    assert poset.rank(special) == 1
    witness = subset.contraction_witnesses()[0]
    assert witness.num_contracted_edges() == 2


def test_adjacent_rank_mode_skips_nonconsecutive_covers():
    full = _enumerate_stable_graph_levels(2, 1)
    smooth = StableGraphs(2, 1).smooth()
    codim_two = full.curve_type_levels()[2][0]
    subset = _build_stratification_from_types(
        StableGraphs(2, 1),
        (smooth, codim_two),
        induced_order=False,
    )
    assert not subset.is_induced_subposet()
    assert subset.covers() == ()
