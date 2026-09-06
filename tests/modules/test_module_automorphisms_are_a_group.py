r"""The automorphisms of a free module are a group, and a predicate carves it.

\(\operatorname{Aut}_R(M)\) is the unit group of \(\operatorname{End}_R(M)\):
an endomorphism has a two-sided inverse in that ring exactly when it is an
isomorphism of \(M\).  Reading it that way is what makes it a group object,
and a predicate subgroup needs a group object to carve.

The specimen is the free \(\mathbf Z\)-module on two labels, whose
automorphism group is \(\mathrm{GL}_2(\mathbf Z)\).  The predicate is the
stabilizer of one basis element, a subgroup because the maps fixing a given
element are closed under composition and inverses.  Doubling is injective and
not surjective, so it is an endomorphism and not an automorphism, which is the
case that separates the unit group from the whole ring.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    OwnedGroups,
    OwnedRings,
    ZZ,
    module_homset,
    predicate_subgroup,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _plane():
    return BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))


def _swap(plane):
    return module_homset(plane, plane)(
        {"a": plane.module_generator("b"), "b": plane.module_generator("a")}
    )


def test_the_automorphisms_of_a_free_module_are_the_units_of_its_endomorphism_ring() -> None:
    plane = _plane()
    automorphisms = OwnedRings().unit_group()(plane.End())

    doubling = module_homset(plane, plane)(
        {
            "a": 2 * plane.module_generator("a"),
            "b": 2 * plane.module_generator("b"),
        }
    )

    assert automorphisms in OwnedGroups()
    assert _swap(plane) in automorphisms
    assert doubling not in automorphisms


def test_the_stabilizer_of_a_basis_element_is_a_subgroup_of_the_automorphisms() -> None:
    plane = _plane()
    a = plane.module_generator("a")
    automorphisms = OwnedRings().unit_group()(plane.End())

    stabilizer = predicate_subgroup(
        automorphisms,
        lambda automorphism: automorphism(a) == a,
        "f fixes a",
    )

    assert stabilizer in OwnedGroups()
    assert stabilizer.supergroup() is automorphisms
    assert automorphisms.one() in stabilizer
    assert _swap(plane) not in stabilizer
