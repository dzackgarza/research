r"""Archive reconciliation for the decorated two-dimensional ADE SVG view."""

from dzack_research.preamble.all import ADELogPair, QQ


def test_ade_svg_retains_the_distinguished_point_and_side_decorations() -> None:
    pair = ADELogPair("A", 3, QQ, variant=("long", "short"))
    svg = pair.ade_svg()

    assert pair.polygon_vertex_order().cardinality() == pair.vertices().cardinality()
    assert svg.startswith("<svg")
    assert 'data-role="ade-polygon"' in svg
    assert 'data-ade-type="A3"' in svg
    assert svg.count('data-role="decorated-side"') == 2
    assert 'data-length-class="long"' in svg
    assert 'data-length-class="short"' in svg
    assert 'data-vertex-colour="white"' in svg
    assert 'data-vertex-colour="black"' in svg
    assert 'data-role="p-star"' in svg
    assert 'data-point="0,2"' in svg


def test_ade_svg_marks_the_actual_blue_boundary_points() -> None:
    pair = ADELogPair("A", 1, QQ)
    svg = pair._repr_svg_()

    represented = {
        tuple(int(coordinate) for coordinate in point)
        for point in pair.distinguished_boundary_points()
    }
    assert represented
    assert svg.count('data-role="blue-boundary-point"') == len(represented)
    for x, y in represented:
        assert f'data-lattice-point="{x},{y}"' in svg
