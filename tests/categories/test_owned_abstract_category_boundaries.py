r"""Pure abstract category objects use the owned runtime category boundary."""

from dzack_research.preamble.all import Cat, Sets
from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategories,
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
        "Cat.ParentMethods.IsoArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.AutomorphismArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.MonomorphismArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.EpimorphismArrowCategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.core": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.WideSubcategory": "src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py",
        "Cat.ParentMethods.domain_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.codomain_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.diagonal_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.limit_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.colimit_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.product_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.coproduct_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "Cat.ParentMethods.Limits": "src/dzack_research/preamble/categories/abstract_categories/products.py",
        "Cat.ParentMethods.Colimits": "src/dzack_research/preamble/categories/abstract_categories/products.py",
        "Cat.ParentMethods.Products": "src/dzack_research/preamble/categories/abstract_categories/products.py",
        "Cat.ParentMethods.Coproducts": "src/dzack_research/preamble/categories/abstract_categories/products.py",
        "Cat.ParentMethods.opposite": "src/dzack_research/preamble/categories/abstract_categories/category_constructions.py",
        "Cat.product": "src/dzack_research/preamble/categories/abstract_categories/category_constructions.py",
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
        Sets().Core(),
        Sets().Subobjects(points),
        Sets().WideSubcategory(Sets().MonomorphismArrowCategory()),
        IdentityFunctor(Sets()).algebras(),
        HomCategories(),
        Sets().HomCategory(),
        Sets().Limits(discrete),
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

    assert sets.ArrowCategory() is sets.ArrowCategory()
    assert sets.Core().base_category() is sets
    assert sets.opposite() is sets.opposite()
    product = Cat().product((sets, sets))
    pair = product(points, points)
    assert pair.first() is points
    assert pair.second() is points
    assert tuple(pair) == (points, points)
    assert sets.Subobjects(points) is sets.Subobjects(points)


def test_cat_parent_method_provider_is_plain_and_reuses_the_hom_packet_owner() -> None:
    from dzack_research.preamble.categories.abstract_categories.cat import Cat as CatClass
    from dzack_research.preamble.categories.abstract_categories.hom_foundation import (
        CategoryPacketMethods,
    )

    assert CatClass.ParentMethods.__bases__ == (object,)
    assert CatClass.ParentMethods.HomCategory is CategoryPacketMethods.HomCategory
    assert CatClass.ParentMethods.Mor is CategoryPacketMethods.Mor
    points = finite_ordered_set(("x", "y"))
    homset = Sets().Mor(points, points)
    assert homset.domain() is points
    assert homset.codomain() is points


def test_fresh_public_import_does_not_warn_about_cat_parent_methods() -> None:
    import subprocess
    import sys

    code = r"""
import warnings
warnings.filterwarnings(
    "error",
    message=r"Cat\.ParentMethods should not have a super class",
    category=UserWarning,
)
from dzack_research.preamble.all import Cat, Lattices, ZZ
assert Cat().an_object() is not None
assert Lattices(ZZ).an_object() is not None
"""
    result = subprocess.run(
        [sys.executable, "-c", code],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
