r"""Owned sets used by the preamble.

The category and its axioms live in the lattice spike.  This module keeps the
preamble inside that category while reusing Sage's concrete set parents.  It
also supplies the canonical finite ordinals and the construction that
transports the order of a finite enumeration.  An arbitrary parent is not
declared ordered merely because it can be iterated.
"""

from collections.abc import Iterable
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
            if source.category().is_subcategory(Sets()):
                return source
            result = SageSet(source)
        case Iterable():
            result = SageSet(source)
        case _:
            raise TypeError(
                f"a set is constructed from a parent or iterable, got {source!r}"
            )
    if result.category().is_subcategory(Sets()):
        return result
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
    if source in Sets():
        return source
    if isinstance(source, (list, tuple)):
        if len(source) != len(set(source)):
            raise ValueError(f"{source!r} contains duplicate elements; a framing set must be a set")
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
        Sets().Finite().TotallyOrdered(),
    )


class _Delta:
    r"""Finite and countable simplex indexing objects \(\Delta[n]\)."""

    def __getitem__(self, n: Any) -> Parent:
        match n:
            case int() | SageInteger():
                assert n >= -1, f"a simplex ordinal has dimension at least -1, got {n}"
                return refine(
                    TotallyOrderedFiniteSet(range(int(n) + 1)),
                    Sets().Finite().TotallyOrdered(),
                )
            case _ if n == _ALEPH[0]:
                return NN
            case _:
                raise TypeError(f"Δ expects an integer, got {n!r}")

    def __repr__(self) -> str:
        return "Δ"


_DELTA = _Delta()
setattr(Sets, "Δ", _DELTA)


class _Aleph:
    r"""Selected aleph cardinal symbols used as ordinal indices."""

    def __getitem__(self, n: Any) -> Any:
        match n:
            case int() | SageInteger():
                if n == 0:
                    return NN.cardinality()
                if n == 1:
                    return RR.cardinality()
                raise ValueError("aleph index is only defined for 0 and 1")
            case _:
                raise TypeError(f"aleph expects an integer, got {n!r}")

    def __repr__(self) -> str:
        return "ℵ"


_ALEPH = _Aleph()
setattr(Sets, "ℵ", _ALEPH)
setattr(Sets, "א", _ALEPH)
