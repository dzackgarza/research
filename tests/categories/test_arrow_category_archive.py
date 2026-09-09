r"""Archived arrow-category contract: arrows are objects and squares are morphisms."""

from dzack_research.preamble.all import ArrowCategory, Sets


def test_arrow_category_homs_are_commuting_squares_with_componentwise_composition() -> None:
    points = Sets.Δ[1]
    identity = Sets().Mor(points, points).identity()
    swap = Sets().Mor(points, points)(lambda point: points[1 - int(point)])
    arrows = ArrowCategory(Sets())
    arrow_object = arrows(identity)
    hom = arrows.Mor(arrow_object, arrow_object)
    square = hom(swap, swap)

    assert arrow_object.arrow() is identity
    assert hom is arrows.HomCategory().Of(arrow_object, arrow_object)
    assert square.left() is swap
    assert square.right() is swap
    assert square * square == hom.identity()
    assert hom.identity().left() == identity
    assert hom.identity().right() == identity
