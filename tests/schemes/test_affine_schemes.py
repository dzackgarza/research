
from dzack_research.preamble.all import (
    QQ,
    Schemes,
)






















def test_affine_fiber_product_is_spec_of_algebra_pushout_with_universal_map() -> None:
    from dzack_research.preamble.all import Algebras

    common = QQ.polynomial_ring("s")
    left_algebra = QQ.polynomial_ring("x")
    right_algebra = QQ.polynomial_ring("y")
    target_algebra = QQ.polynomial_ring("t")
    s = common.algebra_generator("s")
    x = left_algebra.algebra_generator("x")
    y = right_algebra.algebra_generator("y")
    t = target_algebra.algebra_generator("t")

    common_to_left = common.Mor(left_algebra)({"s": x**2})
    common_to_right = common.Mor(right_algebra)({"s": y**3})
    spec = Algebras(QQ).Associative().Unital().Commutative().spectrum()
    left_map = spec(common_to_left)
    right_map = spec(common_to_right)

    pullback = Schemes(QQ).fiber_product(left_map, right_map)
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
    from dzack_research.preamble.all import Algebras

    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    presentation = parameter.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family_algebra = (presentation).quotient_by_relations((x * y - t,))
    residue_algebra = parameter.quotient_ring(parameter.ideal(t))

    spec = Algebras(parameter).Associative().Unital().Commutative().spectrum()
    parameter_scheme = (parameter).affine_spectrum(base_ring=parameter)
    family = spec(family_algebra)
    zero = spec(residue_algebra)

    assert parameter_scheme is Schemes(parameter).base_scheme()
    assert family.base_scheme() is parameter_scheme
    assert zero.base_scheme() is parameter_scheme

    special_fiber = Schemes(parameter).fiber_product(
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

    presentation = QQ.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    special_algebra = (presentation).quotient_by_relations((x * y,))
    special_fiber = (special_algebra).affine_spectrum(base_ring=QQ)
    x0 = special_algebra.algebra_generator("x")
    y0 = special_algebra.algebra_generator("y")

    singular = special_fiber.singular_subscheme()

    assert singular.inclusion().codomain() is special_fiber
    assert singular.defining_ideal_owned() == special_algebra.ideal(x0, y0)
    assert tuple(singular.defining_equations()) == (y0, x0)
    assert singular.coordinate_algebra().krull_dimension() == 0
    assert special_fiber.relative_differentials().fitting_ideal(1) == (
        special_algebra.ideal(x0, y0)
    )


def test_xy_equals_t_family_is_flat_with_relative_nonsmooth_node() -> None:
    from pytest import raises


    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    presentation = parameter.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family_algebra = (presentation).quotient_by_relations((x * y - t,))
    family = (family_algebra).affine_spectrum(base_ring=parameter)
    xbar = family_algebra.algebra_generator("x")
    ybar = family_algebra.algebra_generator("y")

    assert family.is_flat()
    nonsmooth = family.relative_nonsmooth_subscheme()
    assert nonsmooth.inclusion().codomain() is family
    assert nonsmooth.defining_ideal_owned() == family_algebra.ideal(xbar, ybar)
    assert family.relative_differentials().fitting_ideal(1) == family_algebra.ideal(
        xbar,
        ybar,
    )
    nonsmooth_algebra = nonsmooth.coordinate_algebra()
    assert nonsmooth_algebra.algebra_structure_morphism()(t) == nonsmooth_algebra.zero()

    killed_presentation = parameter.polynomial_ring(("z", "w"))
    nonflat_algebra = (killed_presentation).quotient_by_relations((t,))
    nonflat = (nonflat_algebra).affine_spectrum(base_ring=parameter)
    assert not nonflat.is_flat()
    with raises(AssertionError):
        nonflat.relative_nonsmooth_subscheme()


