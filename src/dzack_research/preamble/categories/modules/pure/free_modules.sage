r"""Free modules over a base ring."""


from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from sage.categories.modules import Modules


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
