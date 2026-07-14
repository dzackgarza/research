r"""Tier-1 literature oracle: published automorphism actions on edges and flags.

* Markwig, *Tropical compactification of the moduli space of stable curves*
  (2009), Example 2.2 / Figure 2 (`\overline{\mathcal M}_{1,2}` banana vs loop+bridge);
  Example 2.7 / Figure 5 (genus-two theta and dumbbell).
"""

from __future__ import annotations

import pytest

from dm_moduli_spike.testing_support.support.fixtures import (
    flag_generator_images,
    induced_edge_permutation_group,
    m12_types,
    m20_types,
)

pytestmark = pytest.mark.ci


def test_M12_banana_vs_loop_bridge_aut_edge_and_flag_actions():
    r"""Markwig Ex. 2.2 / Fig. 2: banana nontrivial on `E(\Gamma)`; loop+bridge only on flags.

    The banana has `|\operatorname{Aut}(\Gamma)|=2` with a transposition of the two
    parallel edges.  The loop+bridge type has the same full automorphism order but
    the induced action on edge indices is trivial; only the loop half-edges are swapped.
    """
    banana = m12_types()["E"]._canonical_record()
    loop_bridge = m12_types()["B"]._canonical_record()

    assert banana.automorphism_group(on="vertices").order() == 2 or banana.automorphism_group(on="edges").order() == 2
    banana_edge_group = induced_edge_permutation_group(banana)
    assert banana_edge_group.order() == 2
    assert banana_edge_group.is_transitive()

    assert loop_bridge.automorphism_group(on="half_edges").order() == 2
    loop_edge_group = induced_edge_permutation_group(loop_bridge)
    assert loop_edge_group.order() == 1

    loop_flags = [
        flag
        for flag in range(loop_bridge.num_flags())
        if loop_bridge.flag_vertex[flag] == 0 and loop_bridge.flag_involution[flag] != flag
    ]
    flag_perm = flag_generator_images(loop_bridge)[0]
    assert {flag_perm[loop_flags[0]], flag_perm[loop_flags[1]]} == set(loop_flags)
    assert flag_perm[loop_flags[0]] != loop_flags[0]


def test_M12_banana_has_C2_edge_transposition():
    r"""Markwig Ex. 2.2 / Fig. 2: type E banana has `C_2` edge transposition."""
    banana = m12_types()["E"]._canonical_record()
    group = induced_edge_permutation_group(banana)
    assert group.order() == 2
    assert group.is_transitive()
    assert len(group.orbit((1,), action="OnSets")) == 2


def test_M12_loop_bridge_has_trivial_induced_edge_action():
    r"""Markwig Ex. 2.2 / Fig. 2: type B loop+bridge has trivial induced `E(\Gamma)` action."""
    loop_bridge = m12_types()["B"]._canonical_record()
    group = induced_edge_permutation_group(loop_bridge)
    assert group.order() == 1
    loop_flags = [
        flag
        for flag in range(loop_bridge.num_flags())
        if loop_bridge.flag_vertex[flag] == 0 and loop_bridge.flag_involution[flag] != flag
    ]
    flag_perm = flag_generator_images(loop_bridge)[0]
    assert {flag_perm[loop_flags[0]], flag_perm[loop_flags[1]]} == set(loop_flags)
    assert flag_perm[loop_flags[0]] != loop_flags[0]


def test_genus_two_theta_has_S3_edge_action():
    r"""Markwig Ex. 2.7 / Fig. 5: type I theta graph has `S_3` edge action."""
    theta = m20_types()["I"]._canonical_record()
    group = induced_edge_permutation_group(theta)
    assert group.order() == 6


def test_genus_two_dumbbell_has_order_two_edge_action_exchanging_loops():
    r"""Markwig Ex. 2.7 / Fig. 5: type II dumbbell exchanges the two loop edges."""
    dumbbell = m20_types()["II"]._canonical_record()
    group = induced_edge_permutation_group(dumbbell)
    assert group.order() == 2
    loop_edges = [
        index
        for index, (flag, partner) in enumerate(dumbbell.internal_edges())
        if dumbbell.flag_vertex[flag] == dumbbell.flag_vertex[partner]
    ]
    bridge_edges = [
        index
        for index, (flag, partner) in enumerate(dumbbell.internal_edges())
        if dumbbell.flag_vertex[flag] != dumbbell.flag_vertex[partner]
    ]
    assert len(loop_edges) == 2 and len(bridge_edges) == 1
    bridge_point = bridge_edges[0] + 1
    for generator in group.gens():
        assert generator(bridge_point) == bridge_point


def test_native_gamma_edge_aut_matches_literature_orders_M12_banana():
    r"""Native ``PermutationGroup`` on edges has Markwig order 2 for the banana."""
    from dm_moduli_spike import StableGraphCategory

    banana = m12_types()["E"]._canonical_record()
    native = StableGraphCategory(1, 2).automorphism_group(banana, on="edges")
    assert native.order() == induced_edge_permutation_group(banana).order() == 2
