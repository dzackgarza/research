from typing import Generic, TypeVar

from sage.categories.enumerated_sets import EnumeratedSets
from sage.rings.integer import Integer

_E = TypeVar("_E")

class FiniteEnumeratedSets(EnumeratedSets):
    class ParentMethods(EnumeratedSets.ParentMethods[_E], Generic[_E]):
        def __len__(self) -> int: ...
        def cardinality(self) -> Integer: ...
