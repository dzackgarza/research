"""Owned indexed families of mathematical values."""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterator, Mapping
from itertools import islice
from typing import TYPE_CHECKING, Any

from sage.misc.unknown import Unknown
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.objects import Objects

from dzack_research.preamble.lexicon.set_theory import SetObject
from dzack_research.preamble.owned_category import _object_of

if TYPE_CHECKING:
    from dzack_research.preamble.categories.sets.cardinals import Cardinal


class IndexedFamily[IndexT, ValueT]:
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
        **rest,
    ) -> None:
        if not callable(value):
            raise TypeError(
                f"an indexed family over {index_set} needs a map from indices to values, but {value!r} is "
                "not callable"
            )
        self._index_set = index_set
        self._value_function = value
        self._value_cache: dict[IndexT, ValueT] = {}
        self._unhashable_value_cache: list[tuple[IndexT, ValueT]] = []
        self._name = name
        super().__init__(**rest)

    def index_set(self) -> SetObject:
        return self._index_set

    def cardinality(self) -> Cardinal:
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
        match normalized:
            case Hashable():
                missing = object()
                cached = self._value_cache.get(normalized, missing)
                if cached is not missing:
                    return cached
                value = self._value_function(normalized)
                self._value_cache[normalized] = value
                return value
            case _:
                # Hashability is representation data, not a hypothesis on an
                # indexing set. Only unhashable labels actually requested are
                # retained on this exact fallback path.
                for known, value in self._unhashable_value_cache:
                    if (normalized == known) is True:
                        return value
                value = self._value_function(normalized)
                self._unhashable_value_cache.append((normalized, value))
                return value

    __call__ = value

    def __getitem__(self, index: IndexT) -> ValueT:
        r"""The value at a label, otherwise at a position in the index set's enumeration."""
        match index in self.index_set():
            case True:
                return self.value(index)
            case False:
                return self.value(self.index_set().ranking_map().inverse()(index))

    def items(self) -> Iterator[tuple[IndexT, ValueT]]:
        return ((index, self.value(index)) for index in self.index_set())

    def keys(self) -> SetObject:
        r"""Return the mathematical index set of this family."""
        return self.index_set()

    def values(self) -> Iterator[ValueT]:
        return iter(self)

    def get(self, index: IndexT, default=None):
        r"""Return the value at ``index`` when indexed here, otherwise ``default``."""
        return self.value(index) if index in self.index_set() else default

    def __iter__(self) -> Iterator[ValueT]:
        return (self.value(index) for index in self.index_set())

    def __contains__(self, candidate: object) -> bool:
        r"""Return whether candidate occurs among the values of a finite family.

        The family retains its indexing data and is not identified with its
        image set.  For a finite family, however, occurrence among the selected
        values is decidable and is the membership operation used by finite
        invariant and generator families.
        """
        if self.cardinality().is_finite() is not True:
            raise TypeError(
                "value membership is represented only for a finite indexed family"
            )
        return any(
            (self.value(index) == candidate) is True
            for index in self.index_set()
        )

    def __len__(self) -> int:
        r"""Return the Python length when the mathematical index set is finite."""
        size = self.cardinality()
        if not size.is_finite():
            raise TypeError(
                f"the family {self} has infinite index set of cardinality {size}, so it has no length"
            )
        return int(size.finite_value())

    def map[MappedValueT](
        self,
        function: Callable[[ValueT], MappedValueT],
        *,
        name: str | None = None,
    ) -> IndexedFamily[IndexT, MappedValueT]:
        if not callable(function):
            raise TypeError(f"cannot map {function!r} over the family {self}: it is not callable")
        return indexed_family(
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
        from dzack_research.preamble.categories.sets.set_categories import (
            EnumeratedSets,
            FiniteSets,
        )

        index_set = self.index_set()
        label = self._name or "Indexed family"
        if index_set in FiniteSets() and index_set in EnumeratedSets():
            size = int(index_set.cardinality().finite_value())
            shown = tuple(index_set) if size <= 12 else tuple(islice(index_set, 6))
            entries = ", ".join(
                f"{index} ↦ {self.value(index)}" for index in shown
            )
            suffix = "" if size <= 12 else ", ..."
            data = f"[{entries}{suffix}]"
            prefix = f"{label}: " if self._name else ""
            count = "" if size <= 12 else f" ({size} entries)"
            return f"{prefix}{data}{count}"

        return f"{label} over {index_set}"


def indexed_family[IndexT, ValueT](
    index_set: Parent,
    value: Callable[[IndexT], ValueT],
    *,
    name: str | None = None,
) -> IndexedFamily[IndexT, ValueT]:
    r"""Return the family ``index |-> value(index)`` as an owned mathematical object.

    A family is not the set of its values: repeated values at distinct indices
    remain distinct family slots.  Until a consumer supplies a more specific
    codomain/category (for example a discrete diagram in ``[I,C]``), the family
    therefore lives at the existing root ``Objects()`` rather than being
    misdeclared as a set.
    """
    return _object_of(
        Objects(),
        _engine=(Objects(), IndexedFamily, None),
        index_set=index_set,
        value=value,
        name=name,
    )


finite_indexed_family = indexed_family


def finite_indexed_family_from_values(
    index_set,
    values,
    *,
    name: str | None = None,
) -> IndexedFamily:
    r"""Read finite literal data as an indexed family, preserving its labels.

    ``values`` may already be an indexed family, a mapping keyed by labels, or
    an ordinary finite iterable.  When ``index_set`` is omitted, those three
    cases use the family's own labels, the mapping keys, or the ordinal of the
    iterable positions respectively.  Literal-container interpretation belongs
    here, at the indexed-family owner; mathematical consumers only state the
    index set they require.
    """
    from dzack_research.preamble.categories.sets.finite_ordered_sets import (
        finite_ordered_set,
    )

    match values:
        case IndexedFamily():
            match index_set:
                case None:
                    labels = finite_ordered_set(tuple(values.index_set()))
                case _:
                    labels = index_set
            family = indexed_family(labels, values.value, name=name)
            supplied_cardinality = values.cardinality()
            match supplied_cardinality.is_finite():
                case True:
                    pass
                case _:
                    raise TypeError(
                        f"cannot read {values} as a finite family: its index set has cardinality {supplied_cardinality}"
                    )
            supplied_size = int(supplied_cardinality.finite_value())
        case Mapping():
            match index_set:
                case None:
                    labels = finite_ordered_set(tuple(values))
                case _:
                    labels = index_set
            family = indexed_family(labels, values.__getitem__, name=name)
            supplied_size = len(values)
        case _:
            entries = tuple(values)
            match index_set:
                case None:
                    labels = finite_ordered_set(range(len(entries)))
                case _:
                    labels = index_set
            family = indexed_family(
                labels,
                lambda label: entries[int(labels.ranking_map()(label))],
                name=name,
            )
            supplied_size = len(entries)

    match family.cardinality().is_finite():
        case True:
            pass
        case _:
            raise TypeError(
                f"cannot read {values!r} as a finite family: the index set {labels} is not finite"
            )
    match int(family.cardinality().finite_value()) == supplied_size:
        case True:
            pass
        case False:
            raise ValueError(
                f"cannot read {values!r} as a family indexed by {labels}: it has {supplied_size} entries, but "
                f"{labels} has {family.cardinality()} elements"
            )
    return family


__all__ = [
    "IndexedFamily",
    "finite_indexed_family",
    "finite_indexed_family_from_values",
    "indexed_family",
]
