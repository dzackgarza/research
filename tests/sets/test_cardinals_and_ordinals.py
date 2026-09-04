from dzack_research.preamble.all import (
    CardinalComparison,
    Cardinalities,
    Ordinals,
    aleph,
    aleph0,
    cardinal,
    continuum,
    omega,
)


def test_initial_ordinals_have_the_corresponding_aleph_cardinals() -> None:
    assert omega(0).cardinality() == aleph(0)
    assert omega(3).cardinality() == aleph(3)
    assert omega(omega(1)).cardinality() == aleph(omega(1))
    assert aleph(omega(1)).initial_ordinal() == omega(omega(1))


def test_natural_ordinal_operations_form_the_commutative_semiring() -> None:
    alpha = omega(0)
    beta = omega(1)
    gamma = omega(2)
    assert alpha + beta == beta + alpha
    assert alpha * beta == beta * alpha
    assert (alpha + beta) + gamma == alpha + (beta + gamma)
    assert (alpha * beta) * gamma == alpha * (beta * gamma)
    assert (alpha + beta) * gamma == alpha * gamma + beta * gamma
    assert Ordinals()(2).ordinal_sum(3) == 5
    assert alpha.ordinal_sum(1) != Ordinals()(1).ordinal_sum(alpha)


def test_cardinal_arithmetic_and_order_do_not_assume_continuum_hypothesis() -> None:
    cardinals = Cardinalities()
    assert cardinal(3) + cardinal(5) == cardinal(8)
    assert cardinal(3) * cardinal(5) == cardinal(15)
    assert cardinal(3) ** cardinal(5) == cardinal(243)
    assert aleph0 + continuum == continuum
    assert aleph0 * continuum == continuum
    assert aleph0 ** aleph0 == continuum

    assert cardinals.compare(aleph(1), continuum) is CardinalComparison.LESS_OR_EQUAL
    assert cardinals.mor(aleph(1), continuum).cardinality() == 1
    assert cardinals.mor(continuum, aleph(1)).cardinality() == 0
    assert cardinals.compare(aleph(2), continuum) is CardinalComparison.INCOMPARABLE
    assert cardinals.mor(aleph(2), continuum).cardinality() == 0
    assert cardinals.mor(continuum, aleph(2)).cardinality() == 0
    assert cardinals.mor(aleph0, continuum).unique_morphism().domain() == aleph0


def test_cardinality_is_functorial_on_set_isomorphisms() -> None:
    from dzack_research.preamble.all import Core, Sets, ZZ, cardinality_functor

    source = Sets.Δ[2]
    target = __import__("dzack_research.preamble.categories.sets", fromlist=["finite_ordered_set"]).finite_ordered_set((ZZ(10), ZZ(20), ZZ(30)))
    forward = Sets().mor( dzack, esearc)(lambda value: target((ZZ(10), ZZ(20), ZZ(30))[source.position(value)]))
    backward = Sets().mor( dzack, esearc)(lambda value: source((ZZ(10), ZZ(20), ZZ(30)).index(value)))
    core = Core(Sets())
    isomorphism = core.mor(source, target)(forward, backward)
    cardinality = cardinality_functor()

    assert cardinality(source) == cardinal(3)
    assert cardinality(target) == cardinal(3)
    image = cardinality(isomorphism)
    assert image.domain() == cardinal(3)
    assert image.codomain() == cardinal(3)
