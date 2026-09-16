r"""Products of schemes as categorical products over the stated base.

Affine factors use coproducts of coordinate algebras, projective factors use
the multiprojective realization, and finite mixed affine/projective families
are glued from products of standard affine charts.  Every represented route
retains the same factor family and its actual projections.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    AffineSchemes,
    Schemes,
    IntegralSchemes,
    NormalSchemes,
    ProductSchemes,
    ProjectiveSchemes,
    SmoothSchemes,
    Surfaces,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_blowups_and_non_toric_families.sage",
    "live_owner": "tests/schemes/test_scheme_products_over_a_base.py",
    "disposition": "reconciled-live-owner",
}


def test_the_product_of_two_projective_lines_is_a_projective_surface() -> None:
    line = ProjectiveSpaces(QQ)(1)
    quadric = line.scheme_category().product((line, line))

    assert quadric in ProjectiveSchemes(QQ)
    assert quadric in Schemes(QQ).FiniteType()
    assert quadric in Schemes(QQ).Separated()
    assert quadric in IntegralSchemes(QQ)
    assert quadric.relative_dimension() == 2
    assert quadric in Surfaces(QQ)
    assert quadric.projection(0).codomain() is line
    assert quadric.projection(1).codomain() is line
    assert quadric.factors().cardinality() == 2


def test_a_product_of_affine_spaces_is_affine_of_the_summed_dimension() -> None:
    line = AffineSpaces(ZZ)(1)
    plane = line.scheme_category().product((line, line))

    assert plane in AffineSchemes(ZZ)
    assert plane in Schemes(ZZ).QuasiAffine()
    assert plane in Schemes(ZZ).QuasiProjective()
    assert plane.relative_dimension() == 2
    assert plane.projection(0).codomain() is line
    # Over Z the coordinate ring has one more Krull dimension than the fibre.
    assert plane.coordinate_ring().krull_dimension() == 3


def test_a_mixed_affine_projective_product_retains_projections_and_exact_properties() -> None:
    affine = AffineSpaces(QQ)(1)
    projective = ProjectiveSpaces(QQ)(1)

    product = affine.scheme_category().product((affine, projective))

    assert product.relative_dimension() == 2
    assert product.projection(0).codomain() is affine
    assert product.projection(1).codomain() is projective
    assert product in Schemes(QQ).Separated()
    assert product in Schemes(QQ).FiniteType()
    assert product in SmoothSchemes(QQ)
    assert product in Schemes(QQ).QuasiProjective()
    assert product in IntegralSchemes(QQ)
    assert product in NormalSchemes(QQ)
    assert product not in AffineSchemes(QQ)


def test_terminal_affine_factor_retains_the_selected_product_without_algebra_framing() -> None:
    line = AffineSpaces(QQ)(1)
    base = (QQ).affine_spectrum(base_ring=QQ)
    product = line.scheme_category().product((line, base))

    assert product is not line
    assert product.coordinate_algebra() is line.coordinate_algebra()
    assert tuple(product.factors()) == (line, base)
    assert product.projection(0).codomain() is line
    assert product.projection(1).codomain() is base
    assert product.projection(1) == product.structure_morphism()
    assert (
        product.projection(0).coordinate_algebra_morphism()
        == line.coordinate_algebra().Mor(line.coordinate_algebra()).identity()
    )

    cone = product.from_product_cone(
        (line.categorical_identity_morphism(), line.structure_morphism())
    )
    assert product.projection(0) * cone == line.categorical_identity_morphism()
    assert product.projection(1) * cone == line.structure_morphism()


def test_projective_line_diagonal_uses_the_projective_product_cone() -> None:
    line = ProjectiveSpaces(QQ)(1)

    diagonal = line.diagonal_morphism()
    product = diagonal.codomain()

    assert product in ProductSchemes(QQ)
    assert product in ProjectiveSchemes(QQ)
    assert diagonal.domain() is line
    assert product.projection(0) * diagonal == line.categorical_identity_morphism()
    assert product.projection(1) * diagonal == line.categorical_identity_morphism()


def test_affine_line_times_plane_and_mixed_projective_affine_products_keep_dimensions_and_legs() -> None:
    line = AffineSpaces(QQ)(1)
    affine_plane = AffineSpaces(QQ)(2)
    affine_product = line.scheme_category().product((line, affine_plane))

    assert affine_product in AffineSchemes(QQ)
    assert affine_product.relative_dimension() == 3
    assert affine_product.projection(0).codomain() is line
    assert affine_product.projection(1).codomain() is affine_plane

    projective_line = ProjectiveSpaces(QQ)(1)
    projective_surface = projective_line.scheme_category().product((projective_line, projective_line))
    mixed = projective_surface.scheme_category().product((projective_surface, affine_plane))

    assert mixed.relative_dimension() == 4
    assert mixed.projection(0).codomain() is projective_surface
    assert mixed.projection(1).codomain() is affine_plane
    assert mixed in Schemes(QQ).QuasiProjective()
    assert mixed not in AffineSchemes(QQ)
