"""CAP-backed kernels for cochain complexes over ``ZZ[x]``.

The provider is ModulePresentationsForCAP.  The public objects below are the
ordinary owned modules, subobjects and cohomology quotients; no CAP object is
part of the assertions.
"""

from dzack_research.preamble.all import ZZ, PolynomialRing
from dzack_research.preamble.categories.functors.cohomology import cohomology_functor
from dzack_research.preamble.categories.modules import (
    BasedFreeModule,
    CochainComplex,
    cochain_homset,
    module_homset,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _specimen():
    ring = PolynomialRing(ZZ, "x")
    x = ring.algebra_generator("x")
    source = BasedFreeModule(ring, finite_ordered_set(("a", "b")))
    target = BasedFreeModule(ring, finite_ordered_set(("c",)))
    a = source.module_generator("a")
    b = source.module_generator("b")
    c = target.module_generator("c")
    differential = module_homset(source, target)(
        {
            "a": target.scalar_multiple(ring(2), c),
            "b": target.scalar_multiple(x, c),
        }
    )
    complex_ = CochainComplex(ring, {0: source, 1: target}, {0: differential})
    return ring, x, source, target, a, b, c, differential, complex_


def test_cap_kernel_retains_the_syzygy_inclusion_and_lift() -> None:
    ring, x, source, _target, a, b, _c, differential, _complex = _specimen()
    kernel = differential.kernel()
    candidate = source.scalar_multiple(-x, a) + source.scalar_multiple(ring(2), b)

    assert kernel.inclusion().is_in_image(candidate)
    lifted = kernel.inclusion().lift(candidate)
    assert kernel.inclusion()(lifted) == candidate
    assert int(kernel.number_of_module_generators()) == 1

    coefficients = module_coefficients(lifted, kernel)
    nonzero = tuple(coefficient for coefficient in coefficients.values() if coefficient)
    assert len(nonzero) == 1
    assert nonzero[0].is_unit()


def test_cap_cohomology_retains_the_quotient_projection_R_mod_2_x() -> None:
    ring, x, _source, target, _a, _b, c, _differential, complex_ = _specimen()
    h1 = complex_.cohomology(1)
    one_class = h1.class_of_cycle(c)

    assert one_class != h1.zero()
    assert h1.class_of_cycle(target.scalar_multiple(ring(2), c)) == h1.zero()
    assert h1.class_of_cycle(target.scalar_multiple(x, c)) == h1.zero()
    assert h1.cycle_representative(one_class) == c


def test_cap_cohomology_is_functorial_on_a_nonidentity_cochain_map() -> None:
    ring, _x, source, target, _a, _b, c, _differential, complex_ = _specimen()
    zero = cochain_homset(complex_, complex_)(
        {
            0: module_homset(source, source)(
                {label: source.zero() for label in source.module_generating_set()}
            ),
            1: module_homset(target, target)(
                {label: target.zero() for label in target.module_generating_set()}
            ),
        }
    )
    functor = cohomology_functor(ring, 1)
    h1 = functor(complex_)
    nonzero = h1.class_of_cycle(c)
    induced = functor(zero)

    assert nonzero != h1.zero()
    assert induced(nonzero) == h1.zero()
    assert induced != module_homset(h1, h1).identity()
