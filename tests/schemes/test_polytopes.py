from dzack_research.preamble.all import (
    QQ,
    ZZ,
    ConvexPolygons,
    ConvexPolytopes,
    LatticePolygons,
    LatticePolytopes,
    Sets,
)


def test_lattice_polygon_carries_exact_lattice_point_and_volume_data() -> None:
    lattice = ZZ.free_module(2)
    polygon = LatticePolygons(lattice)(((0, 0), (0, 3), (6, 0)))
    assert polygon in ConvexPolytopes(lattice)
    assert polygon in ConvexPolygons(lattice)
    assert polygon in LatticePolytopes(lattice)
    assert polygon in LatticePolygons(lattice)
    assert polygon in Sets().Subobjects(polygon.ambient_space())
    assert polygon.dimension() == 2
    assert polygon.volume() == 9
    assert polygon.normalized_volume() == 18
    assert polygon.n_integral_points() == 16
    assert polygon.n_interior_points() == 4
    assert polygon.n_boundary_points() == 12
    assert all(
        point.parent() is polygon.ambient_lattice()
        for point in polygon.integral_points()
    )
    assert polygon.contains_point((1, 1))
    assert polygon.interior_contains_point((1, 1))
    assert not polygon.interior_contains_point((0, 1))


def test_rational_polygon_is_not_silently_called_a_lattice_polytope() -> None:
    lattice = ZZ.free_module(2)
    polygon = ConvexPolygons(lattice)(((0, 0), (0, QQ(3) / 2), (3, 0)))
    assert polygon in ConvexPolygons(lattice)
    assert polygon not in LatticePolytopes(lattice)
    assert polygon.volume() == QQ(9) / 4


def test_ehrhart_polynomial_and_h_star_are_computed_without_latte() -> None:
    lattice = ZZ.free_module(2)
    square = LatticePolygons(lattice)(((-1, -1), (-1, 1), (1, 1), (1, -1)))
    polynomial = square.ehrhart_polynomial()
    t = polynomial.parent().algebra_generator("t")
    assert polynomial == 4 * t**2 + 4 * t + 1
    _values = square.h_star_vector()
    assert _values.cardinality() == 3
    assert _values[0] == 1
    assert _values[1] == 6
    assert _values[2] == 1
    assert square.is_reflexive()
    polar = square.polar_dual()
    assert polar in LatticePolygons(polar.ambient_lattice())
    assert tuple(point.to_tuple() for point in polar.polar_dual().vertices()) == tuple(
        point.to_tuple() for point in square.vertices()
    )


def test_polygon_svg_is_a_view_of_the_live_exact_polygon() -> None:
    lattice = ZZ.free_module(2)
    triangle = LatticePolygons(lattice)(((0, 0), (2, 0), (0, 1)))
    svg = triangle._repr_svg_()

    assert svg.startswith('<svg xmlns="http://www.w3.org/2000/svg"')
    assert '<polygon points="' in svg
    assert 'fill="none"' in svg
    assert 'stroke="currentColor"' in svg
    assert triangle.vertices() == LatticePolygons(lattice)(((0, 0), (2, 0), (0, 1))).vertices()


def test_three_dimensional_polytope_delegates_to_sages_local_threejs_view() -> None:
    lattice = ZZ.free_module(3)
    tetrahedron = ConvexPolytopes(lattice).an_object()
    html = tetrahedron.threejs_html()

    assert "threejs" in html.lower() or "THREE" in html
    assert tetrahedron.dimension() == 3


def test_dodecahedron_schlafli_symbol_has_h3_full_reflection_symmetry() -> None:
    from dzack_research.preamble.categories.sets.set_categories import PartiallyOrderedSets

    dodecahedron = RegularPolytopes().from_schlafli_symbol("{5,3}")
    diagram = dodecahedron.symmetry_coxeter_diagram()

    assert dodecahedron in PartiallyOrderedSets()
    assert tuple(dodecahedron.schlafli_symbol()) == (5, 3)
    assert dodecahedron.dimension() == 3
    assert diagram.coxeter_matrix()[0, 1] == 5
    assert diagram.coxeter_matrix()[1, 2] == 3
    assert dodecahedron.symmetry_group().order() == 120
