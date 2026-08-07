# Repo-scoped stubs; see lexicon/README.md.
#
# ``Set`` here is honestly Sage's CONSTRUCTOR (a factory function); the class
# of its values is Set_object, which declares the Sets.ParentMethods MRO edge
# and so realizes the lexicon noun ``Set``. The preamble imports this under
# the name ``SageSet`` precisely because the bare name is the noun
# (INVENTORY.md II.5 / naming rule IV.3).
from collections.abc import Iterable, Iterator

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent

class Set_object(Sets.ParentMethods[Element], Parent[Element]):
    def cardinality(self) -> Integer: ...
    def __iter__(self) -> Iterator[Element]: ...
    def __contains__(self, x: object) -> bool: ...
    def union(self, other: Set_object) -> Set_object: ...
    def intersection(self, other: Set_object) -> Set_object: ...
    def difference(self, other: Set_object) -> Set_object: ...

class Set_object_enumerated(Set_object):
    def list(self) -> list[Element]: ...

def Set(
    X: Parent | Iterable[Element] | None = ...,
    category: Category | None = ...,
) -> Set_object: ...
