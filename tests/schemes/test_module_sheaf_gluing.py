from __future__ import annotations


def _rank_one_generator(module):
    return module.module_generator(next(iter(module.module_generating_set())))


def _rank_one_transition(source, target, unit):
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    source_generator = _rank_one_generator(source)
    target_generator = _rank_one_generator(target)
    forward = module_homset(source, target)(
        lambda _label: target.scalar_multiple(unit, target_generator)
    )
    inverse = module_homset(target, source)(
        lambda _label: source.scalar_multiple(unit.inverse_of_unit(), source_generator)
    )
    return Isomorphism(forward, inverse)


def test_two_chart_module_descent_builds_the_actual_compatible_section_module() -> None:
    from dzack_research.preamble.all import QQ, FreeModule, PolynomialRing, Spec

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    left, right = cover.opens()
    left_module = FreeModule(left.coordinate_algebra(), 1)
    right_module = FreeModule(right.coordinate_algebra(), 1)
    left_overlap = cover.restrict_module(left_module, 0, 1)
    right_overlap = cover.restrict_module(right_module, 1, 0)

    overlap_x = scheme.structure_sheaf().restriction_map(
        scheme,
        cover.overlap(0, 1),
    )(x)
    transition = _rank_one_transition(left_overlap, right_overlap, overlap_x)
    gluing = cover.glue_modules(
        (left_module, right_module),
        {(0, 1): transition},
    )

    sheaf = gluing.sheaf()
    sections = sheaf.global_sections()
    left_generator = _rank_one_generator(left_module)
    right_generator = _rank_one_generator(right_module)
    right_x = scheme.structure_sheaf().restriction_map(scheme, right)(x)
    compatible = sections(
        (
            left_generator,
            right_module.scalar_multiple(right_x, right_generator),
        )
    )

    assert compatible in sections
    assert compatible.component(0) == left_generator
    assert sheaf.sections_on_chart(0) is left_module
    assert sheaf.sections_on_intersection(0, 0, 1) is left_overlap
    assert sheaf.transition(0, 1).domain() is left_overlap
    assert sheaf.transition(0, 1).codomain() is right_overlap

    scaled = sections.scalar_multiple(x, compatible)
    left_x = scheme.structure_sheaf().restriction_map(scheme, left)(x)
    assert scaled.component(0) == left_module.scalar_multiple(left_x, left_generator)
    assert sections.scalar_action()(x)(compatible) == scaled

    try:
        sections((left_generator, right_generator))
    except ValueError as error:
        assert "do not agree" in str(error)
    else:
        raise AssertionError("the noncompatible local tuple must not define a global section")


def test_three_chart_module_descent_checks_the_transition_cocycle() -> None:
    from dzack_research.preamble.all import (
        QQ,
        FreeModule,
        Modules,
        PolynomialRing,
        Spec,
    )

    algebra = PolynomialRing(QQ, ("x", "y"))
    x, y = algebra.algebra_generators()
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, y, algebra.one() - x - y)
    local_modules = tuple(
        FreeModule(open_subscheme.coordinate_algebra(), 1)
        for open_subscheme in cover.opens()
    )

    identity_transitions = {}
    for left_index in range(3):
        for right_index in range(left_index + 1, 3):
            left_overlap = cover.restrict_module(
                local_modules[left_index],
                left_index,
                right_index,
            )
            right_overlap = cover.restrict_module(
                local_modules[right_index],
                right_index,
                left_index,
            )
            identity_transitions[left_index, right_index] = _rank_one_transition(
                left_overlap,
                right_overlap,
                left_overlap.base_ring().one(),
            )

    gluing = cover.glue_modules(local_modules, identity_transitions)
    triple_left = gluing.restricted_module(0, 0, 1, 2)
    triple_right = gluing.restricted_module(2, 0, 1, 2)
    triple_transition = gluing.transition_on_intersection(0, 2, 0, 1, 2)
    assert triple_transition.domain() is triple_left
    assert triple_transition.codomain() is triple_right
    assert triple_transition(_rank_one_generator(triple_left)) == _rank_one_generator(
        triple_right
    )

    pair_left = gluing.restricted_module(0, 0, 1)
    pair_to_triple = gluing.restriction_between_intersections(
        0,
        (0, 1),
        (0, 1, 2),
    )
    direct_to_triple = gluing.restriction_map(0, 0, 1, 2)
    chart_to_pair = gluing.restriction_map(0, 0, 1)
    local_generator = _rank_one_generator(local_modules[0])
    via_pair = pair_to_triple(
        chart_to_pair(local_generator).underlying_element()
    ).underlying_element()
    assert pair_to_triple.domain() is pair_left
    assert via_pair == direct_to_triple(local_generator).underlying_element()

    sections = gluing.sheaf().global_sections()
    assert sections in Modules(algebra)
    assert sections.zero() + sections.zero() == sections.zero()

    bad_transitions = dict(identity_transitions)
    overlap_02 = cover.overlap(0, 2)
    overlap_x = scheme.structure_sheaf().restriction_map(scheme, overlap_02)(x)
    bad_transitions[0, 2] = _rank_one_transition(
        cover.restrict_module(local_modules[0], 0, 2),
        cover.restrict_module(local_modules[2], 2, 0),
        overlap_x,
    )
    try:
        cover.glue_modules(local_modules, bad_transitions)
    except ValueError as error:
        assert "cocycle" in str(error)
    else:
        raise AssertionError("incompatible transition isomorphisms must fail the triple cocycle")


def test_presented_local_modules_descend_with_their_relations() -> None:
    from dzack_research.preamble.all import (
        QQ,
        BasedFreeModule,
        FinitelyPresentedModule,
        FinitelyPresentedModules,
        PolynomialRing,
        Spec,
        module_homset,
    )
    from dzack_research.preamble.categories.sets import finite_ordered_set

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    relation = x - algebra(2)

    local_modules = []
    for open_subscheme in cover.opens():
        ring = open_subscheme.coordinate_algebra()
        relation_value = scheme.structure_sheaf().restriction_map(
            scheme,
            open_subscheme,
        )(relation)
        relations = BasedFreeModule(ring, finite_ordered_set(("r",)))
        generators = BasedFreeModule(ring, finite_ordered_set(("e",)))
        local_modules.append(
            FinitelyPresentedModule(
                module_homset(relations, generators)(
                    {
                        "r": generators.scalar_multiple(
                            relation_value,
                            generators.module_generator("e"),
                        )
                    }
                )
            )
        )
    local_modules = tuple(local_modules)

    left_overlap = cover.restrict_module(local_modules[0], 0, 1)
    right_overlap = cover.restrict_module(local_modules[1], 1, 0)
    transition = _rank_one_transition(
        left_overlap,
        right_overlap,
        left_overlap.base_ring().one(),
    )
    gluing = cover.glue_modules(
        local_modules,
        {(0, 1): transition},
    )

    assert left_overlap in FinitelyPresentedModules(cover.overlap(0, 1).coordinate_algebra())
    assert right_overlap in FinitelyPresentedModules(cover.overlap(0, 1).coordinate_algebra())
    compatible = gluing.sheaf().global_sections()(
        tuple(_rank_one_generator(module) for module in local_modules)
    )
    assert compatible.component(0) == _rank_one_generator(local_modules[0])
    assert transition.forward()(_rank_one_generator(left_overlap)) == _rank_one_generator(
        right_overlap
    )
