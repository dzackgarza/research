r"""The Lebesgue space ``L^1(RR)`` as integrable maps modulo maps vanishing almost everywhere.

``L^1 = \mathcal L^1 / N`` with ``N`` the maps vanishing off a null set; the
integral vanishes on ``N`` and so descends to the classes.  Two maps agreeing
off the single point ``0`` have the same class.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_the_integral_descends_to_classes_modulo_null_maps() -> None:
    r"""``int [e^{-|x|}] = 2`` and ``int ([e^{-|x|}] + [e^{-x^2}]) = 2 + sqrt(pi)``."""
    maps = Lp(1)
    x = maps.indeterminate()
    classes = maps.quotient_by_null_functions()
    laplace = classes(maps(exp(-abs(x))))
    gaussian = classes(maps(exp(-x * x)))

    assert classes.map_space() is maps
    assert classes.integrability_exponent() == 1
    assert classes.integration_morphism()(laplace) == 2
    assert classes.integration_morphism()(laplace + gaussian) == 2 + sqrt(pi)


def test_the_quotient_projection_preserves_the_integral() -> None:
    r"""``int pi(f) = int f`` for ``pi: \mathcal L^1 -> L^1``, at ``f = e^{-|x|}``."""
    maps = Lp(1)
    x = maps.indeterminate()
    classes = maps.quotient_by_null_functions()
    laplace = maps(exp(-abs(x)))

    assert classes.integration_morphism()(classes.quotient_projection()(laplace)) == maps.integration_morphism()(laplace)


def test_maps_that_differ_on_an_interval_have_different_classes() -> None:
    r"""``e^{-|x|} != e^{-x^2}`` on ``(0, 1)``, a set of positive measure."""
    maps = Lp(1)
    x = maps.indeterminate()
    classes = maps.quotient_by_null_functions()

    assert classes(maps(exp(-abs(x)))) != classes(maps(exp(-x * x)))


def test_maps_that_differ_only_at_the_origin_have_the_same_class() -> None:
    r"""``e^{-|x|} sgn(x)^2 = e^{-|x|}`` off ``{0}``, a null set."""
    maps = Lp(1)
    x = maps.indeterminate()
    classes = maps.quotient_by_null_functions()

    assert (classes(maps(exp(-abs(x)))) == classes(maps(exp(-abs(x)) * sgn(x) * sgn(x)))) is True


def test_two_formulas_for_one_map_have_the_same_class() -> None:
    r"""``sqrt(x^2) = |x|`` for every real ``x``, so ``e^{-sqrt(x^2)}`` and ``e^{-|x|}`` are one map."""
    maps = Lp(1)
    x = maps.indeterminate()

    assert ask(maps.almost_everywhere_equal(maps(exp(-abs(x))), maps(exp(-sqrt(x * x))))) is True
