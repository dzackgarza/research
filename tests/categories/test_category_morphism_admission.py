r"""Unverified specimens distinguishing arrow admission from object placement.

``Cat().Mor(C, D)`` is the category of functors and natural transformations,
not the parent of the arrows of ``Cat``. These constructions must accept the
actual functor arrows without making them placed functor objects implicitly.
"""

import pytest

from dzack_research.preamble.categories.abstract_categories.cat import (
    Cat,
    CategoryFunctorMorphism,
)
from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
from dzack_research.preamble.categories.functors.core import IdentityFunctor, NaturalTransformation
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


@pytest.fixture
def discrete_arrow() -> CategoryFunctorMorphism:
    source = DiscreteCategory(finite_ordered_set((0, 1)))
    target = DiscreteCategory(finite_ordered_set(("a", "b")))
    functor = Cat().Mor(source, target).from_object_map(
        lambda point: "b" if point == 0 else "a",
    )
    return Cat().arrow(functor)


def test_a_functor_arrow_is_admitted_without_becoming_a_functor_object(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    functors = Cat().Mor(arrow.domain(), arrow.codomain())
    assert arrow not in functors
    stated = functors.object(arrow)
    assert stated in functors
    assert stated.arrow() is arrow
    assert IdentityFunctor(Cat())(arrow) is arrow
    assert arrow not in functors

    with pytest.raises(ValueError, match="wrong functor-category endpoints"):
        Cat().Mor(arrow.codomain(), arrow.domain()).object(arrow)


def test_products_admit_functor_components_and_reject_wrong_endpoints(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    product = Cat().product((Cat(), Cat()))
    source = product(arrow.domain(), arrow.domain())
    target = product(arrow.codomain(), arrow.codomain())
    maps = product.Mor(source, target)
    pair = maps(arrow, arrow)
    assert pair.first() is arrow
    assert pair.second() is arrow
    assert pair * product.identity(source) == pair
    assert product.identity(target) * pair == pair

    with pytest.raises(ValueError, match="first map"):
        maps(Cat().identity(arrow.domain()), arrow)


def test_opposites_admit_functor_arrows_with_reversed_endpoints(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    opposite = Cat().opposite()
    source = opposite(arrow.codomain())
    target = opposite(arrow.domain())
    maps = opposite.Mor(source, target)
    reversed_arrow = maps(arrow)
    assert reversed_arrow.domain() is source
    assert reversed_arrow.codomain() is target
    assert reversed_arrow.underlying_arrow() is arrow
    assert (reversed_arrow * opposite.identity(source)).underlying_arrow() == arrow

    with pytest.raises(ValueError, match="reversed arrow"):
        maps(Cat().identity(arrow.domain()))


def test_a_square_in_cat_retains_its_actual_functor_edges(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    arrows = Cat().ArrowCategory()
    stated = arrows(arrow)
    square = arrows.Mor(stated, stated).identity()
    assert square.left() is Cat().identity(arrow.domain())
    assert square.right() is Cat().identity(arrow.codomain())
    assert square * square == square


def test_presented_images_in_cat_retain_functor_arrows_and_identities(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    images = IdentityFunctor(Cat()).Image()
    source = images(arrow.domain())
    target = images(arrow.codomain())
    maps = images.Mor(source, target)
    represented = maps(arrow)
    assert represented.underlying_arrow() is arrow
    assert images.inclusion()(represented) is arrow
    identity = images.identity(source)
    assert identity.underlying_arrow() is Cat().identity(arrow.domain())
    assert (represented * identity).underlying_arrow() == arrow

    with pytest.raises(ValueError, match="underlying functor images"):
        maps(Cat().identity(arrow.domain()))


def test_natural_transformation_components_in_cat_are_actual_functor_arrows(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    identity = IdentityFunctor(Cat())
    transformation = NaturalTransformation(identity, identity, Cat().identity)
    component = transformation.component(arrow.domain())
    assert component is Cat().identity(arrow.domain())
    assert transformation.naturality_target_composite(arrow) == arrow
    assert transformation.naturality_source_composite(arrow) == arrow
