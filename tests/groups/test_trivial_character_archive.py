r"""Archive reconciliation for the ordinary trivial character."""

from dzack_research.preamble.all import Groups
from dzack_research.preamble.categories.group.characters import character_set


def test_finite_group_trivial_character_is_one_on_every_conjugacy_class() -> None:
    group = Groups.S(3)
    character = group.trivial_character()

    assert character.parent() is character_set(group)
    assert character.group() is group
    assert character.degree() == character.codomain().one()
    for representative in group.conjugacy_classes_representatives():
        assert character(representative) == character.codomain().one()


def test_trivial_character_is_an_irreducible_constituent_of_itself() -> None:
    group = Groups.S(3)
    character = group.trivial_character()
    constituents = character.irreducible_constituents()

    assert constituents.cardinality() == 1
    constituent = next(iter(constituents))
    assert constituent.degree() == constituent.codomain().one()
    for representative in group.conjugacy_classes_representatives():
        assert constituent(representative) == constituent.codomain().one()
