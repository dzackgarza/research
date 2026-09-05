r"""Feeding the session's objects into one another.

Lattices over orders, polynomials over quotients, matrices over polynomials,
quotients of quotients, localizations of quotients, completions of
localizations, spectra of all of these, Kähler differentials of localizations
and quotients, tensor products and pushouts of algebras, the trace form of a
number field as a lattice, and morphisms as matrices.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_lattices_over_orders_and_over_p_adics(build) -> None:
    for name, size in (("ZZ[i]", 9), ("ZZ[sqrt-5]", 9), ("ZZ_3", 3), ("ZZ[phi]", 9)):
        ring = build(name)
        lattice = Lattices(ring)([[2, 1], [1, 2]])
        assert lattice in Lattices(ring)
        assert lattice.determinant() == 3 * ring.one()
        assert lattice.dual_lattice().rank() == 2
        assert lattice.discriminant_module().cardinality() == size


def test_polynomials_over_quotients_orders_and_polynomial_rings(build) -> None:
    over_order = PolynomialRing(build("ZZ[i]"), "x")
    over_quotient = PolynomialRing(Zmod(12), "x")
    iterated = PolynomialRing(PolynomialRing(QQ, "x"), "y")
    assert over_order in IntegralDomains()
    assert over_order in NoetherianRings()
    assert over_order.krull_dimension() == 2
    assert over_quotient not in IntegralDomains()
    assert over_quotient.krull_dimension() == 1
    assert iterated in IntegralDomains()
    assert iterated.krull_dimension() == 2
    assert iterated in CommutativeAlgebras(PolynomialRing(QQ, "x"))
    assert iterated in CommutativeAlgebras(QQ)


def test_matrices_over_polynomial_rings_and_modules_over_matrix_algebras() -> None:
    polynomials = PolynomialRing(QQ, "x")
    x = polynomials.algebra_generator("x")
    matrices = MatrixSpace(polynomials, 2)
    jordan = matrices.from_rows([[x, 1], [0, x]])
    assert jordan.determinant() == x**2
    assert (jordan * jordan).matrix_entry(0, 1) == 2 * x
    assert jordan.transpose().matrix_entry(1, 0) == 1
    over_matrices = FreeModule(MatrixSpace(QQ, 2), 2)
    assert over_matrices in Modules(MatrixSpace(QQ, 2))
    assert over_matrices.rank() == 2


def test_quotients_of_quotients_and_localizations_of_quotients() -> None:
    twelve = Zmod(12)
    four = twelve.quotient_ring(twelve.ideal(twelve(4)))
    local = twelve.localize_at_prime(twelve.ideal(twelve(2)))
    assert four.cardinality() == 4
    assert four.characteristic() == 4
    assert local in LocalRings()
    assert local.cardinality() == 4
    assert local.residue_field().cardinality() == 2
    assert twelve.spectrum().closed_set(twelve.ideal(twelve(2)))
    polynomials = PolynomialRing(QQ, "x")
    x = polynomials.algebra_generator("x")
    cubic = polynomials.quotient_ring(polynomials.ideal(x**3))
    assert cubic.quotient_ring(cubic.ideal(cubic.quotient_map()(x**2))).cardinality() == aleph0
    assert cubic in LocalRings()
    assert cubic.residue_field().characteristic() == 0
    assert cubic.residue_field().cardinality() == aleph0


def test_completions_of_localizations_and_fraction_fields_of_quotients() -> None:
    local = ZZ.localize_at_prime(5)
    completion = local.adic_completion(local.maximal_ideal())
    assert completion in CompleteLocalRings()
    assert completion.residue_field().cardinality() == 5
    assert completion.characteristic() == 0
    assert local.fraction_field() is QQ
    polynomials = PolynomialRing(ZZ, "x")
    x = polynomials.algebra_generator("x")
    gaussian = polynomials.quotient_ring(polynomials.ideal(x**2 + 1))
    fractions = gaussian.fraction_field()
    assert fractions in Fields()
    assert fractions.characteristic() == 0
    assert fractions in OwnedNumberFields()
    assert fractions.degree() == 2


@pytest.mark.parametrize(
    "name, points",
    [("ZZ_(5)", 2), ("ZZ_3", 2), ("ZZ/12", 2), ("QQ[x]/(x^3)", 1), ("GF(4)", 1), ("QQ(x)", 1), ("QQ[e]/(e^2)", 1), ("ZZ/8", 1)],
)
def test_the_underlying_space_of_the_spectrum_of_a_small_ring(build, name, points) -> None:
    ring = build(name)
    assert Spec(ring).underlying_space().cardinality() == points
    assert ring.spectrum().cardinality() == points


def test_spectra_with_infinitely_many_points(build) -> None:
    for name in ("ZZ", "ZZ[i]", "QQ[x]", "ZZ[x]", "QQ[x,y]"):
        assert build(name).spectrum().cardinality() == aleph0
    assert build("RR").spectrum().cardinality() == 1


def test_kahler_differentials_of_localizations_and_quotients(build) -> None:
    local = KahlerDifferentials(build("ZZ_(5)").as_algebra_over(ZZ))
    dual = KahlerDifferentials(build("GF(2)[t]/(t^2)").as_algebra_over(GF(2)))
    finite = KahlerDifferentials(Zmod(12).as_algebra_over(ZZ))
    assert local.cardinality() == 1
    assert dual.cardinality() == 4
    assert finite.cardinality() == 1
    integers = PolynomialRing(ZZ, "x")
    x = integers.algebra_generator("x")
    quotient = integers.quotient_ring(integers.ideal(x**2 + 1))
    assert KahlerDifferentials(quotient.as_algebra_over(ZZ)).cardinality() == 4


def test_tensor_products_and_pushouts_of_algebras() -> None:
    first = PolynomialRing(QQ, "x")
    second = PolynomialRing(QQ, "y")
    plane = commutative_algebra_coproduct(first, second)
    assert plane in CommutativeAlgebraCoproducts(QQ)
    assert plane in CommutativeAlgebras(QQ)
    assert plane.krull_dimension() == 2
    assert plane in IntegralDomains()
    assert plane.coproduct_injection(0)(first.algebra_generator("x")) * plane.coproduct_injection(1)(second.algebra_generator("y")) != plane.zero()
    gaussian = build_gaussian_rationals()
    split = commutative_algebra_coproduct(gaussian, gaussian)
    assert split not in IntegralDomains()
    assert split.krull_dimension() == 0

    parameter = PolynomialRing(QQ, "t")
    t = parameter.algebra_generator("t")
    square = parameter.Mor(first)({"t": first.algebra_generator("x") ** 2})
    cube = parameter.Mor(second)({"t": second.algebra_generator("y") ** 3})
    glued = commutative_algebra_pushout(square, cube)
    assert glued in CommutativeAlgebraPushouts(QQ)
    assert glued.krull_dimension() == 1
    assert glued in IntegralDomains()
    fibered = scheme_fiber_product(Spec(square), Spec(cube))
    assert fibered.relative_dimension() == 1
    assert fibered in AffineSchemes(QQ)
    assert fibered.coordinate_ring() == glued


def build_gaussian_rationals():
    return QuadraticField(-1, "i").as_algebra()


def test_the_trace_form_of_a_number_field_is_a_lattice(build) -> None:
    for name, discriminant in (("QQ(i)", -4), ("QQ(sqrt5)", 5), ("QQ(cbrt2)", -108)):
        field = build(name)
        basis = field.ring_of_integers().integral_basis()
        gram = [[(a * b).trace() for b in basis] for a in basis]
        trace_form = Lattices(ZZ)(gram)
        assert trace_form.rank() == field.degree()
        assert trace_form.determinant() == discriminant
        assert trace_form.discriminant_group().cardinality() == abs(discriminant)
        assert trace_form.is_nondegenerate()


def test_a_torsion_module_with_a_form_and_a_lattice_over_it() -> None:
    values = FractionFieldQuotient(ZZ, 1)
    form = TorsionBilinearFormModules(ZZ).from_relations_and_gram([[4]], [[QQ(1) / 4]], values)
    assert form.cardinality() == 4
    torsion = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))
    assert torsion.cardinality() == form.cardinality()
    assert form.unformed_module().cardinality() == 4


def test_module_morphisms_as_matrices_and_back(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    e0, e1 = module.module_generator(0), module.module_generator(1)
    morphism = module.Mor(module)({0: e0 + e1, 1: 2 * e1})
    matrix = morphism.matrix()
    homs = module.Hom(module)

    assert matrix in MatrixSpace(ring, 2)
    assert matrix.determinant() == 2 * ring.one()
    assert homs.from_morphism(morphism) in homs
    assert homs.as_morphism(homs.from_morphism(morphism)) == morphism
    assert (morphism * morphism).matrix() == matrix * matrix
    assert morphism.is_surjective() == ring(2).is_unit()


def test_schemes_over_orders_and_over_quotients(build) -> None:
    gaussian = build("ZZ[i]")
    line = AffineSpace(1, gaussian)
    projective = ProjectiveSpace(1, Zmod(12))
    assert line in AffineSchemes(gaussian)
    assert line.relative_dimension() == 1
    assert line.coordinate_ring().krull_dimension() == 2
    assert projective.relative_dimension() == 1
    assert Spec(Zp(3)).relative_dimension() == 0
    assert Spec(gaussian) in AffineSchemes(ZZ)
    assert Spec(gaussian.as_algebra_over(ZZ)).structure_morphism().codomain() == Spec(ZZ)
