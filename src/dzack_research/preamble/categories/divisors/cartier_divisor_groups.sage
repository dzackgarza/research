r"""Cartier divisor groups."""

from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module

from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules
from dzack_research.preamble.refine import refine
from dzack_research.preamble.owned_category_bases import Category


def CartierDivisorGroup(module: "Module") -> "Module":
    r"""Refine the supplied framed module of Cartier divisors."""
    assert module in FramedModules(SageZZ), (
        "a Cartier divisor group must declare its framing at construction"
    )
    return refine(module, CartierDivisorGroups())


class CartierDivisorGroups(Category):
    r"""Framed \(\mathbb Z\)-modules of Cartier divisors."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "Cartier divisor groups"

    def super_categories(self) -> list:
        return [FramedModules(SageZZ)]
