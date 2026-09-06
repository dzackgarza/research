r"""Equality of localization fractions is relation membership over the source.

``m/s = m'/s'`` in ``S^{-1}M`` exactly when some element of ``S`` kills the
cross difference ``d = s'm - sm'``.  On a chosen presentation ``M = coker(A)``
that says the annihilator of ``d``, the transporter carrying its coordinates
into the relations, meets ``S``, so equality is decided by the presentation
algorithm rather than by searching for a denominator witness.

The specimen is ``QQ[x,y]/(xy)`` with ``y`` inverted.  There ``x`` becomes zero,
because ``y`` annihilates it, while the generator does not.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedModule,
    PolynomialRing,
    QQ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _coordinate_axes():
    r"""Return ``QQ[x,y]``, its variables, and ``QQ[x,y]/(xy)`` on one generator."""
    ring = PolynomialRing(QQ, ("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    free = BasedFreeModule(ring, finite_ordered_set(("g",)))
    relations = BasedFreeModule(ring, finite_ordered_set(("r",)))
    module = FinitelyPresentedModule(
        module_homset(relations, free)(
            {"r": free.scalar_multiple(x * y, free.module_generator("g"))}
        )
    )
    return ring, x, y, module


def test_the_annihilator_of_an_element_is_its_transporter_into_the_relations() -> None:
    ring, x, y, module = _coordinate_axes()

    on_the_axis = module.scalar_multiple(x, module.module_generator("g"))

    assert module.annihilator_of(on_the_axis) == ring.ideal(y)
    assert module.annihilator_of(module.module_generator("g")) == ring.ideal(x * y)


def test_inverting_the_annihilator_of_an_element_makes_that_element_zero() -> None:
    _ring, x, y, module = _coordinate_axes()
    localized = module.localize(y)

    on_the_axis = module.scalar_multiple(x, module.module_generator("g"))

    assert localized.fraction(on_the_axis).equality_status(localized.zero()) is True


def test_the_generator_survives_inverting_a_scalar_outside_its_annihilator() -> None:
    _ring, _x, y, module = _coordinate_axes()
    localized = module.localize(y)

    assert localized.fraction(module.module_generator("g")).equality_status(
        localized.zero()
    ) is False
