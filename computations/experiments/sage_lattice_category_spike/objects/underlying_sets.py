r"""Underlying sets: the object action of the structure-forgetting functors.

``UnderlyingSet(X)`` is the set ``U(X)`` of a structured parent ``X`` —
the same elements with the operations forgotten, realized as a facade over
``X`` and placed in the owned ``Sets()`` axioms by translating the set
axioms declared on ``X``'s category. The structured parent supplies only
its enumeration (the witness data); every generic set behavior of ``U(X)``
then resolves through CP1's owners, and structured categories forward
their set behavior here instead of inheriting it — composition, not
subcategory inclusion (a forgetful functor is faithful, not monic).
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING, cast

from ..lexicon import SageParent, SageUniqueRepresentation
from .sets import Sets

if TYPE_CHECKING:
    from .cardinals import Cardinal

_SET_AXIOM_NAMES = ("Finite", "Infinite", "Countable", "Uncountable")


def _translated_placement(structured: SageParent) -> Sets:
    r"""The owned ``Sets()`` placement carried by a structured parent's
    declared set axioms. Contradictory declarations are refused by the
    owned axiom guards at translation time."""
    declared = frozenset(structured.category().axioms()) & frozenset(_SET_AXIOM_NAMES)
    placement = Sets()
    if "Finite" in declared:
        return placement.Finite()
    if "Countable" in declared:
        placement = placement.Countable()
    if "Uncountable" in declared:
        placement = placement.Uncountable()
    elif "Infinite" in declared:
        placement = placement.Infinite()
    return placement


class UnderlyingSet(SageUniqueRepresentation, SageParent):
    r"""The underlying set ``U(X)`` of a structured parent: same elements,
    structure forgotten."""

    if TYPE_CHECKING:
        # The generic set surface is injected by the owned Sets() axiom
        # categories at parent construction; every UnderlyingSet lives in
        # those axioms, so the surface is a real invariant of the class.
        def cardinality(self) -> Cardinal: ...
        def is_finite(self) -> bool: ...
        def is_countable(self) -> bool: ...
        def is_uncountable(self) -> bool: ...
        def index(self, element: object) -> int: ...
        def __getitem__(self, n: int) -> object: ...
        def enumeration_injection(self) -> object: ...

    def __init__(self, structured: SageParent) -> None:
        self._structured = structured
        SageParent.__init__(self, facade=structured, category=_translated_placement(structured).Facade())

    def _repr_(self) -> str:
        return f"Underlying set of {self._structured}"

    def structured_parent(self) -> SageParent:
        r"""The structured parent this set underlies."""
        return self._structured

    def __iter__(self) -> Iterator[object]:
        # The structured parent's enumeration is its witness data, supplied
        # dynamically; the static Parent surface cannot see it.
        return iter(cast(Iterable[object], self._structured))

    def __contains__(self, x: object) -> bool:
        return x in self._structured
