r"""Products of schemes as categorical products over the stated base.

Affine factors use coproducts of coordinate algebras, projective factors use
the multiprojective realization, and finite mixed affine/projective families
are glued from products of standard affine charts.  Every represented route
retains the same factor family and its actual projections.
"""

from dzack_research.preamble.all import (
    AffineSchemes,
    AffineSpace,
    FiniteTypeSchemes,
    IntegralSchemes,
    NormalSchemes,
    ProductSchemes,
    ProjectiveSchemes,
    ProjectiveSpace,
    QQ,
    QuasiAffineSchemes,
    QuasiProjectiveSchemes,
    SeparatedSchemes,
    SmoothSchemes,
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
    assert plane in QuasiAffineSchemes(ZZ)
    assert plane in QuasiProjectiveSchemes(ZZ)
    assert plane.relative_dimension() == 2
    assert plane.projection(0).codomain() is line
    # Over Z the coordinate ring has one more Krull dimension than the fibre.
    assert plane.coordinate_ring().krull_dimension() == 3


def test_a_mixed_affine_projective_product_retains_projections_and_exact_properties() -> None:
    affine = AffineSpace(1, QQ)
    projective = ProjectiveSpace(1, QQ)

    product = scheme_product(affine, projective)

    assert product.relative_dimension() == 2
    assert product.projection(0).codomain() is affine
    assert product.projection(1).codomain() is projective
    assert product in SeparatedSchemes(QQ)
    assert product in FiniteTypeSchemes(QQ)
    assert product in SmoothSchemes(QQ)
    assert product in QuasiProjectiveSchemes(QQ)
    assert product in IntegralSchemes(QQ)
    assert product in NormalSchemes(QQ)
    assert product not in AffineSchemes(QQ)


def test_projective_line_diagonal_uses_the_projective_product_cone() -> None:
    line = ProjectiveSpace(1, QQ)

    diagonal = line.diagonal_morphism()
    product = diagonal.codomain()

    assert product in ProductSchemes(QQ)
    assert product in ProjectiveSchemes(QQ)
    assert diagonal.domain() is line
    assert product.projection(0) * diagonal == line.categorical_identity_morphism()
    assert product.projection(1) * diagonal == line.categorical_identity_morphism()
