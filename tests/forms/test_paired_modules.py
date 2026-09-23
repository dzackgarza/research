from sage.all import exp, pi, sqrt
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import (
    C,
    QQ,
    FormModules,
    Lp,
    PairedModules,
    RR,
    ell,
)






def test_holder_pairs_lp_with_its_conjugate() -> None:
    maps = C(Infinity, RR)
    gaussian = maps(exp(-(maps.indeterminate() ** 2)))
    holder = Lp(1) * Lp(Infinity)
    left = Lp(1)(gaussian)
    right = Lp(Infinity)(gaussian)

    assert Lp(2) in FormModules(RR)
    assert Lp(2) in PairedModules(RR)
    assert Lp(1) not in FormModules(RR)
    assert holder is Lp(1).pairing_module()
    assert Lp(Infinity).pairing_module().left_module() is Lp(Infinity)
    assert holder in PairedModules(RR)
    assert holder not in FormModules(RR)
    assert holder.left_module() is Lp(1)
    assert holder.right_module() is Lp(Infinity)
    assert holder.pairing(left, right) == RR(sqrt(pi / 2))


def test_l2_times_l2_is_the_formed_module() -> None:
    space = Lp(2)
    maps = C(Infinity, RR)
    gaussian = space(maps(exp(-(maps.indeterminate() ** 2))))

    assert space * space is space
    assert space.pairing_module() is space
    assert space.conjugate_lebesgue_space() is space
    assert space.b(gaussian, gaussian) == RR(sqrt(pi / 2))
    assert space.q(gaussian) == space.b(gaussian, gaussian)
    assert space.pairing(gaussian, gaussian) == space.b(gaussian, gaussian)




def test_holder_pairs_ell_p_with_its_conjugate() -> None:
    n = ell(1).indeterminate()
    decaying = ell(1)(2 ** (-n))
    bounded = ell(Infinity)(1)
    holder = ell(1) * ell(Infinity)

    assert ell(2) in FormModules(RR)
    assert ell(1) not in FormModules(RR)
    assert holder is ell(1).pairing_module()
    assert holder in PairedModules(RR)
    assert holder not in FormModules(RR)
    assert holder.left_module() is ell(1)
    assert holder.right_module() is ell(Infinity)
    assert holder.pairing(decaying, bounded) == RR(2)
    geometric = ell(2)(2 ** (-ell(2).indeterminate()))
    assert ell(2) * ell(2) is ell(2)
    assert ell(2).q(geometric) == RR(QQ(4) / 3)
