r"""Free and permutation groups expose their defining basis and natural action data."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_rank_two_free_group_retains_basis_generators_and_reduced_words() -> None:
    group = Groups.Free(2)
    basis = group.free_basis()
    first = group.free_generator(basis[0])
    second = group.free_generator(basis[1])
    word = group.reduced_word(first * second.inverse())

    assert basis.cardinality() == cardinal(2)
    assert first == group.group_generator(basis[0])
    assert second == group.group_generator(basis[1])
    assert word.cardinality() == cardinal(2)


def test_symmetric_three_retains_natural_points_action_and_sign() -> None:
    group = Groups.S(3)
    points = group.natural_points()
    action = group.natural_g_set()
    transposition = group.group_generators()[0]

    assert points.cardinality() == cardinal(3)
    assert action.underlying_set() is points
    assert transposition.sign() in (ZZ(-1), ZZ(1))
