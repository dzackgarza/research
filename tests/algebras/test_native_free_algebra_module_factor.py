r"""The native free algebra has the module basis of all words or monomials.

Stacks, Tag 00DM: the tensor algebra is the direct sum of tensor powers,
and the symmetric algebra of a free module is the polynomial algebra.
The specified monomials below test the correspondence, not just its two
implementations composed with each other.
"""

from dzack_research.preamble.all import Algebras, Modules, QQ, ZZ


















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


