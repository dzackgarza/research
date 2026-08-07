r"""Regression tests for discriminant forms, stated as mathematics.

Written before the migration onto ``FormModule``/``Cokernel`` so they can judge
it.  Every assertion here is about behaviour a mathematician could check --
identities, invariants, and classical values from the literature -- and none is
about which class, category, or method routing produces it.  A rewrite that
keeps the mathematics passes these; one that breaks it does not.

The oracles are independent of the implementation: $|A_L|=|\det G_L|$, the
discriminant groups of the root lattices, the polarization identity, and the
fact that an isometry preserves the multiset of form values.
"""


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from pathlib import Path
    import dzack_research

    p = Path(dzack_research.__file__).resolve().parent / "preamble"
    load(str(p / "install.sage"))
    load(str(p / "utilities.py"))
    load(str(p / "catalogue.sage"))
    Lattices.install(globals())


def _elementary_divisors(invariants: tuple) -> list:
    """Return the prime-power elementary divisors behind invariant factors."""
    divisors: list = []
    for factor_ in invariants:
        divisors.extend(p ** e for p, e in ZZ(factor_).factor())
    return sorted(divisors)


def test_discriminant_group_order_is_the_absolute_determinant() -> None:
    r"""$|A_L|=|\det G_L|$, for every named lattice in the catalogue.

    An oracle outside the construction: the order comes from the Gram matrix,
    the group from the cokernel, and they have to agree.
    """
    _ensure_preamble()
    for name in ("A2", "A3", "D4", "D5", "E6", "E7", "E8", "U", "U_2", "TEn", "LK3"):
        L = getattr(Lattices, name)
        order = prod(L.discriminant_group().invariants()) or ZZ.one()
        assert order == abs(L.gram_matrix().det()), (
            f"{name}: |A_L| = {order} but |det G| = {abs(L.gram_matrix().det())}"
        )


def test_root_lattice_discriminant_groups_are_the_classical_ones() -> None:
    r"""$A_{A_n}=\mathbb Z/(n+1)$, $A_{D_n}$ of order 4, $A_{E_n}$ of order $9-n$.

    Textbook values, independent of how the cokernel is presented.
    """
    _ensure_preamble()
    for rank in range(2, 8):
        invariants = Lattices.root_lattice("A", rank).discriminant_group().invariants()
        assert prod(invariants) == rank + 1, f"A_{rank}: got {invariants}"
    for rank in range(4, 8):
        invariants = Lattices.root_lattice("D", rank).discriminant_group().invariants()
        assert prod(invariants) == 4, f"D_{rank}: got {invariants}"
        assert _elementary_divisors(invariants) == ([2, 2] if rank % 2 == 0 else [4]), (
            f"D_{rank} should be (Z/2)^2 for even rank and Z/4 for odd: {invariants}"
        )
    for rank, order in ((6, 3), (7, 2), (8, 1)):
        invariants = Lattices.root_lattice("E", rank).discriminant_group().invariants()
        assert (prod(invariants) or ZZ.one()) == order, f"E_{rank}: got {invariants}"


def test_polarization_relates_q_and_b_by_a_factor_of_two() -> None:
    r"""$q(x+y)-q(x)-q(y)=2b(x,y)$, and $q(x)=b(x,x)$ modulo $\mathbb Z$.

    These two identities pin down which convention the discriminant form uses.
    Here $q(x)=\tilde b(x,x)\bmod 2\mathbb Z$ and $b(x,y)=\tilde b(x,y)\bmod
    \mathbb Z$ are both read off the same lift pairing, so polarizing $q$ picks
    up the factor of two: $\tilde b(x+y,x+y)-\tilde b(x,x)-\tilde b(y,y)=
    2\tilde b(x,y)$.  The other convention, $q=\tfrac12 b_q$, would make the
    first identity hold without the two and the second fail, so asserting both
    distinguishes them.
    """
    _ensure_preamble()
    for name in ("A2", "D4", "E6", "U_2", "TEn"):
        A = getattr(Lattices, name).discriminant_group()
        for x in A.module_generators():
            assert QQ(x.q().lift() - x.b(x).lift()) in ZZ, (
                f"{name}: q(x) and b(x,x) disagree mod Z"
            )
            for y in A.module_generators():
                polarized = QQ((x + y).q().lift() - x.q().lift() - y.q().lift())
                assert polarized - 2 * QQ(x.b(y).lift()) in 2 * ZZ, (
                    f"{name}: q(x+y)-q(x)-q(y) is {polarized}, not 2b(x,y) = "
                    f"{2 * QQ(x.b(y).lift())}"
                )


def test_q_is_quadratic_and_b_is_symmetric_bilinear() -> None:
    r"""$q(nx)=n^2q(x)$, $b(x,y)=b(y,x)$, and $b$ is additive in each slot."""
    _ensure_preamble()
    A = Lattices.TEn.discriminant_group()
    x, y, z = A.module_generators()[0], A.module_generators()[1], A.module_generators()[4]
    for n in (2, 3, 5):
        assert QQ((n * x).q().lift() - n ** 2 * x.q().lift()) in 2 * ZZ, (
            f"q({n}x) != {n}^2 q(x)"
        )
    assert x.b(y) == y.b(x), "b is not symmetric"
    assert QQ((x + y).b(z).lift() - x.b(z).lift() - y.b(z).lift()) in ZZ, (
        "b is not additive in its first slot"
    )


def test_discriminant_form_is_the_inverse_gram_modulo_one() -> None:
    r"""$b$ on the induced generators is $G^{-1}\bmod\mathbb Z$.

    The defining computation, checked against the Gram matrix directly rather
    than against whatever the object reports.
    """
    _ensure_preamble()
    for name in ("A2", "D4", "E7", "U_2"):
        L = getattr(Lattices, name)
        inverse = L.gram_matrix().inverse()
        generators = L.discriminant_bilinear_form().module_generators()
        for i, x in enumerate(generators):
            for j, y in enumerate(generators):
                assert QQ(x.b(y).lift() - inverse[i, j]) in ZZ, (
                    f"{name}: b(g{i}, g{j}) is not G^-1[{i},{j}] mod Z"
                )


def test_normal_form_is_an_isometry_onto_a_smaller_generating_set() -> None:
    r"""The normal form has the same group and the same multiset of $b(x,x)$.

    An isometry preserves the form, so the multiset of self-pairings over the
    whole group is an invariant; and the normal form's generating set is
    minimal, so it has one generator per invariant factor where the induced one
    has one per generator of $L$.
    """
    _ensure_preamble()
    for name in ("A2", "D4", "TEn"):
        b = getattr(Lattices, name).discriminant_bilinear_form()
        normal = b.normal_form()
        assert normal.invariants() == b.invariants(), f"{name}: group changed"
        assert len(normal.module_generators()) == len(normal.invariants()), (
            f"{name}: normal form should sit on a minimal generating set"
        )
        assert sorted(QQ(x.b(x).lift()) for x in b) == sorted(
            QQ(x.b(x).lift()) for x in normal
        ), f"{name}: normal form is not isometric"


def test_invariant_factor_form_is_an_isometry_on_invariant_factor_generators() -> None:
    _ensure_preamble()
    b = Lattices.TEn.discriminant_bilinear_form()
    factored = b.invariant_factor_form()
    assert factored.invariants() == b.invariants()
    assert len(factored.module_generators()) == len(factored.invariants())
    assert sorted(QQ(x.b(x).lift()) for x in b) == sorted(
        QQ(x.b(x).lift()) for x in factored
    )


def test_primary_parts_have_the_prime_power_orders_and_exhaust_the_group() -> None:
    r"""$|A_p|$ is the $p$-part of $|A|$, and $\prod_p|A_p|=|A|$.

    The Sylow decomposition, checked on a group with two primes so the claim is
    not vacuous.
    """
    _ensure_preamble()
    A = Lattices.root_lattice("A", 5).discriminant_group()
    order = prod(A.invariants())
    assert order == 6, f"A_5 should have discriminant group of order 6, got {order}"
    total = ZZ.one()
    for p, exponent in ZZ(order).factor():
        part = A.primary_part(p).structure_morphism().domain()
        part_order = prod(part.invariants()) or ZZ.one()
        assert part_order == p ** exponent, (
            f"{p}-primary part has order {part_order}, expected {p ** exponent}"
        )
        total *= part_order
    assert total == order, f"primary parts multiply to {total}, not {order}"


def test_odd_lattices_have_no_quadratic_discriminant_form() -> None:
    r"""$q$ exists exactly when $L$ is even.

    Moving a lift by $\ell$ shifts $b(\tilde x,\tilde x)$ by $b(\ell,\ell)$,
    which lies in $2\mathbb Z$ only for even $L$ -- so an odd lattice's $A_L$
    carries $b$ alone and asking for $q$ must fail rather than return something.
    """
    import pytest

    _ensure_preamble()
    odd = Lattices.IPQ(1, 2)
    assert not odd.is_even(), "I_{1,2} is odd"
    with pytest.raises(AssertionError):
        odd.discriminant_quadratic_form()
    even = Lattices.U_2
    assert even.is_even()
    assert prod(even.discriminant_quadratic_form().invariants()) == 4


def test_correlation_is_the_gram_matrix_into_the_dual() -> None:
    r"""$c: L\to L^\vee$ has matrix $G$, and $L^\vee$ has Gram $G^{-1}$.

    $c(e_i)=\sum_j G_{ij}e_j^\vee$ is what makes $c$ the map $v\mapsto b(v,-)$
    rather than an inclusion of coordinate vectors.

    The claim is that the two *arrays* agree, so it is asserted on the arrays.
    The matrix of a morphism and the Gram matrix of a form are different
    objects and never compare equal as objects.
    """
    _ensure_preamble()
    for name in ("A2", "D4", "E8", "U_2"):
        L = getattr(Lattices, name)
        assert L.correlation().matrix()._sage_matrix() == L.gram_matrix(), (
            f"{name}: c is not G"
        )
        assert L.dual_lattice().gram_matrix() == L.gram_matrix().inverse(), (
            f"{name}: L^v does not carry G^-1"
        )


def test_discriminant_group_of_a_direct_sum_is_the_direct_sum_of_the_groups() -> None:
    r"""$A_{L\oplus M}\cong A_L\oplus A_M$, as elementary divisors."""
    _ensure_preamble()
    left, right = Lattices.A2, Lattices.root_lattice("A", 3)
    combined = (left + right).discriminant_group()
    assert _elementary_divisors(combined.invariants()) == sorted(
        _elementary_divisors(left.discriminant_group().invariants())
        + _elementary_divisors(right.discriminant_group().invariants())
    ), f"A_{{A2+A3}} is {combined.invariants()}"


def test_discriminant_form_convention_is_nikulins_not_peters_sterks() -> None:
    r"""Pin which of the two conventions this preamble uses.

    Peters--Sterk Remark 1.6.6 [PS24] names both: theirs is
    $q_L(x)=\tfrac12 b_{\mathbb Q}(x,x)\bmod\mathbb Z$, valued in
    $\mathbb Q/\mathbb Z$; Nikulin's is $q_L^\#(x)=b_{\mathbb Q}(x,x)\bmod
    2\mathbb Z$, valued in $\mathbb Q/2\mathbb Z$.  They are isomorphic by
    multiplication by 2, so nothing distinguishes them except the numbers -- and
    a silent flip would rescale every discriminant form in the project.

    This preamble uses Nikulin's, which is also Sage's.  The oracle is the
    book's own Example 1.6.9: the lattice with Gram $A$ below has $A^{-1}$ with
    third column $(1,2,-5)/12$, discriminant group $\mathbb Z/12$, and
    $b_{A,\mathbb Q}(e_3^*,e_3^*)=7/12$ -- all three printed there and all three
    asserted here.  $q$ is then $b_{\mathbb Q}$ on a lift read modulo
    $2\mathbb Z$, which is $-5/12$, i.e. $19/12$.
    """
    _ensure_preamble()
    A = matrix(ZZ, [[-2, 1, 0], [1, 2, 1], [0, 1, -2]])
    L = IntegralLattice(A)
    assert A.inverse().column(2) == vector(QQ, [1, 2, -5]) / 12, (
        "this is not the book's Example 1.6.9 lattice"
    )
    disc = L.discriminant_group()
    assert disc.invariants() == (12,), f"book says Z/12, got {disc.invariants()}"

    third = disc.module_generators()[2]
    assert third.order() == 12, "e_3^* has order 12 in the book"
    assert third.b(third).lift() == QQ(7) / 12, (
        f"b(e_3^*, e_3^*) is {third.b(third).lift()}, book says 7/12"
    )
    assert third.q().lift() == QQ(-5) / 12 + 2, (
        f"q(e_3^*) is {third.q().lift()}; Nikulin's convention gives "
        "b_Q(x,x) = -5/12 read mod 2Z"
    )
    assert third.q().parent().n == 2, (
        "q must take values in Q/2Z under Nikulin's convention"
    )
    assert third.b(third).parent().n == 1, "b takes values in Q/Z"
