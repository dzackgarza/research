from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.all import (
    AffineSchemes,
    AffineSpace,
    AffineSpaces,
    ClosedEmbeddings,
    IntegralSchemes,
    ProjectiveSpace,
    ProjectiveSpaces,
    ProductProjectiveSpaces,
    ProductSchemes,
    QQ,
    Schemes,
    SmoothSchemes,
    Spec,
    ZZ,
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


def test_space_dimensions_accept_owned_and_backend_integer_numerals() -> None:
    assert AffineSpace(ZZ(2), QQ).relative_dimension() == 2
    assert ProjectiveSpace(SageZZ(2), QQ).relative_dimension() == 2


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
    identity_square = slice_category.Mor(slice_object, slice_object).identity()
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


def test_a_closed_subscheme_carries_its_inclusion_and_knows_its_codimension() -> None:
    affine = AffineSpace(2, QQ)
    x, _y = affine.coordinate_ring().algebra_generators()
    divisor = affine.closed_subscheme(x)

    assert divisor in Schemes(QQ)
    assert divisor in ClosedEmbeddings(affine)
    assert divisor.ambient_scheme() is affine
    assert divisor.inclusion() in Schemes(QQ).Mor(divisor, affine)
    assert divisor.inclusion().domain() is divisor
    assert divisor.inclusion().codomain() is affine
    _values = divisor.defining_equations()
    assert _values.cardinality() == 1
    assert _values[0] == x
    assert divisor.codimension() == 1


def test_affine_space_product_is_a_scheme_product_with_actual_projections() -> None:
    line = AffineSpace(1, QQ, names=("u",))
    plane = AffineSpace(2, QQ, names=("v", "w"))
    product = scheme_product(line, plane)

    assert product in Schemes(QQ)
    assert product in AffineSpaces(QQ)
    assert product in ProductSchemes(QQ)
    assert product.relative_dimension() == 3

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
        FinitelyPresentedAlgebra,
        PolynomialRing,
        Spec,
    )
    from dzack_research.preamble.categories.abstract_categories import Coproduct

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
    assert first.domain() is product and first.codomain() is left
    assert second.domain() is product and second.codomain() is right
    assert first.coordinate_algebra_morphism() is tensor.left_coproduct_map()
    assert second.coordinate_algebra_morphism() is tensor.right_coproduct_map()


def test_affine_spec_and_fiber_product_maps_keep_their_owned_endpoints() -> None:
    from dzack_research.preamble.all import PolynomialRing, SpecFunctor
    from dzack_research.preamble.categories.abstract_categories import FiberProduct

    base = Spec(QQ)
    assert base.scheme_base_ring() is QQ
    assert base.structure_morphism().domain() is base
    assert base.structure_morphism().codomain() is base
    assert Spec(QQ) is base

    common = PolynomialRing(QQ, "s")
    left_algebra = PolynomialRing(QQ, "x")
    right_algebra = PolynomialRing(QQ, "y")
    target_algebra = PolynomialRing(QQ, "t")
    s = common.algebra_generator("s")
    x = left_algebra.algebra_generator("x")
    y = right_algebra.algebra_generator("y")
    t = target_algebra.algebra_generator("t")

    spec = SpecFunctor(QQ)
    left = spec(left_algebra)
    assert left.structure_morphism().domain() is left
    assert left.structure_morphism().codomain() is base
    assert left.categorical_identity_morphism().domain() is left
    assert left.categorical_identity_morphism().codomain() is left

    left_map = spec(common.Mor(left_algebra)({"s": x**2}))
    right_map = spec(common.Mor(right_algebra)({"s": y**3}))
    assert left_map.domain() is left
    assert left_map.codomain() is spec(common)

    pullback = FiberProduct(left_map, right_map)
    left_projection, right_projection = pullback.fiber_product_projections()
    assert left_projection.domain() is pullback
    assert left_projection.codomain() is left
    assert right_projection.domain() is pullback
    assert right_projection.codomain() is spec(right_algebra)
    assert (
        left_projection.coordinate_algebra_morphism()(x) ** 2
        == right_projection.coordinate_algebra_morphism()(y) ** 3
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


def test_affine_fiber_product_is_spec_of_algebra_pushout_with_universal_map() -> None:
    from dzack_research.preamble.all import PolynomialRing, SpecFunctor
    from dzack_research.preamble.categories.abstract_categories import FiberProduct

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


def test_xy_equals_t_family_has_its_t_zero_special_fiber_as_a_pullback() -> None:
    from dzack_research.preamble.all import FinitelyPresentedAlgebra, PolynomialRing, SpecFunctor
    from dzack_research.preamble.categories.abstract_categories import FiberProduct

    parameter = PolynomialRing(QQ, "t")
    t = parameter.algebra_generator("t")
    presentation = PolynomialRing(parameter, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family_algebra = FinitelyPresentedAlgebra(presentation, (x * y - t,))
    residue_algebra = parameter.quotient_ring(parameter.ideal(t))

    spec = SpecFunctor(parameter)
    parameter_scheme = Spec(parameter, base_ring=parameter)
    family = spec(family_algebra)
    zero = spec(residue_algebra)

    assert parameter_scheme is Schemes(parameter).base_scheme()
    assert family.base_scheme() is parameter_scheme
    assert zero.base_scheme() is parameter_scheme

    special_fiber = FiberProduct(
        family.structure_morphism(),
        zero.structure_morphism(),
    )
    to_family, to_zero = special_fiber.fiber_product_projections()

    assert special_fiber in Schemes(parameter)
    assert special_fiber.fiber_product_base() is parameter_scheme
    assert to_family.domain() is special_fiber
    assert to_family.codomain() is family
    assert to_zero.domain() is special_fiber
    assert to_zero.codomain() is zero

    special_algebra = special_fiber.coordinate_algebra()
    x0 = special_algebra.algebra_generator("x")
    y0 = special_algebra.algebra_generator("y")
    assert special_algebra.base_ring() is parameter
    assert x0 * y0 == special_algebra.zero()

    left_square = family.structure_morphism() * to_family
    right_square = zero.structure_morphism() * to_zero
    assert left_square == right_square
    assert left_square.coordinate_algebra_morphism()(t) == special_algebra.zero()
    assert right_square.coordinate_algebra_morphism()(t) == special_algebra.zero()

    induced_identity = special_fiber.from_pullback_cone(to_family, to_zero)
    assert induced_identity == special_fiber.categorical_identity_morphism()


def test_xy_zero_fiber_has_represented_singular_closed_subscheme() -> None:
    from dzack_research.preamble.all import FinitelyPresentedAlgebra, PolynomialRing

    presentation = PolynomialRing(QQ, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    special_algebra = FinitelyPresentedAlgebra(presentation, (x * y,))
    special_fiber = Spec(special_algebra, base_ring=QQ)
    x0 = special_algebra.algebra_generator("x")
    y0 = special_algebra.algebra_generator("y")

    singular = special_fiber.singular_subscheme()

    assert singular.ambient_scheme() is special_fiber
    assert singular.defining_ideal_owned() == special_algebra.ideal(x0, y0)
    assert tuple(singular.defining_equations()) == (y0, x0)
    assert singular.coordinate_algebra().krull_dimension() == 0
    assert special_fiber.relative_differentials().fitting_ideal(1) == (
        special_algebra.ideal(x0, y0)
    )


def test_xy_equals_t_family_is_flat_with_relative_nonsmooth_node() -> None:
    from dzack_research.preamble.categories.algebras.free_algebras import (
        FinitelyPresentedAlgebra,
        PolynomialRing,
    )
    from pytest import raises

    parameter = PolynomialRing(QQ, "t")
    t = parameter.algebra_generator("t")
    presentation = PolynomialRing(parameter, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family_algebra = FinitelyPresentedAlgebra(presentation, (x * y - t,))
    family = Spec(family_algebra, base_ring=parameter)
    xbar = family_algebra.algebra_generator("x")
    ybar = family_algebra.algebra_generator("y")

    assert family.is_flat()
    nonsmooth = family.relative_nonsmooth_subscheme()
    assert nonsmooth.ambient_scheme() is family
    assert nonsmooth.defining_ideal_owned() == family_algebra.ideal(xbar, ybar)
    assert family.relative_differentials().fitting_ideal(1) == family_algebra.ideal(
        xbar,
        ybar,
    )
    nonsmooth_algebra = nonsmooth.coordinate_algebra()
    assert nonsmooth_algebra.algebra_structure_morphism()(t) == nonsmooth_algebra.zero()

    killed_presentation = PolynomialRing(parameter, ("z", "w"))
    nonflat_algebra = FinitelyPresentedAlgebra(killed_presentation, (t,))
    nonflat = Spec(nonflat_algebra, base_ring=parameter)
    assert not nonflat.is_flat()
    with raises(NotImplementedError, match="requires represented flatness"):
        nonflat.relative_nonsmooth_subscheme()
