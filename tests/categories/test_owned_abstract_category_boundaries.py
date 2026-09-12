r"""Pure abstract category objects use the owned runtime category boundary."""

from dzack_research.preamble.all import Cat, Sets
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Core,
    EndofunctorAlgebras,
    MonomorphismArrowCategory,
    SubobjectCategory,
    WideSubcategory,
)
from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategories,
    HomCategoryOf,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    BiproductCategory,
    LimitsOfCategory,
    TensorProductCategory,
)
from dzack_research.preamble.categories.functors.core import IdentityFunctor
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_pure_abstract_category_constructions_are_objects_of_cat() -> None:
    points = finite_ordered_set(("a", "b"))
    discrete = DiscreteCategory(points)
    categories = (
        Core(Sets()),
        SubobjectCategory(Sets(), points),
        WideSubcategory(Sets(), MonomorphismArrowCategory(Sets())),
        EndofunctorAlgebras(IdentityFunctor(Sets())),
        HomCategories(),
        HomCategoryOf(Sets()),
        LimitsOfCategory(discrete, Sets()),
        BiproductCategory((points, points)),
        TensorProductCategory((points, points)),
        Cat().Mor(Sets(), Sets()),
    )

    for category in categories:
        assert category in Cat()
        assert category.category() is Cat()


def test_fixed_homset_keeps_its_enrichment_parent_role() -> None:
    points = finite_ordered_set(("a", "b"))
    homset = Sets().Mor(points, points)

    assert homset in Cat()
    assert homset.category() is not Cat()
    assert homset.domain() is points
    assert homset.codomain() is points
