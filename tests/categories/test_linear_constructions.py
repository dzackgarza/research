from dzack_research.preamble.all import (
    BasedFreeModule,
    BiproductBifunctor,
    CokernelArrowFunctor,
    DualizationFunctor,
    FinitelyGeneratedFreeModules,
    FinitelyPresentedTorsionModules,
    KernelArrowFunctor,
    Lattices,
    ArrowCategory,
    FinitelyPresentedModules,
    OrthogonalDirectSumBifunctor,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_module_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for label in left.domain().module_generating_set():
        generator = left.domain().module_generator(label)
        assert left(generator) == right(generator)


def test_finite_free_dualization_is_contravariant_and_biduality_is_natural() -> None:
    m = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    n = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    p = BasedFreeModule(ZZ, finite_ordered_set(("r", "s")))
    x, y = m.module_generators()
    u, v = n.module_generators()
    r, s = p.module_generators()
    f = module_homset(m, n)({"x": u + 2 * v, "y": 3 * u - v})
    g = module_homset(n, p)({"u": 2 * r + s, "v": r - 4 * s})

    dual = DualizationFunctor(ZZ)
    f_dual = dual(f)
    assert f_dual(dual(n).module_generator("u")) == (
        dual(m).module_generator("x") + 3 * dual(m).module_generator("y")
    )
    assert f_dual(dual(n).module_generator("v")) == (
        2 * dual(m).module_generator("x") - dual(m).module_generator("y")
    )

    _assert_module_maps_agree(dual(g * f), dual(f) * dual(g))

    eta_m = dual.double_dual_morphism(m)
    eta_n = dual.double_dual_morphism(n)
    _assert_module_maps_agree(dual(dual(f)) * eta_m, eta_n * f)


def test_module_biproduct_is_both_product_and_coproduct_and_is_functorial() -> None:
    left = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))
    right = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2,))
    left_generator = left.module_generator(0)
    right_generator = right.module_generator(0)
    biproduct = BiproductBifunctor(ZZ)
    direct_sum = biproduct(left, right)

    left_identity = module_homset(left, left).identity()
    right_identity = module_homset(right, right).identity()
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

    right_to_left = module_homset(right, left)({0: 2 * left_generator})
    coproduct_map = direct_sum.from_summands(left_identity, right_to_left)
    assert coproduct_map(direct_sum.left_inclusion()(left_generator)) == left_generator
    assert (
        coproduct_map(direct_sum.right_inclusion()(right_generator))
        == 2 * left_generator
    )

    reduction = module_homset(left, right)({0: right_generator})
    product_map = direct_sum.to_product(left_identity, reduction)
    assert direct_sum.left_projection()(product_map(left_generator)) == left_generator
    assert direct_sum.right_projection()(product_map(left_generator)) == right_generator

    left_times_three = module_homset(left, left)({0: 3 * left_generator})
    right_zero = module_homset(right, right)({0: right.zero()})
    _assert_module_maps_agree(
        biproduct(left_times_three * left_times_three, right_zero * right_zero),
        biproduct(left_times_three, right_zero)
        * biproduct(left_times_three, right_zero),
    )
    _assert_module_maps_agree(
        biproduct(left_identity, right_identity),
        module_homset(direct_sum, direct_sum).identity(),
    )


def test_kernel_and_cokernel_are_functorial_on_commutative_module_squares() -> None:
    finite_free_arrow_category = ArrowCategory(FinitelyGeneratedFreeModules(ZZ))

    plane = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    line = BasedFreeModule(ZZ, finite_ordered_set(("z",)))
    x, y = plane.module_generators()
    z = line.module_generator("z")
    projection = module_homset(plane, line)({"x": z, "y": line.zero()})

    left_three = module_homset(plane, plane)({"x": 2 * x, "y": 3 * y})
    right_two = module_homset(line, line)({"z": 2 * z})
    projection_arrow = finite_free_arrow_category(projection)
    first_square = finite_free_arrow_category.morphism(
        projection_arrow, projection_arrow, left_three, right_two
    )
    left_seven = module_homset(plane, plane)({"x": 5 * x, "y": 7 * y})
    right_five = module_homset(line, line)({"z": 5 * z})
    second_square = finite_free_arrow_category.morphism(
        projection_arrow, projection_arrow, left_seven, right_five
    )

    kernel = KernelArrowFunctor(ZZ)
    kernel_object = kernel(projection_arrow)
    assert kernel_object.rank() == 1
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
        module_homset(kernel_object, kernel_object).identity(),
    )

    cyclic_source = BasedFreeModule(ZZ, finite_ordered_set(("a",)))
    cyclic_target = BasedFreeModule(ZZ, finite_ordered_set(("b",)))
    a = cyclic_source.module_generator("a")
    b = cyclic_target.module_generator("b")
    twice = module_homset(cyclic_source, cyclic_target)({"a": 2 * b})
    left3 = module_homset(cyclic_source, cyclic_source)({"a": 3 * a})
    right3 = module_homset(cyclic_target, cyclic_target)({"b": 3 * b})
    arrow_category = ArrowCategory(FinitelyPresentedModules(ZZ))
    twice_arrow = arrow_category(twice)
    square3 = arrow_category.morphism(twice_arrow, twice_arrow, left3, right3)
    left5 = module_homset(cyclic_source, cyclic_source)({"a": 5 * a})
    right5 = module_homset(cyclic_target, cyclic_target)({"b": 5 * b})
    square5 = arrow_category.morphism(twice_arrow, twice_arrow, left5, right5)

    cokernel = CokernelArrowFunctor(ZZ)
    cokernel_object = cokernel(twice_arrow)
    invariants = cokernel_object.invariant_factors()
    assert int(invariants.cardinality()) == 1
    assert invariants.unrank(0) == ZZ(2)
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
        module_homset(cokernel_object, cokernel_object).identity(),
    )

    # Cokernel functoriality is not restricted to free arrows: on the
    # presented arrow 2: Z/4 -> Z/4 the cokernel is Z/2 and multiplication by
    # three descends to its unique nonzero automorphism.
    torsion = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))
    torsion_generator = torsion.module_generator(0)
    torsion_twice = module_homset(torsion, torsion)(
        {0: 2 * torsion_generator}
    )
    torsion_times_three = module_homset(torsion, torsion)(
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
    assert torsion_invariants.unrank(0) == ZZ(2)
    induced_torsion_cokernel = cokernel(torsion_square)
    _assert_module_maps_agree(
        induced_torsion_cokernel * torsion_cokernel.cokernel_projection(),
        torsion_cokernel.cokernel_projection() * torsion_times_three,
    )


def test_orthogonal_direct_sum_is_a_bifunctor_on_lattice_morphisms() -> None:
    left = Lattices(ZZ)("A1")
    right = Lattices(ZZ)("A2")
    left_label = left.module_generating_set().unrank(0)
    right_labels = right.module_generating_set()
    left_negation = left.Isom(left)(
        {left_label: -left.module_generator(left_label)}
    )
    right_negation = right.Isom(right)(
        {label: -right.module_generator(label) for label in right_labels}
    )
    left_identity = left.Aut().identity()
    right_identity = right.Aut().identity()

    orthogonal_sum = OrthogonalDirectSumBifunctor(ZZ)
    summed = orthogonal_sum(left, right)
    image = orthogonal_sum(left_negation, right_identity)
    source_labels = summed.module_generating_set()
    assert image(summed.module_generator(source_labels[0])) == -summed.module_generator(
        source_labels[0]
    )
    assert image(summed.module_generator(source_labels[1])) == summed.module_generator(
        source_labels[1]
    )
    assert image(summed.module_generator(source_labels[2])) == summed.module_generator(
        source_labels[2]
    )

    _assert_module_maps_agree(
        orthogonal_sum(
            left_negation * left_negation, right_negation * right_negation
        ),
        orthogonal_sum(left_negation, right_negation)
        * orthogonal_sum(left_negation, right_negation),
    )
    _assert_module_maps_agree(
        orthogonal_sum(left_identity, right_identity),
        module_homset(summed, summed).identity(),
    )
