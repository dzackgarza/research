r"""CI-tier rank-vector and backend cross-checks on larger moduli spaces."""

from __future__ import annotations

import pytest

from dm_moduli_spike._admcycles.admcycles_stable import AdmcyclesStableGraphs
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.fixtures import rank_sizes, strata_by_codimension

pytestmark = pytest.mark.ci

LARGE_RANK_VECTORS = [
    ((0, 5), (1, 10, 15)),
    ((2, 1), (1, 2, 5, 5, 3)),
]


@pytest.mark.parametrize("gn,expected", LARGE_RANK_VECTORS)
def test_rank_vectors_match_fixtures(gn, expected):
    g, n = gn
    sizes = rank_sizes(g, n)
    assert sizes == expected
    assert StableGraphs(g, n).cardinality() == sum(expected)
    assert StableGraphs(g, n).dimension() == 3 * g - 3 + n
    assert max(gamma.num_edges() for gamma in StableGraphs(g, n)) == 3 * g - 3 + n


def test_bucketing_is_by_num_edges_not_generation_provenance():
    for codim, bucket in enumerate(strata_by_codimension(2, 1)):
        for stratum in bucket:
            assert stratum.num_edges() == codim
            assert stratum.codimension() == codim


def test_admcycles_stable_backend_matches_pure_sage_canonical_keys():
    backend = AdmcyclesStableGraphs()
    for g, n in [(0, 5), (1, 2), (2, 0), (2, 1)]:
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


def test_full_M21_enumeration_is_present():
    assert StableGraphs(2, 1).cardinality() == sum(rank_sizes(2, 1)) == 16
