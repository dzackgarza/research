r"""Archive reconciliation for convex and lattice polytope objects.

The archived polytope categories owned exact vertices, lattice-point sets,
volume, Ehrhart data and lattice-polar duality.  Those invariants now live on
the current ``ConvexPolytopes``/``LatticePolytopes`` objects themselves; this
file records that mathematical migration without reviving an archive parent.
"""

from dzack_research.preamble.all import (
    ZZ,
    ConvexPolygons,
    ConvexPolytopes,
    LatticePolygons,
    LatticePolytopes,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/polytopes.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/polytopes.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_lattice_polygon_invariants_live_on_the_current_object() -> None:
    lattice = ZZ.free_module(2)
    triangle = LatticePolygons(lattice)(((0, 0), (0, 3), (6, 0)))

    assert triangle in ConvexPolytopes(lattice)
    assert triangle in ConvexPolygons(lattice)
    assert triangle in LatticePolytopes(lattice)
    assert triangle in LatticePolygons(lattice)
    assert triangle.dimension() == 2
    assert triangle.volume() == 9
    assert triangle.normalized_volume() == 18
    assert triangle.n_integral_points() == 16
    assert triangle.n_interior_points() == 4
    assert triangle.n_boundary_points() == 12
    assert triangle.contains_point((1, 1))
    assert triangle.interior_contains_point((1, 1))
    assert not triangle.interior_contains_point((0, 1))


def test_archived_ehrhart_h_star_and_polar_duality_are_live_lattice_operations() -> None:
    lattice = ZZ.free_module(2)
    square = LatticePolygons(lattice)(((-1, -1), (-1, 1), (1, 1), (1, -1)))
    polynomial = square.ehrhart_polynomial()
    t = polynomial.parent().algebra_generator("t")
    h_star = square.h_star_vector()

    assert polynomial == 4 * t**2 + 4 * t + 1
    assert tuple(h_star) == (1, 6, 1)
    assert square.is_reflexive()

    polar = square.polar_dual()
    assert polar in LatticePolygons(polar.ambient_lattice())
    assert polar.is_reflexive()
    assert tuple(point.to_tuple() for point in polar.polar_dual().vertices()) == tuple(
        point.to_tuple() for point in square.vertices()
    )
