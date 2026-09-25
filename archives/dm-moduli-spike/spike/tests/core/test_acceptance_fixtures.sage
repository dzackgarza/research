r"""Tier-5 diagnostics: exact rank vectors of the stratification poset.

Rank vectors and total cardinalities are never primary correctness claims.
Tier-1 whole-poset oracles and tier-4 Hasse-diagram tests carry the evidence.
"""

from __future__ import annotations

import pytest

from dm_moduli_spike._admcycles.admcycles_stable import AdmcyclesStableGraphs
from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.fixtures import rank_sizes, strata_by_codimension


RANK_VECTORS = [
    ((0, 3), (1,)),
    ((0, 4), (1, 3)),
    ((1, 1), (1, 1)),
    ((1, 2), (1, 2, 2)),
    ((2, 0), (1, 2, 2, 2)),
]


@pytest.mark.parametrize("gn,expected", RANK_VECTORS)
def test_rank_vectors_match_fixtures(gn, expected):
    g, n = gn
    sizes = rank_sizes(g, n)
    assert sizes == expected
    assert sum(sizes) == StableGraphs(g, n).cardinality()
    assert StableGraphs(g, n).dimension() == 3 * g - 3 + n
    assert max((gamma.num_edges() for gamma in StableGraphs(g, n)), default=-1) == 3 * g - 3 + n


def test_bucketing_is_by_num_edges_not_generation_provenance():
    for codim, bucket in enumerate(strata_by_codimension(1, 2)):
        for stratum in bucket:
            assert stratum.num_edges() == codim
            assert stratum.codimension() == codim


def test_admcycles_stable_backend_matches_pure_sage_canonical_keys():
    backend = AdmcyclesStableGraphs()
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        types = StableGraphs(g, n)
        pure_keys = {gamma.canonical_key() for gamma in types}
        adm = tuple(backend.stable_curve_types(types))
        adm_keys = {gamma.canonical_key() for gamma in adm}
        assert pure_keys == adm_keys
        adm_sizes = tuple(
            sum(1 for gamma in adm if gamma.num_edges() == codim)
            for codim in range(max(gamma.num_edges() for gamma in adm) + 1)
        )
        assert rank_sizes(g, n) == adm_sizes


def test_truncated_poset_omits_higher_codimension():
    truncated = StableGraphCategory(1, 2).truncate(1)
    assert all(gamma.num_edges() <= 1 for gamma in truncated)
    assert truncated.cardinality() == sum(rank_sizes(1, 2)[:2])
    assert StableGraphs(1, 2).cardinality() == sum(rank_sizes(1, 2))


def test_empty_backend_enumeration_disagrees_with_stable_graphs():
    types = StableGraphs(2, 1)
    incomplete_keys = frozenset()
    assert incomplete_keys != {gamma.canonical_key() for gamma in types}
    assert types.cardinality() > 1
