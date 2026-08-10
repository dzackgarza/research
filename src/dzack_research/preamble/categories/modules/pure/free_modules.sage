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
