r"""Cartier divisor groups."""

from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Module

from sage.categories.modules import Modules
from dzack_research.preamble.refine import refine
from sage.categories.category import Category


def CartierDivisorGroup(module: "Module") -> "Module":
    r"""Refine the supplied framed module of Cartier divisors."""
    assert module in Modules(SageZZ).Framed(), (
        "a Cartier divisor group must declare its framing at construction"
    )
    return refine(module, CartierDivisorGroups())


class CartierDivisorGroups(Category):
    r"""Framed \(\mathbb Z\)-modules of Cartier divisors."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "Cartier divisor groups"

    def super_categories(self) -> list:
        return [Modules(SageZZ).Framed()]
