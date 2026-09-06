r"""Varieties, curves and surfaces as full subcategories cut out by hypotheses.

A variety is integral, separated and of finite type over its base; a curve
and a surface are the varieties of relative dimension one and two.  Each
assertion below fails if one hypothesis is dropped from the criterion.
"""

from dzack_research.preamble.all import (
    AffineSpace,
    Curves,
    FiniteTypeSchemes,
    IntegralSchemes,
    PolynomialRing,
    ProjectiveSpace,
    QQ,
    SeparatedSchemes,
    Spec,
    Surfaces,
    Varieties,
    ZZ,
    scheme_product,
)


def _plane():
    plane = AffineSpace(2, QQ, names=("x", "y"))
    algebra = plane.coordinate_ring()
    return plane, algebra.algebra_generator("x"), algebra.algebra_generator("y")


def test_the_affine_plane_is_a_surface_and_the_lines_are_curves() -> None:
    line = AffineSpace(1, QQ)
    plane, _x, _y = _plane()
    projective_line = ProjectiveSpace(1, QQ)
    projective_plane = ProjectiveSpace(2, QQ)

    assert line in Varieties(QQ)
    assert line in Curves(QQ)
    assert line not in Surfaces(QQ)
    assert plane in Varieties(QQ)
    assert plane in Surfaces(QQ)
    assert plane not in Curves(QQ)
    assert projective_line in Curves(QQ)
    assert projective_plane in Surfaces(QQ)
    assert scheme_product(projective_line, projective_line) in Surfaces(QQ)

    # The three hypotheses are each of them separately necessary.
    assert line in IntegralSchemes(QQ)
    assert line in SeparatedSchemes(QQ)
    assert line in FiniteTypeSchemes(QQ)


def test_the_integrality_hypothesis_excludes_a_reducible_subscheme() -> None:
    plane, x, y = _plane()
    two_lines = plane.closed_subscheme(x * y)
    parabola = plane.closed_subscheme(y - x**2)

    assert parabola in Varieties(QQ)
    assert parabola in Curves(QQ)
    assert parabola.relative_dimension() == 1
    # x*y = 0 is a union of two lines: one-dimensional, but not integral.
    assert two_lines.relative_dimension() == 1
    assert two_lines not in IntegralSchemes(QQ)
    assert two_lines not in Varieties(QQ)
    assert two_lines not in Curves(QQ)


def test_the_finite_type_hypothesis_excludes_the_spectrum_of_a_function_field() -> None:
    rational_functions = PolynomialRing(QQ, "t").fraction_field()
    point = Spec(rational_functions, base_ring=QQ)

    assert point in IntegralSchemes(QQ)
    assert point in SeparatedSchemes(QQ)
    assert point not in FiniteTypeSchemes(QQ)
    assert point not in Varieties(QQ)


def test_relative_dimension_is_read_over_the_stated_base() -> None:
    r"""``A^1_Z`` is a surface over nothing: it is a curve over ``Z``, which is one-dimensional."""
    line = AffineSpace(1, ZZ)

    assert line in Varieties(ZZ)
    assert line.relative_dimension() == 1
    assert line in Curves(ZZ)
    assert line not in Surfaces(ZZ)
    # Over Z the coordinate ring Z[x] has Krull dimension two, and the
    # relative dimension subtracts the one dimension of the base.
    assert line.coordinate_ring().krull_dimension() == 2
