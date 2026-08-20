r"""Owned sets used by the preamble.

The category and its axioms live in the lattice spike.  This module keeps the
preamble inside that category while reusing Sage's concrete set parents.  It
also supplies the canonical finite ordinals and the construction that
transports the order of a finite enumeration.  An arbitrary parent is not
declared ordered merely because it can be iterated.
"""

from __future__ import annotations

from sage.rings.semirings.non_negative_integer_semiring import NN
from dzack_research.preamble.refine import refine

from collections.abc import Callable, Hashable, Iterable, Iterator, Sequence
from typing import TYPE_CHECKING, TypeVar

from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism, SetMorphism
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
from dzack_research.preamble.categories.sets.owned_sets import (
    Sets,
    placement_of,
    PosetHomset,
    PosetMorphism,
)

if TYPE_CHECKING:
    # Type-only: the preamble loads into one shared namespace and nothing
    # named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from sage.structure.parent import ElementConstructorInput
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
    universe: "lexicon.Set",
    *predicates: "Element",
    names: "OrderedSet | None" = None,
) -> "lexicon.Set":
    r"""Construct a predicate-defined object of the owned category of sets."""
    result = SageConditionSet(universe, *predicates, names=names)
    return refine(result, placement_of(result))


def ImageSet(
    map_: "Morphism",
    domain_subset: "lexicon.Set",
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


if TYPE_CHECKING:
    # These parents' elements are Sage sets, not ``Element``s.  ``Parent`` is a
    # cython extension type and is not subscriptable at runtime.
    SubsetsParent = Parent[Set_object_enumerated]
else:
    SubsetsParent = Parent


def _has_canonical_set_inclusion(domain: Parent, codomain: Parent) -> bool:
    r"""Return whether the standard catalogue supplies ``domain -> codomain``.

    Sage defines ``NN`` as the nonnegative integers and ``ZZ`` as the integer
    ring.  The inclusion below is the set map induced by those canonical Sage
    parents; it is not inferred from enumeration.
    """
    from dzack_research.preamble.categories.rings.rings import engine_ring
    from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet

    match codomain:
        case UnderlyingSet():
            return domain is NN and engine_ring(codomain.structured_parent()) is SageZZ
        case _:
            return False


class PowerSetParent(SubsetsParent):
    r"""The power object of a set.

    Its elements are subobjects of the base set.  Each element has an inclusion
    into that set and the equivalent characteristic morphism into ``Delta[1]``.
    """

    def __init__(self, base_set: "lexicon.Set") -> None:
        self._base_set = base_set
        category = (
            Sets().Finite()
            if self.cardinality().is_finite()
            else Sets().Uncountable()
        )
        Parent.__init__(self, category=category)

    def base_set(self) -> "lexicon.Set":
        return self._base_set

    def characteristic_homset(self) -> Homset:
        r"""Return ``Hom(base_set, Delta[1])``."""
        return Hom(self._base_set, Sets.Δ[1], Sets())

    def _from_subset(
        self,
        subset: "lexicon.Set",
        characteristic_morphism: SetMorphism,
    ) -> PowerSetElement:
        inclusion = SetMorphism(
            Hom(subset, self._base_set, Sets()),
            lambda member: self._base_set(member),
        )
        return self.element_class(self, inclusion, characteristic_morphism)

    def _subset_from_predicate(
        self,
        predicate: "Callable[[Element], bool]",
    ) -> PowerSetElement:
        subset = ConditionSet(self._base_set, predicate)
        truth_values = Sets.Δ[1]
        characteristic_morphism = SetMorphism(
            self.characteristic_homset(),
            lambda member: truth_values(SageInteger(predicate(member))),
        )
        return self._from_subset(subset, characteristic_morphism)

    def _subset_from_finite_members(
        self,
        members: "lexicon.Set",
    ) -> FinitePowerSetElement:
        subset = ConditionSet(self._base_set, lambda member: member in members)
        truth_values = Sets.Δ[1]
        characteristic_morphism = SetMorphism(
            self.characteristic_homset(),
            lambda member: truth_values(SageInteger(member in members)),
        )
        inclusion = SetMorphism(
            Hom(subset, self._base_set, Sets()),
            lambda member: self._base_set(member),
        )
        return FinitePowerSetElement(
            self,
            inclusion,
            characteristic_morphism,
            frozenset(members),
        )

    def _element_constructor_(
        self,
        candidate: "PowerSetElement | Parent | Iterable[Element]",
    ) -> PowerSetElement:
        match candidate:
            case PowerSetElement():
                assert candidate.inclusion().codomain() is self._base_set, (
                    "a subset must have the required inclusion codomain"
                )
                return candidate
            case Parent() if candidate is self._base_set:
                characteristic = SetMorphism(
                    self.characteristic_homset(),
                    lambda member: Sets.Δ[1](1),
                )
                return self.element_class(
                    self,
                    Hom(self._base_set, self._base_set, Sets()).identity(),
                    characteristic,
                )
            case Parent() if _has_canonical_set_inclusion(candidate, self._base_set):
                truth_values = Sets.Δ[1]
                characteristic_morphism = SetMorphism(
                    self.characteristic_homset(),
                    lambda member: truth_values(
                        SageInteger(member in candidate)
                    ),
                )
                return self._from_subset(candidate, characteristic_morphism)
            case Parent() if candidate in Sets().Finite():
                assert all(member in self._base_set for member in candidate), (
                    "every member of a subset must lie in its base set"
                )
                return self._subset_from_finite_members(candidate)
            case Iterable():
                members = Set(candidate)
                assert all(member in self._base_set for member in members), (
                    "every member of a subset must lie in its base set"
                )
                return self._subset_from_finite_members(members)
            case _:
                assert False, f"{candidate!r} does not present a subset of {self._base_set}"

    def __contains__(
        self,
        candidate: "PowerSetElement | Parent | Iterable[Element]",
    ) -> bool:
        match candidate:
            case PowerSetElement():
                return candidate.inclusion().codomain() is self._base_set
            case Parent() if candidate in Sets().Finite():
                return all(member in self._base_set for member in candidate)
            case Parent():
                return candidate is self._base_set or _has_canonical_set_inclusion(
                    candidate, self._base_set
                )
            case Iterable():
                return all(member in self._base_set for member in candidate)
            case _:
                return False

    def from_predicate(
        self,
        predicate: "Callable[[Element], bool]",
    ) -> PowerSetElement:
        r"""Return the subobject defined by ``predicate``."""
        return self._subset_from_predicate(predicate)

    def from_characteristic_morphism(
        self,
        characteristic_morphism: SetMorphism,
    ) -> PowerSetElement:
        r"""Return the subset classified by ``base_set -> Delta[1]``."""
        assert characteristic_morphism.parent() is self.characteristic_homset(), (
            "a characteristic morphism must lie in Hom(base_set, Delta[1])"
        )
        subset = ConditionSet(
            self._base_set,
            lambda member: characteristic_morphism(member) == Sets.Δ[1](1),
        )
        return self._from_subset(subset, characteristic_morphism)

    def top(self) -> PowerSetElement:
        r"""Return the greatest subset, the base set itself."""
        return self(self._base_set)

    def bottom(self) -> PowerSetElement:
        r"""Return the empty subset."""
        return self(())

    def inverse_image_morphism(self, morphism: Morphism) -> SetMorphism:
        r"""Return the inverse-image map ``P(codomain) -> P(domain)``."""
        assert morphism.codomain() is self._base_set, (
            "inverse image requires the morphism codomain to equal the base set"
        )
        domain_power_set = PowerSet(morphism.domain())
        return SetMorphism(
            Hom(self, domain_power_set, Sets()),
            lambda subset: domain_power_set.from_predicate(
                lambda member: morphism(member) in subset
            ),
        )

    def direct_image_morphism(self, morphism: Morphism) -> SetMorphism:
        r"""Return the direct-image map ``P(domain) -> P(codomain)``."""
        assert morphism.domain() is self._base_set, (
            "direct image requires the morphism domain to equal the base set"
        )
        codomain_power_set = PowerSet(morphism.codomain())
        return SetMorphism(
            Hom(self, codomain_power_set, Sets()),
            lambda subset: self._finite_direct_image(
                subset,
                morphism,
                codomain_power_set,
            ),
        )

    def _finite_direct_image(
        self,
        subset: PowerSetElement,
        morphism: Morphism,
        codomain_power_set: PowerSetParent,
    ) -> PowerSetElement:
        assert subset.underlying_set() in Sets().Finite(), (
            "direct-image membership requires a finite subset or an image decision procedure"
        )
        return codomain_power_set(tuple(morphism(member) for member in subset))

    def __iter__(self) -> "Iterator[PowerSetElement]":
        assert self._base_set in Sets().Finite(), (
            "an uncountable power set has no enumeration"
        )
        from sage.combinat.subset import Subsets as SageSubsets

        for members in SageSubsets(self._base_set):
            yield self(members)

    def cardinality(self) -> Cardinal:
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        return cardinal(2) ** self._base_set.cardinality()

    def _repr_(self) -> str:
        return f"Power set of {self._base_set}"


class PowerSetElement(Element):
    r"""A subobject of ``X`` represented by ``A -> X`` and ``X -> Delta[1]``."""

    def __init__(
        self,
        parent: PowerSetParent,
        inclusion: Morphism,
        characteristic_morphism: SetMorphism,
    ) -> None:
        Element.__init__(self, parent)
        self._inclusion = inclusion
        self._characteristic_morphism = characteristic_morphism

    def inclusion(self) -> Morphism:
        r"""Return the monomorphism that defines this subobject."""
        return self._inclusion

    def underlying_set(self) -> "lexicon.Set":
        r"""Return the domain of the defining monomorphism."""
        return self._inclusion.domain()

    def characteristic_morphism(self) -> SetMorphism:
        r"""Return the classifying morphism into ``Delta[1]``."""
        return self._characteristic_morphism

    def __contains__(self, member: Element) -> bool:
        return self._characteristic_morphism(member) == Sets.Δ[1](1)

    def __iter__(self) -> Iterator[Element]:
        return iter(self.underlying_set())

    def _decidable_finite_equality(self, other: PowerSetElement) -> bool:
        base_set = self.parent().base_set()
        match base_set in Sets().Finite():
            case True:
                return all(
                    (member in self) == (member in other)
                    for member in base_set
                )
            case False:
                match self, other:
                    case FinitePowerSetElement(), FinitePowerSetElement():
                        return self.members() == other.members()
                    case _:
                        return False

    def __eq__(self, other: "PowerSetElement") -> bool:
        match other:
            case _ if self is other:
                return True
            case PowerSetElement() if (
                self.inclusion().codomain() is not other.inclusion().codomain()
            ):
                return False
            case PowerSetElement() if (
                self._characteristic_morphism is other._characteristic_morphism
            ):
                return True
            case PowerSetElement():
                return self._decidable_finite_equality(other)
            case _:
                return False

    def __ne__(self, other: "PowerSetElement") -> bool:
        return not self == other

    def __hash__(self) -> int:
        base_set = self.parent().base_set()
        match base_set in Sets().Finite():
            case True:
                return hash(
                    (
                        self.parent(),
                        tuple(member in self for member in base_set),
                    )
                )
            case False:
                return hash(self._characteristic_morphism)

    def __le__(self, other: PowerSetElement) -> bool:
        assert self.inclusion().codomain() is other.inclusion().codomain(), (
            "subset order requires a common inclusion codomain"
        )
        base_set = self.parent().base_set()
        match base_set in Sets().Finite(), self:
            case True, _:
                return all(
                    member not in self or member in other for member in base_set
                )
            case False, FinitePowerSetElement():
                return all(member in other for member in self.members())
            case _:
                assert False, (
                    "this subset relation has no available decision procedure"
                )

    def union(self, other: PowerSetElement) -> PowerSetElement:
        return self.parent().from_predicate(
            lambda member: member in self or member in other
        )

    def intersection(self, other: PowerSetElement) -> PowerSetElement:
        return self.parent().from_predicate(
            lambda member: member in self and member in other
        )

    def difference(self, other: PowerSetElement) -> PowerSetElement:
        return self.parent().from_predicate(
            lambda member: member in self and member not in other
        )

    def symmetric_difference(self, other: PowerSetElement) -> PowerSetElement:
        return self.parent().from_predicate(
            lambda member: (member in self) != (member in other)
        )

    def complement(self) -> PowerSetElement:
        return self.parent().from_predicate(lambda member: member not in self)

    def _repr_(self) -> str:
        return f"Subobject of {self.inclusion().codomain()} defined by {self.underlying_set()}"


class FinitePowerSetElement(PowerSetElement):
    r"""A power-set element supplied by an explicit finite subset."""

    def __init__(
        self,
        parent: PowerSetParent,
        inclusion: Morphism,
        characteristic_morphism: SetMorphism,
        members: frozenset[Element],
    ) -> None:
        PowerSetElement.__init__(
            self,
            parent,
            inclusion,
            characteristic_morphism,
        )
        self._members = members

    def members(self) -> frozenset[Element]:
        return self._members

    def __hash__(self) -> int:
        base_set = self.parent().base_set()
        match base_set in Sets().Finite():
            case True:
                return PowerSetElement.__hash__(self)
            case False:
                return hash((self.parent(), self._members))


PowerSetParent.Element = PowerSetElement


class FixedCardinalitySubsetsParent(UniqueRepresentation, SubsetsParent):
    r"""The subsets of ``S`` with one fixed finite cardinality.

    The finite case delegates to Sage's mature ``sage.combinat.subset.Subsets``.
    The countable case extends its ordering by increasing greatest index.
    """

    element_class = Set_object_enumerated

    def __init__(self, source: "lexicon.Set", cardinality: "Integer") -> None:
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

    def cardinality(self) -> Cardinal:
        r"""Return \(\bigl|\{A\subseteq S:|A|=k\}\bigr|\).

        Stated from this object's own data, never counted: for finite \(S\)
        it is \(\binom{|S|}{k}\), and for countably infinite \(S\) there are
        \(\aleph_0\) subsets of each positive size \(k\) (choose the largest
        member freely), while the empty subset is the only one of size zero.
        """
        from sage.arith.misc import binomial

        from dzack_research.preamble.categories.sets.cardinals import aleph0, cardinal

        if self._source in Sets().Finite():
            return cardinal(
                binomial(SageZZ(self._source.cardinality()), self._subset_cardinality)
            )
        if self._subset_cardinality == 0:
            return cardinal(1)
        return aleph0

    def subset_cardinality(self) -> SageInteger:
        cardinality: SageInteger = self._subset_cardinality
        return cardinality

    def _element_constructor_(
        self,
        members: Iterable[Element],
    ) -> Set_object_enumerated:
        subset = self.element_class(members)
        assert len(subset) == self._subset_cardinality, (
            f"a member has cardinality {self._subset_cardinality}"
        )
        assert all(member in self._source for member in subset), (
            "every member of a subset must lie in its source set"
        )
        return subset

    def __call__(
        self,
        x: ElementConstructorInput = (),
        *arguments: ElementConstructorInput,
        **keywords: ElementConstructorInput,
    ) -> Set_object_enumerated:
        assert isinstance(x, Iterable), "a subset is built from its members"
        return self._element_constructor_(x)

    def __contains__(self, candidate: ElementConstructorInput) -> bool:
        if not isinstance(candidate, Iterable):
            return False
        subset = SageSet(candidate)
        return (
            len(subset) == self._subset_cardinality
            and all(member in self._source for member in subset)
        )

    def __iter__(self) -> Iterator[Set_object_enumerated]:
        from sage.combinat.subset import Subsets as SageSubsets

        if self._source in Sets().Finite():
            yield from SageSubsets(self._source, self._subset_cardinality)
            return
        if self._subset_cardinality == 0:
            yield self.element_class(())
            return

        preceding: list[Element] = []
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


class FiniteSubsetsParent(UniqueRepresentation, SubsetsParent):
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

    def cardinality(self) -> Cardinal:
        r"""Return \(\bigl|\{A\subseteq S:A\text{ finite}\}\bigr|\).

        Stated from this object's own data, never counted: for finite \(S\)
        every subset is finite, so this is the whole power set, \(2^{|S|}\).
        For countably infinite \(S\) the finite subsets are countable -- a
        finite subset of \(\mathbb N\) is a finite binary string -- so there
        are \(\aleph_0\) of them.
        """
        from dzack_research.preamble.categories.sets.cardinals import aleph0, cardinal

        if self._source in Sets().Finite():
            return cardinal(2) ** self._source.cardinality()
        return aleph0

    def _element_constructor_(
        self,
        members: Iterable[Element],
    ) -> Set_object_enumerated:
        subset = self.element_class(members)
        assert all(member in self._source for member in subset), (
            "every member of a subset must lie in its source set"
        )
        return subset

    def __call__(
        self,
        x: ElementConstructorInput = (),
        *arguments: ElementConstructorInput,
        **keywords: ElementConstructorInput,
    ) -> Set_object_enumerated:
        assert isinstance(x, Iterable), "a subset is built from its members"
        return self._element_constructor_(x)

    def __contains__(self, candidate: ElementConstructorInput) -> bool:
        if not isinstance(candidate, Iterable):
            return False
        subset = SageSet(candidate)
        return all(member in self._source for member in subset)

    def __iter__(self) -> Iterator[Set_object_enumerated]:
        from sage.combinat.subset import Subsets as SageSubsets

        if self._source in Sets().Finite():
            yield from SageSubsets(self._source)
            return

        yield self.element_class(())
        preceding: list[Element] = []
        for maximum in self._source:
            for initial in SageSubsets(tuple(preceding)):
                yield self.element_class(tuple(initial) + (maximum,))
            preceding.append(maximum)

    def _repr_(self) -> str:
        return f"Finite subsets of {self._source}"


@cached_function
def _cached_power_set(base_set: "lexicon.Set") -> PowerSetParent:
    return PowerSetParent(base_set)


def PowerSet(base_set: "lexicon.Set") -> PowerSetParent:
    from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet

    match base_set.category().is_subcategory(Sets()):
        case True:
            underlying_set = base_set
        case False:
            underlying_set = UnderlyingSet(base_set)
    match underlying_set:
        case SageImageSet():
            return PowerSetParent(underlying_set)
        case Hashable():
            return _cached_power_set(underlying_set)
        case _:
            return PowerSetParent(underlying_set)


@cached_function
def SubsetsOfSize(
    source: "lexicon.Set",
    cardinality: "Integer",
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


def _owned_members(
    members: "Iterable[Element | int]",
) -> tuple[Element, ...]:
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
        SageZZ(member) if isinstance(member, int) else member
        for member in members
    )


def ordered_set_owned_by[E: Element](
    elements: "Iterable[E]",
) -> "lexicon.OrderedSet[E]":
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

    def __getitem__(
        self, n: "Integer | int | Cardinal"
    ) -> "lexicon.OrderedSet[Integer]":
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
    r"""The finite-index aleph cardinals."""

    def __getitem__(self, n: "Integer | int") -> "Cardinal":
        match n:
            case int() | SageInteger():
                from dzack_research.preamble.categories.sets.cardinals import aleph

                return aleph(n)
            case _:
                assert False, f"aleph expects an integer, got {n!r}"

    def __repr__(self) -> str:
        return "ℵ"


_ALEPH = _Aleph()
setattr(Sets, "ℵ", _ALEPH)
setattr(Sets, "א", _ALEPH)
