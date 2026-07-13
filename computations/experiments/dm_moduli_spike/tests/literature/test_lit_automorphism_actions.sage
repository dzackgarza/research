r"""Tier-1 literature oracle: published automorphism actions on edges.

* Markwig, tropical M_{1,2} folded cones (banana vs loop+bridge).
* Markwig, genus-two theta (S_3) and dumbbell (fold) examples.
"""

from __future__ import annotations

import pytest

from dm_moduli_spike import DMCompactificationModel
from tests.support.fixtures import induced_edge_permutation_group, m12_types, m20_types

pytestmark = pytest.mark.ci


def test_M12_banana_has_C2_edge_transposition():
    stratification = DMCompactificationModel(1, 2).stratification()
    banana = m12_types(stratification)["E"].curve_type()
    group = induced_edge_permutation_group(banana.automorphism_action())
    assert group.order() == 2
    assert group.is_transitive()
    assert len(group.orbit((1,), action="OnSets")) == 2


def test_M12_loop_bridge_has_trivial_induced_edge_action():
    stratification = DMCompactificationModel(1, 2).stratification()
    loop_bridge = m12_types(stratification)["B"].curve_type()
    group = induced_edge_permutation_group(loop_bridge.automorphism_action())
    assert group.order() == 1
    action = loop_bridge.automorphism_action()
    record = loop_bridge.canonical_representative()
    loop_flags = [
        flag
        for flag in range(record.num_flags())
        if record.flag_vertex[flag] == 0 and record.flag_involution[flag] != flag
    ]
    flag_perm = action.on_flags()[0]
    assert {flag_perm[loop_flags[0]], flag_perm[loop_flags[1]]} == set(loop_flags)
    assert flag_perm[loop_flags[0]] != loop_flags[0]


def test_genus_two_theta_has_S3_edge_action():
    stratification = DMCompactificationModel(2, 0).stratification()
    theta = m20_types(stratification)["I"].curve_type()
    group = induced_edge_permutation_group(theta.automorphism_action())
    assert group.order() == 6


def test_genus_two_dumbbell_has_order_two_edge_action_exchanging_loops():
    stratification = DMCompactificationModel(2, 0).stratification()
    dumbbell = m20_types(stratification)["II"].curve_type()
    group = induced_edge_permutation_group(dumbbell.automorphism_action())
    assert group.order() == 2
    record = dumbbell.canonical_representative()
    loop_edges = [
        index
        for index, (flag, partner) in enumerate(record.internal_edges())
        if record.flag_vertex[flag] == record.flag_vertex[partner]
    ]
    bridge_edges = [
        index
        for index, (flag, partner) in enumerate(record.internal_edges())
        if record.flag_vertex[flag] != record.flag_vertex[partner]
    ]
    assert len(loop_edges) == 2 and len(bridge_edges) == 1
    bridge_point = bridge_edges[0] + 1
    for generator in group.gens():
        assert generator(bridge_point) == bridge_point
