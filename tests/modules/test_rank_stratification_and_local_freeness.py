r"""The rank of a module is a function on the spectrum, and it stratifies it.

A module that is not locally free has no rank.  It has a fibre dimension at
each point, and the Fitting ideals say where each value is taken: the fibre has
dimension at least ``d`` on the closed set cut out by ``Fitt_{d-1}``, so each
value is taken on a locally closed stratum.  Freeness at a point is the
neighbouring statement, that the next Fitting ideal down localizes to zero.

The specimen is ``R/(x) + R`` over ``QQ[x]``, which is free of rank one away
from the origin and has a two-dimensional fibre there.
"""

from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedModule,
    PolynomialRing,
    QQ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _torsion_plus_free():
    r"""Return ``QQ[x]``, its variable, and ``R/(x) + R`` presented on two generators."""
    ring = PolynomialRing(QQ, "x")
    x = ring.algebra_generator("x")
    free = BasedFreeModule(ring, finite_ordered_set(("g", "h")))
    relations = BasedFreeModule(ring, finite_ordered_set(("r",)))
    module = FinitelyPresentedModule(
        module_homset(relations, free)(
            {"r": free.scalar_multiple(x, free.module_generator("g"))}
        )
    )
    return ring, x, module


def test_the_rank_function_is_a_morphism_out_of_the_spectrum() -> None:
    ring, x, module = _torsion_plus_free()
    spectrum = ring.spectrum()

    rank = module.rank_function()

    assert rank.domain() is spectrum
    assert rank(spectrum.generic_point()) == 1
    assert rank(spectrum(ring.ideal(x))) == 2


def test_the_strata_separate_the_generic_point_from_the_origin() -> None:
    ring, x, module = _torsion_plus_free()
    spectrum = ring.spectrum()
    generic = spectrum.generic_point()
    origin = spectrum(ring.ideal(x))

    assert generic in module.rank_stratum(1)
    assert origin not in module.rank_stratum(1)
    assert origin in module.rank_stratum(2)
    assert generic not in module.rank_stratum(2)


def test_the_module_is_free_away_from_the_origin_and_not_at_it() -> None:
    ring, x, module = _torsion_plus_free()
    spectrum = ring.spectrum()

    locus = module.local_freeness_locus()

    assert spectrum.generic_point() in locus
    assert spectrum(ring.ideal(x)) not in locus


def test_the_annihilator_of_a_sum_of_cyclic_modules_over_a_non_pid() -> None:
    r"""``Ann(R/(x) + R/(y))`` is ``(x) cap (y) = (xy)``, computed generator by generator."""
    ring = PolynomialRing(QQ, ("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    free = BasedFreeModule(ring, finite_ordered_set(("g", "h")))
    relations = BasedFreeModule(ring, finite_ordered_set(("r", "s")))
    module = FinitelyPresentedModule(
        module_homset(relations, free)(
            {
                "r": free.scalar_multiple(x, free.module_generator("g")),
                "s": free.scalar_multiple(y, free.module_generator("h")),
            }
        )
    )

    assert module.annihilator() == ring.ideal(x * y)
    assert module.annihilator() == module.scalar_action().kernel()
