r"""Fundamental sets: NN, ZZ, QQ operational, RR trusted (issue #211,
fundamental-sets commit of CP1).

Each named Sage object enters the owned graph as its one-object category:
an owned facade parent carrying the axiomatic placement and API, whose
elements ARE the underlying Sage parent's elements (the forgetful-functor
doctrine: same elements, structure forgotten), with computation routed to
Sage. Enumerations reuse Sage's native orders (ZZ zigzag, QQ by height);
``Integers`` carries the exact zigzag index formula, ``Rationals`` uses
the generic scan. The injection ``X -> NN`` is constructed FROM the
enumeration suite as an element of the actual homset — the effective
witness discharging the categorical obligation.
"""

from __future__ import annotations

import itertools

import pytest

from sage.all import NN, QQ, RR, ZZ, oo
from sage.categories.homset import Hom
from sage.categories.sets_cat import Sets as SageSets

from sage_lattice_category_spike.objects.cardinals import aleph0, continuum
from sage_lattice_category_spike.objects.fundamental_sets import (
    Integers,
    NonNegativeIntegers,
    Rationals,
    Reals,
)


def test_integers_reuse_sage_zigzag_with_the_exact_index_formula():
    integers = Integers()
    assert list(itertools.islice(iter(integers), 7)) == [0, 1, -1, 2, -2, 3, -3]

    assert integers.index(0) == 0
    assert integers.index(1) == 1
    assert integers.index(-1) == 2
    assert integers.index(17) == 33
    assert integers.index(-17) == 34
    assert integers[7] == 4
    assert integers[integers.index(-9)] == -9
    assert integers.index(integers[36]) == 36

    assert integers.is_countable()
    assert not integers.is_uncountable()
    assert not integers.is_finite()
    assert integers.cardinality() == aleph0
    assert integers.cardinality() == oo


def test_integers_elements_are_sage_integers():
    r"""The owned object is a categorical address, not a new arithmetic:
    elements belong to Sage's ZZ, so downstream parent checks and coercion
    keep working."""
    integers = Integers()
    five = integers(5)
    assert five.parent() is ZZ
    assert five == ZZ(5)
    assert 7 in integers
    assert QQ(1) / 2 not in integers


def test_rationals_reuse_sage_height_enumeration_with_scan_reverse_lookup():
    rationals = Rationals()
    prefix = list(itertools.islice(iter(rationals), 9))
    assert prefix == [0, 1, -1, 1 / 2, -1 / 2, 2, -2, 1 / 3, -1 / 3]
    assert len(set(prefix)) == 9

    assert rationals.index(QQ(1) / 3) == 7
    witness = QQ(2) / 5
    assert rationals[rationals.index(witness)] == witness

    assert QQ(1) / 2 in rationals
    assert 3 in rationals
    assert rationals(QQ(2) / 3).parent() is QQ
    assert rationals.is_countable()
    assert rationals.cardinality() == oo


def test_nonnegative_integers_enumerate_identically():
    naturals = NonNegativeIntegers()
    assert list(itertools.islice(iter(naturals), 5)) == [0, 1, 2, 3, 4]
    assert naturals.index(7) == 7
    assert naturals[11] == 11
    assert 0 in naturals
    assert -1 not in naturals
    assert naturals.is_countable()
    assert naturals.cardinality() == oo


def test_reals_are_uncountable_by_trusted_placement():
    r"""Trusted placement: no enumeration data exists or is demanded, and
    the uniform consequences are category facts."""
    reals = Reals()
    assert reals.is_uncountable()
    assert not reals.is_countable()
    assert not reals.is_finite()
    assert reals.cardinality() == continuum
    assert reals.cardinality() > aleph0
    assert reals.cardinality() != oo
    assert reals(1.5).parent() is RR
    assert 1.5 in reals


def test_enumeration_injection_is_an_element_of_the_actual_homset():
    r"""The categorical obligation (a monomorphism X -> NN) is discharged by
    construction from the operational suite: the morphism lives in the real
    homset, computes index values as elements of the owned naturals, and is
    injective on a genuine prefix."""
    integers = Integers()
    naturals = NonNegativeIntegers()
    injection = integers.enumeration_injection()

    assert injection.parent() is Hom(integers, naturals, SageSets())
    assert injection.domain() is integers
    assert injection.codomain() is naturals

    assert injection(ZZ(-9)) == 18
    assert injection(ZZ(5)) == 9
    # Sage's NN is itself a facade over ZZ, so images are (nonnegative) ZZ
    # elements; the semantic fact is membership in the owned codomain.
    assert injection(ZZ(5)) in naturals
    assert injection(ZZ(-9)) in NN

    prefix = list(itertools.islice(iter(integers), 15))
    images = [injection(element) for element in prefix]
    assert len(set(images)) == 15


def test_generic_suite_derives_indexing_from_iteration_alone():
    r"""A countable parent supplying ONLY the enumeration receives working
    indexing, reverse lookup, and the injection, all constructed from the
    iterator — the effective-witness principle in code."""
    from sage.structure.parent import Parent
    from sage_lattice_category_spike.objects.sets import Sets

    class PowersOfTwo(Parent):
        def __init__(self):
            Parent.__init__(self, facade=ZZ, category=Sets().Countable().Infinite().Facade())

        def __iter__(self):
            power = ZZ(1)
            while True:
                yield power
                power *= 2

    powers = PowersOfTwo()
    assert powers[5] == 32
    assert powers.index(1024) == 10
    assert powers[powers.index(64)] == 64
    injection = powers.enumeration_injection()
    assert injection(ZZ(256)) == 8
