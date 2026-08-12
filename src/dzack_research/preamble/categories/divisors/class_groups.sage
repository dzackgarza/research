r"""Weil divisor class groups."""

from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Module

from sage.categories.modules import Modules
from dzack_research.preamble.refine import refine
from sage.categories.category import Category


def ClassGroup(module: "Module") -> "Module":
    r"""Refine the specified framed quotient module as \(\operatorname{Cl}(X)\)."""
    assert module in Modules(SageZZ).Framed(), (
        "a class group must declare its quotient framing at construction"
    )
    return refine(module, ClassGroups())


class ClassGroups(Category):
    r"""Framed \(\mathbb Z\)-modules of Weil divisor classes."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "class groups"

    def super_categories(self) -> list:
        return [Modules(SageZZ).Framed()]
