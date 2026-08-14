r"""The power object of a set and its characteristic-morphism model."""

import dzack_research.preamble.categories.abstract_categories.cat

from sage.all import Primes, RR, ZZ
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism

from dzack_research.preamble.categories.rings.rings import own_ring
from dzack_research.preamble.categories.sets.cardinals import (
    aleph0,
    cardinal,
    continuum,
)
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.sets import ImageSet, PowerSet, Set


def test_power_set_accepts_finite_and_canonical_infinite_subsets() -> None:
    r"""A member of P(X) is a subset of X, not only a finite enumeration."""
    naturals = Sets.Δ[aleph0]
    integers = own_ring(ZZ)
    natural_subsets = PowerSet(naturals)

    assert {1, 2, 3} in natural_subsets
    assert natural_subsets({1, 2, 3}) == natural_subsets({3, 2, 1})
    assert naturals in PowerSet(integers)
    assert {2, 3, 5} in PowerSet(Primes())
    assert {2, 4} not in PowerSet(Primes())
    assert integers not in PowerSet(naturals)


def test_a_power_set_element_is_a_subobject_with_a_characteristic_morphism() -> None:
    r"""A subset exposes both A -> X and chi_A: X -> Delta[1]."""
    naturals = Sets.Δ[aleph0]
    truth_values = Sets.Δ[1]
    subsets = PowerSet(naturals)
    primes_below_ten = subsets({2, 3, 5, 7})

    assert primes_below_ten in subsets
    assert subsets.characteristic_homset() is Hom(naturals, truth_values, Sets())
    assert primes_below_ten.inclusion().codomain() is naturals
    assert primes_below_ten.inclusion()(5) == 5

    characteristic = primes_below_ten.characteristic_morphism()
    assert characteristic.parent() is Hom(naturals, truth_values, Sets())
    assert characteristic(5) == truth_values(1)
    assert characteristic(6) == truth_values(0)


def test_characteristic_morphisms_construct_power_set_elements() -> None:
    r"""Hom(X, Delta[1]) and P(X) give equivalent subset presentations."""
    integers = own_ring(ZZ)
    truth_values = Sets.Δ[1]
    subsets = PowerSet(integers)
    integer_set = subsets.source()
    characteristic_of_evens = SetMorphism(
        Hom(integer_set, truth_values, Sets()),
        lambda n: truth_values(1 if n % 2 == 0 else 0),
    )

    evens = subsets.from_characteristic_morphism(characteristic_of_evens)

    assert evens in subsets
    assert 24 in evens
    assert 25 not in evens
    assert evens.characteristic_morphism() is characteristic_of_evens
    assert evens.inclusion().codomain() is integer_set


def test_predicates_construct_infinite_subsets_without_enumeration() -> None:
    r"""A decidable predicate presents a first-class infinite subobject."""
    integers = own_ring(ZZ)
    subsets = PowerSet(integers)
    integer_set = subsets.source()
    nonnegative = subsets.from_predicate(lambda n: n >= 0)

    assert nonnegative in subsets
    assert 13 in nonnegative
    assert -1 not in nonnegative
    assert nonnegative.inclusion().codomain() is integer_set
    assert nonnegative.characteristic_morphism()(13) == Sets.Δ[1](1)
    assert nonnegative.characteristic_morphism()(-1) == Sets.Δ[1](0)


def test_power_set_boolean_algebra_is_intrinsic() -> None:
    r"""Union, intersection, difference, and complement stay inside P(X)."""
    finite_ordinal = Sets.Δ[5]
    subsets = PowerSet(finite_ordinal)
    left = subsets({0, 1, 2, 3})
    right = subsets({2, 3, 4})

    union = left.union(right)
    intersection = left.intersection(right)
    difference = left.difference(right)
    symmetric_difference = left.symmetric_difference(right)
    complement = left.complement()

    assert union == subsets({0, 1, 2, 3, 4})
    assert intersection == subsets({2, 3})
    assert difference == subsets({0, 1})
    assert symmetric_difference == subsets({0, 1, 4})
    assert complement == subsets({4, 5})
    assert union in subsets
    assert intersection in subsets
    assert complement in subsets


def test_power_set_is_a_bounded_distributive_lattice() -> None:
    r"""Subset order, top, bottom, meet, and join have their set meanings."""
    finite_ordinal = Sets.Δ[4]
    subsets = PowerSet(finite_ordinal)
    a = subsets({0, 1})
    b = subsets({1, 2})
    c = subsets({1, 2, 3})

    assert a <= a.union(b)
    assert b <= c
    assert a.intersection(b.union(c)) == a.intersection(b).union(
        a.intersection(c)
    )
    assert subsets.bottom() <= a <= subsets.top()
    assert subsets.bottom() == subsets(set())
    assert subsets.top() == subsets(finite_ordinal)


def test_characteristic_morphisms_preserve_boolean_operations_pointwise() -> None:
    r"""The Boolean algebra on P(X) agrees with Boolean operations on X -> 2."""
    finite_ordinal = Sets.Δ[5]
    subsets = PowerSet(finite_ordinal)
    left = subsets({0, 2, 4})
    right = subsets({1, 2, 3})
    truth_values = Sets.Δ[1]

    for x in finite_ordinal:
        left_value = left.characteristic_morphism()(x)
        right_value = right.characteristic_morphism()(x)
        assert left.union(right).characteristic_morphism()(x) == truth_values(
            max(left_value, right_value)
        )
        assert left.intersection(right).characteristic_morphism()(x) == truth_values(
            min(left_value, right_value)
        )
        assert left.complement().characteristic_morphism()(x) == truth_values(
            1 - left_value
        )


def test_inverse_image_makes_power_set_contravariant() -> None:
    r"""A map f: X -> Y induces f^-1: P(Y) -> P(X)."""
    naturals = Sets.Δ[aleph0]
    integers = own_ring(ZZ)
    integer_subsets = PowerSet(integers)
    integer_set = integer_subsets.source()
    inclusion = SetMorphism(
        Hom(naturals, integer_set, Sets()),
        lambda n: integer_set(n),
    )
    natural_subsets = PowerSet(naturals)
    even_integers = integer_subsets.from_predicate(lambda n: n % 2 == 0)

    inverse_image = integer_subsets.inverse_image_morphism(inclusion)
    even_naturals = inverse_image(even_integers)

    assert inverse_image.domain() == integer_subsets
    assert inverse_image.codomain() == natural_subsets
    assert even_naturals in natural_subsets
    assert 12 in even_naturals
    assert 13 not in even_naturals


def test_inverse_image_respects_identity_composition_and_boolean_operations() -> None:
    r"""The power-set construction is a contravariant Boolean-algebra functor."""
    finite_ordinal = Sets.Δ[5]
    truth_values = Sets.Δ[1]
    successor = SetMorphism(
        Hom(finite_ordinal, finite_ordinal, Sets()),
        lambda n: finite_ordinal((n + 1) % 6),
    )
    parity = SetMorphism(
        Hom(finite_ordinal, truth_values, Sets()),
        lambda n: truth_values(n % 2),
    )
    subsets = PowerSet(finite_ordinal)
    truth_subsets = PowerSet(truth_values)
    odd_truth_value = truth_subsets({1})
    odd_vertices = truth_subsets.inverse_image_morphism(parity)(odd_truth_value)

    identity_pullback = subsets.inverse_image_morphism(
        Hom(finite_ordinal, finite_ordinal, Sets()).identity()
    )
    successor_pullback = subsets.inverse_image_morphism(successor)
    composite_pullback = truth_subsets.inverse_image_morphism(parity * successor)

    assert identity_pullback(odd_vertices) == odd_vertices
    assert composite_pullback(odd_truth_value) == successor_pullback(odd_vertices)
    assert successor_pullback(odd_vertices.complement()) == successor_pullback(
        odd_vertices
    ).complement()


def test_direct_and_inverse_images_satisfy_the_subset_adjunction() -> None:
    r"""For f: X -> Y, direct image is left adjoint to inverse image."""
    source = Sets.Δ[5]
    target = Sets.Δ[2]
    residue = SetMorphism(
        Hom(source, target, Sets()),
        lambda n: target(n % 3),
    )
    source_subsets = PowerSet(source)
    target_subsets = PowerSet(target)
    selected = source_subsets({0, 1, 3, 4})
    upper_bound = target_subsets({0, 1})

    direct_image = source_subsets.direct_image_morphism(residue)
    inverse_image = target_subsets.inverse_image_morphism(residue)

    assert direct_image.domain() == source_subsets
    assert direct_image.codomain() == target_subsets
    assert direct_image(selected) == target_subsets({0, 1})
    assert direct_image(selected) <= upper_bound
    assert selected <= inverse_image(upper_bound)


def test_power_set_cardinalities_cover_standard_finite_and_infinite_sets() -> None:
    r"""P(X) has cardinality 2^|X| across the standard set catalogue."""
    naturals = Sets.Δ[aleph0]
    doubling = SetMorphism(Hom(naturals, naturals, Sets()), lambda n: 2 * n)
    even_naturals = ImageSet(doubling, naturals, is_injective=True)
    reals = own_ring(RR)

    specimens = (
        (Set([]), cardinal(1)),
        (Sets.Δ[0], cardinal(2)),
        (Sets.Δ[4], cardinal(32)),
        (naturals, continuum),
        (even_naturals, continuum),
        (Primes(), continuum),
        (reals, cardinal(2) ** continuum),
        (PowerSet(naturals), cardinal(2) ** continuum),
    )

    for source, expected_cardinality in specimens:
        assert PowerSet(source).cardinality() == expected_cardinality


def test_cantor_inequality_holds_for_the_standard_catalogue() -> None:
    r"""Every standard specimen has strictly fewer elements than its power set."""
    specimens = (
        Set([0, 1, 2]),
        Sets.Δ[aleph0],
        Primes(),
        own_ring(RR),
        PowerSet(Sets.Δ[aleph0]),
    )

    for source in specimens:
        assert cardinal(source.cardinality()) < PowerSet(source).cardinality()


def test_iterated_power_sets_contain_subsets_of_the_previous_power_set() -> None:
    r"""P(P(X)) contains families of subsets of X as first-class elements."""
    naturals = Sets.Δ[aleph0]
    subsets = PowerSet(naturals)
    families = PowerSet(subsets)
    small_primes = subsets({2, 3, 5, 7})
    small_squares = subsets({1, 4, 9, 16})
    family = families((small_primes, small_squares))

    assert family in families
    assert small_primes in family
    assert small_squares in family
    assert subsets.top() in families.top()
    assert families.cardinality() == cardinal(2) ** continuum
