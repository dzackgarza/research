r"""Free modules over a base ring."""

from sage.categories.category_types import Category_over_base_ring
from sage.categories.modules import Modules
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet


class FreeModules(Category_over_base_ring):
    r"""Category of free modules over a base ring, without a chosen basis."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free modules"

    def super_categories(self) -> list:
        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            r"""Return whether this module is free."""
            return True
