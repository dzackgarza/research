r"""Varieties, curves and surfaces as full subcategories cut out by hypotheses.

A variety is integral, separated and of finite type over its base; a curve
and a surface are the varieties of relative dimension one and two.  Each
assertion below fails if one hypothesis is dropped from the criterion.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    Curves,
    Schemes,
    IntegralSchemes,
    Surfaces,
    Varieties,
)


def _plane():
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    algebra = plane.coordinate_ring()
    return plane, algebra.algebra_generator("x"), algebra.algebra_generator("y")




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
    rational_functions = QQ.polynomial_ring("t").fraction_field()
    point = (rational_functions).affine_spectrum(base_ring=QQ)

    assert point in IntegralSchemes(QQ)
    assert point in Schemes(QQ).Separated()
    assert point not in Schemes(QQ).FiniteType()
    assert point not in Varieties(QQ)


def test_relative_dimension_is_read_over_the_stated_base() -> None:
    r"""``A^1_Z`` is a surface over nothing: it is a curve over ``Z``, which is one-dimensional."""
    line = AffineSpaces(ZZ)(1)

    assert line in Varieties(ZZ)
    assert line.relative_dimension() == 1
    assert line in Curves(ZZ)
    assert line not in Surfaces(ZZ)
    # Over Z the coordinate ring Z[x] has Krull dimension two, and the
    # relative dimension subtracts the one dimension of the base.
    assert line.coordinate_ring().krull_dimension() == 2




def test_singular_plane_cubic_keeps_arithmetic_genus_separate_from_geometric_genus() -> None:
    plane = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    coordinate_ring = plane.coordinate_ring()
    x = coordinate_ring.algebra_generator("x")
    y = coordinate_ring.algebra_generator("y")
    z = coordinate_ring.algebra_generator("z")
    cusp = plane.closed_subscheme(y**2 * z - x**3)

    assert cusp in Curves(QQ)
    assert cusp.arithmetic_genus() == 1
    try:
        cusp.geometric_genus()
    except AssertionError as error:
        assert "normalization" in str(error)
    else:
        raise AssertionError(
            "a singular curve must not identify geometric genus with arithmetic genus"
        )
