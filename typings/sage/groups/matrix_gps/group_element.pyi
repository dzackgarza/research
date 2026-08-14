# Repo-scoped stubs; see lexicon/README.md.
from typing import TYPE_CHECKING

from sage.libs.gap.element import GapElement

#
# An element of a matrix group IS a group element, and its matrix is read off
# by asking for it -- the group element and the matrix are different objects
# (the same distinction the lexicon draws between a morphism and its
# MorphismMatrix, INVENTORY.md I.4).
from sage.structure.element import Matrix, MultiplicativeGroupElement

if TYPE_CHECKING:
    from sage.groups.matrix_gps.finitely_generated_gap import (
        FinitelyGeneratedMatrixGroup_gap,
    )

class MatrixGroupElement_base(MultiplicativeGroupElement):
    def matrix(self) -> Matrix: ...

class MatrixGroupElement_gap(MatrixGroupElement_base):
    def parent(self) -> FinitelyGeneratedMatrixGroup_gap: ...
    # The libGAP conversion protocol: GAP class functions evaluate on these.
    def gap(self) -> GapElement: ...
