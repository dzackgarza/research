"""Owned indexed families of mathematical values."""

from sage.structure.sage_object import SageObject


class IndexedFamily(SageObject):
    r"""A family ``(x_i)_{i in I}`` retaining its indexing set.

    A family is not the set of its values: different indices may have equal
    values.  It therefore has no inverse ``rank(value)`` operation in general.
    Consumers iterate values lazily or address them through ``value(index)``.
    """

    def __init__(self, index_set, value, *, name=None) -> None:
        if not callable(value):
            raise TypeError("an indexed family requires a value map")
        self._index_set = index_set
        self._value_function = value
        self._value_cache = {}
        self._name = name

    def index_set(self):
        return self._index_set

    def cardinality(self):
        return self.index_set().cardinality()

    def value(self, index):
        normalized = self.index_set()(index)
        try:
            return self._value_cache[normalized]
        except (KeyError, TypeError):
            value = self._value_function(normalized)
            try:
                self._value_cache[normalized] = value
            except TypeError:
                pass
            return value

    __call__ = value

    def __getitem__(self, index):
        try:
            normalized = self.index_set()(index)
        except (TypeError, ValueError):
            return self.unrank(index)
        return self.value(normalized)

    def items(self):
        return ((index, self.value(index)) for index in self.index_set())

    def __iter__(self):
        return (self.value(index) for index in self.index_set())

    def unrank(self, position):
        try:
            index = self.index_set().unrank(int(position))
        except AttributeError:
            try:
                index = next(
                    index
                    for offset, index in enumerate(self.index_set())
                    if offset == int(position)
                )
            except StopIteration as error:
                raise IndexError(position) from error
        return self.value(index)

    def map(self, function, *, name=None):
        if not callable(function):
            raise TypeError("a family map must be callable")
        return IndexedFamily(
            self.index_set(),
            lambda index: function(self.value(index)),
            name=name,
        )

    def _repr_(self):
        return self._name or f"Family indexed by {self.index_set()}"


def indexed_family(index_set, value, *, name=None):
    r"""Return the family ``index |-> value(index)`` over ``index_set``."""
    return IndexedFamily(index_set, value, name=name)


finite_indexed_family = indexed_family


__all__ = [
    "IndexedFamily",
    "finite_indexed_family",
    "indexed_family",
]
