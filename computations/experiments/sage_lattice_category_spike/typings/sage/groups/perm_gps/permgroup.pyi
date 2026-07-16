# Repo-scoped stubs; see lexicon/README.md.
from typing import Any, Literal, TypeVar, overload

from sage.rings.integer import Integer
from sage.structure.parent import Parent

_Point = TypeVar("_Point")

class PermutationGroup_generic(Parent):
    def order(self) -> Integer: ...
    def gens(self) -> tuple[Any, ...]: ...
    def structure_description(self) -> str: ...
    def is_isomorphic(self, other: PermutationGroup_generic) -> bool: ...
    def orbits(self) -> Any: ...
    def orbit(
        self,
        point: tuple[_Point, ...],
        action: Literal["OnSets"],
    ) -> list[tuple[_Point, ...]]: ...
    @overload
    def direct_product(
        self,
        other: PermutationGroup_generic,
        maps: Literal[False],
    ) -> PermutationGroup_generic: ...
    @overload
    def direct_product(
        self,
        other: PermutationGroup_generic,
        maps: Literal[True] = True,
    ) -> tuple[PermutationGroup_generic, ...]: ...

def PermutationGroup(gens: Any = ..., *args: Any, **kwds: Any) -> PermutationGroup_generic: ...
