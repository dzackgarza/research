r"""Owned sets used by the preamble.

The category and its axioms live in the lattice spike.  This module keeps the
preamble inside that category while reusing Sage's concrete set parents.  It
also supplies the canonical finite ordinals and the construction that
transports the order of a finite enumeration.  An arbitrary parent is not
declared ordered merely because it can be iterated.
"""

from typing import TYPE_CHECKING
from sage.rings.semirings.non_negative_integer_semiring import NN
from dzack_research.preamble.refine import refine
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism

from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, TypeVar

from sage.rings.integer import Integer as SageInteger
from sage.rings.integer_ring import ZZ as SageZZ
from sage.sets.condition_set import ConditionSet as SageConditionSet
from sage.sets.set import Set_generic, Set_object_enumerated
from sage.sets.image_set import ImageSet as SageImageSet
from sage.sets.integer_range import IntegerRange
from sage.sets.set import Set as SageSet
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.sets.cardinals import Cardinal
from dzack_research.preamble import lexicon
from dzack_research.preamble.categories.sets.owned_sets import Sets, placement_of

if TYPE_CHECKING:
    # Type-only: the preamble loads into one shared namespace and nothing
    # named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.categories.sets.cardinals import Cardinal


def Set(source: Parent | Iterable[Element]) -> "lexicon.Set":
    r"""Return ``source`` as an object of the owned category of sets."""
    match source:
        case Parent():
            if source.category().is_subcategory(Sets()):
                return source
            result = SageSet(source)
        case Iterable():
            result = SageSet(source)
        case _:
            assert False, (
                f"a set is constructed from a parent or iterable, got {source!r}"
            )
    if result.category().is_subcategory(Sets()):
        return result
    return refine(result, placement_of(result))


def ConditionSet(
    universe: "Set",
    *predicates: "Element",
    names: "OrderedSet | None" = None,
) -> "lexicon.Set":
    r"""Construct a predicate-defined object of the owned category of sets."""
    result = SageConditionSet(universe, *predicates, names=names)
    return refine(result, placement_of(result))


def ImageSet(
    map_: "Morphism",
    domain_subset: "Set",
    *,
    is_injective: bool | None = None,
    inverse: "Morphism | None" = None,
) -> "lexicon.Set":
    r"""Construct an image object in the owned category of sets."""
    result = SageImageSet(
        map_,
        domain_subset,
        is_injective=is_injective,
        inverse=inverse,
    )
    return refine(result, placement_of(result))


class PowerSetParent(UniqueRepresentation, Parent):
    r"""The set of all subsets of a finite or countable set."""

    element_class = Set_object_enumerated

    def __init__(self, source: "lexicon.Set") -> None:
        if source not in Sets().Countable():
            source = _as_set(source)
        assert source in Sets().Countable(), (
            "the owned cardinal graph currently represents power sets only "
            "for finite or countably infinite sets"
        )
        self._source = source
        category = (
            Sets().Finite()
            if source in Sets().Finite()
            else Sets().Uncountable()
        )
        Parent.__init__(self, category=category)

    def source(self) -> "lexicon.Set":
        return self._source

    def _element_constructor_(self, members: Iterable) -> "lexicon.Set":
        subset = self.element_class(members)
        assert all(member in self._source for member in subset), (
            "every member of a subset must lie in its source set"
        )
        return subset

    def __call__(self, members: Iterable) -> "lexicon.Set":
        return self._element_constructor_(members)

    def __contains__(self, candidate: object) -> bool:
        if candidate is self._source:
            return True
        if not isinstance(candidate, Iterable):
            return False
        return all(member in self._source for member in candidate)

    def __iter__(self):
        assert self._source in Sets().Finite(), (
            "an uncountable power set has no enumeration"
        )
        from sage.combinat.subset import Subsets as SageSubsets

        yield from SageSubsets(self._source)

    def cardinality(self) -> Cardinal:
        from dzack_research.preamble.categories.sets.cardinals import Cardinal as OwnedCardinal
        from dzack_research.preamble.categories.sets.cardinals import continuum

        if self._source not in Sets().Finite():
            return continuum
        return OwnedCardinal(2 ** int(self._source.cardinality()))

    def _repr_(self) -> str:
        return f"Power set of {self._source}"


class FixedCardinalitySubsetsParent(UniqueRepresentation, Parent):
    r"""The subsets of ``S`` with one fixed finite cardinality.

    The finite case delegates to Sage's mature ``sage.combinat.subset.Subsets``.
    The countable case extends its ordering by increasing greatest index.
    """

    element_class = Set_object_enumerated

    def __init__(self, source: "lexicon.Set", cardinality: int) -> None:
        if source not in Sets().Countable():
            source = _as_set(source)
        cardinality = SageInteger(cardinality)
        assert cardinality >= 0, "a subset cardinality is nonnegative"
        assert source in Sets().Countable(), (
            "fixed-cardinality subsets currently require a chosen countable enumeration"
        )
        self._source = source
        self._subset_cardinality = cardinality
        if source in Sets().Finite():
            category = Sets().Finite()
        elif cardinality == 0:
            category = Sets().Finite()
        else:
            category = Sets().Countable().Infinite()
        Parent.__init__(self, category=category)

    def source(self) -> "lexicon.Set":
        return self._source

    def subset_cardinality(self) -> SageInteger:
        return self._subset_cardinality

    def _element_constructor_(self, members: Iterable) -> "lexicon.Set":
        subset = self.element_class(members)
        assert len(subset) == self._subset_cardinality, (
            f"a member has cardinality {self._subset_cardinality}"
        )
        assert all(member in self._source for member in subset), (
            "every member of a subset must lie in its source set"
        )
        return subset

    def __call__(self, members: Iterable) -> "lexicon.Set":
        return self._element_constructor_(members)

    def __contains__(self, candidate: object) -> bool:
        if not isinstance(candidate, Iterable):
            return False
        subset = SageSet(candidate)
        return (
            len(subset) == self._subset_cardinality
            and all(member in self._source for member in subset)
        )

    def __iter__(self):
        from sage.combinat.subset import Subsets as SageSubsets

        if self._source in Sets().Finite():
            yield from SageSubsets(self._source, self._subset_cardinality)
            return
        if self._subset_cardinality == 0:
            yield self.element_class(())
            return

        preceding = []
        for maximum in self._source:
            if len(preceding) >= self._subset_cardinality - 1:
                for initial in SageSubsets(
                    tuple(preceding),
                    self._subset_cardinality - 1,
                ):
                    yield self.element_class(tuple(initial) + (maximum,))
            preceding.append(maximum)

    def _repr_(self) -> str:
        return (
            f"Subsets of {self._source} of cardinality "
            f"{self._subset_cardinality}"
        )


class FiniteSubsetsParent(UniqueRepresentation, Parent):
    r"""The set of all finite subsets of a countable set.

    The finite case delegates to Sage's mature ``sage.combinat.subset.Subsets``.
    The countable case extends it by increasing greatest index.
    """

    element_class = Set_object_enumerated

    def __init__(self, source: "lexicon.Set") -> None:
        if source not in Sets().Countable():
            source = _as_set(source)
        assert source in Sets().Countable(), (
            "finite subsets currently require a chosen countable enumeration"
        )
        self._source = source
        category = (
            Sets().Finite()
            if source in Sets().Finite()
            else Sets().Countable().Infinite()
        )
        Parent.__init__(self, category=category)

    def source(self) -> "lexicon.Set":
        return self._source

    def _element_constructor_(self, members: Iterable) -> "lexicon.Set":
        subset = self.element_class(members)
        assert all(member in self._source for member in subset), (
            "every member of a subset must lie in its source set"
        )
        return subset

    def __call__(self, members: Iterable) -> "lexicon.Set":
        return self._element_constructor_(members)

    def __contains__(self, candidate: object) -> bool:
        if not isinstance(candidate, Iterable):
            return False
        subset = SageSet(candidate)
        return all(member in self._source for member in subset)

    def __iter__(self):
        from sage.combinat.subset import Subsets as SageSubsets

        if self._source in Sets().Finite():
            yield from SageSubsets(self._source)
            return

        yield self.element_class(())
        preceding = []
        for maximum in self._source:
            for initial in SageSubsets(tuple(preceding)):
                yield self.element_class(tuple(initial) + (maximum,))
            preceding.append(maximum)

    def _repr_(self) -> str:
        return f"Finite subsets of {self._source}"


@cached_function
def PowerSet(source: "lexicon.Set") -> PowerSetParent:
    return PowerSetParent(source)


@cached_function
def SubsetsOfSize(
    source: "lexicon.Set",
    cardinality: int,
) -> FixedCardinalitySubsetsParent:
    return FixedCardinalitySubsetsParent(source, cardinality)


@cached_function
def FiniteSubsets(source: "lexicon.Set") -> FiniteSubsetsParent:
    return FiniteSubsetsParent(source)


E = TypeVar("E", bound=Element)


def _as_set(source: lexicon.Set[E] | lexicon.OrderedSet[E]) -> "lexicon.Set[E]":
    # Membership in ``Sets()`` is not the question: every parent is in it, so
    # asking that returned the semiring $\NN$ where the set of its elements
    # was wanted.  What is asked is whether the source already *is* the set of
    # its elements, and a parent carrying structure is not.
    if isinstance(source, Set_generic):
        return source
    return Set(source)


def finite_ordered_set(
    source: lexicon.Set[E] | lexicon.OrderedSet[E] | Sequence[E],
) -> "lexicon.OrderedSet[E]":
    r"""Transport the displayed finite enumeration to a total order.

    The input is a mathematical set: an unordered set of the owned vocabulary
    (a ``Sets()``-member parent or a finite collection) or a set with a
    distinguished linear order -- a generator tuple, in the lexicon's sense.

    Imposing a total order means supplying its data, not asking Sage to sort.
    An ordered enumeration is that data: the enumeration itself is the order,
    and it is handed to ``TotallyOrderedFiniteSet`` untouched -- never
    coerced through ``Set``, which would discard it.  A repeated member is
    one member, so an enumeration keeps each element at its first position:
    \(\{1,2,1\}=\{1,2\}\).  An unordered finite set is given the total order
    of its own iteration.  A totally ordered finite parent is returned
    unchanged.  The result implements the order through Sage's
    ``TotallyOrderedFiniteSet``; category placement is not standing in for
    the relation.
    """
    if isinstance(source, (list, tuple)):
        return _ordered_set_on(tuple(dict.fromkeys(_owned_members(source))))
    source = _as_set(source)
    assert source in Sets().Finite(), f"{source} is not a finite set"
    if source in Sets().TotallyOrdered():
        return source
    return _ordered_set_on(tuple(_owned_members(source)))


def _owned_members(members) -> tuple:
    r"""Return the members as this preamble's objects.

    A Python ``int`` and a Sage ``Integer`` print alike, compare equal and
    hash together, so a set built from either answers to the same cache key --
    and the canonical set then holds whichever spelling reached it first.
    That made a set's members depend on construction order, and a morphism out
    of such a set returned a bare ``int`` where an ``Element`` was required.
    The repo bans that fork elsewhere for the same reason; this is where it
    would otherwise enter.
    """
    return tuple(
        SageZZ(member)
        if isinstance(member, int) and not isinstance(member, Element)
        else member
        for member in members
    )


def ordered_set_owned_by(elements) -> "lexicon.OrderedSet":
    r"""Return the ordered set on ``elements``, in their given order.

    Not a *fresh* set: ``TotallyOrderedFiniteSet`` is a unique
    representation, so equal members in the same order give one object no
    matter who asks.  This spelling exists because its callers hold elements
    rather than labels and do not want them run through the member
    normalization that ``finite_ordered_set`` applies to raw input.
    """
    return refine(
        TotallyOrderedFiniteSet(tuple(elements)),
        Sets().Finite().TotallyOrdered(),
    )


def _ordered_set_on(elements: tuple) -> "lexicon.OrderedSet":
    r"""Return *the* ordered set on this enumeration.

    One object per enumeration, which is what makes $F_R(S)=F_R(S')$ hold
    when $S=S'$.  The uniqueness is Sage's: ``TotallyOrderedFiniteSet``
    defers to ``FiniteEnumeratedSet``, which is a unique representation, so
    equal members in the same order already give one object.  Caching here
    on top of that bought nothing, and a mutation check said so.
    """
    return refine(
        TotallyOrderedFiniteSet(elements),
        Sets().Finite().TotallyOrdered(),
    )


class _Delta:
    r"""Finite and countable simplex indexing objects \(\Delta[n]\)."""

    def __getitem__(self, n: "Integer") -> "lexicon.OrderedSet[Integer]":
        match n:
            case int() | SageInteger():
                assert n >= -1, f"a simplex ordinal has dimension at least -1, got {n}"
                # IntegerRange, not range: the vertices of Δ[n] are the
                # integers 0..n, and Sage's IntegerRange yields Integer.
                # Python's range yields int, a different object that prints
                # the same, and the repo bans that fork.
                # Through the same constructor as every other ordered set:
                # $\Delta[0]$ and the ordered set on $(0)$ are one set, and
                # anything keyed by them -- a free module, above all -- is the
                # same object only when they are.
                return _ordered_set_on(
                    tuple(IntegerRange(SageZZ(n) + SageZZ.one()))
                )
            case _ if n == _ALEPH[0]:
                # The countable simplex is an owned ordered set like every
                # other Delta[n]; handing back a bare Sage NN would leave the
                # one infinite case outside the vocabulary the finite ones use.
                return refine(
                    NN,
                    Sets().Countable().Infinite().TotallyOrdered(),
                )
            case _:
                assert False, f"Δ expects an integer, got {n!r}"

    def __repr__(self) -> str:
        return "Δ"


_DELTA = _Delta()
setattr(Sets, "Δ", _DELTA)


class _Aleph:
    r"""Selected aleph cardinal symbols used as ordinal indices."""

    def __getitem__(self, n: "Integer") -> "Cardinal":
        match n:
            case int() | SageInteger():
                if n == 0:
                    from dzack_research.preamble.categories.sets.cardinals import aleph0

                    return aleph0
                if n == 1:
                    from dzack_research.preamble.categories.sets.cardinals import continuum

                    return continuum
                assert False, "aleph index is only defined for 0 and 1"
            case _:
                assert False, f"aleph expects an integer, got {n!r}"

    def __repr__(self) -> str:
        return "ℵ"


_ALEPH = _Aleph()
setattr(Sets, "ℵ", _ALEPH)
setattr(Sets, "א", _ALEPH)
