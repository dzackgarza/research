# Repo-scoped stubs; see lexicon/README.md.
#
# Minimal honest stub for the morphism class FreeModule_generic.hom returns
# (free_module_morphism.py:51). ``kernel`` is defined on the ancestor
# MatrixMorphism_abstract (matrix_morphism.py:835) and returns a submodule of
# the domain, so it is declared flat here per the flat-first decision.
from typing import Literal

from sage.categories.morphism import Morphism
from sage.modules.free_module import FreeModule_generic
from sage.structure.element import Matrix

class FreeModuleMorphism(Morphism):
    def kernel(self) -> FreeModule_generic: ...
    # matrix_morphism.py:885 — a submodule of the codomain.
    def image(self) -> FreeModule_generic: ...
    # MatrixMorphism.matrix (matrix_morphism.py:1566) — the defining matrix.
    def matrix(self, side: Literal["left", "right"] | None = ...) -> Matrix: ...
