"""Free modules over a base ring."""

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing


class FreeModules(OwnedCategoryOverBaseRing):
    r"""Modules admitting a basis."""

    @classmethod
    def _repr_object_names(cls):
        return "free modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            return True
