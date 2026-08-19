from __future__ import annotations

from sage.all import QQ, ZZ, matrix, vector
from src.backends.dawes_orbit_backend import (
    _assemble_witness_from_complement_data,
    _build_complement_decomposition,
    _combined_direct_sum_discriminant_isometry,
    _dawes_right_smith_transform,
    _gluing_subgroups_match,
    _induced_discriminant_action_from_gluing,
    _search_discriminant_form_isometries,
    induced_discriminant_action,
)
from src.lattices.lattices import Lattice


def _rank_one_lattice(gram_entry: int) -> Lattice:
    return Lattice.from_gram(matrix(ZZ, [[gram_entry]]))


def _dawes_u_plus_a3() -> Lattice:
    # Dawes Examples 2.2 and 2.6 use this exact Gram matrix.
    # Do not derive it from Sage's named A3 helpers: the sign convention differs.
    return Lattice.from_gram(
        matrix(
            ZZ,
            [
                [0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, -2, -1, 0],
                [0, 0, -1, -2, -1],
                [0, 0, 0, -1, -2],
            ],
        )
    )


def _a2_positive() -> Lattice:
    return Lattice.from_gram(matrix(ZZ, [[2, 1], [1, 2]]))


def _dawes_example_22_theta():
    return matrix(
        ZZ,
        [
            [11, 5, -11, -13, -9],
            [43, 21, -46, -51, -36],
            [1, 1, -1, -2, -2],
            [-9, -5, 10, 12, 8],
            [25, 12, -26, -30, -21],
        ],
    )


def _dawes_example_22_qhat_one():
    return matrix(
        ZZ,
        [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [-1, 1, 1, -1, 0],
            [0, 0, 0, 0, 1],
        ],
    )


def _dawes_example_22_qhat_two():
    return matrix(
        ZZ,
        [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [-5, 180, 45, 25, 34],
            [1, -36, -9, -5, -7],
        ],
    )


def _dawes_example_22_iota_one():
    return matrix(
        QQ,
        [
            [4, 1, 0, 0, 0],
            [4, 0, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [2, 1, 1, -1, 0],
            [-1, 0, 0, 0, 1],
        ],
    )


def _dawes_example_22_iota_two():
    return matrix(
        QQ,
        [
            [36, 1, 0, 0, 0],
            [144, 0, 1, 0, 0],
            [5, 0, 0, 1, 0],
            [-30, 180, 45, 25, 34],
            [83, -36, -9, -5, -7],
        ],
    )


def _dawes_example_22_psi():
    return matrix(
        ZZ,
        [
            [-2, -8, 2, -9],
            [-8, -30, 5, -36],
            [-1, -1, 1, -2],
            [22, 83, -18, 97],
        ],
    )


def _dawes_example_22_k1_gram():
    return matrix(
        ZZ,
        [
            [-2, -1, 1, -1],
            [-1, -2, 1, -1],
            [1, 1, -2, 1],
            [-1, -1, 1, -2],
        ],
    )


def _dawes_example_22_k2_gram():
    return matrix(
        ZZ,
        [
            [-54432, -13607, -7740, -10260],
            [-13607, -3402, -1935, -2565],
            [-7740, -1935, -1102, -1459],
            [-10260, -2565, -1459, -1934],
        ],
    )


def _dawes_example_26_k1_basis():
    return matrix(
        ZZ,
        [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ],
    )


def _dawes_example_26_k2_basis():
    return matrix(
        ZZ,
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 1, -2, 0],
            [0, 0, 0, 1],
        ],
    )


def _dawes_example_26_k1_gram():
    return matrix(
        ZZ,
        [
            [2, 0, 0, 0],
            [0, -2, -1, 0],
            [0, -1, -2, -1],
            [0, 0, -1, -2],
        ],
    )


def _dawes_example_26_k2_gram():
    return matrix(
        ZZ,
        [
            [0, 1, 0, 0],
            [1, -2, 3, -1],
            [0, 3, -6, 2],
            [0, -1, 2, -2],
        ],
    )


def _dawes_example_26_qgram_one():
    return matrix(
        ZZ,
        [
            [0, -1, 3, 2],
            [-1, 0, 2, 1],
            [1, 0, -2, -2],
            [-1, -1, 4, 3],
        ],
    )


def _dawes_example_26_qgram_two():
    return matrix(
        ZZ,
        [
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [0, 0, -1, -1],
            [-1, 0, -2, -3],
        ],
    )


def _dawes_example_26_barpsi():
    return matrix(
        ZZ,
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 3],
        ],
    )


def _dawes_example_26_barpsi_reduced():
    return matrix(ZZ, [[1, 1], [0, 3]])


def _discriminant_hom_from_matrix(domain, codomain, action):
    codomain_gens = codomain.gens()
    images = []
    for column in range(action.ncols()):
        image = codomain.zero()
        for row, generator in enumerate(codomain_gens):
            coefficient = int(action[row, column])
            if coefficient:
                image += coefficient * generator
        images.append(image)
    return domain.hom(codomain, images)


def _equal_mod_2z(left, right) -> bool:
    return ((QQ(left) - QQ(right)) / QQ(2)) in ZZ


def test_full_orthogonal_group_uses_vector_equivalence_backend() -> None:
    lattice = _rank_one_lattice(-2)
    vector_one = lattice((1,))
    vector_two = lattice((-1,))
    witness = lattice.orthogonal_group().find_vector_isometry(vector_one, vector_two)
    assert witness is not None
    assert list(witness * vector_one) == list(vector_two)
    assert lattice.orthogonal_group().vectors_are_equivalent(vector_one, vector_two)


def test_special_orthogonal_subgroup_blocks_the_determinant_minus_one_witness() -> None:
    lattice = _rank_one_lattice(-2)
    vector_one = lattice((1,))
    vector_two = lattice((-1,))
    subgroup = lattice.orthogonal_group().special_orthogonal_subgroup()
    assert not subgroup.vectors_are_equivalent(vector_one, vector_two)


def test_kernel_of_discriminant_action_blocks_nontrivial_discriminant_motion() -> None:
    lattice = _rank_one_lattice(-4)
    vector_one = lattice((1,))
    vector_two = lattice((-1,))
    assert lattice.orthogonal_group().vectors_are_equivalent(vector_one, vector_two)
    subgroup = lattice.orthogonal_group().kernel_of_discriminant_action()
    assert not subgroup.vectors_are_equivalent(vector_one, vector_two)


def test_plus_subgroup_uses_the_real_spinor_norm_predicate() -> None:
    lattice = Lattice.hyperbolic_plane()
    reflection_in_positive_two_root = matrix(ZZ, [[0, -1], [-1, 0]])
    assert reflection_in_positive_two_root in lattice.orthogonal_group()
    assert reflection_in_positive_two_root not in lattice.orthogonal_group().plus_subgroup()


def test_orthogonal_group_generators_use_public_column_action_convention() -> None:
    lattice = _a2_positive()
    generator = next(
        matrix_candidate
        for matrix_candidate in lattice.orthogonal_group().gens()
        if matrix_candidate != matrix_candidate.transpose()
    )
    gram = lattice.inner_product_matrix()
    assert generator in lattice.orthogonal_group()
    assert generator.transpose() * gram * generator == gram
    assert generator * gram * generator.transpose() != gram


def test_full_orthogonal_group_normalizes_nonsymmetric_vector_witness() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = lattice((1, -1, 0, 0, 0))
    vector_two = lattice((1, 0, 1, 0, 0))
    witness = lattice.orthogonal_group().find_vector_isometry(vector_one, vector_two)
    assert witness is not None
    assert witness in lattice.orthogonal_group()
    assert list(witness * vector_one) == list(vector_two)


def test_dawes_example_22_explicit_paper_witness_lies_in_stable_plus_subgroup() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = lattice((4, 4, 1, 2, -1))
    vector_two = lattice((36, 144, 5, -30, 83))
    theta = _dawes_example_22_theta()
    subgroup = lattice.orthogonal_group().kernel_of_discriminant_action().plus_subgroup()
    assert theta in lattice.orthogonal_group()
    assert list(theta * vector_one) == list(vector_two)
    assert theta in subgroup


def test_dawes_example_22_backend_finds_a_stable_plus_witness() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = lattice((4, 4, 1, 2, -1))
    vector_two = lattice((36, 144, 5, -30, 83))
    subgroup = lattice.orthogonal_group().kernel_of_discriminant_action().plus_subgroup()
    witness = subgroup.find_vector_isometry(vector_one, vector_two)
    assert witness is not None
    assert witness in subgroup
    assert list(witness * vector_one) == list(vector_two)


def test_dawes_example_22_exact_algorithm_21_data_matches_the_paper() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = vector(ZZ, [4, 4, 1, 2, -1])
    vector_two = vector(ZZ, [36, 144, 5, -30, 83])
    left = _build_complement_decomposition(lattice, vector_one)
    right = _build_complement_decomposition(lattice, vector_two)
    assert (
        _dawes_right_smith_transform(
            lattice,
            vector_one,
        )
        == _dawes_example_22_qhat_one()
    )
    assert (
        _dawes_right_smith_transform(
            lattice,
            vector_two,
        )
        == _dawes_example_22_qhat_two()
    )
    assert left.inclusion_matrix == _dawes_example_22_iota_one()
    assert right.inclusion_matrix == _dawes_example_22_iota_two()
    assert left.complement_lattice.inner_product_matrix() == _dawes_example_22_k1_gram()
    assert right.complement_lattice.inner_product_matrix() == _dawes_example_22_k2_gram()


def test_dawes_example_22_paper_complement_isometry_extends_to_paper_theta() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = vector(ZZ, [4, 4, 1, 2, -1])
    vector_two = vector(ZZ, [36, 144, 5, -30, 83])
    left = _build_complement_decomposition(lattice, vector_one)
    right = _build_complement_decomposition(lattice, vector_two)
    theta = _assemble_witness_from_complement_data(
        lattice,
        left,
        right,
        _dawes_example_22_psi(),
    )
    assert theta == _dawes_example_22_theta()
    discriminant_generator = vector(
        QQ,
        [QQ.zero(), QQ.zero(), QQ(3) / QQ(4), -QQ(1) / QQ(2), QQ(1) / QQ(4)],
    )
    assert all(entry in ZZ for entry in list(theta * discriminant_generator - discriminant_generator))
    assert induced_discriminant_action(lattice, theta) == matrix(ZZ, [[1]])


def test_dawes_example_22_algorithm_21_handles_opaque_black_box_subgroups() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = lattice((4, 4, 1, 2, -1))
    vector_two = lattice((36, 144, 5, -30, 83))
    theta = _dawes_example_22_theta()
    structured = lattice.orthogonal_group().kernel_of_discriminant_action().plus_subgroup()
    ambient_witness = lattice.orthogonal_group().find_vector_isometry(
        vector_one,
        vector_two,
    )
    subgroup = lattice.orthogonal_group().subgroup(
        None,
        lambda M, _structured=structured, _theta=theta: M in _structured and M * _theta == _theta * M,
    )
    assert ambient_witness is not None
    assert ambient_witness not in subgroup
    assert theta in subgroup
    witness = subgroup.find_vector_isometry(vector_one, vector_two)
    assert witness is not None
    assert witness in subgroup
    assert list(witness * vector_one) == list(vector_two)


def test_dawes_example_26_exact_algorithm_23_data_matches_the_paper() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = vector(ZZ, [1, -1, 0, 0, 0])
    vector_two = vector(ZZ, [1, 0, 1, 0, 0])
    left = _build_complement_decomposition(lattice, vector_one)
    right = _build_complement_decomposition(lattice, vector_two)
    assert left.inclusion_matrix[:, 1:] == _dawes_example_26_k1_basis()
    assert right.inclusion_matrix[:, 1:] == _dawes_example_26_k2_basis()
    assert left.complement_lattice.inner_product_matrix() == _dawes_example_26_k1_gram()
    assert right.complement_lattice.inner_product_matrix() == _dawes_example_26_k2_gram()
    smith_one = left.complement_lattice.inner_product_matrix().smith_form()[2]
    smith_two = right.complement_lattice.inner_product_matrix().smith_form()[2]
    assert smith_one == _dawes_example_26_qgram_one()
    assert smith_two == _dawes_example_26_qgram_two()
    assert list(left.complement_lattice.inner_product_matrix().smith_form()[0].diagonal()) == [1, 1, 2, 4]
    assert list(right.complement_lattice.inner_product_matrix().smith_form()[0].diagonal()) == [1, 1, 2, 4]


def test_dawes_example_26_theorem_23_hypotheses_hold_for_the_complements() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = vector(ZZ, [1, -1, 0, 0, 0])
    vector_two = vector(ZZ, [1, 0, 1, 0, 0])
    left = _build_complement_decomposition(lattice, vector_one).complement_lattice
    right = _build_complement_decomposition(lattice, vector_two).complement_lattice
    assert left.signature_pair() == (1, 3)
    assert right.signature_pair() == (1, 3)
    assert len([entry for entry in left.inner_product_matrix().smith_form()[0].diagonal() if entry != 1]) == 2
    assert len([entry for entry in right.inner_product_matrix().smith_form()[0].diagonal() if entry != 1]) == 2
    assert left.is_isometric_to(right)


def test_dawes_example_26_quadratic_form_formulas_match_the_paper() -> None:
    ambient_gram = _dawes_u_plus_a3().inner_product_matrix()
    x1 = vector(
        QQ,
        [QQ(3) / QQ(2), QQ(3) / QQ(2), QQ.one(), -QQ.one(), QQ(2)],
    )
    x2 = vector(
        QQ,
        [
            QQ(1) / QQ(2),
            QQ(1) / QQ(2),
            QQ(1) / QQ(4),
            -QQ(1) / QQ(2),
            QQ(3) / QQ(4),
        ],
    )
    y1 = vector(
        QQ,
        [QQ(1) / QQ(2), QQ.zero(), -QQ(1) / QQ(2), QQ.one(), -QQ.one()],
    )
    y2 = vector(
        QQ,
        [QQ.zero(), QQ.zero(), -QQ(1) / QQ(4), QQ(1) / QQ(2), -QQ(3) / QQ(4)],
    )
    for a in range(2):
        for b in range(4):
            lhs_one = ((a * x1 + b * x2) * ambient_gram * (a * x1 + b * x2).column())[0]
            rhs_one = -QQ(3) * a * a / QQ(2) - QQ(b * b) / QQ(4) - QQ(a * b)
            lhs_two = ((a * y1 + b * y2) * ambient_gram * (a * y1 + b * y2).column())[0]
            rhs_two = -QQ(3) * a * a / QQ(2) - QQ(3 * b * b) / QQ(4)
            assert _equal_mod_2z(lhs_one, rhs_one)
            assert _equal_mod_2z(lhs_two, rhs_two)


def test_dawes_example_26_gluing_condition_has_a_trivial_d_l_action_solution() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = vector(ZZ, [1, -1, 0, 0, 0])
    vector_two = vector(ZZ, [1, 0, 1, 0, 0])
    left = _build_complement_decomposition(lattice, vector_one)
    right = _build_complement_decomposition(lattice, vector_two)
    line_isometry = left.line_discriminant.hom(
        right.line_discriminant,
        [right.line_discriminant.gens()[0]],
    )
    witness_actions = []
    for complement_isometry in _search_discriminant_form_isometries(
        left.complement_discriminant,
        right.complement_discriminant,
    ):
        direct_sum_isometry = _combined_direct_sum_discriminant_isometry(
            left,
            right,
            line_isometry,
            complement_isometry,
        )
        if not _gluing_subgroups_match(left, right, direct_sum_isometry):
            continue
        witness_actions.append(
            _induced_discriminant_action_from_gluing(
                left,
                right,
                direct_sum_isometry,
            )
        )
    assert matrix(ZZ, [[1]]) in witness_actions


def test_dawes_example_26_matches_the_paper_subgroup_conclusions() -> None:
    lattice = _dawes_u_plus_a3()
    vector_one = lattice((1, -1, 0, 0, 0))
    vector_two = lattice((1, 0, 1, 0, 0))
    stable_subgroup = lattice.orthogonal_group().kernel_of_discriminant_action()
    assert stable_subgroup.vectors_are_equivalent(vector_one, vector_two)
    subgroup = stable_subgroup.special_plus_subgroup()
    witness = subgroup.find_vector_isometry(vector_one, vector_two)
    assert witness is not None
    assert witness in subgroup
    assert list(witness * vector_one) == list(vector_two)
