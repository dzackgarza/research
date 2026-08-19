import os
import sys

import pytest
from conftest import assert_equal, covered_methods_from_module

os.environ.setdefault("HOME", "/tmp/sage-home")
os.environ.setdefault("PYTHON_JULIAPKG_PROJECT", "/tmp/sage-home/julia_env")
os.environ.setdefault("JULIA_DEPOT_PATH", "/tmp/sage-home/.julia")

from juliacall import Main as jl


@pytest.fixture(scope="session", autouse=True)
def _init_julia_oscar() -> None:
    jl.seval("using Pkg")
    jl.seval('Pkg.activate("tests/julia_doc")')
    jl.seval("using Nemo")
    jl.seval("using Hecke")
    jl.seval("using Oscar")


def _jl_true(expr: str) -> bool:
    return bool(jl.seval(expr))


QUADFORM_AND_ISOM_MISSING_METHODS = {
    "primitive_embeddings",
    "primitive_embeddings(G::ZZGenus, M)",
    "primitive_extensions",
    "extend_to_ambient_space",
    "restrict_to_lattice",
    "special_orthogonal_group",
    "special_subgroup",
    "stable_orthogonal_group",
    "stable_subgroup",
    "stabilizer_discriminant_subgroup",
    "stabilizer_in_diagonal_action",
    "maximal_extension",
    "stabilizer_in_orthogonal_group",
    "pointwise_stabilizer_in_orthogonal_group",
    "setwise_stabilizer_in_orthogonal_group",
    "pointwise_stabilizer_orthogonal_complement_in_orthogonal_group",
    "is_isometry_list",
    "is_isometry_group",
    "is_stable_isometry",
    "is_special_isometry",
}


def test_primitive_embeddings_lattice_to_lattice():
    """
    method: primitive_embeddings
    """
    actual = _jl_true(
        "begin M = root_lattice(:A, 1); L1 = root_lattice(:A, 2); L2 = root_lattice(:A, 1); L = direct_sum(L1, L2)[1]; length(primitive_embeddings(L, M)) >= 1 end"
    )
    assert_equal(actual, True, f"primitive_embeddings(L, M) contract mismatch: actual={actual}, expected=True")


def test_primitive_embeddings_genus_overload():
    """
    method: primitive_embeddings(G::ZZGenus, M)
    """
    actual = _jl_true(
        "begin M = root_lattice(:A, 1); G = genus(root_lattice(:A, 2)); length(primitive_embeddings(G, M)) >= 0 end"
    )
    assert_equal(actual, True, f"primitive_embeddings(G::ZZGenus, M) contract mismatch: actual={actual}, expected=True")


def test_primitive_extensions_two_lattices():
    """
    method: primitive_extensions
    """
    actual = _jl_true(
        "begin L1 = root_lattice(:A, 1); L2 = root_lattice(:A, 1); length(primitive_extensions(L1, L2)) >= 1 end"
    )
    assert_equal(actual, True, f"primitive_extensions contract mismatch: actual={actual}, expected=True")


def test_extend_to_ambient_space_identity_round_trip():
    """
    method: extend_to_ambient_space
    """
    actual = _jl_true(
        "begin L = root_lattice(:A, 2); f = identity_matrix(ZZ, rank(L)); F = extend_to_ambient_space(L, f); nrows(F) == degree(L) && ncols(F) == degree(L) end"
    )
    assert_equal(actual, True, f"extend_to_ambient_space contract mismatch: actual={actual}, expected=True")


def test_restrict_to_lattice_inverse_of_extension_on_identity():
    """
    method: restrict_to_lattice
    """
    actual = _jl_true(
        "begin L = root_lattice(:A, 2); f = identity_matrix(ZZ, rank(L)); F = extend_to_ambient_space(L, f); R = restrict_to_lattice(L, F); R == f end"
    )
    assert_equal(actual, True, f"restrict_to_lattice contract mismatch: actual={actual}, expected=True")


def test_special_orthogonal_group_is_isometry_group():
    """
    method: special_orthogonal_group
    """
    actual = _jl_true("begin L = root_lattice(:A, 2); G = special_orthogonal_group(L); is_isometry_group(L, G) && order(G) > 0 end")
    assert_equal(actual, True, f"special_orthogonal_group contract mismatch: actual={actual}, expected=True")


def test_special_subgroup_refines_orthogonal_group():
    """
    method: special_subgroup
    """
    actual = _jl_true(
        "begin L = root_lattice(:A, 2); G = orthogonal_group(L); H = special_subgroup(G); order(H) > 0 && order(H) <= order(G) end"
    )
    assert_equal(actual, True, f"special_subgroup contract mismatch: actual={actual}, expected=True")


def test_stable_orthogonal_group_stabilizes_sublattice():
    """
    method: stable_orthogonal_group
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); S = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); G = stable_orthogonal_group(L, S); is_isometry_group(L, G) && order(G) > 0 end"
    )
    assert_equal(actual, True, f"stable_orthogonal_group contract mismatch: actual={actual}, expected=True")


def test_stable_subgroup_refines_orthogonal_group():
    """
    method: stable_subgroup
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); S = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); G = orthogonal_group(L); H = stable_subgroup(G, S); order(H) > 0 && order(H) <= order(G) end"
    )
    assert_equal(actual, True, f"stable_subgroup contract mismatch: actual={actual}, expected=True")


def test_stabilizer_discriminant_subgroup_refines_group_order():
    """
    method: stabilizer_discriminant_subgroup
    """
    actual = _jl_true(
        "begin L = root_lattice(:A, 2); G = orthogonal_group(L); T = discriminant_group(L); H = stabilizer_discriminant_subgroup(G, T); order(H) > 0 && order(H) <= order(G) end"
    )
    assert_equal(actual, True, f"stabilizer_discriminant_subgroup contract mismatch: actual={actual}, expected=True")


def test_stabilizer_in_diagonal_action_produces_finite_group():
    """
    method: stabilizer_in_diagonal_action
    """
    actual = _jl_true(
        "begin L1 = root_lattice(:A, 1); L2 = root_lattice(:A, 1); G = orthogonal_group(L1); H = stabilizer_in_diagonal_action(L1, L2, G); order(H) > 0 end"
    )
    assert_equal(actual, True, f"stabilizer_in_diagonal_action contract mismatch: actual={actual}, expected=True")


def test_maximal_extension_contains_input_group():
    """
    method: maximal_extension
    """
    actual = _jl_true(
        "begin L = root_lattice(:A, 2); G = special_orthogonal_group(L); H = maximal_extension(G); order(H) >= order(G) end"
    )
    assert_equal(actual, True, f"maximal_extension contract mismatch: actual={actual}, expected=True")


def test_stabilizer_in_orthogonal_group_refines_orthogonal_group():
    """
    method: stabilizer_in_orthogonal_group
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); S = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); G = stabilizer_in_orthogonal_group(L, S); is_isometry_group(L, G) && order(G) > 0 end"
    )
    assert_equal(actual, True, f"stabilizer_in_orthogonal_group contract mismatch: actual={actual}, expected=True")


def test_pointwise_stabilizer_in_orthogonal_group_nested_in_setwise():
    """
    method: pointwise_stabilizer_in_orthogonal_group
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); S = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); P = pointwise_stabilizer_in_orthogonal_group(L, S); Q = setwise_stabilizer_in_orthogonal_group(L, S); order(P) > 0 && order(P) <= order(Q) end"
    )
    assert_equal(actual, True, f"pointwise_stabilizer_in_orthogonal_group contract mismatch: actual={actual}, expected=True")


def test_setwise_stabilizer_in_orthogonal_group_refines_full_group():
    """
    method: setwise_stabilizer_in_orthogonal_group
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); S = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); H = setwise_stabilizer_in_orthogonal_group(L, S); G = orthogonal_group(L); order(H) > 0 && order(H) <= order(G) end"
    )
    assert_equal(actual, True, f"setwise_stabilizer_in_orthogonal_group contract mismatch: actual={actual}, expected=True")


def test_pointwise_stabilizer_orthogonal_complement_refines_group():
    """
    method: pointwise_stabilizer_orthogonal_complement_in_orthogonal_group
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); S = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); H = pointwise_stabilizer_orthogonal_complement_in_orthogonal_group(L, S); G = orthogonal_group(L); order(H) > 0 && order(H) <= order(G) end"
    )
    assert_equal(actual, True, f"pointwise_stabilizer_orthogonal_complement_in_orthogonal_group contract mismatch: actual={actual}, expected=True")


def test_is_isometry_list_recognizes_true_and_false_cases():
    """
    method: is_isometry_list
    """
    actual = _jl_true(
        "begin L = root_lattice(:A, 2); fs = [identity_matrix(ZZ, 2), -identity_matrix(ZZ, 2)]; gs = [identity_matrix(ZZ, 2), ZZ[2 0; 0 1]]; is_isometry_list(L, fs) && !is_isometry_list(L, gs) end"
    )
    assert_equal(actual, True, f"is_isometry_list contract mismatch: actual={actual}, expected=True")


def test_is_isometry_group_true_for_orthogonal_group():
    """
    method: is_isometry_group
    """
    actual = _jl_true("begin L = root_lattice(:A, 2); G = orthogonal_group(L); is_isometry_group(L, G) end")
    assert_equal(actual, True, f"is_isometry_group contract mismatch: actual={actual}, expected=True")


def test_is_stable_isometry_identity_stabilizes_sublattice():
    """
    method: is_stable_isometry
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); S = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); f = identity_matrix(ZZ, 2); is_stable_isometry(L, S, f) end"
    )
    assert_equal(actual, True, f"is_stable_isometry contract mismatch: actual={actual}, expected=True")


def test_is_special_isometry_distinguishes_det_sign():
    """
    method: is_special_isometry
    """
    actual = _jl_true(
        "begin L = root_lattice(:A, 2); f = identity_matrix(ZZ, 2); g = ZZ[-1 0; 0 1]; is_special_isometry(L, f) && !is_special_isometry(L, g) end"
    )
    assert_equal(actual, True, f"is_special_isometry contract mismatch: actual={actual}, expected=True")


def test_quadform_and_isom_missing_methods_coverage():
    """
    method: runtime_coverage

    Coverage guard: every declared missing QuadFormAndIsom method should have
    at least one explicit `method:`-tagged pytest in this module.
    """
    covered = covered_methods_from_module(sys.modules[__name__])
    missing = sorted(QUADFORM_AND_ISOM_MISSING_METHODS - covered)
    assert not missing, (
        "Coverage failure: uncovered QuadFormAndIsom methods found.\n"
        f"Declared methods: {sorted(QUADFORM_AND_ISOM_MISSING_METHODS)}\n"
        f"Covered methods: {sorted(covered)}\n"
        f"Missing methods: {missing}"
    )
