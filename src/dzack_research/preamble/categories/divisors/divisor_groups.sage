r"""Divisor groups as framed free \(\mathbb Z\)-modules."""

from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module

from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.refine import refine
from dzack_research.preamble.owned_category_bases import Category


def DivisorGroup(module: "Module") -> "Module":
    r"""Refine the declared free module of divisors."""
    assert module in FramedFreeModules(SageZZ), (
        "a divisor group is constructed from its actual set of prime divisors"
    )
    return refine(module, DivisorGroups())


class DivisorGroups(Category):
    r"""Free abelian groups on specified prime divisors."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "divisor groups"

    def super_categories(self) -> list:
        return [FramedFreeModules(SageZZ)]
