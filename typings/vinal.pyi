# Repo-scoped stubs; see lexicon/README.md.
#
# The vendored Vinberg-algorithm clone (computations/vendor/): typed with the
# surface hyperbolic_lattices.sage consumes. FindRoots reports whether the
# fundamental polyhedron was established; roots are coordinate rows in the
# basis the Gram matrix was given in.
from collections.abc import Sequence

from sage.structure.element import Matrix, Vector

class VinAl:
    roots: Sequence[Sequence[object]]
    def __init__(
        self, gram: Matrix, v0: Vector | None = ..., use_coxiter: bool = ..., output: object = ...
    ) -> None: ...
    def FindRoots(
        self,
        max_roots: object = ...,
        max_decompositions: object = ...,
        progress: object = ...,
    ) -> bool: ...
