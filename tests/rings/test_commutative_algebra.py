from dzack_research.preamble.all import (
    AffineSpace,
    ArtinianRings,
    CompleteLocalRings,
    DualNumbers,
    GF,
    IntegralDomains,
    LocalRings,
    NoetherianRings,
    PolynomialRing,
    PowerSeriesRing,
    ProjectiveSpace,
    QQ,
    Set,
    ZZ,
)


def test_basic_commutative_ring_placements_and_canonical_ZZ_algebra() -> None:
    field = GF(5)
    polynomial = PolynomialRing(field, "t")

    assert ZZ in IntegralDomains()
    assert ZZ in NoetherianRings()
    assert field in LocalRings()
    assert field in ArtinianRings()
    assert polynomial in IntegralDomains()
    assert polynomial in NoetherianRings()

    algebra = field.as_ZZ_algebra()
    assert algebra.algebra_base_ring() is ZZ
    assert algebra.algebra_structure_morphism()(ZZ(1)) == field.one()


def test_finite_unit_localization_and_prime_localization_are_distinct() -> None:
    inverted_two = ZZ.localization(2)
    assert inverted_two.localization_source() is ZZ
    assert tuple(inverted_two.inverted_elements()) == (ZZ(2),)
    assert inverted_two.localization_map()(ZZ(3)) == inverted_two(3)
    assert inverted_two(2).is_unit()

    local_at_five = ZZ.localize_at_prime(5)
    rational = local_at_five.fraction_field()
    assert rational(1) / 2 in local_at_five
    assert rational(1) / 5 not in local_at_five
    assert local_at_five in LocalRings()
    assert int(local_at_five.residue_field().cardinality()) == 5
    assert local_at_five.maximal_ideal() == local_at_five.ideal(local_at_five(5))


def test_polynomial_prime_localization_has_expected_residue_field() -> None:
    field = GF(5)
    polynomial = PolynomialRing(field, "t")
    t = polynomial.algebra_generator("t")
    local = polynomial.localize_at_prime(polynomial.ideal(t))
    fraction = local.fraction_field()

    assert fraction((t + 1) / (t**2 + 1)) in local
    assert fraction(1 / t) not in local
    assert int(local.residue_field().cardinality()) == 5


def test_quotient_residue_field_dual_numbers_and_adic_completion() -> None:
    field = GF(5)
    polynomial = PolynomialRing(field, "t")
    t = polynomial.algebra_generator("t")

    quotient = polynomial.quotient_ring(t**2)
    tbar = quotient.quotient_map()(t)
    assert tbar != 0
    assert tbar**2 == 0

    residue = polynomial.quotient_ring(t)
    assert residue in LocalRings()
    assert int(residue.cardinality()) == 5

    dual = DualNumbers(field)
    epsilon = dual.algebra_generator("epsilon")
    assert dual in LocalRings()
    assert dual in ArtinianRings()
    assert epsilon != 0
    assert epsilon**2 == 0
    assert dual.residue_field() is field

    completion = polynomial.adic_completion(polynomial.ideal(t), precision=8)
    assert completion in CompleteLocalRings()
    assert completion.completion_source() is polynomial
    assert completion.computation_precision() == 8
    assert int(completion.residue_field().cardinality()) == 5


def test_formal_power_series_ring_is_complete_local_over_a_field() -> None:
    field = GF(7)
    power_series = PowerSeriesRing(field, "t")

    assert power_series in CompleteLocalRings()
    assert power_series.residue_field() is field
    (uniformizer,) = power_series.maximal_ideal().ideal_generators()
    assert uniformizer == power_series.algebra_generator("t")


def test_affine_and_projective_space_point_counts_and_zeta_functions() -> None:
    field = GF(5)
    affine_plane = AffineSpace(2, field)
    projective_plane = ProjectiveSpace(2, field)

    _values = affine_plane.point_counts(3)

    assert _values.cardinality() == 3

    assert _values[0] == 25

    assert _values[1] == 625

    assert _values[2] == 15625
    _values = projective_plane.point_counts(3)
    assert _values.cardinality() == 3
    assert _values[0] == 31
    assert _values[1] == 651
    assert _values[2] == 15751

    affine_zeta = affine_plane.zeta_function()
    (T,) = affine_zeta.parent().algebra_generators()
    assert affine_zeta == 1 / (1 - 25 * T)

    projective_zeta = projective_plane.zeta_function()
    (T,) = projective_zeta.parent().algebra_generators()
    assert projective_zeta == 1 / ((1 - T) * (1 - 5 * T) * (1 - 25 * T))


def test_nonfinite_base_rejects_arithmetic_zeta_interface() -> None:
    affine_line = AffineSpace(1, QQ)
    try:
        affine_line.zeta_function()
    except TypeError:
        pass
    else:
        raise AssertionError("arithmetic zeta_function must require a finite base field")


def test_submonoids_are_generic_subobjects_and_localization_retains_inclusion() -> None:
    from dzack_research.preamble.categories.abstract_categories import SubobjectsOf
    from dzack_research.preamble.categories.group.magmas import Monoids
    from dzack_research.preamble.all import generated_submonoid

    powers_of_two = generated_submonoid(ZZ, (ZZ(2),))
    subobjects = SubobjectsOf(Monoids(), ZZ)

    assert powers_of_two in subobjects
    assert powers_of_two.inclusion().domain() is powers_of_two
    assert powers_of_two.inclusion().codomain() is ZZ
    assert powers_of_two.inclusion().is_injective()

    slice_object = subobjects.as_slice_object(powers_of_two)
    assert slice_object.arrow() is powers_of_two.inclusion()
    assert slice_object in subobjects.slice_category()
    assert slice_object in subobjects.monomorphism_category()

    localization = ZZ.localization(powers_of_two)
    assert localization.localization_submonoid() is powers_of_two
    assert tuple(localization.inverted_elements()) == (ZZ(2),)

    local_at_five = ZZ.localize_at_prime(5)
    prime_complement = local_at_five.localization_submonoid()
    assert prime_complement in subobjects
    assert ZZ(2) in prime_complement
    assert ZZ(5) not in prime_complement


def test_affine_prime_spectrum_zariski_basis_and_structure_sheaf_stalks() -> None:
    affine_line = AffineSpace(1, QQ, names=("x",))
    spectrum = affine_line.underlying_space()
    ring = spectrum.ring()
    x = ring.algebra_generator("x")

    generic = spectrum(ring.ideal(0))
    origin = spectrum(ring.ideal(x))

    from dzack_research.preamble.categories.modules import Modules, ring_as_module
    from dzack_research.preamble.categories.abstract_categories import SubobjectsOf
    assert origin.ideal() in SubobjectsOf(Modules(spectrum.ring()), ring_as_module(spectrum.ring()))
    assert origin.ideal().inclusion().codomain() is ring_as_module(spectrum.ring())

    assert generic.specializes_to(origin)
    assert not origin.specializes_to(generic)
    assert spectrum.generic_point() == generic

    closed_origin = spectrum.V(x)
    assert closed_origin.defining_ideal() in SubobjectsOf(
        Modules(spectrum.ring()), ring_as_module(spectrum.ring())
    )
    punctured_line = spectrum.D(x)
    assert generic not in closed_origin
    assert origin in closed_origin
    assert generic in punctured_line
    assert origin not in punctured_line

    sheaf = affine_line.structure_sheaf()
    principal_sections = sheaf.sections_on_distinguished_open(punctured_line)
    assert principal_sections.localization_source() is spectrum.ring()
    assert principal_sections.inverted_elements() == Set((spectrum.ring()(x),))

    stalk = sheaf.stalk(origin)
    assert stalk is origin.local_ring()
    assert stalk.localization_source() is spectrum.ring()
    assert int(stalk.residue_field().characteristic()) == 0


def test_polynomial_ideals_are_module_subobjects_with_singular_arithmetic() -> None:
    from dzack_research.preamble.categories.abstract_categories import SubobjectsOf
    from dzack_research.preamble.categories.modules import Modules, ring_as_module

    ring = PolynomialRing(QQ, ("x", "y"))
    x, y = ring.algebra_generators()
    ideal = ring.ideal(x**2, x * y)
    other = ring.ideal(y)

    subobjects = SubobjectsOf(Modules(ring), ring_as_module(ring))
    assert ideal in subobjects
    assert ideal.inclusion().codomain() is ring_as_module(ring)
    assert ideal.inclusion().is_injective()
    assert ideal == ring.ideal(ring(x**2), ring(x * y))

    def same_ideal(left, right):
        return all(generator in right for generator in left.ideal_generators()) and all(
            generator in left for generator in right.ideal_generators()
        )

    assert same_ideal(ideal.radical(), ring.ideal(x))
    assert same_ideal(ideal.sum(other), ring.ideal(x**2, x * y, y))
    assert same_ideal(ideal.product(other), ring.ideal(x**2 * y, x * y**2))
    assert same_ideal(ideal.intersection(other), ring.ideal(x * y))


def test_affine_spec_is_contravariant_on_commutative_algebra_maps() -> None:
    from dzack_research.preamble.all import CommutativeAlgebras, Spec, SpecFunctor

    source = PolynomialRing(QQ, "x")
    middle = PolynomialRing(QQ, "t")
    target = PolynomialRing(QQ, "u")
    x = source.algebra_generator("x")
    t = middle.algebra_generator("t")
    u = target.algebra_generator("u")

    assert source in CommutativeAlgebras(QQ)
    assert middle in CommutativeAlgebras(QQ)
    assert target in CommutativeAlgebras(QQ)

    first = source.Mor(middle)({"x": middle(t**2)})
    second = middle.Mor(target)({"t": target(u + 1)})
    composite = second * first

    spec = SpecFunctor(QQ)
    spec_source = spec(source)
    spec_middle = spec(middle)
    spec_target = spec(target)

    assert spec_source is Spec(source)
    assert spec_source.scheme_base_ring() is QQ
    assert spec_source.coordinate_algebra() is source
    assert spec_source.structure_sheaf().global_sections() is source

    first_spec = spec(first)
    second_spec = spec(second)
    composite_spec = spec(composite)

    assert first_spec.domain() is spec_middle
    assert first_spec.codomain() is spec_source
    assert second_spec.domain() is spec_target
    assert second_spec.codomain() is spec_middle
    assert first_spec.coordinate_algebra_morphism() is first
    assert second_spec.coordinate_algebra_morphism() is second

    # Spec(second * first) = Spec(first) * Spec(second), checked through the
    # represented pullback on coordinate algebras and endpoints.
    composed_scheme = first_spec * second_spec
    assert composed_scheme.domain() is spec_target
    assert composed_scheme.codomain() is spec_source
    assert composite_spec.coordinate_algebra_morphism()(source(x)) == composite(source(x))

    identity = CommutativeAlgebras(QQ).Mor(source, source).identity()
    identity_spec = spec(identity)
    assert identity_spec.domain() is spec_source
    assert identity_spec.codomain() is spec_source


def test_commutative_algebra_coproduct_is_tensor_product_with_universal_maps() -> None:
    from dzack_research.preamble.all import Coproduct

    left = PolynomialRing(QQ, "x")
    right = PolynomialRing(QQ, "y")
    coproduct = Coproduct(left, right)
    left_map, right_map = coproduct.coproduct_injections()

    x = left.algebra_generator("x")
    y = right.algebra_generator("y")
    assert left_map.domain() is left and left_map.codomain() is coproduct
    assert right_map.domain() is right and right_map.codomain() is coproduct

    target = PolynomialRing(QQ, "t")
    t = target.algebra_generator("t")
    f = left.Mor(target)({"x": t})
    g = right.Mor(target)({"y": t**2})
    induced = coproduct.from_cocone(f, g)
    assert induced(left_map(x)) == t
    assert induced(right_map(y)) == t**2


def test_commutative_algebra_coproduct_transports_quotient_relations() -> None:
    from dzack_research.preamble.all import Coproduct, FinitelyPresentedAlgebra

    left_free = PolynomialRing(QQ, "x")
    right_free = PolynomialRing(QQ, "y")
    x = left_free.algebra_generator("x")
    y = right_free.algebra_generator("y")
    left = FinitelyPresentedAlgebra(left_free, (x**2,))
    right = FinitelyPresentedAlgebra(right_free, (y**3,))

    coproduct = Coproduct(left, right)
    left_map, right_map = coproduct.coproduct_injections()
    xbar = left.algebra_generator("x")
    ybar = right.algebra_generator("y")
    assert left_map(xbar) ** 2 == 0
    assert right_map(ybar) ** 3 == 0


def test_commutative_algebra_pushout_imposes_common_source_relations() -> None:
    from dzack_research.preamble.all import Pushout

    common = PolynomialRing(QQ, "s")
    left = PolynomialRing(QQ, "x")
    right = PolynomialRing(QQ, "y")
    s = common.algebra_generator("s")
    x = left.algebra_generator("x")
    y = right.algebra_generator("y")
    left_span = common.Mor(left)({"s": x**2})
    right_span = common.Mor(right)({"s": y**3})

    pushout = Pushout(left_span, right_span)
    left_map, right_map = pushout.pushout_maps()
    assert left_map(x) ** 2 == right_map(y) ** 3

    target = PolynomialRing(QQ, "t")
    t = target.algebra_generator("t")
    left_cocone = left.Mor(target)({"x": t**3})
    right_cocone = right.Mor(target)({"y": t**2})
    induced = pushout.from_pushout_cocone(left_cocone, right_cocone)
    assert induced(left_map(x)) == t**3
    assert induced(right_map(y)) == t**2
    assert left_cocone(left_span(s)) == right_cocone(right_span(s)) == t**6


def test_module_local_fiber_rank_generic_rank_and_fitting_loci() -> None:
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        BasedFreeModule,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    free_target = BasedFreeModule(ring, 1)
    free_relations = BasedFreeModule(ring, 1)
    module = FinitelyPresentedModule(
        module_homset(free_relations, free_target)(
            {0: x * free_target.module_generator(0)}
        )
    )

    spectrum = ring.spectrum()
    generic = spectrum.generic_point()
    origin = spectrum(ring.ideal(x))

    assert module.rank_at(generic) == 0
    assert module.generic_rank() == 0
    assert module.rank_at(origin) == 1
    assert module.fiber_dimension(origin) == module.fiber(origin).dimension()
    assert module.local_number_of_generators(origin) == 1
    localized_at_origin = module.localize_at_prime(origin)
    assert localized_at_origin.minimal_number_of_generators() == 1
    residue_module = localized_at_origin.residue_module()
    assert localized_at_origin.minimal_number_of_generators() == residue_module.dimension()
    assert residue_module.basis_generator_labels().cardinality() == residue_module.dimension()
    assert localized_at_origin.submodule(
        localized_at_origin.minimal_module_generators()
    ) == localized_at_origin
    assert origin.residue_map()(ring(x)) == origin.residue_field().zero()

    fitting_zero = module.fitting_ideal(0)
    assert fitting_zero == ring.ideal(ring(x))
    assert module.annihilator() == fitting_zero
    assert module.annihilator() == module.scalar_action().kernel()
    assert generic not in module.support()
    assert origin in module.support()
    assert generic not in module.annihilator_support()
    assert origin in module.annihilator_support()
    assert generic not in module.fiber_dimension_at_least(1)
    assert origin in module.fiber_dimension_at_least(1)

    free_rank_two = BasedFreeModule(ring, 2)
    assert free_rank_two.rank_at(generic) == 2
    assert free_rank_two.rank_at(origin) == 2
    assert free_rank_two.generic_rank() == 2
    assert free_rank_two.projective_rank(origin) == 2


def test_module_localization_is_first_class_and_fibers_factor_through_it() -> None:
    from dzack_research.preamble.all import FreeModule, LocalizedModules
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    free = FreeModule(ZZ, 1)
    generator = free.module_generator(0)
    p2 = ZZ.spectrum()(2)
    localized_free = free.localize_at_prime(p2)

    assert localized_free in LocalizedModules(p2.local_ring())
    assert localized_free.localization_source_module() is free
    assert localized_free.localization_ring() is p2.local_ring()
    assert localized_free.localization_prime_point() == p2
    assert localized_free.localization_submonoid() is p2.local_ring().localization_submonoid()

    unit = localized_free.localization_unit()
    assert unit.domain() is free
    assert unit(generator).underlying_element() == localized_free.module_generator(0)

    multiplication_by_three = module_homset(free, free)({0: 3 * generator})
    localized_map = localized_free.localization_functor()(multiplication_by_three)
    assert localized_map.domain() is localized_free
    assert localized_map(localized_free.module_generator(0)) == localized_free.scalar_multiple(
        3, localized_free.module_generator(0)
    )

    torsion = FinitelyPresentedModule(
        module_homset(free, free)({0: 6 * generator})
    )
    p5 = ZZ.spectrum()(5)
    torsion_at_two = torsion.localize_at_prime(p2)
    torsion_at_five = torsion.localize_at_prime(p5)
    assert torsion.annihilator() == ZZ.ideal(ZZ(6))
    assert torsion.annihilator() == torsion.scalar_action().kernel()
    assert free.annihilator() == ZZ.ideal(ZZ.zero())
    assert free.annihilator() == free.scalar_action().kernel()
    zero_free = FreeModule(ZZ, 0)
    assert zero_free.annihilator() == ZZ.ideal(ZZ.one())
    assert torsion_at_two.localization_source_module() is torsion
    assert torsion_at_five.localization_source_module() is torsion
    assert torsion.rank_at(p2) == 1
    assert torsion.rank_at(p5) == 0

    polynomial = PolynomialRing(QQ, "x")
    x = polynomial.algebra_generator("x")
    polynomial_free = FreeModule(polynomial, 1)
    quotient = FinitelyPresentedModule(
        module_homset(polynomial_free, polynomial_free)(
            {0: x * polynomial_free.module_generator(0)}
        )
    )
    origin = polynomial.spectrum()(polynomial.ideal(x))
    local_quotient = quotient.localize_at_prime(origin)
    fiber = quotient.fiber(origin)
    assert fiber._preamble_fiber_localization is local_quotient
    assert local_quotient.localization_prime_point() == origin


def test_elementwise_module_morphism_verification_is_regime_sensitive(caplog) -> None:
    import logging

    from dzack_research.preamble.all import FreeModule, GF, module_homset, ring_as_module

    field = GF(3)
    finite = ring_as_module(field)
    finite_hom = module_homset(finite, finite)
    linear = finite_hom.elementwise(
        lambda element: finite.scalar_multiple(field(2), element)
    )
    assert linear(field.one()) == finite(field(2))

    try:
        finite_hom.elementwise(
            lambda element: field(element**2)
        )
    except ValueError as error:
        assert "not additive" in str(error) or "not scalar-linear" in str(error)
    else:
        raise AssertionError("a nonlinear map on a finite module must be rejected")

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    infinite = FreeModule(ZZ, 1)
    with caplog.at_level(
        logging.DEBUG,
        logger="dzack_research.preamble.categories.modules.module_morphisms.module_morphisms",
    ):
        basis_label = infinite.module_generating_set().unrank(0)
        declared = module_homset(infinite, infinite).elementwise(
            lambda vector: infinite(
                (module_coefficients(vector, infinite).get(basis_label, ZZ.zero()) ** 2,)
            )
        )
    assert declared(infinite.module_generator(0)) == infinite.module_generator(0)
    assert any("without exhaustive linearity verification" in record.message for record in caplog.records)


def test_general_module_localization_uses_fraction_model_and_detects_s_torsion() -> None:
    from dzack_research.preamble.all import GeneralModule, LocalizedModules, Set, module_homset

    underlying_set = Set([0, 1, 2, 3, 4, 5])
    module = GeneralModule(
        ZZ,
        underlying_set,
        addition=lambda left, right: (left + right) % 6,
        zero=0,
        negation=lambda value: (-value) % 6,
        scalar_action=lambda scalar, value: (int(scalar) * value) % 6,
    )
    localization = ZZ.localization(2)
    localized = module.localize(localization)

    assert localized in LocalizedModules(localization)
    assert localized.localization_source_module() is module
    assert localized.localization_ring() is localization

    half = localized.fraction(module(1), 2)
    assert half.equality_status(localized.fraction(module(2))) is True
    assert localized.fraction(module(3)).equality_status(localized.zero()) is True
    assert localized.fraction(module(1)).equality_status(localized.zero()) is False

    assert (localization(3) / localization(2)) * half == localized.fraction(module(3), 4)

    unit = localized.localization_unit()
    assert unit(module(1)).underlying_element() == localized.fraction(module(1))

    doubling = module_homset(module, module).elementwise(
        lambda element: module((2 * element.underlying_element()) % 6)
    )
    localized_doubling = localized.localization_functor()(doubling)
    assert localized_doubling(half) == localized.fraction(module(2), 2)


def test_ideal_localization_extension_contraction_colon_and_saturation() -> None:
    integer_ideal = ZZ.ideal(6)
    inverted_two = ZZ.localization(2)
    extended_integer_ideal = integer_ideal.extension(inverted_two)

    assert extended_integer_ideal.inclusion().is_injective()
    assert 3 in extended_integer_ideal
    assert 1 not in extended_integer_ideal
    assert extended_integer_ideal.contraction() == ZZ.ideal(ZZ(3))

    ring = PolynomialRing(QQ, ("x", "y"))
    x, y = ring.algebra_generators()
    ideal = ring.ideal(x * y, y**2)
    divisor = ring.ideal(x)

    assert ideal.colon(divisor) == ring.ideal(ring(y))
    assert ideal.saturation(divisor) == ring.ideal(ring(y))

    localized_ring = ring.localization(x)
    extended = ideal.extension(localized_ring)
    assert extended.inclusion().is_injective()
    assert localized_ring(y) in extended
    assert localized_ring.one() not in extended
    assert extended.contraction() == ring.ideal(ring(y))


def test_quotient_localization_comparison_is_an_actual_ring_isomorphism() -> None:
    quotient = ZZ.quotient_ring(ZZ.ideal(6))
    localization = ZZ.localization(2)
    comparison = quotient.localization_comparison(localization)

    left = comparison.localized_quotient()
    right = comparison.quotient_after_localization()
    forward = comparison.forward()
    inverse = comparison.inverse()
    quotient_map = quotient.quotient_map()

    half = left.fraction(quotient_map(1), quotient_map(2))
    assert forward(half) == right(localization(1) / 2)
    assert inverse(forward(half)) == half

    right_half = right(localization(1) / 2)
    assert forward(inverse(right_half)) == right_half
    assert comparison.extended_ideal().contraction() == ZZ.ideal(ZZ(3))

    ring = PolynomialRing(QQ, ("x", "y"))
    x, y = ring.algebra_generators()
    polynomial_quotient = ring.quotient_ring(ring.ideal(x * y, y**2))
    polynomial_localization = ring.localization(x)
    polynomial_comparison = polynomial_quotient.localization_comparison(
        polynomial_localization
    )
    polynomial_left = polynomial_comparison.localized_quotient()
    polynomial_right = polynomial_comparison.quotient_after_localization()
    polynomial_quotient_map = polynomial_quotient.quotient_map()

    assert polynomial_left(polynomial_quotient_map(y)) == polynomial_left.zero()
    assert polynomial_comparison.forward()(
        polynomial_left(polynomial_quotient_map(y))
    ) == polynomial_right.zero()
    element = polynomial_right(polynomial_localization(y + 1))
    assert polynomial_comparison.forward()(
        polynomial_comparison.inverse()(element)
    ) == element


def test_module_localization_exactness_preserves_kernels_and_cokernels() -> None:
    from dzack_research.preamble.categories.modules import FreeModule, module_homset

    source = FreeModule(ZZ, 2)
    target = FreeModule(ZZ, 1)
    morphism = module_homset(source, target)(
        {
            0: target.module_generator(0),
            1: target.zero(),
        }
    )
    localization = ZZ.localization(2)
    functor = source.localize(localization).localization_functor()

    kernel_comparison = functor.kernel_comparison(morphism)
    assert functor.is_exact()
    assert (
        kernel_comparison.localized_kernel()
        is kernel_comparison.kernel_of_localized_morphism()
    )
    assert (
        kernel_comparison.localized_kernel().inclusion().codomain()
        is functor(source)
    )

    rank_one = FreeModule(ZZ, 1)
    generator = rank_one.module_generator(0)
    multiplication_by_six = module_homset(rank_one, rank_one)(
        {0: 6 * generator}
    )
    cokernel_comparison = functor.cokernel_comparison(multiplication_by_six)
    left = cokernel_comparison.localized_cokernel()
    right = cokernel_comparison.cokernel_of_localized_morphism()
    left_generator = left.module_generator(0)
    right_generator = right.module_generator(0)
    assert cokernel_comparison.inverse()(
        cokernel_comparison.forward()(left_generator)
    ) == left_generator
    assert cokernel_comparison.forward()(
        cokernel_comparison.inverse()(right_generator)
    ) == right_generator


def test_nakayama_minimal_generators_and_surjectivity_are_local_module_operations() -> None:
    from dzack_research.preamble.categories.modules import FreeModule, module_homset
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
    )

    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    origin = ring.spectrum()(ring.ideal(ring.algebra_generator("x")))
    local = origin.local_ring()
    free = FreeModule(local, 1)
    generator = free.module_generator(0)
    quotient = FinitelyPresentedModule(
        module_homset(free, free)(
            {0: free.scalar_multiple(local(x), generator)}
        )
    )

    assert quotient.minimal_number_of_generators() == 1
    assert quotient.minimal_number_of_generators() == quotient.residue_module().dimension()
    assert quotient.submodule(quotient.minimal_module_generators()) == quotient

    projection = module_homset(free, quotient)(
        {0: quotient.module_generator(0)}
    )
    residue_projection = projection.residue_morphism()
    residue_generator = residue_projection.domain().module_generator(0)
    assert residue_projection(residue_generator) == residue_projection.codomain().module_generator(0)
    assert projection.is_surjective_mod_maximal_ideal()
    assert projection.is_surjective_by_nakayama()

    multiplication_by_x = module_homset(free, free)(
        {0: free.scalar_multiple(local(x), generator)}
    )
    assert not multiplication_by_x.is_surjective_mod_maximal_ideal()
    assert not multiplication_by_x.is_surjective_by_nakayama()


def test_general_module_materializes_from_an_underlying_set_and_action() -> None:
    from dzack_research.preamble.all import GeneralModule, Modules, module_homset

    field = GF(3)
    module = GeneralModule(
        field,
        [0, 1, 2],
        addition=lambda left, right: (left + right) % 3,
        zero=0,
        negation=lambda value: (-value) % 3,
        scalar_action=lambda scalar, value: (int(scalar) * value) % 3,
    )

    assert module in Modules(field)
    assert module(1) + module(2) == module(0)
    assert -module(1) == module(2)
    assert module.scalar_multiple(field(2), module(2)) == module(1)
    assert module.scalar_action()(field(2))(module(2)) == module(1)

    doubling = module_homset(module, module).elementwise(
        lambda element: module((2 * element.underlying_element()) % 3)
    )
    assert doubling(module(2)) == module(1)

    try:
        module_homset(module, module).elementwise(
            lambda element: module((element.underlying_element() ** 2) % 3)
        )
    except ValueError as error:
        assert "not additive" in str(error) or "not scalar-linear" in str(error)
    else:
        raise AssertionError("finite general modules must reject a nonlinear elementwise map")

    assert module.annihilator() == field.ideal(field.zero())
    assert module.annihilator() == module.scalar_action().kernel()
