r"""Exact relation membership for selected presentations over polynomial rings."""

from dzack_research.preamble.all import QQ, FreeModule, PolynomialRing
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)


def _cyclic_quotient(ring, relation):
    free = FreeModule(ring, 1)
    generator = free.module_generator(0)
    return FinitelyPresentedModule(
        module_homset(free, free)({0: relation * generator})
    )


def test_univariate_relation_membership_is_over_the_polynomial_ring() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    module = _cyclic_quotient(ring, x)
    generator = module.module_generator(0)

    assert generator != module.zero()
    assert module.scalar_multiple(x, generator) == module.zero()


def test_multivariate_relation_membership_does_not_use_fraction_field_span() -> None:
    ring = PolynomialRing(QQ, ("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    module = _cyclic_quotient(ring, x)
    generator = module.module_generator(0)

    assert generator != module.zero()
    assert module.scalar_multiple(x, generator) == module.zero()
    assert module.scalar_multiple(y, generator) != module.zero()
