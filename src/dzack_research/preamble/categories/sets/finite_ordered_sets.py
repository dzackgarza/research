"""Owned ordered enumerated sets, with the finite ones as a refinement."""

from collections.abc import Callable, Iterable
from itertools import chain, islice
from typing import TypeVar

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.sets.set import Set as SageSet
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.cardinals import cardinal, omega, ordinal
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    FiniteSets,
    Sets,
    WellOrderedSets,
    finite_ordinal_set,
)
from dzack_research.preamble.lexicon.category_theory import ObjectOfCategory
from dzack_research.preamble.owned_category import _object_of

IndexT = TypeVar("IndexT")
PointT = TypeVar("PointT")


class OrderedEnumeratedSets(OwnedCategory):
    r"""Sets presented by a chosen enumeration from an index set.

    The defining datum is the enumeration: an index set \(I\), the bijection
    ``element_at`` from \(I\) onto the set, its inverse ``index_of``, which
    answers ``None`` for a candidate that is not a point, and optionally a
    membership decision ``contains``.  The total order is the one the
    enumeration transports from \(I\), which ``EnumeratedSets`` answers.
    """

    def an_object(self) -> ObjectOfCategory:
        r"""The ordinal on three points."""
        return finite_ordered_set((0, 1, 2))

    def super_categories(self):
        return [EnumeratedSets(), WellOrderedSets()]

    def __call__(self, index_set, element_at, **datum):
        r"""Construct from an enumeration even when ``index_set`` is itself in this category.

        Sage's generic category call returns its first argument whenever that
        argument is already an object of the category.  The index set of an
        enumeration may be one, and the enumeration is further data, so the
        call always constructs.
        """
        return self._call_(index_set, element_at, **datum)

    def _call_(
        self,
        index_set: Parent,
        element_at: Callable[[IndexT], PointT],
        *,
        index_of: Callable[[PointT], IndexT | None],
        contains: Callable[[PointT], bool] | None = None,
        name: str | None = None,
    ) -> Sets().ObjectType:
        r"""Construct an ordered enumerated set from its chosen enumeration."""
        assert index_set in EnumeratedSets(), (
            f"an ordered set is indexed by an enumerated set, but {index_set} is not enumerated"
        )
        if index_set in FiniteSets():
            return FiniteOrderedSets().from_indexed(
                index_set, element_at, index_of=index_of, contains=contains, name=name
            )
        return _object_of(
            self,
            index_set=index_set,
            element_at=element_at,
            index_of=index_of,
            contains=contains,
            name=name,
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
            category=None,
            **rest,
        ) -> None:
            assert callable(element_at), (
                f"an ordered set needs a map from its index set {index_set} to its points, but "
                f"{element_at!r} is not callable"
            )
            assert callable(index_of), (
                f"an ordered set needs the map from points back to positions in {index_set}, but "
                f"{index_of!r} is not callable; without it the data is a family, not a set with an order"
            )
            self._index_set = index_set
            self._element_at_function = element_at
            self._index_of_function = index_of
            self._contains_function = contains
            self._name = name
            placement = category if category is not None else OrderedEnumeratedSets()
            match index_set:
                case _ if index_set in FiniteSets():
                    placement = Category.join((placement, FiniteSets()))
                case _ if index_set in Sets().Infinite():
                    placement = Category.join((placement, Sets().Infinite()))
            super().__init__(category=placement, facade=True, **rest)

        def index_set(self) -> Sets().ObjectType:
            return self._index_set

        def enumeration(self) -> Callable[[IndexT], PointT]:
            r"""The chosen bijection from the index set onto this set."""
            return self._element_at_function

        def enumeration_inverse(self) -> Callable[[PointT], IndexT | None]:
            r"""The chosen inverse on this set, with ``None`` allowed off it."""
            return self._index_of_function

        @cached_method
        def ranking_map(self) -> CategoricalIsomorphism:
            r"""The chosen enumeration of this set, as one isomorphism.

            The presentation gives a bijection from the index set, and the
            index set already knows its own ordinal, so this composes the two
            rather than counting the set a second time.
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

        def order_type(self):
            r"""Return the ordinal order type of this ranked well-order."""
            size = cardinal(self.index_set().cardinality())
            if size.is_finite():
                return ordinal(size.finite_value())
            assert size.is_countably_infinite(), (
                f"the represented ordered enumeration {self} has cardinality {size}; its order type is implemented "
                "here only for finite or countably infinite enumerations"
            )
            return omega(0)

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
            r"""Return the member of this set that ``element`` names.

            This is the element constructor, the one boundary that admits
            foreign data, so it reads the presentation directly.  It cannot
            ask the ranking map: applying an arrow coerces its argument into
            the domain, and the domain is this parent.
            """
            if self._contains_function is not None and not self._contains_function(element):
                raise ValueError(f"{element!r} is not in {self}")
            index = self._index_of_function(element)
            if index is None:
                raise ValueError(f"{element!r} is not in {self}")
            return self._element_at_function(index)

        def _an_element_(self):
            r"""Return the first point of a nonempty enumeration."""
            for point in self:
                return point
            raise ValueError(f"{self} is empty, so it has no element")

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
    r"""Ordered enumerated sets over a finite index set, without sequence-valued storage.

    The datum is that of :class:`OrderedEnumeratedSets`; this category adds
    finiteness and the operations it permits.  Every other route -- a finite
    set, finitely many points, an indexed presentation -- computes that datum
    and enters through it.
    """

    def an_object(self) -> ObjectOfCategory:
        r"""The three-point ordered set."""
        return finite_ordered_set((0, 1, 2))

    def super_categories(self):
        # The owned finiteness, not Sage's: Sage's
        # ``FiniteEnumeratedSets`` supplies a ``cardinality`` returning an
        # integer, and a cardinality here is a cardinal.
        return [OrderedEnumeratedSets(), FiniteSets()]

    def _call_(self, elements: Parent | Iterable[PointT]) -> ObjectOfCategory:
        r"""Construct the finite ordered set a finite set or finitely many points present.

        The category call returns ``elements`` itself when it already is one.
        A finite set is read through its own enumeration when it states one,
        and in iteration order otherwise; finitely many points are taken in
        order, with equal points identified.
        """
        match elements:
            case _ if elements in Sets():
                return self._on_finite_set(elements)
            case _:
                return self._on_points(elements)

    def _on_finite_set(self, source: Parent) -> ObjectOfCategory:
        r"""The finite ordered set on the points of the finite set ``source``."""
        size = cardinal(source.cardinality())
        assert size.is_finite(), (
            f"a finite ordered set needs a finite set of points, but {source} has cardinality {size}"
        )
        index_set = finite_ordinal_set(size.finite_value())
        match source:
            case _ if source in EnumeratedSets():
                # The source states its own enumeration, so both directions
                # come from that one isomorphism.
                ranking = source.ranking_map()
                return _object_of(
                    self,
                    index_set=index_set,
                    element_at=lambda position: ranking.inverse()(int(position)),
                    index_of=lambda element: ranking(element) if element in source else None,
                    contains=lambda element: element in source,
                )
            case _:
                return self.from_indexed(
                    index_set,
                    lambda position: next(islice(iter(source), int(position), None)),
                    contains=lambda element: element in source,
                )

    def _on_points(self, points: Iterable[PointT]) -> ObjectOfCategory:
        r"""The finite ordered set on finitely many points, repeated points identified.

        Literal ingress: the points are read once, in order.
        """
        # ``dict.fromkeys`` keeps the first occurrence of each point, in order.
        distinct = tuple(dict.fromkeys(points))
        return self.from_indexed(
            finite_ordinal_set(len(distinct)),
            lambda position: distinct[int(position)],
        )

    def from_indexed(
        self,
        index_set: Parent,
        element_at: Callable[[IndexT], PointT],
        *,
        index_of: Callable[[PointT], IndexT | None] | None = None,
        contains: Callable[[PointT], bool] | None = None,
        name: str | None = None,
    ) -> ObjectOfCategory:
        r"""Construct the finite ordered set enumerated by ``element_at`` on ``index_set``.

        When the caller states no membership decision, membership is Sage's
        enumerated set on the points (``Set``, a hashed ``frozenset``); when it
        states no inverse, the position of a point is read from a hash map of
        the points.  Neither searches the enumeration.
        """
        assert cardinal(index_set.cardinality()).is_finite(), (
            f"a finite ordered set needs a finite index set, but {index_set} is not finite"
        )
        assert index_set in EnumeratedSets(), (
            f"a finite ordered set needs an enumerated index set, but {index_set} is not enumerated"
        )
        if index_of is None or contains is None:
            indices = tuple(index_set)
            points = tuple(element_at(index) for index in indices)
        if index_of is None:
            index_of = dict(zip(points, indices, strict=True)).get
        if contains is None:
            contains = SageSet(points).__contains__
        return _object_of(
            self,
            index_set=index_set,
            element_at=element_at,
            index_of=index_of,
            contains=contains,
            name=name,
        )

    class ParentMethods:
        def filtered(self, predicate, *, name=None):
            r"""Return the ordered subset of this set cut out by ``predicate``."""
            return _FilteredOrderedSet(self, predicate, name=name)

        def union(self, other):
            r"""The finite set of the points of this set and of the finite set ``other``.

            Ordered as this set, followed by the points of ``other`` not
            already present, in the order of ``other``.
            """
            assert other in FiniteSets(), (
                f"the union with {self} is taken here only with a finite set, but {other} is not known to be finite"
            )
            return FiniteOrderedSets()(chain(self, other))

        def intersection(self, other):
            r"""The points of this set that lie in ``other``, in this set's order."""
            return self.filtered(lambda point: point in other)

        def difference(self, other):
            r"""The points of this set that do not lie in ``other``, in this set's order."""
            return self.filtered(lambda point: point not in other)

        def __or__(self, other):
            return self.union(other)

        def __and__(self, other):
            return self.intersection(other)

        def __sub__(self, other):
            return self.difference(other)

        def __eq__(self, other) -> bool:
            r"""Equal to a finite set with the same points; two finite ordered sets also agree in order."""
            match other:
                case _ if other is self:
                    return True
                case _ if other in FiniteOrderedSets():
                    return self.cardinality() == other.cardinality() and all(
                        left == right for left, right in zip(self, other, strict=True)
                    )
                case _ if other in Sets() and other in FiniteSets():
                    return self.cardinality() == cardinal(other.cardinality()) and all(
                        point in other for point in self
                    )
                case _:
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


class _FilteredOrderedSet(FiniteOrderedSets().ObjectType):
    r"""The subset \(\{x\in S : P(x)\}\) of a finite enumerated set \(S\), in the order of \(S\).

    A finite ordered set, enumerated over the ordinal counting the points
    satisfying \(P\), the \(k\)-th point being the \(k\)-th such point of
    \(S\).  The datum this level introduces is \((S, P)\); the enumeration
    is computed from it when the object is constructed, and the inclusion
    into \(S\) is the subobject the set is.
    """

    def __init__(
        self,
        universe: Parent,
        predicate: Callable[[PointT], bool],
        *,
        name: str | None = None,
    ) -> None:
        assert universe in FiniteSets() and universe in EnumeratedSets(), (
            f"the subset of {universe} cut out by a condition is an ordered set only when {universe} is "
            "finite and enumerated"
        )
        self._universe = universe
        self._predicate = predicate

        def survivors():
            return (point for point in universe if predicate(point))

        def element_at(index):
            return next(islice(survivors(), int(index), None))

        def index_of(element):
            if element not in universe or not predicate(universe(element)):
                return None
            return next(
                position
                for position, point in enumerate(survivors())
                if point == element
            )

        super().__init__(
            index_set=finite_ordinal_set(sum(1 for _point in survivors())),
            element_at=element_at,
            index_of=index_of,
            contains=lambda element: element in universe and bool(predicate(universe(element))),
            name=name,
            category=FiniteOrderedSets(),
        )

    def universe(self) -> Sets().ObjectType:
        r"""The set \(S\) this subset is cut out of."""
        return self._universe

    def predicate(self) -> Callable[[PointT], bool]:
        r"""The predicate \(P\) cutting this subset out of \(S\)."""
        return self._predicate

    @cached_method
    def inclusion(self):
        r"""The inclusion \(\{x\in S : P(x)\}\hookrightarrow S\)."""
        from dzack_research.preamble.categories.sets.set_categories import SetInclusion

        return SetInclusion(self, self.universe())

    def __iter__(self):
        return (point for point in self.universe() if self.predicate()(point))

    def _repr_(self):
        return self._name or f"Ordered subset of {self.universe()}"


class _EnumeratedImageSet(OrderedEnumeratedSets().ObjectType):
    r"""An injective image realized by the ordered-enumeration engine.

    No category of images is introduced.  The source, map and inverse are
    exactly the index set and the two directions of the enumeration, stored
    by that owner.  In the infinite case the supplied inverse is a decision
    extension: it returns ``None`` on candidates for which no preimage is
    represented.  Membership also checks the forward equation, so a total
    extension of an inverse cannot admit values outside the image.
    """

    def __init__(
        self,
        source: Sets().ObjectType,
        map_: Callable[[IndexT], PointT],
        inverse: Callable[[PointT], IndexT | None],
    ) -> None:
        match source:
            case _ if source in FiniteSets():
                placement = FiniteOrderedSets()

                def contains(value):
                    return any(map_(point) == value for point in source)
            case _:
                placement = OrderedEnumeratedSets()

                def contains(value):
                    preimage = inverse(value)
                    return preimage in source and map_(source(preimage)) == value

        super().__init__(
            index_set=source,
            element_at=map_,
            index_of=inverse,
            contains=contains,
            category=placement,
        )

    def source_set(self) -> Sets().ObjectType:
        r"""The source of the injective map presenting this image."""
        return self.index_set()

    def image_map(self) -> Callable[[IndexT], PointT]:
        r"""The map presenting this image, which is its enumeration."""
        return self.enumeration()

    def inverse_on_image(self) -> Callable[[PointT], IndexT | None]:
        r"""The selected inverse of the image map."""
        return self.enumeration_inverse()

    def is_injective_image(self) -> bool:
        r"""The supplied inverse satisfies ``g(f(a)) = a`` on the source."""
        return True


def finite_ordered_set[PointT](
    elements: Parent | Iterable[PointT],
) -> FiniteOrderedSets().ObjectType:
    r"""The finite ordered set a finite set or finitely many points present."""
    return FiniteOrderedSets()(elements)
