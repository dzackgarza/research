r"""Free modules over a base ring."""


from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from typing import TYPE_CHECKING

from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category_over_base_ring
from dzack_research.preamble.categories.modules.pure.modules import Modules

if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData


class FreeModules(OwnedCategoryOverBaseRing):
    r"""Category of free modules over a base ring, without a chosen module_generators."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free modules"

    def super_categories(self) -> list:
        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            r"""Return whether this module is free."""
            return True

        def is_torsion_free(self) -> bool:
            r"""Free \(\Rightarrow\) torsion-free, over an integral domain.

            The implication is a theorem *with a hypothesis*: in a free
            module over a domain, \(r\cdot m = 0\) with \(r\neq 0\) forces
            \(m = 0\) coordinatewise.  Over a base with zero divisors the
            statement depends on which torsion convention is in force, so
            the hypothesis is asserted rather than silently assumed.
            """
            assert self.base_ring().is_integral_domain(), (
                f"free => torsion-free is a theorem over an integral "
                f"domain; {self.base_ring()} is not one, and this node "
                "states no torsion answer there"
            )
            return True


class FiniteRankFreeModules(Category_over_base_ring):
    r"""The free module on the standard ordered set of cardinality \(n\).

    Its underlying set is the set of finitely supported functions from that
    standard set into \(R\).  Since the domain is finite, this set is
    equinumerous with \(R^n\).  It is not an object of the category of actual
    cartesian-product sets, and its elements remain module elements.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free modules of finite rank"

    def super_categories(self) -> list:
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules

        return [FinitelyGeneratedFreeModules(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            rank: "Integer",
            **rest: "ConstructionData",
        ) -> None:
            assert rank >= 0, "a free module has nonnegative rank"
            super().__init__(module_generating_set=rank, **rest)

        def _repr_(self) -> str:
            return f"{self.base_ring()}^{self.rank()}"

def FreeModuleOfRank(base_ring: "Ring", rank: "Integer") -> "Parent":
    r"""Return \(R^n\), built through the chain."""
    return object_of(FiniteRankFreeModules(base_ring), rank=rank)
