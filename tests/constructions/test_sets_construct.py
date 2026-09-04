r"""Set and cardinal constructions a mathematician expects.

Finite and infinite sets, their products, coproducts, power sets, function
sets and subsets, the Hom sets between them, and the cardinal arithmetic
those constructions realize.
"""

import pytest

from dzack_research.preamble.all import (
    NN,
    QQ,
    RR,
    ZZ,
    Cardinalities,
    CartesianProductOfSets,
    ConditionSet,
    CoproductOfSets,
    CountableSets,
    CountablyInfiniteSets,
    ExponentialOfSets,
    FiniteSets,
    FiniteSubsets,
    ImageSet,
    IsoCategoryOf,
    MonoCategoryOf,
    Ordinals,
    PowerSet,
    Set,
    Sets,
    SubsetsOfSize,
    TotallyOrderedSets,
    UncountableSets,
    aleph,
    aleph0,
    cardinal,
    continuum,
    omega,
    ordinal,
)


def _three():
    return Set((1, 2, 3))


def _two():
    return Sets.Δ[1]


def test_a_finite_set_and_its_constructions() -> None:
    three = _three()
    two = _two()

    assert three in Sets()
    assert three in FiniteSets()
    assert three in CountableSets()
    assert three.cardinality() == 3
    assert two.cardinality() == 2
    assert 2 in three
    assert 4 not in three
    assert three.power_set().cardinality() == 8
    assert PowerSet(three).cardinality() == 8
    assert three.product_with(two).cardinality() == 6
    assert CartesianProductOfSets(three, two, three).cardinality() == 18
    assert CoproductOfSets(three, two).cardinality() == 5
    assert three.subsets_of_size(2).cardinality() == 3
    assert SubsetsOfSize(three, 2).cardinality() == 3
    assert FiniteSubsets(three).cardinality() == 8
    assert three.finite_subsets().cardinality() == 8


def test_function_sets_between_finite_sets() -> None:
    three = _three()
    two = _two()
    assert ExponentialOfSets(three, two).cardinality() == 9
    assert three.exponential(two).cardinality() == 9
    assert Sets().Mor(two, three).cardinality() == 9
    assert Sets().Mor(three, two).cardinality() == 8
    assert MonoCategoryOf(Sets()).Of(two, three).cardinality() == 6
    assert MonoCategoryOf(Sets()).Of(three, two).cardinality() == 0
    assert IsoCategoryOf(Sets()).Of(three, three).cardinality() == 6
    assert Sets().Mor(three, Sets.Δ[0]).cardinality() == 1


def test_subsets_by_condition_and_by_image() -> None:
    three = _three()
    large = ConditionSet(three, lambda n: n > 1)
    squares = ImageSet(lambda n: n * n, three)

    assert large.cardinality() == 2
    assert 3 in large
    assert 1 not in large
    assert squares.cardinality() == 3
    assert 4 in squares
    assert 2 not in squares
    assert large.inclusion().codomain() is three


def test_infinite_sets_and_their_constructions() -> None:
    assert NN.cardinality() == aleph0
    assert NN in CountablyInfiniteSets()
    assert NN in CountableSets()
    assert NN not in FiniteSets()
    assert ZZ.cardinality() == aleph0
    assert ZZ in CountablyInfiniteSets()
    assert QQ.cardinality() == aleph0
    assert RR.cardinality() == continuum
    assert RR in UncountableSets()
    assert NN.power_set().cardinality() == continuum
    assert FiniteSubsets(NN).cardinality() == aleph0
    assert CartesianProductOfSets(NN, NN).cardinality() == aleph0
    assert CoproductOfSets(NN, _three()).cardinality() == aleph0
    assert NN.subsets_of_size(2).cardinality() == aleph0
    assert ExponentialOfSets(NN, _two()).cardinality() == aleph0
    assert ExponentialOfSets(_two(), NN).cardinality() == continuum
    assert Sets().Mor(NN, NN).cardinality() == continuum
    assert ConditionSet(NN, lambda n: n % 2 == 0).cardinality() == aleph0
    assert Sets.Δ[aleph0] is NN


def test_cardinal_arithmetic() -> None:
    cardinals = Cardinalities()
    assert cardinal(3) + cardinal(4) == cardinal(7)
    assert cardinal(3) * cardinal(4) == cardinal(12)
    assert cardinal(2) ** cardinal(3) == cardinal(8)
    assert cardinal(3) == 3
    assert cardinal(2) ** aleph0 == continuum
    assert cardinals.le(cardinal(3), aleph0)
    assert cardinal(5).is_finite()
    assert cardinal(5).finite_value() == 5
    assert cardinals.sum(cardinal(1), cardinal(2), cardinal(3)) == cardinal(6)
    assert cardinals.product(cardinal(2), cardinal(3), aleph0) == aleph0
    assert aleph0 + 1 == aleph0
    assert aleph0 * aleph0 == aleph0
    assert aleph0 ** 2 == aleph0
    assert 2 ** aleph0 == continuum
    assert continuum * continuum == continuum
    assert continuum ** aleph0 == continuum
    assert cardinals.lt(aleph0, continuum)
    assert not cardinals.le(continuum, aleph0)
    assert aleph0.is_countable()
    assert continuum.is_uncountable()
    assert aleph(1).is_uncountable()


def test_ordinal_arithmetic_is_not_commutative() -> None:
    first = omega(0)
    assert ordinal(1).ordinal_sum(first) == first
    assert first.ordinal_sum(1) != first
    assert Ordinals()(2).ordinal_sum(3) == 5
    assert first.cardinality() == aleph0
    assert omega(1).cardinality() == aleph(1)


def test_finite_ordinals_are_totally_ordered() -> None:
    four = Sets.Δ[3]
    assert four.cardinality() == 4
    assert four in TotallyOrderedSets()
    assert four.unrank(0) == four(0)
    assert four.rank(four(2)) == 2
    assert four.le(four(1), four(3))
    assert not four.le(four(3), four(1))


def test_sets_of_sets() -> None:
    three = _three()
    power = PowerSet(three)
    element = power(Set((1, 2)))
    assert element in power
    assert element.cardinality() == 2
    assert element.complement().cardinality() == 1
    assert element.union(element.complement()).cardinality() == 3
    assert element.intersection(element.complement()).cardinality() == 0
    assert power(three).cardinality() == 3
    assert power.top().cardinality() == 3
    assert power.bottom().cardinality() == 0


def test_a_set_of_rings_and_a_set_of_lattices_are_sets() -> None:
    from dzack_research.preamble.all import GF, Lattices

    rings = Set((ZZ, QQ, GF(5)))
    lattices = Set((Lattices(ZZ)("U"), Lattices(ZZ)("A2")))
    assert rings.cardinality() == 3
    assert QQ in rings
    assert lattices.cardinality() == 2
    assert Lattices(ZZ)("U") in lattices
    assert rings.product_with(lattices).cardinality() == 6
