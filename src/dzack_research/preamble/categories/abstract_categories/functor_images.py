r"""Presented images of a functor.

For ``F : C -> D`` an object of ``ImageOfFunctor(F)`` is a chosen presentation
``(X, F(X))``.  Two different ``X`` may therefore give distinct presented
objects even when ``F(X)`` is literally the same object of ``D``.  Morphisms
are the arrows of ``D`` between the underlying images, wrapped so their
endpoints are the presented objects.  The faithful forgetful functor to ``D``
forgets only the chosen presentation.
"""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    _category_hom,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.owned_category import object_of


class FunctorImageMorphism(Morphism):
    r"""A codomain arrow read between two chosen functor presentations."""

    def __init__(self, parent, underlying_arrow) -> None:
        Morphism.__init__(self, parent)
        self._underlying_arrow = underlying_arrow

    def underlying_arrow(self):
        return self._underlying_arrow

    def __mul__(self, other):
        if not isinstance(other, FunctorImageMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        category = self.parent().image_category()
        return category.Mor(other.domain(), self.codomain())(
            self.underlying_arrow() * other.underlying_arrow()
        )


class FunctorImageHomset(CategoricalHomset):
    Element = FunctorImageMorphism

    def image_category(self):
        return self.base_category()

    def _underlying_homset(self):
        category = self.image_category().functor().codomain()
        return _category_hom(
            category,
            self.domain().underlying_image(),
            self.codomain().underlying_image(),
        )

    def _element_constructor_(self, arrow):
        if isinstance(arrow, FunctorImageMorphism):
            if arrow.parent() is self:
                return arrow
            arrow = arrow.underlying_arrow()
        if arrow not in self._underlying_homset():
            raise ValueError("the arrow is not a morphism between the underlying functor images")
        return FunctorImageMorphism(self, arrow)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only for an endomorphism Hom-set")
        return self(self._underlying_homset().identity())


class FunctorImageHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = FunctorImageHomset


class ImageOfFunctor(OwnedCategory):
    r"""The category of outputs of one functor with a chosen source presentation."""

    _HomCategory = FunctorImageHomCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, functor: (cls, id(functor)))
    def __classcall__(cls, functor):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(functor)
        return typecall(cls, functor)

    class ParentMethods:
        def __init__(self, preimage, underlying_image, **rest) -> None:
            self._preamble_functor_preimage = preimage
            self._preamble_underlying_functor_image = underlying_image
            super().__init__(**rest)

        def preimage(self):
            return self._preamble_functor_preimage

        def underlying_image(self):
            return self._preamble_underlying_functor_image

        def constructing_functor(self):
            return self.category().functor()

        def _repr_(self) -> str:
            return f"{self.underlying_image()} presented as {self.constructing_functor()}({self.preimage()})"

    def __init__(self, functor) -> None:
        self._functor = functor
        self._presentations = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return id(self._functor)

    def super_categories(self):
        return [Objects()]

    def functor(self):
        return self._functor

    def an_object(self):
        return self.object(self.functor().domain().an_object())

    def object(self, preimage):
        if preimage not in self.functor().domain():
            raise TypeError("a presented image starts from an object of the functor domain")
        key = id(preimage)
        recorded = self._presentations.get(key)
        if recorded is not None and recorded[0] is preimage:
            return recorded[1]
        image = self.functor()(preimage)
        presented = object_of(self, preimage=preimage, underlying_image=image)
        self._presentations[key] = (preimage, presented)
        return presented

    __call__ = object

    def adopt(self, preimage, image):
        self.functor().adopt_object_image(preimage, image)
        return self.object(preimage)

    def __contains__(self, candidate) -> bool:
        return getattr(candidate, "category", lambda: None)() is self

    def Mor(self, domain: Parent, codomain: Parent):
        if domain not in self or codomain not in self:
            raise TypeError("a functor-image Hom requires two presentations of this image category")
        return self.HomCategory().Of(domain, codomain)

    def identity(self, obj):
        return self.Mor(obj, obj).identity()

    @cached_method
    def inclusion(self):
        return FunctorImageForgetfulFunctor(self)

    def _repr_(self) -> str:
        return f"Category of chosen presentations in the image of {self.functor()}"


class FunctorImageForgetfulFunctor(Functor):
    r"""Forget a chosen preimage and retain the underlying codomain object."""

    _faithful = True

    def __init__(self, image_category: ImageOfFunctor) -> None:
        self._image_category = image_category
        super().__init__(image_category, image_category.functor().codomain())

    def image_category(self):
        return self._image_category

    def _apply_object(self, presented):
        return presented.underlying_image()

    def _apply_morphism(self, morphism):
        return morphism.underlying_arrow()


__all__ = [
    "FunctorImageForgetfulFunctor",
    "FunctorImageHomset",
    "FunctorImageMorphism",
    "ImageOfFunctor",
]
