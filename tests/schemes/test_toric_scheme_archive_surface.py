r"""Reconcile the archived toric-scheme wrapper with the live owned fan surface.

The archive mixed genuine toric data with backend exposure and coordinate-pattern
classification.  The live owner keeps the mathematical data -- fan, dimension,
optional polarizing polytope, ordinary closed subschemes and standard toric
identifications -- while the native engine remains private and identifications
are decided by fan isomorphism.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    LatticePolygons,
    RationalPolyhedralFans,
    Schemes,
    ToricSchemes,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/toric/toric_schemes.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/toric/toric_schemes.py",
    "disposition": "reconciled-live-owner",
}


def test_fan_defined_toric_scheme_retains_its_mathematical_data() -> None:
    fans = RationalPolyhedralFans(ZZ.free_module(2))
    fan = fans.projective_space_fan()
    plane = fan.toric_variety(QQ)

    assert plane in ToricSchemes(QQ)
    assert plane.fan() is fan
    assert plane.dimension() == 2
    assert plane.is_projective_space()
    assert plane.is_weighted_projective_space((1, 1, 1))


def test_polytope_construction_retains_the_selected_polarization() -> None:
    lattice = ZZ.free_module(2)
    triangle = LatticePolygons(lattice)(((0, 0), (1, 0), (0, 1)))
    plane = triangle.toric_variety(QQ)

    assert plane in ToricSchemes(QQ)
    assert plane.is_polarized()
    assert plane.polarizing_polytope() is triangle
    assert plane.is_projective_space()


def test_general_equation_defined_subscheme_is_not_promoted_to_toric() -> None:
    fans = RationalPolyhedralFans(ZZ.free_module(2))
    plane = fans.projective_space_fan().toric_variety(QQ)
    chart = plane.affine_chart(plane.fan().maximal_cones()[0])
    algebra = chart.coordinate_algebra()
    first, second = tuple(algebra.algebra_generating_set())
    hypersurface = chart.closed_subscheme(
        algebra.algebra_generator(first) + algebra.algebra_generator(second)
    )

    assert hypersurface in Schemes(QQ)
    assert hypersurface not in ToricSchemes(QQ)
