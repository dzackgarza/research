r"""Owned sets used by the preamble.

The category and its axioms live in the lattice spike.  This module keeps the
preamble inside that category while reusing Sage's concrete set parents.  It
also supplies the canonical finite ordinals and the construction that
transports the order of a finite enumeration.  An arbitrary parent is not
declared ordered merely because it can be iterated.
"""

from typing import Any

from sage.rings.integer import Integer as SageInteger
from sage.sets.condition_set import ConditionSet as SageConditionSet
from sage.sets.image_set import ImageSet as SageImageSet
from sage.sets.set import Set as SageSet
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets


def Set(source: Any) -> Parent:
    r"""Return ``source`` as an object of the owned category of sets."""
    match source:
        case Parent():
            result = source
        case _:
            result = SageSet(source)
    return refine(result, Sets())


def ConditionSet(
    universe: Any,
    *predicates: Any,
    names: Any = None,
) -> Parent:
    r"""Construct a predicate-defined object of the owned category of sets."""
    return refine(
        SageConditionSet(universe, *predicates, names=names),
        Sets(),
    )


def ImageSet(
    map_: Any,
    domain_subset: Any,
    *,
    is_injective: Any = None,
    inverse: Any = None,
) -> Parent:
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


def _as_set(source: Any) -> Parent:
    return Set(source)


def finite_ordered_set(source: Any) -> TotallyOrderedFiniteSet:
    r"""Transport the displayed finite enumeration to a total order.

    An already totally ordered finite parent is returned unchanged.  Otherwise
    the order is fixed now, at construction, by the iteration order of the
    supplied finite set.  The result implements the order through Sage's
    ``TotallyOrderedFiniteSet``; category placement is not standing in for the
    relation.
    """
    source = _as_set(source)
    assert source in Sets().Finite(), f"{source} is not a finite set"
    if source in Sets().TotallyOrdered():
        return source
    return refine(
        TotallyOrderedFiniteSet(tuple(source)),
        Sets().TotallyOrdered(),
    )


class _Delta:
    r"""The finite ordinals \(\Delta[n]=\{0<1<\cdots<n\}\)."""

    def __getitem__(self, n: Any) -> TotallyOrderedFiniteSet:
        match n:
            case int() | SageInteger():
                assert n >= -1, f"a simplex ordinal has dimension at least -1, got {n}"
                return refine(
                    TotallyOrderedFiniteSet(range(int(n) + 1)),
                    Sets().TotallyOrdered(),
                )
            case _:
                raise TypeError(f"Δ expects an integer, got {n!r}")

    def __repr__(self) -> str:
        return "Δ"


_DELTA = _Delta()
setattr(Sets, "Δ", _DELTA)
