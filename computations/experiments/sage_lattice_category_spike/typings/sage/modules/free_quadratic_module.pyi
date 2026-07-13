# Repo-scoped stubs; see lexicon/README.md.
from sage.modules.free_module import FreeModule_generic
from sage.structure.element import Matrix


class FreeQuadraticModule_generic_pid(FreeModule_generic):
    def gram_matrix(self) -> Matrix: ...
