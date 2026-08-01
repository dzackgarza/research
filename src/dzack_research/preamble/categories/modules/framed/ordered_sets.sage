r"""Ordered sets used as finite framing sets.

The owned set category lives in the lattice spike.  This module adds only the
canonical finite ordinals and the construction that transports the order of a
finite enumeration.  It does not claim that an arbitrary parent is ordered
merely because it can be iterated.
"""

from typing import Any

from sage.categories.sets_cat import Sets as SageSets
from sage.rings.integer import Integer as SageInteger
from sage.sets.set import Set
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets as OwnedSets


def OrderedSets():
    r"""Return the owned category of partially ordered sets."""
    return OwnedSets().PartiallyOrdered()


def _as_set(source: Any) -> Parent:
    r"""Return ``source`` as a Sage parent."""
    match source:
        case Parent():
            return source
        case _:
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
    assert source in SageSets().Finite(), f"{source} is not a finite set"
    if source in OwnedSets().TotallyOrdered():
        return source
    return refine(
        TotallyOrderedFiniteSet(tuple(source)),
        OwnedSets().TotallyOrdered(),
    )


class _Delta:
    r"""The finite ordinals \(\Delta[n]=\{0<1<\cdots<n\}\)."""

    def __getitem__(self, n: Any) -> TotallyOrderedFiniteSet:
        match n:
            case int() | SageInteger():
                assert n >= -1, f"a simplex ordinal has dimension at least -1, got {n}"
                return refine(
                    TotallyOrderedFiniteSet(range(int(n) + 1)),
                    OwnedSets().TotallyOrdered(),
                )
            case _:
                raise TypeError(f"Δ expects an integer, got {n!r}")

    def __repr__(self) -> str:
        return "Δ"


_DELTA = _Delta()
setattr(SageSets, "Δ", _DELTA)
setattr(OwnedSets, "Δ", _DELTA)
