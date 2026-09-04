"""Dependency-light runtime foundation for owned Hom-set parents."""

from sage.categories.homset import Homset
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets


class OwnedHomset(Homset):
    r"""A Hom-set whose elements enter through its owned constructor directly.

    Sage's ``Homset`` remains the runtime parent required by ``Morphism``.
    Mathematical inputs are not sent through Sage coercion discovery: each
    concrete Hom-set owns the interpretation implemented by
    ``_element_constructor_``.
    """

    def __call__(self, *args, **kwargs):
        return self._element_constructor_(*args, **kwargs)

    def identity_at(self, obj):
        if obj is not self.domain() or obj is not self.codomain():
            raise ValueError("this Hom parent does not represent endomorphisms of the stated object")
        return self.identity()


__all__ = ["OwnedHomset", "UnderlyingSetHomset", "underlying_set_homset"]

class UnderlyingSetHomset(OwnedHomset):
    r"""Plain-function Homset used only when an owned category declares no stronger arrows."""

    Element = SetMorphism

    def __init__(self, domain, codomain) -> None:
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

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity requires equal endpoints")
        return SetMorphism(self, lambda element: element)


_underlying_set_homsets = {}

def underlying_set_homset(domain, codomain):
    r"""Return the identity-cached plain-function Homset on these endpoints."""
    key = (id(domain), id(codomain))
    cached = _underlying_set_homsets.get(key)
    if cached is not None and cached.domain() is domain and cached.codomain() is codomain:
        return cached
    result = UnderlyingSetHomset(domain, codomain)
    _underlying_set_homsets[key] = result
    return result
