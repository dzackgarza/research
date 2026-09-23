r"""Archive reconciliation for automorphism groups of standard finite groups."""

import pytest

from dzack_research.preamble.categories.group.groups import OwnedGroups, Subgroups


@pytest.mark.parametrize(
    ("group", "expected_order"),
    (
        (OwnedGroups().C(8), 4),
        (OwnedGroups().V4(), 6),
        (OwnedGroups().Q(), 24),
        (OwnedGroups().S(3), 6),
        (OwnedGroups().S(6), 1440),
    ),
)
def test_standard_finite_group_automorphism_orders(group, expected_order) -> None:
    assert group.Aut().order() == expected_order


def test_aut_c8_is_elementary_abelian_of_order_four() -> None:
    automorphisms = OwnedGroups().C(8).Aut()
    identity = automorphisms.one()

    assert automorphisms.order() == 4
    assert all(element * element == identity for element in automorphisms)


def test_aut_v4_is_nonabelian_of_order_six() -> None:
    automorphisms = OwnedGroups().V4().Aut()
    elements = tuple(automorphisms)

    assert automorphisms.order() == 6
    assert any(
        left * right != right * left
        for left in elements
        for right in elements
    )


def test_conjugation_realizes_all_automorphisms_of_s3() -> None:
    group = OwnedGroups().S(3)
    conjugation = group.conjugation_morphism()
    automorphisms = group.Aut()
    inner = conjugation.image()

    assert conjugation.is_injective()
    assert conjugation.kernel().order() == 1
    assert inner.order() == automorphisms.order() == 6
    assert inner in Subgroups(automorphisms)
    assert inner.supergroup() is automorphisms
    assert inner.inclusion().domain() is inner
    assert inner.inclusion().codomain() is automorphisms
    assert inner not in automorphisms
    assert all(element.parent() is automorphisms for element in inner)


def test_s6_inner_automorphisms_have_index_two() -> None:
    group = OwnedGroups().S(6)
    conjugation = group.conjugation_morphism()
    automorphisms = group.Aut()
    inner = conjugation.image()

    assert conjugation.kernel().order() == 1
    assert inner.order() == 720
    assert automorphisms.order() == 1440
    assert inner in Subgroups(automorphisms)
    assert inner.supergroup() is automorphisms
    assert inner.inclusion().codomain() is automorphisms
    assert inner not in automorphisms
    assert all(element.parent() is automorphisms for element in inner)
