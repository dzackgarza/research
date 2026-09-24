r"""Cartesian products and disjoint unions of finite and countable sets.

$|X \times Y| = |X| |Y|$ and $|X \sqcup Y| = |X| + |Y|$, so
$\{0, 1\} \times \{0, 1, 2\}$ has $6$ points and $\{0, 1\} \sqcup \{0, 1, 2\}$
has $5$; $\mathbb{N} \times \mathbb{N}$ and $\mathbb{N} \sqcup \{0, 1\}$ are
countably infinite.  An enumeration of $\mathbb{N} \times \mathbb{N}$ by
diagonals lists each pair once, so the rank of the $k$-th listed pair is
$k$.  The product functor sends $(\sigma, \mathrm{id})$ to
$(a, b) \mapsto (\sigma a, b)$.  These are the definitions of cardinal
arithmetic and of the product functor.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_the_product_of_two_and_three_points_has_six_points() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    product = Sets().product((two, three))
    corner = product((two(1), three(2)))

    assert product.cardinality() == cardinal(6)
    assert sum(1 for _point in product) == 6
    assert corner == product((two(1), three(2)))
    assert corner != product((two(0), three(2)))


def test_the_disjoint_union_of_two_and_three_points_has_five_points() -> None:
    union = Sets().coproduct((Sets.Δ[1], Sets.Δ[2]))

    assert union.cardinality() == cardinal(5)
    assert sum(1 for _point in union) == 5


def test_the_square_of_the_natural_numbers_is_countable_and_listed_by_diagonals() -> None:
    square = Sets().product((NN, NN))
    listing = iter(square)
    first_six = [next(listing) for _step in range(6)]

    assert square.cardinality() == aleph0
    assert first_six[0] == square((NN(0), NN(0)))
    assert all(
        square((NN(a), NN(b))) in first_six for a in range(3) for b in range(3) if a + b <= 2
    )


def test_the_diagonal_enumeration_of_the_square_of_the_naturals_is_ranked() -> None:
    square = Sets().product((NN, NN))
    ranking = square.ranking_map()
    listing = iter(square)

    assert [ranking(next(listing)) for _step in range(6)] == [0, 1, 2, 3, 4, 5]


def test_the_natural_numbers_plus_two_points_are_countable_and_enumerated() -> None:
    union = Sets().coproduct((NN, Sets.Δ[1]))
    listing = iter(union)
    first_five = [next(listing) for _step in range(5)]

    assert union.cardinality() == aleph0
    assert all(first_five[i] != first_five[j] for i in range(5) for j in range(i))


def test_the_product_functor_applies_a_transposition_to_the_first_coordinate() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    pairs = Cat().product([Sets(), Sets()])
    transposition = Sets().Mor(two, two)(lambda x: two(1) if x == 0 else two(0))
    identity = Sets().Mor(three, three).identity()
    induced = Sets().product_functor()(pairs.Mor(pairs(two, three), pairs(two, three))((transposition, identity)))
    product = induced.domain()

    assert induced(product((two(1), three(2)))) == product((two(0), three(2)))
    assert induced(product((two(0), three(0)))) == product((two(1), three(0)))
