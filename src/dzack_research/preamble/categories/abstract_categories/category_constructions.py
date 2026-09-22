r"""Opposite categories and binary products of categories."""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown, UnknownClass
from sage.structure.element import parent
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
    _category_accepts_morphism,
    _category_mor_parent,
    _precomposable,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.owned_category import _object_of


class OppositeMorphism(Morphism):
    r"""An arrow of ``C^op`` represented by the reverse arrow in ``C``."""

    def __init__(
        self,
        parent: OppositeMor,
        underlying_arrow: Morphism,
    ) -> None:
        Morphism.__init__(self, parent)
        if underlying_arrow.domain() is not self.codomain().underlying_object():
            raise ValueError("the underlying opposite arrow has the wrong domain")
        if underlying_arrow.codomain() is not self.domain().underlying_object():
            raise ValueError("the underlying opposite arrow has the wrong codomain")
        self._underlying_arrow = underlying_arrow

    def underlying_arrow(self) -> Morphism:
        return self._underlying_arrow

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if self is other:
            return True
        if parent(other) is not self.parent():
            return False
        return self.underlying_arrow() == other.underlying_arrow()

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        return self.parent().opposite_category().Mor(
            other.domain(), self.codomain()
        )(other.underlying_arrow() * self.underlying_arrow())


class OppositeMor(CategoricalMor):
    Element = OppositeMorphism

    def __init__(
        self,
        family: MorCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(
            self, family, domain, codomain
        )

    def opposite_category(self) -> _OppositeCategory:
        return self.base_category()

    def _element_constructor_(self, underlying_arrow):
        match underlying_arrow:
            case OppositeMorphism():
                if underlying_arrow.parent() is self:
                    return underlying_arrow
                if underlying_arrow.domain() is not self.domain() or underlying_arrow.codomain() is not self.codomain():
                    raise ValueError("the opposite morphism has the wrong endpoints")
                underlying_arrow = underlying_arrow.underlying_arrow()
        base = self.opposite_category().base_category()
        if not _category_accepts_morphism(
            base,
            self.codomain().underlying_object(),
            self.domain().underlying_object(),
            underlying_arrow,
        ):
            raise ValueError("the reversed arrow does not belong to the base category")
        return OppositeMorphism(self, underlying_arrow)

    def identity(self) -> OppositeMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Mor object")
        underlying = self.domain().underlying_object()
        base = self.opposite_category().base_category()
        return self(_category_mor_parent(base, underlying, underlying).identity())


class OppositeMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = OppositeMor


class _OppositeCategory(OwnedCategory):
    r"""The opposite category ``C^op``."""

    _MorCategory = OppositeMorCategoryConstruction

    def an_object(self) -> Parent:
        r"""An object of the base category, read in the opposite."""
        return self.object(self.base_category().an_object())

    class ParentMethods:
        r"""An object of ``C`` regarded as an object of ``C^op``."""

        def __init__(self, underlying_object: Parent, **rest) -> None:
            self._underlying_object = underlying_object
            super().__init__(**rest)

        def opposite_category(self) -> _OppositeCategory:
            return self.category()

        def underlying_object(self) -> Parent:
            return self._underlying_object

        def _repr_(self) -> str:
            return f"op({self.underlying_object()})"

    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self) -> Category:
        return self._base_category

    def super_categories(self):
        return [Objects()]

    @cached_method(key=lambda self, underlying_object: id(underlying_object))
    def object(self, underlying_object: Parent) -> Parent:
        if underlying_object not in self.base_category():
            raise TypeError("the object lies outside the base category")
        return _object_of(self, underlying_object=underlying_object)

    __call__ = object

    def Mor(self, domain: Parent, codomain: Parent) -> OppositeMor:
        if domain not in self or codomain not in self:
            raise TypeError("an opposite Mor requires two opposite objects")
        return self.MorCategory().Of(domain, codomain)


    def identity(self, obj: Parent) -> OppositeMorphism:
        return self.Mor(obj, obj).identity()

    def opposite_category(self) -> Category:
        return self.base_category()

    def _repr_(self) -> str:
        return f"Opposite of {self.base_category()}"



class ProductMorphism(Morphism):
    r"""A pair of morphisms in a product category."""

    def __init__(
        self,
        parent: ProductMor,
        first: Morphism,
        second: Morphism,
    ) -> None:
        Morphism.__init__(self, parent)
        if first.domain() is not self.domain().first() or first.codomain() is not self.codomain().first():
            raise ValueError("the first component has the wrong endpoints")
        if second.domain() is not self.domain().second() or second.codomain() is not self.codomain().second():
            raise ValueError("the second component has the wrong endpoints")
        self._first = first
        self._second = second

    def first(self) -> Morphism:
        return self._first

    def second(self) -> Morphism:
        return self._second

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if self is other:
            return True
        if parent(other) is not self.parent():
            return False
        equalities = (self.first() == other.first(), self.second() == other.second())
        if any(answer is False for answer in equalities):
            return False
        return True if all(answer is True for answer in equalities) else Unknown

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        return self.parent().product_category().Mor(
            other.domain(), self.codomain()
        )(self.first() * other.first(), self.second() * other.second())


class ProductMor(CategoricalMor):
    Element = ProductMorphism

    def __init__(
        self,
        family: MorCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(
            self, family, domain, codomain
        )

    def product_category(self) -> _ProductCategory:
        return self.base_category()

    def _element_constructor_(self, first, second=None):
        match first:
            case ProductMorphism() if second is None:
                if first.parent() is self:
                    return first
                if first.domain() is not self.domain() or first.codomain() is not self.codomain():
                    raise ValueError("the product morphism has the wrong endpoints")
                first, second = first.first(), first.second()
        if second is None:
            first, second = first
        product = self.product_category()
        if not _category_accepts_morphism(
            product.first_category(),
            self.domain().first(),
            self.codomain().first(),
            first,
        ):
            raise ValueError("the first map is not a morphism of the first category")
        if not _category_accepts_morphism(
            product.second_category(),
            self.domain().second(),
            self.codomain().second(),
            second,
        ):
            raise ValueError("the second map is not a morphism of the second category")
        return ProductMorphism(self, first, second)

    def identity(self) -> ProductMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Mor object")
        first = self.domain().first()
        second = self.domain().second()
        product = self.product_category()
        return self(
            _category_mor_parent(product.first_category(), first, first).identity(),
            _category_mor_parent(product.second_category(), second, second).identity(),
        )


class ProductMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = ProductMor


class _ProductCategory(OwnedCategory):
    r"""The categorical product ``C x D``.

    Unverified specimens use nonidentity component maps and check both Mor
    ownership and the reversed composition in an opposite category::

        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: points = finite_ordered_set(("a", "b"))
        sage: swap = Sets().Mor(points, points)(lambda point: "b" if point == "a" else "a")
        sage: collapse = Sets().Mor(points, points)(lambda point: "a")
        sage: category = Cat().product((Sets(), Sets()))
        sage: obj = category(points, points)
        sage: Mor = category.Mor(obj, obj)
        sage: Mor is category.MorCategory().Of(obj, obj)
        True
        sage: arrow = Mor(swap, swap)
        sage: arrow * arrow == Mor.identity()
        True
        sage: opposite = Sets().opposite()
        sage: obj = opposite(points)
        sage: Mor = opposite.Mor(obj, obj)
        sage: Mor is opposite.MorCategory().Of(obj, obj)
        True
        sage: (Mor(swap) * Mor(collapse)).underlying_arrow()("a")
        'a'
        sage: (Mor(collapse) * Mor(swap)).underlying_arrow()("a")
        'b'

    Unverified specimens: equal endpoints alone do not admit an arrow of a
    factor category whose morphisms are restricted::

        sage: injections = Sets().WideSubcategory(Sets().MonomorphismArrowCategory())
        sage: category = Cat().product((injections, Sets()))
        sage: obj = category(points, points)
        sage: category.Mor(obj, obj)(swap, swap).first() is swap
        True
        sage: category.Mor(obj, obj)(collapse, swap)
        Traceback (most recent call last):
        ...
        ValueError: the first map is not a morphism of the first category
        sage: opposite = injections.opposite()
        sage: obj = opposite(points)
        sage: opposite.Mor(obj, obj)(swap).underlying_arrow() is swap
        True
        sage: opposite.Mor(obj, obj)(collapse)
        Traceback (most recent call last):
        ...
        ValueError: the reversed arrow does not belong to the base category
    """

    _MorCategory = ProductMorCategoryConstruction

    def an_object(self) -> Parent:
        r"""The pair of witnesses of the two factors."""
        return self.pair(
            self.first_category().an_object(),
            self.second_category().an_object(),
        )

    class ParentMethods:
        r"""An object ``(X,Y)`` of a product category ``C x D``."""

        def __init__(self, first: Parent, second: Parent, **rest) -> None:
            self._first = first
            self._second = second
            super().__init__(**rest)

        def product_category(self) -> _ProductCategory:
            return self.category()

        def first(self) -> Parent:
            return self._first

        def second(self) -> Parent:
            return self._second

        def __iter__(self):
            r"""Iterate the two factors of this categorical product object.

            This is presentation of the retained pair, not a replacement by a
            Python tuple: the parent remains the object of ``C x D`` and its
            two components keep their original mathematical owners.
            """
            return iter((self.first(), self.second()))

        def _repr_(self) -> str:
            return f"({self.first()}, {self.second()})"

    def __init__(self, first_category: Category, second_category: Category) -> None:
        self._first_category = first_category
        self._second_category = second_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._first_category, self._second_category

    def first_category(self) -> Category:
        return self._first_category

    def second_category(self) -> Category:
        return self._second_category

    def super_categories(self):
        return [Objects()]

    @cached_method(key=lambda self, first, second: (id(first), id(second)))
    def pair(self, first: Parent, second: Parent) -> Parent:
        if first not in self.first_category() or second not in self.second_category():
            raise TypeError("the pair lies outside the product category")
        return _object_of(self, first=first, second=second)

    __call__ = pair

    def Mor(self, domain: Parent, codomain: Parent) -> ProductMor:
        if domain not in self or codomain not in self:
            raise TypeError("a product Mor requires two product-category objects")
        return self.MorCategory().Of(domain, codomain)


    def identity(self, obj: Parent) -> ProductMorphism:
        return self.Mor(obj, obj).identity()

    def _repr_(self) -> str:
        return f"Product of {self.first_category()} and {self.second_category()}"


__all__ = [
    "OppositeMor",
    "OppositeMorphism",
    "ProductMor",
    "ProductMorphism",
]
