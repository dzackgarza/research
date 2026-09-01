"""The enumerated set of Fourier characters as formal symbols in SR."""

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


class FourierCharacters(UniqueRepresentation, Parent):
    r"""The enumerated set \(\{e^{i n x} : n\in\mathbb Z\}\) as symbols \(F_n\in\mathrm{SR}\).

    Each character is the formal symbol \(F_n\), not an evaluated
    exponential, so \(F_0\) does not collapse to \(1\).
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
        return indexed_symbol("F", integer_from_natural(n), "F")

    def rank(self, elt):
        return natural_from_integer(index_of_symbol(elt, "F", "F"))

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
        return "{e^{i n x} : n in ZZ}"
