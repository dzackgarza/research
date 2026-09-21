import pytest

from dzack_research.preamble.all import (
    FinitelyPresentedTorsionModules,
    QQ,
    QuadraticField,
    ZZ,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    _represented_value_module,
)

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
    module = ZZ.free_module(finite_ordered_set(("e",)))
    formed = module.equip_bilinear_form(ZZ, [[2]])
    generator = formed.module_generator("e")

    module_map = formed.module_category().Mor(formed, formed)(
        {"e": 3 * generator}
    )
    values = ZZ.regular_module()
    value_map = values.module_category().Mor(values, values)(
        {0: 9 * values.module_generator(0)}
    )
    morphism = formed.Mor(formed)((module_map, value_map))

    assert morphism.map_value(formed.b(generator, generator)) == formed.b(
        morphism(generator), morphism(generator)
    )

    # The old strict surface remains genuinely stricter: multiplication by
    # three is not an isometry of the form [2].
    with pytest.raises(ValueError):
        formed.Mor(formed)({"e": 3 * generator})


def test_divided_square_classifies_quadratic_maps_integrally_on_zmod4() -> None:
    module = _cyclic(4)
    generator = module.module_generator(0)
    square = module.divided_square()
    assert module.divided_square() is square
    universal_value = square.quadratic(generator)

    assert square.invariant_factors().cardinality() == 1
    assert square.invariant_factors()[0] == ZZ(8)
    assert universal_value.additive_order() == 8
    assert square.quadratic(2 * generator) == 4 * universal_value

    factor = square.from_quadratic(
        lambda element: 3 * square.quadratic(element),
        square,
    )
    assert factor(universal_value) == 3 * universal_value


def test_fibered_formed_morphisms_compose_after_base_change_in_one_target_fiber() -> None:
    module = ZZ.free_module(finite_ordered_set(("e",)))
    source = module.equip_bilinear_form(ZZ, [[2]])
    source_generator = source.module_generator("e")

    zz_to_qq = ZZ.Mor(QQ)(lambda element: QQ(element))
    middle = source.base_change(zz_to_qq)
    first_mor = source.fibered_formed_mor(middle, zz_to_qq)
    source_over_qq = first_mor.base_changed_domain()
    middle_generator = middle.module_generator("e")
    first_module_map = source_over_qq.module_category().Mor(source_over_qq, middle)(
        {"e": middle.scalar_multiple(3, middle_generator)}
    )
    source_values = _represented_value_module(source_over_qq)
    middle_values = _represented_value_module(middle)
    first_value_map = source_values.module_category().Mor(source_values, middle_values)(
        {0: middle_values.scalar_multiple(9, middle_values.module_generator(0))}
    )
    first = first_mor((first_module_map, first_value_map))

    field = QuadraticField(2, "a")
    qq_to_field = QQ.Mor(field)(lambda element: field(element))
    target = middle.base_change(qq_to_field)
    second_mor = middle.fibered_formed_mor(
        target,
        qq_to_field,
    )
    middle_over_field = second_mor.base_changed_domain()
    target_generator = target.module_generator("e")
    second_module_map = middle_over_field.module_category().Mor(middle_over_field, target)(
        {"e": target.scalar_multiple(2, target_generator)}
    )
    middle_changed_values = _represented_value_module(middle_over_field)
    target_values = _represented_value_module(target)
    second_value_map = middle_changed_values.module_category().Mor(middle_changed_values, target_values)(
        {0: target_values.scalar_multiple(4, target_values.module_generator(0))}
    )
    second = second_mor((second_module_map, second_value_map))

    composite = second * first
    assert composite.ring_map().domain() is ZZ
    assert composite.ring_map().codomain() is field
    assert composite(source_generator) == target.scalar_multiple(6, target_generator)
    assert composite.map_value(2) == field(72)

    # Identities are genuine fibered morphisms over identity ring maps, not
    # an unrelated fixed-fiber shortcut.
    identity_ring_map = QQ.Mor(QQ).identity()
    middle_identity = middle.fibered_formed_mor(
        middle,
        identity_ring_map,
    ).identity()
    assert (second * middle_identity)(middle_generator) == second(middle_generator)
    assert (middle_identity * first)(source_generator) == first(source_generator)
    assert (second * middle_identity).map_value(2) == second.map_value(2)
    assert (middle_identity * first).map_value(2) == first.map_value(2)


@pytest.mark.parametrize(
    "adjunction_method, expected_classifier_invariants",
    [
        ("bilinear_free_form_adjunction", 4),
        ("quadratic_free_form_adjunction", 8),
    ],
)
def test_free_form_classifier_adjunctions_have_mor_bijections_naturality_and_triangles(
    adjunction_method,
    expected_classifier_invariants,
) -> None:
    source = _cyclic(4)
    quotient = _cyclic(2)
    source_generator = source.module_generator(0)
    quotient_generator = quotient.module_generator(0)
    projection = source.module_category().Mor(source, quotient)({0: quotient_generator})

    adjunction = getattr(source.module_category(), adjunction_method)()
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()
    free_source = free(source)
    free_quotient = free(quotient)

    classifier_invariants = free_source.value_module().invariant_factors()
    assert classifier_invariants.cardinality() == 1
    assert classifier_invariants[0] == ZZ(expected_classifier_invariants)

    doubling = source.module_category().Mor(source, source)({0: 2 * source_generator})
    module_map = adjunction.unit(source) * doubling
    transpose_inverse = adjunction.mor_set_isomorphism_inverse(
        module_map,
        free_source,
    )
    recovered = adjunction.mor_set_isomorphism_forward(transpose_inverse, source)
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
        free_source.Mor(free_source).identity(),
    )

    right_object = underlying(free_source)
    right_triangle = (
        underlying(adjunction.counit(free_source))
        * adjunction.unit(right_object)
    )
    _assert_module_maps_agree(
        right_triangle,
        right_object.module_category().Mor(right_object, right_object).identity(),
    )

    # The nontrivial quotient is also genuinely acted on by the functors.
    assert free_quotient is free(projection.codomain())
