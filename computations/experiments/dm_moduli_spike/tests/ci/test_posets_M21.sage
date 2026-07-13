r"""CI-tier specialization/closure poset checks on Mbar(2, 1)."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import DMCompactificationModel


pytestmark = pytest.mark.ci


def test_specialization_poset_is_graded_by_num_edges_with_smooth_minimum():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification()
    poset = stratification.specialization_poset()
    assert poset.is_graded()
    minimal = poset.minimal_elements()
    assert len(minimal) == 1
    assert minimal[0].curve_type().is_smooth()
    rank = poset.rank_function()
    for stratum in poset:
        assert rank(stratum) == stratum.codimension()


def test_closure_poset_is_the_dual_with_smooth_maximum():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification()
    specialization = stratification.specialization_poset()
    closure = stratification.closure_poset()
    assert closure == specialization.dual()
    maximal = closure.maximal_elements()
    assert len(maximal) == 1
    assert maximal[0].curve_type().is_smooth()
