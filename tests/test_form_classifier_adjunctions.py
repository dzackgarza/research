import pytest

from dzack_research.preamble.all import (
    BasedFreeModule,
    BilinearForm,
    DividedSquare,
    FinitelyPresentedTorsionModules,
    QQ,
    QuadraticField,
    ZZ,
    bilinear_free_form_adjunction,
    fibered_formed_module_homset,
    formed_module_homset,
    module_homset,
    quadratic_free_form_adjunction,
    ring_as_module,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    _represented_value_module,
)
from dzack_research.preamble.categories.rings import engine_ring
from dzack_research.preamble.categories.sets import finite_ordered_set


def _cyclic(order):
    return FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((order,))


def _assert_module_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for label in left.domain().module_generating_set():
        generator = left.domain().module_generator(label)
        assert left(generator) == right(generator)


def _assert_formed_maps_agree(left, right) -> None:
    _assert_module_maps_agree(left.module_morphism(), right.module_morphism())
    _assert_module_maps_agree(left.value_morphism(), right.value_morphism())


def test_general_formed_morphism_keeps_value_map_separate_from_strict_form_preservation() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    formed = BilinearForm(module, ZZ, [[2]])
    generator = formed.module_generator("e")

    module_map = module_homset(formed, formed)(
        {"e": 3 * generator}
    )
    values = ring_as_module(ZZ)
    value_map = module_homset(values, values)(
        {0: 9 * values.module_generator(0)}
    )
    morphism = formed_module_homset(formed, formed)((module_map, value_map))

    assert morphism.map_value(formed.b(generator, generator)) == formed.b(
        morphism(generator), morphism(generator)
    )

    # The old strict surface remains genuinely stricter: multiplication by
    # three is not an isometry of the form [2].
    with pytest.raises(ValueError):
        formed.hom({"e": 3 * generator}, codomain=formed)


def test_divided_square_classifies_quadratic_maps_integrally_on_zmod4() -> None:
    module = _cyclic(4)
    generator = module.module_generator(0)
    square = DividedSquare(module)
    universal_value = square.quadratic(generator)

    assert square.invariants() == (8,)
    assert universal_value.additive_order() == 8
    assert square.quadratic(2 * generator) == 4 * universal_value

    factor = square.from_quadratic(
        lambda element: 3 * square.quadratic(element),
        square,
    )
    assert factor(universal_value) == 3 * universal_value


def test_fibered_formed_morphisms_compose_after_base_change_in_one_target_fiber() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    source = BilinearForm(module, ZZ, [[2]])
    source_generator = source.module_generator("e")

    zz_to_qq = engine_ring(QQ).coerce_map_from(engine_ring(ZZ))
    middle = source.base_change(zz_to_qq)
    first_homset = fibered_formed_module_homset(source, middle, zz_to_qq)
    source_over_qq = first_homset.base_changed_domain()
    middle_generator = middle.module_generator("e")
    first_module_map = module_homset(source_over_qq, middle)(
        {"e": middle.scalar_multiple(3, middle_generator)}
    )
    source_values = _represented_value_module(source_over_qq)
    middle_values = _represented_value_module(middle)
    first_value_map = module_homset(source_values, middle_values)(
        {0: middle_values.scalar_multiple(9, middle_values.module_generator(0))}
    )
    first = first_homset((first_module_map, first_value_map))

    field = QuadraticField(2, "a")
    qq_to_field = engine_ring(field).coerce_map_from(engine_ring(QQ))
    target = middle.base_change(qq_to_field)
    second_homset = fibered_formed_module_homset(
        middle,
        target,
        qq_to_field,
    )
    middle_over_field = second_homset.base_changed_domain()
    target_generator = target.module_generator("e")
    second_module_map = module_homset(middle_over_field, target)(
        {"e": target.scalar_multiple(2, target_generator)}
    )
    middle_changed_values = _represented_value_module(middle_over_field)
    target_values = _represented_value_module(target)
    second_value_map = module_homset(middle_changed_values, target_values)(
        {0: target_values.scalar_multiple(4, target_values.module_generator(0))}
    )
    second = second_homset((second_module_map, second_value_map))

    composite = second * first
    assert engine_ring(composite.ring_map().domain()) is engine_ring(ZZ)
    assert engine_ring(composite.ring_map().codomain()) is engine_ring(field)
    assert composite(source_generator) == target.scalar_multiple(6, target_generator)
    assert composite.map_value(2) == engine_ring(field)(72)

    # Identities are genuine fibered morphisms over identity ring maps, not
    # an unrelated fixed-fiber shortcut.
    identity_ring_map = engine_ring(QQ).coerce_map_from(engine_ring(QQ))
    middle_identity = fibered_formed_module_homset(
        middle,
        middle,
        identity_ring_map,
    ).identity()
    assert (second * middle_identity)(middle_generator) == second(middle_generator)
    assert (middle_identity * first)(source_generator) == first(source_generator)
    assert (second * middle_identity).map_value(2) == second.map_value(2)
    assert (middle_identity * first).map_value(2) == first.map_value(2)


@pytest.mark.parametrize(
    "adjunction_factory, expected_classifier_invariants",
    [
        (bilinear_free_form_adjunction, (4,)),
        (quadratic_free_form_adjunction, (8,)),
    ],
)
def test_free_form_classifier_adjunctions_have_hom_bijections_naturality_and_triangles(
    adjunction_factory,
    expected_classifier_invariants,
) -> None:
    source = _cyclic(4)
    quotient = _cyclic(2)
    source_generator = source.module_generator(0)
    quotient_generator = quotient.module_generator(0)
    projection = module_homset(source, quotient)({0: quotient_generator})

    adjunction = adjunction_factory(ZZ)
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()
    free_source = free(source)
    free_quotient = free(quotient)

    assert free_source.value_module().invariants() == expected_classifier_invariants

    doubling = module_homset(source, source)({0: 2 * source_generator})
    module_map = free_source.equip_form_morphism() * doubling
    transpose_inverse = adjunction.hom_set_isomorphism_inverse(
        module_map,
        free_source,
    )
    recovered = adjunction.hom_set_isomorphism_forward(transpose_inverse)
    _assert_module_maps_agree(recovered, module_map)

    # The universal value map is forced, not selected independently.
    induced = free(doubling)
    _assert_formed_maps_agree(transpose_inverse, induced)

    left, right = adjunction.unit_transformation().naturality_square(projection)
    _assert_module_maps_agree(left, right)

    formed_projection = free(projection)
    left, right = adjunction.counit_transformation().naturality_square(
        formed_projection
    )
    _assert_formed_maps_agree(left, right)

    left_triangle = adjunction.counit(free_source) * free(adjunction.unit(source))
    _assert_formed_maps_agree(
        left_triangle,
        formed_module_homset(free_source, free_source).identity(),
    )

    right_object = underlying(free_source)
    right_triangle = (
        underlying(adjunction.counit(free_source))
        * adjunction.unit(right_object)
    )
    _assert_module_maps_agree(
        right_triangle,
        module_homset(right_object, right_object).identity(),
    )

    # The nontrivial quotient is also genuinely acted on by the functors.
    assert free_quotient is free(projection.codomain())
