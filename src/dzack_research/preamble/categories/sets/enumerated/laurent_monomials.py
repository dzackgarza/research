r"""The enumerated set of Laurent monomials \(\{z^n : n\in\mathbb Z\}\).

Elements are formal symbols in \(\mathrm{SR}\), not evaluated powers:
\(z^0\) is the symbol, not the scalar \(1\).
"""

from sage.rings.infinity import Infinity
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByIntegers,
    FunctionEnumeratedSets,
    index_of_symbol,
    indexed_symbol,
    integer_from_natural,
    natural_from_integer,
)


class LaurentMonomials(UniqueRepresentation, Parent):
    r"""The enumerated set \(\{z^n : n\in\mathbb Z\}\subset\mathrm{SR}\)."""

    def __init__(self) -> None:
        Parent.__init__(
            self,
            facade=SR,
            category=(FunctionEnumeratedSets(), EnumeratedByIntegers()),
        )

    def cardinality(self):
        return Infinity

    def unrank(self, n):
        return indexed_symbol("z", integer_from_natural(n), "z")

    def rank(self, elt):
        return natural_from_integer(index_of_symbol(elt, "z", "z"))

    def __contains__(self, elt):
        try:
            self.rank(elt)
        except (TypeError, ValueError):
            return False
        return True

    def __iter__(self):
        index = 0
        while True:
            yield self.unrank(index)
            index += 1

    def _repr_(self) -> str:
        return "{z^n : n in ZZ}"
