"""Owned indexed families of mathematical values."""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterator, Mapping
from itertools import islice
from typing import TYPE_CHECKING, Any

from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.objects import Objects

from dzack_research.preamble.lexicon.set_theory import SetObject
from dzack_research.preamble.owned_category import _object_of

if TYPE_CHECKING:
    from dzack_research.preamble.categories.sets.cardinals import Cardinal
    from dzack_research.preamble.logic import Predicate


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
        value: Callable[[IndexT], ValueT] | Parent,
        *,
        value_category=None,
        name: str | None = None,
        **rest,
    ) -> None:
        self._constant_value = value if isinstance(value, Parent) else None
        if isinstance(value, Parent):
            selected = value
            value = lambda _index: selected
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
        self._diagram = None
        self._value_category = value_category
        super().__init__(**rest)

    def index_set(self) -> SetObject:
        return self._index_set

    def constant_value(self):
        r"""The defining value of a constant family, or ``None`` otherwise."""
        return self._constant_value

    def selected_diagram(self):
        return self._diagram

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
        return self._value_at_normalized_index(self.index_set()(index))

    def _value_at_normalized_index(self, normalized: IndexT) -> ValueT:
        r"""Return the cached value at an index already supplied by ``index_set()``.

        Iteration over an indexed family obtains its labels from the index set
        itself.  Reapplying the index-set constructor to those labels is not a
        mathematical operation and can be expensive for represented index
        sets, so the internal iteration path enters the value cache directly.
        Public ``value(index)`` still performs the canonical normalization.
        """
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
        return (
            (index, self._value_at_normalized_index(index))
            for index in self.index_set()
        )

    def keys(self) -> SetObject:
        r"""Return the mathematical index set of this family."""
        return self.index_set()

    def values(self) -> Iterator[ValueT]:
        return iter(self)

    def get(self, index: IndexT, default=None):
        r"""Return the value at ``index`` when indexed here, otherwise ``default``."""
        return self.value(index) if index in self.index_set() else default

    def __iter__(self) -> Iterator[ValueT]:
        return (
            self._value_at_normalized_index(index)
            for index in self.index_set()
        )

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
            (self._value_at_normalized_index(index) == candidate) is True
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

    def __eq__(self, other: Any) -> bool | Predicate:
        r"""Return extensional equality, decided on a finite index set.

        Otherwise the answer is the proposition that the two families are
        equal.
        """
        from dzack_research.preamble.logic import AtomicProposition, conjunction

        if self is other:
            return True
        if not isinstance(other, IndexedFamily):
            return False

        same_indices = self.index_set() == other.index_set()
        if same_indices is False:
            return False
        if same_indices is not True or self.cardinality().is_finite() is not True:
            return AtomicProposition("equal", self, other)
        return conjunction(self.value(index) == other.value(index) for index in self.index_set())

    def __ne__(self, other) -> bool | Predicate:
        from dzack_research.preamble.logic import negation

        return negation(self == other)

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
    value: Callable[[IndexT], ValueT] | Parent,
    *,
    value_category=None,
    name: str | None = None,
) -> IndexedFamily[IndexT, ValueT]:
    r"""Return the family ``index |-> value(index)`` as an owned mathematical object.

    A family is not the set of its values: repeated values at distinct indices
    remain distinct family slots.  Until a consumer supplies a more specific
    codomain/category (for example a discrete diagram in ``[I,C]``), the family
    therefore lives at the existing root ``Objects()`` rather than being
    misdeclared as a set.
    """
    from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory, _DiscreteDiagram
    from dzack_research.preamble.categories.functors.core import Functor

    selected_functor = value if isinstance(value, Functor) else None
    if selected_functor is not None:
        from dzack_research.preamble.categories.sets.set_categories import Sets

        if isinstance(selected_functor, _DiscreteDiagram) and not Sets().is_provably_finite(index_set):
            raise TypeError(
                "a diagram on an infinite index set assembled from an unchecked object callback "
                "does not establish that its values belong to its claimed codomain"
            )
        index_category = DiscreteCategory(index_set)
        if selected_functor.domain() is not index_category:
            raise ValueError("the selected family functor has the wrong discrete index category")
        if value_category is not None and value_category is not selected_functor.codomain():
            raise ValueError("the requested category differs from the selected functor codomain")
        value_category = selected_functor.codomain()
        value = lambda index: selected_functor(index_category.object(index))

    family = _object_of(
        Objects(),
        _engine=(Objects(), IndexedFamily, None),
        index_set=index_set,
        value=value,
        value_category=value_category,
        name=name,
    )
    if value_category is not None:
        from dzack_research.preamble.categories.abstract_categories.cat import Cat
        from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
        from dzack_research.preamble.categories.sets.set_categories import Sets

        if not Sets().is_provably_finite(index_set) and family.constant_value() is None and selected_functor is None:
            raise TypeError(
                "an infinite nonconstant family cannot establish its value category by declaring one: "
                "supply a mathematically justified category-valued diagram"
            )
        if Sets().is_provably_finite(index_set):
            for index in index_set:
                if family(index) not in value_category:
                    raise ValueError(
                        f"the selected family has value {family(index)} at {index}, outside {value_category}"
                    )

        family._diagram = selected_functor or Cat().Mor(DiscreteCategory(index_set), value_category).discrete_diagram(family)
    return family


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
