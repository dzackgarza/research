r"""The monoid morphism parent is the owned fixed Mor category."""

from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.group.magmas import MonoidMor, Monoids


def test_monoid_mor_is_the_owned_fixed_mor_category() -> None:
    monoids = Monoids()
    group = OwnedGroups().C(4)
    mor = monoids.Mor(group, group)

    assert isinstance(mor, MonoidMor)
    assert mor is monoids.MorCategory().Of(group, group)
    assert mor.mor_family() is monoids.MorCategory()
    assert mor.mor_category() is monoids
    assert mor.domain() is group
    assert mor.codomain() is group


def test_monoid_identity_and_composition_stay_in_the_owned_mor_packet() -> None:
    monoids = Monoids()
    group = OwnedGroups().C(4)
    mor = monoids.Mor(group, group)
    generator = group.gen(0)

    square = mor(lambda element: element**2)
    identity = mor.identity()
    fourth_power = square * square

    assert identity.parent() is mor
    assert identity(generator) == generator
    assert square.parent() is mor
    assert square(generator) == generator**2
    assert fourth_power.parent() is mor
    assert fourth_power(generator) == group.one()
    assert monoids.End(group) is mor
