r"""Archive reconciliation for constructing characters from class values."""

from dzack_research.preamble.all import Groups


def test_character_from_class_values_round_trips_owned_character_arithmetic() -> None:
    group = Groups.S(3)
    irreducibles = group.irreducible_characters()
    source = irreducibles[0] + irreducibles[1]

    reconstructed = group.character(tuple(source.values()))

    assert reconstructed.group() is group
    assert reconstructed.codomain() is source.codomain()
    assert tuple(reconstructed.values()) == tuple(source.values())
    assert reconstructed.degree() == source.degree()
    assert reconstructed.irreducible_constituents() == source.irreducible_constituents()


def test_character_value_count_is_the_conjugacy_class_count() -> None:
    group = Groups.S(3)
    values = tuple(group.trivial_character().values())

    assert len(values) == int(group.conjugacy_classes_representatives().cardinality())
    try:
        group.character(values[:-1])
    except ValueError as error:
        assert "one value for each conjugacy class" in str(error)
    else:
        raise AssertionError("a character with a missing conjugacy-class value was accepted")


def test_arbitrary_class_function_values_are_not_relabelled_as_a_character() -> None:
    group = Groups.S(3)
    values = tuple(group.trivial_character().values())
    noncharacter = list(values)
    noncharacter[0] = noncharacter[0] + 1

    try:
        group.character(tuple(noncharacter))
    except ValueError as error:
        assert "ordinary character" in str(error)
    else:
        raise AssertionError("a non-character class function was accepted as a character")
