r"""A commutative owned ring becomes its own commutative algebra after initialization."""

from dzack_research.preamble.all import ZZ, Algebras


def test_integer_ring_self_algebra_uses_the_finished_owned_parent() -> None:
    category = Algebras(ZZ).Associative().Unital().Commutative()

    assert ZZ in category
    assert ZZ.algebra_base_ring() is ZZ
    structure = ZZ.algebra_structure_morphism()
    assert structure.domain() is ZZ
    assert structure.codomain() is ZZ.ring_center()
    assert structure(ZZ(7)) == ZZ(7)


def test_exact_real_field_initializes_the_product_needed_by_function_algebras() -> None:
    from dzack_research.preamble.all import RR

    assert RR.unformed_module() is RR
    assert RR.multiplication()(RR(2), RR(3)) == RR(6)
    assert RR.algebra_structure_morphism() is RR.Mor(RR).identity()
    assert RR.unit_morphism()(RR(5)) == RR(5)


def test_native_products_supply_coefficients_to_their_own_tensor_classifier() -> None:
    from dzack_research.preamble.all import QQ, RR, ZZ

    for ring in (ZZ, QQ, RR):
        left, right = ring(2), ring(3)
        assert left * right == ring(6)
        assert ring.multiplication()(left, right) == left * right
        classifier = ring.multiplication_morphism()
        assert classifier(classifier.domain().pure_tensor(left, right)) == ring(6)
        vector = ring.free_module(1).module_generator(0)
        assert left * vector == vector + vector


def test_reflected_native_product_keeps_noncommutative_operand_order() -> None:
    from dzack_research.preamble.all import QQ

    algebra = QQ.free_module(("x", "y")).tensor_algebra()
    x, y = algebra.algebra_generator("x"), algebra.algebra_generator("y")
    assert x * y != y * x
    assert (x * y).__rmul__(y) == y * (x * y)
