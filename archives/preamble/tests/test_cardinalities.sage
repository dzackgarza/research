r"""Mathematical tests for ordinals, cardinals, and the cardinality functor."""

import dzack_research.preamble.categories.abstract_categories.cat

from sage.all import (
    CC,
    GF,
    MatrixSpace,
    PolynomialRing,
    PowerSeriesRing,
    QQ,
    QQbar,
    QuadraticField,
    Qp,
    RR,
    Primes,
    ZZ,
)
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism

# Sage's namespace first, and the preamble's over it: these tests name
# ``AbelianGroup``, ``FreeGroup``, ``RR`` and their fellows, which the
# preamble does not export and a lowered module is not given.
from sage.all import *  # noqa: F401,F403

from dzack_research.preamble.categories.abstract_categories.products import (
    CartesianProductOfSets,
    CoproductOfSets,
)
from dzack_research.preamble.categories.functors.cardinality import (
    cardinality_functor,
)
from dzack_research.preamble.categories.rings.rings import own_ring
from dzack_research.preamble.categories.sets.cardinals import (
    CardinalComparison,
    Cardinalities,
    aleph,
    aleph0,
    cardinal,
    continuum,
)
from dzack_research.preamble.categories.sets.ordinals import Ordinals, omega
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.sets import ImageSet, PowerSet, Set


def test_initial_ordinals_have_the_corresponding_aleph_cardinals() -> None:
    r"""The cardinal of ω_α is ℵ_α, also for transfinite α."""
    assert omega(0).cardinality() == aleph(0)
    assert omega(3).cardinality() == aleph(3)
    assert omega(omega(1)).cardinality() == aleph(omega(1))
    assert aleph(omega(1)).initial_ordinal() == omega(omega(1))


def test_natural_ordinal_operations_form_the_owned_semiring() -> None:
    r"""Natural sum and product are commutative and distributive."""
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


def test_cardinal_arithmetic_satisfies_semiring_laws_and_order_bounds() -> None:
    r"""Finite, countable, and uncountable cardinals obey the same laws."""
    finite = cardinal(3)
    specimens = (
        (finite, cardinal(5)),
        (aleph0, continuum),
        (continuum, aleph(2)),
    )

    assert finite + cardinal(5) == cardinal(8)
    assert finite * cardinal(5) == cardinal(15)
    assert finite ** cardinal(5) == cardinal(243)
    assert aleph0 + continuum == continuum
    assert aleph0 * continuum == continuum
    assert aleph0 ** aleph0 == continuum

    for left, right in specimens:
        assert left + right == right + left
        assert left * right == right * left
        assert left * (right + continuum) == left * right + left * continuum
        assert left <= left + right
        assert left <= left * right
        assert left <= left ** right


def test_cardinal_homsets_are_the_provable_cardinal_order() -> None:
    r"""A hom-set is singleton exactly when its inequality is provable."""
    cardinalities = Cardinalities()

    assert aleph(1) != continuum
    assert cardinalities.compare(aleph(1), continuum) is (
        CardinalComparison.LESS_OR_EQUAL
    )
    assert cardinalities.hom(aleph(1), continuum).cardinality() == 1
    assert cardinalities.hom(continuum, aleph(1)).cardinality() == 0

    assert cardinalities.compare(aleph(2), continuum) is (
        CardinalComparison.INCOMPARABLE
    )
    assert cardinalities.hom(aleph(2), continuum).cardinality() == 0
    assert cardinalities.hom(continuum, aleph(2)).cardinality() == 0

    assert cardinalities.hom(aleph0, continuum).cardinality() == 1
    assert cardinalities.hom(continuum, aleph0).cardinality() == 0


def test_cardinality_functor_preserves_set_coproducts_and_products() -> None:
    r"""Cardinality sends disjoint unions to sums and products to products."""
    left = Set([1, 2])
    right = Set([3, 4, 5])
    coproduct = CoproductOfSets((left, right))
    product = CartesianProductOfSets((left, right))
    cardinality = cardinality_functor()

    assert cardinality(coproduct) == cardinality(left) + cardinality(right) == 5
    assert cardinality(product) == cardinality(left) * cardinality(right) == 6

    coproduct_comparison = cardinality.coproduct_comparison(coproduct)
    assert coproduct_comparison.domain() == coproduct_comparison.codomain() == 5

    product_comparison = cardinality.cartesian_product_comparison(product)
    assert product_comparison.domain() == product_comparison.codomain() == 6


def test_power_set_of_naturals_and_real_line_have_the_continuum() -> None:
    r"""Power sets construct over countable and continuum-sized sets."""
    naturals = Sets.Δ[aleph0]
    doubling = SetMorphism(Hom(naturals, naturals, Sets()), lambda n: 2 * n)
    even_naturals = ImageSet(doubling, naturals, is_injective=True)
    subsets_of_naturals = PowerSet(naturals)
    subsets_of_even_naturals = PowerSet(even_naturals)
    subsets_of_primes = PowerSet(Primes())
    real_line = own_ring(RR)
    subsets_of_reals = PowerSet(real_line)
    cardinality = cardinality_functor()

    assert cardinality(naturals) == aleph0
    assert cardinality(subsets_of_naturals) == cardinal(2) ** aleph0 == continuum
    assert cardinality(subsets_of_even_naturals) == continuum
    assert cardinality(subsets_of_primes) == continuum
    assert cardinality(subsets_of_naturals) == cardinality(real_line)
    assert cardinality(subsets_of_reals) == cardinal(2) ** continuum
    assert cardinality(PowerSet(subsets_of_naturals)) == cardinal(2) ** continuum

    comparison = cardinality.power_set_comparison(subsets_of_naturals)
    assert comparison.domain() == comparison.codomain() == continuum


def test_standard_mathematical_objects_have_their_exact_cardinals() -> None:
    r"""Standard finite, countable, and continuum objects retain their sizes."""
    finite_objects = (
        (Set([]), cardinal(0)),
        (Sets.Δ[4], cardinal(5)),
        (own_ring(GF(7)), cardinal(7)),
    )
    countable_objects = (
        own_ring(ZZ),
        own_ring(QQ),
        own_ring(QQbar),
        own_ring(PolynomialRing(QQ, "x")),
        own_ring(QuadraticField(2, "a")),
        own_ring(MatrixSpace(QQ, 2)),
    )
    continuum_objects = (
        own_ring(RR),
        own_ring(CC),
        own_ring(Qp(5)),
        own_ring(PowerSeriesRing(QQ, "t")),
        own_ring(MatrixSpace(RR, 2)),
        PowerSet(Sets.Δ[aleph0]),
    )

    for mathematical_object, expected in finite_objects:
        assert mathematical_object.cardinality() == expected
    for mathematical_object in countable_objects:
        assert mathematical_object.cardinality() == aleph0
    for mathematical_object in continuum_objects:
        assert mathematical_object.cardinality() == continuum

    countable_product = CartesianProductOfSets(
        (own_ring(ZZ), own_ring(PolynomialRing(QQ, "y")))
    )
    continuum_product = CartesianProductOfSets((own_ring(ZZ), own_ring(RR)))
    continuum_coproduct = CoproductOfSets((own_ring(QQbar), own_ring(CC)))

    assert countable_product.cardinality() == aleph0
    assert continuum_product.cardinality() == continuum
    assert continuum_coproduct.cardinality() == continuum
