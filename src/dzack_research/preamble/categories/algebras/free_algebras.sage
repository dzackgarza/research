r"""Free algebras over a base ring, without a chosen generating set."""

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing



class FreeAlgebras(OwnedCategoryOverBaseRing):
    r"""Category of free commutative algebras over a base ring, without a chosen algebra_generators."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free algebras"

    def super_categories(self) -> list:
        # Local: both nodes import this module, so module-level imports here
        # would close those cycles; the modules are built by call time.
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.modules.pure.free_modules import FreeModules

        # Free *commutative* algebra: the monomials come from the free
        # abelian monoid, so xy = yx holds by construction and the axiom is
        # a declaration, not a claim to be checked.
        return [
            Algebras(self.base_ring()).Commutative(),
            FreeModules(self.base_ring()),
        ]

    class SubcategoryMethods:
        def on(self, algebra_generating_set):
            r"""Return the free algebra on ``algebra_generating_set``."""
            # Local: framed_free_algebras imports this module, so a
            # module-level import here would close that cycle.
            from dzack_research.preamble.categories.algebras.framed_free_algebras import FreeAlgebraOn

            return FreeAlgebraOn(self.base_ring(), algebra_generating_set)

    class ParentMethods:
        def is_free(self) -> bool:
            r"""Return whether this algebra is free."""
            return True
