r"""Pure abstract category objects use the owned runtime category boundary."""

from dzack_research.preamble.all import Cat, Sets
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    ArrowCategory,
    Core,
    EndofunctorAlgebras,
    MonomorphismArrowCategory,
    SubobjectCategory,
    WideSubcategory,
)
from dzack_research.preamble.categories.abstract_categories.category_constructions import (
    OppositeCategory,
    ProductCategory,
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

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/abstract_categories/cat.sage",
    "live_owner": "src/dzack_research/preamble/categories/abstract_categories/cat.py",
    "owner_overrides": {
        "Cat.ParentMethods.HomCategory": "src/dzack_research/preamble/categories/abstract_categories/hom_foundation.py",
        "Cat.ParentMethods.EndCategory": "src/dzack_research/preamble/categories/abstract_categories/hom_foundation.py",
        "Cat.ParentMethods.AutCategory": "src/dzack_research/preamble/categories/abstract_categories/hom_foundation.py",
        "Cat.ParentMethods.IsoCategory": "src/dzack_research/preamble/categories/abstract_categories/hom_foundation.py",
        "Cat.ParentMethods.MonoCategory": "src/dzack_research/preamble/categories/abstract_categories/hom_foundation.py",
        "Cat.ParentMethods.EpiCategory": "src/dzack_research/preamble/categories/abstract_categories/hom_foundation.py",
        "Cat.ParentMethods.ArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.EndArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.IsomorphismArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.AutArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.MonomorphismArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.EpimorphismArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.core": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.WideSubcategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.DomainFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.CodomainFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.DiagonalFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.LimitFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.ColimitFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.ProductFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.CoproductFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.Limits": "src/dzack_research/preamble/categories/abstract_categories/products.py",
        "Cat.ParentMethods.Colimits": "src/dzack_research/preamble/categories/abstract_categories/products.py",
        "Cat.ParentMethods.Products": "src/dzack_research/preamble/categories/abstract_categories/products.py",
        "Cat.ParentMethods.Coproducts": "src/dzack_research/preamble/categories/abstract_categories/products.py",
        "Cat.ParentMethods.OppositeCategory": "src/dzack_research/preamble/categories/abstract_categories/category_constructions.py",
        "Cat.ParentMethods.ProductCategory": "src/dzack_research/preamble/categories/abstract_categories/category_constructions.py",
        "Cat.ParentMethods.ImageOf": "src/dzack_research/preamble/categories/abstract_categories/functor_images.py",
        "Cat.ParentMethods.SliceOver": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.CosliceUnder": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.Subobjects": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.Superobjects": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.CoveringObjects": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.CoveredObjects": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
    },
    "disposition": "reconciled-live-owner",
}


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


def test_archived_category_constructions_use_the_current_singletons() -> None:
    sets = Sets()
    points = finite_ordered_set(("a", "b"))

    assert sets.ArrowCategory() is ArrowCategory(sets)
    assert sets.Core() is Core(sets)
    assert sets.opposite() is OppositeCategory(sets)
    product = ProductCategory(sets, sets)
    pair = product(points, points)
    assert pair.first() is points
    assert pair.second() is points
    assert sets.Subobjects(points) is SubobjectCategory(sets, points)
