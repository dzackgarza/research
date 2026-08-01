r"""Set-valued framing witnesses used by the module categories.

The active lattice spike owns the set category and its countability witness
contract.  This module only supplies small parent facades for values returned
by the preamble's module methods; it does not reimplement enumeration or use
Sage's ``rank``/``unrank`` vocabulary as the mathematical interface.
"""

from typing import Any

from sage.categories.sets_cat import Sets as SageSets
from sage.rings.integer import Integer as SageInteger
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets as OwnedSets


def OrderedSets():
    r"""Return the owned root category of sets.

    Kept as a compatibility spelling for callers that used the old preamble
    name.  Ordering is expressed by the ``PartiallyOrdered`` and
    ``TotallyOrdered`` axioms on this category.
    """
    return OwnedSets()


class _Delta:
    r"""The object-level finite ordinals in the simplex category."""

    def __getitem__(self, n: Any) -> TotallyOrderedFiniteSet:
        match n:
            case int() | SageInteger():
                assert n >= -1, f"a simplex ordinal has dimension at least -1, got {n}"
                result = TotallyOrderedFiniteSet(range(int(n) + 1))
                # Sage supplies the implementation; the owned category supplies
                # the preamble's declaration that this is a totally ordered set.
                return refine(result, OwnedSets().TotallyOrdered())
            case _:
                raise TypeError(f"Δ expects a nonnegative integer, got {n!r}")

    def __repr__(self) -> str:
        return "Δ"


# Install the same object on both category spellings used by the preamble:
# ``Sets.Δ`` in notebooks and the active spike's ``OwnedSets.Δ`` in category
# code.  The returned parents are Sage's canonical finite ordered sets, refined
# into the owned total-order category.
_DELTA = _Delta()
setattr(SageSets, "Δ", _DELTA)
setattr(OwnedSets, "Δ", _DELTA)


class TotallyOrderedSet(Parent):
    r"""A parent whose elements have the displayed total order.

    A finite iterable is normalized once into its ordered elements.  An
    existing parent (including the spike's countable parents) is delegated to,
    preserving its native membership and iteration implementation.
    """

    def __init__(self, source: Any) -> None:
        match source:
            case tuple() | list() | range():
                self._source = tuple(source)
                self._cardinality = len(self._source)
            case _:
                self._source = source
                self._cardinality = source.cardinality()
        Parent.__init__(self, category=OwnedSets().TotallyOrdered())

    def __iter__(self):
        return iter(self._source)

    def __contains__(self, element: object) -> bool:
        return element in self._source

    def __getitem__(self, index: Any) -> Any:
        return self._source[index]

    def __len__(self) -> int:
        return len(self._source)

    def cardinality(self) -> Any:
        return self._cardinality

    def list(self) -> list:
        return list(self._source)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TotallyOrderedSet):
            return tuple(self) == tuple(other)
        if isinstance(other, (tuple, list)):
            return tuple(self) == tuple(other)
        return False


# Existing callers used this name before the owned set root was found.  It is
# now an honest totally ordered parent, not a tuple/list facade.
OrderedSet = TotallyOrderedSet
