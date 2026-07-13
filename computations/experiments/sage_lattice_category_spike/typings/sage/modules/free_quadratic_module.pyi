# Repo-scoped stubs; see lexicon/README.md.
from sage.modules.free_module import FreeModule_generic
from sage.structure.element import Matrix


class FreeQuadraticModule_generic_pid(FreeModule_generic):
    # Sage leaves this unset until generator names are assigned.
    _names: tuple[str, ...] | None

    def gram_matrix(self) -> Matrix: ...
