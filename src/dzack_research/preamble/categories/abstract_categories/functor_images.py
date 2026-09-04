r"""Categories of objects equipped with a chosen presentation as a functor image."""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from sage.misc.cachefunc import cached_method
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.abstract_categories.functors import ImageInclusionFunctor


class FunctorImageObject(Parent):
    r"""A chosen presentation ``A`` together with its image ``F(A)``."""

    def __init__(self, image_category, preimage, image_object) -> None:
        self._image_category = image_category
        self._preimage = preimage
        self._image_object = image_object
        Parent.__init__(self, category=SageSets())

    def image_category(self):
        return self._image_category

    def constructing_functor(self):
        return self.image_category().functor()

    def preimage(self):
        return self._preimage

    def image_object(self):
        return self._image_object

    def _repr_(self) -> str:
        return f"{self.image_object()} presented as {self.constructing_functor()}({self.preimage()})"


class FunctorImageMorphism(Morphism):
    r"""A codomain arrow between two chosen functor-image presentations."""

    def __init__(self, parent, codomain_arrow) -> None:
        Morphism.__init__(self, parent)
        if codomain_arrow.domain() is not self.domain().image_object():
            raise ValueError("the codomain arrow has the wrong image-domain")
        if codomain_arrow.codomain() is not self.codomain().image_object():
            raise ValueError("the codomain arrow has the wrong image-codomain")
        self._codomain_arrow = codomain_arrow

    def codomain_arrow(self):
        return self._codomain_arrow

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        category = self.parent().image_category()
        return category.Mor(other.domain(), self.codomain())(
            self.codomain_arrow() * other.codomain_arrow()
        )


class FunctorImageHomset(CategoricalHomset):
    Element = FunctorImageMorphism

    def __init__(self, image_category, domain, codomain) -> None:
        self._image_category = image_category
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(image_category), domain, codomain
        )

    def image_category(self):
        return self._image_category

    def _element_constructor_(self, codomain_arrow):
        return FunctorImageMorphism(self, codomain_arrow)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        image = self.domain().image_object()
        try:
            identity = image.Mor(image).identity()
        except (AttributeError, TypeError, ValueError):
            from sage.categories.homset import Hom

            identity = Hom(image, image).identity()
        return self(identity)


class FunctorImageCategories(Category):
    r"""The category whose objects are represented functor-image categories."""

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return isinstance(candidate, ImageOfFunctor)


class ImageOfFunctor(Category):
    r"""The category of outputs of ``F`` equipped with chosen preimages.

    An object is the pair ``(A, F(A))``.  The inclusion/projection to the
    codomain forgets only the chosen presentation.  This does not attempt to
    recover ``A`` from ``F(A)``, which is impossible for a general functor.
    """

    def __init__(self, functor) -> None:
        self._functor = functor
        super().__init__()

    def _make_named_class_key(self, name):
        return self._functor

    def functor(self):
        return self._functor

    def super_categories(self):
        return [Objects()]

    @cached_method
    def present(self, preimage):
        if preimage not in self.functor().domain():
            raise TypeError("the chosen preimage lies outside the functor domain")
        return FunctorImageObject(self, preimage, self.functor()(preimage))

    __call__ = present

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, FunctorImageObject)
            and candidate.image_category().functor() is self.functor()
        )

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("an image-category Hom requires two presented image objects")
        return FunctorImageHomset(self, domain, codomain)


    def identity(self, obj):
        return self.Mor(obj, obj).identity()

    def inclusion(self):

        return ImageInclusionFunctor(self)

    def _repr_(self) -> str:
        return f"Category of chosen images of {self.functor()}"


__all__ = [
    "FunctorImageCategories",
    "FunctorImageHomset",
    "FunctorImageMorphism",
    "FunctorImageObject",
    "ImageOfFunctor",
]
