r"""Native algebras use a constructed module and an actual tensor morphism."""

from dzack_research.preamble.all import Algebras, Modules, QQ, RR, ZZ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.modules.pure.modules import TensorProductModules


def test_regular_native_rings_have_their_actual_rank_one_frame_and_classifier() -> None:
    for ring in (ZZ, QQ, RR):
        assert ring in FramedFreeModules(ring).FinitelyGenerated()
        assert ring.regular_module() is ring
        frame = ring.framing_morphism()
        assert frame.codomain() is ring
        label = next(iter(frame.domain().module_generating_set()))
        assert frame(frame.domain().module_generator(label)) == ring.one()
        assert ring.linear_combination(ring.framing_coefficients(ring(7))) == ring(7)
        multiplication = ring.multiplication()
        assert multiplication.domain() in TensorProductModules(ring)
        assert multiplication.domain().tensor_factor(0) is ring
        assert multiplication.domain().tensor_factor(1) is ring
        assert multiplication.codomain() is ring
        assert multiplication(ring(3), ring(4)) == ring(12)
        assert ring.algebra_structure_morphism() is ring.Mor(ring).identity()


def test_a_second_native_module_product_does_not_replace_the_original_ring() -> None:
    tensor = Modules(QQ).tensor_product((QQ, QQ))
    zero = tensor.from_bilinear_map(QQ, lambda left, right: QQ.zero())
    algebra = Algebras(QQ)(QQ, zero)
    assert algebra is not QQ
    assert algebra.unformed_module() is QQ
    assert algebra(QQ(2)) * algebra(QQ(3)) == algebra.zero()
    assert QQ(algebra(QQ(7))) == QQ(7)
    assert QQ(algebra(QQ(2)) + algebra(QQ(3))) == QQ(5)
    assert QQ(2) * QQ(3) == QQ(6)
    assert QQ.multiplication()(QQ(2), QQ(3)) == QQ(6)


def test_relative_native_ring_keeps_its_selected_scalar_action() -> None:
    ring = QQ.polynomial_ring("x")
    x = ring.algebra_generator("x")
    assert ring.base_ring() is QQ
    product = ring.multiplication()
    assert product.domain().tensor_factor(0) is ring
    assert product.domain().tensor_factor(1) is ring
    assert product.codomain() is ring
    assert product(x + ring.one(), x - ring.one()) == x * x - ring.one()
    assert ring.scalar_multiple(QQ(3), x) == x + x + x


def test_alternate_product_on_real_scalars_preserves_both_element_readings() -> None:
    tensor = Modules(RR).tensor_product((RR, RR))
    product = tensor.from_bilinear_map(RR, lambda left, right: -(left * right))
    algebra = Algebras(RR).Associative().Unital().Commutative()(RR, product, -RR.one())
    element = algebra(RR(3))
    assert algebra is not RR
    assert RR(element) == RR(3)
    assert algebra.one() * element == element
    assert RR(element * element) == -RR(9)
    assert RR(3) * RR(3) == RR(9)


def test_monic_quotient_supplies_its_basis_before_the_native_tensor_product() -> None:
    polynomial = QQ.polynomial_ring("z")
    z = polynomial.algebra_generator("z")
    algebra = polynomial.quotient_by_relations((z**2 - QQ(2),))
    one, generator = algebra.module_generator(0), algebra.module_generator(1)
    frame = algebra.framing_morphism()
    assert frame.domain().module_rank() == 2
    assert frame.codomain() is algebra
    assert one == algebra.one()
    assert generator * generator == 2 * one
    element = one + 3 * generator
    assert algebra.linear_combination(algebra.framing_coefficients(element)) == element
    multiplication = algebra.multiplication()
    assert multiplication.domain() in FramedFreeModules(QQ).FinitelyGenerated()
    assert multiplication.domain().module_rank() == 4
    assert multiplication(generator, generator) == 2 * one
