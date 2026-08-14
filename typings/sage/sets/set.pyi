# Repo-scoped stubs; see lexicon/README.md.
#
# ``Set`` here is honestly Sage's CONSTRUCTOR (a factory function); the class
# of its values is Set_object, which declares the Sets.ParentMethods MRO edge
# and so realizes the lexicon noun ``Set``. The preamble imports this under
# the name ``SageSet`` precisely because the bare name is the noun
# (INVENTORY.md II.5 / naming rule IV.3).
from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar, overload

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import MembershipInput, Parent

_E = TypeVar("_E", default=Element, covariant=True)

class Set_generic(Parent[_E], Generic[_E]): ...

class Set_object(Set_generic[_E], Sets.ParentMethods[_E], Generic[_E]):
    # A set can be infinite: Set(ZZ) has cardinality +Infinity (verified), so
    # Integer alone would be false; finite sets answer their Integer count.
    def cardinality(self) -> Integer | PlusInfinity: ...
    def __iter__(self) -> Iterator[_E]: ...
    def __contains__(self, x: MembershipInput) -> bool: ...
    def union(self, other: Set_object[_E]) -> Set_object[_E]: ...
    def intersection(self, other: Set_object[_E]) -> Set_object[_E]: ...
    def difference(self, other: Set_object[_E]) -> Set_object[_E]: ...

class Set_object_enumerated(Set_object[_E], Generic[_E]):
    def list(self) -> list[_E]: ...
    def __len__(self) -> int: ...

# A finite iterable enumerates (which is why len() works on the result);
# a parent stays a general set object.
@overload
def Set(X: Iterable[_E], category: Category | None = ...) -> Set_object_enumerated[_E]: ...
@overload
def Set(X: Parent[_E], category: Category | None = ...) -> Set_object[_E]: ...
@overload
def Set(X: None = ..., category: Category | None = ...) -> Set_object[Element]: ...
