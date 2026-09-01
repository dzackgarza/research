r"""The enumerated set of Shannon sinc translates \(\{\operatorname{sinc}(\,\cdot\,-n):n\in\mathbb Z\}\).

Elements are formal symbols in \(\mathrm{SR}\), not evaluated sinc
functions. This set does not compute integrals or \(L^2\) Gram matrices.
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


class SincTranslates(UniqueRepresentation, Parent):
    r"""The enumerated set \(\{\operatorname{sinc}(\,\cdot\,-n):n\in\mathbb Z\}\subset\mathrm{SR}\).

    Each translate is the formal symbol \(\mathrm{sinc}_n\), not Sage's
    evaluated \(\operatorname{sinc}\).
    """

    def __init__(self) -> None:
        Parent.__init__(
            self,
            facade=SR,
            category=(FunctionEnumeratedSets(), EnumeratedByIntegers()),
        )

    def cardinality(self):
        return Infinity

    def unrank(self, n):
        return indexed_symbol("sinc", integer_from_natural(n), r"\mathrm{sinc}")

    def rank(self, elt):
        return natural_from_integer(
            index_of_symbol(elt, "sinc", r"\mathrm{sinc}")
        )

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
        return "{sinc(· - n) : n in ZZ}"
