r"""The Kreuzer--Skarke reflexive-polytope classification, as owned polytopes.

There are exactly sixteen reflexive polygons up to lattice equivalence, and
by Batyrev's theorem the toric variety of the normal fan of a reflexive
polytope is Gorenstein Fano; the projective plane is among them.
"""

from dzack_research.preamble.all import (
    LatticePolygons,
    LatticePolytopes,
    QQ,
)


def test_there_are_sixteen_reflexive_polygons() -> None:
    reflexive = LatticePolytopes().reflexive_polytopes(2)

    assert reflexive.cardinality() == 16
    for polygon in reflexive:
        assert polygon in LatticePolygons()
        assert polygon.is_reflexive()
        assert polygon.n_interior_points() == 1


def test_one_reflexive_polygon_has_the_projective_plane_as_its_toric_variety() -> None:
    reflexive = LatticePolytopes().reflexive_polytopes(2)
    varieties = tuple(polygon.toric_variety(QQ) for polygon in reflexive)

    assert any(variety.is_projective_space() for variety in varieties)
    assert any(variety.is_hirzebruch_surface(0) for variety in varieties)
    assert not all(variety.is_projective_space() for variety in varieties)


def test_a_non_reflexive_lattice_polygon_is_not_in_the_classification() -> None:
    r"""The triangle on ``(0,0)``, ``(2,0)``, ``(0,2)`` has no interior lattice
    point at the origin, so it is not reflexive and the predicate is not
    answering true for every lattice polygon."""
    from dzack_research.preamble.all import LatticePolygon

    assert not LatticePolygon(((0, 0), (2, 0), (0, 2))).is_reflexive()
