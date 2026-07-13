# Repo-scoped stubs; see lexicon/README.md.
from typing import Any, Literal, TypeVar

from sage.rings.integer import Integer
from sage.structure.parent import Parent

_Point = TypeVar("_Point")

class PermutationGroup_generic(Parent):
    def order(self) -> Integer: ...
    def gens(self) -> tuple[Any, ...]: ...
    def structure_description(self) -> str: ...
    def is_isomorphic(self, other: PermutationGroup_generic) -> bool: ...
    def orbit(
        self,
        point: tuple[_Point, ...],
        action: Literal["OnSets"],
    ) -> list[tuple[_Point, ...]]: ...

def PermutationGroup(gens: Any = ..., *args: Any, **kwds: Any) -> PermutationGroup_generic: ...
