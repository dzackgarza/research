from dzack_research.preamble.all import (
    AffineSchemes,
    AffineSpace,
    AffineSpaces,
    ClosedSubschemes,
    EquationDefinedClosedSubschemes,
    IntegralSchemes,
    ProjectiveSpace,
    ProjectiveSpaces,
    ProductProjectiveSpaces,
    ProductSchemes,
    QQ,
    Schemes,
    SmoothSchemes,
    Spec,
    scheme_product,
)


def test_affine_projective_and_base_schemes_live_in_the_owned_scheme_graph() -> None:
    affine = AffineSpace(2, QQ)
    projective = ProjectiveSpace(2, QQ)
    base = Spec(QQ)

    assert affine in Schemes(QQ)
    assert affine in AffineSpaces(QQ)
    assert affine in AffineSchemes(QQ)
    assert affine in SmoothSchemes(QQ)
    assert affine in IntegralSchemes(QQ)

    assert projective in Schemes(QQ)
    assert projective in ProjectiveSpaces(QQ)
    assert projective in SmoothSchemes(QQ)
    assert projective in IntegralSchemes(QQ)

    assert base in Schemes(QQ)
    assert base in AffineSchemes(QQ)
    assert base.base_scheme() is base
    assert base.relative_dimension() == 0
    assert affine.base_scheme() is base
    assert affine.relative_dimension() == 2


def test_structure_sheaf_is_an_actual_object_with_exact_supported_global_sections() -> None:
    affine = AffineSpace(2, QQ)
    projective = ProjectiveSpace(3, QQ)

    affine_sheaf = affine.structure_sheaf()
    projective_sheaf = projective.structure_sheaf()

    assert affine_sheaf.scheme() is affine
    assert affine_sheaf.global_sections() is affine.coordinate_ring()
    assert projective_sheaf.global_sections() is QQ


def test_scheme_over_base_is_realized_in_the_generic_slice_category() -> None:
    affine = AffineSpace(2, QQ)
    base = Spec(QQ)
    slice_category = Schemes(QQ).slice_category()
    slice_object = affine.as_slice_object()

    assert slice_object in slice_category
    assert slice_object.arrow().domain() is affine
    assert slice_object.arrow().codomain() is base
    identity_square = slice_category.hom(slice_object, slice_object).identity()
    assert identity_square.domain() is slice_object
    assert identity_square.codomain() is slice_object


def test_scheme_point_is_a_morphism_from_an_owned_residue_field_scheme() -> None:
    affine = AffineSpace(2, QQ)
    point = affine.point_morphism([1, 2])

    assert point in Schemes(QQ).Mor(point.domain(), affine)
    assert point.domain() in Schemes(QQ)
    assert point.domain() in AffineSchemes(QQ)
    assert point.codomain() is affine

    structural_value = affine.structure_morphism().evaluate_at(point)
    assert structural_value in Schemes(QQ).Mor(point.domain(), Spec(QQ))
    assert structural_value.domain() is point.domain()
    assert structural_value.codomain() is Spec(QQ)


def test_equation_defined_closed_subscheme_has_live_inclusion_and_codimension() -> None:
    affine = AffineSpace(2, QQ)
    x, _y = affine.coordinate_ring().algebra_generators()
    divisor = affine.closed_subscheme(x)

    assert divisor in Schemes(QQ)
    assert divisor in ClosedSubschemes(QQ)
    assert divisor in EquationDefinedClosedSubschemes(QQ)
    assert divisor.ambient_scheme() is affine
    assert divisor.inclusion() in Schemes(QQ).Mor(divisor, affine)
    assert divisor.inclusion().domain() is divisor
    assert divisor.inclusion().codomain() is affine
    assert divisor.defining_equations() == (x,)
    assert divisor.codimension() == 1


def test_affine_space_product_is_a_scheme_product_with_actual_projections() -> None:
    line = AffineSpace(1, QQ, names=("u",))
    plane = AffineSpace(2, QQ, names=("v", "w"))
    product = scheme_product(line, plane)

    assert product in Schemes(QQ)
    assert product in AffineSpaces(QQ)
    assert product in ProductSchemes(QQ)
    assert product.relative_dimension() == 3
    assert product.factors() == (line, plane)

    point = product.point_morphism([2, 3, 5])
    first, second = product.projections()
    assert first.codomain() is line
    assert second.codomain() is plane
    first_value = first.evaluate_at(point)
    second_value = second.evaluate_at(point)
    assert first_value.domain() is point.domain()
    assert first_value.codomain() is line
    assert second_value.domain() is point.domain()
    assert second_value.codomain() is plane


def test_product_of_projective_spaces_is_the_actual_multiprojective_scheme() -> None:
    first_factor = ProjectiveSpace(1, QQ, names=("x0", "x1"))
    second_factor = ProjectiveSpace(1, QQ, names=("y0", "y1"))
    product = scheme_product(first_factor, second_factor)

    assert product in Schemes(QQ)
    assert product in ProductSchemes(QQ)
    assert product in ProductProjectiveSpaces(QQ)
    assert product.relative_dimension() == 2
    assert product.factors() == (first_factor, second_factor)

    point = product.point_morphism([1, 2, 3, 4])
    first, second = product.projections()
    assert first.codomain() is first_factor
    assert second.codomain() is second_factor
    first_value = first.evaluate_at(point)
    second_value = second.evaluate_at(point)
    assert first_value == first_factor.point_morphism([1, 2])
    assert second_value == second_factor.point_morphism([3, 4])


def test_general_affine_scheme_product_is_spec_of_algebra_coproduct() -> None:
    from dzack_research.preamble.all import (
        Coproduct,
        FinitelyPresentedAlgebra,
        PolynomialRing,
        Spec,
    )

    left_free = PolynomialRing(QQ, "x")
    right_free = PolynomialRing(QQ, "y")
    x = left_free.algebra_generator("x")
    y = right_free.algebra_generator("y")
    left_algebra = FinitelyPresentedAlgebra(left_free, (x**2,))
    right_algebra = FinitelyPresentedAlgebra(right_free, (y**3,))
    left = Spec(left_algebra)
    right = Spec(right_algebra)

    product = scheme_product(left, right)
    tensor = Coproduct(left_algebra, right_algebra)
    first, second = product.projections()

    assert product.coordinate_algebra() is tensor
    assert product.factors() == (left, right)
    assert first.domain() is product and first.codomain() is left
    assert second.domain() is product and second.codomain() is right
    assert first.coordinate_algebra_morphism() is tensor.left_coproduct_map()
    assert second.coordinate_algebra_morphism() is tensor.right_coproduct_map()


def test_affine_fiber_product_is_spec_of_algebra_pushout_with_universal_map() -> None:
    from dzack_research.preamble.all import FiberProduct, PolynomialRing, SpecFunctor

    common = PolynomialRing(QQ, "s")
    left_algebra = PolynomialRing(QQ, "x")
    right_algebra = PolynomialRing(QQ, "y")
    target_algebra = PolynomialRing(QQ, "t")
    s = common.algebra_generator("s")
    x = left_algebra.algebra_generator("x")
    y = right_algebra.algebra_generator("y")
    t = target_algebra.algebra_generator("t")

    common_to_left = common.Mor(left_algebra)({"s": x**2})
    common_to_right = common.Mor(right_algebra)({"s": y**3})
    spec = SpecFunctor(QQ)
    left_map = spec(common_to_left)
    right_map = spec(common_to_right)

    pullback = FiberProduct(left_map, right_map)
    left_projection, right_projection = pullback.fiber_product_projections()
    left_pullback = left_projection.coordinate_algebra_morphism()
    right_pullback = right_projection.coordinate_algebra_morphism()
    assert left_pullback(x) ** 2 == right_pullback(y) ** 3

    left_square = left_map * left_projection
    right_square = right_map * right_projection
    assert (
        left_square.coordinate_algebra_morphism()(s)
        == right_square.coordinate_algebra_morphism()(s)
    )

    target_to_left = spec(left_algebra.Mor(target_algebra)({"x": t**3}))
    target_to_right = spec(right_algebra.Mor(target_algebra)({"y": t**2}))
    induced = pullback.from_pullback_cone(target_to_left, target_to_right)
    assert induced.domain() is spec(target_algebra)
    assert induced.codomain() is pullback
    assert (
        (left_projection * induced).coordinate_algebra_morphism()(x)
        == target_to_left.coordinate_algebra_morphism()(x)
    )
    assert (
        (right_projection * induced).coordinate_algebra_morphism()(y)
        == target_to_right.coordinate_algebra_morphism()(y)
    )
