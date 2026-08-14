# Repo-scoped stubs; see lexicon/README.md.
#
# ``Set`` here is honestly Sage's CONSTRUCTOR (a factory function); the class
# of its values is Set_object, which declares the Sets.ParentMethods MRO edge
# and so realizes the lexicon noun ``Set``. The preamble imports this under
# the name ``SageSet`` precisely because the bare name is the noun
# (INVENTORY.md II.5 / naming rule IV.3).
from collections.abc import Iterable, Iterator
from typing import overload

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent

class Set_generic(Parent[Element]): ...

class Set_object(Set_generic, Sets.ParentMethods[Element]):
    # A set can be infinite: Set(ZZ) has cardinality +Infinity (verified), so
    # Integer alone would be false; finite sets answer their Integer count.
    def cardinality(self) -> Integer | PlusInfinity: ...
    def __iter__(self) -> Iterator[Element]: ...
    def __contains__(self, x: object) -> bool: ...
    def union(self, other: Set_object) -> Set_object: ...
    def intersection(self, other: Set_object) -> Set_object: ...
    def difference(self, other: Set_object) -> Set_object: ...

class Set_object_enumerated(Set_object):
    def list(self) -> list[Element]: ...
    def __len__(self) -> int: ...

# A finite iterable enumerates (which is why len() works on the result);
# a parent stays a general set object.
@overload
def Set(X: Iterable[Element], category: Category | None = ...) -> Set_object_enumerated: ...
@overload
def Set(X: Parent | None = ..., category: Category | None = ...) -> Set_object: ...
