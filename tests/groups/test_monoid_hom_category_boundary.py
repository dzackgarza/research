r"""The monoid morphism parent is the owned fixed Hom category."""

from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.group.magmas import MonoidHomset, Monoids


def test_monoid_hom_is_the_owned_fixed_hom_category() -> None:
    monoids = Monoids()
    group = OwnedGroups().C(4)
    hom = monoids.Mor(group, group)

    assert isinstance(hom, MonoidHomset)
    assert hom is monoids.HomCategory().Of(group, group)
    assert hom.hom_family() is monoids.HomCategory()
    assert hom.homset_category() is monoids
    assert hom.domain() is group
    assert hom.codomain() is group


def test_monoid_identity_and_composition_stay_in_the_owned_hom_packet() -> None:
    monoids = Monoids()
    group = OwnedGroups().C(4)
    hom = monoids.Mor(group, group)
    generator = group.gen(0)

    square = hom(lambda element: element**2)
    identity = hom.identity()
    fourth_power = square * square

    assert identity.parent() is hom
    assert identity(generator) == generator
    assert square.parent() is hom
    assert square(generator) == generator**2
    assert fourth_power.parent() is hom
    assert fourth_power(generator) == group.one()
    assert monoids.End(group) is hom
