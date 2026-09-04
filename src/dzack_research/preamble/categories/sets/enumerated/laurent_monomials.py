r"""The enumerated set of Laurent monomials \(\{z^n : n\in\mathbb Z\}\).

Elements are formal symbols in \(\mathrm{SR}\), not evaluated powers:
\(z^0\) is the symbol, not the scalar \(1\).
"""

from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByIntegers,
    IndexedSymbolicFunctionSet,
)


class LaurentMonomials(IndexedSymbolicFunctionSet):
    r"""The enumerated set \(\{z^n : n\in\mathbb Z\}\subset\mathrm{SR}\)."""

    _indexing_category = EnumeratedByIntegers
    _symbol_prefix = "z"
    _latex_symbol_prefix = "z"

    def _repr_(self) -> str:
        return "{z^n : n in ZZ}"
