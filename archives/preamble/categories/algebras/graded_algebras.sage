r"""Graded algebras: \(A=\bigoplus_nA_n\) with \(A_iA_j\subseteq A_{i+j}\).

Split out of the graded-modules node: the module half of the grading lives
with the modules, and the algebra category lives beside its consumers here.
"""

from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing


class GradedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras \(A=\bigoplus_nA_n\) with \(A_iA_j\subseteq A_{i+j}\).

    The grading is compatible with the product, which is what makes the degree
    additive and each \(A_n\) a module over \(A_0\).  Every free construction
    in the preamble is one of these: the degree of a monomial is the number of
    letters it has, however that construction spells them.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "graded algebras"

    def super_categories(self) -> list:
        # Local: the algebra node reaches this one, so a module-level import
        # would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return [GradedModules(self.base_ring()), Algebras(self.base_ring())]
