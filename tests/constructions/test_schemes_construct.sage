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
    spectrum = (ring).affine_spectrum()

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
    assert ((ring).affine_spectrum() in NormalSchemes(ring)) == (name in NORMAL)
    assert ((ring).affine_spectrum() in NormalSchemes(ZZ)) == (name in NORMAL)


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
    assert ((ring.as_algebra_over(base_ring)).affine_spectrum() in SmoothSchemes(base_ring)) == smooth


def test_point_counts_of_a_hypersurface_over_a_finite_field() -> None:
    field = GF(5)
    plane = AffineSpaces(field)(2, names=("x", "y"))
    x = plane.coordinate_ring().algebra_generator("x")
    y = plane.coordinate_ring().algebra_generator("y")
    parabola = plane.closed_subscheme(y - x**2)
    assert parabola.point_count() == 5
    assert parabola.point_count(2) == 25


def test_spec_is_a_contravariant_functor(field) -> None:
    spec = Algebras(field).Associative().Unital().Commutative().spectrum()
    polynomials = field.polynomial_ring("x")
    x = polynomials.algebra_generator("x")
    squaring = polynomials.Mor(polynomials)({"x": x**2})
    morphism = spec(squaring)

    assert spec(polynomials) is (polynomials).affine_spectrum()
    assert morphism.domain() is (polynomials).affine_spectrum()
    assert morphism.codomain() is (polynomials).affine_spectrum()
    assert spec(squaring * squaring) == spec(squaring) * spec(squaring)
    assert spec(polynomials.Mor(polynomials).identity()) == (polynomials).affine_spectrum().Mor((polynomials).affine_spectrum()).identity()


def test_the_stalk_of_the_structure_sheaf_is_the_local_ring() -> None:
    line = AffineSpaces(QQ)(1, names=("x",))
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
        assert (build(name)).affine_spectrum().relative_dimension() == 0
        assert (build(name)).affine_spectrum() in IntegralSchemes(build(name))
    integers = (ZZ).affine_spectrum()
    assert integers.relative_dimension() == 0
    assert integers.underlying_space().generic_point().residue_field() is QQ
    assert (ZZ).affine_spectrum().Mor((QQ).affine_spectrum()).cardinality() == 0
    assert (QQ).affine_spectrum().Mor((ZZ).affine_spectrum()).cardinality() == 1
