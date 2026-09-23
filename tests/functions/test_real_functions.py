from sage.all import (
    QQ,
    SR,
    exp,
    factorial,
    log,
    pi,
    sin,
    sqrt,
    zeta,
)
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import (
    RR,
    C,
    FormModules,
    Lp,
    PairedModules,
    ell,
)




















def test_smooth_maps_have_formal_taylor_series() -> None:
    maps = C(Infinity, RR)
    x = maps.indeterminate()
    exponential = maps(exp)
    maclaurin = exponential.maclaurin_series()
    expansion_at_one = exponential.taylor_series(1)
    sine = maps(sin).maclaurin_series()
    geometric = maps(1 / (1 + x)).maclaurin_series()
    cubic = maps(x**3).maclaurin_series()
    jet = C(2, RR)(x**3).maclaurin_series()

    assert maclaurin[0] == 1
    assert maclaurin[1] == 1
    assert maclaurin[5] == QQ(1) / factorial(5)
    assert expansion_at_one[0] == exp(1)
    assert expansion_at_one[1] == exp(1)
    assert expansion_at_one[2] == exp(1) / 2
    assert sine[0] == 0
    assert sine[1] == 1
    assert sine[2] == 0
    assert sine[3] == QQ(-1) / 6
    assert geometric[0] == 1
    assert geometric[1] == -1
    assert geometric[3] == -1
    assert cubic[3] == 1
    assert cubic[4] == 0
    assert jet[0] == 0
    assert jet[1] == 0
    assert jet[2] == 0
    assert jet[3] == 0
    assert ell(2)(maclaurin)(5) == QQ(1) / factorial(5)

    try:
        Lp(2)(exp(-(Lp(2).indeterminate() ** 2))).maclaurin_series()
    except TypeError as error:
        assert "C^k" in str(error)
    else:
        raise AssertionError("L^p is not a C^k mapping space")

    try:
        ell(2)(1 / factorial(ell(2).indeterminate())).maclaurin_series()
    except TypeError as error:
        assert "C^k" in str(error)
    else:
        raise AssertionError("ell^p is not a C^k mapping space")

    def square(point):
        return point * point

    try:
        maps(square).maclaurin_series()
    except ValueError as error:
        assert "placed" in str(error)
        return
    raise AssertionError("a placed callable has no Taylor series")




def test_l2_is_the_formed_lebesgue_space() -> None:
    space = Lp(2)
    maps = C(Infinity, RR)
    gaussian = space(maps(exp(-(maps.indeterminate() ** 2))))
    pairing = space.b(gaussian, gaussian)

    assert pairing == RR(sqrt(pi / 2))
    assert gaussian.b(gaussian) == pairing
    assert space.q(gaussian) == pairing










def test_ell2_is_the_formed_sequence_space() -> None:
    space = ell(2)
    geometric = space(2 ** (-space.indeterminate()))
    pairing = space.b(geometric, geometric)

    assert pairing == RR(QQ(4) / 3)
    assert geometric.b(geometric) == pairing
    assert space.q(geometric) == pairing


def test_holder_pairs_ell_p_with_its_conjugate() -> None:
    n = ell(1).indeterminate()
    decaying = ell(1)(2 ** (-n))
    bounded = ell(Infinity)(1)
    holder = ell(1) * ell(Infinity)

    assert ell(2) * ell(2) is ell(2)
    assert ell(2).pairing_module() is ell(2)
    assert holder is ell(1).pairing_module()
    assert holder in PairedModules(RR)
    assert holder not in FormModules(RR)
    assert holder.pairing(decaying, bounded) == RR(2)
    try:
        ell(3) * ell(3)
    except TypeError as error:
        assert "1/p + 1/q = 1" in str(error)
        return
    raise AssertionError("ell^3 ⊗ ell^3 is not a Hölder pairing")






def test_ell2_pairing_sums_classical_series() -> None:
    n = ell(2).indeterminate()
    geometric = ell(2)(2 ** (-n))
    harmonic = ell(2)(1 / (n + 1))
    basel = ell(2)(1 / (n + 1) ** 2)
    alternating = ell(2)((-1) ** n / (n + 1))
    exponential = ell(2)(1 / factorial(n))
    t = SR.var("t")

    assert harmonic(3) == QQ(1) / 4
    assert exponential(5) == QQ(1) / factorial(5)
    assert ell(2).b(harmonic, harmonic) == RR(pi**2 / 6)
    assert ell(2).b(basel, basel) == RR(pi**4 / 90)
    assert ell(2).b(harmonic, basel) == RR(zeta(3))
    assert ell(2).b(geometric, harmonic) == RR(2 * log(2))
    assert ell(2).b(harmonic, alternating) == RR(pi**2 / 12)
    assert ell(2).b(exponential, geometric) == RR(exp(QQ(1) / 2))
    assert (ell(1) * ell(Infinity)).pairing(
        ell(1)(1 / factorial(n)), ell(Infinity)(1)
    ) == RR(exp(1))
    assert exponential.generating_series() == exp(t)
    assert harmonic.generating_series() == -log(1 - t) / t
