r"""Mathematical invariants: canonical representatives, immutability, automorphisms."""

from __future__ import annotations

import pytest

from dm_moduli_spike import DMCompactificationModel, StableCurveTypes, StableGraph
from dm_moduli_spike.objects.canonical import canonical_record
from dm_moduli_spike.objects.stratification import build_stratification_from_types


def test_isomorphic_labeled_inputs_define_the_same_curve_type():
    types = StableCurveTypes(0, 4)
    left = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    right = types.from_vertices(genera=(0, 0), markings=((3, 4), (1, 2)), edges=((0, 1),))
    assert left == right
    assert left.canonical_representative() == right.canonical_representative()
    assert left is right


def test_record_is_immutable_after_construction():
    record = StableGraph(
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
    types = StableCurveTypes(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    once = canonical_record(gamma.canonical_representative())
    twice = canonical_record(once)
    assert once == twice


def test_automorphism_group_order_matches_number():
    types = StableCurveTypes(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    assert int(gamma.automorphism_group().order()) == gamma.automorphism_number()
    presentation = DMCompactificationModel(0, 4).stratum(gamma).open_stack_presentation()
    assert int(presentation.automorphism_group().order()) == presentation.group_order()


def test_stack_signature_carries_automorphism_group_not_just_order():
    model = DMCompactificationModel(1, 1)
    loop = model.curve_types().from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    clutching = model.stratum(loop).clutching_morphism()
    group = clutching.automorphism_group()
    assert int(group.order()) == 2


def test_external_backend_completeness_requires_full_rank_span():
    curve_types = DMCompactificationModel(2, 1).curve_types()
    partial = build_stratification_from_types(curve_types, (curve_types.smooth(),))
    assert not partial.is_complete()
    assert partial.rank_sizes() == (1,)

    full = DMCompactificationModel(2, 1).stratification(backend="admcycles-stable")
    truncated_types = tuple(gamma for level in full.curve_type_levels()[:2] for gamma in level)
    truncated = build_stratification_from_types(curve_types, truncated_types)
    assert not truncated.is_complete()
    assert truncated.maximum_codim() == 1


def test_admcycles_stable_backend_matches_pure_sage_when_complete():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0)]:
        model = DMCompactificationModel(g, n)
        pure = model.stratification(backend="pure-sage")
        adm = model.stratification(backend="admcycles-stable")
        assert adm.is_complete()
        pure_keys = {gamma.canonical_key() for level in pure.curve_type_levels() for gamma in level}
        adm_keys = {gamma.canonical_key() for level in adm.curve_type_levels() for gamma in level}
        assert pure_keys == adm_keys


def test_contraction_composition_across_isomorphic_representatives():
    types = StableCurveTypes(0, 5)
    gamma = types.from_vertices(
        genera=(0, 0, 0),
        markings=((1, 2), (3,), (4, 5)),
        edges=((0, 1), (1, 2)),
    )
    graph = gamma.canonical_representative()
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
    relabeled_graph = relabeled.canonical_representative()
    _, second = relabeled_graph.contract(relabeled_graph.internal_edges()[0])
    composite = first.compose(second)
    assert composite.domain() == graph
    assert composite.codomain().graph_type().is_smooth()


def test_contracts_to_matches_specialization_order():
    poset = DMCompactificationModel(2, 0).stratification().specialization_poset()
    for generic in poset:
        for special in poset:
            assert poset.is_lequal(generic, special) == special.curve_type().contracts_to(generic.curve_type())


def test_stratification_contraction_witnesses_use_level_representatives():
    stratification = DMCompactificationModel(1, 2).stratification()
    for witness in stratification.contraction_witnesses():
        generic_type = witness.target_type()
        assert witness.codomain() is generic_type.canonical_representative()
        special_candidates = {
            stratum.curve_type().canonical_representative()
            for stratum in stratification.strata(codim=generic_type.num_edges() + 1)
        }
        assert witness.domain() in special_candidates


def test_presentation_data_is_invariant_under_vertex_relabeling():
    types = StableCurveTypes(0, 4)
    left = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    right = types.from_vertices(genera=(0, 0), markings=((3, 4), (1, 2)), edges=((0, 1),))
    left_presentation = DMCompactificationModel(0, 4).stratum(left).open_stack_presentation()
    right_presentation = DMCompactificationModel(0, 4).stratum(right).open_stack_presentation()
    assert left_presentation == right_presentation
    assert left.to_json() == right.to_json()


def test_automorphism_action_fixes_markings_and_permutes_parallel_edges():
    types = StableCurveTypes(1, 2)
    theta = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    action = theta.automorphism_action()
    assert all(image == tuple(range(1, 3)) for image in action.on_markings())
    assert theta.elementary_contraction_orbits()[0].orbit_size() == 2


def test_backend_independence_without_verify():
    model = DMCompactificationModel(0, 4)
    adm = model.stratification(backend="admcycles-stable")
    assert adm.is_complete()
    verified = model.stratification(backend="admcycles-stable", verify_against="pure-sage")
    assert verified.rank_sizes() == adm.rank_sizes()


def test_completeness_false_when_enumeration_stops_early(monkeypatch):
    from dm_moduli_spike.objects import enumeration

    def stop_after_first(_gamma):
        return ()

    monkeypatch.setattr(enumeration, "one_edge_degenerations", stop_after_first)
    incomplete = DMCompactificationModel(0, 4).stratification(backend="pure-sage")
    assert not incomplete.is_complete()
    assert incomplete.rank_sizes() == (1,)
    certificate = incomplete.enumeration_result()
    assert not certificate.globally_complete
    assert certificate.complete_through_codim == 0
    assert certificate.backend == "pure-sage"


def test_admcycles_backend_skips_pure_sage_without_verify(monkeypatch):
    from dm_moduli_spike.objects import stratification as stratification_module

    def boom(*_args, **_kwargs):
        raise RuntimeError("pure-sage enumeration must not run for admcycles-stable")

    monkeypatch.setattr(stratification_module, "build_stratification", boom)
    result = DMCompactificationModel(0, 4).stratification(backend="admcycles-stable")
    assert result.is_complete()
    assert result.backend() == "admcycles-stable"


def test_contraction_flag_map_is_immutable_to_caller_mutation():
    types = StableCurveTypes(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    graph = gamma.canonical_representative()
    _, contraction = graph.contract(graph.internal_edges()[0])
    flag_map = contraction.domain_flag_of_codomain_flag()
    flag_map[0] = 999
    assert contraction.domain_flag_of_codomain_flag()[0] != 999


def test_dumbbell_graph_automorphism_swaps_loop_branches():
    types = StableCurveTypes(1, 2)
    dumbbell = types.from_vertices(
        genera=(0, 0),
        markings=((), (1, 2)),
        edges=((0, 0), (0, 1)),
    )
    action = dumbbell.automorphism_action()
    assert int(action.group().order()) == 2
    assert dumbbell.elementary_contraction_orbits()[0].orbit_size() == 1


def test_automorphism_actions_on_all_incidence_data():
    types = StableCurveTypes(1, 2)
    fixtures = {
        "theta": types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1))),
        "dumbbell": types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1))),
    }
    for gamma in fixtures.values():
        graph = gamma.canonical_representative()
        action = gamma.automorphism_action()
        assert int(action.group().order()) == gamma.automorphism_number()
        assert len(action.on_vertices()[0]) == graph.num_vertices()
        assert len(action.on_flags()[0]) == graph.num_flags()
        assert len(action.on_edges()[0]) == graph.num_edges()
        assert len(action.on_markings()[0]) == graph.num_markings()
        assert action.on_factors() == action.on_vertices()
        assert all(image == tuple(range(1, graph.num_markings() + 1)) for image in action.on_markings())


def test_branch_swap_semantics_on_flags_and_edges():
    types = StableCurveTypes(1, 2)
    theta = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    dumbbell = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    theta_action = theta.automorphism_action()
    dumbbell_action = dumbbell.automorphism_action()
    assert theta_action.on_edges()[0] == (1, 0)
    assert theta_action.on_flags()[0] != tuple(range(theta.num_flags()))
    assert dumbbell_action.on_flags()[0] != tuple(range(dumbbell.num_flags()))


def test_decorated_edge_orbit_morphisms_contract_to_codimension_one():
    from admcycles.decorated_graph import DecoratedGraph

    from dm_moduli_spike.backends.admcycles_decorated import contraction_from_decorated_morphism

    dg = DecoratedGraph([0, 0], [[1, 2], [3, 4]], [(0, 1, 1)])
    for u, v, _size in dg.edge_orbit_representatives():
        morphism = dg.edge_contraction_morphism([(u, v, 1)])
        contraction = contraction_from_decorated_morphism(morphism, 0, 4)
        assert contraction.target_type().num_edges() == dg.num_edges() - 1


def test_clutching_datum_exposes_gluing_partition():
    types = StableCurveTypes(1, 2)
    dumbbell = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    clutching = DMCompactificationModel(1, 2).stratum(dumbbell).clutching_morphism()
    assert clutching.gluing_partition() == (frozenset(), frozenset({1, 2}))
    assert clutching.local_markings_by_factor() == ((), (1, 2))
    assert clutching.edge_incidence() == ((0, 0), (0, 1))
    assert int(clutching.automorphism_action().group().order()) == 2


def test_clutching_gluing_map_assigns_markings_and_edge_branches():
    types = StableCurveTypes(1, 2)
    dumbbell = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    clutching = DMCompactificationModel(1, 2).stratum(dumbbell).clutching_morphism()
    marking_slots, edge_branches = clutching.gluing_map()
    assert marking_slots == ((1, 0), (1, 1))
    assert edge_branches == dumbbell.canonical_representative().internal_edges()


def test_all_invariants_equal_under_vertex_relabeling():
    types = StableCurveTypes(0, 4)
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
    assert (
        DMCompactificationModel(0, 4).stratum(left).open_stack_presentation()
        == DMCompactificationModel(0, 4).stratum(right).open_stack_presentation()
    )


def test_canonical_key_unchanged_after_failed_mutation():
    types = StableCurveTypes(0, 4)
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    record = gamma.canonical_representative()
    key_before = gamma.canonical_key()
    hash_before = hash(gamma)
    try:
        record._vertex_genera = (1, 1)  # noqa: SLF001
    except AttributeError:
        pass
    assert gamma.canonical_key() == key_before
    assert hash(gamma) == hash_before


def test_complete_stratifications_span_all_ranks():
    for g, n in [(0, 4), (1, 1), (1, 2), (2, 0), (2, 1)]:
        model = DMCompactificationModel(g, n)
        stratification = model.stratification()
        assert stratification.is_complete()
        assert len(stratification.rank_sizes()) == model.dimension() + 1


def test_theta_dumbbell_and_m12_type_e_orbit_sizes():
    from tests.support.fixtures import m12_types

    types = StableCurveTypes(1, 2)
    theta = types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1)))
    dumbbell = types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1)))
    m12_e = m12_types(DMCompactificationModel(1, 2).stratification())["E"].curve_type()
    assert theta.elementary_contraction_orbits()[0].orbit_size() == 2
    dumbbell_orbits = {orbit.orbit_size() for orbit in dumbbell.elementary_contraction_orbits()}
    assert dumbbell_orbits == {1, 1}
    m12_orbits = sorted(orbit.orbit_size() for orbit in m12_e.elementary_contraction_orbits())
    assert m12_orbits == [2]


def test_automorphism_generators_agree_with_incidence_actions():
    from dm_moduli_spike.objects.canonical import _incidence_graph
    from tests.support.fixtures import m12_types

    types = StableCurveTypes(1, 2)
    fixtures = {
        "theta": types.from_vertices(genera=(0, 0), markings=((1,), (2,)), edges=((0, 1), (0, 1))),
        "dumbbell": types.from_vertices(genera=(0, 0), markings=((), (1, 2)), edges=((0, 0), (0, 1))),
        "m12_type_e": m12_types(DMCompactificationModel(1, 2).stratification())["E"].curve_type(),
    }
    for gamma in fixtures.values():
        graph = gamma.canonical_representative()
        incidence, _partition, color_of = _incidence_graph(graph)
        vertex_nodes = sorted(node for node in color_of if node[0] == "V")
        vertex_index = {node: index for index, node in enumerate(vertex_nodes)}
        action = gamma.automorphism_action()
        group = action.group()
        for index, generator in enumerate(group.gens()):
            for vertex in range(gamma.num_vertices()):
                image_node = generator(("V", vertex))
                assert action.on_vertices()[index][vertex] == vertex_index[image_node]
            for label in range(1, gamma.num_markings() + 1):
                image_label = generator(("M", label))[1]
                assert action.on_markings()[index][label - 1] == image_label
            assert action.on_factors()[index] == action.on_vertices()[index]
            assert len(action.on_local_markings()[index]) == gamma.num_vertices()
