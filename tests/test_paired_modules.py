from sage.all import exp, pi, sqrt
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import (
    C,
    QQ,
    ZZ,
    FormModules,
    FormedModules,
    FreeModuleOn,
    Lp,
    PairedModules,
    Pairings,
    RR,
    ell,
)


def test_a_pairing_of_distinct_modules_is_not_a_form() -> None:
    left = FreeModuleOn(ZZ, ["a"])
    right = FreeModuleOn(ZZ, ["b"])
    pairing = Pairings(left, right, ZZ)([[2]])
    paired = PairedModules(ZZ)(pairing)
    a = left.module_generator("a")
    b = right.module_generator("b")

    assert paired in PairedModules(ZZ)
    assert paired not in FormedModules(ZZ)
    assert paired not in FormModules(ZZ)
    assert paired.left_module() is left
    assert paired.right_module() is right
    assert paired.value_module() == ZZ
    assert pairing(a, b) == 2
    assert paired.pairing(a, b) == 2


def test_the_diagonal_pairing_is_a_formed_module() -> None:
    module = FreeModuleOn(ZZ, ["e"])
    form = Pairings(module, module, ZZ)([[1]])
    formed = PairedModules(ZZ)(form)
    generator = formed.module_generator("e")

    assert form.parent() is Pairings(module, module, ZZ)
    assert formed in FormedModules(ZZ)
    assert formed in PairedModules(ZZ)
    assert formed in FormModules(ZZ)
    assert formed.left_module() is formed
    assert formed.right_module() is formed
    assert formed.b(generator, generator) == 1


def test_holder_pairs_lp_with_its_conjugate() -> None:
    maps = C(Infinity, RR)
    gaussian = maps(exp(-(maps.indeterminate() ** 2)))
    holder = Lp(1) * Lp(Infinity)
    left = Lp(1)(gaussian)
    right = Lp(Infinity)(gaussian)

    assert Lp(2) in FormedModules(RR)
    assert Lp(2) in PairedModules(RR)
    assert Lp(1) not in FormedModules(RR)
    assert holder is Lp(1).pairing_module()
    assert Lp(Infinity).pairing_module().left_module() is Lp(Infinity)
    assert holder in PairedModules(RR)
    assert holder not in FormedModules(RR)
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


def test_holder_conjugates_are_exactly_the_pairing_modules() -> None:
    assert Lp(4) * Lp(QQ(4) / 3) in PairedModules(RR)
    assert (Lp(4) * Lp(QQ(4) / 3)).left_module() is Lp(4)
    try:
        Lp(3) * Lp(3)
    except TypeError as error:
        assert "1/p + 1/q = 1" in str(error)
        return
    raise AssertionError("L^3 ⊗ L^3 is not a Hölder pairing")


def test_holder_pairs_ell_p_with_its_conjugate() -> None:
    n = ell(1).indeterminate()
    decaying = ell(1)(2 ** (-n))
    bounded = ell(Infinity)(1)
    holder = ell(1) * ell(Infinity)

    assert ell(2) in FormedModules(RR)
    assert ell(1) not in FormedModules(RR)
    assert holder is ell(1).pairing_module()
    assert holder in PairedModules(RR)
    assert holder not in FormedModules(RR)
    assert holder.left_module() is ell(1)
    assert holder.right_module() is ell(Infinity)
    assert holder.pairing(decaying, bounded) == RR(2)
    geometric = ell(2)(2 ** (-ell(2).indeterminate()))
    assert ell(2) * ell(2) is ell(2)
    assert ell(2).q(geometric) == RR(QQ(4) / 3)
