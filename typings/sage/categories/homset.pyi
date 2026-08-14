from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.structure.element import Element
from sage.structure.parent import Parent

# A homset is a parent whose elements are maps between its two objects
# (Homset._element_constructor_, homset.py:806). Most are Morphism
# subclasses. Some historical Sage families, such as scheme morphisms, are
# direct Element subclasses.
_DomainElement = TypeVar("_DomainElement", bound=Element, default=Element, covariant=True)
_CodomainElement = TypeVar("_CodomainElement", bound=Element, default=Element, covariant=True)
_M = TypeVar("_M", bound=Element, default=Element, covariant=True)

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
    X: Parent,
    Y: Parent,
    category: Category | None = ...,
    check: bool = ...,
) -> Homset: ...
