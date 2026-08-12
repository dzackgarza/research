import builtins

# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Iterator
from typing import Any, Literal, TypeVar, overload

from sage.rings.integer import Integer
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.structure.parent import Parent

_Point = TypeVar("_Point")

class PermutationGroup_generic(Parent):
    def as_finitely_presented_group(self, reduced: bool = ...) -> FinitelyPresentedGroup: ...
    def order(self) -> Integer: ...
    def gens(self) -> tuple[Any, ...]: ...
    def ngens(self) -> int: ...
    def list(self) -> list[Any]: ...
    def __iter__(self) -> Iterator[Any]: ...
    def structure_description(self) -> str: ...
    def is_isomorphic(self, other: PermutationGroup_generic) -> bool: ...
    def orbit(
        self,
        point: tuple[_Point, ...],
        action: Literal["OnSets"],
    ) -> builtins.list[tuple[_Point, ...]]: ...  # builtins.: the class's own `list` method shadows the name here
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
