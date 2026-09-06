r"""A product of schemes is asked of the objects, or taken over an index set.

``X.product_with(Y)`` is the operator spelling of the binary case, where one
argument is distinguished; a product whose index set is part of the
mathematics is taken over that set with ``Schemes(R).product(family)``.
Neither reads an arity.
"""

from dzack_research.preamble.all import (
    AffineSpace,
    ProjectiveSpace,
    QQ,
    Schemes,
    ZZ,
)


def test_the_affine_plane_is_the_line_multiplied_by_the_line() -> None:
    line = AffineSpace(1, ZZ)
    plane = line.product_with(line)

    assert plane.relative_dimension() == 2
    assert plane.factors().cardinality() == 2
    assert plane.projection(0).codomain() is line
    assert plane.projection(1).codomain() is line


def test_the_quadric_surface_is_the_projective_line_multiplied_by_itself() -> None:
    line = ProjectiveSpace(1, QQ)
    quadric = line.product_with(line)

    assert quadric.relative_dimension() == 2
    assert quadric.projection(1).codomain() is line


def test_the_category_takes_the_product_over_a_family_of_three_factors() -> None:
    r"""The same word one level up, over the index set rather than an arity."""
    line = AffineSpace(1, QQ)
    space = Schemes(QQ).product((line, line, line))

    assert space.relative_dimension() == 3
