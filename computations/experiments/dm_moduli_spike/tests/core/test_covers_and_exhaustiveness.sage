r"""Cover API deduplication and exhaustive-cap normalization."""

from __future__ import annotations

from dm_moduli_spike import DMCompactificationModel
from dm_moduli_spike.objects.stratification import build_stratification_from_types
from tests.support.fixtures import genus_six_counterexample


def test_cover_types_deduplicates_aut_orbit_targets():
    gamma = genus_six_counterexample()
    covers = gamma.covers()
    cover_types = gamma.cover_types()
    assert covers == cover_types
    assert len(covers) == 7
    targets = {target.canonical_key() for target, _source in covers}
    assert len(targets) == len(covers)


def test_stratification_has_one_witness_per_cover():
    gamma = genus_six_counterexample()
    parents = {orbit.target() for orbit in gamma.elementary_contraction_orbits()}
    mini = build_stratification_from_types(gamma.parent(), (gamma, *parents))
    assert len(mini.covers()) == 7
    assert len(mini.contraction_witnesses()) == 7


def test_max_codim_at_least_dimension_is_exhaustive():
    for g, n in [(0, 4), (1, 2), (2, 0)]:
        model = DMCompactificationModel(g, n)
        dimension = model.dimension()
        full = model.stratification()
        capped = model.stratification(max_codim=dimension)
        overshot = model.stratification(max_codim=dimension + 10)
        for stratification in (full, capped, overshot):
            assert stratification.is_exhaustive()
            assert stratification.is_full_stratification()
            assert stratification.enumeration_result().complete_through_codim == stratification.maximum_codim()
        assert full.rank_sizes() == capped.rank_sizes() == overshot.rank_sizes()


def test_truncated_enumeration_reports_incomplete_codim():
    model = DMCompactificationModel(2, 1)
    truncated = model.stratification(max_codim=2)
    assert not truncated.is_exhaustive()
    assert truncated.enumeration_result().complete_through_codim == -1
