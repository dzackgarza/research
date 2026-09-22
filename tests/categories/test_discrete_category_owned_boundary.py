r"""Discrete categories remain in the owned category graph under real consumers."""

from dzack_research.preamble.categories.abstract_categories.functors import (
    DiscreteCategories,
    DiscreteCategory,
    ObjectSetFunctor,
)
from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_discrete_category_family_is_owned_and_retains_a_nonidentity_functor() -> None:
    source_points = finite_ordered_set((0, 1))
    target_points = finite_ordered_set(("a", "b"))
    source = DiscreteCategory(source_points)
    target = DiscreteCategory(target_points)

    assert isinstance(DiscreteCategories(), OwnedCategory)
    assert source in DiscreteCategories()
    assert target in DiscreteCategories()
    assert source in Cat()
    assert source(0) in source
    assert source(0) not in Cat()

    functor = Cat().Mor(source, target).from_object_map(
        lambda value: "b" if value == 0 else "a",
    )
    assert functor(source(0)) is target("b")
    assert functor(source(1)) is target("a")

    source_identity = source.identity(source(0))
    target_identity = functor(source_identity)
    assert target_identity == target.identity(target("b"))


def test_object_set_functor_consumes_the_same_owned_discrete_category() -> None:
    points = finite_ordered_set((0, 1, 2))
    category = DiscreteCategory(points)
    object_set = ObjectSetFunctor()

    assert object_set(category) is points


def test_discrete_functor_endpoints_retain_placement_and_the_object_map() -> None:
    """The object-set functor applies to Cat arrows as well as raw categories."""
    source_points = finite_ordered_set((0, 1))
    target_points = finite_ordered_set(("a", "b"))
    source = DiscreteCategory(source_points)
    target = DiscreteCategory(target_points)
    functor = Cat().Mor(source, target).from_object_map(
        lambda value: "b" if value == 0 else "a",
    )
    arrow = Cat().arrow(functor)
    object_set = ObjectSetFunctor()

    assert arrow.domain() is Cat().object(source)
    assert arrow.codomain() is Cat().object(target)
    assert arrow.domain().category() is DiscreteCategories()
    assert arrow.codomain().category() is DiscreteCategories()
    assert arrow.domain() in DiscreteCategories()
    assert arrow.codomain() in DiscreteCategories()
    assert object_set(arrow.domain()) is source_points
    assert object_set(arrow.codomain()) is target_points

    image = object_set(arrow)
    assert image.domain() is source_points
    assert image.codomain() is target_points
    assert image(source_points(0)) == target_points("b")
    assert image(source_points(1)) == target_points("a")


def test_category_endpoints_do_not_infer_discreteness_or_set_enrichment() -> None:
    from dzack_research.preamble.categories.abstract_categories.products import (
        FiniteOrdinalCategory,
    )
    from dzack_research.preamble.categories.sets.set_categories import Sets

    walking_arrow = Cat().object(FiniteOrdinalCategory(2))
    assert walking_arrow in Cat()
    assert walking_arrow not in DiscreteCategories()

    points = finite_ordered_set((0, 1))
    set_mor = Sets().Mor(points, points)
    endpoint = Cat().object(set_mor)
    assert endpoint.represented_category() is set_mor
    assert endpoint in Cat()
    assert endpoint not in Sets()
