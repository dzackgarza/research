from sage.all import (
    QQ,
    SR,
    ZZ,
    Integer,
    LaurentPolynomialRing,
    LaurentSeriesRing,
    PolynomialRing,
    PowerSeriesRing,
    exp,
    factorial,
    log,
    pi,
    sin,
    sqrt,
    zeta,
)
from sage.rings.infinity import Infinity
from sage.rings.semirings.non_negative_integer_semiring import NN

from dzack_research.preamble.all import (
    CommutativeAlgebras,
    Algebras,
    C,
    FormModules,
    FormedModules,
    Lp,
    PairedModules,
    RR,
    SymmetricBilinearFormModules,
    VectorSpaces,
    ell,
)


def test_c_is_parameterized_by_regularity_and_spaces() -> None:
    maps = C(Infinity, RR)

    assert maps is C(Infinity, RR, RR)
    assert maps is C(Infinity, RR)
    assert maps in VectorSpaces(RR)
    assert maps in Algebras(RR)
    assert maps in CommutativeAlgebras(RR)
    assert maps.differentiability() is Infinity
    assert maps.domain() is RR
    assert maps.codomain() is RR
    assert C(2, RR) is not maps
    assert C(2, RR).differentiability() == 2
    assert C(2, RR) in Algebras(RR)


def test_polynomials_exponentials_and_coordinates_evaluate() -> None:
    maps = C(Infinity, RR)
    x = maps.coordinate()
    exponential = maps(exp)
    quadratic = maps(x.expression() ** 2 + 1)

    assert x(3) == 3
    assert exponential(0) == 1
    assert quadratic(2) == 5
    assert (exponential * x)(0) == 0
    assert exponential(x * x)(0) == 1


def test_smooth_real_maps_are_the_function_algebra() -> None:
    maps = C(Infinity, RR)
    exponential = maps(exp)
    constants = maps.algebra_structure_morphism()

    assert maps.algebra_base_ring() is RR
    assert maps.one()(5) == 1
    assert (maps(2) * exponential)(0) == 2
    assert constants(RR(3))(1) == 3
    assert maps.cardinality() is Infinity
    assert maps.is_integral_domain() is False
    assert maps.is_field() is False
    assert Lp(2) not in Algebras(RR)
    assert ell(2) not in Algebras(RR)


def test_integral_formula_is_the_indefinite_integral_from_a_basepoint() -> None:
    maps = C(Infinity, RR)
    x = maps.coordinate()
    antiderivative = maps.integral(x, 0)

    assert antiderivative(2) == 2
    assert antiderivative.derivative()(3) == 3


def test_series_and_laurent_polynomials_are_formulas() -> None:
    maps = C(Infinity, RR)
    polynomials = PolynomialRing(QQ, "t")
    t = polynomials.algebra_generator("t")
    series_ring = PowerSeriesRing(QQ, "u")
    u = series_ring.algebra_generator("u")
    laurent_ring = LaurentPolynomialRing(QQ, "w")
    w = laurent_ring.algebra_generator("w")
    laurent_series = LaurentSeriesRing(QQ, "z")
    z = laurent_series.algebra_generator("z")

    assert maps(t**2 + 1)(2) == 5
    assert maps(1 + u + u**2)(1) == 3
    assert maps(w + w**-1)(2) == QQ(2) + QQ(1) / 2
    assert maps(z**-1 + z)(2) == QQ(2) + QQ(1) / 2


def test_ratios_and_rational_functions_evaluate() -> None:
    maps = C(Infinity, RR)
    x = maps.coordinate()
    rational = maps((1 + x) / (1 + x * x))
    polynomials = PolynomialRing(QQ, "t")
    t = polynomials.algebra_generator("t")
    field = polynomials.fraction_field()

    assert rational(0) == 1
    assert maps(field((1 + t) / (1 + t**2)))(0) == 1


def test_callables_are_trusted_by_placement() -> None:
    maps = C(1, RR)

    def square(point):
        return point * point

    placed = maps(square)

    assert square not in maps
    assert placed in maps
    assert placed in C(0, RR)
    assert placed not in C(2, RR)
    assert placed(3) == 9
    assert (placed + placed)(2) == 8


def test_finite_regularity_derivative_lowers_k() -> None:
    cubic = C(2, RR)(SR.var("x") ** 3)

    derivative = cubic.derivative()
    assert derivative.parent() is C(1, RR)
    assert derivative(2) == 12


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
        Lp(2)(exp).maclaurin_series()
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


def test_lebesgue_space_places_formulas_and_callables() -> None:
    space = Lp(2)
    maps = C(Infinity, RR)
    gaussian = maps(exp(-(maps.indeterminate() ** 2)))

    def bump(point):
        return exp(-(point * point))

    assert space in VectorSpaces(RR)
    assert space in SymmetricBilinearFormModules(RR)
    assert space in FormedModules(RR)
    assert space in PairedModules(RR)
    assert Lp(1) not in FormModules(RR)
    assert Lp(1) not in FormedModules(RR)
    assert space.integrability_exponent() == 2
    assert space(gaussian)(0) == 1
    assert space(bump)(0) == 1
    assert Lp(Infinity).integrability_exponent() is Infinity


def test_l2_is_the_formed_lebesgue_space() -> None:
    space = Lp(2)
    maps = C(Infinity, RR)
    gaussian = space(maps(exp(-(maps.indeterminate() ** 2))))
    pairing = space.b(gaussian, gaussian)

    assert pairing == RR(sqrt(pi / 2))
    assert gaussian.b(gaussian) == pairing
    assert space.q(gaussian) == pairing


def test_c_to_the_k_is_the_mapping_space() -> None:
    assert C**Infinity is C ^ Infinity
    assert (C**Infinity)(RR) is C(Infinity, RR)
    assert (C**2)(RR, RR) is C(2, RR)
    assert (C**Infinity)(RR) is (C**Infinity)(RR, RR)


def test_research_dialect_accepts_c_to_the_k_of_spaces() -> None:
    from sageparse.preparser import preparse

    namespace = {"C": C, "RR": RR, "Infinity": Infinity, "Integer": Integer}
    exec(preparse("space = C^Infinity(RR)\n"), namespace)
    assert namespace["space"] is C(Infinity, RR)
    exec(preparse("same = C^2(RR, RR)\n"), namespace)
    assert namespace["same"] is C(2, RR)


def test_research_dialect_accepts_ell_to_the_p_of_reals() -> None:
    from sageparse.preparser import preparse

    namespace = {"ell": ell, "RR": RR, "Infinity": Infinity, "Integer": Integer}
    exec(preparse("space = ell^2(RR)\n"), namespace)
    assert namespace["space"] is ell(2, RR)
    exec(preparse("unbounded = ell^Infinity(RR)\n"), namespace)
    assert namespace["unbounded"] is ell(Infinity)


def test_sequence_space_places_formulas_and_callables() -> None:
    space = ell(2)
    n = space.indeterminate()
    geometric = space(2 ** (-n))

    def decaying(index):
        return QQ(1) / (index + 1)

    assert space is ell(2, RR)
    assert space in VectorSpaces(RR)
    assert space in SymmetricBilinearFormModules(RR)
    assert space in FormedModules(RR)
    assert space in PairedModules(RR)
    assert ell(1) not in FormModules(RR)
    assert ell(1) not in FormedModules(RR)
    assert space.integrability_exponent() == 2
    assert space.domain() is NN
    assert geometric(0) == 1
    assert geometric(3) == QQ(1) / 8
    assert space(decaying)(3) == QQ(1) / 4
    assert ell(Infinity).integrability_exponent() is Infinity


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
    assert holder not in FormedModules(RR)
    assert holder.pairing(decaying, bounded) == RR(2)
    try:
        ell(3) * ell(3)
    except TypeError as error:
        assert "1/p + 1/q = 1" in str(error)
        return
    raise AssertionError("ell^3 ⊗ ell^3 is not a Hölder pairing")


def test_smooth_maps_are_set_morphisms() -> None:
    exponential = C(Infinity, RR)(exp)
    morphism = exponential.as_set_morphism()

    assert morphism.domain() is RR
    assert morphism.codomain() is RR
    assert morphism(RR(0)) == 1
    assert exponential(RR.pi()) == RR(exp(pi))


def test_a_formal_power_series_is_its_coefficient_sequence_in_ell_p() -> None:
    maps = C(Infinity, RR)
    polynomials = PolynomialRing(QQ, "t")
    t = polynomials.algebra_generator("t")
    series_ring = PowerSeriesRing(QQ, "u")
    u = series_ring.algebra_generator("u")
    laurent_ring = LaurentPolynomialRing(QQ, "w")
    w = laurent_ring.algebra_generator("w")
    quadratic = ell(2)(t**2 + 1)
    truncated = ell(2)(1 + u + u**2)

    assert maps(t**2 + 1)(2) == 5
    assert quadratic(0) == 1
    assert quadratic(1) == 0
    assert quadratic(2) == 1
    assert quadratic(3) == 0
    assert truncated(0) == 1
    assert truncated(1) == 1
    assert truncated(2) == 1
    assert truncated(3) == 0
    assert ell(2).b(truncated, truncated) == 3
    assert ell(2).b(quadratic, truncated) == 2
    recovered = truncated.generating_series()
    assert recovered[0] == 1
    assert recovered[1] == 1
    assert recovered[2] == 1
    assert recovered[3] == 0
    geometric = ell(2)(2 ** (-ell(2).indeterminate()))
    assert ell(2).b(truncated, geometric) == RR(QQ(7) / 4)
    try:
        ell(2)(w + w**-1)
    except TypeError as error:
        assert "two-sided" in str(error)
        return
    raise AssertionError("a Laurent polynomial with negative degree is not a sequence on NN")


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
