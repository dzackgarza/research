r"""CI-tier mathematical invariant checks requiring full Mbar(2, 1) enumeration."""

from __future__ import annotations

import pytest

from dm_moduli_spike.backends.admcycles_stable import AdmcyclesStableGraphBackend
from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.fixtures import rank_sizes, strata_by_codimension

pytestmark = pytest.mark.ci


def test_external_backend_subset_disagrees_with_full_enumeration():
    curve_types = StableGraphs(2, 1)
    partial_keys = {curve_types.smooth().canonical_key()}
    full_keys = {gamma.canonical_key() for gamma in curve_types}
    assert partial_keys != full_keys

    backend = AdmcyclesStableGraphBackend()
    full = tuple(backend.stable_curve_types(curve_types))
    truncated = tuple(gamma for gamma in full if gamma.num_edges() <= 1)
    assert {gamma.canonical_key() for gamma in truncated} != full_keys
    assert max(gamma.num_edges() for gamma in truncated) == 1


def test_missing_type_still_spans_all_ranks():
    levels = strata_by_codimension(2, 1)
    all_types = [gamma for level in levels for gamma in level]
    removed = next(gamma for level in levels if len(level) > 1 for gamma in level)
    pruned = tuple(gamma for gamma in all_types if gamma is not removed)
    pruned_sizes = tuple(
        sum(1 for gamma in pruned if gamma.num_edges() == codim)
        for codim in range(StableGraphs(2, 1).dimension() + 1)
    )
    assert all(size > 0 for size in pruned_sizes)
    assert sum(pruned_sizes) == StableGraphs(2, 1).cardinality() - 1


def test_complete_enumeration_spans_all_ranks_M21():
    g, n = 2, 1
    assert len(rank_sizes(g, n)) == StableGraphs(g, n).dimension() + 1


def test_truncated_poset_stops_at_codim_cap():
    truncated = StableGraphCategory(2, 1).truncate(2)
    assert all(gamma.num_edges() <= 2 for gamma in truncated)
    assert max(gamma.num_edges() for gamma in truncated) == 2


@pytest.mark.parametrize("g,n", [(0, 5), (2, 1)])
def test_dimension_computed_two_independent_ways_large(g, n):
    for gamma in StableGraphs(g, n):
        by_vertices = gamma.stratum_dimension()
        by_codim = StableGraphs(g, n).dimension() - gamma.num_edges()
        assert by_vertices == by_codim
