# Repo-scoped stubs; see lexicon/README.md.
#
# The image of a set under a map, as a set in its own right -- what the
# preamble returns where the lexicon noun ``Set`` is declared (a framed
# module's generators may be infinite, so the image object is the answer, not
# a coerced tuple). Declares the ``Sets.ParentMethods`` MRO edge, so it
# satisfies the noun.
from collections.abc import Callable, Iterator
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.sets_cat import Sets
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.parent import Parent

_DomainElement = TypeVar("_DomainElement")
_CodomainElement = TypeVar("_CodomainElement")

class ImageSubobject(
    Sets.ParentMethods[_CodomainElement],
    Generic[_DomainElement, _CodomainElement],
):
    def __init__(
        self,
        map: Map[_DomainElement, _CodomainElement]
        | Callable[[_DomainElement], _CodomainElement],
        domain_subset: Parent[_DomainElement],
        *,
        category: Category | None = ...,
        is_injective: bool | None = ...,
        inverse: Map[_CodomainElement, _DomainElement]
        | Callable[[_CodomainElement], _DomainElement]
        | None = ...,
    ) -> None: ...
    # Sage names the codomain of the defining map ``ambient`` here.
    def ambient(self) -> Parent[_CodomainElement] | None: ...
    def lift(self, x: _CodomainElement) -> _CodomainElement: ...
    def retract(self, x: _CodomainElement) -> _CodomainElement: ...
    # The image of an infinite domain may be infinite: over ZZ in QQ the
    # cardinality is +Infinity (verified), so Integer alone would be false.
    def cardinality(self) -> Integer | PlusInfinity: ...
    def __iter__(self) -> Iterator[_CodomainElement]: ...

class ImageSet(ImageSubobject[_DomainElement, _CodomainElement]): ...
