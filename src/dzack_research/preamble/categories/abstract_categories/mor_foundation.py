"""Dependency-light runtime foundation for owned Mor object parents."""

from __future__ import annotations

from sage.categories.category import Category
from sage.categories.mor import Mor as SageMor
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.element import Element
from sage.structure.parent import Parent


class OwnedMor(SageMor):
    r"""A Mor object whose elements enter through its owned constructor directly.

    Sage's ``Mor`` remains the runtime parent required by ``Morphism``.
    Mathematical inputs are not sent through Sage coercion discovery: each
    concrete Mor object owns the interpretation implemented by
    ``_element_constructor_``.
    """

    def __call__(self, *args, **kwargs) -> Morphism:
        return self._element_constructor_(*args, **kwargs)

    def identity_at(self, obj: Parent) -> Morphism:
        if obj is not self.domain() or obj is not self.codomain():
            raise ValueError("this Mor parent does not represent endomorphisms of the stated object")
        return self.identity()


__all__ = ["CategoryPacketMethods", "OwnedMor", "UnderlyingSetMor"]

class UnderlyingSetMor(OwnedMor):
    r"""Plain-function Mor used only when an owned category declares no stronger arrows."""

    Element = SetMorphism

    def __init__(self, domain: Parent, codomain: Parent) -> None:
        SageMor.__init__(self, domain, codomain, category=SageSets())

    def _element_constructor_(self, datum):
        if isinstance(datum, SetMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the set morphism has the wrong endpoints")
            if datum.parent() is self:
                return datum
            datum = datum._call_
        if not callable(datum):
            raise TypeError("an underlying set map is supplied by a callable")
        return SetMorphism(self, datum)

    def identity(self) -> SetMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity requires equal endpoints")
        return SetMorphism(self, lambda element: element)


_underlying_set_mors = {}

def _underlying_set_mor(domain: Parent, codomain: Parent) -> UnderlyingSetMor:
    r"""Return the identity-cached plain-function Mor on these endpoints."""
    key = (id(domain), id(codomain))
    cached = _underlying_set_mors.get(key)
    if cached is not None and cached.domain() is domain and cached.codomain() is codomain:
        return cached
    result = UnderlyingSetMor(domain, codomain)
    _underlying_set_mors[key] = result
    return result


def _has_category_packet_surface(category: Category) -> bool:
    r"""Whether ``category``'s Mor construction is the owned packet or Sage's ``Hom``.

    ``OWN-06`` adapter.  Every category is an object of ``Cat``; what differs
    is the runtime that realizes its Mors.  The owned packet reaches a
    category in exactly two ways, both fixed by the runtime root: an owned
    category, and every join or axiom category Sage assembles from owned
    members, carries ``Cat.ParentMethods`` through its ``subcategory_class``
    (``CatConstructionsMixin`` in ``owned_category.py``); ``Cat`` itself and
    the Mor categories realized on Sage's ``Mor`` carry
    :class:`CategoryPacketMethods` as a declared base.  A category carrying
    neither is Sage's own and keeps Sage's ``Hom`` ingress.  This reads which
    of the two realizations is present and decides nothing else; it is not
    membership in ``Cat``, which a Sage-native category also has
    mathematically and a join of owned categories has without its placement
    being recorded.
    """
    from dzack_research.preamble.categories.abstract_categories.cat import Cat

    match category:
        case CategoryPacketMethods() | Cat.ParentMethods():
            return True
        case _:
            return False


class CategoryPacketMethods:
    r"""The coordinated ``C/Hom_C/End_C/Iso_C/Aut_C`` construction surface.

    Sited here, below the packet itself, so that the owned category bases can
    carry it: an axiom category is built from those bases, states no morphisms
    of its own, and must still be askable for the Mor of the category it
    refines.

    The packet assembles into two categories of its own: the arrow category
    ``Ar(C) = [[1], C]``, whose objects are all the arrows the Mor families
    classify, and the core, whose arrows are the isomorphisms the Iso family
    classifies.  Both are stated here once, so a Mor category realized on
    Sage's ``Mor`` reaches them by the same construction as every other
    category; ``Cat.ParentMethods`` names these same functions.
    """

    @property
    def ObjectType(self) -> type[Parent]:
        r"""The implementation type for objects of this category."""
        return self.parent_class

    @property
    def ElementType(self) -> type[Element]:
        r"""The implementation type for elements of those objects."""
        return self.element_class

    def ArrowCategory(self) -> Category:
        r"""Return \(\mathrm{Ar}(C) = [[1], C]\), the functor category out of the walking arrow."""
        from dzack_research.preamble.categories.abstract_categories.cat import Cat
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        return Cat().Mor(FiniteOrdinalCategory(2), self)

    def Core(self) -> Category:
        r"""Return the core of this category: its objects and its isomorphisms."""
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            _CoreCategory,
        )

        return _CoreCategory(self)

    def _mor_endpoint(self, obj: Parent | Category) -> Parent | Category:
        r"""Represent an endpoint in this category's Mor construction.

        Ordinary categories already receive their objects. ``Cat`` overrides
        this at its own boundary because Sage morphisms use parent objects
        representing categories as their endpoints.

        Protected construction protocol: Mor-family entries and categories
        with the same objects may delegate to this method. Such a category
        retains the base's endpoint representation, not its Mor family or
        its arrow admission. The method does not establish membership;
        the receiving Mor-family entry checks placement after normalization.
        """
        return obj

    def category_packet(self):
        r"""Return the Mor/End/Mono/Epi/Iso/Aut packet owned by this category."""
        from dzack_research.preamble.categories.abstract_categories.mor_categories import (
            _category_packet,
        )

        return _category_packet(self)

    def MorCategory(self) -> Category:
        return self.category_packet().Mors()

    def EndCategory(self) -> Category:
        return self.category_packet().Ends()

    def MonoCategory(self) -> Category:
        return self.category_packet().Monos()

    def EpiCategory(self) -> Category:
        return self.category_packet().Epis()

    def IsoCategory(self) -> Category:
        return self.category_packet().Isos()

    def AutCategory(self) -> Category:
        return self.category_packet().Auts()

    def Mor(self, source: Parent, target: Parent) -> Category:
        return self.MorCategory().Of(source, target)

    def End(self, obj: Parent) -> Category:
        return self.EndCategory().Of(obj)

    def Mono(self, source: Parent, target: Parent) -> Category:
        return self.MonoCategory().Of(source, target)

    def Epi(self, source: Parent, target: Parent) -> Category:
        return self.EpiCategory().Of(source, target)

    def Iso(self, source: Parent, target: Parent) -> Category:
        return self.IsoCategory().Of(source, target)

    def Aut(self, obj: Parent) -> Category:
        return self.AutCategory().Of(obj)
