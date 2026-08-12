# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Iterable, Sequence

from sage.groups.matrix_gps.isometries import GroupOfIsometries
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
from sage.rings.integer import Integer
from sage.structure.element import Matrix

class FreeQuadraticModule_integer_symmetric(FreeModule_generic):
    def gram_matrix(self) -> Matrix: ...
    def discriminant_group(self, s: int = ...) -> TorsionQuadraticModule: ...
    # O(L) as a matrix group of isometries; Sage's generators V satisfy
    # V G V^T = G (the transpose of the U^T G U = G convention).
    def orthogonal_group(
        self,
        gens: Iterable[Matrix] | None = ...,
        is_finite: bool | None = ...,
    ) -> GroupOfIsometries: ...
    def signature_pair(self) -> tuple[int, int]: ...

# The descriptor is a Gram matrix, a Euclidean rank, a Cartan type for a root
# lattice, or "U"/"H" for the hyperbolic plane.
def IntegralLattice(
    data: Matrix | int | Integer | str | Sequence[object],
    basis: Matrix | Sequence[FreeModuleElement] | None = ...,
) -> FreeQuadraticModule_integer_symmetric: ...
