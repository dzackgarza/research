r"""Archive reconciliation for the mathematical class values of a character."""

from dzack_research.preamble.all import Groups


def test_character_class_values_are_indexed_by_its_retained_conjugacy_classes() -> None:
    group = Groups.S(3)
    character = group.irreducible_characters()[1]
    representatives = character.conjugacy_class_representatives()
    values = character.class_values()

    assert values is character.values()
    assert values.index_set() is representatives
    for representative in representatives:
        assert values[representative] == character(representative)
