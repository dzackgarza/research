from dzack_research.preamble.all import (
    QQ,
    QuadraticField,
)


def test_exact_embeddings_are_an_owned_ordered_finite_set() -> None:
    x = QQ.polynomial_ring("x").algebra_generator("x")
    quadratic = QuadraticField(2, "s")
    quartic = (x**4 - 2).number_field("t")
    embeddings = quadratic.exact_embeddings(quartic)

    assert embeddings.cardinality() == 2
    assert embeddings[0].domain() is quadratic
    assert embeddings[0].codomain() is quartic




