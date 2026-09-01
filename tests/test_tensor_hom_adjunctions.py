from dzack_research.preamble.all import (
    BasedFreeModule,
    BilinearMap,
    FinitelyPresentedTorsionModules,
    ZZ,
    module_homset,
    tensor_hom_adjunction,
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
    left = _cyclic(4)
    right = _cyclic(2)
    left_generator = left.module_generator(0)
    right_generator = right.module_generator(0)

    tensor = left.tensor_product(right)
    pure = tensor.pure_tensor(left_generator, right_generator)

    assert pure != tensor.zero()
    assert 2 * pure == tensor.zero()
    assert pure.additive_order() == 2

    beta = BilinearMap(
        left,
        right,
        right,
        {(0, 0): right_generator},
    )
    factorization = tensor.from_bilinear(beta)

    assert factorization(pure) == beta(left_generator, right_generator)

    # Universality is uniqueness, not merely existence.  Any linear map with
    # the required value on the universal pure tensor agrees on the selected
    # generating set of the tensor product and hence on every element.
    competing = module_homset(tensor, right)(
        {(0, 0): beta(left_generator, right_generator)}
    )
    _assert_module_maps_agree(factorization, competing)


def test_tensor_internal_hom_adjunction_has_bijection_naturality_functoriality_and_triangles() -> None:
    fixed = _cyclic(4)
    adjunction = tensor_hom_adjunction(fixed)
    tensor_by = adjunction.left_adjoint()
    internal_hom_from = adjunction.right_adjoint()

    source = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
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
    morphism = tensor_source.from_bilinear(beta)
    transpose = adjunction.hom_set_isomorphism_forward(morphism)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, target)
    _assert_module_maps_agree(recovered, morphism)

    hom_object = internal_hom_from(target)
    for source_label in source.module_generating_set():
        curried = transpose(source.module_generator(source_label))
        assert curried.parent() is hom_object
        assert curried(fixed_generator) == beta(
            source.module_generator(source_label),
            fixed_generator,
        )

    # Naturality of the unit under a nontrivial map of free modules.
    unit_target = BasedFreeModule(ZZ, finite_ordered_set(("c", "d", "e")))
    source_map = module_homset(source, unit_target)(
        {
            "a": unit_target.module_generator("c") + unit_target.module_generator("d"),
            "b": 2 * unit_target.module_generator("e"),
        }
    )
    left, right = adjunction.unit_transformation().naturality_square(source_map)
    _assert_module_maps_agree(left, right)

    # Naturality of evaluation under the quotient Z/4 -> Z/2.
    smaller_target = _cyclic(2)
    target_map = module_homset(target, smaller_target)(
        {0: smaller_target.module_generator(0)}
    )
    left, right = adjunction.counit_transformation().naturality_square(target_map)
    _assert_module_maps_agree(left, right)

    # Functoriality is checked on an actual nonidentity composite.
    third = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    second_map = module_homset(unit_target, third)(
        {
            "c": third.module_generator("x"),
            "d": 2 * third.module_generator("x"),
            "e": -third.module_generator("x"),
        }
    )
    tensor_composite = tensor_by(second_map * source_map)
    tensor_stepwise = tensor_by(second_map) * tensor_by(source_map)
    _assert_module_maps_agree(tensor_composite, tensor_stepwise)

    hom_composite = internal_hom_from(target_map)
    hom_identity = internal_hom_from(module_homset(target, target).identity())
    _assert_module_maps_agree(
        hom_composite * hom_identity,
        hom_composite,
    )

    # The two triangle identities are the definitive coherence conditions.
    left_triangle = (
        adjunction.counit(tensor_by(source))
        * tensor_by(adjunction.unit(source))
    )
    _assert_module_maps_agree(
        left_triangle,
        module_homset(tensor_by(source), tensor_by(source)).identity(),
    )

    right_object = internal_hom_from(target)
    right_triangle = (
        internal_hom_from(adjunction.counit(target))
        * adjunction.unit(right_object)
    )
    _assert_module_maps_agree(
        right_triangle,
        module_homset(right_object, right_object).identity(),
    )
