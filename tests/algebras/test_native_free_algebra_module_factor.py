r"""The native free algebra has the module basis of all words or monomials.

Stacks, Tag 00DM: the tensor algebra is the direct sum of tensor powers,
and the symmetric algebra of a free module is the polynomial algebra.
The specified monomials below test the correspondence, not just its two
implementations composed with each other.
"""

from dzack_research.preamble.all import Algebras, Modules, NN, QQ, ZZ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules


def test_symmetric_algebra_constructs_the_full_monomial_frame():
    module = QQ.free_module(("a", "b"))
    algebra = module.symmetric_algebra()
    a, b = algebra.algebra_generator("a"), algebra.algebra_generator("b")
    free = algebra.framing_source()
    labels = free.module_generating_set()
    cubics = labels.cofactor(NN(3))
    aab = labels(NN(3), cubics.from_multiplicities({"a": 2, "b": 1}))

    assert algebra.free_source_module() is module
    assert algebra.graded_piece(1) is module
    assert algebra.graded_piece(3) is module.symmetric_power(3)
    assert free is not module
    assert free in FramedFreeModules(QQ)
    assert not free.module_rank().is_finite()
    assert algebra.module_generator(aab) == a * a * b
    assert algebra.framing_coefficients(7 * a * a * b) == {aab: QQ(7)}
    assert algebra.framing_morphism()(free.module_generator(aab)) == a * a * b
    assert algebra.scalar_multiple(QQ(7), a * a * b) == 7 * a * a * b
    assert Algebras(QQ).underlying_module()(algebra) is algebra
    assert algebra in Modules(QQ)


def test_tensor_algebra_frame_keeps_the_order_and_repeated_letters():
    module = QQ.free_module(("a", "b"))
    algebra = module.tensor_algebra()
    a, b = algebra.algebra_generator("a"), algebra.algebra_generator("b")
    free = algebra.framing_source()
    labels = free.module_generating_set()
    words = labels.cofactor(NN(3))
    aba = labels(NN(3), words(lambda i: ("a", "b", "a")[int(i)]))
    aab = labels(NN(3), words(lambda i: ("a", "a", "b")[int(i)]))

    assert algebra.free_source_module() is module
    assert algebra.graded_piece(3) is module.tensor_power(3)
    assert free in FramedFreeModules(QQ)
    assert algebra.module_generator(aba) == a * b * a
    assert algebra.module_generator(aab) == a * a * b
    assert aba != aab
    assert algebra.framing_coefficients(2 * a * b * a - 3 * a * a * b) == {
        aba: QQ(2), aab: QQ(-3),
    }
    assert algebra.multiplication()(a * b, a) == a * b * a


def test_univariate_native_coefficients_are_decoded_without_enumerating_the_frame():
    algebra = ZZ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    labels = algebra.module_generating_set()
    seventh = labels(NN(7), labels.cofactor(NN(7)).from_multiplicities({"x": 7}))
    third = labels(NN(3), labels.cofactor(NN(3)).from_multiplicities({"x": 3}))
    empty = labels(NN(0), labels.cofactor(NN(0)).from_multiplicities({}))
    element = x**7 + 3 * x**3 + 11 * algebra.one()

    assert algebra.framing_coefficients(element) == {
        seventh: ZZ(1), third: ZZ(3), empty: ZZ(11),
    }
    assert algebra.linear_combination(algebra.framing_coefficients(element)) == element
    assert algebra.module_generator(empty) == algebra.one()


def test_native_monomial_coefficients_keep_the_exact_polynomial_scalar_ring():
    scalars = QQ.polynomial_ring("t")
    t = scalars.algebra_generator("t")
    algebra = scalars.polynomial_ring(("x", "y"))
    x, y = algebra.algebra_generator("x"), algebra.algebra_generator("y")
    element = algebra(t) * x**3 + algebra(t + scalars.one()) * y
    coefficients = algebra.framing_coefficients(element)

    assert algebra.base_ring() is scalars
    assert all(value.parent() is scalars for value in coefficients.values())
    assert set(coefficients.values()) == {t, t + scalars.one()}
    assert algebra.linear_combination(coefficients) == element
    assert algebra.scalar_multiple(t, x) == algebra(t) * x


def test_free_algebra_on_the_zero_module_has_only_the_empty_word():
    module = QQ.free_module(0)
    for algebra in (module.tensor_algebra(), module.symmetric_algebra()):
        free = algebra.framing_source()
        assert algebra.free_source_module() is module
        assert free.module_rank() == 1
        labels = tuple(free.module_generating_set())
        assert len(labels) == 1
        assert labels[0].summand_index() == 0
        assert algebra.module_generator(labels[0]) == algebra.one()
        assert algebra.framing_coefficients(algebra(QQ(5))) == {labels[0]: QQ(5)}
        assert algebra.graded_piece(1) is module


def test_native_variable_spelling_does_not_replace_the_chosen_generator_labels():
    module = QQ.free_module(("first letter", "second letter"))
    for algebra in (module.tensor_algebra(), module.symmetric_algebra()):
        left = algebra.algebra_generator("first letter")
        right = algebra.algebra_generator("second letter")
        element = left * right + 2 * left
        assert algebra.free_source_module() is module
        assert algebra.algebra_generating_set() is module.module_generating_set()
        assert algebra.linear_combination(algebra.framing_coefficients(element)) == element


def test_raw_native_polynomials_reach_the_same_constructed_module():
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
    from sage.rings.rational_field import QQ as SageQQ
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
    from dzack_research.preamble.categories.rings.commutative_algebra import _refine_commutative_algebra

    algebra = _own_ring(PolynomialRing(SageQQ, "x"))
    assert algebra is QQ.polynomial_ring("x")
    assert algebra in FramedFreeModules(QQ)
    assert _refine_commutative_algebra(algebra, QQ, ("x",)) is algebra
    x = algebra.algebra_generator("x")
    assert algebra.linear_combination(algebra.framing_coefficients(x**5 + algebra.one())) == x**5 + algebra.one()


def test_polynomial_coproduct_retains_the_module_frame_and_both_inclusions():
    left = QQ.polynomial_ring("x")
    right = QQ.polynomial_ring("y")
    coproduct = Algebras(QQ).Associative().Unital().Commutative().coproduct((left, right))
    x = coproduct.left_coproduct_map()(left.algebra_generator("x"))
    y = coproduct.right_coproduct_map()(right.algebra_generator("y"))
    element = x**2 * y + 3 * y

    assert coproduct in FramedFreeModules(QQ)
    assert coproduct.left_coproduct_map().domain() is left
    assert coproduct.right_coproduct_map().domain() is right
    assert coproduct.linear_combination(coproduct.framing_coefficients(element)) == element
    assert coproduct.multiplication()(x**2, y) == x**2 * y
