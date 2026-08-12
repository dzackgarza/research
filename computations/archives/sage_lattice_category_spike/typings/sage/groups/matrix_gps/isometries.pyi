# Repo-scoped stubs; see lexicon/README.md.
#
# O(L) for an integral lattice: the group Sage returns from
# ``IntegralLattice.orthogonal_group``. It is a matrix group (the declared MRO
# edge is the true one) that additionally remembers the form it preserves.
from sage.groups.matrix_gps.finitely_generated_gap import (
    FinitelyGeneratedMatrixGroup_gap,
)
from sage.structure.element import Matrix

class GroupOfIsometries(FinitelyGeneratedMatrixGroup_gap):
    def invariant_bilinear_form(self) -> Matrix: ...
