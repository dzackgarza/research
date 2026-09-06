r"""Ring maps, and moving modules, algebras, forms and lattices along them.

Extension and restriction of scalars along the ring maps a mathematician
reaches for first, the base-change adjunction and its Hom bijection,
localization of modules, twisting by Frobenius, and the tensor–Hom
adjunction over every commutative ring.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403

RING_MAPS = {
    "ZZ->QQ": (lambda: ZZ, lambda: QQ, True, 0),
    "ZZ->GF(5)": (lambda: ZZ, lambda: GF(5), False, 5),
    "ZZ->ZZ_3": (lambda: ZZ, lambda: Zp(3), True, 0),
    "ZZ->ZZ[i]": (lambda: ZZ, lambda: QuadraticField(-1, "i").ring_of_integers(), True, 0),
    "QQ->QQ(i)": (lambda: QQ, lambda: QuadraticField(-1, "i"), True, 0),
    "ZZ->ZZ[x]": (lambda: ZZ, lambda: PolynomialRing(ZZ, "x"), True, 0),
    "GF(5)->GF(25)": (lambda: GF(5), lambda: GF(25), True, 0),
}


@pytest.fixture(params=sorted(RING_MAPS), ids=str)
def ring_map(request):
    source, target, injective, kernel_generator = RING_MAPS[request.param]
    source, target = source(), target()
    return source.Mor(target)(lambda element: target(element)), injective, kernel_generator


def test_a_ring_map_is_a_ring_morphism(ring_map) -> None:
    phi, injective, kernel_generator = ring_map
    source, target = phi.domain(), phi.codomain()
    assert phi in source.Mor(target)
    assert phi(source.one()) == target.one()
    assert phi(source(2) + source(3)) == phi(source(2)) + phi(source(3))
    assert phi(source(2) * source(3)) == phi(source(2)) * phi(source(3))
    assert phi.is_injective() == injective
    assert phi.kernel() == source.ideal(source(kernel_generator))


def test_extension_of_scalars_of_a_free_module(ring_map) -> None:
    phi, _, _ = ring_map
    source, target = phi.domain(), phi.codomain()
    module = FreeModule(source, 3)
    extended = module.base_change(phi)
    functorial = Modules(source).scalar_extension(phi)(module)

    assert extended in Modules(target)
    assert extended in FinitelyGeneratedModules(target)
    assert extended.module_rank() == 3
    assert extended.base_ring() is target
    assert functorial == extended
    if target in Fields():
        assert extended in VectorSpaces(target)


def test_extension_of_scalars_of_a_torsion_module_over_the_integers() -> None:
    torsion = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((6,))
    for name, size in (("ZZ->QQ", 1), ("ZZ->GF(5)", 1), ("ZZ->ZZ_3", 3), ("ZZ->ZZ[i]", 36)):
        source, target, _, _ = RING_MAPS[name]
        target = target()
        phi = ZZ.Mor(target)(lambda element, target=target: target(element))
        extended = torsion.base_change(phi)
        assert extended in Modules(target)
        assert extended.cardinality() == size
    two = ZZ.Mor(GF(2))(lambda element: GF(2)(element))
    assert torsion.base_change(two).cardinality() == 2
    assert torsion.base_change(two).module_rank() == 1


def test_restriction_of_scalars(ring_map) -> None:
    phi, _, _ = ring_map
    source, target = phi.domain(), phi.codomain()
    module = FreeModule(target, 2)
    restricted = Modules(target).restriction_of_scalars(phi)(module)
    also = restrict_scalars(module, phi)

    assert restricted in Modules(source)
    assert also in Modules(source)
    assert restricted.cardinality() == module.cardinality()
    if target.cardinality().is_finite():
        assert restricted.cardinality() == target.cardinality() ** 2


def test_restriction_of_scalars_of_the_gaussian_integers_to_the_integers() -> None:
    gaussian = QuadraticField(-1, "i").ring_of_integers()
    phi = ZZ.Mor(gaussian)(lambda element: gaussian(element))
    restricted = restrict_scalars(FreeModule(gaussian, 1), phi)
    assert restricted in Modules(ZZ)
    assert restricted.module_rank() == 2
    assert restricted in FinitelyGeneratedModules(ZZ)
    rationals = restrict_scalars(FreeModule(QQ, 1), ZZ.Mor(QQ)(lambda element: QQ(element)))
    assert rationals in Modules(ZZ)
    assert rationals not in FinitelyGeneratedModules(ZZ)


def test_the_base_change_adjunction(ring_map) -> None:
    phi, _, _ = ring_map
    source, target = phi.domain(), phi.codomain()
    adjunction = Modules(source).base_change_adjunction(phi)
    module = FreeModule(source, 2)
    target_module = FreeModule(target, 1)
    extended = adjunction.left_adjoint()(module)
    restricted = adjunction.right_adjoint()(target_module)

    assert extended in Modules(target)
    assert restricted in Modules(source)
    unit = adjunction.unit(module)
    assert unit.domain() is module
    assert unit.codomain() == adjunction.right_adjoint()(extended)
    counit = adjunction.counit(target_module)
    assert counit.codomain() is target_module
    assert counit.is_surjective()
    forward = extended.Mor(target_module)(
        {0: target_module.module_generator(0), 1: 2 * target_module.module_generator(0)}
    )
    transposed = adjunction.hom_set_isomorphism_forward(forward)
    assert transposed.domain() is module
    assert transposed(module.module_generator(1)) == restricted(2 * target_module.module_generator(0))
    assert adjunction.hom_set_isomorphism_inverse(transposed, target_module) == forward


def test_extension_of_scalars_of_an_algebra(ring_map) -> None:
    phi, _, _ = ring_map
    source, target = phi.domain(), phi.codomain()
    polynomials = PolynomialRing(source, "x")
    extended = CommutativeAlgebras(source).scalar_extension(phi)(polynomials)
    assert extended in CommutativeAlgebras(target)
    assert extended.algebra_generators().cardinality() == 1
    assert (extended in IntegralDomains()) == (target in IntegralDomains())
    adjunction = CommutativeAlgebras(source).base_change_adjunction(phi)
    assert adjunction.left_adjoint()(polynomials) == extended
    assert adjunction.unit(polynomials).domain() is polynomials


def test_base_change_of_a_lattice_and_of_a_form(ring_map) -> None:
    phi, _, _ = ring_map
    source, target = phi.domain(), phi.codomain()
    lattice = Lattices(source)([[2, 1], [1, 2]])
    changed = lattice.base_change(phi)
    assert changed in Lattices(target)
    assert changed in BilinearFormModules(target)
    assert changed.module_rank() == 2
    assert changed.determinant() == 3 * target.one()
    assert changed.is_nondegenerate() == (3 * target.one() != target.zero())


def test_localization_of_modules_at_a_prime_of_the_integers() -> None:
    local = ZZ.localize_at_prime(5)
    localize = module_localization_functor(local)
    torsion = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((6, 25))
    free = FreeModule(ZZ, 2)

    assert localize(torsion) in Modules(local)
    assert localize(torsion).cardinality() == 25
    assert localize(free).module_rank() == 2
    assert localize(free).base_ring() is local
    doubling = free.Mor(free)({0: 2 * free.module_generator(0), 1: free.module_generator(1)})
    assert localize(doubling).is_surjective()
    assert not doubling.is_surjective()


def test_twisting_a_module_by_frobenius() -> None:
    field = GF(4)
    frobenius = field.Mor(field)(lambda element: element**2)
    module = FreeModule(field, 2)
    twisted = twist_scalar_action(module, frobenius)
    generator = field.multiplicative_generator()
    assert twisted in Modules(field)
    assert twisted.module_rank() == 2
    assert twisted.scalar_multiple(generator, twisted.module_generator(0)) == generator**2 * twisted.module_generator(0)
    assert frobenius * frobenius == field.Mor(field).identity()


def test_the_tensor_hom_adjunction_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    fixed = FreeModule(ring, 2)
    adjunction = fixed.tensor_hom_adjunction()
    module = FreeModule(ring, 3)
    other = FreeModule(ring, 1)

    tensored = adjunction.left_adjoint()(module)
    homs = adjunction.right_adjoint()(other)
    assert tensored == module.tensor_product(fixed)
    assert homs == fixed.Hom(other)
    assert tensored.module_rank() == 6
    assert homs.module_rank() == 2
    assert adjunction.unit(module).domain() is module
    assert adjunction.counit(other).codomain() is other
    evaluation = tensored.Mor(other)({label: other.zero() for label in range(6)})
    transposed = adjunction.hom_set_isomorphism_forward(evaluation)
    assert transposed.domain() is module
    assert adjunction.hom_set_isomorphism_inverse(transposed, other) == evaluation
