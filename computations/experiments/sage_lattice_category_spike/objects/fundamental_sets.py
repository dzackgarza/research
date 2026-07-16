r"""Fundamental sets: the named Sage objects as objects of the owned graph.

Each named Sage object enters the owned category tree as its one-object
category: an owned facade parent carries the axiomatic placement and the
owned API, while its elements ARE the underlying Sage parent's elements
and computation routes to Sage (governing decision:
``named-sage-objects-enter-the-owned-graph-as-one-object-categories-with-
delegating-facades``). Enumerations reuse Sage's native orders; exact
index formulas override the generic scan where they exist.

``NN``, ``ZZ``, ``QQ`` use the operational countable route. ``RR`` uses
trusted placement in ``Uncountable``: its Sage-level witness is the
declared category placement, documented by Mathlib's
``Cardinal.not_countable_real``
(https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Cardinality.html#Cardinal.not_countable_real).
"""

from __future__ import annotations

from collections.abc import Iterator

from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.rings.real_mpfr import RR
from sage.rings.semirings.non_negative_integer_semiring import NN

from ..lexicon import ExactScalar, Integer, SageParent, SageUniqueRepresentation
from .sets import Sets


class NonNegativeIntegers(SageUniqueRepresentation, SageParent):
    r"""The nonnegative integers as an owned countable set: the identity
    enumeration ``0, 1, 2, ...`` over Sage's ``NN``."""

    def __init__(self) -> None:
        SageParent.__init__(self, facade=NN, category=Sets().Countable().Infinite().Facade())

    def _repr_(self) -> str:
        return "Set of nonnegative integers"

    def __iter__(self) -> Iterator[Integer]:
        return iter(NN)

    def __getitem__(self, n: int) -> Integer:
        assert n >= 0, f"enumeration indices are nonnegative; found {n}"
        # Sage's NN is itself a facade over ZZ: its elements ARE integers.
        return ZZ(n)

    def index(self, element: ExactScalar | int) -> Integer:
        member = ZZ(element)
        assert member >= 0, f"{element} is not a nonnegative integer"
        return member


class Integers(SageUniqueRepresentation, SageParent):
    r"""The integers as an owned countable set: Sage's native zigzag
    enumeration ``0, 1, -1, 2, -2, ...`` with its exact index formula."""

    def __init__(self) -> None:
        SageParent.__init__(self, facade=ZZ, category=Sets().Countable().Infinite().Facade())

    def _repr_(self) -> str:
        return "Set of integers"

    def __iter__(self) -> Iterator[Integer]:
        return iter(ZZ)

    def __getitem__(self, n: int) -> Integer:
        assert n >= 0, f"enumeration indices are nonnegative; found {n}"
        position = ZZ(n)
        if position == 0:
            return ZZ(0)
        if position % 2 == 1:
            return (position + 1) // 2
        return -position // 2

    def index(self, element: ExactScalar | int) -> Integer:
        member = ZZ(element)
        if member == 0:
            return ZZ(0)
        if member > 0:
            return 2 * member - 1
        return -2 * member


class Rationals(SageUniqueRepresentation, SageParent):
    r"""The rationals as an owned countable set: Sage's native
    height-ordered enumeration ``0, 1, -1, 1/2, -1/2, 2, -2, ...``; reverse
    lookup is the generic enumeration scan, which terminates for members."""

    def __init__(self) -> None:
        SageParent.__init__(self, facade=QQ, category=Sets().Countable().Infinite().Facade())

    def _repr_(self) -> str:
        return "Set of rationals"

    def __iter__(self) -> Iterator[ExactScalar]:
        return iter(QQ)


class Reals(SageUniqueRepresentation, SageParent):
    r"""The real numbers as an owned uncountable set, by trusted placement:
    the one-object subcategory on ``RR`` inside the uncountable sets. No
    enumeration data exists or is demanded; the uniform consequences are
    category facts. Formal reference: Mathlib ``Cardinal.not_countable_real``."""

    def __init__(self) -> None:
        SageParent.__init__(self, facade=RR, category=Sets().Uncountable().Facade())

    def _repr_(self) -> str:
        return "Set of real numbers"
