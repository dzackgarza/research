r"""The enumerated set of Hermite polynomials \(\{H_n : n\in\mathbb N\}\).

Elements are formal symbols in \(\mathrm{SR}\), not evaluated
polynomials: \(H_0\) is the symbol, not the scalar \(1\).
"""

from sage.rings.infinity import Infinity
from sage.rings.semirings.non_negative_integer_semiring import NN
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByNaturals,
    FunctionEnumeratedSets,
    index_of_symbol,
    indexed_symbol,
)


class HermitePolynomials(UniqueRepresentation, Parent):
    r"""The enumerated set \(\{H_n : n\in\mathbb N\}\subset\mathrm{SR}\)."""

    def __init__(self) -> None:
        Parent.__init__(
            self,
            facade=SR,
            category=(FunctionEnumeratedSets(), EnumeratedByNaturals()),
        )

    def cardinality(self):
        return Infinity

    def unrank(self, n):
        if n not in NN:
            raise IndexError(n)
        return indexed_symbol("H", n, "H")

    def rank(self, elt):
        return index_of_symbol(elt, "H", "H")

    def __contains__(self, elt):
        try:
            self.rank(elt)
        except (TypeError, ValueError):
            return False
        return True

    def __iter__(self):
        n = 0
        while True:
            yield self.unrank(n)
            n += 1

    def _repr_(self) -> str:
        return "{H_n : n in NN}"
