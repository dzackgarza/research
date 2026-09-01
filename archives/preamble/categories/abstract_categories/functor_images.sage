r"""Images of construction functors as categories over their codomains.

For a construction functor :math:`F:\mathbf A\to\mathbf C`, its image category
has :math:`\mathbf C` as its immediate supercategory.  An object retains its
chosen preimage in :math:`\mathbf A`; its complete implementation otherwise
comes from :math:`\mathbf C` through ``ObjectType``.
"""

from typing import TYPE_CHECKING

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.owned_category_bases import (
    Category as OwnedCategory,
    CategoryWithParameters,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)

if TYPE_CHECKING:
    from typing import TypeIs

    from sage.categories.category import Category
    from sage.structure.element import Element
    from sage.structure.parent import Parent

    from dzack_research.preamble.owned_category import ConstructionData

    type ObjectOfCategory = Parent | Category | Element


class _FunctorImageParameters:
    r"""The functor parameter shared by its image-category hierarchy.

    This is not a category.  Each category below declares its mathematical
    relation through ``super_categories()``.
    """

    def __init__(self, functor: "Element") -> None:
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        assert functor in Cat().ArrowCategory()
        self._functor = functor
        super().__init__()

    def functor(self) -> "Element":
        return self._functor

    def _make_named_class_key(self, name: str) -> "Category":
        return self._functor.codomain()

    @cached_method
    def inclusion(self) -> "Element":
        from dzack_research.preamble.categories.abstract_categories.functors import (
            ImageInclusionFunctor,
        )

        return ImageInclusionFunctor(self)


class FunctorImageCategories(OwnedCategory):
    r"""The subcategory of :math:`\mathbf{Cat}` on functor-image categories."""

    def super_categories(self) -> "list[Category]":
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return [Cat()]

    def __contains__(self, candidate: "ObjectOfCategory") -> bool:
        match candidate:
            case _FunctorImageParameters():
                return True
            case _:
                return False

    def is_image_category(
        self,
        candidate: "ObjectOfCategory",
    ) -> "TypeIs[_FunctorImageParameters]":
        return candidate in self


class ImageOfFunctor(_FunctorImageParameters, CategoryWithParameters):
    r"""The category of outputs carrying a chosen presentation by ``functor``."""

    def super_categories(self) -> "list[Category]":
        return [self._functor.codomain()]

    def _repr_(self) -> str:
        return f"Category of objects in the image of {self._functor}"

    class _HomCategory(HomCategoryConstruction):
        r"""The codomain arrows between represented image objects."""

        def _object_type_of_object_type(self) -> type:
            image = self.base_category()
            return image.functor().codomain().ArrowType

        class ParentMethods:
            def codomain_hom_category(self) -> "Category":
                image = self.base_category()
                return image.functor().codomain().Hom(
                    self.domain(),
                    self.codomain(),
                )

            def __contains__(self, arrow: "Element") -> bool:
                return arrow in self.codomain_hom_category()

            def __call__(self, arrow: "Element") -> "Element":
                assert arrow in self
                return arrow

            def objects(self) -> "Parent":
                codomain = self.base_category().functor().codomain()
                assert codomain.is_locally_discrete(), (
                    "an object set exists here only for a locally discrete codomain"
                )
                return self.codomain_hom_category().objects()

            def identity(self) -> "Element":
                assert self.domain() is self.codomain()
                identity = self.base_category().functor().codomain().identity(
                    self.domain()
                )
                assert identity in self
                return identity

            def compose(self, second: "Element", first: "Element") -> "Element":
                codomain = self.base_category().functor().codomain()
                composite = codomain.compose(second, first)
                assert composite in self
                return composite

    class ParentMethods:
        r"""An output of ``functor`` with its chosen source object."""

        def __init__(
            self,
            preimage: "ObjectOfCategory",
            **rest: "ConstructionData",
        ) -> None:
            self._preimage = preimage
            super().__init__(**rest)
            assert preimage in self.constructing_functor().domain()

        def preimage(self) -> "ObjectOfCategory":
            return self._preimage

        def image_category(self) -> "_FunctorImageParameters":
            image_categories = FunctorImageCategories()
            for category in self.categories():
                if image_categories.is_image_category(category):
                    return category
            raise AssertionError("the object is in no functor-image category")

        def constructing_functor(self) -> "Element":
            return self.image_category().functor()
