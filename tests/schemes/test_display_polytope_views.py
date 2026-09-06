r"""The polygon and polytope views.

These check what the picture contains for given data: one mark per lattice
point, one stroked line per decorated side, one vertex sphere per vertex.  The
drawing cores take plain coordinates, so the pictures are checkable without a
session, and the rendered output was inspected by eye when it landed.
"""

from dzack_research.utilities.polytope_views import (
    _polygon_svg_document,
    _polytope_html_document,
)

_A_ONE_TRIANGLE = ((0, 2), (0, 0), (2, 0))
_A_ONE_BOUNDARY = ((0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (1, 1))


def test_the_polygon_picture_marks_every_lattice_point_it_is_given() -> None:
    svg = _polygon_svg_document(
        _A_ONE_TRIANGLE,
        boundary_points=_A_ONE_BOUNDARY,
        interior_points=((1, 1),),
    )

    assert svg.startswith("<svg")
    assert svg.endswith("</svg>")
    assert svg.count('r="4"') == len(_A_ONE_BOUNDARY) + 1


def test_a_decorated_side_is_stroked_and_an_undecorated_polygon_has_no_lines() -> None:
    plain = _polygon_svg_document(_A_ONE_TRIANGLE)
    decorated = _polygon_svg_document(
        _A_ONE_TRIANGLE,
        highlighted_sides=((0, 1), (0, 2)),
    )

    assert plain.count("<line") == 0
    assert decorated.count("<line") == 2


def test_the_distinguished_point_gets_its_own_mark() -> None:
    without = _polygon_svg_document(_A_ONE_TRIANGLE)
    with_point = _polygon_svg_document(_A_ONE_TRIANGLE, distinguished_point=(0, 2))

    assert without.count('r="6.5"') == 0
    assert with_point.count('r="6.5"') == 1


def test_a_half_integral_point_survives_as_an_exact_rational() -> None:
    r"""The affine families place ``p*`` at a half-integral point, so the view
    must not round it to the nearest lattice point."""
    from fractions import Fraction

    svg = _polygon_svg_document(
        ((0, 2), (0, 0), (4, 0), (2, 2)),
        distinguished_point=(Fraction(1, 2), 1),
    )
    shifted = _polygon_svg_document(
        ((0, 2), (0, 0), (4, 0), (2, 2)),
        distinguished_point=(1, 1),
    )

    assert svg.count('r="6.5"') == 1
    assert svg != shifted


def test_the_polytope_page_carries_one_point_per_vertex() -> None:
    vertices = ((0.0, 2.0, 0.0), (0.0, 0.0, 0.0), (2.0, 0.0, 0.0), (0.0, 2.0, 2.0))
    page = _polytope_html_document(vertices, "A1 pyramid")

    assert page.count("new THREE.Vector3(") == len(vertices)
    assert "ConvexGeometry" in page
    assert "<title>A1 pyramid</title>" in page
