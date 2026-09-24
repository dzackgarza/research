r"""The enumerated set of Hermite polynomials \(\{H_n : n\in\mathbb N\}\).

Elements are formal symbols in \(\mathrm{SR}\), not evaluated
polynomials: \(H_0\) is the symbol, not the scalar \(1\).
"""

from sage.misc.cachefunc import cached_function
from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByNaturals,
    FunctionEnumeratedSets,
)
from dzack_research.preamble.lexicon.set_theory import SetObject


@cached_function
def HermitePolynomials() -> SetObject:
    r"""The enumerated set \(\{H_n : n\in\mathbb N\}\subset\mathrm{SR}\)."""
    return FunctionEnumeratedSets()(
        "H",
        "H",
        "{H_n : n in NN}",
        indexing=EnumeratedByNaturals(),
    )
