r"""Enumerated sets of functions, indexed by \(\mathbb N\) or by \(\mathbb Z\)."""

from operator import index as integer_index

from sage.categories.category import Category
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.sets.enumerated.enumerated_sets import (
    EnumeratedSets,
    InfiniteEnumeratedSets,
)
from dzack_research.preamble.categories.sets.set_categories import NN


def _nonnegative_integer(value, *, error_type):
    try:
        value = integer_index(value)
    except (TypeError, ValueError) as error:
        raise error_type(value) from error
    if value < 0:
        raise error_type(value)
    return ZZ(value)


def integer_from_natural(n):
    r"""The bijection \(\mathbb N\to\mathbb Z\) sending \(0,1,2,3,4,\ldots\) to \(0,1,-1,2,-2,\ldots\)."""
    n = _nonnegative_integer(n, error_type=IndexError)
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

        def _index_from_rank(self, position):
            return _nonnegative_integer(position, error_type=IndexError)

        def _rank_from_index(self, index):
            return _nonnegative_integer(index, error_type=ValueError)

        def function(self, index):
            return self.unrank(self._rank_from_index(index))


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

        def _index_from_rank(self, position):
            return integer_from_natural(position)

        def _rank_from_index(self, index):
            return natural_from_integer(index)

        def function(self, index):
            return self.unrank(self._rank_from_index(index))


class IndexedSymbolicFunctionSet(UniqueRepresentation, Parent):
    r"""An infinite function set represented by one formal symbol per index."""

    _indexing_category = None
    _symbol_prefix = None
    _latex_symbol_prefix = None

    def __init__(self) -> None:
        assert self._indexing_category is not None
        assert self._symbol_prefix is not None
        Parent.__init__(
            self,
            facade=SR,
            category=(FunctionEnumeratedSets(), self._indexing_category()),
        )

    def cardinality(self):
        return Infinity

    def _symbol_at_index(self, index):
        latex_prefix = (
            self._symbol_prefix
            if self._latex_symbol_prefix is None
            else self._latex_symbol_prefix
        )
        return indexed_symbol(self._symbol_prefix, index, latex_prefix)

    def _index_of_element(self, element):
        return index_of_symbol(
            element,
            self._symbol_prefix,
            self._latex_symbol_prefix,
        )

    def unrank(self, position):
        return self._symbol_at_index(self._index_from_rank(position))

    def rank(self, element):
        return self._rank_from_index(self._index_of_element(element))

    def __contains__(self, element):
        try:
            self.rank(element)
        except IndexError, TypeError, ValueError:
            return False
        return True

    def __iter__(self):
        position = 0
        while True:
            yield self.unrank(position)
            position += 1
