r"""Category of categories.

This subtree introduces ``Cat()`` as the singleton category whose objects are
ordinary 1-categories.  It is deliberately small: the immediate goal is to
standardize category-object vocabulary and common boilerplate, not to build a
full subcategory hierarchy for categories.

``Cat()`` is the ambient category at this level.  It is not an object of
itself, and expressions such as ``Cat().Hom(Cat())`` are intentionally outside
this spec: those would be higher-categorical functors.  The Cat-backed wrapper
layer in ``base_category_types.py`` starts one level below this root, for
category objects such as ``Sets()``, ``Rings()``, and their subcategories.

Public surface:

```
Cat()
|-- join(...)
|-- meet(...)
|-- Constructors()
|   |-- EmptyCategory()
|   `-- <registered-category>_<constructor>(...)
|-- Subobjects()
|-- Quotients()
|-- Subquotients()
|-- ObjectsOver()
|-- ObjectsUnder()
|-- CartesianProducts()
|-- JoinCategories()
`-- HomCategory()
    |-- EndCategory()
    `-- AutCategory()
```
"""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, cast, final, override, TypeAlias

from sage.categories.category_singleton import (
    Category_singleton as SageCategorySingleton,
)
from sage.misc.lazy_import import LazyImport
from sage.structure.category_object import CategoryObject as SageCategoryObject

from . import base_category_types as _base_category_types
from .base_category_types import (
    AlgebrasCategory as AlgebrasCategory,
)
from .base_category_types import (
    CartesianProductsCategory as CartesianProductsCategory,
)
from .base_category_types import (
    Category as Category,
)
from .base_category_types import (
    Category_ideal as Category_ideal,
)
from .base_category_types import (
    Category_module as Category_module,
)
from .base_category_types import (
    Category_over_base as Category_over_base,
)
from .base_category_types import (
    Category_over_base_ring as Category_over_base_ring,
)
from .base_category_types import (
    Category_singleton as Category_singleton,
)
from .base_category_types import (
    CategoryWithAxiom as CategoryWithAxiom,
)
from .base_category_types import (
    CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring,
)
from .base_category_types import (
    CategoryWithAxiom_singleton as CategoryWithAxiom_singleton,
)
from .base_category_types import (
    CategoryWithParameters as CategoryWithParameters,
)
from .base_category_types import (
    CovariantConstructionCategory as CovariantConstructionCategory,
)
from .base_category_types import (
    DualObjectsCategory as DualObjectsCategory,
)
from .base_category_types import (
    FilteredModulesCategory as FilteredModulesCategory,
)
from .base_category_types import (
    FunctorialConstructionCategory as FunctorialConstructionCategory,
)
from .base_category_types import (
    GradedModulesCategory as GradedModulesCategory,
)
from .base_category_types import (
    Homsets as Homsets,
)
from .base_category_types import (
    HomsetsCategory as HomsetsCategory,
)
from .base_category_types import (
    HomsetsOf as HomsetsOf,
)
from .base_category_types import (
    IsomorphicObjectsCategory as IsomorphicObjectsCategory,
)
from .base_category_types import (
    QuotientsCategory as QuotientsCategory,
)
from .base_category_types import (
    RealizationsCategory as RealizationsCategory,
)
from .base_category_types import (
    RegressiveCovariantConstructionCategory as RegressiveCovariantConstructionCategory,
)
from .base_category_types import (
    SubobjectsCategory as SubobjectsCategory,
)
from .base_category_types import (
    SubquotientsCategory as SubquotientsCategory,
)
from .base_category_types import (
    SuperModulesCategory as SuperModulesCategory,
)
from .base_category_types import (
    TensorProductsCategory as TensorProductsCategory,
)
from .base_category_types import (
    WithRealizationsCategory as WithRealizationsCategory,
)
from .base_category_types import (
    _SageCategory as _SageCategory,
)
from .base_category_types import (
    register_cat_constructor_class as register_cat_constructor_class,
)

_make_named_class_with_cat_subcategory_methods = _base_category_types._make_named_class_with_cat_subcategory_methods

if TYPE_CHECKING:
    from ..spec_core import ConstructorRegistry
    from ..types import Hom


class _CatObjectMethods:
    r"""Methods on objects of ``Cat()``, i.e. category objects."""

    @abstractmethod
    def Hom(self, codomain: Category) -> Hom:
        r"""Return the functor hom object owned by ``Cat()``."""
        ...

    @final
    def is_join_category(self) -> bool:
        r"""Return whether this category object is a join object in ``Cat()``."""
        from .join_categories import is_join_category

        return bool(is_join_category(self))

    @final
    def leq(self, other: Category) -> bool:
        r"""Return whether ``self`` is a subcategory of ``other``."""
        return bool(cast("Category", self).is_subcategory(other))

    @final
    def geq(self, other: Category) -> bool:
        r"""Return whether ``self`` contains ``other`` as a subcategory."""
        return bool(other.is_subcategory(cast("Category", self)))

    __le__ = leq
    __ge__ = geq


class _CategoryElementMethods:
    r"""Baseline element methods for objects internal to a category object."""


class Cat(SageCategorySingleton):
    r"""Root category whose objects are project category objects.

    Canonical chain: ``Cat()``.

    ``Cat`` deliberately does not use the Cat-backed wrapper bases.  The wrapper
    layer makes ordinary categories into objects of ``Cat()``; applying it to
    ``Cat`` itself would assert a self-membership statement and would turn
    ``Cat().Hom(Cat())`` into an apparent 1-categorical construction.  This spec
    does not model that higher level.

    For the same reason, ``Cat`` does not re-export the object-level
    ``leq``/``geq`` aliases from ``Cat.ParentMethods``.  Ordinary category
    objects may compare as Sage subcategories; the root ``Cat()`` object is not
    specified as an object comparable inside a larger modeled category.
    """

    @override
    @final
    def _make_named_class(
        self,
        name: str,
        method_provider: str,
        cache: bool = False,
        picklable: bool = True,
    ) -> type:
        r"""Use the wrapper-layer universal subcategory-method injection.

        ``Cat`` cannot inherit from the Cat-backed wrapper bases because it is
        not an object of itself.  This override is therefore only a local opt-in
        to the same base-layer Sage integration used by ordinary wrapped
        categories.
        """
        return _make_named_class_with_cat_subcategory_methods(
            self,
            super()._make_named_class,
            name,
            method_provider,
            cache=cache,
            picklable=picklable,
        )

    @override
    @final
    def __contains__(self, candidate: Any) -> bool:
        r"""Return whether ``candidate`` is an object of the category ``Cat()``."""
        from .join_categories import is_join_category

        if candidate is self:
            return False
        if is_join_category(candidate):
            return True
        if isinstance(candidate, SageCategoryObject):
            category = cast("Category", candidate.category())
            return bool(category.is_subcategory(cast("Category", self)))
        return False

    @final
    def join(self, categories: Iterable[Category]) -> Category:
        r"""Return Sage's category-lattice join of ``categories``."""
        return cast("Category", _SageCategory.join(categories))

    @final
    def meet(self, categories: Iterable[Category]) -> Category:
        r"""Return Sage's category-lattice meet of ``categories``.

        Sage intentionally leaves the empty meet unimplemented.  The Cat
        subtree has an explicit bottom object, so the empty meet is the local
        ``EmptyCategory()``.
        """
        categories = tuple(categories)
        if not categories:
            return self.Constructors().EmptyCategory()
        meet_category = cast("Category", _SageCategory.meet(categories))
        if all(meet_category.is_subcategory(category) for category in categories):
            return meet_category
        return self.Constructors().EmptyCategory()

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return the supercategories of the root category ``Cat()``."""
        return []

    @final
    def additional_structure(self) -> None:
        r"""Return Sage's additional-structure marker for ``Cat()``."""
        return None

    class SubcategoryMethods:
        r"""Category-level construction methods supplied by Sage's machinery."""

        @final
        def JoinCategories(self) -> Category:
            r"""Return the subcategory of join objects in ``Cat()``."""
            from .join_categories import JoinCategories

            return JoinCategories()

    ParentMethods : TypeAlias = _CatObjectMethods
    ElementMethods : TypeAlias = _CategoryElementMethods
    Subobjects = LazyImport("category_specs.cat.subcategories.constructions.subobjects", "Subcategories")
    Quotients = LazyImport("category_specs.cat.subcategories.constructions.quotients", "_Quotients")
    Subquotients = LazyImport("category_specs.cat.subcategories.constructions.subquotients", "_Subquotients")
    ObjectsOver = LazyImport("category_specs.cat.subcategories.constructions.objects_over", "SliceCategories")
    ObjectsUnder = LazyImport(
        "category_specs.cat.subcategories.constructions.objects_under",
        "CosliceCategories",
    )
    CartesianProducts = LazyImport(
        "category_specs.cat.subcategories.constructions.cartesian_products",
        "_CartesianProducts",
    )
    HomCategory = LazyImport("category_specs.cat.homsets", "CatHomCategory")
    JoinCategories = LazyImport("category_specs.cat.join_categories", "JoinCategories")
    EmptyCategory = LazyImport("category_specs.cat.empty_category", "EmptyCategory")

    class Constructors:
        r"""Category-object constructor entry points."""

        @final
        def __repr__(self) -> str:
            return "Cat constructors"

        @final
        def EmptyCategory(self) -> Category:
            r"""Return the bottom category object for the local ``Cat()`` hierarchy."""
            from .empty_category import EmptyCategory

            return EmptyCategory()

        @final
        def provenance(self) -> ConstructorRegistry:
            r"""Return typed provenance records for constructors surfaced by ``Cat``."""
            from category_specs.spec_core import cat_constructor_registry

            return cat_constructor_registry()


register_cat_constructor_class(Cat.Constructors, Cat())


from .autsets import CatAutCategory, _CatAutofunctorMethods  # noqa: E402
from .endsets import CatEndCategory, _CatEndofunctorMethods  # noqa: E402
from .homsets import CatHomCategory as CatHomCategory  # noqa: E402
from .homsets import _CatFunctorMethods, _CatHomCategoryObjectMethods  # noqa: E402

CatCategory : TypeAlias = Cat
CatObject : TypeAlias = _CatObjectMethods
CatElement : TypeAlias = _CategoryElementMethods
CatMorphism : TypeAlias = _CatFunctorMethods
CatHom : TypeAlias = _CatHomCategoryObjectMethods
CatEnd : TypeAlias = CatEndCategory.ParentMethods
CatAut : TypeAlias = CatAutCategory.ParentMethods
CatEndomorphism : TypeAlias = _CatEndofunctorMethods
CatAutomorphism : TypeAlias = _CatAutofunctorMethods
