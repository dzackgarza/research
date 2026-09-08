r"""Archive reconciliation for ordinary characters of finite groups."""

from dzack_research.preamble.categories.group.characters import character_set
from dzack_research.preamble.categories.group.groups import OwnedGroups


def test_irreducible_characters_live_in_one_owned_character_set() -> None:
    symmetric = OwnedGroups().S(3)
    characters = symmetric.irreducible_characters()
    parent = character_set(symmetric)

    assert characters.cardinality() == 3
    assert all(character.parent() is parent for character in characters)
    assert sorted(int(character.degree()) for character in characters) == [1, 1, 2]
    assert all(character(symmetric.one()) == character.degree() for character in characters)


def test_direct_sum_character_has_both_irreducible_constituents() -> None:
    symmetric = OwnedGroups().S(3)
    characters = symmetric.irreducible_characters()
    linear = next(character for character in characters if int(character.degree()) == 1)
    standard = next(character for character in characters if int(character.degree()) == 2)

    combined = linear + standard
    constituents = combined.irreducible_constituents()

    assert combined.parent() is character_set(symmetric)
    assert combined.degree() == linear.degree() + standard.degree()
    assert linear in constituents
    assert standard in constituents
    assert constituents.cardinality() == 2


def test_character_table_is_still_read_from_the_same_character_values() -> None:
    cyclic = OwnedGroups().C(3)
    characters = cyclic.irreducible_characters()
    table = cyclic.character_table()

    assert table.nrows() == int(characters.cardinality())
    assert table.ncols() == int(characters.cardinality())
    for row, character in zip(table.rows(), characters, strict=True):
        assert tuple(row) == tuple(character.values())
