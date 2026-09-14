r"""Every public adic-completion route uses the category-owned constructor."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    AdicCompletion,
    AdicCompletions,
    Cat,
    FormalPowerSeriesRings,
    PolynomialRing,
    PowerSeriesRing,
    Zp,
)


def test_adic_completion_routes_share_one_owned_parent_and_maps() -> None:
    ring = PolynomialRing(QQ, ("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    ideal = ring.ideal(x, y)
    category = AdicCompletions()
    assert category in Cat()
    assert category.category() is Cat()

    declared = category(ring, ideal, precision=7)
    notation = AdicCompletion(ring, ideal, precision=7)
    method = ring.adic_completion(ideal, precision=7)

    assert declared is notation
    assert declared is method
    assert declared in category
    assert declared.completion_source() is ring
    assert declared.ideal_of_definition() == ideal
    assert declared.completion_map().domain() is ring
    assert declared.completion_map().codomain() is declared


def test_completion_precision_is_part_of_the_computational_constructor_key() -> None:
    ring = PolynomialRing(QQ, "t")
    t = ring.algebra_generator("t")
    ideal = ring.ideal(t)

    fifth = ring.adic_completion(ideal, precision=5)
    fifth_again = AdicCompletions()(ring, ideal, precision=5)
    eighth = ring.adic_completion(ideal, precision=8)

    assert fifth is fifth_again
    assert fifth is not eighth
    assert fifth.completion_source() is eighth.completion_source()
    assert fifth.ideal_of_definition() == eighth.ideal_of_definition()


def test_power_series_notation_is_the_same_selected_completion() -> None:
    polynomial = PolynomialRing(QQ, "t")
    t = polynomial.algebra_generator("t")
    defining = polynomial.ideal(t)

    completion = polynomial.adic_completion(defining)
    notation = PowerSeriesRing(QQ, "t")
    declared = FormalPowerSeriesRings(QQ)("t")

    assert completion is notation
    assert completion is declared
    assert completion in FormalPowerSeriesRings(QQ)
    assert completion.base_ring() is QQ
    assert completion.completion_source() is polynomial
    assert completion.completion_map().domain() is polynomial
    assert completion.completion_map().codomain() is completion


def test_power_series_over_integers_does_not_require_a_maximal_ideal_decision() -> None:
    series = PowerSeriesRing(ZZ, "q")

    assert series in FormalPowerSeriesRings(ZZ)
    assert series.base_ring() is ZZ
    assert series.completion_source().base_ring() is ZZ
    assert series.formal_parameter_set().cardinality() == 1


def test_p_adic_notation_is_the_same_selected_adic_completion() -> None:
    ideal = ZZ.ideal(ZZ(5))

    completion = ZZ.adic_completion(ideal, precision=12)
    notation = Zp(5, prec=12)
    declared = AdicCompletions()(ZZ, ideal, precision=12)

    assert completion is notation
    assert completion is declared
    assert completion.completion_source() is ZZ
    assert completion.ideal_of_definition() == ideal
    assert completion.completion_map().domain() is ZZ
    assert completion.completion_map().codomain() is completion
