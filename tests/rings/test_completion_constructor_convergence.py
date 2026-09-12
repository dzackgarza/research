r"""Every public adic-completion route uses the category-owned constructor."""

from dzack_research.preamble.all import AdicCompletion, AdicCompletions, PolynomialRing, QQ


def test_adic_completion_routes_share_one_owned_parent_and_maps() -> None:
    ring = PolynomialRing(QQ, ("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    ideal = ring.ideal(x, y)
    category = AdicCompletions()

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
