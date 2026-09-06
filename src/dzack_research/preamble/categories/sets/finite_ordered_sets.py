"""Owned ordered enumerated sets with finite sets as a refinement."""

from itertools import islice

from sage.categories.category import Category
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.posets import Posets
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    NN,
    Sets,
    TotallyOrderedSets,
    finite_ordinal_set,
    ranking_isomorphism,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal






def _finite_ordered_presentation(elements):
    r"""Return the enumeration data of one known-finite ordered source."""

    if elements in FiniteOrderedSets():
        return (
            elements.index_set(),
            elements._element_at_function,
            elements._index_of_function,
            elements._contains_function,
        )

    # Python sequence/range input is syntactic ingress.  Parse it once into the
    # owned set without retaining the sequence as mathematical storage.
    if isinstance(elements, (tuple, list, range)):
        by_position = {}
        for element in elements:
            if any(element == known for known in by_position.values()):
                continue
            by_position[len(by_position)] = element
        index_set = finite_ordinal_set(len(by_position))

        def index_of(element):
            for position in index_set:
                if by_position[int(position)] == element:
                    return position
            raise ValueError(element)

        return (
            index_set,
            lambda position: by_position[int(position)],
            index_of,
            lambda element: any(element == known for known in by_position.values()),
        )

    if elements not in Sets():
        raise TypeError(
            "finite_ordered_set requires a known finite set or explicit finite literal; "
            "use finite_ordered_image(index_set, map) for a computed family"
        )

    size = cardinal(elements.cardinality())
    if not size.is_finite():
        raise TypeError("finite_ordered_set requires a finite source set")
    finite_size = int(size.finite_value())
    index_set = finite_ordinal_set(finite_size)

    if elements in EnumeratedSets():
        # The source states its own enumeration, so this reads it off rather
        # than searching: both directions come from that one isomorphism.
        source_ranking = elements.ranking_map()
        element_at = lambda position: source_ranking.inverse()(int(position))
        index_of = lambda element: source_ranking(element)
    else:
        def element_at(position):
            try:
                return next(islice(iter(elements), int(position), int(position) + 1))
            except StopIteration as error:
                raise IndexError(position) from error

        def index_of(element):
            for position, candidate in enumerate(elements):
                if candidate == element:
                    return position
            raise ValueError(element)

    return index_set, element_at, index_of, lambda element: element in elements




def ordered_enumerated_set(index_set, element_at, *, index_of, contains=None, name=None):
    r"""Return the ordered image of ``index_set`` under the stated enumeration."""
    return object_of(
        OrderedEnumeratedSets(),
        index_set,
        element_at,
        index_of=index_of,
        contains=contains,
        name=name,
    )


def finite_ordered_image(index_set, element_at, *, index_of=None, contains=None, name=None):
    r"""Return a finite ordered image without materializing its members."""
    return FiniteOrderedSets().ObjectType.from_indexed(
        index_set,
        element_at,
        index_of=index_of,
        contains=contains,
        name=name,
    )


def finite_ordered_filter(source, predicate, *, name=None):
    r"""Return the finite ordered subset cut out by ``predicate`` lazily."""
    return object_of(
        FiniteFilteredOrderedSets(), source=source, predicate=predicate, name=name
    )


class OrderedEnumeratedSets(OwnedCategory):
    r"""Ordered sets presented by an index set and a bijection out of it."""

    def an_object(self):
        r"""The ordinal on three points."""
        return finite_ordered_set((0, 1, 2))

    def super_categories(self):
        return [EnumeratedSets(), TotallyOrderedSets()]

    class ParentMethods:
        def __init__(
            self,
            index_set,
            element_at,
            *,
            index_of,
            contains=None,
            name=None,
            finite=False,
            **rest,
        ) -> None:
            assert callable(element_at), (
                "an ordered enumerated set requires a map from its index set"
            )
            assert callable(index_of), (
                "an enumerated set states both directions of its enumeration: a "
                "map out of an index set with no inverse presents a family, "
                "which is not a set with a ranking"
            )
            self._index_set = index_set
            self._element_at_function = element_at
            self._index_of_function = index_of
            self._contains_function = contains
            self._name = name
            super().__init__(facade=True, **rest)
            if finite:
                from dzack_research.preamble.refine import refine

                from dzack_research.preamble.categories.sets.set_categories import FiniteSets

                refine(self, FiniteSets())

        def index_set(self):
            return self._index_set

        def cardinality(self):
            return cardinal(self.index_set().cardinality())

        @cached_method
        def ranking_map(self):
            r"""The chosen enumeration of this image, as one isomorphism.

            The presentation gives a bijection from the index set, and the
            index set already knows its own ordinal, so this composes the two
            rather than counting the image a second time.
            """
            index_ranking = self.index_set().ranking_map()

            def point_at(position):
                return self._element_at_function(index_ranking.inverse()(int(position)))

            def position_of(element):
                index = self._index_of_function(element)
                if index is None:
                    raise ValueError(f"{element!r} is not in {self}")
                return int(index_ranking(index))

            return ranking_isomorphism(self, position_of, point_at)

        def __iter__(self):
            return (self._element_at_function(index) for index in self.index_set())

        def __contains__(self, element) -> bool:
            if self._contains_function is not None:
                return bool(self._contains_function(element))
            return self._index_of_function(element) is not None

        is_parent_of = __contains__

        def __call__(self, element):
            return self._element_constructor_(element)

        def _element_constructor_(self, element):
            r"""Return the member of this image that ``element`` names.

            This is the element constructor, the one boundary that admits
            foreign data, so it reads the presentation directly.  It cannot
            ask the ranking map: applying an arrow coerces its argument into
            the domain, and the domain is this parent.
            """
            index = self._index_of_function(element)
            if index is None:
                raise ValueError(f"{element!r} is not in {self}")
            return self._element_at_function(index)

        def le(self, left, right) -> bool:
            ranking = self.ranking_map()
            return ranking(left) <= ranking(right)

        def _repr_(self) -> str:
            return self._name or f"Ordered image of {self.index_set()}"

class FiniteOrderedSets(OwnedCategory):
    r"""Finite ordered sets, without sequence-valued storage."""

    def an_object(self):
        r"""The three-point ordered set."""
        return finite_ordered_set((0, 1, 2))

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import FiniteSets

        # The owned finiteness, not Sage's: Sage's
        # ``FiniteEnumeratedSets`` supplies a ``cardinality`` returning an
        # integer, and a cardinality here is a cardinal.
        return [OrderedEnumeratedSets(), FiniteSets()]

    class ParentMethods:
        def __init__(self, elements, **rest) -> None:
            index_set, element_at, index_of, contains = _finite_ordered_presentation(elements)
            super().__init__(
                index_set,
                element_at,
                index_of=index_of,
                contains=contains,
                finite=True,
                **rest,
            )

        @staticmethod
        def from_indexed(index_set, element_at, *, index_of=None, contains=None, name=None):
            r"""Return the finite ordered set on a chosen indexed presentation."""
            assert cardinal(index_set.cardinality()).is_finite(), (
                "a finite ordered set requires a finite index set"
            )
            if index_of is None:
                def index_of(element):
                    for index in index_set:
                        if element_at(index) == element:
                            return index
                    raise ValueError(element)
            if contains is None:
                def contains(element):
                    try:
                        index_of(element)
                    except (TypeError, ValueError):
                        return False
                    return True
            return object_of(
                OrderedEnumeratedSets(),
                index_set=index_set,
                element_at=element_at,
                index_of=index_of,
                contains=contains,
                name=name,
                finite=True,
            )

        def __eq__(self, other) -> bool:
            if self is other:
                return True
            try:
                if int(self.cardinality()) != int(other.cardinality()):
                    return False
            except (AttributeError, TypeError, ValueError):
                return False
            if other in FiniteOrderedSets():
                return all(left == right for left, right in zip(self, other, strict=True))
            try:
                return all(element in other for element in self)
            except (TypeError, ValueError):
                return False

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self) -> int:
            # Do not hash members: group/lattice elements may normalize expensively.
            return hash(int(self.cardinality()))

        def __len__(self) -> int:
            return int(self.cardinality())

        def _repr_(self) -> str:
            return "{" + ", ".join(repr(element) for element in self) + "}"

class FiniteFilteredOrderedSets(OwnedCategory):
    r"""A finite ordered subset selected lazily by a predicate."""

    def an_object(self):
        r"""The even points of a three-point ordinal."""
        return finite_ordered_filter(finite_ordered_set((0, 1, 2)), lambda x: True)

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import FiniteSets

        # The owned finiteness, not Sage's: Sage's
        # ``FiniteEnumeratedSets`` supplies a ``cardinality`` returning an
        # integer, and a cardinality here is a cardinal.
        return [OrderedEnumeratedSets(), FiniteSets()]

    class ParentMethods:
        def __init__(self, source, predicate, *, name=None, **rest) -> None:

            assert cardinal(source.cardinality()).is_finite(), (
                "a finite ordered filter requires a finite source set"
            )
            self._source = source
            self._predicate = predicate
            self._filtered_name = name
            # This level supplies its own ranking map and cardinality, so the
            # base takes the source as index set and this level's enumeration.
            super().__init__(
                source,
                lambda position: self.ranking_map().inverse()(position),
                index_of=lambda element: self.ranking_map()(element),
                contains=lambda element: predicate(element),
                name=name,
                finite=True,
                **rest,
            )

        def source(self):
            return self._source

        def predicate(self):
            return self._predicate

        def __iter__(self):
            return (element for element in self.source() if self.predicate()(element))

        def cardinality(self):
            return cardinal(sum(1 for _element in self))

        @cached_method
        def ranking_map(self):
            r"""The enumeration the surviving members inherit from the source order."""

            def point_at(position):
                try:
                    return next(islice(iter(self), int(position), int(position) + 1))
                except StopIteration as error:
                    raise IndexError(position) from error

            def position_of(element):
                for position, candidate in enumerate(self):
                    if candidate == element:
                        return position
                raise ValueError(f"{element!r} is not in {self}")

            return ranking_isomorphism(self, position_of, point_at)

        def __contains__(self, element) -> bool:
            return element in self.source() and bool(self.predicate()(element))

        is_parent_of = __contains__

        def __call__(self, element):
            if element not in self:
                raise ValueError(f"{element!r} is not in {self}")
            return self.source()(element)

        def le(self, left, right) -> bool:
            ranking = self.ranking_map()
            return ranking(left) <= ranking(right)

        def __len__(self):
            return int(self.cardinality())

        def __eq__(self, other) -> bool:
            if self is other:
                return True
            if other not in FiniteOrderedSets():
                return False
            if self.cardinality() != other.cardinality():
                return False
            return all(left == right for left, right in zip(self, other, strict=True))

        def __hash__(self):
            return hash(int(self.cardinality()))

        def _repr_(self):
            return self._filtered_name or f"Ordered subset of {self.source()}"

def finite_ordered_set(elements):
    r"""Transport one known finite ordered enumeration to an owned set."""
    if elements in FiniteOrderedSets():
        return elements
    return object_of(FiniteOrderedSets(), elements=elements)
