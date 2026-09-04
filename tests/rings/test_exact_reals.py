import math

import pytest

from sage.all import AA, QQ, QQbar, RDF, RBF, RIF, RLF, SR, ZZ, e, exp, log, pi, sqrt
from sage.categories.fields import Fields
from sage.misc.unknown import Unknown
from sage.rings.real_mpfr import RR as SageRR

from dzack_research.preamble.logic import ask
from dzack_research.preamble.rings import RR, RealApproximation


def test_rr_is_the_exact_real_field() -> None:
    assert RR in Fields()
    assert RR.is_exact()
    assert RR.characteristic() == 0
    assert RR.base_ring() is RR


def test_sqrt_two_is_exact() -> None:
    root = RR(sqrt(2))

    assert root.parent() is RR
    assert root**2 == 2
    assert root * root == 2
    assert sqrt(RR(2)) ** 2 == 2


def test_transcendental_constants_are_exact_real_elements() -> None:
    assert pi in RR
    assert e in RR
    assert log(2) in RR
    assert RR.pi() == RR(pi)
    assert RR.e() == RR(e)
    assert exp(RR(1)) == RR(e)


def test_nonreal_numbers_are_not_in_rr() -> None:
    assert QQbar(sqrt(2)) in RR
    assert QQbar(-sqrt(2)) in RR
    assert QQbar.gen() not in RR
    assert SR(-1).sqrt() not in RR


def test_the_real_algebraic_subfield_coerces_but_qqbar_does_not() -> None:
    assert RR.has_coerce_map_from(ZZ)
    assert RR.has_coerce_map_from(QQ)
    assert RR.has_coerce_map_from(AA)
    assert not RR.has_coerce_map_from(QQbar)

    value = AA(sqrt(2)) + RR(1)
    assert value.parent() is RR
    assert value - 1 == RR(sqrt(2))

    # QQbar -> RR is partial, so it cannot be a Sage coercion map.  Individual
    # real algebraic values nevertheless belong to RR and convert explicitly.
    algebraic = QQbar(sqrt(2))
    assert algebraic in RR
    assert RR(algebraic) ** 2 == 2


def test_approximations_are_not_silently_reclassified_as_exact() -> None:
    for approximation in (
        0.1,
        SageRR(0.1),
        RDF(0.1),
        RBF(0.1),
        RIF(0.1),
        SR(0.1),
        pi + SR(0.1),
    ):
        assert approximation not in RR

    # RLF advertises itself as exact, but its value semantics are lazy
    # numerical enclosures: in particular RLF(sqrt(2))^2 != 2 in Sage.
    assert RLF(sqrt(2)) not in RR


def test_n_is_the_explicit_approximation_boundary() -> None:
    value = RR(pi).n()
    high_precision = RR(pi).n(prec=200)

    assert not value.parent().is_exact()
    assert not high_precision.parent().is_exact()
    assert abs(float(value) - math.pi) < 1e-15


def test_real_approximation_is_the_decimal_literal_constructor() -> None:
    value = RealApproximation("0.1")

    assert not value.parent().is_exact()
    assert value not in RR


def test_preamble_decimal_literals_remain_explicit_approximations() -> None:
    from sage.repl.preparse import preparse

    lowered = preparse("x = 1.25")
    assert lowered == "x = RealApproximation('1.25')"


def test_decidable_equalities_return_booleans() -> None:
    assert (RR(sqrt(2)) ** 2 == RR(2)) is True
    assert (RR(sqrt(2)) == RR(sqrt(8)) / 2) is True
    assert (RR(sqrt(2)) == RR(3)) is False


def test_unresolved_equality_is_a_predicate_for_ask() -> None:
    # Close enough that the constructor's 128-bit ball cannot separate it,
    # but 256 bits can.  No approximate value enters either real number.
    q = QQ(3141592653589793238462643383279502884197) / 10**39
    proposition = RR(pi) == RR(q)

    with pytest.raises(TypeError):
        bool(proposition)
    assert ask(proposition, max_prec=128) is Unknown
    assert ask(proposition) is False


def test_order_relations_are_certified_not_floating_point_guesses() -> None:
    assert (RR(pi) > RR(3)) is True
    assert (RR(e) < RR(3)) is True
    assert (RR(sqrt(2)) > RR(QQ(7) / 5)) is True
