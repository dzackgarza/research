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
from sage.rings.real_mpfr import RR as SageRR
from sage.sets.condition_set import ConditionSet as SageConditionSet
from sage.misc.cachefunc import cached_function
from sage.sets.set import Set_generic
from sage.sets.image_set import ImageSet as SageImageSet
from sage.sets.integer_range import IntegerRange
from sage.sets.set import Set as SageSet
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.cardinals import Cardinal
from sage_lattice_category_spike import lexicon
from sage_lattice_category_spike.objects.sets import Sets

if TYPE_CHECKING:
    # Type-only: the preamble loads into one shared namespace and nothing
    # named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import Cardinal, OrderedSet


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
    return refine(result, Sets())


def ConditionSet(
    universe: "Set",
    *predicates: "Element",
    names: "OrderedSet | None" = None,
) -> "lexicon.Set":
    r"""Construct a predicate-defined object of the owned category of sets."""
    return refine(
        SageConditionSet(universe, *predicates, names=names),
        Sets(),
    )


def ImageSet(
    map_: "Morphism",
    domain_subset: "Set",
    *,
    is_injective: bool | None = None,
    inverse: "Morphism | None" = None,
) -> "lexicon.Set":
    r"""Construct an image object in the owned category of sets."""
    return refine(
        SageImageSet(
            map_,
            domain_subset,
            is_injective=is_injective,
            inverse=inverse,
        ),
        Sets(),
    )


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
    r"""Return a fresh ordered set on ``elements``, owned by its constructor.

    ``finite_ordered_set`` is canonical: $S=S'$ means one set, which is what
    makes $F_R(S)=F_R(S')$ hold on the nose.  A family of *elements* is not
    canonical in that way -- the generators of one module and of another can
    compare equal while being different generators -- so a set of them belongs
    to whatever built it and is not shared by value.
    """
    return refine(
        TotallyOrderedFiniteSet(tuple(elements)),
        Sets().Finite().TotallyOrdered(),
    )


@cached_function
def _ordered_set_on(elements: tuple) -> "lexicon.OrderedSet":
    r"""Return *the* ordered set on this enumeration.

    One object per enumeration, not one per call.  Two ordered sets with the
    same members in the same order are the same set, and things keyed by them
    -- a free module on a generating set, most of all -- are only the same
    object when the key is.  ``TotallyOrderedFiniteSet`` is not a unique
    representation, so without this a module built twice from equal
    generators has two parents that print alike and refuse to coerce.
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
                return refine(NN, Sets().Infinite().TotallyOrdered())
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
                    return NN.cardinality()
                if n == 1:
                    return SageRR.cardinality()
                assert False, "aleph index is only defined for 0 and 1"
            case _:
                assert False, f"aleph expects an integer, got {n!r}"

    def __repr__(self) -> str:
        return "ℵ"


_ALEPH = _Aleph()
setattr(Sets, "ℵ", _ALEPH)
setattr(Sets, "א", _ALEPH)
