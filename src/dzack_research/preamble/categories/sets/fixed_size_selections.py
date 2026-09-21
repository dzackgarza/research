"""Fixed-size subsets and multisets of enumerated sets."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from heapq import merge
from itertools import count
from operator import index
from typing import SupportsIndex, TypeVar

from sage.arith.misc import binomial
from sage.misc.cachefunc import cached_function, cached_method
from sage.structure.element import Element
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import FiniteOrderedSets
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    FiniteSets,
    Sets,
    TotallyOrderedSets,
)

PointT = TypeVar("PointT")


def _selection_integer(value: SupportsIndex) -> int:
    r"""Read integer index data through Python's exact integer-index protocol.

    This native ingress accepts Python, preparsed Sage and owned integers.
    Unlike Sage's integer constructor it also admits the owned natural-number
    element, whose native integer operation is ``__index__``.  The equality
    guard refuses a foreign implementation that truncates in ``__index__``.
    """
    result = index(value)
    if value != result:
        raise TypeError("selection integer data cannot be truncated")
    return result


def _largest_combinadic_entry(rank: int, size: int) -> int:
    entry = size - 1
    while binomial(entry + 1, size) <= rank:
        entry += 1
    return entry


def _strict_positions_from_combinadic(rank: int, size: int):
    if size == 0:
        return iter(())
    largest = _largest_combinadic_entry(rank, size)
    remainder = rank - int(binomial(largest, size))

    def values():
        yield from _strict_positions_from_combinadic(remainder, size - 1)
        yield largest

    return values()


class FixedSizeSelectionElement(Element):
    r"""One selection, identified with its combinatorial rank."""

    def __init__(self, parent: FixedSizeSelections, combinatorial_rank: int) -> None:
        Element.__init__(self, parent)
        self._combinatorial_rank = combinatorial_rank

    def combinatorial_rank(self) -> int:
        return self._combinatorial_rank

    def degree(self) -> int:
        return self.parent().selection_size()

    def allows_repetition(self) -> bool:
        return self.parent().allows_repetition()

    def _source_positions(self):
        strict = _strict_positions_from_combinadic(
            self.combinatorial_rank(),
            self.degree(),
        )
        if not self.allows_repetition():
            return strict
        return (
            strict_position - offset
            for offset, strict_position in enumerate(strict)
        )

    def word(self) -> IndexedFamily:
        r"""The selection as the family of its points in increasing order."""
        indices = Sets.Δ[self.degree() - 1]

        def value(index):
            requested = int(index)
            for position, source_position in enumerate(self._source_positions()):
                if position == requested:
                    return self.parent().source()[source_position]
            raise IndexError(requested)

        return indexed_family(indices, value, name="Selection word")

    def __iter__(self):
        return iter(self.word())

    def multiplicity(self, label: PointT) -> int:
        source_position = int(self.parent().source().ranking_map()(label))
        return sum(
            1 for position in self._source_positions() if position == source_position
        )

    def support(self) -> FiniteOrderedSets.ObjectType:
        r"""The set of points occurring in the selection, in increasing order."""

        def distinct_positions():
            previous = None
            first = True
            for position in self._source_positions():
                if first or position != previous:
                    yield position
                first = False
                previous = position

        count_distinct = sum(1 for _position in distinct_positions())
        indices = Sets.Δ[count_distinct - 1]

        def source_label(index):
            requested = int(index)
            for offset, position in enumerate(distinct_positions()):
                if offset == requested:
                    return self.parent().source()[position]
            raise IndexError(requested)

        return FiniteOrderedSets().from_indexed(
            indices,
            source_label,
            name="Selection support",
        )

    def add_label(self, label: PointT) -> FixedSizeSelectionElement:
        target = self.parent().with_size(self.degree() + 1)
        position = int(self.parent().source().ranking_map()(label))
        if not self.allows_repetition() and self.multiplicity(label):
            raise ValueError("a subset cannot contain one label twice")
        return target.from_source_rank_positions(
            merge(self._source_positions(), (position,))
        )

    def merged_with(self, other: FixedSizeSelectionElement) -> FixedSizeSelectionElement:
        r"""The union of two selections over one source, as a selection of the summed size."""
        assert element_parent(other) is self.parent().with_size(other.degree()), (
            "selections are merged only with selections from one source set "
            "under one repetition rule"
        )
        target = self.parent().with_size(self.degree() + other.degree())
        if not self.allows_repetition():
            for label in self.support():
                if other.multiplicity(label):
                    raise ValueError("the two subsets are not disjoint")
        return target.from_source_rank_positions(
            merge(self._source_positions(), other._source_positions())
        )

    def wedge_with(
        self, other: FixedSizeSelectionElement
    ) -> tuple[FixedSizeSelectionElement, int] | None:
        assert element_parent(other) is self.parent().with_size(other.degree()), (
            "a wedge of subset indices is taken over one enumerated source"
        )
        if self.allows_repetition() or other.allows_repetition():
            raise TypeError("wedge is defined here for subset indices")
        for label in self.support():
            if other.multiplicity(label):
                return None
        inversions = sum(
            left_position > right_position
            for left_position in self._source_positions()
            for right_position in other._source_positions()
        )
        merged = self.merged_with(other)
        return merged, (-1 if inversions % 2 else 1)

    def __eq__(self, other) -> bool:
        return (
            element_parent(other) is self.parent()
            and other.combinatorial_rank() == self.combinatorial_rank()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.parent()), self.combinatorial_rank()))

    def _repr_(self) -> str:
        if self.degree() == 0:
            return "1"
        if not self.allows_repetition():
            return "{" + ", ".join(map(repr, self)) + "}"
        terms = []
        for label in self.support():
            multiplicity = self.multiplicity(label)
            terms.append(
                repr(label)
                if multiplicity == 1
                else f"{label!r}^{multiplicity}"
            )
        return " ".join(terms)


class FixedSizeSelections(EnumeratedSets().ObjectType):
    r"""The set of \(k\)-element selections from an enumerated set \(S\).

    An engine realizing objects of ``EnumeratedSets()``.  Without repetition
    these are the \(k\)-element subsets of \(S\); with repetition they are the
    \(k\)-element multisets on \(S\).  The datum is \((S, k)\) and whether
    repetition is allowed.  A selection is identified with its rank in the
    combinatorial number system, which enumerates the set and orders it; the
    set is finite exactly when \(S\) is finite or \(k = 0\), and countably
    infinite otherwise.  These refinements are inherited from the source's
    placement, without requiring a cardinality computation to construct the
    selections.  ``S.fixed_size_selections(k, repetition=r)`` is the
    construction route.
    """

    Element = FixedSizeSelectionElement

    def __init__(
        self,
        source: EnumeratedSets.ObjectType,
        selection_size: SupportsIndex,
        *,
        repetition: bool,
    ) -> None:
        size = _selection_integer(selection_size)
        assert size >= 0, "a selection size is a natural number"
        assert source in EnumeratedSets(), "fixed-size selections require an enumerated source set"
        self._source = source
        self._selection_size = size
        self._repetition = repetition
        match source:
            case _ if size == 0 or source in FiniteSets():
                size_placement = (FiniteSets(),)
            case _ if source in Sets().Countable().Infinite():
                size_placement = (Sets().Countable().Infinite(),)
            case _:
                size_placement = ()
        super().__init__(
            category=Cat().meet([EnumeratedSets(), TotallyOrderedSets(), *size_placement]),
            facade=False,
        )

    def source(self) -> EnumeratedSets.ObjectType:
        return self._source

    def selection_size(self) -> int:
        return self._selection_size

    def allows_repetition(self) -> bool:
        return self._repetition

    def with_size(self, selection_size: int) -> FixedSizeSelections:
        return self.source().fixed_size_selections(
            selection_size,
            repetition=self.allows_repetition(),
        )

    def cardinality(self) -> Cardinalities.ObjectType:
        r"""The number of \(k\)-selections from \(S\).

        For finite \(S\) with \(|S| = n\): \(\binom{n}{k}\) subsets and
        \(\binom{n+k-1}{k}\) multisets.  For \(k = 0\) the empty selection is
        the only one.  For infinite \(S\) and \(k \ge 1\) the selections number
        \(|S|\).  The chosen enumeration of an infinite \(S\) identifies it
        with \(\mathbb N\): the disjoint blocks
        \(\{kn,\ldots,kn+k-1\}\) inject \(\mathbb N\) into its
        \(k\)-subsets, which inject into \(\mathbb N^k\); the same lower
        bound works for multisets.  Both bounds are countable.
        """
        size = self.selection_size()
        if size == 0:
            return cardinal(1)
        source_size = cardinal(self.source().cardinality())
        match source_size:
            case _ if source_size.is_finite() and self.allows_repetition():
                return cardinal(binomial(source_size.finite_value() + size - 1, size))
            case _ if source_size.is_finite():
                return cardinal(binomial(source_size.finite_value(), size))
            case _:
                return source_size

    @cached_method
    def ranking_map(self) -> CategoricalIsomorphism:
        r"""The combinadic enumeration: a selection *is* its combinatorial rank."""

        def selection_at(position):
            position = _selection_integer(position)
            size = self.cardinality()
            if position < 0 or (size.is_finite() and position >= int(size)):
                raise IndexError(position)
            # For a finite source the cardinality bound is precisely the
            # combinadic range in which every selected position lies in
            # the source.
            return self.element_class(self, position)

        return self._ranking_isomorphism(
            lambda selection: self(selection).combinatorial_rank(), selection_at
        )

    def __iter__(self):
        size = self.cardinality()
        positions = range(int(size)) if size.is_finite() else count()
        selection_at = self.ranking_map().inverse()
        return (selection_at(position) for position in positions)

    def __contains__(self, candidate) -> bool:
        r"""A selection of this set is an element constructed in it."""
        return element_parent(candidate) is self

    is_parent_of = __contains__

    def _element_constructor_(self, datum):
        if datum in self:
            return datum
        raise TypeError(
            "a fixed-size selection is constructed by rank, source positions, or multiplicities"
        )

    def from_source_rank_positions(
        self,
        positions: Iterable[SupportsIndex],
    ) -> FixedSizeSelectionElement:
        degree = self.selection_size()
        rank = 0
        count_positions = 0
        previous = None
        first = True
        for offset, source_position in enumerate(positions):
            source_position = _selection_integer(source_position)
            if source_position < 0:
                raise ValueError("source ranks are nonnegative")
            if not first:
                if self.allows_repetition():
                    if source_position < previous:
                        raise ValueError("multiset source ranks must be nondecreasing")
                elif source_position <= previous:
                    raise ValueError("subset source ranks must be strictly increasing")
            strict_position = (
                source_position + offset
                if self.allows_repetition()
                else source_position
            )
            rank += int(binomial(strict_position, offset + 1))
            count_positions += 1
            previous = source_position
            first = False
        if count_positions != degree:
            raise ValueError(
                f"a member of {self} requires exactly {degree} source positions"
            )
        return self[rank]

    def from_labels(self, labels: Iterable[PointT]) -> FixedSizeSelectionElement:
        return self.from_source_rank_positions(
            self.source().ranking_map()(label) for label in labels
        )

    def from_multiplicities(
        self,
        multiplicities: Mapping[PointT, SupportsIndex],
    ) -> FixedSizeSelectionElement:
        if any(_selection_integer(value) < 0 for value in multiplicities.values()):
            raise ValueError("selection multiplicities are nonnegative integers")
        total = sum(_selection_integer(value) for value in multiplicities.values())
        if total != self.selection_size():
            raise ValueError(
                f"the multiplicities must have total degree {self.selection_size()}"
            )
        if not self.allows_repetition() and any(
            _selection_integer(value) not in (0, 1) for value in multiplicities.values()
        ):
            raise ValueError("subset multiplicities are zero or one")
        rank = 0
        for label, raw_multiplicity in multiplicities.items():
            multiplicity = _selection_integer(raw_multiplicity)
            if multiplicity == 0:
                continue
            source_position = int(self.source().ranking_map()(label))
            preceding = sum(
                _selection_integer(other_multiplicity)
                for other_label, other_multiplicity in multiplicities.items()
                if _selection_integer(other_multiplicity) > 0
                and int(self.source().ranking_map()(other_label)) < source_position
            )
            for occurrence in range(multiplicity):
                offset = preceding + occurrence
                strict_position = (
                    source_position + offset
                    if self.allows_repetition()
                    else source_position
                )
                rank += int(binomial(strict_position, offset + 1))
        return self[rank]

    def singleton_power(self, label: PointT) -> FixedSizeSelectionElement:
        if self.selection_size() == 0:
            raise ValueError("the degree-zero selection has no singleton label")
        return self.from_multiplicities({label: self.selection_size()})

    def _repr_(self) -> str:
        noun = "Multisets" if self.allows_repetition() else "Subsets"
        return f"{noun} of {self.source()} of size {self.selection_size()}"


@cached_function(key=lambda source, selection_size, repetition: (id(source), _selection_integer(selection_size), bool(repetition)))
def _fixed_size_selections(
    source: EnumeratedSets.ObjectType,
    selection_size: int,
    *,
    repetition: bool,
) -> FixedSizeSelections:
    return FixedSizeSelections(source, selection_size, repetition=bool(repetition))


__all__ = [
    "FixedSizeSelectionElement",
    "FixedSizeSelections",
]
