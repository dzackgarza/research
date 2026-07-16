r"""The owned ``Sets()`` root and its four axioms.

The owned root sits over Sage's ``Sets()`` and reuses Sage's standard
``Finite`` and ``Infinite`` axioms; project-owned ``Countable`` and
``Uncountable`` enter Sage's global ``all_axioms`` registry through the
exact idempotent adapter below — the only Sage mutation this module
performs.

The axiom lattice is mathematical fact: ``Finite`` refines ``Countable``
(every finite set receives the enumeration contract), ``Uncountable``
refines ``Infinite``, ``Countable`` and ``Uncountable`` are disjoint, and
countably-infinite is the join ``Sets().Countable().Infinite()``, never a
new named root. Membership is opt-in-with-trust: ``Countable`` forces the
executable witness suite (exhaustive duplicate-free iteration, integer
indexing, reverse lookup) through Sage ``abstract_method`` obligations;
``Uncountable`` is trusted placement carrying uniform consequences and no
enumeration obligation. Generic infinite-set consequences (``is_finite``,
``cardinality() == +Infinity``) are inherited from Sage's ``Infinite``
axiom through the join and are never reimplemented here.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, cast

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom, all_axioms
from sage.categories.sets_cat import Sets as SageSets

if TYPE_CHECKING:
    # Sage's abstract_method ships untyped; for type-checking use
    # abc.abstractmethod (typed, and permits the empty abstract bodies
    # below). Runtime uses Sage's.
    from abc import abstractmethod as abstract_method

    from .cardinals import Cardinal
else:
    from sage.misc.abstract_method import abstract_method

_SET_AXIOMS = ("Countable", "Uncountable")


def register_set_axioms() -> None:
    r"""Register exactly ``Countable`` and ``Uncountable`` in Sage's global
    axiom registry. Idempotent: after the first registration, repeated calls
    leave the registry unchanged."""
    for axiom_name in _SET_AXIOMS:
        if axiom_name not in all_axioms:
            all_axioms.add(axiom_name)
    assert all(axiom_name in all_axioms for axiom_name in _SET_AXIOMS)


register_set_axioms()


class Sets(Category):
    r"""The owned category of sets: declaration owner of the generic
    meanings of cardinality, finiteness, infinitude, countability,
    uncountability, enumeration, indexing, and reverse lookup."""

    def super_categories(self) -> list[Category]:
        return [SageSets()]

    if TYPE_CHECKING:
        # Typed axiom navigation: at runtime Sage synthesizes these from
        # SubcategoryMethods; the axiom tree is closed under its own axioms.
        # The class-attribute wiring at the bottom of this module is Sage's
        # class-resolution shortcut and is runtime-only.
        def Countable(self) -> Sets: ...
        def Uncountable(self) -> Sets: ...
        def Finite(self) -> Sets: ...
        def Infinite(self) -> Sets: ...
        def Facade(self) -> Sets: ...

    class SubcategoryMethods:
        # Runtime Sage mixes this class into every subcategory, so ``self``
        # is a Category there; the casts state that fact for the checker.
        def Countable(self) -> Category:
            r"""Sets with a chosen computable, exhaustive, duplicate-free
            enumeration."""
            category = cast(Category, self)
            assert "Uncountable" not in category.axioms(), "Countable and Uncountable are disjoint"
            return category._with_axiom("Countable")

        def Uncountable(self) -> Category:
            r"""Sets placed beyond every enumeration, by trusted
            declaration. (The reverse contradiction, ``Uncountable`` then
            ``Finite``, is refused by Sage's native finite/infinite
            incompatibility because ``Uncountable`` implies ``Infinite``.)"""
            category = cast(Category, self)
            assert "Countable" not in category.axioms(), "Countable and Uncountable are disjoint"
            return category._with_axiom("Uncountable")

    class ParentMethods:
        @abstract_method
        def is_countable(self) -> bool:
            r"""Whether this set admits an enumeration; determined by the
            ``Countable``/``Uncountable`` placement, abstract when neither
            axiom determines it."""

        @abstract_method
        def is_uncountable(self) -> bool:
            r"""Whether this set is beyond every enumeration; determined by
            the placement, abstract when undetermined."""


class FiniteSets(CategoryWithAxiom):
    r"""Finite sets: Sage's standard axiom, plus the owned refinement that
    finiteness implies the countable enumeration contract."""

    _base_category_class_and_axiom = (Sets, "Finite")

    def extra_super_categories(self) -> list[Category]:
        return [cast("Sets", self.base_category()).Countable()]


class InfiniteSets(CategoryWithAxiom):
    r"""Infinite sets: Sage's standard axiom supplies the uniform
    consequences (``is_finite() == False``, ``cardinality() == +Infinity``)
    through the join; nothing is reimplemented here."""

    _base_category_class_and_axiom = (Sets, "Infinite")


class CountableSets(CategoryWithAxiom):
    r"""Countable sets: membership forces the executable witness suite.

    A set with a chosen enumeration is exactly an enumerated set, so this
    axiom refines Sage's ``EnumeratedSets`` — the sanctioned adapter
    integration that lets Sage's solved construction machinery (fair
    Cartesian-product iteration, disjoint unions) consume owned countable
    sets natively. The owned public meanings remain ``iter(X)``, ``X[n]``,
    and ``X.index(x)``."""

    _base_category_class_and_axiom = (Sets, "Countable")

    def extra_super_categories(self) -> list[Category]:
        from sage.categories.enumerated_sets import EnumeratedSets

        return [EnumeratedSets()]

    class ParentMethods:
        # The enumeration is the sole abstract witness obligation: indexing,
        # reverse lookup, and the injection into the naturals are all
        # constructed from it (generic first-owner implementations below,
        # overridable by exact formulas).
        @abstract_method
        def __iter__(self) -> Iterator[object]:
            r"""A chosen computable, exhaustive, duplicate-free enumeration
            of this set."""

        def __getitem__(self, n: int) -> object:
            r"""The ``n``-th element of the chosen enumeration, ``n >= 0``."""
            assert n >= 0, f"enumeration indices are nonnegative; found {n}"
            for position, element in enumerate(self):
                if position == n:
                    return element
            assert False, f"index {n} exceeds the enumeration of {self}"

        def index(self, element: object) -> int:
            r"""Reverse lookup in the chosen enumeration: terminates for
            members and satisfies ``X[X.index(x)] == x``. No termination
            promise for a nonmember of an infinite parent."""
            for position, candidate in enumerate(self):
                if candidate == element:
                    return position
            assert False, f"{element} is not in the enumeration of {self}"

        def enumeration_injection(self) -> object:
            r"""The monomorphism into the nonnegative integers realized by
            the chosen enumeration, ``x -> index(x)``, as an element of the
            actual homset — the constructed effective witness of
            countability."""
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism

            from .fundamental_sets import NonNegativeIntegers

            naturals = NonNegativeIntegers()
            homset = Hom(self, naturals, SageSets())
            # naturals[n] IS the natural number n (identity enumeration),
            # already normalized into the host parent.
            return SetMorphism(homset, lambda element: naturals[self.index(element)])

        def is_countable(self) -> bool:
            return True

        def is_uncountable(self) -> bool:
            return False


class CountablyInfiniteSets(CategoryWithAxiom):
    r"""Countably infinite sets — the join ``Sets().Countable().Infinite()``,
    never a new named root. Owns the exact cardinal: ``aleph_0``."""

    _base_category_class_and_axiom = (CountableSets, "Infinite")

    class ParentMethods:
        def cardinality(self) -> Cardinal:
            r"""``aleph_0``, exactly — not Sage's countable-blind
            ``+Infinity`` (to which it compares equal)."""
            from .cardinals import aleph0

            return aleph0


class UncountableSets(CategoryWithAxiom):
    r"""Uncountable sets: trusted placement, uniform consequences, and in
    particular infinite."""

    _base_category_class_and_axiom = (Sets, "Uncountable")

    def extra_super_categories(self) -> list[Category]:
        return [cast("Sets", self.base_category()).Infinite()]

    class ParentMethods:
        def is_countable(self) -> bool:
            return False

        def is_uncountable(self) -> bool:
            return True

        def cardinality(self) -> Cardinal:
            r"""The continuum, ``2^aleph_0``: exact for every uncountable
            object constructible in this graph (see ``objects/cardinals``)."""
            from .cardinals import continuum

            return continuum


if not TYPE_CHECKING:
    # Sage's class-resolution shortcut: the axiom category class must be
    # reachable as `<BaseCategory>.<Axiom>` for `_base_category_class_and_axiom`
    # to resolve. Runtime-only wiring; the typed surface of these names is the
    # axiom-navigation method declarations on the category class above.
    Sets.Finite = FiniteSets
    Sets.Infinite = InfiniteSets
    Sets.Countable = CountableSets
    Sets.Uncountable = UncountableSets
    CountableSets.Infinite = CountablyInfiniteSets
