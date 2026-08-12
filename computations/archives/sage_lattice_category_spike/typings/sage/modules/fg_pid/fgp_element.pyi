# Repo-scoped stubs; see lexicon/README.md.
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import ModuleElement

class FGP_Element(ModuleElement):
    # A representative in the covering module V.
    def lift(self) -> FreeModuleElement: ...
    # Coordinates with respect to the module's own (invariant-factor)
    # generators -- not coordinates in the cover.
    def vector(self) -> FreeModuleElement: ...
