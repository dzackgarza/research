r"""CI-tier mathematical invariant checks requiring full Mbar(2, 1) enumeration."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import _enumerate_stable_graph_levels
from dm_moduli_spike.objects.stable_graphs import StableGraphs

from dm_moduli_spike.objects.stratification import _build_stratification_from_types

pytestmark = pytest.mark.ci


def test_external_backend_completeness_requires_full_rank_span():
    curve_types = StableGraphs(2, 1)
    partial = _build_stratification_from_types(curve_types, (curve_types.smooth(),))
    assert not partial.is_complete()
    assert not partial.has_full_rank_support()
    assert partial.rank_sizes() == (1,)

    full = _enumerate_stable_graph_levels(2, 1, backend="admcycles-stable")
    truncated_types = tuple(gamma for level in full.curve_type_levels()[:2] for gamma in level)
    truncated = _build_stratification_from_types(curve_types, truncated_types)
    assert not truncated.is_complete()
    assert not truncated.has_full_rank_support()
    assert truncated.maximum_codim() == 1


def test_rank_support_without_exhaustiveness():
    full = _enumerate_stable_graph_levels(2, 1)
    all_types = [gamma for level in full.curve_type_levels() for gamma in level]
    removed = next(gamma for level in full.curve_type_levels() if len(level) > 1 for gamma in level)
    pruned = tuple(gamma for gamma in all_types if gamma is not removed)
    rebuilt = _build_stratification_from_types(StableGraphs(2, 1), pruned)
    assert rebuilt.has_full_rank_support()
    assert not rebuilt.is_complete()


def test_complete_stratifications_span_all_ranks_M21():
    stratification = _enumerate_stable_graph_levels(2, 1)
    assert stratification.is_complete()
    assert len(stratification.rank_sizes()) == StableGraphs(g, n).dimension() + 1


def test_truncated_enumeration_is_complete_through_cap():
    truncated = _enumerate_stable_graph_levels(2, 1, max_codim=2)
    assert not truncated.is_exhaustive()
    assert truncated.is_codimension_truncation()
    assert truncated.complete_through_codim() == 2
    assert truncated.maximum_codim() == 2


@pytest.mark.parametrize("g,n", [(0, 5), (2, 1)])
def test_dimension_computed_two_independent_ways_large(g, n):
    for level in _enumerate_stable_graph_levels(g, n).curve_type_levels():
        for gamma in level:
            by_vertices = gamma.stratum_dimension()
            by_codim = StableGraphs(g, n).dimension() - gamma.num_edges()
            assert by_vertices == by_codim
