r"""A session in module theory over a principal ideal domain.

Free modules, submodules by generators, quotients and their invariant
factors, Hom and tensor, localization, base change, resolutions, and a
short cochain complex with its cohomology, typed as into a notebook.
"""

import pytest
from sage.misc.latex import latex

from dzack_research.preamble.all import *  # noqa: F401,F403


def rendered(obj) -> str:
    text = repr(obj)
    assert "object at 0x" not in text
    assert "object at 0x" not in latex(obj)
    return text


DOMAINS = {
    "ZZ": lambda: ZZ,
    "QQ[x]": lambda: PolynomialRing(QQ, "x"),
    "GF(5)[t]": lambda: PolynomialRing(GF(5), "t"),
    "ZZ[i]": lambda: QuadraticField(-1, "i").ring_of_integers(),
    "ZZ_3": lambda: Zp(3),
    "ZZ_(5)": lambda: ZZ.localize_at_prime(5),
}


@pytest.mark.parametrize("name", sorted(DOMAINS))
def test_a_module_session_over_a_principal_ideal_domain(name) -> None:
    ring = DOMAINS[name]()
    rendered(ring)
    fractions = ring.fraction_field()

    # A free module, elements, a submodule spanned by three vectors.
    module = FreeModule(ring, 3)
    rendered(module)
    e0, e1, e2 = module.module_generator(0), module.module_generator(1), module.module_generator(2)
    v = 2 * e0 + 4 * e1
    w = 6 * e1 + 2 * e2
    u = 4 * e0 + 8 * e1
    rendered(v)
    assert module in FreeModules(ring)
    assert module in FinitelyGeneratedFreeModules(ring)
    assert module.rank() == 3
    submodule = module.subobject_on([v, w, u])
    rendered(submodule)
    assert submodule in ModuleSubobjects(ring)
    assert submodule.rank() == 2
    assert submodule.inclusion().is_injective()
    assert v in submodule
    assert submodule.is_saturated() == ring(2).is_unit()
    saturation = submodule.saturation()
    rendered(saturation)
    assert saturation.rank() == 2
    assert saturation.is_saturated()

    # The quotient, its torsion, its annihilator.
    quotient = Cokernel(submodule.inclusion())
    rendered(quotient)
    assert quotient in FinitelyPresentedModules(ring)
    assert quotient in Modules(ring)
    assert quotient.rank() == 1
    torsion = quotient.torsion_submodule()
    rendered(torsion)
    assert torsion in TorsionModules(ring)
    assert torsion.cardinality() == ring.quotient_ring(ring.ideal(ring(2))).cardinality() ** 2
    assert quotient.annihilator() == ring.ideal(ring.zero())
    presented = FinitelyPresentedModule(submodule.inclusion())
    rendered(presented)
    assert presented.rank() == 1
    invariant_factors = presented.invariant_factors()
    rendered(invariant_factors)
    assert ring(2) in invariant_factors

    # Hom and tensor.
    homs = InternalHom(module, module)
    rendered(homs)
    assert homs.rank() == 9
    tensor = TensorProduct(module, quotient)
    rendered(tensor)
    assert tensor in Modules(ring)
    assert tensor.rank() == 3
    dual = module.dual_module()
    assert dual.rank() == 3
    assert InternalHom(quotient, ring_as_module(ring)).rank() == 1

    # A morphism, its kernel, image and cokernel; the rank–nullity relation.
    morphism = module.Mor(module)({0: e1, 1: e2, 2: 2 * e0})
    rendered(morphism)
    assert morphism.is_injective()
    assert morphism.is_surjective() == ring(2).is_unit()
    assert Kernel(morphism).rank() == 0
    assert morphism.image().rank() == 3
    assert morphism.cokernel().cardinality() == ring.quotient_ring(ring.ideal(ring(2))).cardinality()
    assert (morphism * morphism)(e0) == 2 * e1
    assert morphism.kernel().rank() + morphism.image().rank() == 3

    # Base change to the fraction field, and localization where it applies.
    extended = quotient.base_change(ring.Mor(fractions)(lambda element: fractions(element)))
    rendered(extended)
    assert extended in VectorSpaces(fractions)
    assert extended.rank() == 1
    prime = ring.spectrum()(ring.ideal(ring(2))) if ring(2) != ring.zero() and not ring(2).is_unit() else None
    if prime is not None:
        localized = quotient.localize_at_prime(prime)
        rendered(localized)
        assert localized in Modules(prime.local_ring())
        assert localized.rank() == 1

    # A free resolution of the quotient.
    resolution = free_resolution(quotient)
    rendered(resolution)
    assert resolution.is_exact()
    assert resolution.term(0).rank() == 3
    assert resolution.term(1).rank() == 2
    assert resolution.term(2).rank() == 0

    # A short cochain complex 0 -> R -> R^2 -> R -> 0 and its cohomology.
    line = FreeModule(ring, 1)
    plane = FreeModule(ring, 2)
    d0 = line.Mor(plane)({0: 2 * plane.module_generator(0) + 2 * plane.module_generator(1)})
    d1 = plane.Mor(line)({0: line.module_generator(0), 1: -line.module_generator(0)})
    complex_ = CochainComplex(ring, {0: line, 1: plane, 2: line}, {0: d0, 1: d1})
    rendered(complex_)
    assert complex_ in CochainComplexes(ring)
    assert (d1 * d0)(line.module_generator(0)) == line.zero()
    assert complex_.cohomology(0).cardinality() == 1
    assert complex_.cohomology(1).cardinality() == ring.quotient_ring(ring.ideal(ring(2))).cardinality()
    assert complex_.cohomology(2).cardinality() == 1
    for degree in (0, 1, 2):
        rendered(complex_.cohomology(degree))
