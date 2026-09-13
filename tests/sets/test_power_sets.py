
from dzack_research.preamble.all import (
    ZZ,
    FiniteSubsets,
    PowerSet,
    PowerSets,
    Set,
    Sets,
    SubsetsOfSize,
    aleph0,
    cardinal,
)
from dzack_research.preamble.categories.sets.set_categories import (
    FinitePowerSets,
    FixedCardinalitySubsetSets,
    FunctionSets,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/sets/sets.sage",
    "live_owner": "src/dzack_research/preamble/categories/sets/set_categories.py",
    "owner_overrides": {
        "ObjectSetFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "CartesianProductFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "DisjointUnionFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "ExponentialFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "InverseImagePowerSetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "FinitePowerSetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "FixedCardinalitySubsetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "object_set_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "ObjectSet": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "finite_ordered_set": "src/dzack_research/preamble/categories/sets/finite_ordered_sets.py",
        "ordered_set_owned_by": "src/dzack_research/preamble/categories/sets/finite_ordered_sets.py",
        "E": "src/dzack_research/preamble/categories/schemes/ade_surfaces.py",
    },
    "disposition": "reconciled-live-owner",
}


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
    residue = Sets().Mor(source, target)(lambda n: target(int(n) % 3))
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
    assert naturals.cardinality() == aleph0
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
    assert Set(pairs).cardinality() == pairs.cardinality()
    assert Set((1, 4)) in PowerSet(source)


def test_set_collection_notation_routes_through_owning_categories() -> None:
    source = Sets.Δ[3]
    target = Sets.Δ[1]

    declared_power = PowerSets()(source)
    declared_pairs = FixedCardinalitySubsetSets()(source, 2)
    declared_finite = FinitePowerSets()(source)
    declared_functions = FunctionSets()(target, source)

    assert declared_power.base_set() is source
    assert declared_pairs.source() is source
    assert declared_pairs.subset_cardinality() == 2
    assert declared_finite.source() is source
    assert declared_functions.base() is target
    assert declared_functions.exponent() is source
    assert PowerSet(source).base_set() is source
    assert SubsetsOfSize(source, 2).source() is source
    assert FiniteSubsets(source).source() is source


def test_power_set_functors_transport_a_nonidentity_injection_both_ways() -> None:
    from dzack_research.preamble.categories.functors.set_constructions import (
        finite_power_set_functor,
        inverse_image_power_set_functor,
    )

    source = Sets.Δ[1]
    target = Sets.Δ[2]
    injection = Sets().Mor(source, target)(
        lambda point: target(0) if point == source(0) else target(2)
    )

    direct = finite_power_set_functor()(injection)
    selected = FiniteSubsets(source)({source(0), source(1)})
    assert direct(selected) == FiniteSubsets(target)({target(0), target(2)})

    inverse_functor = inverse_image_power_set_functor()
    opposite = inverse_functor.opposite_morphism(injection)
    inverse = inverse_functor(opposite)
    assert inverse(PowerSet(target)({target(2)})) == PowerSet(source)({source(1)})
