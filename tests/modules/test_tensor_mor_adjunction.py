import pytest

from dzack_research.preamble.all import (
    BilinearMap,
    FinitelyPresentedTorsionModules,
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_module_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for label in left.domain().module_generating_set():
        generator = left.domain().module_generator(label)
        assert left(generator) == right(generator)


def _cyclic(order):
    return FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((order,))


def test_tensor_product_of_presented_modules_has_the_bilinear_universal_property() -> None:
    left = _cyclic(2)
    right = _cyclic(4)
    left_generator = left.module_generator(0)
    right_generator = right.module_generator(0)

    tensor = left.tensor_product(right)
    pure = tensor.pure_tensor(left_generator, right_generator)
    universal = tensor.universal_bilinear_map()

    assert tuple(tensor.invariant_factors()) == (ZZ(2),)
    assert pure != tensor.zero()
    assert 2 * pure == tensor.zero()
    assert pure.additive_order() == 2
    assert universal.domain() is tensor
    assert universal.left_module() is left
    assert universal.right_module() is right
    assert universal.codomain() is tensor
    assert universal(left_generator, right_generator) == pure

    beta = BilinearMap(
        left,
        right,
        left,
        {(0, 0): left_generator},
    )
    factorization = beta
    assert factorization.domain() is tensor

    assert factorization(pure) == beta(left_generator, right_generator)

    # Universality is uniqueness, not merely existence.  Any linear map with
    # the required value on the universal pure tensor agrees on the selected
    # generating set of the tensor product and hence on every element.
    tensor_label = tensor.module_generating_set()[0]
    competing = tensor.module_category().Mor(tensor, left)(
        {tensor_label: beta(left_generator, right_generator)}
    )
    _assert_module_maps_agree(factorization, competing)

    # The left relation 2e=0 cannot be sent to a generator of order four.
    # Rejection happens at the bilinear datum, before a tensor classifier can
    # pretend that the assignment descends through the source relations.
    with pytest.raises(ValueError, match="domain relations"):
        BilinearMap(
            left,
            right,
            right,
            {(0, 0): right_generator},
        )






def test_tensor_internal_mor_adjunction_has_bijection_naturality_functoriality_and_triangles() -> None:
    fixed = _cyclic(4)
    adjunction = fixed.tensor_mor_adjunction()
    tensor_by = adjunction.left_adjoint()
    internal_mor_from = adjunction.right_adjoint()

    source = ZZ.free_module(finite_ordered_set(("a", "b")))
    target = _cyclic(4)
    tensor_source = tensor_by(source)
    target_generator = target.module_generator(0)
    fixed_generator = fixed.module_generator(0)

    beta = BilinearMap(
        source,
        fixed,
        target,
        {
            ("a", 0): target_generator,
            ("b", 0): 2 * target_generator,
        },
    )
    morphism = beta
    assert morphism.domain() is tensor_source
    transpose = adjunction.mor_set_isomorphism_forward(morphism, source)
    recovered = adjunction.mor_set_isomorphism_inverse(transpose, target)
    _assert_module_maps_agree(recovered, morphism)

    mor_object = internal_mor_from(target)
    for source_label in source.module_generating_set():
        curried = transpose(source.module_generator(source_label))
        assert curried.parent() is mor_object
        assert curried(fixed_generator) == beta(
            source.module_generator(source_label),
            fixed_generator,
        )

    # Naturality of the unit under a nontrivial map of free modules.
    unit_target = ZZ.free_module(finite_ordered_set(("c", "d", "e")))
    source_map = source.module_category().Mor(source, unit_target)(
        {
            "a": unit_target.module_generator("c") + unit_target.module_generator("d"),
            "b": 2 * unit_target.module_generator("e"),
        }
    )
    left, right = adjunction.unit_transformation().naturality_square(source_map)
    _assert_module_maps_agree(left, right)

    # Naturality of evaluation under the quotient Z/4 -> Z/2.
    smaller_target = _cyclic(2)
    target_map = target.module_category().Mor(target, smaller_target)(
        {0: smaller_target.module_generator(0)}
    )
    left, right = adjunction.counit_transformation().naturality_square(target_map)
    _assert_module_maps_agree(left, right)

    # Functoriality is checked on an actual nonidentity composite.
    third = ZZ.free_module(finite_ordered_set(("x",)))
    second_map = unit_target.module_category().Mor(unit_target, third)(
        {
            "c": third.module_generator("x"),
            "d": 2 * third.module_generator("x"),
            "e": -third.module_generator("x"),
        }
    )
    tensor_composite = tensor_by(second_map * source_map)
    tensor_stepwise = tensor_by(second_map) * tensor_by(source_map)
    _assert_module_maps_agree(tensor_composite, tensor_stepwise)

    mor_composite = internal_mor_from(target_map)
    mor_identity = internal_mor_from(target.module_category().Mor(target, target).identity())
    _assert_module_maps_agree(
        mor_composite * mor_identity,
        mor_composite,
    )

    # The two triangle identities are the definitive coherence conditions.
    left_triangle = (
        adjunction.counit(tensor_by(source))
        * tensor_by(adjunction.unit(source))
    )
    tensor_source = tensor_by(source)
    _assert_module_maps_agree(
        left_triangle,
        tensor_source.module_category().Mor(tensor_source, tensor_source).identity(),
    )

    right_object = internal_mor_from(target)
    right_triangle = (
        internal_mor_from(adjunction.counit(target))
        * adjunction.unit(right_object)
    )
    _assert_module_maps_agree(
        right_triangle,
        right_object.module_category().Mor(right_object, right_object).identity(),
    )
