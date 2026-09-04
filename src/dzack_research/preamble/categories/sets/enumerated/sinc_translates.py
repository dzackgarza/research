r"""The enumerated set of Shannon sinc translates \(\{\operatorname{sinc}(\,\cdot\,-n):n\in\mathbb Z\}\).

Elements are formal symbols in \(\mathrm{SR}\), not evaluated sinc
functions. This set does not compute integrals or \(L^2\) Gram matrices.
"""

from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByIntegers,
    IndexedSymbolicFunctionSet,
)


class SincTranslates(IndexedSymbolicFunctionSet):
    r"""The enumerated set \(\{\operatorname{sinc}(\,\cdot\,-n):n\in\mathbb Z\}\subset\mathrm{SR}\).

    Each translate is the formal symbol \(\mathrm{sinc}_n\), not Sage's
    evaluated \(\operatorname{sinc}\).
    """

    _indexing_category = EnumeratedByIntegers
    _symbol_prefix = "sinc"
    _latex_symbol_prefix = r"\mathrm{sinc}"

    def _repr_(self) -> str:
        return "{sinc(· - n) : n in ZZ}"
