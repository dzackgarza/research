r"""Archive reconciliation for represented toric schemes.

The archived toric parent stored a fan and an optional presenting polytope.
The live owner is fan-first: every toric variety retains its actual fan and
character/cocharacter lattices, while a variety constructed from a lattice
polytope separately retains that polytope as polarization data.  Thus a bare
fan and a polarizing polytope are not conflated.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    LatticePolygons,
    RationalPolyhedralFans,
    ToricSchemes,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/toric/__init__.py",
    "live_owner": "src/dzack_research/preamble/categories/schemes/toric/__init__.py",
    "owner_overrides": {
        "ToricScheme": "src/dzack_research/preamble/categories/schemes/toric/toric_schemes.py",
        "ToricSchemes": "src/dzack_research/preamble/categories/schemes/toric/toric_schemes.py",
    },
    "disposition": "reconciled-live-owner",
}


def _plane_fans():
    return RationalPolyhedralFans(ZZ.free_module(2))


def test_archived_fan_datum_is_the_live_toric_variety_owner() -> None:
    fan = _plane_fans().projective_space_fan()
    variety = fan.toric_variety(QQ)

    assert variety in ToricSchemes(QQ)
    assert variety.is_toric()
    assert variety.fan() is fan
    assert variety.cocharacter_lattice() is fan.cocharacter_lattice()
    assert variety.character_lattice() is fan.character_lattice()
    assert variety.dimension() == 2
    assert variety.is_projective_space()
    assert not variety.is_polarized()


def test_archived_optional_polytope_is_retained_as_actual_polarization_data() -> None:
    lattice = ZZ.free_module(2)
    triangle = LatticePolygons(lattice)(((0, 0), (1, 0), (0, 1)))
    variety = triangle.toric_variety(QQ)

    assert variety in ToricSchemes(QQ)
    assert variety.is_projective_space()
    assert variety.is_polarized()
    assert variety.polarizing_polytope() is triangle
    assert variety.fan().is_isomorphic(triangle.normal_fan())


def test_bare_fan_and_polarized_construction_remain_distinct_data() -> None:
    fan = _plane_fans().projective_space_fan()
    bare = fan.toric_variety(QQ)
    lattice = ZZ.free_module(2)
    triangle = LatticePolygons(lattice)(((0, 0), (1, 0), (0, 1)))
    polarized = triangle.toric_variety(QQ)

    assert bare.fan().is_isomorphic(polarized.fan())
    assert bare.is_projective_space()
    assert polarized.is_projective_space()
    assert not bare.is_polarized()
    assert polarized.is_polarized()
