"""
Unit tests for fundamental matrix construction formulas.

Tests the core mathematical relationships between Coxeter and Gram matrices.
"""

import pytest
import math
from unittest.mock import Mock, patch


@pytest.mark.unit
@pytest.mark.fast
@pytest.mark.gram_matrices
@pytest.mark.mathematical_foundations
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestGramMatrixConstruction:
    """Test the fundamental construction of Gram matrices from Coxeter matrices."""
    
    # CITATION: [Humphreys1990] Section 2.1, [PROJECT_CONVENTIONS.md]
    # CONVENTION: Our Gram matrix B has entries B_ij = 2×cos(π/M_ij)
    # This differs from standard literature: B_ij = -cos(π/M_ij), B_ii = 1
    # Our convention: B_ii = 2×cos(π/1) = 2×(-1) = -2 (negative diagonal)
    # NOTE: Our matrix = -2 × standard geometric Gram matrix
    def test_gram_matrix_construction_formula(self):
        """Test Gram matrix constructed correctly from Coxeter matrix via cosine formula."""
        try:
            from coxeter_matrices import CoxeterMatrix, GramMatrix
            from sage.all import matrix
            from tests.helpers.sage_extraction import extract_coxeter_matrix_from_sage, get_expected_gram_for_test
            
            # Get canonical Coxeter matrix from Sage
            sage_cm = extract_coxeter_matrix_from_sage(['A', 2])
            # Convert to our CoxeterMatrix format using safe conversion
            coxeter_matrix = CoxeterMatrix(sage_cm.list())
            gram_matrix = GramMatrix.from_coxeter_matrix(coxeter_matrix)
            
            # Get expected Gram matrix from Sage
            expected_gram = get_expected_gram_for_test(['A', 2])
            
            # Verify our implementation matches Sage extraction
            assert matrix(gram_matrix.data) == expected_gram
            
        except ImportError:
            pytest.skip("Matrix classes not yet available")
    
    # CITATION: [Humphreys1990] Section 2.1, [PROJECT_CONVENTIONS.md]
    # CONVENTION: For infinite order (parallel mirrors), M_ij = ∞ gives B_ij = 2×cos(0) = 2
    def test_infinite_order_edge_convention(self):
        """Test infinite order edges give 2 in Gram matrix (our convention)."""
        try:
            from coxeter_matrices import CoxeterMatrix, GramMatrix
            
            # Affine case with infinite edge
            # Note: float('inf') or special handling may be needed
            pytest.skip("Need to determine infinite order representation in implementation")
            
        except ImportError:
            pytest.skip("Matrix classes not yet available")
    
    # CITATION: [Humphreys1990] Section 2.1, [PROJECT_CONVENTIONS.md]
    # CONVENTION: Order 2 edges (commuting generators) give B_ij = 2×cos(π/2) = 0
    def test_commuting_generators_convention(self):
        """Test order 2 edges (commuting generators) give 0 in Gram matrix."""
        try:
            from coxeter_matrices import CoxeterMatrix, GramMatrix
            from sage.all import matrix, ZZ
            
            # Disconnected components (order 2 = commuting)
            # Build a Coxeter matrix for two commuting generators
            # This represents A1 × A1 (two disconnected nodes)
            from tests.helpers.sage_extraction import extract_coxeter_matrix_from_sage
            # For reducible type, construct from block diagonal
            from sage.all import block_matrix
            cm_A1 = extract_coxeter_matrix_from_sage(['A', 1])
            # Build 2x2 Coxeter matrix for A1 × A1
            coxeter_data = [[1, 2], [2, 1]]  # Order 2 = commuting
            coxeter_matrix = CoxeterMatrix(coxeter_data)
            gram_matrix = GramMatrix.from_coxeter_matrix(coxeter_matrix)
            
            # For A1 × A1, we expect block diagonal with A1 blocks
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            expected_A1 = get_expected_gram_for_test(['A', 1])
            # Build block diagonal matrix
            expected = matrix.block_diagonal([expected_A1, expected_A1])
            
            # Verify our implementation matches expected
            assert matrix(gram_matrix.data) == expected
            
        except ImportError:
            pytest.skip("Matrix classes not yet available")


@pytest.mark.unit
@pytest.mark.fast
@pytest.mark.conventions
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestMatrixConventionVerification:
    """Test our matrix conventions match standard literature."""
    
    # CITATION: [Humphreys1990] Section 2.1, [PROJECT_CONVENTIONS.md]
    # CONVENTION: We use Gram matrices B = 2×cos(π/M_ij) with NEGATIVE diagonal entries,
    # NOT Cartan matrices A with positive diagonal. Our B = -2 × standard Gram matrix.
    def test_gram_vs_cartan_matrix_convention(self):
        """Test we use our specific Gram matrix convention with negative diagonal."""
        try:
            from coxeter_matrices import GramMatrix
            
            # A2 example: our convention gives [[-2, 1], [1, -2]]
            gram = GramMatrix.from_coxeter_type(['A', 2])
            
            # Our convention: POSITIVE off-diagonal for Gram matrices
            assert gram.get(0, 1) > 0  # Should be 1
            assert gram.get(1, 0) > 0  # Should be 1
            
            # NEGATIVE diagonal (key difference from standard)
            assert gram.get(0, 0) < 0  # Should be -2
            assert gram.get(1, 1) < 0  # Should be -2
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")
    
    # CITATION: [Humphreys1990] Section 2.7, [PerronFrobenius1907-1912], [PROJECT_CONVENTIONS.md]
    # THEOREM: Classification by definiteness applies to Gram matrices
    # CONVENTION: Our B = -2 × standard, so finite ⟺ negative definite (all eigenvalues < 0)
    # FOUNDATION: Classification relies on Perron-Frobenius theory for spectral analysis
    def test_classification_applies_to_gram_matrices(self):
        """Test that inverted eigenvalue classification applies to our Gram matrices."""
        try:
            from coxeter_matrices import GramMatrix
            
            # A2 Gram matrix should have negative eigenvalues (finite type)
            # Our convention: B = [[-2, 1], [1, -2]] has eigenvalues [-3, -1]
            gram = GramMatrix.from_coxeter_type(['A', 2])
            eigenvals = gram.eigenvalues()
            
            # For finite types with our convention: NEGATIVE definite (all eigenvalues < 0)
            # This inverts standard literature due to our -2× factor
            assert all(ev < 0 for ev in eigenvals)
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")


@pytest.mark.unit
@pytest.mark.fast
@pytest.mark.edge_cases
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestMatrixConstructionEdgeCases:
    """Test edge cases in matrix construction."""
    
    def test_rank_one_gram_matrix(self):
        """Test rank 1 case (A1) constructs correctly."""
        try:
            from coxeter_matrices import GramMatrix
            
            # A1: single generator
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            
            gram = GramMatrix.from_coxeter_type(['A', 1])
            expected_gram = get_expected_gram_for_test(['A', 1])
            
            assert gram.data == expected_gram.list()
            assert gram.rank == 1
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")
    
    def test_symmetric_matrix_property(self):
        """Test constructed Gram matrices are symmetric."""
        try:
            from coxeter_matrices import GramMatrix
            
            # Test B3 (non-trivial case)
            gram = GramMatrix.from_coxeter_type(['B', 3])
            
            # Verify symmetry
            for i in range(gram.rank):
                for j in range(gram.rank):
                    assert abs(gram.get(i, j) - gram.get(j, i)) < 1e-9
                    
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")