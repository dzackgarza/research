from typing import TYPE_CHECKING

from sage.structure.element import MultiplicativeGroupElement

if TYPE_CHECKING:
    from sage.groups.perm_gps.permgroup import PermutationGroup_generic

class PermutationGroupElement(MultiplicativeGroupElement):
    def parent(self) -> PermutationGroup_generic: ...

class SymmetricGroupElement(PermutationGroupElement): ...
