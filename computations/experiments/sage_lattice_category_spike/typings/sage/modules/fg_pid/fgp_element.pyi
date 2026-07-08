# Repo-scoped stubs; see lexicon/README.md.
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import ModuleElement

class FGP_Element(ModuleElement):
    def lift(self) -> FreeModuleElement: ...
