r"""Canonical labelling (isomorphism invariance) and automorphism numbers."""

from __future__ import annotations

from sage.combinat.permutation import Permutations

from dm_moduli_spike import DMCompactificationModel, StableCurveTypes, StableGraphRecord
from dm_moduli_spike.backends.admcycles_stable import AdmcyclesStableGraphBackend


def _relabel(record, vertex_perm, flag_perm):
    r"""An isomorphic record under given vertex and flag permutations (0-indexed
    maps ``old -> new``)."""
    num_vertices = record.num_vertices()
    num_flags = record.num_flags()
    new_genera = [0] * num_vertices
    for vertex in range(num_vertices):
        new_genera[vertex_perm[vertex]] = record.vertex_genera[vertex]
    new_flag_vertex = [0] * num_flags
    new_flag_involution = [0] * num_flags
    for flag in range(num_flags):
        new_flag_vertex[flag_perm[flag]] = vertex_perm[record.flag_vertex[flag]]
        new_flag_involution[flag_perm[flag]] = flag_perm[record.flag_involution[flag]]
    new_marking_to_flag = tuple(flag_perm[flag] for flag in record.marking_to_flag)
    return StableGraphRecord(
        vertex_genera=tuple(new_genera),
        flag_vertex=tuple(new_flag_vertex),
        flag_involution=tuple(new_flag_involution),
        marking_to_flag=new_marking_to_flag,
    )


def test_random_relabelings_produce_the_same_canonical_key():
    types = StableCurveTypes(2, 1)
    model = DMCompactificationModel(2, 1)
    for level in model.stratification().curve_type_levels():
        for gamma in level:
            record = gamma.record()
            num_vertices = record.num_vertices()
            num_flags = record.num_flags()
            for vperm in Permutations(num_vertices)[:3]:
                for fperm in Permutations(num_flags)[:3]:
                    vmap = {i: int(vperm[i]) - 1 for i in range(num_vertices)}
                    fmap = {i: int(fperm[i]) - 1 for i in range(num_flags)}
                    relabelled = types.from_record(_relabel(record, vmap, fmap))
                    assert relabelled.canonical_key() == gamma.canonical_key()
                    assert relabelled == gamma


def test_loop_has_a_branch_swap_automorphism():
    types = StableCurveTypes(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    assert loop.automorphism_number() == 2


def test_automorphism_numbers_agree_with_admcycles():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0), (2, 1)]:
        model = DMCompactificationModel(g, n)
        types = model.curve_types()
        backend = AdmcyclesStableGraphBackend()
        for level in model.stratification().curve_type_levels():
            for gamma in level:
                assert gamma.automorphism_number() == backend.admcycles_automorphism_number(types, gamma)
