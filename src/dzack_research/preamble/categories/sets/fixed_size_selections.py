"""Fixed-size subsets and multisets of ordered enumerated sets."""

from itertools import count

from sage.misc.cachefunc import cached_function
from sage.arith.misc import binomial
from sage.categories.category import Category
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.structure.element import Element
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.enumerated.enumerated_sets import EnumeratedSets
from dzack_research.preamble.categories.sets.set_categories import TotallyOrderedSets
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_image
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets


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


def _merge_sorted(left, right):
    left_iter = iter(left)
    right_iter = iter(right)
    sentinel = object()
    left_value = next(left_iter, sentinel)
    right_value = next(right_iter, sentinel)
    while left_value is not sentinel or right_value is not sentinel:
        if right_value is sentinel or (
            left_value is not sentinel and left_value <= right_value
        ):
            yield left_value
            left_value = next(left_iter, sentinel)
        else:
            yield right_value
            right_value = next(right_iter, sentinel)


class FixedSizeSelectionElement(Element):
    r"""One fixed-size subset/multiset, encoded by its combinatorial rank."""

    def __init__(self, parent, combinatorial_rank) -> None:
        Element.__init__(self, parent)
        self._combinatorial_rank = int(combinatorial_rank)

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

    def word(self):

        indices = Sets.Δ[self.degree() - 1]

        def value(index):
            requested = int(index)
            for position, source_position in enumerate(self._source_positions()):
                if position == requested:
                    return self.parent().source().unrank(source_position)
            raise IndexError(requested)

        return indexed_family(indices, value, name="Selection word")

    def __iter__(self):
        return iter(self.word())

    def multiplicity(self, label) -> int:
        source_position = int(self.parent().source().rank(label))
        return sum(
            1 for position in self._source_positions() if position == source_position
        )

    def support(self):

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
                    return self.parent().source().unrank(position)
            raise IndexError(requested)

        return finite_ordered_image(
            indices,
            source_label,
            name="Selection support",
        )

    def add_label(self, label):
        target = self.parent().with_size(self.degree() + 1)
        position = int(self.parent().source().rank(label))
        if not self.allows_repetition() and self.multiplicity(label):
            raise ValueError("a subset cannot contain one label twice")
        return target.from_source_rank_positions(
            _merge_sorted(self._source_positions(), (position,))
        )

    def merged_with(self, other):
        if (
            not isinstance(other, FixedSizeSelectionElement)
            or other.parent().source() is not self.parent().source()
            or other.allows_repetition() != self.allows_repetition()
        ):
            raise TypeError("selections can be merged only over one source set")
        target = self.parent().with_size(self.degree() + other.degree())
        if not self.allows_repetition():
            for label in self.support():
                if other.multiplicity(label):
                    raise ValueError("the two subsets are not disjoint")
        return target.from_source_rank_positions(
            _merge_sorted(self._source_positions(), other._source_positions())
        )

    def wedge_with(self, other):
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
            isinstance(other, FixedSizeSelectionElement)
            and other.parent() is self.parent()
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


class FixedSizeSelections(Parent):
    Element = FixedSizeSelectionElement

    def __init__(self, source, selection_size, *, repetition) -> None:

        self._source = source
        self._selection_size = int(selection_size)
        self._repetition = bool(repetition)
        if self._selection_size < 0:
            raise ValueError("a selection size is nonnegative")
        if not hasattr(source, "rank") or not hasattr(source, "unrank"):
            raise TypeError(
                "fixed-size ordered selections require a ranked source set"
            )
        source_cardinality = cardinal(source.cardinality())
        categories = [EnumeratedSets(), TotallyOrderedSets()]
        try:
            source_is_finite = source_cardinality.is_finite()
        except NotImplementedError:
            source_is_finite = False
        if source_is_finite:
            categories.append(FiniteEnumeratedSets())
        Parent.__init__(self, facade=False, category=Category.join(tuple(categories)))

    def source(self):
        return self._source

    def selection_size(self) -> int:
        return self._selection_size

    def allows_repetition(self) -> bool:
        return self._repetition

    def with_size(self, selection_size):
        return fixed_size_selections(
            self.source(),
            selection_size,
            repetition=self.allows_repetition(),
        )

    def cardinality(self):

        source_size = cardinal(self.source().cardinality())
        degree = self.selection_size()
        if degree == 0:
            return cardinal(1)
        try:
            source_is_finite = source_size.is_finite()
        except NotImplementedError:
            source_is_finite = False
        if source_is_finite:
            rank = int(source_size.finite_value())
            if self.allows_repetition():
                return cardinal(binomial(rank + degree - 1, degree))
            if degree > rank:
                return cardinal(0)
            return cardinal(binomial(rank, degree))
        # For a ranked source of unresolved cardinality the selection set is
        # represented by its combinatorial ranking directly.  Cardinality need
        # not be decided in order to construct or enumerate its members.
        try:
            if source_size.is_countable():
                return source_size
        except NotImplementedError:
            pass
        return source_size

    def unrank(self, position):

        position = int(position)
        if position < 0:
            raise IndexError(position)
        size = self.cardinality()
        try:
            finite_size = int(size.finite_value()) if size.is_finite() else None
        except NotImplementedError:
            finite_size = None
        if finite_size is not None and position >= finite_size:
            raise IndexError(position)
        result = self.element_class(self, position)
        # For finite source sets the cardinality bound above is precisely the
        # combinadic range in which every selected position lies in the source.
        return result

    def rank(self, selection):
        selection = self(selection)
        return selection.combinatorial_rank()

    position = rank
    index = rank

    def __iter__(self):

        size = self.cardinality()
        try:
            finite_size = int(size.finite_value()) if size.is_finite() else None
        except NotImplementedError:
            finite_size = None
        positions = range(finite_size) if finite_size is not None else count()
        return (self.unrank(position) for position in positions)

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, FixedSizeSelectionElement)
            and candidate.parent() is self
        )

    is_parent_of = __contains__

    def _element_constructor_(self, datum):
        if datum in self:
            return datum
        raise TypeError(
            "a fixed-size selection is constructed by rank, source positions, or multiplicities"
        )

    def __getitem__(self, position):
        return self.unrank(position)

    def from_source_rank_positions(self, positions):
        degree = self.selection_size()
        rank = 0
        count_positions = 0
        previous = None
        first = True
        for offset, source_position in enumerate(positions):
            source_position = int(source_position)
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
        return self.unrank(rank)

    def from_labels(self, labels):
        return self.from_source_rank_positions(
            self.source().rank(label) for label in labels
        )

    def from_multiplicities(self, multiplicities):
        total = sum(int(value) for value in multiplicities.values())
        if total != self.selection_size():
            raise ValueError(
                f"the multiplicities must have total degree {self.selection_size()}"
            )
        if not self.allows_repetition() and any(
            int(value) not in (0, 1) for value in multiplicities.values()
        ):
            raise ValueError("subset multiplicities are zero or one")
        rank = 0
        for label, raw_multiplicity in multiplicities.items():
            multiplicity = int(raw_multiplicity)
            if multiplicity <= 0:
                continue
            source_position = int(self.source().rank(label))
            preceding = sum(
                int(other_multiplicity)
                for other_label, other_multiplicity in multiplicities.items()
                if int(other_multiplicity) > 0
                and int(self.source().rank(other_label)) < source_position
            )
            for occurrence in range(multiplicity):
                offset = preceding + occurrence
                strict_position = (
                    source_position + offset
                    if self.allows_repetition()
                    else source_position
                )
                rank += int(binomial(strict_position, offset + 1))
        return self.unrank(rank)

    def singleton_power(self, label):
        if self.selection_size() == 0:
            raise ValueError("the degree-zero selection has no singleton label")
        return self.from_multiplicities({label: self.selection_size()})

    def _repr_(self) -> str:
        noun = "Multisets" if self.allows_repetition() else "Subsets"
        return f"{noun} of {self.source()} of size {self.selection_size()}"


@cached_function(key=lambda source, selection_size, repetition: (id(source), int(selection_size), bool(repetition)))
def fixed_size_selections(source, selection_size, *, repetition):
    result = FixedSizeSelections(
        source,
        selection_size,
        repetition=repetition,
    )
    return result


def ordered_subsets_of_size(source, size):
    return fixed_size_selections(source, size, repetition=False)


def multisets_of_size(source, size):
    return fixed_size_selections(source, size, repetition=True)


__all__ = [
    "FixedSizeSelectionElement",
    "FixedSizeSelections",
    "fixed_size_selections",
    "multisets_of_size",
    "ordered_subsets_of_size",
]
