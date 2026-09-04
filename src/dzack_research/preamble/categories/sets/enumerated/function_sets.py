r"""Enumerated sets of functions, indexed by \(\mathbb N\) or by \(\mathbb Z\)."""

from sage.categories.category import Category
from sage.rings.integer_ring import ZZ
from dzack_research.preamble.categories.sets.set_categories import NN
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.sets.enumerated.enumerated_sets import (
    EnumeratedSets,
    InfiniteEnumeratedSets,
)


def integer_from_natural(n):
    r"""The bijection \(\mathbb N\to\mathbb Z\) sending \(0,1,2,3,4,\ldots\) to \(0,1,-1,2,-2,\ldots\)."""
    n = ZZ(n)
    if n == 0:
        return ZZ(0)
    if n % 2 == 1:
        return (n + 1) // 2
    return -n // 2


def natural_from_integer(k):
    r"""The inverse of :func:`integer_from_natural`."""
    k = ZZ(k)
    if k == 0:
        return ZZ(0)
    if k > 0:
        return 2 * k - 1
    return -2 * k


def indexed_symbol(prefix: str, index, latex_prefix: str):
    r"""The symbol in \(\mathrm{SR}\) for this prefix and integer index."""
    index = ZZ(index)
    if index >= 0:
        name = f"{prefix}_{index}"
    else:
        name = f"{prefix}_m{-index}"
    return SR.var(name, latex_name=rf"{latex_prefix}_{{{index}}}")


def index_of_symbol(elt, prefix: str, latex_prefix: str | None = None):
    r"""Return \(n\) when ``elt`` is the indexed symbol of this prefix."""
    if elt not in SR:
        raise ValueError(elt)
    symbol = SR(elt)
    if not symbol.is_symbol():
        raise ValueError(elt)
    text = str(symbol)
    head = f"{prefix}_"
    if not text.startswith(head):
        raise ValueError(elt)
    rest = text[len(head) :]
    if rest.startswith("m") and rest[1:].isdigit():
        index = -ZZ(rest[1:])
    elif rest.isdigit():
        index = ZZ(rest)
    else:
        raise ValueError(elt)
    latex = prefix if latex_prefix is None else latex_prefix
    if symbol != indexed_symbol(prefix, index, latex):
        raise ValueError(elt)
    return index


class FunctionEnumeratedSets(Category):
    r"""Enumerated sets whose elements stand for functions."""

    def super_categories(self):
        return [EnumeratedSets()]


class EnumeratedByNaturals(Category):
    r"""Infinite enumerated sets ranked by \(\mathbb N\)."""

    def super_categories(self):
        return [InfiniteEnumeratedSets()]

    class ParentMethods:
        def index_set(self):
            return NN

        def function(self, index):
            return self.unrank(int(index))


class EnumeratedByIntegers(Category):
    r"""Infinite enumerated sets whose functions are indexed by \(\mathbb Z\).

    Sage's ranking still runs through \(\mathbb N\); :meth:`function` takes the
    integer index, and :meth:`unrank` takes the corresponding natural number.
    """

    def super_categories(self):
        return [InfiniteEnumeratedSets()]

    class ParentMethods:
        def index_set(self):
            return ZZ

        def function(self, index):
            return self.unrank(natural_from_integer(index))
