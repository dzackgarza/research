from __future__ import annotations

from itertools import product

import pytest

from sage.all import Matrix, Polyhedron, QQ, ZZ, identity_matrix, matrix
from sage.categories.modules import Modules

from sage_lattice_category_spike.lattice_categories import (
    DiscriminantGroups,
    Lattice,
    Lattices,
    QuadraticModules,
    RationalLattices,
    SyntheticGenus,
    SyntheticLattice,
)


def assert_matrix_equal(left, right):
    assert matrix(QQ, left) == matrix(QQ, right)


def test_category_axioms_bind_to_synthetic_lattice_contract():
    C = RationalLattices(ZZ)
    Q = QuadraticModules(ZZ)
    assert C is Lattices(ZZ)
    assert C.is_subcategory(Q)
    assert Modules(ZZ).WithBasis() in C.super_categories()
    assert C.Even().is_subcategory(C.Integral())
    assert C.Unimodular().is_subcategory(C.Integral())
    assert C.PositiveDefinite().is_subcategory(C.Definite())
    assert C.NegativeDefinite().is_subcategory(C.Definite())
    assert C.Embedded().WithDistinguishedBasis().is_subcategory(C.Embedded())
    assert C.WithDistinguishedBasis().Embedded().is_subcategory(C.WithDistinguishedBasis())

    D_category = DiscriminantGroups(ZZ)
    assert D_category.FiniteQuadraticForms().is_subcategory(D_category.FiniteBilinearForms())
    assert D_category.Even().is_subcategory(D_category.FiniteQuadraticForms())


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
    A2 = Lattice("A2", label="A2")
    minus_A2 = Lattice(-A2.gram_matrix(), label="-A2")
    radical = Lattice(matrix(QQ, 1, 1, [0]), label="rad")

    assert A2 in RationalLattices(ZZ).PositiveDefinite()
    assert A2 in RationalLattices(ZZ).WithDistinguishedBasis()
    assert A2 not in RationalLattices(ZZ).Embedded()
    assert minus_A2 in RationalLattices(ZZ).NegativeDefinite()
    assert Lattice("U", label="U") in RationalLattices(ZZ).Indefinite()
    assert radical in RationalLattices(ZZ).Symmetric()
    assert radical not in RationalLattices(ZZ).Nondegenerate()
    assert radical.signature_pair() == (0, 0)


def test_positive_definite_algorithms_are_axiom_gated():
    A2 = Lattice("A2", label="A2")
    U = Lattice("U", label="U")
    rank_one = Lattice(matrix(ZZ, 1, 1, [2]), label="<2>")
    rank_three = Lattice(matrix.diagonal(ZZ, [2, 4, 6]), label="<2,4,6>")

    reduced = A2.LLL()
    assert isinstance(reduced, SyntheticLattice)
    change_of_basis = matrix(ZZ, A2.gram_matrix()).LLL_gram()
    assert_matrix_equal(reduced.gram_matrix(), change_of_basis * A2.gram_matrix() * change_of_basis.transpose())
    assert reduced.determinant() == A2.determinant()
    assert reduced.discriminant() == A2.discriminant()
    G = matrix(ZZ, 3, 3, [4, 1, 1, 1, 3, 1, 1, 1, 2])
    G_lattice = Lattice(G, label="G")
    bkz_lattice = G_lattice.BKZ(block_size=2)
    assert_matrix_equal(bkz_lattice.gram_matrix(), matrix(ZZ, 3, 3, [2, 1, 1, 1, 3, 1, 1, 1, 4]))
    assert bkz_lattice.determinant() == G_lattice.determinant()
    assert bkz_lattice.discriminant() == G_lattice.discriminant()
    assert [[tuple(vector.coordinates()) for vector in vectors] for vectors in rank_one.short_vectors(5)] == [
        [(0,)],
        [],
        [(1,), (-1,)],
        [],
        [],
    ]
    short = A2.short_vectors(3)
    assert [[tuple(vector.coordinates()) for vector in vectors] for vectors in short] == [
        [(0, 0)],
        [],
        [(1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)],
    ]
    assert [[tuple(vector.coordinates()) for vector in vectors] for vectors in rank_three.short_vectors(7)] == [
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
        key=lambda vector: (
            (matrix(QQ, 1, 2, [vector.coordinates()[i] - target[i] for i in range(2)])
             * A2.gram_matrix()
             * matrix(QQ, 2, 1, [vector.coordinates()[i] - target[i] for i in range(2)]))[0, 0],
            tuple(vector.coordinates()),
        ),
    )
    assert A2.closest_vector(target) == brute_force == A2([1, 1])
    expected_ieqs = []
    for vectors in A2.short_vectors(3):
        for lattice_vector in vectors:
            if lattice_vector != A2.zero():
                column = matrix(QQ, 2, 1, list(lattice_vector.coordinates()))
                gram_vector = A2.gram_matrix() * column
                expected_ieqs.append([QQ(lattice_vector.q()) / 2] + [-gram_vector[i, 0] for i in range(2)])
    assert A2.voronoi_cell(radius=3) == Polyhedron(ieqs=expected_ieqs, base_ring=QQ)
    assert len(A2.voronoi_cell().vertices()) == 6

    for name in ("LLL", "BKZ", "short_vectors", "shortest_vector", "closest_vector", "voronoi_cell"):
        assert not hasattr(U, name)


def test_raw_module_methods_are_available_only_through_accessors():
    A2 = Lattice("A2", label="A2")

    for name in (
        "free_resolution",
        "graded_free_resolution",
        "pseudoHom",
        "pseudohom",
        "sparse_module",
        "dense_module",
        "subspaces",
        "quotient_abstract",
    ):
        assert not hasattr(A2, name)
    assert A2.underlying_module() is not A2
    assert A2.underlying_quadratic_module() is A2
    with pytest.raises(NotImplementedError):
        A2.underlying_quotient_module()


def test_rational_span_is_scalar_extension_not_external_ambient_embedding():
    U = Lattice("U", label="U")
    U_QQ = U.rational_span()

    assert U_QQ.base_ring() is QQ
    assert_matrix_equal(U_QQ.gram_matrix(), U.gram_matrix())
    assert_matrix_equal(U_QQ.basis_matrix(), U.basis_matrix())
    assert U_QQ.gen(0).b(U_QQ.gen(1)) == 1
    assert U.quadratic_form()(U([1, 1])) == 2


def test_elements_have_owned_module_arithmetic_and_bilinear_form():
    U = Lattice("U", label="U")
    e, f = U.gens()

    assert e + f == U([1, 1])
    assert 2 * e - f == U([2, -1])
    assert -(e + f) == U([-1, -1])
    assert (e + f).q() == 2


def test_rank_one_sublattice_uses_coordinate_membership_not_ambient_embedding():
    U = Lattice("U", label="U")
    diagonal = U.sublattice([[1, 1]], label="diag")

    assert diagonal.rank() == 1
    assert diagonal.gram_matrix() == matrix(QQ, 1, 1, [2])
    assert diagonal.is_submodule(U)
    assert not U.is_submodule(diagonal)


def test_dual_lattice_is_owned_fractional_zz_lattice():
    A2 = Lattice("A2", label="A2")
    A2_dual = A2.dual_lattice()

    assert A2.is_submodule(A2_dual)
    assert not A2_dual.is_integral()
    assert_matrix_equal(
        A2_dual.basis_matrix(),
        matrix(QQ, 2, 2, [QQ(1) / 3, QQ(2) / 3, 0, 1]),
    )
    assert_matrix_equal(
        A2_dual.gram_matrix(),
        matrix(QQ, 2, 2, [QQ(2) / 3, 1, 1, 2]),
    )
    assert A2_dual.dual_lattice() == A2


def test_span_overlattice_intersection_saturation_and_index_use_underlying_modules():
    U = Lattice("U", label="U")
    half_e = matrix(QQ, 1, 2, [QQ(1) / 2, 0])
    overlattice = U.overlattice(half_e, label="U_half_e")

    assert U.is_submodule(overlattice)
    assert overlattice.index_in(U) == QQ(1) / 2
    assert U.index_in(overlattice) == 2
    assert_matrix_equal(overlattice.basis_matrix(), matrix(QQ, 2, 2, [QQ(1) / 2, 0, 0, 1]))

    even_e = U.span([[2, 0], [0, 1]], label="even_e")
    assert_matrix_equal(even_e.saturation().basis_matrix(), U.basis_matrix())
    assert U.intersection(overlattice).basis_matrix() == U.basis_matrix()
    assert U.is_primitive(U.sublattice([[1, 0]], label="e"))


def test_orthogonal_direct_sum_and_tensor_product_constructions_are_synthetic():
    U = Lattice("U", label="U")
    e_line = U.sublattice([[1, 0]], label="e")
    complement = U.orthogonal_complement(e_line)

    assert complement.rank() == 1
    assert_matrix_equal(complement.basis_matrix(), matrix(QQ, 1, 2, [1, 0]))

    A2 = Lattice("A2", label="A2")
    direct = U.direct_sum(A2)
    assert direct.rank() == 4
    assert direct.signature_pair() == (3, 1)

    tensor = e_line.tensor_product(A2)
    assert tensor.rank() == 2
    assert_matrix_equal(tensor.gram_matrix(), matrix(QQ, 2, 2, [0, 0, 0, 0]))


def test_discriminant_group_is_owned_smith_quotient_with_forms():
    A2 = Lattice("A2", label="A2")
    D = A2.discriminant_group()

    assert D.invariants() == (3,)
    assert D.cardinality() == 3
    assert D.gen(0).q() == QQ(2) / 3
    assert D.gen(0) + 2 * D.gen(0) == D([0])
    assert D.lift(D.gen(0)).q() == QQ(2) / 3
    assert D.projection(D.lift(D.gen(0))) == D.gen(0)
    assert D.inner_product(D.gen(0), D.gen(0)) == QQ(2) / 3
    assert D.quadratic_product(D.gen(0)) == QQ(2) / 3
    assert D.value_module() == (QQ, ZZ)
    assert D.value_module_qf() == (QQ, 2 * ZZ)
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
    assert D.value_module() == (QQ, ZZ)
    assert D.value_module_qf() == (QQ, ZZ)
    assert D.gen(0).b(D.gen(0)) == QQ(1) / 3
    assert D.gen(0).q() == QQ(1) / 3
    with pytest.raises(ValueError):
        D.brown_invariant()


def test_discriminant_subgroups_actions_and_overlattice_construction_are_owned():
    L = Lattice(matrix(ZZ, 1, 1, [4]), label="<4>")
    D = L.discriminant_group()
    g = D.gen(0)
    H = D.submodule_with_gens([2 * g])

    assert H.cardinality() == 2
    assert H.is_bilinear_isotropic()
    assert not H.is_quadratic_isotropic()
    assert D.orthogonal_submodule_to(H).cardinality() == 2

    M = D.overlattice_from_isotropic_subgroup(H, label="<1>")
    assert_matrix_equal(M.gram_matrix(), matrix(QQ, 1, 1, [1]))

    primary = L.discriminant_group(primary=2)
    local = L.local_modification([2 * primary.gen(0)], 2, label="<1>_local")
    assert_matrix_equal(local.gram_matrix(), matrix(QQ, 1, 1, [1]))

    negation = D.orthogonal_group(gens=[matrix(ZZ, 1, 1, [-1])], check=True)[0]
    assert negation(g) == -g
    assert negation.preserves_form()


def test_homs_are_form_preserving_by_construction():
    U = Lattice("U", label="U")

    identity = U.Hom(U).from_matrix(identity_matrix(ZZ, 2))
    assert identity(U.gen(0)) == U.gen(0)
    assert identity(U.gen(0)).b(identity(U.gen(1))) == U.gen(0).b(U.gen(1))

    swap = U.Hom(U).from_matrix(matrix(ZZ, 2, 2, [0, 1, 1, 0]))
    assert swap(U.gen(0)) == U.gen(1)
    assert swap(U.gen(1)) == U.gen(0)

    with pytest.raises(ValueError):
        U.Hom(U).from_matrix(matrix(ZZ, 2, 2, [2, 0, 0, 1]))


def test_hom_image_and_kernel_are_synthetic_lattices():
    A2 = Lattice("A2", label="A2")
    A2_dual = A2.dual_lattice()
    inclusion = A2.Hom(A2_dual).from_matrix(Matrix(ZZ, 2, 2, [3, 0, -2, 1]))

    image = inclusion.image()
    kernel = inclusion.kernel()

    assert image.is_submodule(A2_dual)
    assert_matrix_equal(image.gram_matrix(), A2.gram_matrix())
    assert kernel.rank() == 0
    assert kernel.gram_matrix().nrows() == 0


def test_integral_lattice_inclusion_into_dual_is_a_synthetic_morphism():
    A2 = Lattice("A2", label="A2")
    A2_dual = A2.dual_lattice()
    inclusion = A2.Hom(A2_dual).from_matrix(Matrix(ZZ, 2, 2, [3, 0, -2, 1]))

    assert inclusion(A2.gen(0)).q() == A2.gen(0).q()


def test_explicit_isometries_act_on_discriminant_groups():
    U = Lattice("U", label="U")
    swap = matrix(ZZ, 2, 2, [0, 1, 1, 0])

    isometry = U.isometry_group(gens=[swap])[0]
    assert isometry(U.gen(0)) == U.gen(1)
    assert U.action_on_discriminant_group(gens=[swap])[0].is_identity()
    assert U.kernel_on_discriminant_group(gens=[swap]) == (isometry,)
