from __future__ import annotations

import sys

import pytest

import sage.all  # noqa: F401
from sage.all import libgap

from .conftest import assert_gap_methods_covered


GAP_CORE_METHODS = {
    "HermiteNormalFormIntegerMat",
    "HermiteNormalFormIntegerMatTransform",
    "SmithNormalFormIntegerMat",
    "SmithNormalFormIntegerMatTransforms",
    "NullspaceIntMat",
    "SolutionIntMat",
    "SolutionNullspaceIntMat",
    "BaseIntMat",
    "BaseIntersectionIntMats",
    "ComplementIntMat",
    "DeterminantIntMat",
    "LLLReducedBasis",
    "LLLReducedGramMat",
    "ShortestVectors",
    "OrthogonalEmbeddings",
}


def test_gap_hnf_recovers_expected_diagonal_form():
    """
    method: HermiteNormalFormIntegerMat

    Hermite normal form should preserve the row lattice.
    Assertion: Example matrix reduces to expected diagonal HNF.
    """
    actual = bool(libgap.eval("HermiteNormalFormIntegerMat([[2,4],[6,8]]) = [[2,0],[0,4]]"))
    expected = True
    assert actual == expected, f"HNF mismatch: actual={actual}, expected={expected}"


def test_gap_hnf_transform_normal_matches_hnf_and_rank():
    """
    method: HermiteNormalFormIntegerMatTransform

    Transform variant should expose normal form and rank metadata.
    Assertion: Returned normal matrix equals HNF and rank is 2.
    """
    actual = (
        bool(libgap.eval("HermiteNormalFormIntegerMatTransform([[2,4],[6,8]]).normal = [[2,0],[0,4]]")),
        int(libgap.eval("HermiteNormalFormIntegerMatTransform([[2,4],[6,8]]).rank")),
    )
    expected = (True, 2)
    assert actual == expected, f"HNF transform mismatch: actual={actual}, expected={expected}"


def test_gap_snf_returns_invariant_factor_diagonal():
    """
    method: SmithNormalFormIntegerMat

    Smith normal form encodes abelian invariants of the row module quotient.
    Assertion: Example matrix has SNF diag(2,4).
    """
    actual = bool(libgap.eval("SmithNormalFormIntegerMat([[2,4],[6,8]]) = [[2,0],[0,4]]"))
    expected = True
    assert actual == expected, f"SNF mismatch: actual={actual}, expected={expected}"


def test_gap_snf_transforms_include_correct_rank_and_normal():
    """
    method: SmithNormalFormIntegerMatTransforms

    Transform variant should include normal form and rank data.
    Assertion: Returned normal matrix equals SNF and rank is 2.
    """
    actual = (
        bool(libgap.eval("SmithNormalFormIntegerMatTransforms([[2,4],[6,8]]).normal = [[2,0],[0,4]]")),
        int(libgap.eval("SmithNormalFormIntegerMatTransforms([[2,4],[6,8]]).rank")),
    )
    expected = (True, 2)
    assert actual == expected, f"SNF transforms mismatch: actual={actual}, expected={expected}"


def test_gap_nullspace_finds_integer_relation():
    """
    method: NullspaceIntMat

    Nullspace basis vectors encode integer row dependencies.
    Assertion: For dependent rows, NullspaceIntMat returns expected relation basis.
    """
    actual = bool(libgap.eval("NullspaceIntMat([[1,2,3],[2,4,6]]) = [[2,-1]]"))
    expected = True
    assert actual == expected, f"NullspaceIntMat mismatch: actual={actual}, expected={expected}"


def test_gap_solutionintmat_solves_integral_linear_system():
    """
    method: SolutionIntMat

    SolutionIntMat solves x*M = b over integers.
    Assertion: Returned solution is exact for test system.
    """
    actual = bool(libgap.eval("SolutionIntMat([[1,2],[3,4]], [7,10]) = [1,2]"))
    expected = True
    assert actual == expected, f"SolutionIntMat mismatch: actual={actual}, expected={expected}"


def test_gap_solutionnullspace_returns_solution_and_kernel_basis():
    """
    method: SolutionNullspaceIntMat

    SolutionNullspaceIntMat returns [solution, nullspace-basis].
    Assertion: For full-rank system, nullspace part is empty.
    """
    actual = bool(libgap.eval("SolutionNullspaceIntMat([[1,2],[3,4]], [7,10]) = [[1,2],[]]"))
    expected = True
    assert actual == expected, f"SolutionNullspaceIntMat mismatch: actual={actual}, expected={expected}"


def test_gap_baseintmat_produces_basis_of_row_module():
    """
    method: BaseIntMat

    BaseIntMat removes dependent generators while preserving row module.
    Assertion: Example basis equals expected reduced basis.
    """
    actual = bool(libgap.eval("BaseIntMat([[1,2,3],[2,4,6],[1,0,1]]) = [[1,0,1],[0,2,2]]"))
    expected = True
    assert actual == expected, f"BaseIntMat mismatch: actual={actual}, expected={expected}"


def test_gap_baseintersection_returns_expected_sublattice():
    """
    method: BaseIntersectionIntMats

    BaseIntersectionIntMats computes intersection of two row lattices.
    Assertion: Intersection equals 2Z x 2Z in sample.
    """
    actual = bool(
        libgap.eval("BaseIntersectionIntMats([[2,0],[0,2]], [[1,1],[1,-1]]) = [[2,0],[0,2]]")
    )
    expected = True
    assert actual == expected, f"BaseIntersectionIntMats mismatch: actual={actual}, expected={expected}"


def test_gap_complementintmat_returns_direct_summand_data():
    """
    method: ComplementIntMat

    ComplementIntMat computes complement data for a sublattice.
    Assertion: Returned record has 2-row complement and preserves given submodule.
    """
    actual = bool(
        libgap.eval(
            "Length(ComplementIntMat([[1,0,0],[0,1,0],[0,0,1]], [[1,1,0]]).complement) = 2 "
            "and ComplementIntMat([[1,0,0],[0,1,0],[0,0,1]], [[1,1,0]]).sub = [[1,1,0]]"
        )
    )
    expected = True
    assert actual == expected, f"ComplementIntMat mismatch: actual={actual}, expected={expected}"


def test_gap_determinantintmat_matches_exact_determinant():
    """
    method: DeterminantIntMat

    DeterminantIntMat computes exact integer determinant.
    Assertion: det([[1,2],[3,4]]) = -2.
    """
    actual = int(libgap.eval("DeterminantIntMat([[1,2],[3,4]])"))
    expected = -2
    assert actual == expected, f"DeterminantIntMat mismatch: actual={actual}, expected={expected}"


def test_gap_lll_reduced_basis_preserves_smith_normal_form():
    """
    method: LLLReducedBasis

    LLL basis change should preserve lattice module invariants.
    Assertion: SNF of input basis equals SNF of reduced basis.
    """
    actual = bool(
        libgap.eval(
            "SmithNormalFormIntegerMat([[1,1,1],[1,0,2],[1,2,3]]) = "
            "SmithNormalFormIntegerMat(LLLReducedBasis([[1,1,1],[1,0,2],[1,2,3]]).basis)"
        )
    )
    expected = True
    assert actual == expected, f"LLLReducedBasis invariant mismatch: actual={actual}, expected={expected}"


def test_gap_lll_reduced_gram_returns_conjugate_remainder():
    """
    method: LLLReducedGramMat

    LLLReducedGramMat returns transformation T and reduced remainder R.
    Assertion: R = T * G * TransposedMat(T) on sample Gram matrix.
    """
    actual = bool(
        libgap.eval(
            "LLLReducedGramMat([[2,1],[1,2]]).remainder = "
            "LLLReducedGramMat([[2,1],[1,2]]).transformation * [[2,1],[1,2]] * "
            "TransposedMat(LLLReducedGramMat([[2,1],[1,2]]).transformation)"
        )
    )
    expected = True
    assert actual == expected, f"LLLReducedGramMat mismatch: actual={actual}, expected={expected}"


def test_gap_shortestvectors_finds_minimal_shell():
    """
    method: ShortestVectors

    ShortestVectors should return vectors in the minimal norm shell.
    Assertion: For Gram 2*I_2 and bound 2, norms are exactly [2,2].
    """
    actual = bool(libgap.eval("ShortestVectors([[2,0],[0,2]], 2).norms = [2,2]"))
    expected = True
    assert actual == expected, f"ShortestVectors mismatch: actual={actual}, expected={expected}"


def test_gap_orthogonal_embeddings_identity_gram_has_standard_solution():
    """
    method: OrthogonalEmbeddings

    OrthogonalEmbeddings should include standard basis embedding for I_2.
    Assertion: Identity Gram returns vectors [1,0],[0,1] and encoded solution [1,2].
    """
    actual = bool(
        libgap.eval(
            "OrthogonalEmbeddings([[1,0],[0,1]]).vectors = [[1,0],[0,1]] and "
            "OrthogonalEmbeddings([[1,0],[0,1]]).solutions = [[1,2]]"
        )
    )
    expected = True
    assert actual == expected, f"OrthogonalEmbeddings mismatch: actual={actual}, expected={expected}"


def test_gap_core_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant GAP core method listed for this
    module should correspond to at least one explicit test method tag.
    """
    assert_gap_methods_covered(
        test_module=sys.modules[__name__],
        method_names=GAP_CORE_METHODS,
    )
