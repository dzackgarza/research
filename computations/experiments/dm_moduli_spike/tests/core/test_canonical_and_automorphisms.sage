r"""Tier-4 internal consistency: canonical labelling and automorphism numbers."""

from __future__ import annotations

from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.backends.admcycles_stable import AdmcyclesStableGraphBackend


def test_loop_has_a_branch_swap_automorphism():
    types = StableGraphs(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    assert loop.automorphism_number() == 2


def test_automorphism_numbers_agree_with_admcycles():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        types = StableGraphs(g, n)
        backend = AdmcyclesStableGraphBackend()
        for gamma in types:
                assert gamma.automorphism_number() == backend.admcycles_automorphism_number(types, gamma)


def test_high_genus_vertex_labels_do_not_break_canonical_keys():
    types = StableGraphs(12, 0)
    left = types.from_vertices(genera=(10, 2), markings=((), ()), edges=((0, 1),))
    right = types.from_vertices(genera=(2, 10), markings=((), ()), edges=((0, 1),))
    assert left.canonical_key() == right.canonical_key()
    assert left == right
