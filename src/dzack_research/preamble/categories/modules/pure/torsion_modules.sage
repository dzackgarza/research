r"""Torsion modules over a base ring.

Defines ``TorsionModules`` as the category of torsion modules over a base ring $R$,
with no finite presentation or finite generation hypothesis.
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.modules import Modules


class TorsionModules(Category_over_base_ring):
    r"""Category of torsion modules over a base ring."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "torsion modules"

    def super_categories(self) -> list:
        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_torsion(self: Any) -> bool:
            r"""Return whether this module is torsion."""
            return True
