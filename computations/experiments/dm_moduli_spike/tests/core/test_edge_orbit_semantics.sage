r"""Tier-4 internal consistency: Aut edge-orbit semantics vs contraction fibers."""

from __future__ import annotations

from collections import Counter

from dm_moduli_spike.objects.model import DMCompactificationModel

from dm_moduli_spike.objects.edge_orbits import _elementary_contraction_data, contraction_target_multiset
from tests.support.fixtures import genus_six_counterexample, m12_types


def test_genus_six_counterexample_has_distinct_aut_orbits_same_target():
    gamma = genus_six_counterexample()
    assert gamma.automorphism_number() == 1
    data = _elementary_contraction_data(gamma)
    assert len(data) == 8
    assert all(size == 1 for _target, _witness, size in data)
    target_counts = Counter(target.canonical_key() for target, _witness, _size in data)
    assert max(target_counts.values()) == 2
    duplicated = next(key for key, count in target_counts.items() if count == 2)
    matched = [entry for entry in data if entry[0].canonical_key() == duplicated]
    assert matched[0][0] == matched[1][0]


def test_M12_type_E_parallel_orbit_has_size_two():
    m12_e = m12_types(DMCompactificationModel(1, 2).stratification())["E"].curve_type()
    data = _elementary_contraction_data(m12_e)
    assert len(data) == 1
    assert data[0][2] == 2


def test_contraction_target_multiset_matches_covers():
    gamma = genus_six_counterexample()
    multiset = contraction_target_multiset(gamma)
    assert len(multiset) == 8
    assert len({target.canonical_key() for target, _size in multiset}) == 7


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
                pure_data = _elementary_contraction_data(pure_by_key[key])
                decorated_data = _elementary_contraction_data(delta)
                assert len(pure_data) == len(decorated_data)
                assert sorted(size for _target, _witness, size in pure_data) == sorted(
                    size for _target, _witness, size in decorated_data
                )
