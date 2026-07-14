r"""Tier-4 internal consistency: specialization/closure posets and order conventions."""

from __future__ import annotations

from dm_moduli_spike.objects.model import _enumerate_stable_graph_levels



def test_m04_specialization_poset_is_the_smooth_minimum_and_three_boundary_points():
    stratification = _enumerate_stable_graph_levels(0, 4)
    poset = stratification.specialization_poset()
    assert poset.cardinality() == 4
    assert len(poset.minimal_elements()) == 1
    assert poset.minimal_elements()[0].is_smooth()
    # three maximal boundary points 12|34, 13|24, 14|23
    maximal = poset.maximal_elements()
    assert len(maximal) == 3
    for stratum in maximal:
        assert stratum.codimension() == 1
    assert len(stratification.covers()) == 3


def test_no_bare_poset_method_exists_without_a_convention():
    stratification = _enumerate_stable_graph_levels(1, 1)
    assert not hasattr(stratification, "poset")
    assert hasattr(stratification, "specialization_poset")
    assert hasattr(stratification, "closure_poset")
