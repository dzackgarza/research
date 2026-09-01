"""Finite-rank free modules with a chosen ordered basis."""

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing
from sage.rings.integer import Integer


class FinitelyGeneratedFreeModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely generated free modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            FinitelyPresentedModules,
        )
        from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import (
            FinitelyGeneratedModules,
        )
        from dzack_research.preamble.categories.modules.pure.projective_modules import ProjectiveModules

        return [
            FramedFreeModules(self.base_ring()),
            FinitelyGeneratedModules(self.base_ring()),
            FinitelyPresentedModules(self.base_ring()),
            ProjectiveModules(self.base_ring()),
        ]

    class ParentMethods:
        def dual_module(self):
            r"""Return the selected dual free module on the dual basis."""
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FreeModuleOn,
            )

            return FreeModuleOn(self.base_ring(), self.module_generating_set())

        def determinant_line(self):
            from dzack_research.preamble.categories.modules.hodge import DeterminantLine

            return DeterminantLine(self)

        def exterior_forms(self, degree):
            from dzack_research.preamble.categories.modules.hodge import ExteriorForms

            return ExteriorForms(self, degree)

        def volume_trivialization(self, forward, inverse):
            from dzack_research.preamble.categories.modules.hodge import VolumeTrivialization

            return VolumeTrivialization(self, forward, inverse)

        def framing_volume_trivialization(self, unit=None):
            from dzack_research.preamble.categories.modules.hodge import (
                FramingVolumeTrivialization,
            )

            return FramingVolumeTrivialization(self, unit=unit)

        def poincare_duality(self, volume, degree):
            from dzack_research.preamble.categories.modules.hodge import PoincareDuality

            return PoincareDuality(self, volume, degree)


def BasedFreeModule(base_ring, rank_or_labels):
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreeModule,
        FreeModuleOn,
    )

    if isinstance(rank_or_labels, (int, Integer)):
        return FreeModule(base_ring, rank_or_labels)
    return FreeModuleOn(base_ring, rank_or_labels)
