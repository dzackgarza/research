r"""Free algebras over a base ring, without a chosen generating set."""

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing



class FreeAlgebras(OwnedCategoryOverBaseRing):
    r"""Category of free commutative algebras over a base ring, without a chosen algebra_generators."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free algebras"

    def super_categories(self) -> list:
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
            return FreeAlgebraOn(self.base_ring(), algebra_generating_set)

    class ParentMethods:
        def is_free(self) -> bool:
            r"""Return whether this algebra is free."""
            return True
