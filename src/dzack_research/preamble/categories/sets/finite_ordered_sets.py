"""Owned ordered enumerated sets with finite sets as a refinement."""

from collections.abc import Callable
from itertools import islice
from typing import TypeVar

from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    Sets,
    TotallyOrderedSets,
    finite_ordinal_set,
)
from dzack_research.preamble.owned_category import _object_of

IndexT = TypeVar("IndexT")
PointT = TypeVar("PointT")


class _IndexedFiniteOrderedPresentation:
    r"""Private constructor data for a finite ordered image.

    ``FiniteOrderedSets`` is the specialization ``OrderedEnumeratedSets`` plus
    finiteness.  Constructing an indexed image through the general category and
    refining afterward can replay the specialization constructor with the index
    set as its ``elements`` datum, silently replacing the intended value map by
    the index enumeration.  Carry the indexed presentation as the one datum of
    the specialized constructor instead.
    """

    def __init__(self, index_set, element_at, index_of, contains, *, image_source=None, image_map=None, image_inverse=None) -> None:
        self.index_set = index_set
        self.element_at = element_at
        self.index_of = index_of
        self.contains = contains
        self.image_source = image_source
        self.image_map = image_map
        self.image_inverse = image_inverse


class _SetImageConstruction:
    r"""A selected source set, image map, and inverse on its represented image."""

    def __init__(self, source, image_map, inverse) -> None:
        self._source = source
        self._image_map = image_map
        self._inverse = inverse

    def source(self):
        return self._source

    def image_map(self):
        return self._image_map

    def inverse(self):
        return self._inverse


def _finite_ordered_presentation(elements):
    r"""Return the enumeration data of one known-finite ordered source."""

    if isinstance(elements, _IndexedFiniteOrderedPresentation):
        return (
            elements.index_set,
            elements.element_at,
            elements.index_of,
            elements.contains,
        )

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
            "use FiniteOrderedSets().from_indexed(index_set, map) for a computed family"
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

        def element_at(position):
            return source_ranking.inverse()(int(position))

        def index_of(element):
            return source_ranking(element)
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




class OrderedEnumeratedSets(OwnedCategory):
    r"""Ordered sets presented by an index set and a bijection out of it."""

    def an_object(self) -> Parent:
        r"""The ordinal on three points."""
        return finite_ordered_set((0, 1, 2))

    def super_categories(self):
        return [EnumeratedSets(), TotallyOrderedSets()]

    def _call_(
        self,
        index_set,
        element_at,
        *,
        index_of,
        contains=None,
        name=None,
        finite=False,
        image_source=None,
        image_map=None,
        image_inverse=None,
    ):
        r"""Construct an ordered enumerated set from its chosen enumeration."""
        return _object_of(
            self,
            index_set=index_set,
            element_at=element_at,
            index_of=index_of,
            contains=contains,
            name=name,
            finite=finite,
            image_source=image_source,
            image_map=image_map,
            image_inverse=image_inverse,
        )

    class ParentMethods:
        def __init__(
            self,
            index_set: Parent,
            element_at: Callable[[IndexT], PointT],
            *,
            index_of: Callable[[PointT], IndexT | None],
            contains: Callable[[PointT], bool] | None = None,
            name: str | None = None,
            finite: bool = False,
            image_source=None,
            image_map=None,
            image_inverse=None,
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
            self._image_construction = (
                None
                if image_source is None and image_map is None and image_inverse is None
                else _SetImageConstruction(image_source, image_map, image_inverse)
            )
            super().__init__(facade=True, **rest)
            if finite:
                from dzack_research.preamble.categories.sets.set_categories import FiniteSets
                from dzack_research.preamble.refine import refine

                refine(self, FiniteSets())

        def index_set(self) -> Parent:
            return self._index_set

        def source_set(self):
            if self._image_construction is None or self._image_construction.source() is None:
                raise TypeError(f"{self} is not represented as an image construction")
            return self._image_construction.source()

        def image_map(self):
            if self._image_construction is None or self._image_construction.image_map() is None:
                raise TypeError(f"{self} is not represented as an image construction")
            return self._image_construction.image_map()

        def inverse_on_image(self):
            assert self._image_construction is not None and self._image_construction.inverse() is not None, (
                "inverse_on_image requires a selected inverse for this image construction"
            )
            return self._image_construction.inverse()

        def cardinality(self) -> Parent:
            return cardinal(self.index_set().cardinality())

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
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

            return self._ranking_isomorphism(position_of, point_at)

        def __iter__(self):
            return (self._element_at_function(index) for index in self.index_set())

        def __getitem__(self, position):
            r"""Return the point at ``position`` directly from the chosen enumeration."""
            index = self.index_set().ranking_map().inverse()(position)
            return self._element_at_function(index)

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

        def le(self, left: PointT, right: PointT) -> bool:
            ranking = self.ranking_map()
            return ranking(left) <= ranking(right)

        def _an_element_(self):
            r"""Return the first point of a nonempty selected enumeration."""
            try:
                return next(iter(self))
            except StopIteration as error:
                raise ValueError("the empty ordered enumerated set has no element") from error

        def _repr_(self) -> str:
            size = cardinal(self.cardinality())
            prefix = f"{self._name} = " if self._name else ""
            if size.is_finite():
                count = int(size.finite_value())
                shown = tuple(self) if count <= 12 else tuple(islice(self, 6))
                suffix = "" if count <= 12 else ", ..."
                data = "{" + ", ".join(repr(element) for element in shown) + suffix + "}"
                return f"{prefix}{data}" if count <= 12 else f"{prefix}{data} ({count} elements)"
            shown = tuple(islice(self, 6))
            data = "{" + ", ".join(repr(element) for element in shown) + ", ...}"
            return f"{prefix}{data} (cardinality {size})"

class FiniteOrderedSets(OwnedCategory):
    r"""Finite ordered sets, without sequence-valued storage."""

    def an_object(self) -> Parent:
        r"""The three-point ordered set."""
        return finite_ordered_set((0, 1, 2))

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import FiniteSets

        # The owned finiteness, not Sage's: Sage's
        # ``FiniteEnumeratedSets`` supplies a ``cardinality`` returning an
        # integer, and a cardinality here is a cardinal.
        return [OrderedEnumeratedSets(), FiniteSets()]

    def _call_(self, elements):
        r"""Construct a finite ordered set from a known finite enumeration."""
        if elements in self:
            return elements
        return _object_of(self, elements=elements)

    def from_indexed(
        self,
        index_set,
        element_at,
        *,
        index_of=None,
        contains=None,
        name=None,
        image_source=None,
        image_map=None,
        image_inverse=None,
    ):
        r"""Construct a finite ordered image from its chosen indexed presentation."""
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
        return _object_of(
            self,
            elements=_IndexedFiniteOrderedPresentation(
                index_set,
                element_at,
                index_of,
                contains,
                image_source=image_source,
                image_map=image_map,
                image_inverse=image_inverse,
            ),
            name=name,
        )

    class ParentMethods:
        _derived_construction_parameters = frozenset(
            {"index_set", "element_at", "index_of"}
        )

        def filtered(self, predicate, *, name=None):
            r"""Return the ordered subset of this set cut out lazily by ``predicate``."""
            return FiniteFilteredOrderedSets()(self, predicate, name=name)

        def __init__(
            self,
            elements: Parent | tuple[PointT, ...] | list[PointT] | range,
            **rest,
        ) -> None:
            image_source = elements.image_source if isinstance(elements, _IndexedFiniteOrderedPresentation) else None
            image_map = elements.image_map if isinstance(elements, _IndexedFiniteOrderedPresentation) else None
            image_inverse = elements.image_inverse if isinstance(elements, _IndexedFiniteOrderedPresentation) else None
            index_set, element_at, index_of, contains = _finite_ordered_presentation(elements)
            super().__init__(
                index_set,
                element_at,
                index_of=index_of,
                contains=contains,
                finite=True,
                image_source=image_source,
                image_map=image_map,
                image_inverse=image_inverse,
                **rest,
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

    def an_object(self) -> Parent:
        r"""The even points of a three-point ordinal."""
        return finite_ordered_set((0, 1, 2)).filtered(lambda x: True)

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import FiniteSets

        # The owned finiteness, not Sage's: Sage's
        # ``FiniteEnumeratedSets`` supplies a ``cardinality`` returning an
        # integer, and a cardinality here is a cardinal.
        return [OrderedEnumeratedSets(), FiniteSets()]

    def __call__(self, source, predicate, *, name=None):
        r"""Construct the subset even when ``source`` is already filtered.

        Sage's generic category call is a coercion first: it returns its first
        argument unchanged whenever that object is already in the category.
        Here the predicate is additional defining data, so filtering a filtered
        finite set must construct the intersection rather than discard the new
        predicate.
        """
        return self._call_(source, predicate, name=name)

    def _call_(self, source, predicate, *, name=None):
        r"""Construct the finite ordered subset cut out by ``predicate``."""
        return _object_of(self, source=source, predicate=predicate, name=name)

    class ParentMethods:
        _derived_construction_parameters = frozenset(
            {"index_set", "element_at", "index_of"}
        )

        def __init__(
            self,
            source: Parent,
            predicate: Callable[[PointT], bool],
            *,
            name: str | None = None,
            **rest,
        ) -> None:

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

        def source(self) -> Parent:
            return self._source

        def predicate(self) -> Callable[[PointT], bool]:
            return self._predicate

        def __iter__(self):
            return (element for element in self.source() if self.predicate()(element))

        def __getitem__(self, position):
            r"""Return the surviving member at ``position`` in inherited order."""
            return self.ranking_map().inverse()(position)

        def cardinality(self) -> Parent:
            return cardinal(sum(1 for _element in self))

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
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

            return self._ranking_isomorphism(position_of, point_at)

        def __contains__(self, element) -> bool:
            return element in self.source() and bool(self.predicate()(element))

        is_parent_of = __contains__

        def __call__(self, element):
            if element not in self:
                raise ValueError(f"{element!r} is not in {self}")
            return self.source()(element)

        def le(self, left: PointT, right: PointT) -> bool:
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

def finite_ordered_set[PointT](
    elements: Parent | tuple[PointT, ...] | list[PointT] | range,
) -> Parent:
    r"""Transport one known finite ordered enumeration to an owned set."""
    return FiniteOrderedSets()(elements)
