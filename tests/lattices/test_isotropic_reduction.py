r"""The isotropic reduction \(K_I=I^\perp/I\) and its parabolic data.

For a totally isotropic \(\iota:I\hookrightarrow L\) the form of \(L\)
descends to \(I^\perp/I\), and the descended form is nondegenerate of
signature \((p-k,q-k)\) when \(L\) has signature \((p,q)\) and
\(\operatorname{rk}I=k\).  Witt's decomposition of a hyperbolic plane off an
isotropic line is the smallest specimen of that statement:
\(U\oplus X\) reduces along a generator of the first plane to \(X\).
"""

from dzack_research.preamble.all import ZZ, Lattices, signature_pair


def test_reducing_a_hyperbolic_plane_off_an_isotropic_line_returns_the_complement() -> None:
    plane = Lattices(ZZ)("U")
    lattice = plane + plane
    isotropic = lattice.module_generator(0)

    reduction = isotropic.isotropic_reduction()

    assert reduction.rank() == 2
    assert reduction.signature_pair() == signature_pair(1, 1)
    assert reduction.determinant() == -1
    assert reduction.is_even()
    assert reduction.is_isometric(plane)


def test_the_reduction_drops_one_from_each_side_of_the_signature() -> None:
    root_lattice = Lattices(ZZ)("A2")
    lattice = Lattices(ZZ)("U") + root_lattice
    assert lattice.signature_pair() == signature_pair(1, 3)

    reduction = lattice.module_generator(0).isotropic_reduction()

    assert reduction.signature_pair() == signature_pair(0, 2)
    assert reduction.determinant() == 3
    assert reduction.is_isometric(root_lattice)


def test_the_reduction_retains_the_embedding_and_the_complement_it_came_from() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic = lattice.module_generator(0)

    reduction = isotropic.isotropic_reduction()

    assert reduction.isotropic_sublattice().rank() == 1
    assert reduction.isotropic_embedding().codomain() is lattice
    # e^perp is spanned by e and the two roots; the reduction kills e alone.
    assert reduction.orthogonal_complement().rank() == 3
    assert reduction.quotient_lattice() is reduction
    assert reduction.projection().domain() is reduction.orthogonal_complement()
    assert reduction.projection().codomain() is reduction


def test_the_projection_kills_the_isotropic_sublattice_and_nothing_else() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic = lattice.module_generator(0)
    reduction = isotropic.isotropic_reduction()

    perpendicular = reduction.orthogonal_complement()
    projection = reduction.projection()
    inclusion = perpendicular.inclusion()
    inside = inclusion.lift(isotropic)

    assert projection(inside) == reduction.zero()
    assert projection.cokernel().cardinality() == 1
    assert all(
        projection(lift) != reduction.zero()
        for lift in reduction.reduction_lifts()
    )


def test_the_descended_form_is_the_form_of_the_complement_on_the_lifts() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    reduction = lattice.module_generator(0).isotropic_reduction()

    perpendicular = reduction.orthogonal_complement()
    lifts = reduction.reduction_lifts()
    projection = reduction.projection()

    assert all(
        reduction.b(projection(lifts(left)), projection(lifts(right)))
        == perpendicular.b(lifts(left), lifts(right))
        for left in reduction.module_generating_set()
        for right in reduction.module_generating_set()
    )


def test_an_eichler_transvection_lies_in_the_unipotent_radical_of_its_parabolic() -> None:
    r"""\(t(e,a)\) fixes \(e\) and acts trivially on \(e^\perp/e\).

    That is the defining property of the unipotent radical of the parabolic
    subgroup stabilizing the isotropic line \(\mathbb Ze\), so the
    transvection must land there and its Levi image must be the identity.
    """
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic, hyperbolic_partner, root, _second_root = lattice.module_generators()
    transvection = lattice.eichler_transvection(isotropic, root)

    assert transvection(isotropic) == isotropic
    assert transvection(hyperbolic_partner) == hyperbolic_partner + root + isotropic

    reduction = isotropic.isotropic_reduction()
    assert transvection in reduction.parabolic_subgroup()
    assert reduction.levi_action()(transvection) == reduction.Aut().one()
    assert transvection in reduction.unipotent_kernel()


def test_the_reflection_in_a_root_is_parabolic_but_not_unipotent() -> None:
    r"""\(s_r\) for \(r\perp e\) stabilizes \(\mathbb Ze\) and acts as \(s_r\) on \(e^\perp/e\).

    Its Levi image is therefore a nonidentity involution, which separates the
    parabolic subgroup from its unipotent radical.
    """
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic, _partner, root, _second_root = lattice.module_generators()
    reflection = lattice.reflection(root)

    reduction = isotropic.isotropic_reduction()
    levi_image = reduction.levi_action()(reflection)

    assert reflection in reduction.parabolic_subgroup()
    assert levi_image != reduction.Aut().one()
    assert levi_image * levi_image == reduction.Aut().one()
    assert reflection not in reduction.unipotent_kernel()
