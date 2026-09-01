"""Projective modules."""

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing


class ProjectiveModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "projective modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_projective(self) -> bool:
            return True

        def projective_rank(self, point):
            r"""Return the local free rank of a finite projective module at ``point``."""
            from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import (
                FinitelyGeneratedModules,
            )

            if self not in FinitelyGeneratedModules(self.base_ring()):
                raise TypeError("projective_rank currently requires a finite projective module")
            return self.fiber_dimension(point)
