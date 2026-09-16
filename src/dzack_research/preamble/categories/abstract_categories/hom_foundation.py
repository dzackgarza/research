"""Dependency-light runtime foundation for owned Hom-set parents."""

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent


class OwnedHomset(Homset):
    r"""A Hom-set whose elements enter through its owned constructor directly.

    Sage's ``Homset`` remains the runtime parent required by ``Morphism``.
    Mathematical inputs are not sent through Sage coercion discovery: each
    concrete Hom-set owns the interpretation implemented by
    ``_element_constructor_``.
    """

    def __call__(self, *args, **kwargs) -> Morphism:
        return self._element_constructor_(*args, **kwargs)

    def identity_at(self, obj: Parent) -> Morphism:
        if obj is not self.domain() or obj is not self.codomain():
            raise ValueError("this Hom parent does not represent endomorphisms of the stated object")
        return self.identity()


__all__ = ["CategoryPacketMethods", "OwnedHomset", "UnderlyingSetHomset"]

class UnderlyingSetHomset(OwnedHomset):
    r"""Plain-function Homset used only when an owned category declares no stronger arrows."""

    Element = SetMorphism

    def __init__(self, domain: Parent, codomain: Parent) -> None:
        Homset.__init__(self, domain, codomain, category=SageSets())

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


_underlying_set_homsets = {}

def _underlying_set_homset(domain: Parent, codomain: Parent) -> UnderlyingSetHomset:
    r"""Return the identity-cached plain-function Homset on these endpoints."""
    key = (id(domain), id(codomain))
    cached = _underlying_set_homsets.get(key)
    if cached is not None and cached.domain() is domain and cached.codomain() is codomain:
        return cached
    result = UnderlyingSetHomset(domain, codomain)
    _underlying_set_homsets[key] = result
    return result


def _has_category_packet_surface(category) -> bool:
    r"""Return whether ``category`` carries the coordinated Hom packet surface.

    Owned category objects receive these operations through ``Cat.ParentMethods``
    in their dynamic ``subcategory_class``.  That is a mathematical capability,
    not reliably a Python ``isinstance`` relation: Sage requires nested method
    providers themselves to have no superclass.
    """
    return callable(getattr(category, "category_packet", None)) and callable(
        getattr(category, "_hom_endpoint", None)
    )


class CategoryPacketMethods:
    r"""The coordinated ``C/Hom_C/End_C/Iso_C/Aut_C`` construction surface.

    Sited here, below the packet itself, so that the owned category bases can
    carry it: an axiom category is built from those bases, states no morphisms
    of its own, and must still be askable for the Hom of the category it
    refines.
    """

    def _hom_endpoint(self, obj: Parent | Category) -> Parent | Category:
        r"""Represent an endpoint in this category's Hom construction.

        Ordinary categories already receive their objects. ``Cat`` overrides
        this at its own boundary because Sage morphisms use parent objects
        representing categories as their endpoints.
        """
        return obj

    def category_packet(self):
        r"""Return the Hom/End/Mono/Epi/Iso/Aut packet owned by this category."""
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            _category_packet,
        )

        return _category_packet(self)

    def HomCategory(self) -> Category:
        return self.category_packet().Homs()

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
        return self.HomCategory().Of(source, target)

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
