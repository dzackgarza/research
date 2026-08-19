"""
Unit tests for GramMatrix class.

Tests our GramMatrix implementation using real Sage data.
"""

import pytest
# REMOVED: Mock imports - using real Sage data instead
# from unittest.mock import Mock, patch, MagicMock


@pytest.mark.unit
@pytest.mark.fast
@pytest.mark.gram_matrices
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestGramMatrixConstructors:
    """Test GramMatrix constructor methods."""
    
    # CITATION: [Humphreys1990], [PROJECT_CONVENTIONS.md]
    # CONVENTION: Extract actual Gram matrix from Sage root system
    def test_from_coxeter_type_A2(self):
        """Test GramMatrix construction from Coxeter type A2 against Sage."""
        try:
            from coxeter_matrices import GramMatrix
            from sage.all import RootSystem
            
            # Construct using our implementation
            gram = GramMatrix.from_coxeter_type(['A', 2])
            
            # Get canonical Gram matrix from Sage's root system
            R = RootSystem(['A', 2])
            simple_roots = R.root_lattice().simple_roots()
            
            # Extract Gram matrix directly from Sage
            expected_gram = matrix([
                [simple_roots[i].scalar(simple_roots[j]) 
                 for j in [1, 2]] 
                for i in [1, 2]
            ])
            
            # Our convention: multiply by -2 to match our negative diagonal
            expected_gram_our_convention = -2 * expected_gram
            
            # Verify against Sage-extracted values
            assert matrix(gram.data) == expected_gram_our_convention
            assert gram.rank == R.rank()
            assert gram.determinant() == expected_gram_our_convention.det()
            assert gram.type == 'finite'
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")
    
    def test_from_coxeter_type_B3(self):
        """Test GramMatrix construction from Coxeter type B3."""
        try:
            from coxeter_matrices import GramMatrix
            
            gram = GramMatrix.from_coxeter_type(['B', 3])
            
            # B3 has mixed root lengths, so Gram matrix is more complex
            assert gram.rank == 3
            assert gram.type == 'finite' 
            # Exact matrix depends on our scaling convention
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")
    
    def test_from_simple_roots(self):
        """Test GramMatrix construction from simple roots."""
        try:
            from coxeter_matrices import GramMatrix
            from root_systems import SimpleRoot
            
            # Use real Sage A2 simple roots instead of mock data
            from sage.combinat.root_system.root_system import RootSystem
            R = RootSystem(['A', 2])
            sage_roots = R.root_lattice().simple_roots()
            
            # Use actual Sage A2 Gram matrix with negative diagonal convention
            root1, root2 = sage_roots
            
            # Create GramMatrix directly from real Sage data - no mocking
            gram = GramMatrix.from_simple_roots([root1, root2])
            
            # Get the canonical A2 matrix for comparison
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            expected_gram_A2 = get_expected_gram_for_test(['A', 2])
            
            assert gram.data == expected_gram_A2.list()
            
        except ImportError:
            pytest.skip("Implementation not yet available")


@pytest.mark.unit
@pytest.mark.fast  
@pytest.mark.gram_matrices
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestGramMatrixProperties:
    """Test GramMatrix mathematical properties using real implementations."""
    
    # CITATION: [Humphreys1990] Section 2.1, [PROJECT_CONVENTIONS.md]
    # CONVENTION: Test against Sage-extracted values, not formulas
    def test_A2_determinant_calculation(self):
        """Test determinant calculation for A2 Gram matrix against Sage."""
        try:
            from coxeter_matrices import GramMatrix
            from sage.all import RootSystem, matrix
            
            # Get the ACTUAL Gram matrix from Sage's root system
            R = RootSystem(['A', 2])
            roots = R.root_lattice().simple_roots()
            
            # Extract inner product matrix
            sage_gram = matrix([
                [roots[i].scalar(roots[j]) for j in [1, 2]]
                for i in [1, 2]
            ])
            
            # Apply our convention factor
            our_gram_data = (-2 * sage_gram).list()
            
            # Test our implementation with Sage-extracted data
            gram = GramMatrix(our_gram_data)
            
            # Verify determinant matches
            assert gram.determinant() == (-2 * sage_gram).det()
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")
    
    # CITATION: [BogachevKolpakov2024], [PROJECT_CONVENTIONS.md]
    # THEOREM: Eigenvalue classification determines Coxeter group type
    # CONVENTION: Our negative definite matrices indicate finite type
    def test_A2_eigenvalue_calculation(self):
        """Test eigenvalue calculation and finite type classification."""
        try:
            from coxeter_matrices import GramMatrix
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            
            # Get expected Gram matrix with our convention from Sage
            expected_gram = get_expected_gram_for_test(['A', 2])
            
            # Test our implementation
            gram = GramMatrix(expected_gram.list())
            eigenvals = gram.eigenvalues()
            
            # Verify eigenvalues match Sage's calculation
            expected_eigenvals = expected_gram.eigenvalues()
            assert len(eigenvals) == len(expected_eigenvals)
            assert set(eigenvals) == set(expected_eigenvals)
            assert all(ev < 0 for ev in eigenvals)  # Negative definite → finite
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")
    
    # CITATION: [BogachevKolpakov2024], [PerronFrobenius1907-1912], [PROJECT_CONVENTIONS.md]
    # THEOREM: Signature (p,q,r) classifies Coxeter groups
    # CONVENTION: Our finite types have signature (0,n,0) due to negative convention
    def test_signature_classification(self):
        """Test signature-based type classification for various types."""
        try:
            from coxeter_matrices import GramMatrix
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            
            # Test finite type (A2) - get from Sage
            expected_gram_A2 = get_expected_gram_for_test(['A', 2])
            gram_finite = GramMatrix(expected_gram_A2.list())
            sig_finite = gram_finite.signature()
            assert sig_finite == (0, 2, 0)  # All negative eigenvalues
            
            # Test affine type (A2~) - get from Sage
            expected_gram_A2_affine = get_expected_gram_for_test(['A', 2, 1])
            
            gram_affine = GramMatrix(expected_gram_A2_affine.list())
            sig_affine = gram_affine.signature()
            
            # Verify it's singular (determinant = 0)
            assert abs(gram_affine.determinant()) < 1e-10
            # Verify signature for affine type
            assert sig_affine == (0, 2, 1)  # Two negative, one zero
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")
    
    # CITATION: [Humphreys1990] Chapter 2
    # THEOREM: Rank equals dimension of the root system
    def test_rank_calculation(self):
        """Test rank calculation matches matrix dimension."""
        try:
            from coxeter_matrices import GramMatrix
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            
            # Test various ranks using Sage-extracted matrices
            expected_A1 = get_expected_gram_for_test(['A', 1])
            gram_A1 = GramMatrix(expected_A1.list())
            assert gram_A1.rank == 1
            
            expected_A2 = get_expected_gram_for_test(['A', 2])
            gram_A2 = GramMatrix(expected_A2.list())
            assert gram_A2.rank == 2
            
            expected_A3 = get_expected_gram_for_test(['A', 3])
            gram_A3 = GramMatrix(expected_A3.list())
            assert gram_A3.rank == 3
            
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")


@pytest.mark.unit
@pytest.mark.fast
@pytest.mark.gram_matrices  
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestGramMatrixValidation:
    """Test GramMatrix input validation."""
    
    # CITATION: research/wikiwand/coxeter_schlaefli_matrices.md
    # CONVENTION: Gram matrices are always symmetric (inner product property)
    # FACT: Schläfli matrices inherit symmetry from inner product definition
    def test_symmetric_matrix_validation(self):
        """Test validation of matrix symmetry."""
        try:
            from coxeter_matrices import GramMatrix
            
            # Create a non-symmetric matrix by corrupting a canonical one
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            canonical = get_expected_gram_for_test(['A', 2])
            
            # Make it non-symmetric
            non_symmetric_data = canonical.list()
            non_symmetric_data[0] = [-2, 1]  # First row
            non_symmetric_data[1] = [2, -2]  # Second row (different [1,0] element)
            
            # Should reject non-symmetric matrix
            with pytest.raises(ValueError, match="Matrix must be symmetric"):
                GramMatrix(non_symmetric_data)
            
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_negative_diagonal_convention(self):
        """Test our negative diagonal convention."""
        try:
            from coxeter_matrices import GramMatrix
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            
            # Get canonical matrix and flip its sign to violate convention
            canonical = get_expected_gram_for_test(['A', 2])
            positive_diagonal_data = (-canonical).list()  # Flip sign
            
            # Should reject positive diagonal entries
            with pytest.raises(ValueError, match="negative diagonal"):
                GramMatrix(positive_diagonal_data)
            
            # Should accept negative diagonal - use Sage-extracted matrix
            expected_A2 = get_expected_gram_for_test(['A', 2])
            gram = GramMatrix(expected_A2.list())
            assert gram.data == expected_A2.list()
            
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_integral_entries_requirement(self):
        """Test requirement for integral matrix entries."""
        try:
            from coxeter_matrices import GramMatrix
            from sage.all import QQ
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            
            # Get canonical matrix and scale by non-integer
            canonical = get_expected_gram_for_test(['A', 2])
            non_integral_data = (QQ(1)/QQ(2) * canonical).list()  # Scale by 1/2
            
            # Should reject non-integral entries
            with pytest.raises(ValueError, match="integral entries"):
                GramMatrix(non_integral_data)
            
        except ImportError:
            pytest.skip("Implementation not yet available")


@pytest.mark.unit
@pytest.mark.medium
@pytest.mark.gram_matrices
@pytest.mark.literature
@pytest.mark.wikiwand
@pytest.mark.tdd
@pytest.mark.not_implemented  
class TestGramMatrixLiteratureExamples:
    """Test GramMatrix using literature examples."""
    
    # CITATION: research/wikiwand/coxeter_schlaefli_matrices.md, [PROJECT_CONVENTIONS.md]
    # EXAMPLE: A2 triangle group with angles π/3, π/3, π/3
    # FACT: the Coxeter matrix M=[[1,3],[3,1]] has literature Schläfli matrix
    #       C_ij = -2cos(π/M_ij), so C = [[2,-1],[-1,2]] with eigenvalues 1 and 3.
    # CONVENTION: this project's Gram matrix is B = 2cos(π/M_ij) = -C = [[-2,1],[1,-2]],
    #       with eigenvalues -1 and -3. B is the NEGATIVE of the Schläfli matrix;
    #       determinants agree (det = 3) only because the rank is even.
    def test_wikiwand_triangle_example(self):
        """Test triangle example from Wikiwand Schläfli matrix article."""
        try:
            from coxeter_matrices import GramMatrix
            
            # Triangle group (3,3,3) = A2
            gram = GramMatrix.from_coxeter_type(['A', 2])
            
            # From Wikiwand: triangle has angles π/3, π/3, π/3
            # Coxeter diagram has edges of order 3
            # Verify against Sage-extracted values
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            expected_gram = get_expected_gram_for_test(['A', 2])
            assert gram.data == expected_gram.list()
            
            # Expected determinant from Sage
            assert gram.determinant() == expected_gram.det()
            
            # Expected type: finite
            assert gram.type == 'finite'
            
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_wikiwand_square_example(self):
        """Test square example from Wikiwand."""
        try:
            from coxeter_matrices import GramMatrix
            
            # Square corresponds to B2 or I2(4)
            gram = GramMatrix.from_coxeter_type(['I', 4])
            
            # I2(4) should be finite with order 8
            assert gram.type == 'finite'
            
        except ImportError:
            pytest.skip("Implementation not yet available")


@pytest.mark.unit
@pytest.mark.fast
@pytest.mark.gram_matrices
@pytest.mark.edge_case
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestGramMatrixEdgeCases:
    """Test GramMatrix edge cases and boundary conditions."""
    
    def test_rank_one_case(self):
        """Test rank 1 Gram matrix (A1)."""
        try:
            from coxeter_matrices import GramMatrix
            from sage.all import matrix, QQ
            from tests.helpers.sage_extraction import get_expected_gram_for_test
            
            # Get expected Gram matrix with our convention from Sage
            expected_gram = get_expected_gram_for_test(['A', 1])
            
            gram = GramMatrix.from_coxeter_type(['A', 1])
            
            assert matrix(QQ, gram.data) == expected_gram
            assert gram.rank == expected_gram.nrows()
            assert gram.determinant() == expected_gram.det()  # -2, not 2!
            assert gram.type == 'finite'
            
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_zero_determinant_affine(self):
        """Test affine type with zero determinant."""
        try:
            from coxeter_matrices import GramMatrix
            
            # Affine A1 tilde
            gram = GramMatrix.from_coxeter_type(['A', 1, 1])
            
            assert gram.determinant() == 0
            assert gram.type == 'affine'
            
        except ImportError:
            pytest.skip("Implementation not yet available")
    
    def test_hyperbolic_negative_determinant(self):
        """Test hyperbolic type with negative determinant."""
        try:
            from coxeter_matrices import GramMatrix
            
            # Some hyperbolic Coxeter group
            # This would need a specific example
            pytest.skip("Need specific hyperbolic example")
            
        except ImportError:
            pytest.skip("Implementation not yet available")