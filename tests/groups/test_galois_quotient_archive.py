r"""Archive reconciliation for finite Galois quotients and restriction maps."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/profinite/galois_quotient.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
    "disposition": "reconciled-live-owner",
}


def test_restriction_map_is_the_actual_finite_galois_quotient_coordinate() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    stage = group.finite_extension(4)
    quotient = group.finite_quotient(stage)
    restriction = group.restriction_map(stage)

    assert restriction.parent() is group.Mor(quotient)
    assert restriction.domain() is group
    assert restriction.codomain() is quotient
    assert restriction.is_continuous()
    assert restriction.is_surjective()
    assert restriction(frobenius**3 * frobenius**2) == (
        restriction(frobenius**3) * restriction(frobenius**2)
    )

    kernel = restriction.kernel()
    assert kernel.supergroup() is group
    assert kernel.index() == 4
    assert frobenius not in kernel
    assert frobenius**4 in kernel


def test_restrict_along_and_extensions_along_solve_the_same_commuting_square() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    degree_two = group.finite_extension(2)
    degree_four = group.finite_extension(4)
    group.finite_quotient(degree_two)
    quotient_four = group.finite_quotient(degree_four)
    restriction_two = group.restriction_map(degree_two)
    restriction_four = group.restriction_map(degree_four)

    smaller_generator = degree_two.field().field_generators()[0]
    compatible = tuple(
        embedding
        for embedding in degree_two.field().exact_embeddings(degree_four.field())
        if degree_four.embedding()(embedding(smaller_generator))
        == degree_two.embedding()(smaller_generator)
    )
    assert len(compatible) == 1
    inclusion = compatible[0]

    sigma = restriction_four(frobenius)
    tau = restriction_two(frobenius)
    assert sigma.action().restrict_along(inclusion) == tau.action()

    extensions = tau.action().extensions_along(
        inclusion,
        tuple(candidate.action() for candidate in quotient_four),
    )
    assert extensions.cardinality() == 2
    assert sigma.action() in extensions


def test_lift_fiber_is_a_coset_of_the_restriction_kernel() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    stage = group.finite_extension(4)
    restriction = group.restriction_map(stage)
    finite_element = restriction(frobenius**3)
    coset = group.lifts(finite_element)

    assert coset.kernel() == restriction.kernel()
    assert coset.representative() == frobenius**3
    assert frobenius**3 in coset


def test_cyclotomic_restrictions_retain_the_archived_quadratic_subfield_arithmetic() -> None:
    from dzack_research.preamble.all import QQ, QuadraticField

    polynomial_ring = QQ.polynomial_ring("x")
    x = polynomial_ring.algebra_generator("x")
    cyclotomic = (x**4 - x**2 + QQ.one()).number_field("z")
    zeta = cyclotomic.primitive_element()
    gaussian = QuadraticField(-1, "i")
    real_quadratic = QuadraticField(3, "r")

    gaussian_embedding = next(
        embedding
        for embedding in gaussian.exact_embeddings(cyclotomic)
        if embedding(gaussian.primitive_element()) == zeta**3
    )
    real_embedding = next(
        embedding
        for embedding in real_quadratic.exact_embeddings(cyclotomic)
        if embedding(real_quadratic.primitive_element()) == zeta + zeta**-1
    )

    group = AbsoluteGaloisGroup(QQ)
    quotient = group.finite_quotient(group.extension_data(cyclotomic))
    expected = {
        1: (False, False),
        5: (False, True),
        7: (True, True),
        11: (True, False),
    }
    by_exponent = {
        exponent: next(
            automorphism
            for automorphism in quotient
            if automorphism(zeta) == zeta**exponent
        )
        for exponent in expected
    }

    for exponent, (moves_i, moves_root_three) in expected.items():
        automorphism = by_exponent[exponent]
        on_gaussian = automorphism.action().restrict_along(gaussian_embedding)
        on_real = automorphism.action().restrict_along(real_embedding)
        assert (
            on_gaussian(gaussian.primitive_element()) == -gaussian.primitive_element()
        ) is moves_i
        assert (
            on_real(real_quadratic.primitive_element())
            == -real_quadratic.primitive_element()
        ) is moves_root_three


def test_cyclotomic_restriction_is_multiplicative_without_a_false_absolute_lift() -> None:
    from dzack_research.preamble.all import QQ, QuadraticField

    polynomial_ring = QQ.polynomial_ring("x")
    x = polynomial_ring.algebra_generator("x")
    cyclotomic = (x**4 - x**2 + QQ.one()).number_field("z")
    zeta = cyclotomic.primitive_element()
    gaussian = QuadraticField(-1, "i")
    embedding = next(
        candidate
        for candidate in gaussian.exact_embeddings(cyclotomic)
        if candidate(gaussian.primitive_element()) == zeta**3
    )
    group = AbsoluteGaloisGroup(QQ)
    quotient = group.finite_quotient(group.extension_data(cyclotomic))
    generator = gaussian.primitive_element()

    for sigma in quotient:
        for tau in quotient:
            product = (sigma * tau).action().restrict_along(embedding)
            left = sigma.action().restrict_along(embedding)
            right = tau.action().restrict_along(embedding)
            assert product(generator) == left(right(generator))
