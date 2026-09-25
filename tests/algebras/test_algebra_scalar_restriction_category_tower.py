r"""Algebra categories inherit along the selected scalar restriction tower."""

from dzack_research.preamble.all import QQ, ZZ, Algebras


def test_rational_algebras_are_integer_algebras_without_a_second_object_route() -> None:
    assert Algebras(QQ).is_subcategory(Algebras(ZZ))
    assert Algebras(QQ).Associative().Unital().Commutative().is_subcategory(Algebras(ZZ).Associative().Unital().Commutative())
    assert QQ in Algebras(QQ).Associative().Unital().Commutative()
    assert QQ in Algebras(ZZ).Associative().Unital().Commutative()


def test_scalar_restriction_does_not_transport_relative_finite_presentation() -> None:
    finite_over_qq = Algebras(QQ).Associative().Unital().FinitelyPresentedAsAlgebra()
    finite_over_zz = Algebras(ZZ).Associative().Unital().FinitelyPresentedAsAlgebra()

    assert not finite_over_qq.is_subcategory(finite_over_zz)
