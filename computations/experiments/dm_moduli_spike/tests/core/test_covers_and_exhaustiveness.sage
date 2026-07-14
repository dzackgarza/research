r"""Tier-4 internal consistency: cover deduplication and exhaustive enumeration."""

from __future__ import annotations

from dm_moduli_spike.objects.edge_orbits import _elementary_contraction_data
from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.fixtures import genus_six_counterexample, rank_sizes


def test_covers_deduplicates_aut_orbit_targets():
    gamma = genus_six_counterexample()
    covers = gamma.covers()
    assert len(covers) == 7
    targets = {target.canonical_key() for target, _source in covers}
    assert len(targets) == len(covers)


def test_genus_six_has_eight_orbits_and_seven_covers():
    gamma = genus_six_counterexample()
    assert len(_elementary_contraction_data(gamma)) == 8
    assert len(gamma.covers()) == 7


def test_orbit_data_has_one_witness_per_orbit():
    gamma = genus_six_counterexample()
    data = _elementary_contraction_data(gamma)
    assert len(data) == 8
    distinct_targets = {target.canonical_key() for target, _witness, _size in data}
    assert len(distinct_targets) == 7
    assert len(gamma.covers()) == 7


def test_full_enumeration_matches_truncated_at_dimension_cap():
    for g, n in [(0, 4), (1, 2), (2, 0)]:
        dimension = StableGraphs(g, n).dimension()
        full = StableGraphCategory(g, n).specialization_poset()
        capped = StableGraphCategory(g, n).truncate(dimension)
        overshot = StableGraphCategory(g, n).truncate(dimension + 10)
        assert full.cardinality() == capped.cardinality() == overshot.cardinality()
        assert rank_sizes(g, n) == tuple(
            sum(1 for gamma in StableGraphs(g, n) if gamma.num_edges() == codim)
            for codim in range(dimension + 1)
        )
