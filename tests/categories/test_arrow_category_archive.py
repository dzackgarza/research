r"""Archive reconciliation for arrow categories, restricted arrows, and cores."""

from dzack_research.preamble.all import (
    Cat,
    Sets,
)
from dzack_research.preamble.categories.abstract_categories import FiniteOrdinalCategory
from dzack_research.preamble.categories.functors.core import IdentityFunctor

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/abstract_categories/arrow_categories.sage",
    "live_owner": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
    "disposition": "reconciled-live-owner",
}


def test_arrow_category_homs_are_commuting_squares_with_componentwise_composition() -> None:
    points = Sets.Δ[1]
    identity = Sets().Mor(points, points).identity()
    swap = Sets().Mor(points, points)(lambda point: points[1 - int(point)])
    arrows = Sets().ArrowCategory()
    assert arrows is Cat().Mor(FiniteOrdinalCategory(2), Sets())
    arrow_object = arrows(identity)
    hom = arrows.Mor(arrow_object, arrow_object)
    square = hom(swap, swap)
    components = square.components()

    assert components.parent().projection(0)(components) == square.left()
    assert components.parent().projection(1)(components) == square.right()
    assert arrow_object.arrow() is identity
    assert hom is arrows.HomCategory().Of(arrow_object, arrow_object)
    assert square.left() is swap
    assert square.right() is swap
    assert square * square == hom.identity()
    assert hom.identity().left() == identity
    assert hom.identity().right() == identity
    assert arrow_object is Cat().Mor(FiniteOrdinalCategory(2), Sets()).object(identity)
    assert square.component(FiniteOrdinalCategory(2)(0)) is square.left()
    assert square.component(FiniteOrdinalCategory(2)(1)) is square.right()


def test_an_arrow_of_cat_retains_its_category_endpoints() -> None:
    functor = IdentityFunctor(Sets())
    arrow = Cat().arrow(functor)
    arrows = Cat().ArrowCategory()
    represented = arrows(arrow)

    assert represented.arrow() is arrow
    assert represented.source_object() is arrow.domain()
    assert represented.target_object() is arrow.codomain()


def test_archived_arrow_subcategories_retain_their_semantic_predicates() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    one = Sets.Δ[0]
    inclusion = Sets().Mono(two, three)(lambda point: three(int(point)))
    quotient = Sets().Epi(three, one)(lambda _point: one[0])
    swap = Sets().Mor(two, two)(lambda point: two[1 - int(point)])
    isomorphism = Sets().Core().Mor(two, two)(swap, swap)

    assert Cat().join((two.category(), three.category())).is_subcategory(Sets())
    assert Sets().MonomorphismArrowCategory()(inclusion).arrow() is inclusion
    assert Sets().EpimorphismArrowCategory()(quotient).arrow() is quotient
    assert Sets().EndArrowCategory()(swap).arrow() is swap
    assert Sets().IsoArrowCategory()(isomorphism).arrow() is isomorphism
    assert Sets().AutomorphismArrowCategory()(isomorphism).arrow() is isomorphism


def test_archived_wide_subcategory_and_core_keep_actual_allowed_arrows() -> None:
    points = Sets.Δ[1]
    maps = Sets().Mor(points, points)
    swap = maps(lambda point: points[1 - int(point)])
    collapse = maps(lambda _point: points[0])
    injections = Sets().WideSubcategory(Sets().MonomorphismArrowCategory())

    assert injections.admits(swap)
    assert not injections.admits(collapse)
    injection_object = injections.Mor(points, points)(swap)
    assert injection_object.arrow() is swap
    assert injection_object in injections.Mor(points, points)
    assert injections.compose(swap, swap) == injections.identity(points)

    isomorphism = Sets().Core().Mor(points, points)(swap, swap)
    core = Sets().Core()
    assert core.Core() is core
    core_hom = core.Mor(points, points)
    assert isomorphism in core_hom
    converted = core_hom(isomorphism)
    assert converted.parent() is core_hom
    assert converted.forward() is isomorphism.forward()
    assert converted.inverse() is isomorphism.inverse()
    assert converted * core_hom.identity() == converted
    assert core_hom.identity() * converted == converted
