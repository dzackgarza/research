r"""Opposite categories and binary products of categories."""

from dzack_research.preamble.categories.abstract_categories.hom_foundation import OwnedHomset
from sage.misc.cachefunc import cached_method
from sage.categories.category import Category
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.sets.set_categories import Sets as _OwnedSets
from sage.structure.parent import Parent


def _identity(obj):
    try:
        return Hom(obj, obj).identity()
    except (TypeError, ValueError):
        return _OwnedSets().Mor(obj, obj).identity()


class OppositeObject(Parent):
    r"""An object of ``C`` regarded as an object of ``C^op``."""

    def __init__(self, opposite_category, underlying_object) -> None:
        self._opposite_category = opposite_category
        self._underlying_object = underlying_object
        Parent.__init__(self, category=SageSets())

    def opposite_category(self):
        return self._opposite_category

    def underlying_object(self):
        return self._underlying_object

    def _repr_(self) -> str:
        return f"op({self.underlying_object()})"


class OppositeMorphism(Morphism):
    r"""An arrow of ``C^op`` represented by the reverse arrow in ``C``."""

    def __init__(self, parent, underlying_arrow) -> None:
        Morphism.__init__(self, parent)
        if underlying_arrow.domain() is not self.codomain().underlying_object():
            raise ValueError("the underlying opposite arrow has the wrong domain")
        if underlying_arrow.codomain() is not self.domain().underlying_object():
            raise ValueError("the underlying opposite arrow has the wrong codomain")
        self._underlying_arrow = underlying_arrow

    def underlying_arrow(self):
        return self._underlying_arrow

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().opposite_category().Mor(
            other.domain(), self.codomain()
        )(other.underlying_arrow() * self.underlying_arrow())


class OppositeHomset(OwnedHomset):
    Element = OppositeMorphism

    def __init__(self, opposite_category, domain, codomain) -> None:
        self._opposite_category = opposite_category
        Homset.__init__(self, domain, codomain, category=SageSets())

    def opposite_category(self):
        return self._opposite_category

    def _element_constructor_(self, underlying_arrow):
        return OppositeMorphism(self, underlying_arrow)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        return self(_identity(self.domain().underlying_object()))


class OppositeCategory(Category):
    r"""The opposite category ``C^op``."""

    def __init__(self, base_category) -> None:
        self._base_category = base_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self):
        return self._base_category

    def super_categories(self):
        return [Objects()]

    @cached_method
    def object(self, underlying_object):
        if underlying_object not in self.base_category():
            raise TypeError("the object lies outside the base category")
        return OppositeObject(self, underlying_object)

    __call__ = object

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, OppositeObject)
            and candidate.opposite_category().base_category() == self.base_category()
        )

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("an opposite Hom requires two opposite objects")
        return OppositeHomset(self, domain, codomain)


    def identity(self, obj):
        return self.Mor(obj, obj).identity()

    def opposite_category(self):
        return self.base_category()

    def _repr_(self) -> str:
        return f"Opposite of {self.base_category()}"


class ProductObject(Parent):
    r"""An object ``(X,Y)`` of a product category ``C x D``."""

    def __init__(self, product_category, first, second) -> None:
        self._product_category = product_category
        self._first = first
        self._second = second
        Parent.__init__(self, category=SageSets())

    def product_category(self):
        return self._product_category

    def first(self):
        return self._first

    def second(self):
        return self._second

    def _repr_(self) -> str:
        return f"({self.first()}, {self.second()})"


class ProductMorphism(Morphism):
    r"""A pair of morphisms in a product category."""

    def __init__(self, parent, first, second) -> None:
        Morphism.__init__(self, parent)
        if first.domain() is not self.domain().first() or first.codomain() is not self.codomain().first():
            raise ValueError("the first component has the wrong endpoints")
        if second.domain() is not self.domain().second() or second.codomain() is not self.codomain().second():
            raise ValueError("the second component has the wrong endpoints")
        self._first = first
        self._second = second

    def first(self):
        return self._first

    def second(self):
        return self._second

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().product_category().Mor(
            other.domain(), self.codomain()
        )(self.first() * other.first(), self.second() * other.second())


class ProductHomset(OwnedHomset):
    Element = ProductMorphism

    def __init__(self, product_category, domain, codomain) -> None:
        self._product_category = product_category
        Homset.__init__(self, domain, codomain, category=SageSets())

    def product_category(self):
        return self._product_category

    def _element_constructor_(self, first, second=None):
        if second is None:
            first, second = first
        return ProductMorphism(self, first, second)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        return self(_identity(self.domain().first()), _identity(self.domain().second()))


class ProductCategory(Category):
    r"""The categorical product ``C x D``."""

    def __init__(self, first_category, second_category) -> None:
        self._first_category = first_category
        self._second_category = second_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._first_category, self._second_category

    def first_category(self):
        return self._first_category

    def second_category(self):
        return self._second_category

    def super_categories(self):
        return [Objects()]

    @cached_method
    def pair(self, first, second):
        if first not in self.first_category() or second not in self.second_category():
            raise TypeError("the pair lies outside the product category")
        return ProductObject(self, first, second)

    __call__ = pair

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, ProductObject)
            and candidate.first() in self.first_category()
            and candidate.second() in self.second_category()
        )

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a product Hom requires two product-category objects")
        return ProductHomset(self, domain, codomain)


    def identity(self, obj):
        return self.Mor(obj, obj).identity()

    def _repr_(self) -> str:
        return f"Product of {self.first_category()} and {self.second_category()}"


__all__ = [
    "OppositeCategory",
    "OppositeHomset",
    "OppositeMorphism",
    "OppositeObject",
    "ProductCategory",
    "ProductHomset",
    "ProductMorphism",
    "ProductObject",
]
