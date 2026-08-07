r"""The scalar hierarchy: semirings through fields.

Each owned node chains into BOTH operation roots — a semiring is a
multiplicative monoid over an additively commutative monoid, a rng is a
multiplicative semigroup over an additively commutative group, a ring is
their unital join — and reuses Sage's standard category of the same name
as an integration point. Domains, GCD/unique-factorization/principal-ideal
/Euclidean refinements, and noetherian rings arrive through Sage's own
trunk in placements (joins), never as a hand-written parallel tree.

No node here declares any set behavior: generic set operations resolve
through the forwarding owners at the operation roots and CP1's owners
below them. Set refinements (``Finite``, ``Countable``, ``Uncountable``)
are requested through the roots' axiom classes and remain available on
every scalar node by inheritance.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.fields import Fields as SageFields
from sage.categories.rings import Rings as SageRings
from sage.categories.rngs import Rngs as SageRngs
from sage.categories.semirings import Semirings as SageSemirings

from .functors import CatObject
from .magmas import AdditiveGroups, AdditiveMonoids, Monoids, Semigroups

if TYPE_CHECKING:
    pass


class Semirings(CatObject, Category):
    r"""The owned category of semirings: a multiplicative monoid over an
    additively commutative monoid, with distributivity carried by Sage's
    standard node."""

    def super_categories(self) -> list[Category]:
        return [SageSemirings(), Monoids(), AdditiveMonoids().AdditiveCommutative()]

    if TYPE_CHECKING:
        # Typed axiom navigation, synthesized by Sage at runtime; the axiom
        # tree is closed under its own axioms.
        def Commutative(self) -> Semirings: ...
        def Countable(self) -> Semirings: ...
        def Uncountable(self) -> Semirings: ...
        def Infinite(self) -> Semirings: ...
        def Finite(self) -> Semirings: ...
        def Facade(self) -> Semirings: ...


class Rngs(CatObject, Category):
    r"""The owned category of rngs: a multiplicative semigroup over an
    additively commutative group."""

    def super_categories(self) -> list[Category]:
        return [SageRngs(), Semigroups(), AdditiveGroups().AdditiveCommutative()]


class Rings(CatObject, Category):
    r"""The owned category of unital rings: the join of the semiring and
    rng routes."""

    def super_categories(self) -> list[Category]:
        return [SageRings(), Semirings(), Rngs()]

    if TYPE_CHECKING:
        # Typed axiom navigation, synthesized by Sage at runtime; the axiom
        # tree is closed under its own axioms.
        def Commutative(self) -> Rings: ...
        def Countable(self) -> Rings: ...
        def Uncountable(self) -> Rings: ...
        def Infinite(self) -> Rings: ...
        def Finite(self) -> Rings: ...
        def Facade(self) -> Rings: ...


class DivisionRings(CatObject, Category):
    r"""The owned category of division rings."""

    def super_categories(self) -> list[Category]:
        return [SageDivisionRings(), Rings()]


class Fields(CatObject, Category):
    r"""The owned category of fields: commutative division rings."""

    def super_categories(self) -> list[Category]:
        return [SageFields(), DivisionRings()]

    if TYPE_CHECKING:
        # Typed axiom navigation, synthesized by Sage at runtime; the axiom
        # tree is closed under its own axioms.
        def Countable(self) -> Fields: ...
        def Uncountable(self) -> Fields: ...
        def Infinite(self) -> Fields: ...
        def Finite(self) -> Fields: ...
        def Facade(self) -> Fields: ...
