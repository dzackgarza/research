from dzack_research.preamble.all import (
    ZZ,
    FinitelyGeneratedFreeModules,
    FinitelyPresentedModules,
    FinitelyPresentedTorsionModules,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_module_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for label in left.domain().module_generating_set():
        generator = left.domain().module_generator(label)
        assert left(generator) == right(generator)


def _product_object(functor, left, right):
    return functor.domain()(left, right)


def _product_morphism(functor, left, right):
    source = _product_object(functor, left.domain(), right.domain())
    target = _product_object(functor, left.codomain(), right.codomain())
    return functor.domain().Mor(source, target)(left, right)


def _opposite_object(functor, obj):
    return functor.domain()(obj)


def _opposite_morphism(functor, morphism):
    source = _opposite_object(functor, morphism.codomain())
    target = _opposite_object(functor, morphism.domain())
    return functor.domain().Mor(source, target)(morphism)


def test_finite_free_dualization_is_contravariant_and_biduality_is_natural() -> None:
    m = ZZ.free_module(finite_ordered_set(("x", "y")))
    n = ZZ.free_module(finite_ordered_set(("u", "v")))
    p = ZZ.free_module(finite_ordered_set(("r", "s")))
    x, y = m.module_generators()
    u, v = n.module_generators()
    r, s = p.module_generators()
    f = m.module_category().Mor(m, n)({"x": u + 2 * v, "y": 3 * u - v})
    g = n.module_category().Mor(n, p)({"u": 2 * r + s, "v": r - 4 * s})

    dual = FinitelyGeneratedFreeModules(ZZ).dualization()
    f_dual = dual(_opposite_morphism(dual, f))
    assert f_dual(dual(_opposite_object(dual, n)).module_generator("u")) == (
        dual(_opposite_object(dual, m)).module_generator("x")
        + 3 * dual(_opposite_object(dual, m)).module_generator("y")
    )
    assert f_dual(dual(_opposite_object(dual, n)).module_generator("v")) == (
        2 * dual(_opposite_object(dual, m)).module_generator("x")
        - dual(_opposite_object(dual, m)).module_generator("y")
    )

    _assert_module_maps_agree(
        dual(_opposite_morphism(dual, g * f)),
        dual(_opposite_morphism(dual, f)) * dual(_opposite_morphism(dual, g)),
    )

    eta_m = dual.double_dual_morphism(m)
    eta_n = dual.double_dual_morphism(n)
    _assert_module_maps_agree(
        dual(_opposite_morphism(dual, dual(_opposite_morphism(dual, f)))) * eta_m,
        eta_n * f,
    )


def test_module_biproduct_is_both_product_and_coproduct_and_is_functorial() -> None:
    left = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))
    right = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2,))
    left_generator = left.module_generator(0)
    right_generator = right.module_generator(0)
    biproduct = FinitelyPresentedModules(ZZ).biproduct_bifunctor()
    direct_sum = biproduct(_product_object(biproduct, left, right))

    left_identity = left.module_category().Mor(left, left).identity()
    right_identity = right.module_category().Mor(right, right).identity()
    _assert_module_maps_agree(
        direct_sum.left_projection() * direct_sum.left_inclusion(),
        left_identity,
    )
    _assert_module_maps_agree(
        direct_sum.right_projection() * direct_sum.right_inclusion(),
        right_identity,
    )
    assert (
        direct_sum.right_projection()(direct_sum.left_inclusion()(left_generator))
        == right.zero()
    )
    assert (
        direct_sum.left_projection()(direct_sum.right_inclusion()(right_generator))
        == left.zero()
    )

    right_to_left = right.module_category().Mor(right, left)({0: 2 * left_generator})
    coproduct_map = direct_sum.from_summands(left_identity, right_to_left)
    assert coproduct_map(direct_sum.left_inclusion()(left_generator)) == left_generator
    assert (
        coproduct_map(direct_sum.right_inclusion()(right_generator))
        == 2 * left_generator
    )

    reduction = left.module_category().Mor(left, right)({0: right_generator})
    product_map = direct_sum.to_product(left_identity, reduction)
    assert direct_sum.left_projection()(product_map(left_generator)) == left_generator
    assert direct_sum.right_projection()(product_map(left_generator)) == right_generator

    left_times_three = left.module_category().Mor(left, left)({0: 3 * left_generator})
    right_zero = right.module_category().Mor(right, right)({0: right.zero()})
    _assert_module_maps_agree(
        biproduct(
            _product_morphism(
                biproduct,
                left_times_three * left_times_three,
                right_zero * right_zero,
            )
        ),
        biproduct(_product_morphism(biproduct, left_times_three, right_zero))
        * biproduct(_product_morphism(biproduct, left_times_three, right_zero)),
    )
    _assert_module_maps_agree(
        biproduct(_product_morphism(biproduct, left_identity, right_identity)),
        direct_sum.module_category().Mor(direct_sum, direct_sum).identity(),
    )


def test_kernel_and_cokernel_are_functorial_on_commutative_module_squares() -> None:
    finite_free_arrow_category = FinitelyGeneratedFreeModules(ZZ).ArrowCategory()

    plane = ZZ.free_module(finite_ordered_set(("x", "y")))
    line = ZZ.free_module(finite_ordered_set(("z",)))
    x, y = plane.module_generators()
    z = line.module_generator("z")
    projection = plane.module_category().Mor(plane, line)({"x": z, "y": line.zero()})

    left_three = plane.module_category().Mor(plane, plane)({"x": 2 * x, "y": 3 * y})
    right_two = line.module_category().Mor(line, line)({"z": 2 * z})
    projection_arrow = finite_free_arrow_category(projection)
    first_square = finite_free_arrow_category.morphism(
        projection_arrow, projection_arrow, left_three, right_two
    )
    left_seven = plane.module_category().Mor(plane, plane)({"x": 5 * x, "y": 7 * y})
    right_five = line.module_category().Mor(line, line)({"z": 5 * z})
    second_square = finite_free_arrow_category.morphism(
        projection_arrow, projection_arrow, left_seven, right_five
    )

    kernel = FinitelyGeneratedFreeModules(ZZ).kernel_arrow_functor()
    kernel_object = kernel(projection_arrow)
    assert kernel_object.module_rank() == 1
    induced_kernel = kernel(first_square)
    _assert_module_maps_agree(
        kernel_object.inclusion() * induced_kernel,
        left_three * kernel_object.inclusion(),
    )
    _assert_module_maps_agree(
        kernel(finite_free_arrow_category.compose(second_square, first_square)),
        kernel(second_square) * kernel(first_square),
    )
    _assert_module_maps_agree(
        kernel(finite_free_arrow_category.identity(projection_arrow)),
        kernel_object.module_category().Mor(kernel_object, kernel_object).identity(),
    )

    cyclic_source = ZZ.free_module(finite_ordered_set(("a",)))
    cyclic_target = ZZ.free_module(finite_ordered_set(("b",)))
    a = cyclic_source.module_generator("a")
    b = cyclic_target.module_generator("b")
    twice = cyclic_source.module_category().Mor(cyclic_source, cyclic_target)({"a": 2 * b})
    left3 = cyclic_source.module_category().Mor(cyclic_source, cyclic_source)({"a": 3 * a})
    right3 = cyclic_target.module_category().Mor(cyclic_target, cyclic_target)({"b": 3 * b})
    arrow_category = FinitelyPresentedModules(ZZ).ArrowCategory()
    twice_arrow = arrow_category(twice)
    square3 = arrow_category.morphism(twice_arrow, twice_arrow, left3, right3)
    left5 = cyclic_source.module_category().Mor(cyclic_source, cyclic_source)({"a": 5 * a})
    right5 = cyclic_target.module_category().Mor(cyclic_target, cyclic_target)({"b": 5 * b})
    square5 = arrow_category.morphism(twice_arrow, twice_arrow, left5, right5)

    cokernel = FinitelyPresentedModules(ZZ).cokernel_arrow_functor()
    cokernel_object = cokernel(twice_arrow)
    invariants = cokernel_object.invariant_factors()
    assert int(invariants.cardinality()) == 1
    assert invariants[0] == ZZ(2)
    induced_cokernel = cokernel(square3)
    _assert_module_maps_agree(
        induced_cokernel * cokernel_object.cokernel_projection(),
        cokernel_object.cokernel_projection() * right3,
    )
    _assert_module_maps_agree(
        cokernel(arrow_category.compose(square5, square3)),
        cokernel(square5) * cokernel(square3),
    )
    _assert_module_maps_agree(
        cokernel(arrow_category.identity(twice_arrow)),
        cokernel_object.module_category().Mor(cokernel_object, cokernel_object).identity(),
    )

    # Cokernel functoriality is not restricted to free arrows: on the
    # presented arrow 2: Z/4 -> Z/4 the cokernel is Z/2 and multiplication by
    # three descends to its unique nonzero automorphism.
    torsion = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))
    torsion_generator = torsion.module_generator(0)
    torsion_twice = torsion.module_category().Mor(torsion, torsion)(
        {0: 2 * torsion_generator}
    )
    torsion_times_three = torsion.module_category().Mor(torsion, torsion)(
        {0: 3 * torsion_generator}
    )
    torsion_twice_arrow = arrow_category(torsion_twice)
    torsion_square = arrow_category.morphism(
        torsion_twice_arrow,
        torsion_twice_arrow,
        torsion_times_three,
        torsion_times_three,
    )
    torsion_cokernel = cokernel(torsion_twice_arrow)
    torsion_invariants = torsion_cokernel.invariant_factors()
    assert int(torsion_invariants.cardinality()) == 1
    assert torsion_invariants[0] == ZZ(2)
    induced_torsion_cokernel = cokernel(torsion_square)
    _assert_module_maps_agree(
        induced_torsion_cokernel * torsion_cokernel.cokernel_projection(),
        torsion_cokernel.cokernel_projection() * torsion_times_three,
    )


