r"""Torsion modules over a base ring.

Defines ``TorsionModules`` as the category of torsion modules over a base ring $R$,
with no finite presentation or finite generation hypothesis.
"""


from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from typing import Self

from dzack_research.preamble.categories.modules.pure.modules import Modules


class TorsionModules(OwnedCategoryOverBaseRing):
    r"""Category of torsion modules over a base ring."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "torsion modules"

    def super_categories(self) -> list:
        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_torsion(self: Self) -> bool:
            r"""Return whether this module is torsion."""
            return True
