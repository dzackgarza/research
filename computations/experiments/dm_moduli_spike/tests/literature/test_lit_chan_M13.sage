r"""Tier-1 literature oracle: Chan's explicit M̄_{1,3} example.

* Chan, *Tropical curves and metric graphs*: banana graph with
  `[M_{0,4}/(Z/2)]` and branch-exchange monodromy.
"""

from __future__ import annotations

from dm_moduli_spike import DMCompactificationModel, StableGraphTypes
from dm_moduli_spike.objects.edge_orbits import _elementary_contraction_data
from tests.support.fixtures import chan_m13_curve_type, induced_edge_permutation_group


def test_chan_M13_clutching_factors():
    types = StableGraphTypes(1, 3)
    gamma = chan_m13_curve_type(types)
    stratum = DMCompactificationModel(1, 3).stratum(gamma)
    factors = stratum.clutching_morphism().source_factors()
    assert len(factors) == 2
    assert sorted((factor.genus(), factor.number_of_markings()) for factor in factors) == [(0, 3), (0, 4)]
    presentation = stratum.open_stack_presentation()
    assert presentation.group_order() == 2
    assert presentation.dimension() == 1


def test_chan_M13_edge_automorphism_and_contraction_targets():
    types = StableGraphTypes(1, 3)
    gamma = chan_m13_curve_type(types)
    group = induced_edge_permutation_group(gamma.automorphism_action())
    assert group.order() == 2
    data = _elementary_contraction_data(gamma)
    assert len(data) == 1
    targets = {target.canonical_key() for target, _witness, _size in data}
    assert len(targets) == 1
    graph = gamma.canonical_representative()
    images = []
    for edge in graph.internal_edges():
        image, _ = graph.contract(edge)
        images.append(image.canonical_key())
    assert len(set(images)) == 1


def test_chan_M13_markings_fixed_and_quotient_presentation():
    types = StableGraphTypes(1, 3)
    gamma = chan_m13_curve_type(types)
    action = gamma.automorphism_action()
    for marking_perm in action.on_markings():
        assert marking_perm == (1, 2, 3)
    stratum = DMCompactificationModel(1, 3).stratum(gamma)
    presentation = stratum.open_stack_presentation()
    assert presentation.group_order() == 2
    assert sorted((factor.genus(), factor.number_of_markings()) for factor in presentation.product()) == [(0, 3), (0, 4)]
    assert presentation.dimension() == 1
