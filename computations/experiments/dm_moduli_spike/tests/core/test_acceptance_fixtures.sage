r"""Acceptance fixtures: exact rank vectors of the stratification poset.

Rank vectors and total cardinalities are secondary diagnostics.  The primary
correctness claims live in the whole-poset oracle and Hasse-diagram tests.
"""

from __future__ import annotations

import pytest

from dm_moduli_spike import DMCompactificationModel

RANK_VECTORS = [
    ((0, 3), (1,)),
    ((0, 4), (1, 3)),
    ((1, 1), (1, 1)),
    ((0, 5), (1, 10, 15)),
    ((1, 2), (1, 2, 2)),
    ((2, 0), (1, 2, 2, 2)),
    ((2, 1), (1, 2, 5, 5, 3)),
]


@pytest.mark.parametrize("gn,expected", RANK_VECTORS)
def test_rank_vectors_match_fixtures(gn, expected):
    g, n = gn
    model = DMCompactificationModel(g, n)
    stratification = model.stratification()
    assert stratification.rank_sizes() == expected
    assert stratification.cardinality() == sum(expected)
    assert stratification.is_complete()
    assert stratification.dimension() == 3 * g - 3 + n
    assert stratification.maximum_codim() == 3 * g - 3 + n


def test_bucketing_is_by_num_edges_not_generation_provenance():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification()
    for codim, bucket in enumerate(stratification.rank_buckets()):
        for stratum in bucket:
            assert stratum.curve_type().num_edges() == codim
            assert stratum.codimension() == codim


def test_admcycles_stable_backend_matches_pure_sage_canonical_keys():
    for g, n in [(0, 4), (1, 1), (0, 5), (1, 2), (2, 0), (2, 1)]:
        model = DMCompactificationModel(g, n)
        pure = model.stratification(backend="pure-sage")
        adm = model.stratification(backend="admcycles-stable")
        pure_keys = {
            gamma.canonical_key()
            for level in pure.curve_type_levels()
            for gamma in level
        }
        adm_keys = {
            gamma.canonical_key()
            for level in adm.curve_type_levels()
            for gamma in level
        }
        assert pure_keys == adm_keys
        assert pure.rank_sizes() == adm.rank_sizes()


def test_truncated_stratification_is_marked_incomplete():
    model = DMCompactificationModel(2, 1)
    truncated = model.stratification(max_codim=2)
    assert not truncated.is_complete()
    assert truncated.maximum_codim() == 2
    assert truncated.rank_sizes() == (1, 2, 5)
    # The full object, by contrast, is complete.
    assert model.stratification().is_complete()
