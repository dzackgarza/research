r"""Operation spines with forwarding at the two roots (issue #212, CP2).

The owned multiplicative and additive spines are built from Sage's
standard axioms — ``Semigroups`` is ``Magmas().Associative()``,
``Monoids`` adds ``Unital``, ``Groups`` adds ``Inverse``, with the exact
additive parallel — and the structured-to-set route is composition, not
inheritance: the underlying-set functor ``U`` is a faithful element of
``Fun(Magmas(), Sets())`` whose object action is the ``UnderlyingSet``
facade (same elements, structure forgotten) placed by translating the
structured parent's set axioms. Generic set behavior forwards through
``U`` exactly at ``Magmas()`` and ``AdditiveMagmas()`` — a structured
parent defines no set methods of its own, and a structure carrying both
operations reaches the SAME underlying set through either route.
"""

from __future__ import annotations

import itertools

from sage.all import QQ, ZZ, Zmod
from sage.categories.homset import Hom
from sage.categories.magmas import Magmas as SageMagmas
from sage.categories.additive_magmas import AdditiveMagmas as SageAdditiveMagmas
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.cardinals import aleph0
from sage_lattice_category_spike.objects.functors import FunctorSpace
from sage_lattice_category_spike.objects.magmas import (
    AdditiveGroups,
    AdditiveMagmas,
    AdditiveMonoids,
    AdditiveSemigroups,
    Groups,
    Magmas,
    Monoids,
    Semigroups,
    UnderlyingSetFunctor,
)
from sage_lattice_category_spike.objects.sets import Sets
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet


def test_the_multiplicative_spine_follows_sage_standard_axioms():
    assert Magmas().is_subcategory(SageMagmas())
    assert Semigroups() is Magmas().Associative()
    assert Monoids() is Semigroups().Unital()
    assert Groups() is Monoids().Inverse()
    assert Groups().is_subcategory(Magmas())
    assert Magmas().Countable().is_subcategory(Magmas())


def test_the_additive_spine_follows_sage_standard_axioms():
    assert AdditiveMagmas().is_subcategory(SageAdditiveMagmas())
    assert AdditiveSemigroups() is AdditiveMagmas().AdditiveAssociative()
    assert AdditiveMonoids() is AdditiveSemigroups().AdditiveUnital()
    assert AdditiveGroups() is AdditiveMonoids().AdditiveInverse()
    assert AdditiveGroups().is_subcategory(AdditiveMagmas())


class NonzeroRationalsUnderMultiplication(Parent):
    r"""The group ``QQ^x``: countably infinite, enumeration inherited from
    the rationals with zero removed. Supplies ONLY the enumeration — every
    other set behavior must arrive through the underlying-set route."""

    def __init__(self):
        Parent.__init__(self, facade=QQ, category=Groups().Countable().Infinite())

    def __iter__(self):
        return (q for q in iter(QQ) if q != 0)

    def __contains__(self, x):
        return x in QQ and x != 0


class IntegersModFiveUnderAddition(Parent):
    r"""The additive group ``ZZ/5``: finite, enumeration from the host."""

    def __init__(self):
        Parent.__init__(self, facade=Zmod(5), category=AdditiveGroups().Finite())

    def __iter__(self):
        return iter(Zmod(5))


def test_set_behavior_forwards_through_the_underlying_set_route():
    r"""The rollup in action: the group defines no cardinality, no
    countability predicates, no indexing — yet answers all of them, through
    ``U`` and CP1's owners."""
    units = NonzeroRationalsUnderMultiplication()
    assert units.cardinality() == aleph0
    assert units.is_countable()
    assert not units.is_uncountable()
    assert not units.is_finite()

    underlying = units.underlying_set()
    assert underlying is UnderlyingSet(units)
    assert underlying.category().is_subcategory(Sets().Countable().Infinite())
    prefix = list(itertools.islice(iter(underlying), 6))
    assert prefix == [1, -1, 1 / 2, -1 / 2, 2, -2]
    assert underlying[underlying.index(QQ(2))] == 2

    mod_five = IntegersModFiveUnderAddition()
    assert mod_five.cardinality() == 5
    assert mod_five.is_finite()
    assert mod_five.underlying_set().category().is_subcategory(Sets().Finite())
    assert sorted(int(x) for x in mod_five.underlying_set()) == [0, 1, 2, 3, 4]


def test_the_underlying_set_functor_is_a_faithful_kernel_element():
    forget = UnderlyingSetFunctor(Magmas())
    assert forget in FunctorSpace(Magmas(), Sets())
    assert forget.is_faithful()

    units = NonzeroRationalsUnderMultiplication()
    assert forget(units) is UnderlyingSet(units)

    doubling = SetMorphism(Hom(units, units, Magmas()), lambda q: 2 * q)
    image = forget(doubling)
    assert image.parent() is Hom(UnderlyingSet(units), UnderlyingSet(units), SageSets())
    assert image(QQ(3)) == 6


class IntegersWithBothOperations(Parent):
    r"""``ZZ`` carrying both operations: the two structure-forgetting
    routes must reach the SAME underlying set."""

    def __init__(self):
        from sage.categories.category import Category

        category = Category.join([Magmas(), AdditiveGroups()]).Countable().Infinite()
        Parent.__init__(self, facade=ZZ, category=category)

    def __iter__(self):
        return iter(ZZ)


def test_both_operation_routes_reach_the_same_underlying_set():
    both = IntegersWithBothOperations()
    through_multiplication = UnderlyingSetFunctor(Magmas())(both)
    through_addition = UnderlyingSetFunctor(AdditiveMagmas())(both)
    assert through_multiplication is through_addition
    assert both.cardinality() == aleph0
