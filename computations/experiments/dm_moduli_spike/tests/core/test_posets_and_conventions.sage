r"""The specialization/closure posets and their explicit order conventions."""

from __future__ import annotations

from dm_moduli_spike import DMCompactificationModel


def test_specialization_poset_is_graded_by_num_edges_with_smooth_minimum():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification()
    poset = stratification.specialization_poset()
    assert poset.convention() == "specialization"
    assert poset.is_graded()
    minimal = poset.minimal_elements()
    assert len(minimal) == 1
    assert minimal[0].curve_type().is_smooth()
    rank = poset.rank_function()
    for stratum in poset.sage_poset():
        assert rank(stratum) == stratum.codimension()


def test_closure_poset_is_the_dual_with_smooth_maximum():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification()
    specialization = stratification.specialization_poset()
    closure = stratification.closure_poset()
    assert closure.convention() == "closure"
    assert closure.sage_poset() == specialization.sage_poset().dual()
    maximal = closure.maximal_elements()
    assert len(maximal) == 1
    assert maximal[0].curve_type().is_smooth()


def test_m04_specialization_poset_is_the_smooth_minimum_and_three_boundary_points():
    model = DMCompactificationModel(0, 4)
    stratification = model.stratification()
    poset = stratification.specialization_poset()
    sage_poset = poset.sage_poset()
    assert sage_poset.cardinality() == 4
    assert len(poset.minimal_elements()) == 1
    assert poset.minimal_elements()[0].curve_type().is_smooth()
    # three maximal boundary points 12|34, 13|24, 14|23
    maximal = poset.maximal_elements()
    assert len(maximal) == 3
    for stratum in maximal:
        assert stratum.codimension() == 1
    assert len(stratification.covers()) == 3


def test_no_bare_poset_method_exists_without_a_convention():
    stratification = DMCompactificationModel(1, 1).stratification()
    assert not hasattr(stratification, "poset")
    assert hasattr(stratification, "specialization_poset")
    assert hasattr(stratification, "closure_poset")
