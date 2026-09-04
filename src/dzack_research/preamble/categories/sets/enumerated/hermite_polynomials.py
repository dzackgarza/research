r"""The enumerated set of Hermite polynomials \(\{H_n : n\in\mathbb N\}\).

Elements are formal symbols in \(\mathrm{SR}\), not evaluated
polynomials: \(H_0\) is the symbol, not the scalar \(1\).
"""

from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByNaturals,
    IndexedSymbolicFunctionSet,
)


class HermitePolynomials(IndexedSymbolicFunctionSet):
    r"""The enumerated set \(\{H_n : n\in\mathbb N\}\subset\mathrm{SR}\)."""

    _indexing_category = EnumeratedByNaturals
    _symbol_prefix = "H"
    _latex_symbol_prefix = "H"

    def _repr_(self) -> str:
        return "{H_n : n in NN}"
