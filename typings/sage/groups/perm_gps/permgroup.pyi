import builtins

# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Iterable, Iterator
from typing import Literal, TypeVar, overload

from sage.categories.groups import Groups
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.rings.integer import Integer
from sage.structure.parent import ElementConstructorInput

_Point = TypeVar("_Point")

class PermutationGroup_generic(Groups.ParentMethods[PermutationGroupElement]):
    def as_finitely_presented_group(self, reduced: bool = ...) -> FinitelyPresentedGroup: ...
    def order(self) -> Integer: ...
    def gens(self) -> tuple[PermutationGroupElement, ...]: ...
    def ngens(self) -> int: ...
    def list(self) -> list[PermutationGroupElement]: ...
    def __iter__(self) -> Iterator[PermutationGroupElement]: ...
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

type PermutationGroupGeneratorInput = (
    PermutationGroupElement | list[int] | tuple[int, ...] | ElementConstructorInput
)

def PermutationGroup(
    group_generators: Iterable[PermutationGroupGeneratorInput] | None = ...,
    *args: ElementConstructorInput,
    **kwds: ElementConstructorInput,
) -> PermutationGroup_generic: ...
