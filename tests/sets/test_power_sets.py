
from dzack_research.preamble.all import (
    FiniteSubsets,
    PowerSet,
    Set,
    Sets,
    SubsetsOfSize,
    ZZ,
    aleph0,
    cardinal,
)


def test_power_set_elements_are_subobjects_with_characteristic_morphisms() -> None:
    finite_ordinal = Sets.Δ[5]
    subsets = PowerSet(finite_ordinal)
    selected = subsets({0, 2, 4})

    assert selected.inclusion() is selected
    assert selected.inclusion().codomain() is finite_ordinal
    assert selected.inclusion()(finite_ordinal(2)) == finite_ordinal(2)
    characteristic = selected.characteristic_morphism()
    assert characteristic.domain() is finite_ordinal
    assert characteristic.codomain() is Sets.Δ[1]
    assert characteristic(finite_ordinal(2)) == Sets.Δ[1](1)
    assert characteristic(finite_ordinal(3)) == Sets.Δ[1](0)


def test_power_set_boolean_algebra_and_lattice_laws_hold() -> None:
    finite_ordinal = Sets.Δ[5]
    subsets = PowerSet(finite_ordinal)
    left = subsets({0, 1, 2, 3})
    right = subsets({2, 3, 4})

    assert left.union(right) == subsets({0, 1, 2, 3, 4})
    assert left.intersection(right) == subsets({2, 3})
    assert left.difference(right) == subsets({0, 1})
    assert left.symmetric_difference(right) == subsets({0, 1, 4})
    assert left.complement() == subsets({4, 5})
    assert subsets.bottom() <= left <= subsets.top()
    assert left.intersection(right.union(subsets({1, 5}))) == left.intersection(
        right
    ).union(left.intersection(subsets({1, 5})))


def test_inverse_and_direct_image_form_the_set_subobject_galois_connection() -> None:
    source = Sets.Δ[5]
    target = Sets.Δ[2]
    residue = Sets().hom(source, target)(lambda n: target(int(n) % 3))
    source_subsets = PowerSet(source)
    target_subsets = PowerSet(target)
    selected = source_subsets({0, 1, 3, 4})
    upper_bound = target_subsets({0, 1})

    direct = source_subsets.direct_image_morphism(residue)
    inverse = target_subsets.inverse_image_morphism(residue)
    assert direct(selected) == target_subsets({0, 1})
    assert direct(selected) <= upper_bound
    assert selected <= inverse(upper_bound)


def test_predicate_subsets_and_power_set_cardinalities_include_countable_case() -> None:
    integers = ZZ
    nonnegative = PowerSet(integers).from_predicate(lambda n: n >= 0)
    assert 13 in nonnegative
    assert -1 not in nonnegative

    finite = Sets.Δ[4]
    assert PowerSet(finite).cardinality() == cardinal(32)
    naturals = Sets.Δ[aleph0]
    assert cardinal(naturals.cardinality()) == aleph0
    assert PowerSet(naturals).cardinality() == cardinal(2) ** aleph0


def test_fixed_and_finite_subsets_have_the_expected_universal_membership() -> None:
    source = Sets.Δ[4]
    pairs = SubsetsOfSize(source, 2)
    finite_subsets = FiniteSubsets(source)
    pair = pairs({1, 4})

    assert pair in pairs
    assert pair in finite_subsets
    assert pair.cardinality() == cardinal(2)
    assert pairs.cardinality() == cardinal(10)
    assert finite_subsets.cardinality() == cardinal(32)
    assert len(pairs) == pairs.cardinality()
    assert Set((1, 4)) in PowerSet(source)
