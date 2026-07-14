r"""Tier-5 diagnostics: exact rank vectors of the stratification poset.

Rank vectors and total cardinalities are never primary correctness claims.
Tier-1 whole-poset oracles and tier-4 Hasse-diagram tests carry the evidence.
"""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import _enumerate_stable_graph_levels
from dm_moduli_spike.objects.stable_graphs import StableGraphs


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
    stratification = _enumerate_stable_graph_levels(g, n)
    assert stratification.rank_sizes() == expected
    assert stratification.cardinality() == sum(expected)
    assert stratification.is_complete()
    assert stratification.dimension() == 3 * g - 3 + n
    assert stratification.maximum_codim() == 3 * g - 3 + n


def test_bucketing_is_by_num_edges_not_generation_provenance():
    stratification = _enumerate_stable_graph_levels(1, 2)
    for codim, bucket in enumerate(stratification.strata_by_codimension()):
        for stratum in bucket:
            assert stratum.num_edges() == codim
            assert stratum.codimension() == codim


def test_admcycles_stable_backend_matches_pure_sage_canonical_keys():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        pure = _enumerate_stable_graph_levels(g, n, backend="pure-sage")
        adm = _enumerate_stable_graph_levels(g, n, backend="admcycles-stable")
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
    truncated = _enumerate_stable_graph_levels(1, 2, max_codim=1)
    assert not truncated.is_complete()
    assert truncated.maximum_codim() == 1
    assert truncated.rank_sizes() == (1, 2)
    assert _enumerate_stable_graph_levels(1, 2).is_complete()


def test_empty_external_enumeration_is_not_marked_complete():
    from dm_moduli_spike.objects.stratification import _build_stratification_from_types

    curve_types = StableGraphs(2, 1)
    incomplete = _build_stratification_from_types(curve_types, ())
    assert not incomplete.is_complete()
    assert incomplete.rank_sizes() == (1,)
