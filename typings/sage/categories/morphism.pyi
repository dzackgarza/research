# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Callable
from typing import Generic, Self, TypeVar

from sage.categories.category import Category
from sage.categories.map import Map
from sage.structure.element import Element
from sage.structure.parent import Parent

_DomainElement = TypeVar("_DomainElement", default=Element)
_CodomainElement = TypeVar("_CodomainElement", default=Element)
_SourceElement = TypeVar("_SourceElement")
_IdentityElement = TypeVar("_IdentityElement", default=Element)

class Morphism(Map[_DomainElement, _CodomainElement], Generic[_DomainElement, _CodomainElement]):
    def __init__(self, parent: Parent[Self]) -> None: ...
    # The domain and codomain of a morphism are objects of its category,
    # realized as Sage parents (verified on ring homomorphisms).
    def domain(self) -> Parent[_DomainElement]: ...
    def codomain(self) -> Parent[_CodomainElement]: ...
    def category_for(self) -> Category: ...
    # Map.__call__ converts into the domain before applying the morphism.
    # The coercion-free hook assumes x already lies in the domain.
    def _call_(self, x: _DomainElement) -> _CodomainElement: ...
    # Map.__mul__ is composition.
    def __mul__(
        self,
        right: Morphism[_SourceElement, _DomainElement],
    ) -> Morphism[_SourceElement, _CodomainElement]: ...

class IdentityMorphism(Morphism[_IdentityElement, _IdentityElement]): ...

class SetMorphism(Morphism[_DomainElement, _CodomainElement]):
    def __init__(
        self: Self,
        parent: Parent[Self],
        function: Callable[[_DomainElement], _CodomainElement],
    ) -> None: ...
