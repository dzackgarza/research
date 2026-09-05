r"""Scheme constructions a mathematician expects, over every named ring.

Spectra, affine and projective spaces, closed subschemes, products and fiber
products, over every commutative ring in the catalogue, with the dimensions,
point counts and placements the definitions determine.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403


NORMAL = {"ZZ", "QQ", "GF(5)", "ZZ[i]", "ZZ[sqrt-5]", "ZZ[x]", "QQ[x,y]", "QQ[x]", "ZZ_3", "QQ[[t]]"}
NOT_NORMAL = {"QQ[x,y]/(y^2-x^3)", "ZZ/12", "QQ[e]/(e^2)", "QQ[x,y]/(xy)"}


def test_spec_of_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    spectrum = Spec(ring)

    assert spectrum in Schemes(ring)
    assert spectrum in AffineSchemes(ring)
    assert spectrum in Schemes(ZZ)
    assert spectrum.is_affine()
    assert spectrum.coordinate_ring() is ring
    assert spectrum.relative_dimension() == 0
    assert (spectrum in IntegralSchemes(ring)) == (ring in IntegralDomains())
    assert spectrum in SmoothSchemes(ring)


@pytest.mark.parametrize("name", sorted(NORMAL | NOT_NORMAL))
def test_normality_of_spec(build, name) -> None:
    ring = build(name)
    assert (Spec(ring) in NormalSchemes(ring)) == (name in NORMAL)
    assert (Spec(ring) in NormalSchemes(ZZ)) == (name in NORMAL)


@pytest.mark.parametrize(
    "name, base, smooth",
    [
        ("QQ(i)", "QQ", True),
        ("GF(4)", "GF(2)", True),
        ("QQ[x,y]", "QQ", True),
        ("QQ[x,y]/(y^2-x^3)", "QQ", False),
        ("QQ[e]/(e^2)", "QQ", False),
        ("ZZ[i]", "ZZ", False),
        ("ZZ[x]", "ZZ", True),
    ],
)
def test_smoothness_of_spec_over_a_base(build, name, base, smooth) -> None:
    ring = build(name)
    base_ring = GF(2) if base == "GF(2)" else build(base)
    assert (Spec(ring.as_algebra_over(base_ring)) in SmoothSchemes(base_ring)) == smooth


def test_affine_space_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    plane = AffineSpace(2, ring, names=("x", "y"))

    assert plane in AffineSpaces(ring)
    assert plane in AffineSchemes(ring)
    assert plane in SmoothSchemes(ring)
    assert plane in Schemes(ring)
    assert plane.relative_dimension() == 2
    assert plane.coordinate_ring() in CommutativeAlgebras(ring)
    assert plane.coordinate_ring().krull_dimension() == ring.krull_dimension() + 2
    assert (plane in IntegralSchemes(ring)) == (ring in IntegralDomains())
    assert plane.scheme_base_ring() is ring
    assert plane.structure_morphism().codomain() == Spec(ring)


def test_projective_space_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    line = ProjectiveSpace(1, ring)

    assert line in ProjectiveSpaces(ring)
    assert line in ProjectiveSchemes(ring)
    assert line in SmoothSchemes(ring)
    assert line in Schemes(ring)
    assert line.relative_dimension() == 1
    assert line.is_projective()
    assert (line in IntegralSchemes(ring)) == (ring in IntegralDomains())


def test_varieties_over_every_field(field) -> None:
    line = AffineSpace(1, field)
    plane = ProjectiveSpace(2, field)
    assert line in Varieties(field)
    assert line in Curves(field)
    assert ProjectiveSpace(1, field) in Curves(field)
    assert plane in Varieties(field)
    assert plane in Surfaces(field)
    assert AffineSpace(2, field) in Surfaces(field)
    assert line.dimension() == 1
    assert plane.dimension() == 2


def test_closed_subschemes_of_the_affine_plane(commutative_ring) -> None:
    ring = commutative_ring
    plane = AffineSpace(2, ring, names=("x", "y"))
    x = plane.coordinate_ring().algebra_generator("x")
    y = plane.coordinate_ring().algebra_generator("y")
    cusp = plane.closed_subscheme(y**2 - x**3)
    origin = plane.closed_subscheme(x, y)

    assert cusp in ClosedSubschemes(ring)
    assert cusp in Schemes(ring)
    assert cusp.ambient_scheme() is plane
    assert cusp.codimension() == 1
    assert cusp.relative_dimension() == 1
    assert cusp.inclusion().codomain() is plane
    assert cusp not in SmoothSchemes(ring)
    assert origin.codimension() == 2
    assert origin.relative_dimension() == 0
    assert origin.coordinate_ring().Mor(ring).cardinality() == 1


def test_closed_subscheme_over_a_field_is_a_curve(field) -> None:
    plane = AffineSpace(2, field, names=("x", "y"))
    x = plane.coordinate_ring().algebra_generator("x")
    y = plane.coordinate_ring().algebra_generator("y")
    parabola = plane.closed_subscheme(y - x**2)
    assert parabola in Curves(field)
    assert parabola in SmoothSchemes(field)
    assert parabola in IntegralSchemes(field)
    assert parabola.dimension() == 1


def test_products_of_schemes(commutative_ring) -> None:
    ring = commutative_ring
    line = AffineSpace(1, ring)
    projective = ProjectiveSpace(1, ring)
    plane = scheme_product(line, line)
    quadric = scheme_product(projective, projective)
    mixed = line.product(projective)

    assert plane in ProductSchemes(ring)
    assert plane in AffineSchemes(ring)
    assert plane.relative_dimension() == 2
    assert plane.factors().cardinality() == 2
    assert plane.projections().cardinality() == 2
    assert plane.projection(0).codomain() is line
    assert quadric in ProductSchemes(ring)
    assert quadric in ProjectiveSchemes(ring)
    assert quadric.relative_dimension() == 2
    assert mixed.relative_dimension() == 2
    assert mixed not in AffineSchemes(ring)


def test_fiber_products_over_the_base(commutative_ring) -> None:
    ring = commutative_ring
    line = AffineSpace(1, ring)
    square = scheme_fiber_product(line.structure_morphism(), line.structure_morphism())
    assert square in FiberProductSchemes(ring)
    assert square.relative_dimension() == 2
    assert square.left_projection().codomain() is line
    assert square.fiber_product_base() == Spec(ring)


@pytest.mark.parametrize(
    "dimension, size, affine_count, projective_count",
    [(1, 5, 5, 6), (2, 5, 25, 31), (1, 4, 4, 5), (2, 4, 16, 21), (1, 27, 27, 28)],
)
def test_point_counts_over_finite_fields(dimension, size, affine_count, projective_count) -> None:
    field = GF(size)
    assert AffineSpace(dimension, field).point_count() == affine_count
    assert ProjectiveSpace(dimension, field).point_count() == projective_count
    assert AffineSpace(dimension, field).point_count(2) == size ** (2 * dimension)


def test_point_counts_of_a_hypersurface_over_a_finite_field() -> None:
    field = GF(5)
    plane = AffineSpace(2, field, names=("x", "y"))
    x = plane.coordinate_ring().algebra_generator("x")
    y = plane.coordinate_ring().algebra_generator("y")
    parabola = plane.closed_subscheme(y - x**2)
    assert parabola.point_count() == 5
    assert parabola.point_count(2) == 25


def test_spec_is_a_contravariant_functor(field) -> None:
    spec = CommutativeAlgebras(field).spectrum()
    polynomials = PolynomialRing(field, "x")
    x = polynomials.algebra_generator("x")
    squaring = polynomials.Mor(polynomials)({"x": x**2})
    morphism = spec(squaring)

    assert spec(polynomials) is Spec(polynomials)
    assert morphism.domain() is Spec(polynomials)
    assert morphism.codomain() is Spec(polynomials)
    assert spec(squaring * squaring) == spec(squaring) * spec(squaring)
    assert spec(polynomials.Mor(polynomials).identity()) == Spec(polynomials).Mor(Spec(polynomials)).identity()


def test_the_stalk_of_the_structure_sheaf_is_the_local_ring() -> None:
    line = AffineSpace(1, QQ, names=("x",))
    ring = line.coordinate_ring()
    x = ring.algebra_generator("x")
    origin = line.underlying_space()(ring.ideal(x))
    stalk = line.stalk(origin)

    assert stalk in LocalRings()
    assert stalk.residue_field() in Fields()
    assert stalk.residue_field().characteristic() == 0
    assert stalk.krull_dimension() == 1
    assert line.structure_sheaf().global_sections() is ring


def test_spec_of_a_field_is_a_point_and_spec_of_the_integers_is_not(build) -> None:
    for name in ("QQ", "GF(5)", "QQ(i)"):
        assert Spec(build(name)).relative_dimension() == 0
        assert Spec(build(name)) in IntegralSchemes(build(name))
    integers = Spec(ZZ)
    assert integers.relative_dimension() == 0
    assert integers.underlying_space().generic_point().residue_field() is QQ
    assert Spec(ZZ).Mor(Spec(QQ)).cardinality() == 0
    assert Spec(QQ).Mor(Spec(ZZ)).cardinality() == 1
