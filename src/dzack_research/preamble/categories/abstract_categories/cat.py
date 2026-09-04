r"""A represented category ``Cat`` of categories, functors, and natural transformations."""

from dzack_research.preamble.categories.abstract_categories.hom_foundation import OwnedHomset
from sage.misc.cachefunc import cached_method
from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    ArrowCategory,
)



class CategoryObject(Parent):
    r"""A Sage category regarded as an object of ``Cat``."""

    def __init__(self, category_of_categories, represented_category) -> None:
        self._category_of_categories = category_of_categories
        self._represented_category = represented_category
        Parent.__init__(self, category=SageSets())

    def category_of_categories(self):
        return self._category_of_categories

    def represented_category(self):
        return self._represented_category

    def _repr_(self) -> str:
        return f"[{self.represented_category()}]"


class CategoryFunctorMorphism(Morphism):
    r"""A live functor regarded as a morphism in ``Cat``."""

    def __init__(self, parent, functor) -> None:
        Morphism.__init__(self, parent)
        if functor.domain() != self.domain().represented_category():
            raise ValueError("the functor has the wrong Cat-domain")
        if functor.codomain() != self.codomain().represented_category():
            raise ValueError("the functor has the wrong Cat-codomain")
        self._functor = functor

    def functor(self):
        return self._functor

    def __call__(self, value):
        return self.functor()(value)

    def _call_(self, value):
        return self.functor()(value)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        from dzack_research.preamble.categories.functors.core import CompositeFunctor

        return self.parent().category_of_categories().arrow(
            CompositeFunctor(other.functor(), self.functor())
        )

    def _repr_(self) -> str:
        return repr(self.functor())


class CategoryFunctorHomset(OwnedHomset):
    Element = CategoryFunctorMorphism

    def __init__(self, category_of_categories, domain, codomain) -> None:
        self._category_of_categories = category_of_categories
        Homset.__init__(self, domain, codomain, category=SageSets())

    def category_of_categories(self):
        return self._category_of_categories

    def _element_constructor_(self, functor):
        return CategoryFunctorMorphism(self, functor)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism functor Hom-set")
        from dzack_research.preamble.categories.functors.core import IdentityFunctor

        return self(IdentityFunctor(self.domain().represented_category()))


class Cat(Category):
    r"""The represented category of categories."""

    def __init__(self) -> None:
        self._arrows = {}
        super().__init__()

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return isinstance(candidate, (Category, CategoryObject))

    def object(self, category):
        if isinstance(category, CategoryObject):
            return category
        if not isinstance(category, Category):
            raise TypeError("an object of Cat is a category")
        return self._object_on(category)

    @cached_method
    def _object_on(self, category):
        return CategoryObject(self, category)

    def functor_homset(self, domain, codomain):
        return CategoryFunctorHomset(self, self.object(domain), self.object(codomain))

    def arrow(self, functor):
        key = id(functor)
        cached = self._arrows.get(key)
        if cached is not None and cached.functor() is functor:
            return cached
        result = self.functor_homset(functor.domain(), functor.codomain())(functor)
        self._arrows[key] = result
        return result

    def Mor(self, domain, codomain):
        return FunctorCategory(self, domain, codomain)

    def identity(self, category):
        return self.functor_homset(category, category).identity()

    def compose(self, second, first):
        if first.codomain() is not second.domain():
            raise ValueError("functors are not composable in Cat")
        return second * first

    def ArrowCategory(self):
        return ArrowCategory(self)

    def _repr_(self) -> str:
        return "Category of categories"


class NaturalTransformationMorphism(Morphism):
    r"""A natural transformation as a morphism in a functor category."""

    def __init__(self, parent, transformation) -> None:
        Morphism.__init__(self, parent)
        if transformation.source() is not self.domain().arrow().functor():
            raise ValueError("the natural transformation has the wrong source functor")
        if transformation.target() is not self.codomain().arrow().functor():
            raise ValueError("the natural transformation has the wrong target functor")
        self._transformation = transformation

    def transformation(self):
        return self._transformation

    def component(self, obj):
        return self.transformation().component(obj)

    def naturality_square(self, morphism):
        return self.transformation().naturality_square(morphism)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain().arrow().functor()
        target = self.codomain().arrow().functor()
        from dzack_research.preamble.categories.functors.core import NaturalTransformation

        composite = NaturalTransformation(
            source,
            target,
            lambda obj: self.component(obj) * other.component(obj),
        )
        return self.parent().functor_category().Mor(other.domain(), self.codomain())(
            composite
        )


class NaturalTransformationHomset(OwnedHomset):
    Element = NaturalTransformationMorphism

    def __init__(self, functor_category, domain, codomain) -> None:
        self._functor_category = functor_category
        Homset.__init__(self, domain, codomain, category=SageSets())

    def functor_category(self):
        return self._functor_category

    def _element_constructor_(self, transformation):
        from dzack_research.preamble.categories.functors.core import NaturalTransformation

        if callable(transformation) and not isinstance(transformation, NaturalTransformation):
            transformation = NaturalTransformation(
                self.domain().arrow().functor(), self.codomain().arrow().functor(), transformation
            )
        return NaturalTransformationMorphism(self, transformation)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism natural-transformation Hom-set")
        functor = self.domain().arrow().functor()
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            _identity_morphism,
        )

        from dzack_research.preamble.categories.functors.core import NaturalTransformation

        return self(
            NaturalTransformation(
                functor,
                functor,
                lambda obj: _identity_morphism(functor(obj)),
            )
        )


class FunctorCategory(Category):
    r"""The category ``[C,D]`` of represented functors and natural transformations."""

    def __init__(self, category_of_categories, domain, codomain) -> None:
        self._cat = category_of_categories
        self._domain_category = domain
        self._codomain_category = codomain
        super().__init__()

    def _make_named_class_key(self, name):
        return self._cat, self._domain_category, self._codomain_category

    def domain_category(self):
        return self._domain_category

    def codomain_category(self):
        return self._codomain_category

    def super_categories(self):
        return [Objects()]

    def object(self, functor):
        if functor.domain() != self.domain_category() or functor.codomain() != self.codomain_category():
            raise ValueError("the functor has the wrong functor-category endpoints")
        return self._object_on(functor)

    @cached_method
    def _object_on(self, functor):
        return self._cat.ArrowCategory()(self._cat.arrow(functor))

    __call__ = object

    def __contains__(self, candidate) -> bool:
        try:
            arrow = candidate.arrow()
        except AttributeError:
            return False
        return (
            isinstance(arrow, CategoryFunctorMorphism)
            and arrow.functor().domain() == self.domain_category()
            and arrow.functor().codomain() == self.codomain_category()
        )

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a natural-transformation Hom requires two parallel functors")
        return NaturalTransformationHomset(self, domain, codomain)


    def identity(self, functor_object):
        return self.Mor(functor_object, functor_object).identity()

    def _repr_(self) -> str:
        return f"Functor category [{self.domain_category()}, {self.codomain_category()}]"


class NaturalIsomorphism:
    r"""A selected pair of mutually inverse natural transformations."""

    def __init__(self, forward, inverse) -> None:
        if forward.domain() is not inverse.codomain() or forward.codomain() is not inverse.domain():
            raise ValueError("inverse natural transformations have reversed endpoints")
        self._forward = forward
        self._inverse = inverse

    def forward(self):
        return self._forward

    def inverse(self):
        return self._inverse

    def component(self, obj):
        return self.forward().component(obj)


__all__ = [
    "Cat",
    "CategoryFunctorHomset",
    "CategoryFunctorMorphism",
    "CategoryObject",
    "FunctorCategory",
    "NaturalIsomorphism",
    "NaturalTransformationHomset",
    "NaturalTransformationMorphism",
]
