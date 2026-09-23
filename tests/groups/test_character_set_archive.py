r"""Archive reconciliation for ordinary characters of finite groups."""

from dzack_research.preamble.categories.group.groups import OwnedGroups

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/group_modules/characters.py",
    "live_owner": "src/dzack_research/preamble/categories/group/groups.py",
    "owner_overrides": {
        "RingElement": "src/dzack_research/preamble/lexicon/__init__.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_irreducible_characters_live_in_one_owned_character_set() -> None:
    symmetric = OwnedGroups().S(3)
    characters = symmetric.irreducible_characters()
    parent = symmetric.character_set()

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

    assert combined.parent() is symmetric.character_set()
    assert combined.degree() == linear.degree() + standard.degree()
    assert linear in constituents
    assert standard in constituents
    assert constituents.cardinality() == 2


