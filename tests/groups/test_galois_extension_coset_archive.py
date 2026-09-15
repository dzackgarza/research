from dzack_research.preamble.all import QQ, NumberField, PolynomialRing, QuadraticField
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)


def test_extensions_of_gaussian_conjugation_form_the_expected_finite_coset() -> None:
    polynomial_ring = PolynomialRing(QQ, "x")
    x = polynomial_ring.algebra_generator("x")
    cyclotomic = NumberField(x**4 - x**2 + QQ.one(), "z")
    zeta = cyclotomic.primitive_element()
    gaussian = QuadraticField(-1, "i")
    gaussian_generator = gaussian.primitive_element()

    embedding = next(
        candidate
        for candidate in gaussian.exact_embeddings(cyclotomic)
        if candidate(gaussian_generator) == zeta**3
    )
    conjugation = next(
        automorphism
        for automorphism in gaussian.exact_embeddings(gaussian)
        if automorphism(gaussian_generator) == -gaussian_generator
    )

    group = AbsoluteGaloisGroup(QQ)
    quotient = group.finite_quotient(group.extension_data(cyclotomic))
    extensions = conjugation.extensions_along(
        embedding,
        tuple(automorphism.action() for automorphism in quotient),
    )

    assert extensions.cardinality() == 2
    exponents = {
        exponent
        for exponent in (1, 5, 7, 11)
        if any(extension(zeta) == zeta**exponent for extension in extensions)
    }
    assert exponents == {7, 11}

    fixing_gaussian = {
        automorphism
        for automorphism in quotient
        if automorphism.action()(embedding(gaussian_generator))
        == embedding(gaussian_generator)
    }
    assert len(fixing_gaussian) == 2

    chosen_extension = next(
        automorphism
        for automorphism in quotient
        if automorphism.action() in extensions
    )
    finite_coset = {
        kernel_element * chosen_extension
        for kernel_element in fixing_gaussian
    }
    assert {
        automorphism.action() for automorphism in finite_coset
    } == set(extensions)
