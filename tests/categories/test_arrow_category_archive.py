r"""Archive reconciliation for arrow categories, restricted arrows, and cores."""

from dzack_research.preamble.all import (
    ArrowCategory,
    AutomorphismArrowCategory,
    Core,
    EndArrowCategory,
    EpimorphismArrowCategory,
    IsoArrowCategory,
    Isomorphism,
    MonomorphismArrowCategory,
    Sets,
    WideSubcategory,
    common_category,
    set_injection,
    set_surjection,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/abstract_categories/arrow_categories.sage",
    "live_owner": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
    "disposition": "reconciled-live-owner",
}


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


def test_archived_arrow_subcategories_retain_their_semantic_predicates() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    one = Sets.Δ[0]
    inclusion = set_injection(two, three, lambda point: three(int(point)))
    quotient = set_surjection(three, one, lambda _point: one[0])
    swap = Sets().Mor(two, two)(lambda point: two[1 - int(point)])
    isomorphism = Isomorphism(swap, swap)

    assert common_category(two, three).is_subcategory(Sets())
    assert MonomorphismArrowCategory(Sets())(inclusion).arrow() is inclusion
    assert EpimorphismArrowCategory(Sets())(quotient).arrow() is quotient
    assert EndArrowCategory(Sets())(swap).arrow() is swap
    assert IsoArrowCategory(Sets())(isomorphism).arrow() is isomorphism
    assert AutomorphismArrowCategory(Sets())(isomorphism).arrow() is isomorphism


def test_archived_wide_subcategory_and_core_keep_actual_allowed_arrows() -> None:
    points = Sets.Δ[1]
    maps = Sets().Mor(points, points)
    swap = maps(lambda point: points[1 - int(point)])
    collapse = maps(lambda _point: points[0])
    injections = WideSubcategory(Sets(), MonomorphismArrowCategory(Sets()))

    assert injections.admits(swap)
    assert not injections.admits(collapse)
    assert injections.Mor(points, points)(swap) is swap
    assert injections.compose(swap, swap) == injections.identity(points)

    isomorphism = Isomorphism(swap, swap)
    core = Core(Sets())
    assert isomorphism in core.Mor(points, points)
    assert core.Mor(points, points)(isomorphism) == isomorphism
