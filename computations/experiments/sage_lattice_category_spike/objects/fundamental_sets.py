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

from sage.categories.category import Category
from sage.categories.euclidean_domains import EuclideanDomains as SageEuclideanDomains
from sage.rings.finite_rings.finite_field_constructor import GF
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as SageIntegerModRing
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.rings.real_mpfr import RR
from sage.rings.semirings.non_negative_integer_semiring import NN

from ..lexicon import ExactScalar, Integer, SageParent, SageUniqueRepresentation
from .cardinals import Cardinal, cardinal
from .scalars import Fields, Rings, Semirings


class NonNegativeIntegers(SageUniqueRepresentation, SageParent):
    r"""The nonnegative integers as an owned countable set: the identity
    enumeration ``0, 1, 2, ...`` over Sage's ``NN``."""

    def __init__(self) -> None:
        SageParent.__init__(self, facade=NN, category=Semirings().Commutative().Countable().Infinite().Facade())

    def _repr_(self) -> str:
        return "Set of nonnegative integers"

    def __iter__(self) -> Iterator[Integer]:
        return iter(NN)

    def index(self, element: ExactScalar | int) -> Integer:
        member = ZZ(element)
        assert member >= 0, f"{element} is not a nonnegative integer"
        return member


class Integers(SageUniqueRepresentation, SageParent):
    r"""The integers as an owned countable set: Sage's native zigzag
    enumeration ``0, 1, -1, 2, -2, ...`` with its exact index formula."""

    def __init__(self) -> None:
        placement = Rings().Commutative().Countable().Infinite().Facade()
        SageParent.__init__(self, facade=ZZ, category=Category.join([placement, SageEuclideanDomains()]))

    def _repr_(self) -> str:
        return "Set of integers"

    def __iter__(self) -> Iterator[Integer]:
        return iter(ZZ)

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
        SageParent.__init__(self, facade=QQ, category=Fields().Countable().Infinite().Facade())

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
        SageParent.__init__(self, facade=RR, category=Fields().Uncountable().Facade())

    def _repr_(self) -> str:
        return "Set of real numbers"


class IntegerModRing(SageUniqueRepresentation, SageParent):
    r"""``ZZ/nZZ`` as an owned finite commutative ring, delegating to
    Sage's residue ring."""

    def __init__(self, modulus: int) -> None:
        self._modulus = ZZ(modulus)
        assert self._modulus >= 1, f"the modulus of a residue ring is a positive integer; found {modulus}"
        self._host = SageIntegerModRing(modulus)
        SageParent.__init__(self, facade=self._host, category=Rings().Commutative().Finite().Facade())

    def _repr_(self) -> str:
        return f"Ring of integers modulo {self._modulus}"

    def __iter__(self) -> Iterator[object]:
        return iter(self._host)

    def __contains__(self, x: object) -> bool:
        return x in self._host

    def cardinality(self) -> Cardinal:
        r"""``|ZZ/nZZ| = n``, exactly."""
        return cardinal(self._modulus)


class FiniteField(SageUniqueRepresentation, SageParent):
    r"""``GF(q)`` as an owned finite field, delegating to Sage's finite
    field (which validates that ``q`` is a prime power)."""

    def __init__(self, order: int) -> None:
        self._host = GF(order, "a")
        SageParent.__init__(self, facade=self._host, category=Fields().Finite().Facade())

    def _repr_(self) -> str:
        return f"Finite field of order {self._host.cardinality()}"

    def __iter__(self) -> Iterator[object]:
        return iter(self._host)

    def __contains__(self, x: object) -> bool:
        return x in self._host

    def cardinality(self) -> Cardinal:
        return cardinal(self._host.cardinality())
