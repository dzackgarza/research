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


def test_divided_powers_of_linear_combinations_satisfy_the_pd_laws() -> None:
    r"""\(\gamma_3(x+y)=\sum_{i+j=3}\gamma_i(x)\gamma_j(y)\)."""
    _ensure_preamble()
    algebra = DividedPowerAlgebraOn(ZZ, Sets.Δ[1])
    x, y = _generators(algebra)

    assert algebra.divided_power(x + y, 3) == (
        algebra.divided_power(0, 3)
        + algebra.divided_power(0, 2) * y
        + x * algebra.divided_power(1, 2)
        + algebra.divided_power(1, 3)
    )
    assert algebra.divided_power(2 * x, 3) == 8 * algebra.divided_power(0, 3)


def test_the_divided_power_ideal_contains_all_divided_relations() -> None:
    r"""For \(M=\mathbb Z/2\), \(\Gamma^3M=\mathbb Z/2\) and \(\Gamma^4M=\mathbb Z/8\)."""
    _ensure_preamble()
    algebra = DividedPowerAlgebraOn(ZZ, Sets.Δ[0])
    x = next(iter(_generators(algebra)))

    for degree, expected_order in ((3, 2), (4, 8)):
        monomial = algebra.monomial_system().monomials_of_degree(degree)[0]
        relations = algebra.ideal_generators_in_degree((2 * x,), degree)
        coefficients = [
            relation.coefficient(monomial)
            for relation in relations
            if relation != algebra.zero()
        ]
        assert gcd(coefficients) == expected_order


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


def test_polynomial_algorithms_belong_only_to_the_symmetric_algebra() -> None:
    r"""Noncommutative, alternating, and divided products have different arithmetic."""
    _ensure_preamble()
    labels = Sets.Δ[0]
    symmetric = FreeAlgebraOn(ZZ, labels)
    sx = next(iter(_generators(symmetric)))
    assert (sx**2 - 1).leading_coefficient() == 1
    assert (sx**2 - 1).gcd(sx - 1) == sx - 1

    for algebra in (
        TensorAlgebraOn(ZZ, labels),
        AlternatingAlgebraOn(ZZ, labels),
        DividedPowerAlgebraOn(ZZ, labels),
    ):
        generator = next(iter(_generators(algebra)))
        with pytest.raises(AssertionError, match="symmetric algebra"):
            generator.leading_coefficient()
        with pytest.raises(AssertionError, match="symmetric algebra"):
            generator.gcd(generator)


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


def test_the_center_of_a_tensor_algebra_on_two_generators_is_the_scalars() -> None:
    r"""For rank at least two, \(Z(T(M))=R\)."""
    _ensure_preamble()
    tensor = TensorAlgebraOn(QQ, Sets.Δ[1])
    x, y = _generators(tensor)

    assert tensor.ring_center() is QQ
    assert tensor.center_embedding()(QQ(3)) == 3 * tensor.one()
    assert x * y - y * x != tensor.zero(), "a generator is not central"


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


def test_a_graded_piece_is_a_submodule_carrying_its_inclusion() -> None:
    r"""$A_n\subseteq A$, with the map that says so.

    $T(M)[2]$ is $M\otimes_RM$ and $\Gamma(M)[2]$ is $\Gamma^2M$, so this is
    where a bilinear form's domain and a quadratic form's domain come from.
    Neither is built separately, and neither is a bare module: the grading is
    a statement about maps into $A$, so the piece carries its inclusion.
    """
    _ensure_preamble()
    algebra = TensorAlgebraOn(QQ, Sets.Δ[1])
    piece = algebra.graded_piece(2)

    inclusion = piece.inclusion()
    assert inclusion.codomain() is algebra
    assert piece.rank() == 4, "four words of length two on two generators"

    x, y = _generators(algebra)
    assert x * y in piece, "a degree-two element lies in the degree-two piece"
    assert x not in piece, "and a degree-one element does not"


def test_tensor_and_divided_squares_respect_a_module_presentation() -> None:
    r"""$T^2(\mathbb Z/2)=\mathbb Z/2$ and $\Gamma^2(\mathbb Z/2)=\mathbb Z/4$.

    The first relation is $2(x\otimes x)=0$.  The divided-power relation is
    $\gamma_2(2x)=4\gamma_2(x)=0$.  Thus the two square constructions cannot
    use the same quotient presentation.
    """
    _ensure_preamble()
    module = FinitelyPresentedTorsionModules().from_relations(matrix(ZZ, [[2]]))

    assert TensorSquare(module).invariants() == (2,)
    assert DividedSquare(module).invariants() == (4,)


def test_the_divided_square_classifies_quadratic_maps() -> None:
    r"""Linear maps \(\Gamma^2M\to W\) and quadratic maps \(M\to W\) agree.

    The mixed divided monomial records polarization.  This specimen uses
    \(q(a,b)=2a^2+3ab+5b^2\).
    """
    _ensure_preamble()
    module = BasedFreeModule(ZZ, Sets.Δ[1])
    value_module = BasedFreeModule(ZZ, Sets.Δ[0])
    x, y = module.module_generators()
    value_generator = next(iter(value_module.module_generators()))

    quadratic = QuadraticMap(
        module,
        value_module,
        lambda element: (
            2 * element._coordinates_[0] ** 2
            + 3 * element._coordinates_[0] * element._coordinates_[1]
            + 5 * element._coordinates_[1] ** 2
        ) * value_generator,
    )
    classifier = classifying_morphism(quadratic)
    recovered = quadratic_map_from_morphism(classifier)
    reclassified = classifying_morphism(recovered)

    for element in (x, y, x + y, 2 * x - y):
        assert recovered(element) == quadratic(element)
    assert quadratic(x + y) - quadratic(x) - quadratic(y) == 3 * value_generator
    assert quadratic(2 * x) == 4 * quadratic(x)
    for generator in DividedSquare(module).module_generators():
        assert reclassified(generator) == classifier(generator)


def test_divided_squares_are_symmetric_tensor_invariants() -> None:
    r"""The inclusion and polarization compose as (2) and (1+\tau)."""
    _ensure_preamble()
    module = BasedFreeModule(ZZ, Sets.Δ[1])
    divided = DividedSquare(module)
    tensor = TensorSquare(module)
    inclusion = divided_square_invariant_inclusion(module)
    polarization = tensor_square_polarization(module)
    gamma_x, xy, gamma_y = tuple(divided.module_generators())
    xx, tensor_xy, tensor_yx, yy = tuple(tensor.module_generators())

    assert inclusion(gamma_x) == xx
    assert inclusion(xy) == tensor_xy + tensor_yx
    assert inclusion(gamma_y) == yy
    assert polarization(xx) == 2 * gamma_x
    assert polarization(tensor_xy) == xy
    assert polarization(tensor_yx) == xy
    assert polarization(yy) == 2 * gamma_y
    for generator in divided.module_generators():
        assert polarization(inclusion(generator)) == 2 * generator
    assert inclusion(polarization(tensor_xy)) == tensor_xy + tensor_yx


def test_the_free_constructions_are_related_by_the_canonical_maps() -> None:
    r"""The quotient relations vanish, and \(\operatorname{Sym}\cong\Gamma\) over \(\mathbb Q\)."""
    _ensure_preamble()
    labels = Sets.Δ[1]
    tensor = TensorAlgebraOn(QQ, labels)
    symmetric = FreeAlgebraOn(QQ, labels)
    alternating = AlternatingAlgebraOn(QQ, labels)
    divided = DividedPowerAlgebraOn(QQ, labels)
    tx, ty = _generators(tensor)

    to_symmetric = tensor_to_symmetric(tensor)
    to_alternating = tensor_to_alternating(tensor)
    assert to_symmetric(tx * ty - ty * tx) == symmetric.zero()
    assert to_alternating(tx * tx) == alternating.zero()
    assert to_alternating(tx * ty + ty * tx) == alternating.zero()

    to_divided = symmetric_to_divided(symmetric)
    to_symmetric_from_divided = divided_to_symmetric(divided)
    sx, sy = _generators(symmetric)
    dx, dy = _generators(divided)
    for element in (symmetric.one(), sx, sx**2, sx * sy, (sx + sy) ** 3):
        assert to_symmetric_from_divided(to_divided(element)) == element
    for element in (
        divided.one(),
        dx,
        divided.divided_power(0, 2),
        dx * dy,
        divided.divided_power(0, 3),
    ):
        assert to_divided(to_symmetric_from_divided(element)) == element


def test_symmetric_to_divided_is_not_an_isomorphism_over_the_integers() -> None:
    r"""Over \(\mathbb Z\), \(x^2\mapsto2\gamma_2(x)\), not \(\gamma_2(x)\)."""
    _ensure_preamble()
    symmetric = FreeAlgebraOn(ZZ, Sets.Δ[0])
    divided = DividedPowerAlgebraOn(ZZ, Sets.Δ[0])
    x = next(iter(_generators(symmetric)))
    morphism = symmetric_to_divided(symmetric)

    assert morphism(x**2) == 2 * divided.divided_power(0, 2)
    assert morphism(x**2) != divided.divided_power(0, 2)


def test_tensor_and_symmetric_freeness_are_homset_bijections() -> None:
    r"""Extension and restriction are inverse on algebra and module maps."""
    _ensure_preamble()
    module = BasedFreeModule(QQ, Sets.Δ[1])
    tensor = TensorAlgebraOn(QQ, Sets.Δ[1])
    symmetric = FreeAlgebraOn(QQ, Sets.Δ[1])
    mx, my = module.module_generators()
    tx, ty = _generators(tensor)
    sx, sy = _generators(symmetric)

    tensor_linear = module_homset(module, tensor)({0: tx + ty, 1: tx})
    tensor_map = tensor_extension(tensor_linear)
    tensor_restriction = restrict_free_algebra_morphism(module, tensor_map)
    assert tensor_restriction(mx) == tensor_linear(mx)
    assert tensor_restriction(my) == tensor_linear(my)
    assert tensor_map(tx * ty) == (tx + ty) * tx

    symmetric_linear = module_homset(module, symmetric)({0: sx + sy, 1: sx})
    symmetric_map = symmetric_extension(symmetric_linear)
    symmetric_restriction = restrict_free_algebra_morphism(module, symmetric_map)
    assert symmetric_restriction(mx) == symmetric_linear(mx)
    assert symmetric_restriction(my) == symmetric_linear(my)
    assert symmetric_map(sx * sy) == (sx + sy) * sx


def test_exterior_and_divided_power_functoriality_preserve_their_operations() -> None:
    r"""\(\Lambda(f)\) preserves wedges and \(\Gamma(f)\) preserves divided powers."""
    _ensure_preamble()
    module = BasedFreeModule(ZZ, Sets.Δ[1])
    x, y = module.module_generators()
    exterior = AlternatingAlgebraOn(ZZ, Sets.Δ[1])
    ex, ey = _generators(exterior)
    exterior_linear = module_homset(module, exterior)({0: ex + ey, 1: ey})
    exterior_map = alternating_extension(exterior_linear)
    assert exterior_map(ex * ey) == ex * ey

    target_module = BasedFreeModule(ZZ, Sets.Δ[1])
    u, v = target_module.module_generators()
    linear = module_homset(module, target_module)({0: u + v, 1: v})
    divided_map = divided_power_induced_morphism(linear)
    source_divided = DividedPowerAlgebraOn(ZZ, Sets.Δ[1])
    target_divided = DividedPowerAlgebraOn(ZZ, Sets.Δ[1])
    assert divided_map(source_divided.divided_power(0, 2)) == (
        target_divided.divided_power(0, 2)
        + target_divided.algebra_generator(0) * target_divided.algebra_generator(1)
        + target_divided.divided_power(1, 2)
    )


def test_the_divided_power_adjunction_is_extension_and_restriction() -> None:
    r"""Maps \(\Gamma(M)\to A\) preserve every \(\gamma_n\) by construction."""
    _ensure_preamble()
    module = BasedFreeModule(ZZ, Sets.Δ[1])
    target = DividedPowerAlgebraOn(ZZ, Sets.Δ[1])
    x, y = module.module_generators()
    u, v = _generators(target)
    linear = module_homset(module, target)({0: u + v, 1: v})
    extension = divided_power_extension(linear)
    restriction = restrict_free_algebra_morphism(module, extension)
    source = extension.domain()

    assert restriction(x) == linear(x)
    assert restriction(y) == linear(y)
    assert extension(source.divided_power(0, 2)) == target.divided_power(u + v, 2)
    assert extension.preserves_divided_power(source.algebra_generator(0) + source.algebra_generator(1), 3)


def test_the_grading_decomposes_every_element() -> None:
    r"""$a=\sum_na_n$ with $a_n\in A_n$, which is what $\bigoplus$ asserts.

    A decomposition and not a filtration: the parts add back to the element,
    and each part is homogeneous.
    """
    _ensure_preamble()
    labels = Sets.Δ[1]

    for algebra in (
        FreeAlgebraOn(QQ, labels),
        TensorAlgebraOn(QQ, labels),
        AlternatingAlgebraOn(QQ, labels),
        DividedPowerAlgebraOn(QQ, labels),
    ):
        x, y = _generators(algebra)
        element = algebra.one() + x + x * y

        components = element.homogeneous_components()
        assert set(components) == {0, 1, 2}
        assert sum(components.values(), algebra.zero()) == element
        assert all(part.is_homogeneous() for part in components.values())
        assert components[2].degree() == 2
