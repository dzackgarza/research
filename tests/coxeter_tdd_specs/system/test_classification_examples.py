"""
System tests for Coxeter group classification using literature examples.

Tests complete end-to-end workflows with proper mathematical citations.
"""

import pytest
from pathlib import Path
from tests.helpers.sage_canonical import get_canonical_types


@pytest.mark.system
@pytest.mark.slow
@pytest.mark.classification
@pytest.mark.literature
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestFiniteTypeClassification:
    """Test complete finite type classification system."""
    
    # CITATION: [Humphreys1990] Theorem 2.7.1, [PerronFrobenius1907-1912], [PROJECT_CONVENTIONS.md]
    # THEOREM: Finite iff standard Gram matrix is positive definite
    # CONVENTION: Our Gram matrix = -2 × standard, so finite iff NEGATIVE definite
    # FOUNDATION: Proof relies on Perron-Frobenius theory for spectral radius of non-negative matrices.
    @pytest.mark.parametrize("coxeter_type,rank", get_canonical_types('all'))
    def test_finite_type_negative_definite_criterion(self, coxeter_type, rank):
        """Test finite type classification by negative definite Gram matrix (our convention)."""
        try:
            from coxeter_systems import CoxeterSystem
            
            system = CoxeterSystem.from_coxeter_type(coxeter_type)
            gram = system.gram_matrix
            
            # Our criterion: ALL eigenvalues < 0 (negative definite due to -2× factor)
            eigenvals = gram.eigenvalues()
            assert all(ev < -1e-9 for ev in eigenvals)  # Numerical tolerance
            assert system.type == 'finite'
            assert system.rank == rank
                
        except ImportError:
            pytest.skip("CoxeterSystem implementation not yet available")
    
    # CITATION: research/wikipedia/coxeter_dynkin_diagrams.md
    # CLASSIFICATION: Exceptional finite types E6, E7, E8, F4, H3, H4, G2
    # FACT: Exceptional types have specific rank and order properties
    @pytest.mark.parametrize("coxeter_type,rank", get_canonical_types('exceptional'))
    def test_exceptional_finite_types(self, coxeter_type, rank):
        """Test exceptional finite Coxeter group properties."""
        try:
            from coxeter_systems import CoxeterSystem
            
            # Get expected values from Sage, not hard-coded
            from sage.all import WeylGroup, CoxeterMatrix
            
            # Get ground truth from Sage
            sage_weyl = WeylGroup(coxeter_type)
            sage_cm = CoxeterMatrix(coxeter_type)
            expected_rank = sage_cm.rank()
            expected_order = sage_weyl.order()
            
            # Test our implementation
            system = CoxeterSystem.from_coxeter_type(coxeter_type)
            
            # Verify properties match Sage
            assert system.rank == expected_rank
            assert system.rank == rank  # Verify against parametrized value
            assert system.type == 'finite'
            assert system.order() == expected_order
                
        except ImportError:
            pytest.skip("CoxeterSystem implementation not yet available")


@pytest.mark.system
@pytest.mark.slow
@pytest.mark.classification
@pytest.mark.literature
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestAffineTypeClassification:
    """Test complete affine type classification system."""
    
    # CITATION: [Humphreys1990] Theorem 4.3.1, [Davis2008] Theorem 6.3.1, [PerronFrobenius1907-1912], [PROJECT_CONVENTIONS.md]
    # THEOREM: Affine iff standard Gram matrix is positive semidefinite of corank 1
    # CONVENTION: Our Gram matrix = -2 × standard, so affine iff NEGATIVE semidefinite
    # FOUNDATION: Proof relies on Perron-Frobenius theory for the spectral radius.
    def test_affine_type_negative_semidefinite_criterion(self):
        """Test affine type classification by negative semidefinite Gram matrix (our convention)."""
        try:
            from coxeter_systems import CoxeterSystem
            
            # Test irreducible extended Dynkin diagrams (affine types)
            affine_types = [
                ['A', 2, 1],  # Ã₂
                ['B', 3, 1],  # B̃₃  
                ['D', 4, 1]   # D̃₄
            ]
            # Note: Ã₁ is reducible, so excluded for irreducible classification
            
            for coxeter_type in affine_types:
                system = CoxeterSystem.from_coxeter_type(coxeter_type)
                eigenvals = sorted(system.gram_matrix.eigenvalues(), reverse=True)
                
                # Our criterion: exactly one zero eigenvalue, others NEGATIVE (due to -2× factor)
                assert abs(eigenvals[0]) < 1e-9  # Largest eigenvalue is zero
                assert all(ev < -1e-9 for ev in eigenvals[1:])  # Others negative
                assert system.type == 'affine'
                
        except ImportError:
            pytest.skip("CoxeterSystem implementation not yet available")


@pytest.mark.system
@pytest.mark.slow
@pytest.mark.classification
@pytest.mark.hyperbolic
@pytest.mark.literature
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestHyperbolicTypeClassification:
    """Test hyperbolic type classification system."""
    
    # CITATION: [Davis2008] Theorem 7.1.1, [PROJECT_CONVENTIONS.md]
    # THEOREM: Compact hyperbolic iff standard Gram matrix has signature (n-1, 1, 0)
    # CONVENTION: Our Gram matrix = -2 × standard, so signature becomes (1, n-1, 0)
    def test_compact_hyperbolic_signature_criterion(self):
        """Test compact hyperbolic classification by Lorentzian signature."""
        try:
            from coxeter_systems import CoxeterSystem
            
            # Example: Triangle group [3,7] - known compact hyperbolic
            # Coxeter matrix M = [[1,3],[7,1]] gives hyperbolic group
            # For now, test with known hyperbolic system
            pytest.skip("Need CoxeterSystem.from_matrix() constructor for custom examples")
            
        except ImportError:
            pytest.skip("CoxeterSystem implementation not yet available")
    
    # CITATION: [BogachevKolpakov2024] Section 2, Example 1 
    # EXAMPLE: Non-reflective Lorentzian lattice with specific roots
    # FACT: f(x) = 3x₀² + 14x₀x₁ + 98x₀x₂ + 49x₂² gives non-reflective lattice
    def test_bogachev_kolpakov_nonreflective_example(self):
        """Test specific non-reflective lattice from Bogachev-Kolpakov paper."""
        try:
            from coxeter_systems import LorentzianLattice
            
            # Literature example with known roots
            pytest.skip("Need LorentzianLattice implementation for this example")
            
        except ImportError:
            pytest.skip("LorentzianLattice implementation not yet available")
    
    # CITATION: research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md
    # EXAMPLE: Non-reflective Lorentzian lattice with roots
    # FACT: Gram matrix f(x) = 3x₀² + 14x₀x₁ + 98x₀x₂ + 49x₂²
    def test_bogachev_kolpakov_example(self):
        """Test specific non-reflective lattice example from literature."""
        try:
            from coxeter_systems import LorentzianLattice
            from tests.helpers.sage_canonical import get_literature_example
            
            # Get literature example from canonical source
            example = get_literature_example('bogachev_kolpakov_2024_nonreflective')
            
            lattice = LorentzianLattice.from_gram_coefficients(example['gram_coeffs'])
            
            # Literature verification: this lattice is non-reflective
            assert not lattice.is_reflective()
            assert lattice.has_roots()  # But still has some roots
            
            # First few roots from paper
            expected_roots = example['roots']
            
            roots = lattice.enumerate_roots(len(expected_roots))
            assert len(roots) == len(expected_roots)
            
            for i, expected_root in enumerate(expected_roots):
                assert roots[i].coordinates == expected_root
                
        except ImportError:
            pytest.skip("LorentzianLattice implementation not yet available")


@pytest.mark.system
@pytest.mark.medium
@pytest.mark.literature
@pytest.mark.wikiwand
@pytest.mark.tdd
@pytest.mark.not_implemented
class TestSchlaefliMatrixExamples:
    """Test Schläfli matrix construction examples."""
    
    # CITATION: research/wikiwand/coxeter_schlaefli_matrices.md, [PROJECT_CONVENTIONS.md]
    # EXAMPLE: A₂ triangle with Coxeter matrix [[1,3],[3,1]]
    # CONVENTION: Our Gram matrix B = 2cos(π/M_ij) = [[-2,1],[1,-2]], eigenvalues [-3,-1]
    # FACT: the literature Schläfli matrix is C_ij = -2cos(π/M_ij) = [[2,-1],[-1,2]],
    #       eigenvalues [3,1]. Our B is the NEGATIVE of C, not equal to it: finite type
    #       reads as negative definite here and as positive definite in the literature.
    def test_A2_gram_construction(self):
        """Test A₂ Gram matrix construction: B is the negative of the literature Schläfli matrix."""
        try:
            from coxeter_matrices import CoxeterMatrix, GramMatrix
            
            # Get A₂ from Sage canonically
            from sage.all import matrix, QQ
            from tests.helpers.sage_extraction import extract_coxeter_matrix_from_sage, get_expected_gram_for_test
            
            # Use Sage's canonical A₂ Coxeter matrix
            sage_cm = extract_coxeter_matrix_from_sage(['A', 2])
            coxeter_matrix = CoxeterMatrix(sage_cm.list())
            gram = GramMatrix.from_coxeter_matrix(coxeter_matrix)
            
            # Get expected Gram matrix with our convention from Sage
            expected_gram = get_expected_gram_for_test(['A', 2])
            
            # Verify our implementation matches
            assert matrix(QQ, gram.data) == expected_gram
            
            # Verify eigenvalues match Sage's calculation
            eigenvals = gram.eigenvalues()
            expected_eigenvals = expected_gram.eigenvalues()
            assert set(eigenvals) == set(expected_eigenvals)
            
            # Verify determinant matches Sage
            assert gram.determinant() == expected_gram.det()
            
        except ImportError:
            pytest.skip("Matrix classes not yet available")