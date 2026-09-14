from dzack_research.preamble.all import (
    QQ,
    AbsoluteGaloisGroup,
    NumberField,
    PolynomialRing,
    QuadraticField,
    exact_embeddings,
)


def test_exact_embeddings_are_an_owned_ordered_finite_set() -> None:
    x = PolynomialRing(QQ, "x").algebra_generator("x")
    quadratic = QuadraticField(2, "s")
    quartic = NumberField(x**4 - 2, "t")
    embeddings = exact_embeddings(quadratic, quartic)

    assert embeddings.cardinality() == 2
    assert embeddings[0].domain() is quadratic
    assert embeddings[0].codomain() is quartic


def test_finite_galois_automorphisms_are_owned_and_indexed() -> None:
    field = QuadraticField(-1, "i")
    quotient = field.galois_group()
    automorphisms = quotient.extension_data().automorphisms()

    assert automorphisms.cardinality() == quotient.order()
    assert automorphisms[0].domain() is field
    assert automorphisms[0].codomain() is field


def test_absolute_galois_realized_stages_are_an_owned_finite_set() -> None:
    group = AbsoluteGaloisGroup(QQ)
    stages = group.one().realized_stages()

    assert stages.cardinality() == 0
