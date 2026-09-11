r"""M1 exact maps constructed directly over a represented local coefficient ring.

Transported kernels already come from exactness of localization.  This file
records the complementary contract: after the coefficient ring itself is
local, an ordinary module morphism constructed there must use the same
presented kernel/cokernel machinery rather than requiring provenance from a
map over the unlocalized source ring.
"""

from dzack_research.preamble.all import QQ, BasedFreeModule, PolynomialRing, module_homset
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_direct_map_over_a_prime_local_ring_has_exact_kernel_and_cokernel() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    point = ring.spectrum()(ring.ideal(x))
    local = point.local_ring()
    source = BasedFreeModule(local, finite_ordered_set(("a", "b")))
    target = BasedFreeModule(local, finite_ordered_set(("c",)))
    morphism = module_homset(source, target)(
        {
            "a": target.module_generator("c"),
            "b": target.zero(),
        }
    )

    kernel = morphism.kernel()
    cokernel = morphism.cokernel()

    assert kernel.inclusion()(kernel.module_generator(0)) == source.module_generator("b")
    assert cokernel.is_zero()


def test_direct_local_map_detects_a_nonunit_cokernel() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    local = ring.spectrum()(ring.ideal(x)).local_ring()
    module = BasedFreeModule(local, finite_ordered_set(("g",)))
    generator = module.module_generator("g")
    multiplication_by_x = module_homset(module, module)(
        {"g": module.scalar_multiple(local(x), generator)}
    )

    quotient = multiplication_by_x.cokernel()

    assert not quotient.is_zero()
    assert quotient.minimal_number_of_generators() == 1
