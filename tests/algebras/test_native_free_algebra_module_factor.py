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

    assert algebra.generating_module() is module
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

    assert algebra.generating_module() is module
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
        assert algebra.generating_module() is module
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
        assert algebra.generating_module() is module
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


def test_free_forgetful_counits_evaluate_the_full_polynomial_module():
    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    for adjunction in (
        Modules(QQ).tensor_algebra_adjunction(),
        Modules(QQ).symmetric_algebra_adjunction(),
    ):
        unit = adjunction.unit(algebra)
        counit = adjunction.counit(algebra)
        formal = counit.domain()
        assert formal.generating_module() is algebra
        assert unit.codomain() is formal
        assert counit.codomain() is algebra
        assert counit(unit(x**3 + 2 * x + algebra.one())) == x**3 + 2 * x + algebra.one()

        # The generator labelled by 1 in U(A) is not the unit of F(U(A)).
        # Evaluation sends both to 1; identifying them at construction would
        # not give the free algebra on the underlying module.
        constant_label, = algebra.framing_coefficients(algebra.one())
        constant_generator = formal.algebra_generator(constant_label)
        assert constant_generator != formal.one()
        assert counit(constant_generator) == algebra.one()
        assert counit(formal.one()) == algebra.one()


def test_scalar_extension_rebuilds_tensor_and_symmetric_algebras_from_the_changed_generating_module():
    ring_map = ZZ.Mor(QQ)(lambda scalar: QQ(scalar))
    module = ZZ.free_module(("x", "y"))
    module_extension = Modules(ZZ).scalar_extension(ring_map)
    algebra_extension = (
        Algebras(ZZ).Associative().Unital().base_change_adjunction(ring_map).left_adjoint()
    )
    changed_module = module_extension(module)

    for algebra in (module.tensor_algebra(), module.symmetric_algebra()):
        changed = algebra_extension(algebra)
        x = changed.algebra_generator("x")
        y = changed.algebra_generator("y")

        assert changed.generating_module() is changed_module
        assert changed.graded_piece(1) is changed_module
        assert changed.unformed_module() is not changed_module
        assert changed.unformed_module().base_ring() is QQ
        assert changed.homogeneous_degree(x * y) == 2
        assert changed.multiplication().domain().tensor_factor(0) is changed.unformed_module()
        assert changed.multiplication().domain().tensor_factor(1) is changed.unformed_module()

        match algebra:
            case _ if algebra is module.tensor_algebra():
                assert x * y != y * x
            case _:
                assert x * y == y * x


def test_scalar_extension_of_free_algebra_morphism_uses_the_full_word_module():
    ring_map = ZZ.Mor(QQ)(lambda scalar: QQ(scalar))
    module = ZZ.free_module(("x", "y"))
    algebra = module.tensor_algebra()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    endomorphism = algebra.Mor(algebra)(
        {"x": x * y + 2 * x, "y": y}
    )
    extension = (
        Algebras(ZZ).Associative().Unital().base_change_adjunction(ring_map).left_adjoint()
    )
    changed = extension(algebra)
    changed_map = extension(endomorphism)
    changed_x = changed.algebra_generator("x")
    changed_y = changed.algebra_generator("y")

    assert changed_map.domain() is changed
    assert changed_map.codomain() is changed
    assert changed_map(changed_x) == changed_x * changed_y + 2 * changed_x
    assert changed_map(changed_x * changed_y) == (
        changed_x * changed_y + 2 * changed_x
    ) * changed_y


def test_sparse_free_algebra_scalar_extension_keeps_infinite_word_semantics():
    ring_map = ZZ.Mor(QQ)(lambda scalar: QQ(scalar))
    module = ZZ.free_module(NN)
    algebra = module.tensor_algebra()
    extension = (
        Algebras(ZZ).Associative().Unital().base_change_adjunction(ring_map).left_adjoint()
    )
    changed = extension(algebra)
    changed_module = Modules(ZZ).scalar_extension(ring_map)(module)
    a = changed.algebra_generator(NN(2))
    b = changed.algebra_generator(NN(5))

    assert changed.generating_module() is changed_module
    assert changed.graded_piece(1) is changed_module
    assert changed.unformed_module() is not changed_module
    assert not changed.module_generating_set().cardinality().is_finite()
    assert a * b != b * a
    assert changed.homogeneous_degree(a * b * a) == 3
