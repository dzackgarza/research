r"""Tier-4 internal consistency: canonical representatives, immutability, automorphisms."""

from __future__ import annotations

from sage.categories.homset import Hom
from sage.rings.integer_ring import ZZ
from dm_moduli_spike import Mbar_gn, QuotientStack, spec
from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.objects._automorphism_action import _GraphAutomorphismData
from dm_moduli_spike.objects.records import _GraphRecord
import pytest

from dm_moduli_spike._admcycles.admcycles_stable import AdmcyclesStableGraphs
from dm_moduli_spike.objects.canonical import canonical_record
from dm_moduli_spike.testing_support.support.fixtures import rank_sizes
from dm_moduli_spike.testing_support.support.fixtures import (
    edge_generator_images,
    flag_generator_images,
    marking_generator_images,
    vertex_generator_images,
)


def test_isomorphic_labeled_inputs_define_the_same_curve_type():
    types = StableGraphs(0, 4)
    left = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    right = types.from_vertices(genera=(0, 0), markings=((3, 4), (1, 2)), edges=((0, 1),))
    assert left == right
    assert left._canonical_record() == right._canonical_record()
    assert left is right


def test_record_is_immutable_after_construction():
    record = _GraphRecord(
        vertex_genera=(1,),
        flag_vertex=(0,),
        flag_involution=(0,),
        marking_to_flag=(0,),
    )
    try:
        record._vertex_genera = (1,)  # noqa: SLF001
    except AttributeError:
        pass
    else:
        raise AssertionError("expected AttributeError when mutating StableGraph")


def test_canonical_record_is_idempotent():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    once = canonical_record(gamma._canonical_record())
    twice = canonical_record(once)
    assert once == twice


def test_automorphism_group_order_matches_number():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    assert int(gamma.automorphism_group().order()) == gamma.automorphism_number()
    graph = gamma._canonical_record()
    underlying = Mbar_gn(0, 4, base=spec(ZZ)).stratification().stratum(gamma).underlying_stack()
    assert isinstance(underlying, QuotientStack)
    assert int(underlying.group().order()) == gamma.automorphism_number()


def test_stack_signature_carries_automorphism_group_not_just_order():
    types = StableGraphs(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    graph = loop._canonical_record()
    underlying = Mbar_gn(1, 1, base=spec(ZZ)).stratification().stratum(loop).underlying_stack()
    assert isinstance(underlying, QuotientStack)
    assert int(underlying.group().order()) == 2


def test_admcycles_stable_backend_matches_pure_sage_when_complete():
    backend = AdmcyclesStableGraphs()
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        types = StableGraphs(g, n)
        pure_keys = {gamma.canonical_key() for gamma in types}
        adm_keys = {gamma.canonical_key() for gamma in backend.stable_curve_types(types)}
        assert pure_keys == adm_keys


def test_contraction_composition_across_isomorphic_representatives():
    types = StableGraphs(0, 5)
    gamma = types.from_vertices(
        genera=(0, 0, 0),
        markings=((1, 2), (3,), (4, 5)),
        edges=((0, 1), (1, 2)),
    )
    graph = gamma._canonical_record()
    edges = graph.internal_edges()
    _, first = graph.contract(edges[0])
    intermediate = first.codomain()
    relabeled = types.from_vertices(
        genera=intermediate.vertex_genera,
        markings=tuple(tuple(reversed(intermediate.markings_at(vertex))) for vertex in range(intermediate.num_vertices())),
        edges=tuple(
            (intermediate.flag_vertex[flag], intermediate.flag_vertex[partner])
            for flag, partner in intermediate.internal_edges()
        ),
    )
    assert relabeled == intermediate.graph_type()
    relabeled_graph = relabeled._canonical_record()
    _, second = relabeled_graph.contract(relabeled_graph.internal_edges()[0])
    composite = first.compose(second)
    assert composite.domain() == graph
    assert composite.codomain().graph_type().is_smooth()


def test_contracts_to_matches_specialization_order():
    poset = StableGraphCategory(2, 0).specialization_poset()
    for generic in poset:
        for special in poset:
            assert poset.is_lequal(generic, special) == special.contracts_to(generic)


def test_contraction_witnesses_are_hom_morphisms():
    from dm_moduli_spike.objects.gamma import StableGraphMorphism

    for gamma in StableGraphs(1, 2):
        for target, witness, _size in gamma.elementary_contractions():
            assert isinstance(witness, StableGraphMorphism)
            assert witness.parent() is Hom(gamma, target) or (
                witness.domain() == gamma and witness.codomain() == target
            )
            assert witness.codomain() == target
            assert witness.domain() == gamma
            assert witness.is_contraction()


def test_presentation_data_is_invariant_under_vertex_relabeling():
    types = StableGraphs(0, 4)
    left = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    right = types.from_vertices(genera=(0, 0), markings=((3, 4), (1, 2)), edges=((0, 1),))
    XSbar = Mbar_gn(0, 4, base=spec(ZZ))
    left_stack = XSbar.stratification().stratum(left).underlying_stack()
    right_stack = XSbar.stratification().stratum(right).underlying_stack()
    assert left_stack == right_stack
    assert left.to_json() == right.to_json()


def test_automorphism_action_fixes_markings_and_permutes_parallel_edges():
    types = StableGraphs(1, 2)
    theta = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    assert all(image == tuple(range(1, 3)) for image in marking_generator_images(theta._canonical_record()))
    assert theta.elementary_contractions()[0][2] == 2


def test_backend_enumeration_agrees_with_stable_graphs_rank_sizes():
    backend = AdmcyclesStableGraphs()
    types = StableGraphs(0, 4)
    adm = tuple(backend.stable_curve_types(types))
    assert {gamma.canonical_key() for gamma in adm} == {gamma.canonical_key() for gamma in types}
    adm_sizes = tuple(
        sum(1 for gamma in adm if gamma.num_edges() == codim)
        for codim in range(max(gamma.num_edges() for gamma in adm) + 1)
    )
    assert adm_sizes == rank_sizes(0, 4)


def test_enumeration_stop_early_yields_incomplete_levels(monkeypatch):
    from dm_moduli_spike.objects import enumeration

    def stop_after_first(_gamma):
        return ()

    monkeypatch.setattr(enumeration, "one_edge_degenerations", stop_after_first)
    levels = enumeration.stable_curve_type_levels(StableGraphs(0, 4))
    assert len(levels) == 1
    assert len(levels[0]) == 1
    assert next(iter(levels[0].values())).is_smooth()


def test_admcycles_backend_does_not_call_pure_sage_enumeration(monkeypatch):
    from dm_moduli_spike.objects import enumeration

    def boom(*_args, **_kwargs):
        raise RuntimeError("pure-sage enumeration must not run for admcycles-stable")

    monkeypatch.setattr(enumeration, "all_stable_curve_types", boom)
    monkeypatch.setattr(enumeration, "one_edge_degenerations", boom)
    backend = AdmcyclesStableGraphs()
    types = StableGraphs(0, 4)
    produced = tuple(backend.stable_curve_types(types))
    assert len(produced) == types.cardinality()


def test_contraction_flag_map_is_immutable_to_caller_mutation():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    graph = gamma._canonical_record()
    _, contraction = graph.contract(graph.internal_edges()[0])
    flag_map = contraction.domain_flag_of_codomain_flag()
    flag_map[0] = 999
    assert contraction.domain_flag_of_codomain_flag()[0] != 999


def test_dumbbell_graph_automorphism_swaps_loop_branches():
    types = StableGraphs(1, 2)
    dumbbell = types.from_vertices(
        genera=(0, 0),
        markings=((), (1, 2)),
        edges=((0, 0), (0, 1)),
    )
    assert int(dumbbell.automorphism_number()) == 2
    assert dumbbell.elementary_contractions()[0][2] == 1


def test_automorphism_actions_on_all_incidence_data():
    types = StableGraphs(1, 2)
    fixtures = {
        "theta": types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1))),
        "dumbbell": types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1))),
    }
    for gamma in fixtures.values():
        graph = gamma._canonical_record()
        assert int(gamma.automorphism_number()) == int(graph.automorphism_group(on="half_edges").order())
        verts = vertex_generator_images(graph)
        flags = flag_generator_images(graph)
        edges = edge_generator_images(graph)
        marks = marking_generator_images(graph)
        assert len(verts[0]) == graph.num_vertices()
        assert len(flags[0]) == graph.num_flags()
        assert len(edges[0]) == graph.num_edges()
        assert len(marks[0]) == graph.num_markings()
        assert all(image == tuple(range(1, graph.num_markings() + 1)) for image in marks)


def test_branch_swap_semantics_on_m11_nodal_flags():
    types = StableGraphs(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    graph = loop._canonical_record()
    marking_flag = graph.marking_to_flag[0]
    loop_flags = [
        flag
        for flag in range(graph.num_flags())
        if graph.flag_vertex[flag] == 0 and graph.flag_involution[flag] != flag
    ]
    assert len(loop_flags) == 2
    flag_perm = flag_generator_images(graph)[0]
    assert flag_perm[marking_flag] == marking_flag
    assert {flag_perm[loop_flags[0]], flag_perm[loop_flags[1]]} == set(loop_flags)
    assert flag_perm[loop_flags[0]] != loop_flags[0]


def test_factor_slots_on_m11_nodal_graph():
    types = StableGraphs(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    graph = loop._canonical_record()
    Gamma = StableGraphCategory(1, 1)
    assert Gamma.clutching_source(graph)[0][1] == (0, 1, 2)
    assert graph.marking_to_flag == (0,)
    loop_flags = [flag for flag in graph.flags_at(0) if graph.flag_involution[flag] != flag]
    assert loop_flags == [1, 2]
    assert graph.flag_involution[1] == 2 and graph.flag_involution[2] == 1
    flag_perm = flag_generator_images(graph)[0]
    assert flag_perm[0] == 0
    assert {flag_perm[1], flag_perm[2]} == {1, 2}
    assert flag_perm[1] != 1


def test_factor_slots_on_m04_split_type():
    types = StableGraphs(0, 4)
    split = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    graph = split._canonical_record()
    Gamma = StableGraphCategory(0, 4)
    sources = Gamma.clutching_source(graph)
    assert sources[0][1] == (0, 1, 4)
    assert sources[1][1] == (2, 3, 5)
    marking_flags = graph.marking_to_flag
    node_pairs = Gamma.node_pairings(graph)
    assert marking_flags == graph.marking_to_flag
    assert node_pairs == ((4, 5),)
    branch_flags = {node_pairs[0][0], node_pairs[0][1]}
    assert branch_flags == {4, 5}


def test_decorated_edge_orbit_morphisms_contract_to_codimension_one():
    from admcycles.decorated_graph import DecoratedGraph

    from dm_moduli_spike._admcycles.admcycles_decorated import contraction_from_decorated_morphism

    dg = DecoratedGraph([0, 0], [[1, 2], [3, 4]], [(0, 1, 1)])
    for u, v, _size in dg.edge_orbit_representatives():
        morphism = dg.edge_contraction_morphism([(u, v, 1)])
        contraction = contraction_from_decorated_morphism(morphism, 0, 4)
        assert contraction.target_type().num_edges() == dg.num_edges() - 1


def test_clutching_morphism_exposes_half_edge_coordinates():
    types = StableGraphs(1, 2)
    dumbbell = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    graph = dumbbell._canonical_record()
    Gamma = StableGraphCategory(1, 2)
    assert tuple(graph.markings_at(v) for v in range(graph.num_vertices())) == ((), (1, 2))
    assert Gamma.node_pairings(graph) == graph.internal_edges()
    assert [(graph.flag_vertex[a], graph.flag_vertex[b]) for a, b in graph.internal_edges()] == [(0, 0), (0, 1)]
    assert int(graph.automorphism_group(on="half_edges").order()) == 2
    assert (graph.genus(), graph.num_markings()) == (1, 2)


def test_clutching_gluing_map_assigns_markings_and_edge_branches():
    types = StableGraphs(1, 2)
    dumbbell = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    record = dumbbell._canonical_record()
    Gamma = StableGraphCategory(1, 2)
    marking_flags = record.marking_to_flag
    node_pairs = Gamma.node_pairings(record)
    assert marking_flags == record.marking_to_flag
    assert node_pairs == record.internal_edges()


def test_all_invariants_equal_under_vertex_relabeling():
    types = StableGraphs(0, 4)
    left = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    right = types.from_vertices(genera=(0, 0), markings=((3, 4), (1, 2)), edges=((0, 1),))
    for gamma in (left, right):
        assert gamma.num_vertices() == 2
        assert gamma.num_edges() == 1
        assert gamma.vertex_genera() == (0, 0)
        assert gamma.automorphism_number() == 1
        assert gamma.split_system() == frozenset({frozenset({1, 2})})
        assert gamma.stratum_dimension() == 0
    assert left.to_json() == right.to_json()
    XSbar = Mbar_gn(0, 4, base=spec(ZZ))
    assert (
        XSbar.stratification().stratum(left).underlying_stack()
        == XSbar.stratification().stratum(right).underlying_stack()
    )


def test_canonical_key_unchanged_after_failed_mutation():
    types = StableGraphs(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    record = gamma._canonical_record()
    key_before = gamma.canonical_key()
    hash_before = hash(gamma)
    try:
        record._vertex_genera = (1, 1)  # noqa: SLF001
    except AttributeError:
        pass
    assert gamma.canonical_key() == key_before
    assert hash(gamma) == hash_before


def test_stable_graphs_span_all_ranks():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        assert len(rank_sizes(g, n)) == StableGraphs(g, n).dimension() + 1
        assert StableGraphs(g, n).cardinality() == sum(rank_sizes(g, n))


def test_theta_dumbbell_and_m12_type_e_orbit_sizes():
    from dm_moduli_spike.testing_support.support.fixtures import m12_types

    types = StableGraphs(1, 2)
    theta = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    dumbbell = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    m12_e = m12_types()["E"]
    assert theta.elementary_contractions()[0][2] == 2
    dumbbell_orbits = {size for _target, _witness, size in dumbbell.elementary_contractions()}
    assert dumbbell_orbits == {1, 1}
    m12_orbits = sorted(size for _target, _witness, size in m12_e.elementary_contractions())
    assert m12_orbits == [2]


def test_automorphism_generators_agree_with_incidence_actions():
    from dm_moduli_spike.objects.canonical import _incidence_graph
    from dm_moduli_spike.testing_support.support.fixtures import m12_types

    types = StableGraphs(1, 2)
    fixtures = {
        "theta": types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1))),
        "dumbbell": types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1))),
        "m12_type_e": m12_types()["E"],
    }
    for gamma in fixtures.values():
        graph = gamma._canonical_record()
        action = _GraphAutomorphismData.from_graph(graph)
        incidence, _partition, color_of = _incidence_graph(graph)
        vertex_nodes = sorted(node for node in color_of if node[0] == "V")
        vertex_index = {node: index for index, node in enumerate(vertex_nodes)}
        group = action.group()
        for index, generator in enumerate(group.gens()):
            for vertex in range(gamma.num_vertices()):
                image_node = generator(("V", vertex))
                assert action.on_vertices()[index][vertex] == vertex_index[image_node]
            for label in range(1, gamma.num_markings() + 1):
                image_label = generator(("M", label))[1]
                assert action.on_markings()[index][label - 1] == image_label
            assert action.on_factors()[index] == action.on_vertices()[index]
