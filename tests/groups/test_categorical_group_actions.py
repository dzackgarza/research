r"""The classifying category and its functor along a group homomorphism."""

from dzack_research.preamble.all import Groups
from dzack_research.preamble.categories.group.classifying_categories import ClassifyingFunctor


def test_classifying_category_and_the_quotient_from_c4_to_c2() -> None:
    group = Groups.C(4)
    quotient = Groups.C(2)
    generator = next(iter(group.group_generators()))
    quotient_generator = next(iter(quotient.group_generators()))
    phi = group.Mor(quotient)({generator: quotient_generator})
    category = group.classifying_category()
    point = category.an_object()
    arrows = category.Mor(point, point)
    arrow = arrows(generator)

    assert (arrow * arrow).group_element() == generator * generator
    assert (arrow * arrow).group_element().order() == 2
    assert arrows.identity().group_element() == group.one()
    assert arrow * arrow.inverse() == arrows.identity()
    assert arrows.identity() * arrow == arrow

    functor = ClassifyingFunctor(phi)
    target = quotient.classifying_category()
    target_point = target.an_object()
    assert functor.domain() is category
    assert functor.codomain() is target
    assert functor(point) is target_point
    assert functor(arrow).group_element() == quotient_generator
    assert functor(arrow * arrow) == target.Mor(target_point, target_point).identity()
    assert functor(arrow * arrow) == functor(arrow) * functor(arrow)
    assert functor(arrows.identity()) == target.Mor(target_point, target_point).identity()
