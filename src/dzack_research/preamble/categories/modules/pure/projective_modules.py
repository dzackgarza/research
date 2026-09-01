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
