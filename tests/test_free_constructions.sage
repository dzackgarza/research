r"""The four free constructions on a module, and what tells them apart.

$T$, $\operatorname{Sym}$, $\Lambda$ and $\Gamma$ are one construction --
$F_R(\text{monomials})$ with a bilinear product -- differing only in what a
monomial is and what two of them multiply to.  So the facts worth asserting
are the ones that would collapse if the difference were lost: the ranks of the
graded pieces, and the products that a wrong monomial system would get right
anyway.

$\Gamma$ is the one that is not a quotient of $T$.  Over $\ZZ$ it is not
$\operatorname{Sym}$ either, and $\Gamma^2$ is what represents quadratic
forms, so the failure of $x^2$ to reach $\gamma_2(x)$ is the fact that matters
most here.
"""


import pytest


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


def _generators(algebra):
    return [
        algebra.algebra_generator(label)
        for label in algebra.algebra_generating_set()
    ]


def test_the_graded_pieces_have_the_ranks_the_constructions_say() -> None:
    r"""On two generators: $T[2]=4$, $\operatorname{Sym}[2]=3$, $\Lambda[2]=1$.

    $\dim T^n=r^n$, $\dim\operatorname{Sym}^n=\binom{r+n-1}{n}$ and
    $\dim\Lambda^n=\binom{r}{n}$.  These are the numbers that separate the
    three, and a construction framed by the wrong monomials gets them wrong.
    """
    _ensure_preamble()
    labels = Sets.Δ[1]

    assert len(TensorAlgebraOn(QQ, labels).graded_piece_monomials(2)) == 4
    assert len(FreeAlgebraOn(QQ, labels).graded_piece_monomials(2)) == 3
    assert len(AlternatingAlgebraOn(QQ, labels).graded_piece_monomials(2)) == 1
    assert len(AlternatingAlgebraOn(QQ, labels).graded_piece_monomials(3)) == 0, (
        "there is no third exterior power of a rank-two module"
    )


def test_the_alternating_algebra_is_free_of_rank_two_to_the_n() -> None:
    r"""$\Lambda(F_R(S))$ is framed by the subsets of $S$.

    Which is what makes it finite-rank at all: a framing by the squarefree
    monomials sitting inside all monomials would be a submodule of an
    infinite-rank one, not this.
    """
    _ensure_preamble()

    for rank in (1, 2, 3):
        algebra = AlternatingAlgebraOn(QQ, Sets.Δ[rank - 1])
        assert algebra.number_of_module_generators() == 2**rank


def test_wedging_a_generator_with_itself_is_zero() -> None:
    r"""$x\wedge x=0$, and $x\wedge y=-y\wedge x$ follows from it."""
    _ensure_preamble()
    algebra = AlternatingAlgebraOn(QQ, Sets.Δ[1])
    x, y = _generators(algebra)

    assert x * x == algebra.zero()
    assert y * y == algebra.zero()
    assert x * y == -(y * x), "anticommuting, which is what the sign is"
    assert x * y != algebra.zero(), "and not by everything being zero"


def test_the_wedge_sign_is_the_shuffle_parity() -> None:
    r"""$(x\wedge y)\wedge z=x\wedge(y\wedge z)$, with the signs it takes.

    Moving a generator past two others costs two transpositions, so $z\wedge
    x\wedge y=x\wedge y\wedge z$ while $y\wedge x\wedge z$ costs one.
    """
    _ensure_preamble()
    algebra = AlternatingAlgebraOn(QQ, Sets.Δ[2])
    x, y, z = _generators(algebra)

    assert (x * y) * z == x * (y * z), "associative"
    assert z * x * y == x * y * z, "two transpositions"
    assert y * x * z == -(x * y * z), "one transposition"
    assert x * y * z != algebra.zero()


def test_the_symmetric_algebra_does_commute_and_the_tensor_algebra_does_not() -> None:
    r"""The relation each is the quotient of $T$ by, seen on generators."""
    _ensure_preamble()
    labels = Sets.Δ[1]

    symmetric = FreeAlgebraOn(QQ, labels)
    x, y = _generators(symmetric)
    assert x * y == y * x

    tensor = TensorAlgebraOn(QQ, labels)
    x, y = _generators(tensor)
    assert x * y != y * x


def test_a_divided_power_is_not_a_power() -> None:
    r"""$x^2=2\gamma_2(x)$, so over $\ZZ$ the powers do not span $\Gamma$.

    This is the whole difference from $\operatorname{Sym}$, and the reason
    $\Gamma^2$ rather than $\operatorname{Sym}^2$ classifies quadratic forms:
    over $\ZZ$ the two are not isomorphic.
    """
    _ensure_preamble()
    algebra = DividedPowerAlgebraOn(ZZ, Sets.Δ[0])
    (x,) = _generators(algebra)

    assert x * x == 2 * algebra.divided_power(0, 2)
    assert x * x != algebra.divided_power(0, 2)


def test_divided_powers_multiply_by_binomial_coefficients() -> None:
    r"""$\gamma_a(x)\gamma_b(x)=\binom{a+b}{a}\gamma_{a+b}(x)$."""
    _ensure_preamble()
    from sage.arith.misc import binomial

    algebra = DividedPowerAlgebraOn(ZZ, Sets.Δ[0])

    for a in (1, 2, 3):
        for b in (1, 2, 3):
            assert algebra.divided_power(0, a) * algebra.divided_power(0, b) == (
                binomial(a + b, a) * algebra.divided_power(0, a + b)
            )


def test_the_divided_and_symmetric_algebras_share_their_monomials() -> None:
    r"""$\Gamma$ is not a quotient of $T$: it has the same basis as $\operatorname{Sym}$.

    Same graded ranks, different products.  So the two are told apart by
    multiplying, never by counting -- which is why the product had to become
    part of what a construction states.
    """
    _ensure_preamble()
    labels = Sets.Δ[1]
    divided = DividedPowerAlgebraOn(ZZ, labels)
    symmetric = FreeAlgebraOn(ZZ, labels)

    for degree in (0, 1, 2, 3):
        assert len(divided.graded_piece_monomials(degree)) == len(
            symmetric.graded_piece_monomials(degree)
        )

    divided_x = _generators(divided)[0]
    symmetric_x = _generators(symmetric)[0]
    monomial = divided.monomial_system().generator(0) ** 2

    assert (symmetric_x * symmetric_x).coefficient(monomial) == 1
    assert (divided_x * divided_x).coefficient(monomial) == 2, (
        "the same monomial, a different coefficient"
    )


def test_the_grading_is_read_off_whichever_monomials_are_used() -> None:
    r"""Degree is the number of letters, however a construction spells them."""
    _ensure_preamble()
    labels = Sets.Δ[1]

    for algebra in (
        FreeAlgebraOn(QQ, labels),
        TensorAlgebraOn(QQ, labels),
        AlternatingAlgebraOn(QQ, labels),
        DividedPowerAlgebraOn(QQ, labels),
    ):
        x, y = _generators(algebra)

        assert x.degree() == 1
        assert (x * y).degree() == 2, f"{algebra} grades its product"
        assert algebra.one().degree() == 0
        assert (x + x * y).is_homogeneous() is False


def test_each_construction_lands_in_its_own_category() -> None:
    r"""The flavour is carried by the object, not inferred from its class."""
    _ensure_preamble()
    from dzack_research.preamble.categories.algebras.free_algebras import (
        AlternatingAlgebras,
        DividedPowerAlgebras,
        SymmetricAlgebras,
        TensorAlgebras,
    )

    labels = Sets.Δ[1]
    for algebra, category in (
        (FreeAlgebraOn(QQ, labels), SymmetricAlgebras(QQ)),
        (TensorAlgebraOn(QQ, labels), TensorAlgebras(QQ)),
        (AlternatingAlgebraOn(QQ, labels), AlternatingAlgebras(QQ)),
        (DividedPowerAlgebraOn(QQ, labels), DividedPowerAlgebras(QQ)),
    ):
        assert algebra in category, f"{algebra} is not in {category}"


def test_the_scalars_enter_every_construction_as_multiples_of_the_unit() -> None:
    r"""$R\to Z(A)$, $r\mapsto r\cdot 1$, is what makes each an $R$-algebra."""
    _ensure_preamble()
    labels = Sets.Δ[1]

    for algebra in (
        FreeAlgebraOn(QQ, labels),
        TensorAlgebraOn(QQ, labels),
        AlternatingAlgebraOn(QQ, labels),
        DividedPowerAlgebraOn(QQ, labels),
    ):
        structure = algebra._ring_morphism_defining_algebra_structure()
        assert structure(QQ(3)) == 3 * algebra.one()

        x = _generators(algebra)[0]
        assert structure(QQ(3)) * x == 3 * x, "central, so it commutes with x"


def test_the_monomials_of_the_alternating_algebra_are_the_subsets() -> None:
    r"""A module generator of $\Lambda$ is named by a subset of $S$.

    Which is why the ranks are binomial coefficients: the degree-$k$
    monomials are the $k$-element subsets, and each is the wedge of its
    members in the generating set's order.
    """
    _ensure_preamble()
    algebra = AlternatingAlgebraOn(QQ, Sets.Δ[2])
    system = algebra.monomial_system()
    x, y, z = _generators(algebra)

    assert algebra.module_generator(system.generator(0) | system.generator(2)) == x * z
    assert set(system.monomials_of_degree(2)) == {
        system.generator(0) | system.generator(1),
        system.generator(0) | system.generator(2),
        system.generator(1) | system.generator(2),
    }


def test_the_alternating_algebra_of_a_countable_module_is_countable() -> None:
    r"""$\Lambda(F_R(S))$ is free on the *finite* subsets of $S$.

    A wedge is a product of finitely many generators whatever $S$ is, so an
    infinite generating set gives an algebra of countable rank rather than
    one that fails to exist.  $\Lambda^k$ is free of rank
    $\binom{|S|}{k}$ at every $k$, and the relations among the generators are
    the same ones a finite $S$ has.
    """
    _ensure_preamble()
    countable = Sets.Δ[Sets.ℵ[0]]

    assert countable not in Sets().Finite()
    algebra = AlternatingAlgebraOn(QQ, countable)

    assert algebra.module_generating_set() not in Sets().Finite()

    x, y = (algebra.algebra_generator(label) for label in (0, 1))
    assert x * x == algebra.zero()
    assert x * y == -(y * x)
    assert (x * y).degree() == 2


@pytest.mark.xfail(
    strict=True,
    reason="the preamble does not own Subsets; see issue #348",
)
def test_the_subsets_of_a_countable_set_are_uncountable() -> None:
    r"""$|\mathcal{P}(S)|=2^{\aleph_0}$ when $S$ is countably infinite.

    So $\mathcal{P}(S)$ is neither finite nor enumerable, and the finite
    subsets -- the ones $\Lambda$ is framed by -- are the countable part of
    it.  Sage's ``Subsets`` of an infinite set says it is a *finite*
    enumerated set, which is why the alternating algebra assembles its
    framing from the sizes instead of asking for it.
    """
    _ensure_preamble()
    from sage.combinat.subset import Subsets

    countable = Sets.Δ[Sets.ℵ[0]]
    subsets = Subsets(countable)

    assert subsets not in Sets().Finite(), (
        "there are uncountably many subsets of a countable set"
    )
