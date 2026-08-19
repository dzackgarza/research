# Origin: gitclones/integral_lattice/cat/tests/test_lattice.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

# from __future__ import annotations

# import pytest
# from deal import ContractError  # type: ignore
# from hypothesis import given, settings
# from hypothesis import strategies as st
# from sage.all import ZZ, Matrix
# from sage.structure.element import Matrix as MatrixType

# from src.lattice import IntegralLattice

# from .conftest import integral_lattices, positive_definite_matrices


# class TestIntegralLattice:
#     """Tests for IntegralLattice using hypothesis for property-based testing."""

#     @given(positive_definite_matrices())
#     @settings(max_examples=50)
#     def test_determinant_is_positive(self, gram: MatrixType) -> None:
#         """Determinant of a positive definite matrix is always positive."""
#         lattice = IntegralLattice(gram_matrix=gram)
#         assert lattice.determinant() > 0

#     @given(positive_definite_matrices())
#     @settings(max_examples=50)
#     def test_rank_equals_matrix_size(self, gram: MatrixType) -> None:
#         """Rank equals the size of the Gram matrix."""
#         lattice = IntegralLattice(gram_matrix=gram)
#         assert lattice.rank == gram.nrows()

#     @given(integral_lattices(), integral_lattices())
#     @settings(max_examples=30)
#     def test_direct_sum_rank_is_additive(self, l1: IntegralLattice, l2: IntegralLattice) -> None:
#         """Rank of L1 ⊕ L2 equals rank(L1) + rank(L2)."""
#         direct = l1.direct_sum(l2)
#         assert direct.rank == l1.rank + l2.rank

#     @given(integral_lattices(), integral_lattices())
#     @settings(max_examples=30)
#     def test_direct_sum_determinant_is_multiplicative(
#         self, l1: IntegralLattice, l2: IntegralLattice
#     ) -> None:
#         """det(L1 ⊕ L2) = det(L1) * det(L2)."""
#         direct = l1.direct_sum(l2)
#         assert direct.determinant() == l1.determinant() * l2.determinant()

#     @given(positive_definite_matrices())
#     @settings(max_examples=30)
#     def test_inner_product_is_symmetric(self, gram: MatrixType) -> None:
#         """Inner product is symmetric: <x, y> = <y, x>."""
#         lattice = IntegralLattice(gram_matrix=gram)
#         n = lattice.rank
#         # Use fixed vectors for reproducibility within this test
#         x = list(range(1, n + 1))
#         y = list(range(n, 0, -1))
#         assert lattice.inner_product(x, y) == lattice.inner_product(y, x)

#     @given(positive_definite_matrices(), st.integers(min_value=-5, max_value=5))
#     @settings(max_examples=30)
#     def test_inner_product_is_bilinear(self, gram: MatrixType, scalar: int) -> None:
#         """Inner product is bilinear: <ax, y> = a<x, y>."""
#         lattice = IntegralLattice(gram_matrix=gram)
#         n = lattice.rank
#         x = [1] * n
#         y = [1] * n
#         ax = [scalar * xi for xi in x]
#         assert lattice.inner_product(ax, y) == scalar * lattice.inner_product(x, y)

#     @given(positive_definite_matrices())
#     @settings(max_examples=30)
#     def test_norm_is_nonnegative(self, gram: MatrixType) -> None:
#         """Norm is always non-negative for positive definite lattices."""
#         lattice = IntegralLattice(gram_matrix=gram)
#         n = lattice.rank
#         x = list(range(1, n + 1))
#         assert lattice.norm(x) >= 0

#     @given(positive_definite_matrices())
#     @settings(max_examples=30)
#     def test_zero_vector_has_zero_norm(self, gram: MatrixType) -> None:
#         """The zero vector has norm 0."""
#         lattice = IntegralLattice(gram_matrix=gram)
#         zero = [0] * lattice.rank
#         assert lattice.norm(zero) == 0

#     @given(positive_definite_matrices())
#     @settings(max_examples=30)
#     def test_nonzero_vector_has_positive_norm(self, gram: MatrixType) -> None:
#         """Non-zero vectors have positive norm in positive definite lattices."""
#         lattice = IntegralLattice(gram_matrix=gram)
#         n = lattice.rank
#         # e_1 = (1, 0, 0, ..., 0)
#         e1 = [1] + [0] * (n - 1)
#         assert lattice.norm(e1) > 0

#     def test_identity_lattice_determinant_is_one(self) -> None:
#         """The identity lattice Z^n has determinant 1."""
#         for n in [1, 2, 3, 5, 10]:
#             lattice = IntegralLattice.identity(n)
#             assert lattice.determinant() == 1
#             assert lattice.is_unimodular()

#     def test_inner_product_on_identity_is_dot_product(self) -> None:
#         """On Z^n with identity Gram matrix, inner product is standard dot product."""
#         lattice = IntegralLattice.identity(3)
#         x = [1, 2, 3]
#         y = [4, 5, 6]
#         # Standard dot product: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
#         assert lattice.inner_product(x, y) == 32

#     def test_norm_on_identity_is_squared_euclidean(self) -> None:
#         """On Z^n with identity Gram matrix, norm is squared Euclidean norm."""
#         lattice = IntegralLattice.identity(3)
#         x = [3, 4, 0]
#         # ||x||^2 = 9 + 16 + 0 = 25
#         assert lattice.norm(x) == 25

#     def test_a2_root_lattice(self) -> None:
#         """
#         Test the A2 root lattice.

#         The A2 lattice has Gram matrix [[2, -1], [-1, 2]] with determinant 3.
#         """
#         a2_gram = Matrix(ZZ, [[2, -1], [-1, 2]])
#         a2 = IntegralLattice(gram_matrix=a2_gram)
#         assert a2.rank == 2
#         assert a2.determinant() == 3
#         assert not a2.is_unimodular()

#     def test_e8_lattice_is_unimodular(self) -> None:
#         """
#         The E8 lattice is an even unimodular lattice of rank 8.

#         Using the standard E8 Cartan matrix.
#         """
#         e8_gram = Matrix(
#             ZZ,
#             [
#                 [2, -1, 0, 0, 0, 0, 0, 0],
#                 [-1, 2, -1, 0, 0, 0, 0, 0],
#                 [0, -1, 2, -1, 0, 0, 0, -1],
#                 [0, 0, -1, 2, -1, 0, 0, 0],
#                 [0, 0, 0, -1, 2, -1, 0, 0],
#                 [0, 0, 0, 0, -1, 2, -1, 0],
#                 [0, 0, 0, 0, 0, -1, 2, 0],
#                 [0, 0, -1, 0, 0, 0, 0, 2],
#             ],
#         )
#         e8 = IntegralLattice(gram_matrix=e8_gram)
#         assert e8.rank == 8
#         assert e8.determinant() == 1
#         assert e8.is_unimodular()

#     def test_deal_contract_rejects_non_symmetric(self) -> None:
#         """Deal contract should reject non-symmetric matrices."""

#         bad_matrix = Matrix(ZZ, [[1, 2], [3, 4]])
#         with pytest.raises(ContractError):
#             IntegralLattice(gram_matrix=bad_matrix)

#     def test_deal_contract_rejects_non_positive_definite(self) -> None:
#         """Deal contract should reject non-positive-definite matrices."""

#         # Symmetric but not positive definite (has negative eigenvalue)
#         bad_matrix = Matrix(ZZ, [[1, 2], [2, 1]])
#         with pytest.raises(ContractError):
#             IntegralLattice(gram_matrix=bad_matrix)

#     def test_from_matrix_roundtrip(self) -> None:
#         """Constructing from a matrix preserves the Gram matrix."""
#         original_gram = Matrix(ZZ, [[2, 1], [1, 2]])
#         lattice = IntegralLattice.from_matrix(original_gram)
#         assert lattice.gram_matrix == original_gram
#         assert lattice.gram_matrix == original_gram
