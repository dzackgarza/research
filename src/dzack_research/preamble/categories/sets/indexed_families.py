"""Owned indexed families of mathematical values."""

from collections.abc import Callable, Iterator
from typing import Any, Generic, TypeVar

from sage.misc.unknown import Unknown
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject


IndexT = TypeVar("IndexT")
ValueT = TypeVar("ValueT")
MappedValueT = TypeVar("MappedValueT")


class IndexedFamily(SageObject, Generic[IndexT, ValueT]):
    r"""A family ``(x_i)_{i in I}`` retaining its indexing set.

    A family is not the set of its values: different indices may have equal
    values, so it is not injective and has no ranking map of its own.  Its
    index set may have one, and positional access goes through that.
    Consumers iterate values lazily or address them through ``value(index)``.
    """

    def __init__(
        self,
        index_set: Parent,
        value: Callable[[IndexT], ValueT],
        *,
        name: str | None = None,
    ) -> None:
        if not callable(value):
            raise TypeError("an indexed family requires a value map")
        self._index_set = index_set
        self._value_function = value
        self._value_cache: dict[IndexT, ValueT] = {}
        self._unhashable_value_cache: list[tuple[IndexT, ValueT]] = []
        self._name = name

    def index_set(self) -> Parent:
        return self._index_set

    def cardinality(self) -> Parent:
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        return cardinal(self.index_set().cardinality())

    def value(self, index: IndexT) -> ValueT:
        r"""Return the chosen value at this label, including unhashable labels.

        Unverified specimen: a family chooses its value once, not each time
        a Python list is used to address the same point of its index set::

            sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
            sage: labels = finite_ordered_set(([0], [1]))
            sage: family = indexed_family(labels, lambda label: finite_ordered_set((label[0],)))
            sage: family.value([0]) is family.value([0])
            True
        """
        normalized = self.index_set()(index)
        try:
            return self._value_cache[normalized]
        except TypeError:
            # Hashing is an implementation property, not a hypothesis on an
            # indexing set. Only labels actually requested are retained.
            for known, value in self._unhashable_value_cache:
                if normalized == known:
                    return value
            value = self._value_function(normalized)
            self._unhashable_value_cache.append((normalized, value))
            return value
        except KeyError:
            value = self._value_function(normalized)
            self._value_cache[normalized] = value
            return value

    __call__ = value

    def __getitem__(self, index: IndexT) -> ValueT:
        r"""The value at ``index``, or -- failing that -- at that position."""
        try:
            normalized = self.index_set()(index)
        except (TypeError, ValueError):
            return self.value(self.index_set().ranking_map().inverse()(index))
        return self.value(normalized)

    def items(self) -> Iterator[tuple[IndexT, ValueT]]:
        return ((index, self.value(index)) for index in self.index_set())

    def __iter__(self) -> Iterator[ValueT]:
        return (self.value(index) for index in self.index_set())

    def map(
        self,
        function: Callable[[ValueT], MappedValueT],
        *,
        name: str | None = None,
    ) -> "IndexedFamily[IndexT, MappedValueT]":
        if not callable(function):
            raise TypeError("a family map must be callable")
        return IndexedFamily(
            self.index_set(),
            lambda index: function(self.value(index)),
            name=name,
        )

    def __eq__(self, other: Any):
        r"""Return extensional equality, or ``Unknown`` when undecidable."""
        if self is other:
            return True
        if not isinstance(other, IndexedFamily):
            return False

        same_indices = self.index_set() == other.index_set()
        if same_indices is False:
            return False
        if same_indices is not True:
            return Unknown
        if self.cardinality().is_finite() is not True:
            return Unknown

        answer = True
        for index in self.index_set():
            same_value = self.value(index) == other.value(index)
            if same_value is False:
                return False
            if same_value is not True:
                answer = Unknown
        return answer

    def __ne__(self, other):
        equal = self == other
        if equal is Unknown:
            return Unknown
        return not equal

    def __hash__(self):
        r"""Hash finite extensional data and infinite families by identity."""
        if self.cardinality().is_finite() is not True:
            return object.__hash__(self)
        return hash(
            (
                self.index_set(),
                frozenset((index, self.value(index)) for index in self.index_set()),
            )
        )

    def _repr_(self):
        return self._name or f"Family indexed by {self.index_set()}"


def indexed_family(
    index_set: Parent,
    value: Callable[[IndexT], ValueT],
    *,
    name: str | None = None,
) -> IndexedFamily[IndexT, ValueT]:
    r"""Return the family ``index |-> value(index)`` over ``index_set``."""
    return IndexedFamily(index_set, value, name=name)


finite_indexed_family = indexed_family


__all__ = [
    "IndexedFamily",
    "finite_indexed_family",
    "indexed_family",
]
