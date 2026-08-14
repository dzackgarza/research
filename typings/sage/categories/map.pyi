from typing import Generic, Self, TypeVar

from sage.categories.homset import Homset
from sage.structure.element import Element
from sage.structure.parent import Parent

_DomainElement = TypeVar("_DomainElement", default=Element)
_CodomainElement = TypeVar("_CodomainElement", default=Element)

class Map(Element, Generic[_DomainElement, _CodomainElement]):
    def __init__(
        self,
        parent: Homset[
            Map[_DomainElement, _CodomainElement],
            _DomainElement,
            _CodomainElement,
        ],
    ) -> None: ...
    def domain(self) -> Parent[_DomainElement]: ...
    def codomain(self) -> Parent[_CodomainElement] | None: ...
    def __call__(self, x: _DomainElement) -> _CodomainElement: ...
