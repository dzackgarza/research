r"""One construction, one object.

``S^{-1}R``, ``R_p``, ``R/I`` and an ideal are each determined by their data,
so writing the same construction twice names one object and must return one.

Where the data is an ideal the key is exact, because ideals decide their own
equality: the quotient by ``(2)`` and the quotient by ``(2,4)`` are one ring
and one object.  Where the data is a generating family for a submonoid the key
is that family as written, since deciding when two finitely generated
submonoids of a commutative monoid coincide is beyond what the preamble can
do.
"""

from dzack_research.preamble.all import (
    PolynomialRing,
    QQ,
    QuotientRing,
    ZZ,
)


def test_an_ideal_is_one_object() -> None:
    assert ZZ.ideal(6) is ZZ.ideal(6)

    line = PolynomialRing(QQ, "x")
    x = line.algebra_generator("x")
    assert line.ideal(x) is line.ideal(x)


def test_a_localization_is_one_object() -> None:
    assert ZZ.localization(2) is ZZ.localization(2)


def test_a_prime_localization_is_one_object() -> None:
    assert ZZ.localize_at_prime(5) is ZZ.localize_at_prime(5)
    assert ZZ.localize_at_prime(5) is ZZ.localize_at_prime(ZZ.ideal(5))


def test_a_quotient_ring_is_one_object() -> None:
    assert QuotientRing(ZZ, ZZ.ideal(6)) is QuotientRing(ZZ, ZZ.ideal(6))


def test_a_quotient_is_keyed_on_the_ideal_not_on_how_it_was_written() -> None:
    assert ZZ.ideal(2) == ZZ.ideal(2, 4)
    assert QuotientRing(ZZ, ZZ.ideal(2)) is QuotientRing(ZZ, ZZ.ideal(2, 4))


def test_an_ideal_of_a_localization_is_one_object() -> None:
    local = ZZ.localize_at_prime(2)

    assert local.ideal(local(2)) is local.ideal(local(2))
    assert local.ideal(local(2)) is local.maximal_ideal()
