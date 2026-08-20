r"""Universal subcategory-method surface for objects of ``Cat()``.

Every ordinary project category is an object of ``Cat()``.  This file is the
single shared source for construction selectors that all such category objects
receive through their ``SubcategoryMethods`` provider.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, final

if TYPE_CHECKING:
    # Repointed on the wholesale move from category_specs: these named type
    # aliases in that tree's ``types`` module. Here Sage's own classes name
    # them, and the Hom/End/Aut trio are all the category of such categories.
    from sage.categories.category import Category
    from sage.structure.category_object import CategoryObject

    CategoryOfHomCategories = Category
    CategoryOfEndCategories = Category
    CategoryOfAutCategories = Category


class UniversalSubcategoryMethods:
    r"""Universal construction selectors for category objects in ``Cat()``.

    Sage mixes ``SubcategoryMethods`` into the dynamic class of category
    instances, not into parents or elements.  Since every ordinary project
    category is an object of ``Cat()``, these methods are the shared categorical
    construction surface for all such objects.

    Individual category classes still declare the construction category class,
    e.g. ``Sets.Subobjects = _Subobjects`` or
    ``Modules.Subobjects = _Subobjects``.  Those classes carry the
    category-specific parent/element/morphism requirements.  The selectors
    here only perform the universal operation already used throughout the
    specs: call ``SomeConstruction.category_of(self)``.
    """

    @final
    def _category_self(self) -> Category:
        return cast("Category", self)
    @final
    def Subobjects(self) -> Category:
        r"""Return the subobject construction category of this category."""
        from .base_category_types import SubobjectsCategory

        return cast(
            "Category",
            SubobjectsCategory.category_of(self._category_self()),
        )

    @final
    def Subsets(self) -> Category:
        """Alias for :meth:`Subobjects`."""
        return self.Subobjects()

    @final
    def Quotients(self) -> Category:
        r"""Return the quotient-object construction category of this category."""
        from .base_category_types import QuotientsCategory

        return cast(
            "Category",
            QuotientsCategory.category_of(self._category_self()),
        )
    @final
    def Subquotients(self) -> Category:
        r"""Return the subquotient construction category of this category."""
        from .base_category_types import SubquotientsCategory

        return cast(
            "Category",
            SubquotientsCategory.category_of(self._category_self()),
        )
    @final
    def ObjectsOver(self, structure_object: CategoryObject) -> Category:
        r"""Return the category of objects over ``structure_object``."""
        from .subcategories.constructions.objects_over import _ObjectsOver

        return cast(
            "Category",
            _ObjectsOver.category_of(self._category_self(), structure_object),
        )
    @final
    def ObjectsUnder(self, structure_object: CategoryObject) -> Category:
        r"""Return the category of objects under ``structure_object``."""
        from .subcategories.constructions.objects_under import _ObjectsUnder

        return cast(
            "Category",
            _ObjectsUnder.category_of(self._category_self(), structure_object),
        )

    @final
    def Slice(self, structure_object: CategoryObject) -> Category:
        """Alias for :meth:`ObjectsOver`."""
        return self.ObjectsOver(structure_object)

    @final
    def Coslice(self, structure_object: CategoryObject) -> Category:
        """Alias for :meth:`ObjectsUnder`."""
        return self.ObjectsUnder(structure_object)
    @final
    def CartesianProducts(self) -> Category:
        r"""Return the Cartesian-product construction category of this category."""
        from .base_category_types import CartesianProductsCategory

        return cast(
            "Category",
            CartesianProductsCategory.category_of(self._category_self()),
        )
    @final
    def HomCategory(self) -> CategoryOfHomCategories:
        r"""Return the hom-category construction over this category."""
        from ..homsets import HomCategoryConstruction

        return cast(
            "CategoryOfHomCategories",
            HomCategoryConstruction.category_of(self._category_self()),
        )
    @final
    def Homsets(self) -> CategoryOfHomCategories:
        r"""Return Sage's homset spelling as an interop alias for ``HomCategory``."""
        return self.HomCategory()
    @final
    def EndCategory(self) -> CategoryOfEndCategories:
        r"""Return the endomorphism-category construction over this category."""
        from ..homsets import HomCategory

        category = self._category_self()
        if category.is_subcategory(HomCategory()):
            return cast("CategoryOfEndCategories", category._with_axiom("Endset"))
        return cast(
            "CategoryOfEndCategories",
            category.HomCategory().EndCategory(),
        )
    @final
    def Endsets(self) -> CategoryOfEndCategories:
        r"""Return Sage's endset spelling as an interop alias for ``EndCategory``."""
        return self.EndCategory()
    @final
    def AutCategory(self) -> CategoryOfAutCategories:
        r"""Return the automorphism-category construction over this category."""
        category = self._category_self()
        if category.is_subcategory(category.EndCategory()):
            return cast("CategoryOfAutCategories", category._with_axiom("Autset"))
        return cast(
            "CategoryOfAutCategories",
            category.EndCategory().AutCategory(),
        )
