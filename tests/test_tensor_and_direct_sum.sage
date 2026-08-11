r"""Mathematical facts about ``+`` (direct sum) and ``@`` (tensor product).

These are facts about lattices, not about the implementation: each assertion is
one a mathematician could find wrong.

The specimens are deliberately **not** unimodular.  A determinant rule read on
unimodular lattices says $\pm 1=\pm 1$ and holds for a wrong formula too, so
$A_1$ ($\det=-2$) and $A_2$ ($\det=3$) carry the arithmetic and $U$ supplies an
indefinite factor.  The convention here is the algebro-geometric one: $A_n$ is
negative definite.
"""


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from pathlib import Path
    import dzack_research

    from dzack_research.preamble.install import install_preamble
    install_preamble(globals())
    Lattices.install(globals())


def _projection_onto(
    L: "Lattice", summand: "Subobject", offset: "Integer"
) -> "ModuleMorphism":
    r"""Return $\pi:L\to S$ reading off the summand's block of coordinates.

    A projection forgets the other summand, so it does not preserve the form:
    it is a morphism of the underlying modules and not of lattices, and it is
    built in the module homset for that reason.
    """
    block = summand
    module_generators = block.module_generators()
    return module_homset(L, block)(
        {
            label: (
                module_generators[index - offset]
                if 0 <= index - offset < module_generators.cardinality()
                else block.zero()
            )
            for index, label in enumerate(L.module_generating_set())
        }
    )


def test_sum_of_a_list_is_the_orthogonal_direct_sum() -> None:
    r"""``sum([...])`` works because ``+`` is the direct sum and ``0`` is the unit."""
    _ensure_preamble()
    summed = sum([Lattices.U, Lattices.U, Lattices.E8])

    assert summed.rank() == 2 + 2 + 8
    assert summed.signature_pair() == (1 + 1 + 0, 1 + 1 + 8)


def test_direct_sum_satisfies_the_biproduct_identity() -> None:
    r"""$\pi_j\circ\iota_i=\delta_{ij}$: the identity on $L_i$, zero off the diagonal.

    Both halves carry information.  A composite that is merely nonzero on the
    diagonal -- $2\cdot\mathrm{id}$, say -- is not a biproduct, and neither is
    one whose off-diagonal composites are nonzero.
    """
    _ensure_preamble()
    L = Lattices.A1 + Lattices.A2
    summands = L.summands()

    assert len(summands) == 2, "A_1 + A_2 splits along its block-diagonal Gram matrix"
    assert [summand.rank() for summand in summands] == [1, 2]

    inclusions = [summand.embedding() for summand in summands]
    projections = [
        _projection_onto(L, summands[0], 0),
        # An offset into a list of generators is a position, so the rank
        # crosses to an integer here: cardinals do not subtract.
        _projection_onto(L, summands[1], summands[0].rank().finite_value()),
    ]

    for i, inclusion in enumerate(inclusions):
        for j, projection in enumerate(projections):
            composite = inclusion.matrix() * projection.matrix()
            match i == j:
                case True:
                    assert composite.is_one(), (
                        f"pi_{j} . iota_{i} must be the identity of the summand"
                    )
                case False:
                    assert composite.is_zero(), f"pi_{j} . iota_{i} must be zero"


def test_direct_summands_are_orthogonal_and_keep_their_own_form() -> None:
    r"""$b(\iota_0x,\iota_1y)=0$, while $\iota_i$ is an isometry onto its image.

    The second half is what stops the first from being vacuous: a form that
    vanished identically would make everything orthogonal.
    """
    _ensure_preamble()
    L = Lattices.A1 + Lattices.A2
    first, second = L.summands()
    first_images = tuple(first.embedded_module_generators())
    second_images = tuple(second.embedded_module_generators())

    assert len(first_images) == 1 and len(second_images) == 2
    assert matrix(ZZ, L.gram_of(first_images)) == matrix(
        ZZ, Lattices.A1.gram_matrix()
    ), "the first summand keeps A_1's Gram matrix inside the sum"
    assert matrix(ZZ, L.gram_of(second_images)) == matrix(
        ZZ, Lattices.A2.gram_matrix()
    ), "the second summand keeps A_2's Gram matrix inside the sum"

    for x in first_images:
        for y in second_images:
            assert L.b(x, y) == 0, "distinct summands of a direct sum are orthogonal"


def test_direct_sum_determinant_is_the_product_of_the_summand_determinants() -> None:
    r"""$\det(L\oplus M)=\det L\cdot\det M$, on summands that are not unimodular."""
    _ensure_preamble()
    A1, A2 = Lattices.A1, Lattices.A2

    assert A1.gram_matrix().det() == -2 and A2.gram_matrix().det() == 3
    assert (A1 + A2).gram_matrix().det() == -6


def test_tensor_rank_is_the_product_of_the_ranks() -> None:
    r"""$\operatorname{rank}(L\otimes M)=\operatorname{rank}L\cdot\operatorname{rank}M$.

    Ranks 2 and 8, so the product (16) and the sum (10) are told apart.
    """
    _ensure_preamble()

    assert (Lattices.U @ Lattices.E8).rank() == 2 * 8


def test_tensor_gram_is_the_kronecker_product() -> None:
    r"""$b(x_1\otimes y_1,x_2\otimes y_2)=b_L(x_1,x_2)\,b_M(y_1,y_2)$."""
    _ensure_preamble()
    L, M = Lattices.U, Lattices.A2
    T = L @ M

    for x1 in L.module_generators():
        for y1 in M.module_generators():
            for x2 in L.module_generators():
                for y2 in M.module_generators():
                    assert T.b(T.pure_tensor(x1, y1), T.pure_tensor(x2, y2)) == (
                        L.b(x1, x2) * M.b(y1, y2)
                    )


def test_tensor_determinant_follows_the_kronecker_rule() -> None:
    r"""$\det(A\otimes B)=\det(A)^n\det(B)^m$ for $A$ $m\times m$ and $B$ $n\times n$."""
    _ensure_preamble()
    L, M = Lattices.A1, Lattices.A2
    T = L @ M

    assert abs(L.gram_matrix().det()) != 1 and abs(M.gram_matrix().det()) != 1, (
        "on unimodular factors the rule reads +-1 = +-1 and says nothing"
    )
    assert T.gram_matrix().det() == (
        L.gram_matrix().det() ** M.rank().finite_value()
        * M.gram_matrix().det() ** L.rank().finite_value()
    )
    assert T.gram_matrix().det() == 12, "(-2)^2 * 3^1, computed by hand"


def test_tensor_is_a_cocone_under_the_cartesian_product() -> None:
    r"""$M\otimes N$ sits under $M\times N$, not under $M$ or $N$.

    There is no canonical $M\to M\otimes N$: sending $m\mapsto m\otimes n$
    needs a choice of $n$.  What is canonical is the bilinear
    $\otimes:M\times N\to M\otimes N$, and that is the cocone's structure map.
    """
    _ensure_preamble()
    L, M = Lattices.U, Lattices.A2
    T = L @ M

    assert T.tensor_factors() == (L, M)
    assert T.cartesian_source().factors() == (L, M)

    tensor_map = T.universal_bilinear_map()
    assert tensor_map.codomain() is UnderlyingSet(T)
    for x in L.module_generators():
        for y in M.module_generators():
            assert tensor_map((x, y)) == T.pure_tensor(x, y)


def test_the_universal_map_is_bilinear_not_linear() -> None:
    r"""$\otimes$ is bilinear: linear in each slot, and not linear on $M\oplus N$.

    $(m_1+m_2)\otimes n=m_1\otimes n+m_2\otimes n$, while a linear map on the
    biproduct would instead send $(m_1,n)+(m_2,0)$ to a sum this does not
    equal -- which is why the cocone is taken in Set.
    """
    _ensure_preamble()
    L, M = Lattices.U, Lattices.A2
    T = L @ M
    m1, m2 = tuple(L.module_generators())[:2]
    n = tuple(M.module_generators())[0]

    assert T.pure_tensor(m1 + m2, n) == T.pure_tensor(m1, n) + T.pure_tensor(m2, n)
    assert T.pure_tensor(2 * m1, n) == 2 * T.pure_tensor(m1, n)
    assert T.pure_tensor(m1, 3 * n) == 3 * T.pure_tensor(m1, n)


def test_the_universal_property_factors_a_bilinear_map() -> None:
    r"""Every bilinear $\beta:M\times N\to P$ factors through $\otimes$.

    This is what a tensor product *is*, and it is what stands in place of the
    projections a product would have: morphisms out of $M\otimes N$ come from
    bilinear maps and from nowhere else.
    """
    _ensure_preamble()
    L, M = Lattices.U, Lattices.A2
    T = L @ M
    P = L @ M

    beta = lambda m, n: P.pure_tensor(m, n)
    factored = T.from_bilinear(beta, P)

    assert factored.domain() is T and factored.codomain() is P
    for x in L.module_generators():
        for y in M.module_generators():
            assert factored(T.pure_tensor(x, y)) == beta(x, y), (
                "the factorization must agree with the bilinear map on pure tensors"
            )


def test_the_factorization_through_tensor_is_unique() -> None:
    r"""The factorization of $\beta(m,n)=-(m\otimes n)$ is $-\mathrm{id}$, by either route.

    Uniqueness is the other half of the universal property: a morphism out of
    $L\otimes M$ is determined by its values on pure tensors.  So the map the
    universal property produces from $\beta$ and the map written down directly
    on the generators are the same morphism.  The two routes are genuinely
    different -- one goes through the bilinear map, the other never mentions
    it -- and the answer is $-\mathrm{id}$, which is neither the zero map nor
    the identity.
    """
    _ensure_preamble()
    L, M = Lattices.U, Lattices.A2
    T = L @ M

    factored = T.from_bilinear(lambda m, n: -T.pure_tensor(m, n), T)
    direct = T.hom([-generator for generator in T.module_generators()], T)

    assert factored.matrix() == direct.matrix()
    assert factored == direct
    assert (-1 * factored.matrix()).is_one(), "the factorization of -(x @ y) is -id"


def test_the_form_on_a_triple_tensor_is_the_product_of_the_three_pairings() -> None:
    r"""Associativity, stated where it can fail: on the form of a triple tensor.

    $b\big((x\otimes y)\otimes z,\,(x'\otimes y')\otimes z'\big)
    =b_L(x,x')\,b_M(y,y')\,b_N(z,z')$, and the same for $x\otimes(y\otimes z)$.
    Each bracketing is checked against the product of the three pairings --
    an oracle outside both -- rather than against the other one, which the
    Kronecker product makes equal by construction.
    """
    _ensure_preamble()
    L, M, N = Lattices.A1, Lattices.U, Lattices.A2
    LM, MN = L @ M, M @ N
    left, right = LM @ N, L @ MN

    assert left.rank() == 1 * 2 * 2 and right.rank() == 1 * 2 * 2
    for x1 in L.module_generators():
        for y1 in M.module_generators():
            for z1 in N.module_generators():
                for x2 in L.module_generators():
                    for y2 in M.module_generators():
                        for z2 in N.module_generators():
                            expected = L.b(x1, x2) * M.b(y1, y2) * N.b(z1, z2)
                            assert left.b(
                                left.pure_tensor(LM.pure_tensor(x1, y1), z1),
                                left.pure_tensor(LM.pure_tensor(x2, y2), z2),
                            ) == expected
                            assert right.b(
                                right.pure_tensor(x1, MN.pure_tensor(y1, z1)),
                                right.pure_tensor(x2, MN.pure_tensor(y2, z2)),
                            ) == expected


def test_direct_sum_distributes_over_tensor() -> None:
    r"""$(L\oplus M)\otimes N$ and $(L\otimes N)\oplus(M\otimes N)$ carry the same form.

    Not only the same rank: the Gram matrices agree entry by entry in the
    generators each construction produces, which pins the order the labels are
    laid out in as well as the arithmetic.  On ranks alone the identity reads
    $(1+2)\cdot 2=1\cdot 2+2\cdot 2$, which any implementation multiplying
    ranks satisfies.
    """
    _ensure_preamble()
    L, M, N = Lattices.A1, Lattices.A2, Lattices.U

    assert matrix(ZZ, ((L + M) @ N).gram_matrix()) == matrix(
        ZZ, ((L @ N) + (M @ N)).gram_matrix()
    )
    assert ((L + M) @ N).rank() == 6
