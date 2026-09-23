import pytest

from dzack_research.preamble.all import (
    FinitelyPresentedTorsionModules,
    ZZ,
)



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
