from dzack_research.preamble.all import (
    ConvexPolygon,
    ConvexPolygons,
    ConvexPolytopes,
    LatticePolygon,
    LatticePolygons,
    LatticePolytopes,
    QQ,
)


def test_lattice_polygon_carries_exact_lattice_point_and_volume_data() -> None:
    polygon = LatticePolygon(((0, 0), (0, 3), (6, 0)))
    assert polygon in ConvexPolytopes()
    assert polygon in ConvexPolygons()
    assert polygon in LatticePolytopes()
    assert polygon in LatticePolygons()
    assert polygon.dimension() == 2
    assert polygon.volume() == 9
    assert polygon.normalized_volume() == 18
    assert polygon.n_integral_points() == 16
    assert polygon.n_interior_points() == 4
    assert polygon.n_boundary_points() == 12
    assert polygon.contains_point((1, 1))
    assert polygon.interior_contains_point((1, 1))
    assert not polygon.interior_contains_point((0, 1))


def test_rational_polygon_is_not_silently_called_a_lattice_polytope() -> None:
    polygon = ConvexPolygon(((0, 0), (0, QQ(3) / 2), (3, 0)))
    assert polygon in ConvexPolygons()
    assert polygon not in LatticePolytopes()
    assert polygon.volume() == QQ(9) / 4


def test_ehrhart_polynomial_and_h_star_are_computed_without_latte() -> None:
    square = LatticePolygon(((-1, -1), (-1, 1), (1, 1), (1, -1)))
    polynomial = square.ehrhart_polynomial()
    t = polynomial.parent().algebra_generator("t")
    assert polynomial == 4 * t**2 + 4 * t + 1
    assert square.h_star_vector() == (1, 6, 1)
    assert square.is_reflexive()
    polar = square.polar_dual()
    assert polar in LatticePolygons()
    assert polar.polar_dual().vertices() == square.vertices()
