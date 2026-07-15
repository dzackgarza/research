r"""Tier-4 internal consistency: Aut edge-orbit semantics vs contraction fibers."""

from __future__ import annotations

from collections import Counter

from dm_moduli_spike._admcycles.admcycles_decorated import AdmcyclesDecoratedGraphs

from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.fixtures import genus_six_counterexample, m12_types


def test_genus_six_counterexample_has_distinct_aut_orbits_same_target():
    gamma = genus_six_counterexample()
    assert gamma.automorphism_number() == 1
    data = gamma.elementary_contractions()
    assert len(data) == 8
    assert all(size == 1 for _target, _witness, size in data)
    target_counts = Counter(target.canonical_key() for target, _witness, _size in data)
    assert max(target_counts.values()) == 2
    duplicated = next(key for key, count in target_counts.items() if count == 2)
    matched = [entry for entry in data if entry[0].canonical_key() == duplicated]
    assert matched[0][0] == matched[1][0]


def test_M12_type_E_parallel_orbit_has_size_two():
    m12_e = m12_types()["E"]
    data = m12_e.elementary_contractions()
    assert len(data) == 1
    assert data[0][2] == 2


def test_contraction_target_multiset_matches_covers():
    gamma = genus_six_counterexample()
    multiset = gamma.contraction_target_multiset()
    assert len(multiset) == 8
    assert len({target.canonical_key() for target, _size in multiset}) == 7


def test_decorated_and_pure_sage_orbit_data_agree():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        types = StableGraphs(g, n)
        pure_by_key = {gamma.canonical_key(): gamma for gamma in types}
        for delta in AdmcyclesDecoratedGraphs().stable_curve_types(types):
            key = delta.canonical_key()
            assert key in pure_by_key
            pure_data = pure_by_key[key].elementary_contractions()
            decorated_data = delta.elementary_contractions()
            assert len(pure_data) == len(decorated_data)
            assert sorted(size for _target, _witness, size in pure_data) == sorted(
                size for _target, _witness, size in decorated_data
            )
