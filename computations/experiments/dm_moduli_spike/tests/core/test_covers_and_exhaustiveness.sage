r"""Tier-4 internal consistency: cover deduplication and exhaustive-cap normalization."""

from __future__ import annotations

from dm_moduli_spike.objects.model import StableGraphStratificationEnumerator

from dm_moduli_spike.objects.edge_orbits import _elementary_contraction_data
from dm_moduli_spike.objects.stratification import build_stratification_from_types
from dm_moduli_spike.testing_support.support.fixtures import genus_six_counterexample


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


def test_stratification_has_one_witness_per_cover():
    gamma = genus_six_counterexample()
    parents = {target for target, _witness, _size in _elementary_contraction_data(gamma)}
    mini = build_stratification_from_types(gamma.parent(), (gamma, *parents))
    assert len(mini.covers()) == 7
    assert len(mini.contraction_witnesses()) == 7


def test_max_codim_at_least_dimension_is_exhaustive():
    for g, n in [(0, 4), (1, 2), (2, 0)]:
        model = StableGraphStratificationEnumerator(g, n)
        dimension = model.dimension()
        full = model.stratification()
        capped = model.stratification(max_codim=dimension)
        overshot = model.stratification(max_codim=dimension + 10)
        for stratification in (full, capped, overshot):
            assert stratification.is_exhaustive()
            assert stratification.is_full_stratification()
            assert stratification.complete_through_codim() == stratification.maximum_codim()
        assert full.rank_sizes() == capped.rank_sizes() == overshot.rank_sizes()

