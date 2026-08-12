r"""Weil divisor groups."""

from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Module

from dzack_research.preamble.categories.divisors.divisor_groups import DivisorGroups
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.refine import refine
from sage.categories.category import Category


def WeilDivisorGroup(module: "Module") -> "Module":
    r"""Refine the free module on the actual codimension-one subvarieties."""
    assert module in FramedFreeModules(SageZZ), (
        "WeilDiv(X) is free on its specified set of prime divisors"
    )
    return refine(module, WeilDivisorGroups())


class WeilDivisorGroups(Category):
    r"""Free abelian groups on codimension-one subvarieties."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "Weil divisor groups"

    def super_categories(self) -> list:
        return [DivisorGroups()]
