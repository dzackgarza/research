r"""Aut edge-orbit semantics versus contraction-target fibers."""

from __future__ import annotations

from collections import Counter

from dm_moduli_spike import DMCompactificationModel
from tests.support.fixtures import genus_six_counterexample, m12_types


def test_genus_six_counterexample_has_distinct_aut_orbits_same_target():
    gamma = genus_six_counterexample()
    assert gamma.automorphism_number() == 1
    orbits = gamma.elementary_contraction_orbits()
    assert len(orbits) == 8
    assert all(orbit.orbit_size() == 1 for orbit in orbits)
    target_counts = Counter(orbit.target().canonical_key() for orbit in orbits)
    assert max(target_counts.values()) == 2
    duplicated = next(key for key, count in target_counts.items() if count == 2)
    matched = [orbit for orbit in orbits if orbit.target().canonical_key() == duplicated]
    assert matched[0].target() == matched[1].target()


def test_M12_type_E_parallel_orbit_has_size_two():
    m12_e = m12_types(DMCompactificationModel(1, 2).stratification())["E"].curve_type()
    orbits = m12_e.elementary_contraction_orbits()
    assert len(orbits) == 1
    assert orbits[0].orbit_size() == 2


def test_decorated_and_pure_sage_orbit_data_agree():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        model = DMCompactificationModel(g, n)
        pure = model.stratification(backend="pure-sage")
        decorated = model.stratification(backend="admcycles-decorated")
        pure_by_key = {
            gamma.canonical_key(): gamma
            for level in pure.curve_type_levels()
            for gamma in level
        }
        for level in decorated.curve_type_levels():
            for delta in level:
                key = delta.canonical_key()
                assert key in pure_by_key
                pure_orbits = pure_by_key[key].elementary_contraction_orbits()
                decorated_orbits = delta.elementary_contraction_orbits()
                assert len(pure_orbits) == len(decorated_orbits)
                assert sorted(orbit.orbit_size() for orbit in pure_orbits) == sorted(
                    orbit.orbit_size() for orbit in decorated_orbits
                )
