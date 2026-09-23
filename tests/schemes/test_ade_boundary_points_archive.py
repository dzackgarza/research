r"""Archive reconciliation for the distinguished boundary points of an ADE polygon."""

from dzack_research.preamble.all import ADELogPairs, QQ


def test_a_one_distinguished_boundary_points_are_exactly_the_two_blue_edges() -> None:
    pair = ADELogPairs(QQ)("A", 1)
    polygon = pair.polygon()
    points = pair.distinguished_boundary_points()

    assert points.cardinality() == 5
    assert all(point in polygon.boundary_integral_points() for point in points)
    assert all(point.parent() is polygon.ambient_lattice() for point in points)

    expected = {
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 1),
        (2, 0),
    }
    assert {tuple(int(coordinate) for coordinate in point) for point in points} == expected
    assert tuple(int(coordinate) for coordinate in pair.p_star()) in expected


