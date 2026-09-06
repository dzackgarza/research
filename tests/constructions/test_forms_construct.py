r"""Bilinear and quadratic forms a mathematician expects, over every named ring.

Forms on free modules from a Gram matrix, pairings between two modules, the
form as a morphism out of the tensor or divided square, torsion forms with
values in $K/R$, the free-form adjunctions, base change of forms, and form
embeddings.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403

A2_GRAM = [[2, 1], [1, 2]]


def test_a_symmetric_bilinear_form_from_a_gram_matrix(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    form = BilinearForm(module, ring, A2_GRAM)
    e0, e1 = form.module_generator(0), form.module_generator(1)

    assert form in BilinearFormModules(ring)
    assert form in SymmetricBilinearFormModules(ring)
    assert form in FormModules(ring)
    assert form in Modules(ring)
    assert form.unformed_module() is module
    assert form.value_module() == ring.regular_module()
    assert form.b(e0, e1) == ring.one()
    assert form.b(e0, e0) == 2 * ring.one()
    assert form.b(e0, e1) == form.b(e1, e0)
    assert form.b(e0 + e1, e0 - e1) == ring.zero()
    assert e0.b(e1) == form.b(e0, e1)
    assert form.determinant() == 3 * ring.one()
    assert form.is_nondegenerate() == (3 * ring.one() != ring.zero())
    assert form.correlation_morphism().is_injective() == (3 * ring.one() != ring.zero())
    assert form.dual_module().module_rank() == 2
    assert form.twist(2).determinant() == 12 * ring.one()
    assert ring.one() in form.scale_submodule()


def test_the_form_is_a_morphism_out_of_the_tensor_square(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    form = BilinearForm(module, ring, A2_GRAM)
    morphism = form.form()
    square = TensorSquare(module)

    assert morphism.domain() is square
    assert morphism.codomain() == form.value_module()
    assert morphism in BilinearForms(module, ring)
    e0, e1 = module.module_generator(0), module.module_generator(1)
    assert morphism(square.pure_tensor(e0, e1)) == form.value_module().module_generator(0)
    assert morphism(square.pure_tensor(e0, e0)) == 2 * form.value_module().module_generator(0)
    assert BilinearForms(module, ring)(A2_GRAM) == morphism


def test_a_quadratic_form_from_its_gram_matrix(commutative_ring) -> None:
    r"""$q(x, y) = x^2 + xy + y^2$ with polar form $b(e_0, e_1) = 1$."""
    ring = commutative_ring
    module = FreeModule(ring, 2)
    quadratic = QuadraticForm(module, ring, [[1, 1], [0, 1]])
    e0, e1 = quadratic.module_generator(0), quadratic.module_generator(1)

    assert quadratic in QuadraticFormModules(ring)
    assert quadratic in FormModules(ring)
    assert quadratic.q(e0) == ring.one()
    assert quadratic.q(e1) == ring.one()
    assert quadratic.q(e0 + e1) == 3 * ring.one()
    assert quadratic.q(2 * e0) == 4 * ring.one()
    assert quadratic.b(e0, e1) == ring.one()
    assert e0.q() == ring.one()
    assert quadratic.form().domain() is DividedSquare(module)
    assert QuadraticForms(module, ring)([[1, 1], [0, 1]]) == quadratic.form()


def test_a_pairing_between_two_modules(commutative_ring) -> None:
    ring = commutative_ring
    left = FreeModule(ring, 2)
    right = FreeModule(ring, 3)
    pairing = Pairings(left, right, ring)([[1, 0, 2], [0, 1, 0]])
    assert pairing.domain().tensor_factors().cardinality() == 2
    assert pairing(pairing.domain().pure_tensor(left.module_generator(0), right.module_generator(2))) == 2 * ring.one()
    assert pairing(pairing.domain().pure_tensor(left.module_generator(1), right.module_generator(0))) == ring.zero()


def test_a_form_module_from_a_form_morphism(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    morphism = BilinearForms(module, ring)(A2_GRAM)
    formed = FormModule(morphism)
    assert formed in FormModules(ring)
    assert formed.unformed_module() is module
    assert formed.form() == morphism
    assert formed.b(formed.module_generator(0), formed.module_generator(1)) == ring.one()


def test_the_free_form_adjunctions_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    for adjunction, category in (
        (Modules(ring).free_bilinear_form_adjunction(), BilinearFormModules(ring)),
        (Modules(ring).free_quadratic_form_adjunction(), QuadraticFormModules(ring)),
    ):
        free = adjunction.left_adjoint()(module)
        assert free in category
        assert adjunction.right_adjoint()(free) in Modules(ring)
        assert adjunction.right_adjoint()(free).module_rank() == 2
        unit = adjunction.unit(module)
        assert unit.domain() is module
        assert unit.codomain() == adjunction.right_adjoint()(free)
        counit = adjunction.counit(free)
        assert counit.codomain() is free


def test_base_change_of_a_form(build) -> None:
    form = BilinearForm(FreeModule(ZZ, 2), ZZ, A2_GRAM)
    rational = form.base_change(ZZ.Mor(QQ)(lambda n: QQ(n)))
    mod_three = form.base_change(ZZ.Mor(GF(3))(lambda n: GF(3)(n)))
    mod_five = form.base_change(ZZ.Mor(GF(5))(lambda n: GF(5)(n)))

    assert rational in BilinearFormModules(QQ)
    assert rational.determinant() == 3
    assert rational.is_nondegenerate()
    assert mod_three in BilinearFormModules(GF(3))
    assert not mod_three.is_nondegenerate()
    assert mod_five.is_nondegenerate()
    assert mod_five.determinant() == GF(5)(3)


@pytest.mark.parametrize(
    "name, modulus, size",
    [("ZZ", 2, 2), ("ZZ", 12, 12), ("ZZ", 1, 1), ("QQ[x]", None, aleph0), ("ZZ[i]", 3, 9), ("ZZ_3", 9, 9)],
)
def test_fraction_field_quotients(build, name, modulus, size) -> None:
    r"""$\tfrac{1}{m}R/R \cong R/mR$ inside $K/R$."""
    ring = build(name)
    element = ring.algebra_generator("x") ** 2 if modulus is None else ring(modulus)
    quotient = FractionFieldQuotient(ring, element)

    assert quotient in FractionFieldQuotients(ring)
    assert quotient in Modules(ring)
    assert quotient.base_ring() is ring
    assert quotient.fraction_field() is ring.fraction_field()
    assert quotient.cardinality() == size
    assert quotient.modulus() == element
    generator = quotient.module_generator(0)
    assert element * generator == quotient.zero()


def test_discriminant_forms_from_relations_and_gram() -> None:
    r"""The discriminant form of $A_1 = \langle -2\rangle$ and the form $u(2)$."""
    values = FractionFieldQuotient(ZZ, 2)
    a1 = TorsionQuadraticFormModules(ZZ).from_relations_and_gram([[2]], [[-QQ(1) / 2]], values)
    u2 = TorsionQuadraticFormModules(ZZ).from_relations_and_gram(
        [[2, 0], [0, 2]], [[0, QQ(1) / 2], [QQ(1) / 2, 0]], values
    )
    generator = a1.module_generator(0)

    assert a1 in TorsionQuadraticFormModules(ZZ)
    assert a1.cardinality() == 2
    assert a1.q(generator) == values(-QQ(1) / 2)
    assert a1.q(2 * generator) == values.zero()
    assert a1.is_anisotropic()
    assert not a1.is_metabolic()
    assert a1.O().order() == 1
    assert a1.brown_invariant() == 7
    assert a1.is_isometric_to(Lattices(ZZ)("A1").discriminant_quadratic_form())
    assert u2.cardinality() == 4
    assert u2.is_metabolic()
    assert not u2.is_anisotropic()
    assert u2.lagrangian_subgroups().cardinality() == 2
    assert u2.isotropic_elements().cardinality() == 3
    assert u2.brown_invariant() == 0
    assert u2.O().order() == 2
    assert not u2.is_isometric_to(a1 + a1)


def test_a_torsion_bilinear_form() -> None:
    values = FractionFieldQuotient(ZZ, 1)
    form = TorsionBilinearFormModules(ZZ).from_relations_and_gram([[4]], [[QQ(1) / 4]], values)
    generator = form.module_generator(0)
    assert form in TorsionBilinearFormModules(ZZ)
    assert form.cardinality() == 4
    assert form.b(generator, generator) == values(QQ(1) / 4)
    assert form.b(2 * generator, 2 * generator) == values.zero()
    assert form.O().order() == 2
    assert form.is_isometric_to(form)
    assert form.is_anti_isometric(form.twist(-1))
    assert form.normal_form().cardinality() == 4


def test_form_embeddings_between_lattices() -> None:
    a1 = Lattices(ZZ)("A1")
    a2 = Lattices(ZZ)("A2")
    embedding = form_embedding(a1, a2, [a2.module_generator(0)])
    assert embedding.domain() is a1
    assert embedding.codomain() is a2
    assert embedding.is_injective()
    assert embedding.is_primitive()
    assert embedding.orthogonal_complement().module_rank() == 1
    assert embedding.orthogonal_complement().determinant() == 6
    assert embedding in a1.Emb(a2)


def test_determinant_lines_and_exterior_forms(commutative_ring) -> None:
    module = FreeModule(commutative_ring, 3)
    assert DeterminantLine(module).module_rank() == 1
    assert ExteriorForms(module, 0).module_rank() == 1
    assert ExteriorForms(module, 1).module_rank() == 3
    assert ExteriorForms(module, 2).module_rank() == 3
    assert ExteriorForms(module, 3).module_rank() == 1
    assert ExteriorForms(module, 4).module_rank() == 0


def test_forms_over_a_polynomial_ring_and_over_a_field() -> None:
    polynomials = PolynomialRing(QQ, "x")
    x = polynomials.algebra_generator("x")
    form = BilinearForm(FreeModule(polynomials, 2), polynomials, [[x, 1], [1, x]])
    e0, e1 = form.module_generator(0), form.module_generator(1)
    assert form.determinant() == x**2 - 1
    assert form.is_nondegenerate()
    assert form.b(e0, e0) == x
    specialized = form.base_change(polynomials.Mor(QQ)({"x": QQ(1)}))
    assert specialized in BilinearFormModules(QQ)
    assert not specialized.is_nondegenerate()
    assert specialized.radical().module_rank() == 1
