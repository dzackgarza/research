
from dzack_research.preamble.all import (
    Sets,
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






def test_inverse_and_direct_image_form_the_set_subobject_galois_connection() -> None:
    source = Sets.Δ[5]
    target = Sets.Δ[2]
    residue = Sets().Mor(source, target)(lambda n: target(int(n) % 3))
    source_subsets = source.power_set()
    target_subsets = target.power_set()
    selected = source_subsets({0, 1, 3, 4})
    upper_bound = target_subsets({0, 1})

    direct = source_subsets.direct_image_morphism(residue)
    inverse = target_subsets.inverse_image_morphism(residue)
    assert direct(selected) == target_subsets({0, 1})
    assert direct(selected) <= upper_bound
    assert selected <= inverse(upper_bound)








def test_power_set_functors_transport_a_nonidentity_injection_both_ways() -> None:
    source = Sets.Δ[1]
    target = Sets.Δ[2]
    injection = Sets().Mor(source, target)(
        lambda point: target(0) if point == source(0) else target(2)
    )

    direct = Sets().power_set_functor()(injection)
    selected = source.finite_subsets()({source(0), source(1)})
    assert direct(selected) == target.finite_subsets()({target(0), target(2)})

    inverse_functor = Sets().inverse_image_power_set_functor()
    opposite = inverse_functor.opposite_morphism(injection)
    inverse = inverse_functor(opposite)
    assert inverse(target.power_set()({target(2)})) == source.power_set()({source(1)})
