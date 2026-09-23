r"""The enumerated set of Shannon sinc translates \(\{\operatorname{sinc}(\,\cdot\,-n):n\in\mathbb Z\}\).

Elements are formal symbols in \(\mathrm{SR}\), not evaluated sinc
functions. This set does not compute integrals or \(L^2\) Gram matrices.
"""

from sage.misc.cachefunc import cached_function
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByIntegers,
    FunctionEnumeratedSets,
)


@cached_function
def SincTranslates() -> Parent:
    r"""The enumerated set \(\{\operatorname{sinc}(\,\cdot\,-n):n\in\mathbb Z\}\subset\mathrm{SR}\).

    Each translate is the formal symbol \(\mathrm{sinc}_n\), not Sage's
    evaluated \(\operatorname{sinc}\).
    """
    return FunctionEnumeratedSets()(
        "sinc",
        r"\mathrm{sinc}",
        "{sinc(· - n) : n in ZZ}",
        indexing=EnumeratedByIntegers(),
    )
