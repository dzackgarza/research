r"""CI-tier mathematical invariant checks requiring full Mbar(2, 1) enumeration."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import DMCompactificationModel

from dm_moduli_spike.objects.stratification import build_stratification_from_types

pytestmark = pytest.mark.ci


def test_external_backend_completeness_requires_full_rank_span():
    curve_types = DMCompactificationModel(2, 1).graph_types()
    partial = build_stratification_from_types(curve_types, (curve_types.smooth(),))
    assert not partial.is_complete()
    assert not partial.has_full_rank_support()
    assert partial.rank_sizes() == (1,)

    full = DMCompactificationModel(2, 1).stratification(backend="admcycles-stable")
    truncated_types = tuple(gamma for level in full.curve_type_levels()[:2] for gamma in level)
    truncated = build_stratification_from_types(curve_types, truncated_types)
    assert not truncated.is_complete()
    assert not truncated.has_full_rank_support()
    assert truncated.maximum_codim() == 1


def test_rank_support_without_exhaustiveness():
    model = DMCompactificationModel(2, 1)
    full = model.stratification()
    all_types = [gamma for level in full.curve_type_levels() for gamma in level]
    removed = next(gamma for level in full.curve_type_levels() if len(level) > 1 for gamma in level)
    pruned = tuple(gamma for gamma in all_types if gamma is not removed)
    rebuilt = build_stratification_from_types(model.graph_types(), pruned)
    assert rebuilt.has_full_rank_support()
    assert not rebuilt.is_complete()


def test_complete_stratifications_span_all_ranks_M21():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification()
    assert stratification.is_complete()
    assert len(stratification.rank_sizes()) == model.dimension() + 1


def test_truncated_enumeration_is_complete_through_cap():
    model = DMCompactificationModel(2, 1)
    truncated = model.stratification(max_codim=2)
    assert not truncated.is_exhaustive()
    assert truncated.is_codimension_truncation()
    assert truncated.complete_through_codim() == 2
    assert truncated.maximum_codim() == 2


@pytest.mark.parametrize("g,n", [(0, 5), (2, 1)])
def test_dimension_computed_two_independent_ways_large(g, n):
    model = DMCompactificationModel(g, n)
    for level in model.stratification().curve_type_levels():
        for gamma in level:
            by_vertices = gamma.stratum_dimension()
            by_codim = model.dimension() - gamma.num_edges()
            assert by_vertices == by_codim
