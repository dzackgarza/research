r"""CI-tier rank-vector and backend cross-checks on larger moduli spaces."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import DMCompactificationModel


pytestmark = pytest.mark.ci

LARGE_RANK_VECTORS = [
    ((0, 5), (1, 10, 15)),
    ((2, 1), (1, 2, 5, 5, 3)),
]


@pytest.mark.parametrize("gn,expected", LARGE_RANK_VECTORS)
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
    for codim, bucket in enumerate(stratification.strata_by_codimension()):
        for stratum in bucket:
            assert stratum.curve_type().num_edges() == codim
            assert stratum.codimension() == codim


def test_admcycles_stable_backend_matches_pure_sage_canonical_keys():
    for g, n in [(0, 5), (1, 2), (2, 0), (2, 1)]:
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


def test_full_M21_stratification_is_complete():
    model = DMCompactificationModel(2, 1)
    assert model.stratification().is_complete()
