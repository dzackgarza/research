r"""Products of schemes as categorical products over the stated base.

The two represented regimes are affine factors, where the product is the
spectrum of the coproduct of coordinate algebras, and projective factors,
where it is the multiprojective scheme.  A mixed product is a projective
space over the affine factor's coordinate algebra, and what is missing there
is its two projections, not the object.
"""

import pytest

from dzack_research.preamble.all import (
    AffineSchemes,
    AffineSpace,
    FiniteTypeSchemes,
    IntegralSchemes,
    ProjectiveSchemes,
    ProjectiveSpace,
    QQ,
    SeparatedSchemes,
    Surfaces,
    ZZ,
    scheme_product,
)


def test_the_product_of_two_projective_lines_is_a_projective_surface() -> None:
    line = ProjectiveSpace(1, QQ)
    quadric = scheme_product(line, line)

    assert quadric in ProjectiveSchemes(QQ)
    assert quadric in FiniteTypeSchemes(QQ)
    assert quadric in SeparatedSchemes(QQ)
    assert quadric in IntegralSchemes(QQ)
    assert quadric.relative_dimension() == 2
    assert quadric in Surfaces(QQ)
    assert quadric.projection(0).codomain() is line
    assert quadric.projection(1).codomain() is line
    assert quadric.factors().cardinality() == 2


def test_a_product_of_affine_spaces_is_affine_of_the_summed_dimension() -> None:
    line = AffineSpace(1, ZZ)
    plane = scheme_product(line, line)

    assert plane in AffineSchemes(ZZ)
    assert plane.relative_dimension() == 2
    assert plane.projection(0).codomain() is line
    # Over Z the coordinate ring has one more Krull dimension than the fibre.
    assert plane.coordinate_ring().krull_dimension() == 3


def test_a_mixed_product_names_the_two_projections_it_cannot_represent() -> None:
    affine = AffineSpace(1, QQ)
    projective = ProjectiveSpace(1, QQ)

    with pytest.raises(AssertionError, match="neither projection is represented"):
        scheme_product(affine, projective)
