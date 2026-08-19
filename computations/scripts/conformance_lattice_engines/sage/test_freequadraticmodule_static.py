from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import FreeQuadraticModule, ZZ, matrix
from .conftest import assert_runtime_methods_covered

def test_freequadraticmodule_gram_matrix_on_submodule_basis():
    """
    method: gram_matrix

    gram_matrix() on a submodule equals B*A*B^T from basis B and ambient inner-product matrix A.
    Assertion: Computed Gram matrix matches direct hand calculation.
    """
    A = matrix(ZZ, [[2, 0], [0, 3]])
    M = FreeQuadraticModule(ZZ, 2, A)
    S = M.span_of_basis([[1, 1], [1, -1]])
    G = S.gram_matrix()
    expected = matrix(ZZ, [[5, -1], [-1, 5]])
    assert G == expected, f"FreeQuadraticModule.gram_matrix mismatch: actual={G}, expected={expected}"


def test_freequadraticmodule_discriminant_sign_convention_rank_two():
    """
    method: discriminant

    discriminant() uses the signed convention (-1)^r * det(gram_matrix()).
    Assertion: In rank 2, discriminant is negative of determinant.
    """
    M = FreeQuadraticModule(ZZ, 2, matrix(ZZ, [[2, 0], [0, 3]]))
    actual = M.discriminant()
    expected = -M.determinant()
    assert actual == expected, (
        f"FreeQuadraticModule.discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_freequadraticmodule_ambient_module_is_self_for_ambient():
    """
    method: ambient_module

    ambient_module() returns the top ambient free quadratic module.
    Assertion: For an ambient module object, ambient_module() is identity.
    """
    M = FreeQuadraticModule(ZZ, 2, matrix(ZZ, [[1, 0], [0, 1]]))
    actual = M.ambient_module()
    expected = M
    assert actual is expected, (
        f"FreeQuadraticModule.ambient_module identity mismatch: actual={actual}, expected={expected}"
    )


def test_freequadraticmodule_inner_product_matrix_returns_ambient_form():
    """
    method: inner_product_matrix

    inner_product_matrix() returns the ambient bilinear matrix A.
    Assertion: Returned matrix equals constructor matrix.
    """
    A = matrix(ZZ, [[2, 0], [0, 3]])
    M = FreeQuadraticModule(ZZ, 2, A)
    actual = M.inner_product_matrix()
    expected = A
    assert actual == expected, (
        f"FreeQuadraticModule.inner_product_matrix mismatch: actual={actual}, expected={expected}"
    )


def test_freequadraticmodule_determinant_matches_gram_det():
    """
    method: determinant

    determinant() equals det(gram_matrix()).
    Assertion: Determinant matches Gram determinant on ambient example.
    """
    M = FreeQuadraticModule(ZZ, 2, matrix(ZZ, [[2, 0], [0, 3]]))
    actual = M.determinant()
    expected = M.gram_matrix().det()
    assert actual == expected, (
        f"FreeQuadraticModule.determinant mismatch: actual={actual}, expected={expected}"
    )


def test_freequadraticmodule_zero_submodule_has_rank_zero():
    """
    method: zero_submodule

    zero_submodule() returns the zero submodule.
    Assertion: Zero submodule has rank 0.
    """
    M = FreeQuadraticModule(ZZ, 2, matrix(ZZ, [[2, 0], [0, 3]]))
    Z0 = M.zero_submodule()
    actual = Z0.rank()
    expected = 0
    assert actual == expected, (
        f"FreeQuadraticModule.zero_submodule rank mismatch: actual={actual}, expected={expected}"
    )


def test_freequadraticmodule_span_and_span_of_basis_agree_on_rank():
    """
    method: span

    span(gens) constructs a submodule from generators.
    Assertion: Two independent generators produce rank 2.
    """
    M = FreeQuadraticModule(ZZ, 3, matrix(ZZ, [[2, 0, 0], [0, 3, 0], [0, 0, 5]]))
    S1 = M.span([[1, 0, 0], [0, 1, 0]])
    actual = S1.rank()
    expected = 2
    assert actual == expected, f"FreeQuadraticModule.span rank mismatch: actual={actual}, expected={expected}"


def test_freequadraticmodule_span_of_basis_rank_two_on_independent_basis():
    """
    method: span_of_basis

    span_of_basis(basis) constructs a submodule from a basis.
    Assertion: Independent basis vectors produce rank 2.
    """
    M = FreeQuadraticModule(ZZ, 3, matrix(ZZ, [[2, 0, 0], [0, 3, 0], [0, 0, 5]]))
    S = M.span_of_basis([[1, 0, 0], [0, 1, 0]])
    actual = S.rank()
    expected = 2
    assert actual == expected, (
        f"FreeQuadraticModule.span_of_basis rank mismatch: actual={actual}, expected={expected}"
    )


def test_freequadraticmodule_ambient_vector_space_keeps_dimension():
    """
    method: ambient_vector_space

    ambient_vector_space() tensors the ambient module to a fraction field vector space.
    Assertion: Ambient vector-space dimension equals module degree.
    """
    M = FreeQuadraticModule(ZZ, 3, matrix(ZZ, [[2, 0, 0], [0, 3, 0], [0, 0, 5]]))
    V = M.ambient_vector_space()
    actual = V.dimension()
    expected = M.degree()
    assert actual == expected, (
        f"FreeQuadraticModule.ambient_vector_space dimension mismatch: actual={actual}, expected={expected}"
    )


def test_freequadraticmodule_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant FreeQuadraticModule runtime method
    should correspond to at least one explicit test method tag in this module.
    """
    sample = FreeQuadraticModule(ZZ, 2, matrix(ZZ, [[2, 0], [0, 3]]))
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.modules.free_quadratic_module",),
    )
