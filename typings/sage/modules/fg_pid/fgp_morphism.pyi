# Repo-scoped stubs; see lexicon/README.md.
from typing import Generic, TypeVar

from sage.categories.morphism import Morphism
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class FGP_Morphism(Morphism[FGP_Element, FGP_Element], Generic[_Scalar]):
    def kernel(self) -> FGP_Module_class[_Scalar]: ...
    def image(self) -> FGP_Module_class[_Scalar]: ...
    # A is a submodule of the codomain; the result is a submodule of the domain.
    def inverse_image(
        self,
        submodule: FGP_Module_class[_Scalar],
    ) -> FGP_Module_class[_Scalar]: ...
    # A preimage element in the domain (ValueError when x has none) -- unlike
    # FGP_Element.lift, which lifts to the cover V.
    def lift(self, x: FGP_Element) -> FGP_Element: ...
