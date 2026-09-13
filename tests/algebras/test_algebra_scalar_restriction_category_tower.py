r"""Algebra categories inherit along the selected scalar restriction tower."""

from dzack_research.preamble.all import QQ, ZZ, Algebras, CommutativeAlgebras


def test_rational_algebras_are_integer_algebras_without_a_second_object_route() -> None:
    assert Algebras(QQ).is_subcategory(Algebras(ZZ))
    assert CommutativeAlgebras(QQ).is_subcategory(CommutativeAlgebras(ZZ))
    assert QQ in CommutativeAlgebras(QQ)
    assert QQ in CommutativeAlgebras(ZZ)
