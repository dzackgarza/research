"""The enumerated set of Fourier characters as formal symbols in SR."""

from sage.misc.cachefunc import cached_function
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.enumerated.function_sets import (
    EnumeratedByIntegers,
    FunctionEnumeratedSets,
)


@cached_function
def FourierCharacters() -> Parent:
    r"""The enumerated set \(\{e^{i n x} : n\in\mathbb Z\}\) as symbols \(F_n\in\mathrm{SR}\).

    Each character is the formal symbol \(F_n\), not an evaluated
    exponential, so \(F_0\) does not collapse to \(1\).
    """
    return FunctionEnumeratedSets()(
        "F",
        "F",
        "{e^{i n x} : n in ZZ}",
        indexing=EnumeratedByIntegers(),
    )
