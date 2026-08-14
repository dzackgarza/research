from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.map import Map
from sage.structure.element import Element
from sage.structure.parent import Parent

# A homset is a parent whose elements are maps between its two objects
# (Homset._element_constructor_, homset.py:806). Most are Morphism
# subclasses. Some historical Sage families, such as scheme morphisms, are
# direct Element subclasses.
_DomainElement = TypeVar("_DomainElement", default=Element, covariant=True)
_CodomainElement = TypeVar("_CodomainElement", default=Element, covariant=True)
_M = TypeVar("_M", bound=Element, default=Element, covariant=True)
_HomDomainElement = TypeVar("_HomDomainElement")
_HomCodomainElement = TypeVar("_HomCodomainElement")

class Homset(Parent[_M], Generic[_M, _DomainElement, _CodomainElement]):
    def __init__(
        self,
        domain: Parent[_DomainElement],
        codomain: Parent[_CodomainElement],
        category: Category | None = ...,
        base: object = ...,
        check: bool = ...,
    ) -> None: ...
    def an_element(self) -> _M: ...
    def domain(self) -> Parent[_DomainElement]: ...
    def codomain(self) -> Parent[_CodomainElement]: ...

# The homset constructor: Hom(X, Y) in the given category (the meet of the
# parents' categories when none is named).
def Hom(
    X: Parent[_HomDomainElement],
    Y: Parent[_HomCodomainElement],
    category: Category | None = ...,
    check: bool = ...,
) -> Homset[
    Map[_HomDomainElement, _HomCodomainElement],
    _HomDomainElement,
    _HomCodomainElement,
]: ...
