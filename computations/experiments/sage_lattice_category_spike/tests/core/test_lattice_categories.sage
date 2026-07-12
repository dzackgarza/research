from __future__ import annotations

from itertools import product

import pytest

from sage.all import (
    Matrix,
    Polyhedron,
    QQ,
    ZZ,
    block_diagonal_matrix,
    identity_matrix,
    matrix,
    vector,
)
from sage.groups.additive_abelian.qmodnz import QmodnZ

from sage_lattice_category_spike.lattice_categories import (
    DiscriminantForms,
    Lattice,
    Lattices,
    SyntheticGenus,
    SyntheticLattice,
    TorsionQuadraticForm,
)


def assert_matrix_equal(left, right):
    assert matrix(QQ, left) == matrix(QQ, right)


def test_category_axioms_bind_to_synthetic_lattice_contract():
    C = Lattices(ZZ)
    assert C.Even().is_subcategory(C.Integral())
    assert C.Unimodular().is_subcategory(C.Integral())
    assert C.PositiveDefinite().is_subcategory(C.Definite())
    assert C.NegativeDefinite().is_subcategory(C.Definite())
    assert C.Nondegenerate().is_subcategory(C)

    D = DiscriminantForms(ZZ)
    assert D.Quadratic().is_subcategory(D.Bilinear())
    assert D.Even().is_subcategory(D.Quadratic())


def test_indefinite_hyperbolic_plane_is_first_class_synthetic_lattice():
    U = Lattice("U", label="U")
    assert isinstance(U, SyntheticLattice)
    assert U.base_ring() is ZZ
    assert U.signature_pair() == (1, 1)
    assert U.is_integral()
    assert U.is_even()
    assert U.is_unimodular()
    assert U.discriminant_group().invariants() == ()


def test_category_dispatch_uses_form_axioms_not_constructor_factories():
    A2 = Lattice("A2(-1)", label="A2")
    minus_A2 = Lattice(-A2.gram_matrix(), label="-A2")
    radical = Lattice(matrix(QQ, 1, 1, [0]), label="rad")

    assert A2 in Lattices(ZZ).PositiveDefinite()
    assert minus_A2 in Lattices(ZZ).NegativeDefinite()
    assert Lattice("U", label="U") in Lattices(ZZ).Indefinite()
    assert radical in Lattices(ZZ)
    assert radical not in Lattices(ZZ).Nondegenerate()
    assert radical.signature_pair() == (0, 0)


def test_positive_definite_algorithms_are_axiom_gated():
    A2 = Lattice("A2(-1)", label="A2")
    U = Lattice("U", label="U")
    rank_one = Lattice(matrix(ZZ, 1, 1, [2]), label="<2>")
    rank_three = Lattice(matrix.diagonal(ZZ, [2, 4, 6]), label="<2,4,6>")

    reduced = A2.LLL()
    assert isinstance(reduced, SyntheticLattice)
    change_of_basis = matrix(ZZ, A2.gram_matrix()).LLL_gram()
    assert_matrix_equal(
        reduced.gram_matrix(),
        change_of_basis * A2.gram_matrix() * change_of_basis.transpose(),
    )
    assert reduced.determinant() == A2.determinant()
    assert reduced.discriminant() == A2.discriminant()
    G = matrix(ZZ, 3, 3, [4, 1, 1, 1, 3, 1, 1, 1, 2])
    G_lattice = Lattice(G, label="G")
    # the reduction/CVP suite is positive-definite vocabulary (D1 revision):
    # present on any PD lattice, no refinement step
    for name in ("BKZ", "closest_vector", "voronoi_cell"):
        assert (name in dir(G_lattice))
    bkz_lattice = G_lattice.BKZ(block_size=2)
    assert_matrix_equal(
        bkz_lattice.gram_matrix(), matrix(ZZ, 3, 3, [2, 1, 1, 1, 3, 1, 1, 1, 4])
    )
    assert bkz_lattice.determinant() == G_lattice.determinant()
    assert bkz_lattice.discriminant() == G_lattice.discriminant()
    assert [
        [tuple(vector.coefficient_vector()) for vector in vectors]
        for vectors in rank_one.short_vectors(5)
    ] == [
        [(0,)],
        [],
        [(1,), (-1,)],
        [],
        [],
    ]
    short = A2.short_vectors(3)
    assert [
        [tuple(vector.coefficient_vector()) for vector in vectors] for vectors in short
    ] == [
        [(0, 0)],
        [],
        [(1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)],
    ]
    assert [
        [tuple(vector.coefficient_vector()) for vector in vectors]
        for vectors in rank_three.short_vectors(7)
    ] == [
        [(0, 0, 0)],
        [],
        [(1, 0, 0), (-1, 0, 0)],
        [],
        [(0, 1, 0), (0, -1, 0)],
        [],
        [(0, 0, 1), (0, 0, -1), (1, 1, 0), (-1, -1, 0), (1, -1, 0), (-1, 1, 0)],
    ]
    assert A2.shortest_vector().q() == 2
    target = [QQ(2) / 3, QQ(2) / 3]
    brute_force = min(
        (A2(coordinates) for coordinates in product(range(-2, 3), repeat=2)),
        key=lambda candidate: (
            (
                vector(
                    QQ,
                    [candidate.coefficient_vector()[i] - target[i] for i in range(2)],
                )
                * A2.gram_matrix()
                * vector(
                    QQ,
                    [candidate.coefficient_vector()[i] - target[i] for i in range(2)],
                )
            ),
            tuple(candidate.coefficient_vector()),
        ),
    )
    assert A2.closest_vector(target) == brute_force == A2([1, 1])
    expected_ieqs = []
    for vectors in A2.short_vectors(3):
        for lattice_vector in vectors:
            if lattice_vector != A2.zero():
                coordinates = vector(QQ, lattice_vector.coefficient_vector())
                gram_vector = coordinates * A2.gram_matrix()
                expected_ieqs.append(
                    [QQ(lattice_vector.q()) / 2] + [-gram_vector[i] for i in range(2)]
                )
    assert A2.voronoi_cell(radius=3) == Polyhedron(ieqs=expected_ieqs, base_ring=QQ)
    assert len(A2.voronoi_cell().vertices()) == 6

    for name in (
        "LLL",
        "BKZ",
        "short_vectors",
        "shortest_vector",
        "closest_vector",
        "voronoi_cell",
    ):
        assert not (name in dir(U))


def test_raw_module_methods_are_available_only_through_accessors():
    A2 = Lattice("A2(-1)", label="A2")

    for name in (
        "free_resolution",
        "graded_free_resolution",
        "pseudoHom",
        "pseudohom",
        "sparse_module",
        "dense_module",
        "subspaces",
        "quotient_abstract",
        "underlying_module",
        "underlying_quadratic_module",
        "underlying_quotient_module",
        "rationalization_module",
        "basis_matrix",
    ):
        assert not (name in dir(A2))


def test_rationalization_is_scalar_extension_not_external_ambient_embedding():
    U = Lattice("U", label="U")
    U_QQ = U.rationalization()

    assert U_QQ.base_ring() is QQ
    assert_matrix_equal(U_QQ.gram_matrix(), U.gram_matrix())
    assert U_QQ.gen(0).b(U_QQ.gen(1)) == 1
    assert U.quadratic_form()(U([1, 1])) == 2


def test_elements_have_owned_module_arithmetic_and_bilinear_form():
    U = Lattice("U", label="U")
    e, f = U.gens()

    assert e + f == U([1, 1])
    assert 2 * e - f == U([2, -1])
    assert -(e + f) == U([-1, -1])
    assert (e + f).q() == 2


def test_rank_one_subobject_is_a_lattice_plus_inclusion():
    U = Lattice("U", label="U")
    # A sublattice is a subobject: a plain lattice generated by an ELEMENT of U,
    # together with its inclusion morphism -- U itself stores no ambient.
    diagonal = U.subobject([U([1, 1])], label="diag")

    assert diagonal.rank() == 1
    assert diagonal.gram_matrix() == matrix(QQ, 1, 1, [2])
    assert diagonal.is_submodule(U)
    assert diagonal.inclusion().codomain() == U


def test_dual_is_owned_zz_lattice_in_the_rationalization():
    A2 = Lattice("A2(-1)", label="A2")
    A2_dual = A2.dual()

    # The based dual is (ZZ, G^{-1}); the inclusion L -> L# is the metric morphism
    # v |-> b(v, -), a form-preserving injection into the dual (matrix G).
    inclusion = A2.dual_inclusion()
    assert inclusion.codomain() == A2_dual
    assert inclusion.image().is_submodule(A2_dual)
    assert not A2_dual.is_integral()
    assert_matrix_equal(
        A2_dual.gram_matrix(),
        A2.gram_matrix().inverse(),
    )
    assert A2_dual.dual() == A2


def test_overlattice_is_the_inclusion_morphism_into_a_plain_lattice():
    U = Lattice("U", label="U")
    half_e = matrix(QQ, 1, 2, [QQ(1) / 2, 0])
    inclusion = U.overlattice(half_e, label="U_half_e")
    overlattice = inclusion.codomain()

    # The overlattice constructor mints the witness U -> L'; the index is the
    # morphism's own (cokernel cardinality), and the det-index law
    # [L':U]^2 = det U / det L' is a genuine cross-check, not the definition.
    assert inclusion.domain() == U
    assert overlattice.rank() == 2
    assert inclusion.index() == 2
    assert abs(U.determinant()) == abs(overlattice.determinant()) * inclusion.index() ** 2
    assert U.is_primitive(U.subobject([U([1, 0])], label="e"))


def test_orthogonal_direct_sum_and_tensor_product_constructions_are_synthetic():
    U = Lattice("U", label="U")
    e_line = U.subobject([U([1, 0])], label="e")
    complement = U.orthogonal_complement(e_line)

    assert complement.rank() == 1

    A2 = Lattice("A2(-1)", label="A2")
    direct = U.direct_sum(A2)
    assert direct.rank() == 4
    assert direct.signature_pair() == (3, 1)

    tensor = e_line.tensor_product(A2)
    assert tensor.rank() == 2
    assert_matrix_equal(tensor.gram_matrix(), matrix(QQ, 2, 2, [0, 0, 0, 0]))


def test_discriminant_group_is_owned_invariant_factor_quotient_with_forms():
    A2 = Lattice("A2(-1)", label="A2")
    D = A2.discriminant_group()

    assert D.invariants() == (3,)
    assert D.cardinality() == 3
    assert D.gen(0).q() == QQ(2) / 3
    assert D.gen(0) + 2 * D.gen(0) == D([0])
    assert D.lift(D.gen(0)).q() == QQ(2) / 3
    assert D.projection(D.lift(D.gen(0))) == D.gen(0)
    assert D.b(D.gen(0), D.gen(0)) == QQ(2) / 3
    assert D.q(D.gen(0)) == QQ(2) / 3
    assert D.value_module() == QmodnZ(QQ(1)) and D.value_module().n == 1
    assert D.value_module_qf() == QmodnZ(QQ(2)) and D.value_module_qf().n == 2
    assert D.is_nondegenerate()
    assert D.annihilator() == 3
    assert D.brown_invariant() == 2
    assert D.is_genus((2, 0))
    assert isinstance(D.genus((2, 0)), SyntheticGenus)
    assert A2.genus() == D.genus((2, 0))

    H5_twist = Lattice(Matrix(ZZ, 2, 2, [4, 2, 2, -4]), label="2H5")
    A = H5_twist.discriminant_group()
    assert A.invariants() == (2, 10)
    assert A.primary_part(2).invariants() == (2, 2)
    assert A.primary_part(5).invariants() == (5,)


def test_odd_integral_discriminant_group_keeps_qq_mod_zz_form():
    L = Lattice(matrix(ZZ, 1, 1, [3]), label="<3>")
    D = L.discriminant_group()

    assert D.invariants() == (3,)
    assert D.value_module() == QmodnZ(QQ(1)) and D.value_module().n == 1
    assert D.value_module_qf() == QmodnZ(QQ(1)) and D.value_module_qf().n == 1
    assert D.gen(0).b(D.gen(0)) == QQ(1) / 3
    assert D.gen(0).q() == QQ(1) / 3
    with pytest.raises(ValueError):
        D.brown_invariant()


def test_discriminant_group_is_typed_as_a_finite_abelian_group_not_a_zz_module():
    D = Lattice("A2(-1)", label="A2").discriminant_group()

    # finite-abelian-group API (order/exponent/is_cyclic/short_name/permutation_group),
    # not a "module over ZZ".
    assert D.order() == 3
    assert D.exponent() == 3
    assert D.is_cyclic()
    assert D.short_name() == "Z/3"
    permutation_group = D.permutation_group()
    assert permutation_group.order() == D.cardinality()

    # element operators: scalar multiplication IS the group action; exponentiation
    # is meaningless on an additive-group element and must fail loud.
    g = D.gen(0)
    assert 2 * g == g + g
    assert 3 * g == D.zero()
    with pytest.raises(TypeError):
        g**2


def test_discriminant_subgroups_actions_and_overlattice_construction_are_owned():
    L = Lattice(matrix(ZZ, 1, 1, [4]), label="<4>")
    D = L.discriminant_group()
    g = D.gen(0)
    H = D.subgroup_generated_by([2 * g])

    assert H.cardinality() == 2
    assert H.is_bilinear_isotropic()
    assert not H.is_quadratic_isotropic()
    assert D.orthogonal_submodule_to(H).cardinality() == 2

    gluing = D.overlattice_from_isotropic_subgroup(H, label="<1>")
    assert gluing.index() == H.cardinality()
    assert_matrix_equal(gluing.codomain().gram_matrix(), matrix(QQ, 1, 1, [1]))

    primary = L.discriminant_group(primary=2)
    local = L.local_modification([2 * primary.gen(0)], 2, label="<1>_local")
    assert_matrix_equal(local.gram_matrix(), matrix(QQ, 1, 1, [1]))

    negation = D.orthogonal_group(gens=[matrix(ZZ, 1, 1, [-1])], check=True)[0]
    assert negation(g) == -g
    assert negation.preserves_form()


def test_homs_are_form_preserving_by_construction():
    U = Lattice("U", label="U")

    identity = U.hom(identity_matrix(ZZ, 2))
    assert identity(U.gen(0)) == U.gen(0)
    assert identity(U.gen(0)).b(identity(U.gen(1))) == U.gen(0).b(U.gen(1))

    swap = U.hom(matrix(ZZ, 2, 2, [0, 1, 1, 0]))
    assert swap(U.gen(0)) == U.gen(1)
    assert swap(U.gen(1)) == U.gen(0)


def test_hom_image_and_kernel_are_synthetic_lattices():
    A2 = Lattice("A2(-1)", label="A2")
    A2_dual = A2.dual()
    inclusion = A2.hom(Matrix(ZZ, 2, 2, [2, -1, -1, 2]), codomain=A2_dual)

    image = inclusion.image()
    kernel = inclusion.kernel()

    assert image.is_submodule(A2_dual)
    assert_matrix_equal(image.gram_matrix(), A2.gram_matrix())
    assert kernel.rank() == 0
    assert kernel.gram_matrix().nrows() == 0


def test_integral_lattice_inclusion_into_dual_is_a_synthetic_morphism():
    A2 = Lattice("A2(-1)", label="A2")
    A2_dual = A2.dual()
    inclusion = A2.hom(Matrix(ZZ, 2, 2, [2, -1, -1, 2]), codomain=A2_dual)
    quotient = A2_dual.finite_quotient(A2)
    negation = A2_dual.hom(-identity_matrix(ZZ, 2))
    induced = negation.induced_map_on_quotient(quotient)
    generator = quotient.gen(0)

    assert inclusion(A2.gen(0)).q() == A2.gen(0).q()
    assert quotient.projection(quotient.lift(generator)) == generator
    assert induced(generator) == quotient.projection(negation(quotient.lift(generator)))

    U = Lattice("U", label="U")
    relation = U.subobject([U([2, 0]), U([0, 1])], label="2e_plus_f")
    quotient = U.finite_quotient(relation)
    swap = U.hom(matrix(ZZ, 2, 2, [0, 1, 1, 0]))


def test_definiteness_and_nondegeneracy_predicates_derive_from_signature():
    A2 = Lattice("A2(-1)", label="A2")
    minus_A2 = Lattice(-A2.gram_matrix(), label="-A2")
    U = Lattice("U", label="U")
    degenerate = Lattice(matrix(QQ, 1, 1, [0]), label="rad")

    assert A2.is_nondegenerate() and A2.is_definite() and A2.is_positive_definite()
    assert not A2.is_negative_definite() and not A2.is_indefinite()
    assert minus_A2.is_negative_definite() and not minus_A2.is_positive_definite()
    assert U.is_nondegenerate() and U.is_indefinite() and not U.is_definite()
    assert not degenerate.is_nondegenerate()
    assert not degenerate.is_definite() and not degenerate.is_indefinite()


def test_radical_quotient_kills_the_radical_and_realizes_eperp_mod_e():
    U = Lattice("U", label="U")
    assert U.radical_quotient() is U  # nondegenerate: nothing to quotient

    UU = U.direct_sum(U, label="U+U")
    e_line = UU.subobject([UU([1, 0, 0, 0])], label="e")
    e_perp = UU.orthogonal_complement(e_line)
    assert e_perp.is_degenerate()

    quotient = e_perp.radical_quotient()
    assert quotient.is_nondegenerate()
    assert_matrix_equal(quotient.gram_matrix(), U.gram_matrix())  # e^perp / e = U

    diagonal = Lattice(matrix(ZZ, 2, 2, [2, 0, 0, 0]), label="<2>+<0>")
    assert_matrix_equal(
        diagonal.radical_quotient().gram_matrix(), matrix(QQ, 1, 1, [2])
    )

    fully_degenerate = Lattice(matrix(ZZ, 2, 2, [0, 0, 0, 0]), label="0^2")
    assert (
        fully_degenerate.radical_quotient().rank() == 0
    )  # rad(L) = L, so L/rad(L) is rank 0


def test_lattice_element_pairs_through_the_star_operator():
    r"""
    Issue #2: ``v * w`` computes the bilinear pairing ``b(v, w)``;
    ``v * v`` computes the quadratic form ``q(v) = b(v, v)``.
    Scalar multiplication works for R-scalars (ZZ) and S-scalars (QQ)
    via base change to ``M ⊗_R S``.
    """
    U = Lattice("U", label="U")
    e, f = U.gens()

    for name in ("inner_product", "dot_product", "norm", "hermitian_inner_product"):
        assert not (name in dir(e))

    # R-scalar action (n ∈ ZZ): result stays in L
    assert 2 * e == U([2, 0]) and e * 2 == U([2, 0])

    # S-scalar action (q ∈ QQ \ ZZ): base change to L_QQ
    s = QQ(1) / 3
    result = e * s
    assert result.parent().base_ring() is QQ
    assert result.parent().rank() == U.rank()
    assert tuple(result.coefficient_vector()) == (QQ(1) / 3, 0)

    # pairing via * (issue #2)
    assert e * f == 1 and f * e == 1
    assert e * e == 0 and f * f == 0  # U has hyperbolic form [[0,1],[1,0]]
    assert (e + f) * (e + f) == 2  # q(e+f) = b(e+f, e+f) = 2

    # b() and q() still work and agree with *
    assert e.b(f) == e * f and (e + f).q() == (e + f) * (e + f)

    # different-parent lattice element: assertion error (not ValueError)
    A2 = Lattice("A2(-1)", label="A2")
    with pytest.raises(AssertionError):
        e * A2.gen(0)

    # unsupported operand types hit assert_never
    with pytest.raises(AssertionError):
        e * "not a scalar"
    with pytest.raises(AssertionError):
        e * [1, 2]


def test_discriminant_group_element_pairs_through_the_star_operator():
    r"""
    Issue #2 (discriminant side): ``x * y`` computes ``b(x, y)``
    on ``SyntheticDiscriminantGroupElement`` with strict same-parent identity.
    R-scalar action (ZZ) stays in D; S-scalar (QQ) base-changes to
    ``D ⊗_ZZ QQ = 0`` (torsion killed by localization).
    """
    L = Lattice(matrix(ZZ, 1, 1, [3]), label="<3>")
    D = L.discriminant_group()
    g = D.gen(0)

    assert g * g == QQ(1) / 3  # q(g) = b(g, g) = 1/3
    assert g.q() == g * g  # q() agrees with *
    assert D.b(g, g) == g * g  # parent b() agrees with *

    # R-scalar action (n ∈ ZZ): result stays in D
    assert 2 * g == D([2]) and g * 2 == D([2])

    # S-scalar action (q ∈ QQ \ ZZ): D ⊗_ZZ QQ = 0, result is zero
    result = g * (QQ(1) / 3)
    assert result.parent().invariants() == ()
    assert result.parent().cardinality() == 1

    # different-parent discriminant element: assertion error
    D2 = Lattice(matrix(ZZ, 1, 1, [5]), label="<5>").discriminant_group()
    with pytest.raises(AssertionError):
        g * D2.gen(0)

    # unsupported operand types hit assert_never
    with pytest.raises(AssertionError):
        g * "not a scalar"


def test_explicit_isometries_act_on_discriminant_groups():
    U = Lattice("U", label="U")
    swap = matrix(ZZ, 2, 2, [0, 1, 1, 0])

    isometry = U.hom(swap)
    assert isometry(U.gen(0)) == U.gen(1)
    assert U.isometry_group().discriminant_action(isometry).is_identity()
    assert U.isometry_group().subgroup([swap]).discriminant_image()[0].is_identity()


def test_functor_layer_realizes_the_categorical_identities():
    U = Lattice("U", label="U")
    A2 = Lattice("A2(-1)", label="A2")

    # discriminant_group LEAVES Lattices for DiscriminantForms; value ring is QQ/ZZ.
    assert A2 in Lattices(ZZ)
    A = A2.discriminant_group()
    assert A in DiscriminantForms(ZZ)
    assert A not in Lattices(ZZ)
    assert A.value_module() == QmodnZ(QQ(1))  # QQ/ZZ

    # radical_quotient STAYS in Lattices and lands in the nondegenerate subcategory.
    UU = U.direct_sum(U, label="U+U")
    e_perp = UU.orthogonal_complement(UU.subobject([UU([1, 0, 0, 0])], label="e"))
    assert e_perp.is_degenerate()
    quotient = e_perp.radical_quotient()
    assert quotient in Lattices(ZZ).Nondegenerate()

    # rationalization L |-> L (x) QQ: base ring QQ, same Gram; base_extend agrees.
    rat = A2.rationalization()
    assert rat.base_ring() is QQ
    assert_matrix_equal(rat.gram_matrix(), A2.gram_matrix())
    assert A2.base_extend(QQ) == rat

    # dual is an involution on nondegenerate ZZ-lattices.
    assert A2.dual().dual() == A2

    # orthogonal direct sum: Gram is block-diagonal, cross-pairings vanish, ranks add.
    S = A2.direct_sum(U)
    assert S.rank() == A2.rank() + U.rank()
    assert_matrix_equal(
        S.gram_matrix(), block_diagonal_matrix(A2.gram_matrix(), U.gram_matrix())
    )
    assert S.b(S.gen(0), S.gen(A2.rank())) == 0  # summands are orthogonal

    # tensor product: Gram is the Kronecker product of the Grams.
    T = A2.tensor_product(U)
    assert_matrix_equal(
        T.gram_matrix(), A2.gram_matrix().tensor_product(U.gram_matrix())
    )


def test_positive_definite_enumeration_suite_matches_sage_and_is_axiom_gated():
    from sage.modules.free_module_integer import IntegerLattice
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    from sage.rings.infinity import Infinity

    B = Matrix(ZZ, 3, 3, [2, 1, 0, 0, 2, 1, 0, 0, 2])
    G = B * B.transpose()
    L = Lattice(G, label="pd3")
    reference = IntegerLattice(
        B
    )  # same lattice, realized with the standard inner product

    # the reduction/CVP/Voronoi suite is positive-definite vocabulary (D1
    # revision): present on the PD lattice itself, no refinement step
    for name in (
        "HKZ",
        "BKZ",
        "gaussian_heuristic",
        "hadamard_ratio",
        "closest_vector",
        "approximate_closest_vector",
        "babai",
        "voronoi_cell",
        "voronoi_relevant_vectors",
        "enumerate_close_vectors",
        "update_reduced_basis",
    ):
        assert (name in dir(L))

    # scalar invariants reference-agree with Sage
    assert L.volume() == reference.volume()
    assert abs(L.gaussian_heuristic().n() - reference.gaussian_heuristic().n()) < 1e-9
    # row 12: the exact Gamma form reference-agrees too (both exact symbolic values).
    assert (
        abs(
            L.gaussian_heuristic(exact_form=True).n()
            - reference.gaussian_heuristic(exact_form=True).n()
        )
        < 1e-9
    )
    assert L.gaussian_heuristic(exact_form=True) != L.gaussian_heuristic()
    assert abs(L.hadamard_ratio().n() - reference.hadamard_ratio().n()) < 1e-9
    assert L.minimum() == IntegralLattice(G).minimum()
    assert L.maximum() == Infinity

    # HKZ: reference-agree the canonical HKZ-reduced Gram with Sage, and check the
    # defining property that the first basis vector is a shortest vector.
    sage_hkz = IntegerLattice(B).HKZ()
    assert L.HKZ().gram_matrix() == sage_hkz * sage_hkz.transpose()
    assert L.HKZ().gram_matrix()[0, 0] == L.minimum()

    # reduced_basis: the returned basis is genuinely LLL-reduced -- verified by Sage's
    # independent is_LLL_reduced on the embedded basis (embed by W*B). Determinant alone
    # would not distinguish this from the unreduced basis, which fails the verifier.
    W = matrix(ZZ, [list(e.coefficient_vector()) for e in L.reduced_basis()])
    assert (W * B).is_LLL_reduced()
    assert not B.is_LLL_reduced()  # teeth: the unreduced basis is not LLL-reduced

    # Babai CVP reference-agrees under the ambient <-> coordinate translation (x_ambient = x_coords * B).
    target = [1, 1, 1]
    mine = L.approximate_closest_vector(target)
    assert tuple(vector(ZZ, mine.coefficient_vector()) * B) == tuple(
        reference.approximate_closest_vector(vector(ZZ, target) * B)
    )
    assert L.babai(target) == mine  # babai is the alias

    # Voronoi relevant vectors: the exact SET (not merely the count) agrees with Sage
    # under the ambient map.
    assert {
        tuple(vector(ZZ, v.coefficient_vector()) * B)
        for v in L.voronoi_relevant_vectors()
    } == {tuple(v) for v in reference.voronoi_relevant_vectors()}

    # [NEW] enumerations (no Sage reference): certified COMPLETE against an independent
    # brute-force box search over Z^3, so a truncated enumeration fails.
    gram = matrix(QQ, G)

    def squared_norm(coordinates, center=(0, 0, 0)):
        delta = vector(QQ, [QQ(coordinates[i]) - center[i] for i in range(3)])
        return delta * gram * delta

    def brute_force(predicate, lo, hi):
        return {c for c in product(range(lo, hi), repeat=3) if predicate(c)}

    assert {
        tuple(v.coefficient_vector()) for v in L.enumerate_short_vectors(4)
    } == brute_force(lambda c: 0 < squared_norm(c) <= 4, -4, 5)
    assert {
        tuple(v.coefficient_vector()) for v in L.enumerate_close_vectors(target, 6)
    } == brute_force(lambda c: squared_norm(c, target) <= 6, -3, 6)

    # update_reduced_basis: immutable functional analog; injecting an in-lattice vector keeps the lattice.
    assert L.update_reduced_basis(L.gen(0)).determinant() == L.determinant()

    # axiom-gating: an indefinite lattice exposes NONE of the suite.
    U = Lattice("U", label="U")
    for name in (
        "HKZ",
        "minimum",
        "maximum",
        "volume",
        "gaussian_heuristic",
        "hadamard_ratio",
        "reduced_basis",
        "approximate_closest_vector",
        "babai",
        "voronoi_relevant_vectors",
        "enumerate_short_vectors",
        "enumerate_close_vectors",
        "update_reduced_basis",
    ):
        assert not (name in dir(U))


def test_negative_definite_enumeration_transports_through_the_sign_twist():
    # G4 + row 9c (ratified): negative-definite conventions ARE the natural
    # conventions on L(-1). Reference values: Sage IntegralLattice doctests
    # (A2.twist(-1).minimum() == -Infinity, .maximum() == -2) and the Sage
    # short-vector oracle for counts.
    from sage.rings.infinity import Infinity
    from sage.quadratic_forms.quadratic_form import QuadraticForm

    A2 = Lattice("A2(-1)", label="A2")
    A2_negative = A2.twist(-1)
    assert A2_negative.is_negative_definite()
    assert A2_negative.minimum() == -Infinity
    assert A2_negative.maximum() == -2
    assert A2_negative.shortest_vector().q() == -2
    assert A2_negative.volume() == A2.volume()

    # AG root regime: roots of the negative-definite lattice are its (-2)-vectors,
    # in bijection (same coefficient vectors) with the norm-2 vectors of L(-1);
    # the count agrees with the Sage enumeration oracle.
    oracle_count = len(
        QuadraticForm(2 * matrix(ZZ, A2.gram_matrix())).short_vector_list_up_to_length(
            3
        )[2]
    )
    negative_roots = A2_negative.roots()
    assert len(negative_roots) == oracle_count
    assert all(root.q() == -2 for root in negative_roots)

    # PD side of the same ratified convention.
    positive_roots = A2.roots()
    assert len(positive_roots) == oracle_count
    assert all(root.q() == 2 for root in positive_roots)
    assert A2.vectors_of_square(0) == (A2.zero(),)
    assert A2_negative.vectors_of_square(0) == (A2_negative.zero(),)

    # short-vector transport: identical coefficient vectors, negated norms.
    for length, vectors in enumerate(A2_negative.short_vectors(3)):
        for vector in vectors:
            assert vector.q() == -length


def test_nikulin_overlattice_and_metabolizer_identities_hold():
    # Nikulin (1980, "Integral symmetric bilinear forms...", Math. USSR Izv. 14, sec.
    # 1.4-1.9): for an even lattice L with discriminant form A and an isotropic subgroup
    # H, the overlattice's discriminant form A_{L'} is ISOMETRIC to the subquotient form
    # H^perp / H. We certify true form isometry, not matching invariants.
    L = Lattice(
        matrix(ZZ, 3, 3, [0, 2, 0, 2, 0, 0, 0, 0, 2]), label="U2+A1"
    )  # U(2) + <2>
    D = L.discriminant_group()
    assert D.invariants() == (2, 2, 2)

    def as_finite_quadratic_form(form):
        # The quadratic Gram of a finite quadratic form (q on the diagonal, b off it,
        # over a generating set) presents it as the canonical quadratic-discriminant-form
        # TYPE, so both Nikulin sides are the SAME type and comparable as forms.
        generators = form.gens()
        gram = matrix(
            QQ,
            len(generators),
            len(generators),
            lambda i, j: (
                form.q(generators[i])
                if i == j
                else form.b(generators[i], generators[j])
            ),
        )
        return TorsionQuadraticForm(gram)

    checked = 0
    for H in D.isotropic_subgroups():
        if H.cardinality() == 1:
            continue
        overlattice_form = as_finite_quadratic_form(
            D.discriminant_form_of_overlattice(H)
        )
        quotient_form = as_finite_quadratic_form(D.orthogonal_quotient(H))  # H^perp / H
        # A form-preserving group isomorphism exists (explicit search), AND the complete
        # genus normal form (Nikulin-Conway-Sloane-Miranda-Morrison) agrees -- either
        # certifies the isometry; together they cross-check.
        assert overlattice_form.is_isomorphic(quotient_form, kind="quadratic")
        assert (
            overlattice_form.miranda_morrison_normal_form()
            == quotient_form.miranda_morrison_normal_form()
        )
        checked += 1
    assert checked > 0

    # metabolizer: a metabolizer is a Lagrangian, i.e. a self-orthogonal isotropic
    # subgroup H = H^perp. Verify that DEFINING content directly -- q|_H = 0 and
    # H = H^perp computed independently -- not the |H|^2 = |A| identity, which the
    # lagrangian filter already guarantees by construction (so it proves nothing).
    for gram in (
        matrix(ZZ, 2, 2, [0, 2, 2, 0]),  # U(2)
        matrix(
            ZZ, 4, 4, [0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0]
        ),  # U(2) + U(2)
    ):
        A = Lattice(gram).discriminant_group()
        assert A.is_metabolic()
        H = A.metabolizer()
        # H is isotropic: the quadratic form vanishes on it (values in QQ/2ZZ).
        assert all(A.q(h) == 0 for h in H.elements())
        # H equals its own orthogonal complement (the Lagrangian property).
        assert set(A.orthogonal(H).elements()) == set(H.elements())


def test_orthogonal_group_is_lazily_computed_for_definite_and_explicit_for_indefinite():
    from sage.all import MatrixGroup

    A2 = Lattice("A2(-1)", label="A2")

    # O(L) generators are computed lazily for a definite lattice and actually
    # generate O(A2) (the dihedral group of order 12).
    O_A2 = A2.isometry_group()
    gens = O_A2.gens()
    assert all(g.is_isometry() for g in gens)
    for g in gens:
        U = g.matrix()
        assert (
            U.transpose() * A2.gram_matrix() * U == A2.gram_matrix()
        )  # form-preserving
        assert U.det() in (1, -1)
    assert MatrixGroup([g.matrix() for g in gens]).order() == 12
    assert O_A2.order() == 12 and O_A2.is_finite()

    # is_isometry separates isomorphisms from mere form-preservation: the metric
    # inclusion A2 -> A2# is form-preserving (matrix G) but not an isometry (det 3).
    A2_dual = A2.dual()
    assert not A2.hom(A2.gram_matrix(), codomain=A2_dual).is_isometry()
    assert A2.hom(identity_matrix(ZZ, 2)).is_isometry()

    U = Lattice("U", label="U")
    O_U = U.isometry_group()
    swap_isometry = U.hom(matrix(ZZ, 2, 2, [0, 1, 1, 0]))
    assert swap_isometry.is_isometry() and swap_isometry in O_U

    # is_isometric: definite decided via Sage; different class / rank -> False;
    # rank-2 indefinite is the excluded binary case of the G1 routing table.
    assert A2.is_isometric(Lattice("A2(-1)", label="other"))
    assert not A2.is_isometric(Lattice(matrix(ZZ, 2, 2, [2, 0, 0, 2])))
    assert not A2.is_isometric(Lattice(matrix(ZZ, 3, 3, [2, 0, 0, 0, 2, 0, 0, 0, 2])))


def test_g1_indefinite_is_isometric_decides_via_sage_spinor_stack():
    # G1 engine (gap-ledger entry 1, Rulings round 3). Mathematical basis:
    # SPLAG Ch. 15 [CS10, Zotero T2WVLTDB] — Theorem 14 (Eichler: indefinite
    # rank >= 3 class = spinor genus) and section 9 (spinor kernel). Expected
    # values below come from the cited extraction or the Sage oracle only.
    from sage.quadratic_forms.genera.genus import Genus
    from sage.matrix.constructor import diagonal_matrix

    # (i) witness-based positive controls: T unimodular => T G T^t is the same
    # class, and the engine must say so through the genus/spinor route.
    G = diagonal_matrix(ZZ, [1, 1, -3, -5])
    L = Lattice(G, label="L")
    T = matrix(ZZ, 4, 4, [1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 1, 1, 1, 0, 0, 1])
    assert T.det() in (1, -1)
    M = Lattice(T * G * T.transpose(), label="M")
    assert L.is_isometric(M) and M.is_isometric(L)

    # (iii) single-spinor fixture: the Sage oracle confirms the genus of G
    # carries a single improper spinor genus, so genus equality decides.
    assert Genus(G).spinor_generators(proper=False) == []

    # same signature pair, different genus (determinant 21 vs 15) -> False.
    assert not L.is_isometric(Lattice(diagonal_matrix(ZZ, [1, 1, -3, -7])))

    # rank-3 control through the same route.
    H = diagonal_matrix(ZZ, [1, -1, 3])
    S = matrix(ZZ, 3, 3, [1, 0, 1, 0, 1, 0, 1, 1, 2])
    assert S.det() in (1, -1)
    assert Genus(H).spinor_generators(proper=False) == []
    assert Lattice(H).is_isometric(Lattice(S * H * S.transpose()))

    # (ii) the SPLAG 2-spinor-genus fixture: forms (51a)/(51b) (SPLAG Ch. 15
    # section 11, det -128) lie in one genus that splits into two spinor
    # genera — two distinct classes (f and f*Delta(3)), hence NOT isometric.
    # Sage's stack cannot PLACE a form in its spinor genus, so the engine
    # refuses this decision by assertion instead of answering (round-2 ruling).
    splag_a = matrix(ZZ, 3, 3, [-1, 1, 0, 1, 63, 0, 0, 0, 2])
    splag_b = matrix(ZZ, 3, 3, [-9, 1, 0, 1, 7, 0, 0, 0, 2])
    genus_a, genus_b = Genus(splag_a), Genus(splag_b)
    # (iv) representatives() self-consistency oracle cross-check: one genus,
    # a nonempty improper spinor-generator set, exactly two class representatives.
    assert genus_a == genus_b
    assert genus_a.spinor_generators(proper=False) != []
    assert len(genus_a.representatives()) == 2

    # degenerate pairs recurse through the radical quotient: rad rank 1 with
    # quotient <2> in two different presentations is one isometry class ...
    assert Lattice(matrix(ZZ, 2, 2, [0, 0, 0, 2])).is_isometric(
        Lattice(matrix(ZZ, 2, 2, [2, 2, 2, 2]))
    )
    # ... and distinct rank-1 quotients (<2> vs <4>) separate.
    assert not Lattice(matrix(ZZ, 2, 2, [0, 0, 0, 2])).is_isometric(
        Lattice(matrix(ZZ, 2, 2, [0, 0, 0, 4]))
    )
    # rank <= 1 is decided by Gram equality.
    assert Lattice(matrix(ZZ, 1, 1, [5])).is_isometric(Lattice(matrix(ZZ, 1, 1, [5])))
    assert not Lattice(matrix(ZZ, 1, 1, [5])).is_isometric(
        Lattice(matrix(ZZ, 1, 1, [7]))
    )
    assert Lattice(matrix(ZZ, 0, 0, [])).is_isometric(Lattice(matrix(ZZ, 0, 0, [])))


def test_reflection_is_an_order_two_isometry_defined_only_for_anisotropic_vectors():
    # Spec: sigma_v(x) = x - (2 b(x,v)/q(v)) v, a member of End(L); q(v) = 0 is
    # a mathematical-hypothesis rejection (ValueError), not a missing feature.
    A2 = Lattice("A2(-1)", label="A2")
    e0, e1 = A2.gen(0), A2.gen(1)
    sigma = A2.reflection(e0)
    assert sigma(e0) == -e0
    assert A2.q(sigma(e1)) == A2.q(e1) and A2.b(sigma(e0), sigma(e1)) == A2.b(e0, e1)
    assert sigma(sigma(e0)) == e0 and sigma(sigma(e1)) == e1


def test_two_signal_placement_gates_dual_and_discriminant_vocabulary_by_stratum():
    # Axis 1 (definedness -> placement/absence): dual needs nondegeneracy;
    # discriminant/genus vocabulary needs integral + nondegenerate.
    # Axis 2 (computability -> abstract signal): declared contracts raise.
    A2 = Lattice("A2(-1)", label="A2")
    degenerate = Lattice(matrix(QQ, [[0, 0], [0, 0]]), label="deg")
    rational = Lattice(matrix(QQ, [[QQ(1) / 2]]), base_ring=QQ, label="half")

    for name in (
        "dual",
        "dual_inclusion",
        "discriminant_group",
        "genus",
        "same_genus",
        "glue",
        "maximal_overlattice",
        "local_modification",
    ):
        assert not (name in dir(degenerate))
    for name in ("discriminant_group", "genus", "same_genus", "glue"):
        assert not (name in dir(rational))
    assert ("dual" in dir(rational))

    assert A2.same_genus(A2) and A2.genus() == A2.genus()


def test_placement_matrix_both_directions_over_the_spec_fixture_set():
    # Spec section 8: for each fixture, exactly the vocabulary of its
    # categories resolves (declared-surface membership, both directions). Expected side:
    # constructor-proven category membership. Vocabulary side: the
    # declaration layer's own per-subcategory delta, projected mechanically —
    # the same projection the category installs ride on.
    from sage_lattice_category_spike.algebra import domain_algebra as da

    def vocabulary(domain_class):
        return tuple(
            sorted(name for name in vars(domain_class) if not name.startswith("_"))
        )

    # Hyperbolic/RootGenerated are axioms OF a subcategory; the bare
    # C.Hyperbolic() is a silent no-op returning C (the trap the old
    # spelling of the U(2) constructor test hit), so every path is scoped.
    # Membership is evaluated over each fixture's OWN base ring.
    refinements = (
        (lambda C: C.Nondegenerate(), da.NondegenerateLattice),
        (lambda C: C.Integral().Nondegenerate(), da.IntegralNondegenerateLattice),
        (lambda C: C.Definite(), da.DefiniteLattice),
        (lambda C: C.PositiveDefinite(), da.PositiveDefiniteLattice),
        (lambda C: C.Indefinite(), da.IndefiniteLattice),
        (lambda C: C.Indefinite().Hyperbolic(), da.HyperbolicLattice),
        (lambda C: C.Even().RootGenerated(), da.RootGeneratedLattice),
    )
    fixtures = (
        Lattice("A2(-1)", label="A2"),  # PD even
        Lattice("A2"),  # ND even (AG default)
        Lattice("U", label="U"),  # hyperbolic
        Lattice("U").twist(2),  # hyperbolic non-unimodular
        Lattice(matrix(QQ, [[0, 0], [0, 2]]), label="deg"),  # degenerate
        Lattice(
            matrix(QQ, [[QQ(1) / 2]]), base_ring=QQ, label="half"
        ),  # rank-1 over QQ, non-integral form
        Lattice(matrix(QQ, 0, 0), label="zero"),  # rank 0
    )
    for fixture in fixtures:
        base_category = Lattices(fixture.base_ring())
        for refine, domain_class in refinements:
            category = refine(base_category)
            expected = fixture in category
            for name in vocabulary(domain_class):
                assert (name in dir(fixture)) == expected, (
                    f"placement violation: {name!r} on {fixture} "
                    f"(member of {category}: {expected}, resolves: {(name in dir(fixture))})"
                )

    # Spec section 8 signal test: nondegenerate vocabulary does not resolve on
    # the degenerate fixture at all.
    assert not ("dual" in dir(fixtures[4]))


def test_named_constructors_route_through_the_category_entry_with_provenance():
    # Spec 1.4/6 + design ruling 2026-07-09: Lattices(R).from_gram_matrix is the
    # only entry point, and constructors live on Lattice itself — a lattice NAME
    # is construction data carrying the RootGenerated certificate, while a raw
    # Gram matrix never acquires it (provenance is never Gram-detected).
    from sage.combinat.root_system.cartan_matrix import CartanMatrix

    U2 = Lattice("U").twist(2)
    assert U2.gram_matrix() == matrix(QQ, [[0, 2], [2, 0]])
    # scoped spelling: Hyperbolic is an axiom of Indefinite; the bare
    # Lattices(ZZ).Hyperbolic() is a silent no-op returning the base category
    assert U2 in Lattices(ZZ).Indefinite().Hyperbolic()
    assert Lattice("A2") not in Lattices(ZZ).Indefinite().Hyperbolic()

    A2_root = Lattice("A2")
    assert A2_root in Lattices(ZZ).Even().RootGenerated()
    assert A2_root.cartan_type() == ("A", 2)
    # the same Gram WITHOUT the name does not carry the certificate
    assert Lattice(matrix(QQ, CartanMatrix(["A", 2]))) not in Lattices(ZZ).Even().RootGenerated()

    E8_neg = Lattice("E8")
    assert E8_neg.signature_pair() == (0, 8)
    assert E8_neg in Lattices(ZZ).Even().RootGenerated()

    composite = A2_root.direct_sum(Lattice("E8"))
    assert composite in Lattices(ZZ).Even().RootGenerated()


def test_rational_dual_is_the_canonical_self_identification():
    # Ratified 2026-07-03: over QQ the metric dual identifies with the space
    # itself along the nondegenerate form; dual is total on nondegenerate
    # lattices and involutive across both base rings.
    A2 = Lattice("A2(-1)", label="A2")
    V = A2.rationalization()
    assert V.dual() is V
    assert A2.dual().dual() == A2


def test_isometry_group_object_algebra_and_negative_definite_delegation():
    # Spec 3.2: O(L) is total, unique per lattice; elements are the End(L)
    # isometries with composition/inversion/power/order algebra.
    A2 = Lattice("A2(-1)", label="A2")
    O = A2.isometry_group()
    assert O is A2.isometry_group()  # unique per lattice
    s = A2.reflection(A2.gen(0))
    t = A2.reflection(A2.gen(1))
    assert s in O and t in O and (s * t) in O
    assert (s * t).order() == 3  # Coxeter element of W(A2) = S3, order h = 3
    assert s * s == O.one() and s**-1 == s and s.inverse() == s
    assert not s.is_unipotent() and O.one().is_unipotent()

    # O(L) = O(L(-1)): the negative-definite case sign-twists internally.
    assert Lattice("A2").isometry_group().order() == 12

    # the trivial rank-0 group is grounded by construction.
    zero_rank = Lattice(matrix(QQ, 0, 0, []))
    assert (
        zero_rank.isometry_group().is_finite()
        and zero_rank.isometry_group().order() == 1
    )


def test_endomorphisms_form_a_monoid_with_ring_like_predicates():
    # V0d amendment: End_Lat(L) = Hom(L, L) is the form-preserving composition
    # monoid; operations escaping into End_ZZ-Mod(L) are not exposed, but
    # ring-like predicates remain well-defined queries on endomorphisms.
    A2 = Lattice("A2(-1)", label="A2")
    s = A2.reflection(A2.gen(0))
    identity = A2.hom(identity_matrix(ZZ, 2))
    assert (
        identity.is_identity() and identity.is_idempotent() and identity.is_unipotent()
    )
    assert (
        not s.is_nilpotent()
    )  # no nonzero form-preserving endo of a nondegenerate lattice is
    assert not s.is_idempotent() and s.order() == 2
    assert not ("endomorphism_ring" in dir(A2))  # the ring object is not vocabulary


def test_bilinear_forms_carry_the_induced_diagonal_quadratic_form():
    # Placement ruling 2026-07-03: Bil(M) -> Quad(M) by b -> (x -> b(x, x)) is
    # always defined; only polarization needs 2 invertible. A standalone
    # bilinear form therefore answers q and the isotropy suite directly.
    from sage_lattice_category_spike.lattice_categories import (
        SyntheticBilinearDiscriminantForm,
        TorsionQuadraticForm,
    )

    B = SyntheticBilinearDiscriminantForm(matrix.diagonal(QQ, [QQ(1) / 2, QQ(1) / 3]))
    x, y = B.gen(0), B.gen(1)
    assert B.q(x) == B.b(x, x) and B.q(x + y) == B.b(x + y, x + y)
    assert not B.is_isotropic_element(x)
    assert B.is_isotropic_element(B.zero())

    # on the quadratic subcategory, q refines the diagonal: q(x) == b(x, x) mod ZZ
    D = TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(1) / 2]))
    z = D.gen(0)
    assert (D.q(z) - D.b(z, z)) in ZZ


def test_rational_isometry_decides_by_square_class_via_the_oracle():
    # Rank-1 rational quadratic forms are isometric iff their discriminants
    # agree up to squares (Serre, A Course in Arithmetic, Ch. IV); the
    # decision is computed by Sage's rational-equivalence test.
    half = Lattice(matrix(QQ, [[QQ(1) / 2]]), base_ring=QQ, label="half")
    two = Lattice(matrix(QQ, [[2]]), base_ring=QQ, label="two")
    three_half = Lattice(matrix(QQ, [[QQ(3) / 2]]), base_ring=QQ, label="3/2")
    assert half.is_isometric(two)  # 2 / (1/2) = 4, a square
    assert not half.is_isometric(three_half)  # ratio 3, not a square
