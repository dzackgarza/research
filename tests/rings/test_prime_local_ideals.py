r"""Ideals of a prime local ring are ideals like any other.

An ideal of ``R_p`` is the extension of an ideal of ``R``, so it is a submodule
of the regular module of ``R_p`` and carries the ideal operations.  Two things
follow that a generating set alone does not give.  A generator whose numerator
lies outside ``p`` is a unit, so the ideal it generates is everything, and the
maximal ideal is distinguished from every other ideal by containment rather
than by the name it was built under.
"""

from dzack_research.preamble.all import (
    CommutativeIdeals,
    PrincipalIdealDomains,
    QQ,
    ZZ,
    aleph0,
)


def test_a_prime_local_ideal_is_an_ideal_of_the_local_ring() -> None:
    local = ZZ.localize_at_prime(2)

    assert local.maximal_ideal() in CommutativeIdeals(local)
    assert local.ideal(local(2)) in CommutativeIdeals(local)


def test_a_unit_generates_the_whole_prime_local_ring() -> None:
    local = ZZ.localize_at_prime(2)

    assert local(3).is_unit()
    assert local.ideal(local(3)).contains_ambient_element(local.one())
    assert local.ideal(local(3)) == local.ideal(local.one())
    assert local.ideal(local(3)) != local.maximal_ideal()


def test_the_maximal_ideal_is_the_non_units() -> None:
    local = ZZ.localize_at_prime(2)

    assert local.maximal_ideal() == local.ideal(local(2))
    assert local.maximal_ideal().contains_ambient_element(local(2))
    assert local.maximal_ideal().contains_ambient_element(local(4))
    assert not local.maximal_ideal().contains_ambient_element(local.one())
    assert not local.maximal_ideal().contains_ambient_element(local(3))


def test_a_prime_local_principal_quotient_has_residue_size_to_valuation() -> None:
    local = ZZ.localize_at_prime(2)
    quotient = local.quotient_ring(local.ideal(local(8)))

    assert quotient.cardinality() == 8


def test_prime_local_ideals_of_a_nonreduced_quotient_need_no_fraction_field() -> None:
    r"""``QQ[x,y]/(xy)`` at the origin: a local ring of a ring with zero divisors."""
    presentation = QQ.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    node = (presentation).quotient_by_relations((x * y,))
    x0 = node.algebra_generator("x")
    y0 = node.algebra_generator("y")

    local = node.localize_at_prime(node.ideal(x0, y0))

    assert local.maximal_ideal() in CommutativeIdeals(local)
    assert local.maximal_ideal().contains_ambient_element(local(x0))
    assert local.maximal_ideal().contains_ambient_element(local(y0))
    assert not local.maximal_ideal().contains_ambient_element(local.one())


def test_localization_of_a_polynomial_pid_remains_a_pid() -> None:
    polynomial = QQ.polynomial_ring("x")
    x = polynomial.algebra_generator("x")
    local = polynomial.localize_at_prime(polynomial.ideal(x))

    assert polynomial in PrincipalIdealDomains()
    assert local in PrincipalIdealDomains()
    assert local.cardinality() == aleph0
    assert not local(x).is_unit()
    assert local(6).is_unit()
