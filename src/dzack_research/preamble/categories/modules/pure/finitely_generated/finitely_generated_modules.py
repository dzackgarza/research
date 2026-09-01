"""Finitely generated modules."""

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing


class FinitelyGeneratedModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely generated modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_finitely_generated(self) -> bool:
            return True

        def free_resolution(self):
            from dzack_research.preamble.categories.modules.free_resolutions import free_resolution

            return free_resolution(self)
