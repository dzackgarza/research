r"""Closed subschemes and the categorical operations on affine schemes.

Diagonals, graphs, equalizers, fixed subschemes, inverse images and the
scheme-theoretic image are all closed subschemes with their inclusions, and
each is checked against the morphism identity that defines it.
"""

import pytest

from dzack_research.preamble.all import (
    AffineSchemes,
    AffineSpace,
    ClosedEmbeddings,
    ClosedSubschemes,
    IntegralSchemes,
    NormalSchemes,
    PolynomialRing,
    ProjectiveSpace,
    QQ,
    Schemes,
    SmoothSchemes,
    Spec,
    SpecFunctor,
    ZZ,
    scheme_product,
)


def _plane():
    plane = AffineSpace(2, QQ, names=("x", "y"))
    algebra = plane.coordinate_ring()
    return plane, algebra, algebra.algebra_generator("x"), algebra.algebra_generator("y")


def _cusp_parametrization():
    r"""``t |-> (t^2, t^3)``, whose image is the cuspidal cubic ``y^2 = x^3``."""
    plane, algebra, x, y = _plane()
    line = PolynomialRing(QQ, "t")
    t = line.algebra_generator("t")
    return plane, x, y, line, t, SpecFunctor(QQ)(algebra.Mor(line)({"x": t**2, "y": t**3}))


def test_a_scheme_over_a_ring_is_a_scheme_over_every_scalar_base_of_that_ring() -> None:
    plane, _algebra, _x, _y = _plane()

    assert plane in Schemes(QQ)
    assert plane in Schemes(ZZ)
    assert Schemes(ZZ) in Schemes(QQ).all_super_categories()
    assert plane in AffineSchemes(ZZ)
    assert plane in IntegralSchemes(ZZ)
    assert plane in NormalSchemes(QQ)
    # Smoothness and affine-space structure are stated relative to the base.
    assert plane in SmoothSchemes(QQ)
    assert plane not in SmoothSchemes(ZZ)
    assert Spec(QQ) in Schemes(ZZ)
    assert Spec(QQ) not in SmoothSchemes(ZZ)

    structure = Spec(QQ).structure_morphism()
    to_integers = Schemes(ZZ).Mor(Spec(QQ), Spec(ZZ))
    assert structure.domain() is Spec(QQ)
    assert to_integers.domain() is Spec(QQ)
    assert to_integers.codomain() is Spec(ZZ)


def test_a_closed_subscheme_is_placed_with_its_dimension_and_ideal_sheaf() -> None:
    plane, algebra, x, y = _plane()
    cusp = plane.closed_subscheme(y**2 - x**3)
    origin_on_cusp = cusp.closed_subscheme(cusp.coordinate_algebra().algebra_generator("x"))

    assert cusp in ClosedSubschemes(QQ)
    assert cusp in ClosedSubschemes(ZZ)
    assert cusp in ClosedEmbeddings(plane)
    assert plane not in ClosedSubschemes(QQ)
    assert cusp.relative_dimension() == 1
    assert cusp.dimension() == 1
    assert cusp.codimension() == 1
    assert origin_on_cusp in ClosedSubschemes(QQ)
    assert origin_on_cusp.ambient_scheme() is cusp
    assert origin_on_cusp.relative_dimension() == 0
    assert origin_on_cusp.inclusion().codomain() is cusp
    through_plane = cusp.inclusion() * origin_on_cusp.inclusion()
    assert through_plane.domain() is origin_on_cusp
    assert through_plane.codomain() is plane
    assert through_plane.coordinate_algebra_morphism()(y) ** 2 == through_plane.coordinate_algebra_morphism()(x) ** 3

    ideal_sheaf = cusp.ideal_sheaf()
    open_x = plane.distinguished_open(x)
    local_ideal = ideal_sheaf.sections_on_distinguished_open(open_x)
    generator = ideal_sheaf.global_sections()(y**2 - x**3)
    restricted = ideal_sheaf.restriction_map(plane, open_x)(generator)
    assert local_ideal.base_ring() is open_x.coordinate_algebra()
    assert restricted.underlying_element() == local_ideal.fraction(generator)


def test_projective_closed_subschemes_require_homogeneous_equations() -> None:
    plane = ProjectiveSpace(2, QQ)
    x, y, z = plane.gens()
    conic = plane.closed_subscheme(x * z - y**2)
    assert conic in ClosedSubschemes(QQ)
    assert conic.dimension() == 1
    with pytest.raises(AssertionError):
        plane.closed_subscheme(x * z - y)


def test_the_diagonal_is_a_section_of_both_projections_and_a_closed_subscheme() -> None:
    plane, algebra, x, y = _plane()
    product = scheme_product(plane, plane)
    diagonal = plane.diagonal_morphism()

    assert diagonal.domain() is plane
    assert diagonal.codomain() is product
    assert product.projection(0) * diagonal == plane.categorical_identity_morphism()
    assert product.projection(1) * diagonal == plane.categorical_identity_morphism()

    image = plane.diagonal_subscheme()
    assert image in ClosedEmbeddings(product)
    assert image.codimension() == 2
    assert image.relative_dimension() == 2
    pullback = diagonal.coordinate_algebra_morphism()
    assert all(pullback(equation) == algebra.zero() for equation in image.defining_equations())
    factored = image.corestriction(diagonal)
    assert factored.domain() is plane
    assert factored.codomain() is image
    assert image.inclusion() * factored == diagonal


def test_the_graph_of_the_cusp_parametrization_is_a_curve_in_the_product() -> None:
    plane, x, y, line, t, parametrization = _cusp_parametrization()
    product = scheme_product(line_scheme := parametrization.domain(), plane)
    graph = parametrization.graph_morphism()

    assert graph.domain() is line_scheme
    assert graph.codomain() is product
    assert product.projection(0) * graph == line_scheme.categorical_identity_morphism()
    assert product.projection(1) * graph == parametrization

    image = parametrization.graph_subscheme()
    assert image in ClosedEmbeddings(product)
    assert image.relative_dimension() == 1
    assert image.codimension() == 2
    assert image.inclusion() * image.corestriction(graph) == graph


def test_the_fixed_subscheme_of_an_involution_is_the_equalizer_with_the_identity() -> None:
    plane, algebra, x, y = _plane()
    swap = SpecFunctor(QQ)(algebra.Mor(algebra)({"x": y, "y": x}))
    reflect = SpecFunctor(QQ)(algebra.Mor(algebra)({"x": x, "y": -y}))

    swap_fixed = swap.fixed_subscheme()
    reflect_fixed = reflect.fixed_subscheme()
    assert swap_fixed in ClosedEmbeddings(plane)
    assert swap_fixed.defining_ideal_owned() == algebra.ideal(x - y)
    assert swap_fixed.relative_dimension() == 1
    assert swap * swap_fixed.inclusion() == swap_fixed.inclusion()
    assert reflect_fixed.defining_ideal_owned() == algebra.ideal(y)
    assert reflect * reflect_fixed.inclusion() == reflect_fixed.inclusion()

    equalizer = Schemes(QQ).equalizer(swap, reflect)
    assert equalizer.defining_ideal_owned() == algebra.ideal(x - y, x + y)
    assert equalizer.relative_dimension() == 0
    assert swap * equalizer.inclusion() == reflect * equalizer.inclusion()
    assert equalizer.corestriction(equalizer.inclusion()) == equalizer.categorical_identity_morphism()


def test_the_inverse_image_of_the_origin_under_the_cusp_parametrization_has_length_two() -> None:
    plane, x, y, line, t, parametrization = _cusp_parametrization()
    origin = plane.closed_subscheme(x, y)
    preimage = parametrization.inverse_image(origin)
    line_algebra = parametrization.domain().coordinate_algebra()
    ideal = preimage.defining_ideal_owned()

    assert preimage in ClosedEmbeddings(parametrization.domain())
    assert ideal == line_algebra.ideal(t**2)
    assert preimage.relative_dimension() == 0
    restricted = origin.corestriction(parametrization * preimage.inclusion())
    assert restricted.domain() is preimage
    assert restricted.codomain() is origin
    assert origin.inclusion() * restricted == parametrization * preimage.inclusion()

    cusp = plane.closed_subscheme(y**2 - x**3)
    whole_line = parametrization.inverse_image(cusp)
    assert whole_line.defining_ideal_owned() == line_algebra.ideal(line_algebra.zero())
    assert whole_line.relative_dimension() == 1


def test_the_scheme_theoretic_image_of_the_cusp_parametrization_is_the_cuspidal_cubic() -> None:
    plane, x, y, line, t, parametrization = _cusp_parametrization()
    algebra = plane.coordinate_ring()
    image = parametrization.scheme_theoretic_image()

    assert image in ClosedEmbeddings(plane)
    assert image.defining_ideal_owned() == algebra.ideal(y**2 - x**3)
    assert image.relative_dimension() == 1
    factored = image.corestriction(parametrization)
    assert factored.domain() is parametrization.domain()
    assert factored.codomain() is image
    assert image.inclusion() * factored == parametrization
    # The parametrization is not a closed immersion: its image misses no point
    # but the pullback A/(y^2 - x^3) -> QQ[t] is not surjective (t is not hit).
    assert not parametrization.is_closed_immersion()
    assert image.inclusion().is_closed_immersion()
