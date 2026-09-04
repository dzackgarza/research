"""The enumerated set of Fourier characters as formal symbols in SR."""

from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByIntegers,
    IndexedSymbolicFunctionSet,
)


class FourierCharacters(IndexedSymbolicFunctionSet):
    r"""The enumerated set \(\{e^{i n x} : n\in\mathbb Z\}\) as symbols \(F_n\in\mathrm{SR}\).

    Each character is the formal symbol \(F_n\), not an evaluated
    exponential, so \(F_0\) does not collapse to \(1\).
    """

    _indexing_category = EnumeratedByIntegers
    _symbol_prefix = "F"
    _latex_symbol_prefix = "F"

    def _repr_(self) -> str:
        return "{e^{i n x} : n in ZZ}"
