r"""Weil divisor class groups."""

from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module

from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules
from dzack_research.preamble.refine import refine
from sage.categories.category import Category


def ClassGroup(module: "Module") -> "Module":
    r"""Refine the specified framed quotient module as \(\operatorname{Cl}(X)\)."""
    assert module in FramedModules(SageZZ), (
        "a class group must declare its quotient framing at construction"
    )
    return refine(module, ClassGroups())


class ClassGroups(Category):
    r"""Framed \(\mathbb Z\)-modules of Weil divisor classes."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "class groups"

    def super_categories(self) -> list:
        return [FramedModules(SageZZ)]
