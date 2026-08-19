"""
Sage verification test specific fixtures.

These tests compare our implementations directly with Sage's canonical results.
"""

import pytest


@pytest.fixture(scope="session")
def sage_imports():
    """Import Sage modules needed for verification."""
    try:
        from sage.all import (
            RootSystem, WeylGroup, CoxeterMatrix, DynkinDiagram,
            matrix, ZZ, QQ, QuadraticField, CyclotomicField,
            IntegralLattice, SymmetricGroup
        )
        return {
            'RootSystem': RootSystem,
            'WeylGroup': WeylGroup, 
            'CoxeterMatrix': CoxeterMatrix,
            'DynkinDiagram': DynkinDiagram,
            'matrix': matrix,
            'ZZ': ZZ,
            'QQ': QQ,
            'QuadraticField': QuadraticField,
            'CyclotomicField': CyclotomicField,
            'IntegralLattice': IntegralLattice,
            'SymmetricGroup': SymmetricGroup
        }
    except ImportError:
        pytest.skip("Sage not available for verification tests")


@pytest.fixture
def sage_gram_matrix_factory(sage_imports):
    """Factory for creating Sage Gram matrices."""
    def create_sage_gram_matrix(coxeter_type):
        """Create Gram matrix using Sage's canonical construction."""
        R = sage_imports['RootSystem'](coxeter_type)
        simple_roots = R.root_lattice().simple_roots()
        
        # Build Gram matrix from inner products
        n = len(simple_roots)
        G = sage_imports['matrix'](sage_imports['QQ'], n, n)
        for i in range(n):
            for j in range(n):
                G[i, j] = simple_roots[i+1].inner_product(simple_roots[j+1])
        
        return G
    
    return create_sage_gram_matrix


@pytest.fixture 
def sage_root_system_factory(sage_imports):
    """Factory for creating Sage root systems."""
    def create_sage_root_system(coxeter_type):
        """Create root system using Sage."""
        return sage_imports['RootSystem'](coxeter_type)
    
    return create_sage_root_system


@pytest.fixture
def sage_weyl_group_factory(sage_imports):
    """Factory for creating Sage Weyl groups."""
    def create_sage_weyl_group(coxeter_type):
        """Create Weyl group using Sage."""
        return sage_imports['WeylGroup'](coxeter_type)
    
    return create_sage_weyl_group


@pytest.fixture
def sage_coxeter_matrix_factory(sage_imports):
    """Factory for creating Sage Coxeter matrices."""
    def create_sage_coxeter_matrix(coxeter_type):
        """Create Coxeter matrix using Sage."""
        return sage_imports['CoxeterMatrix'](coxeter_type)
    
    return create_sage_coxeter_matrix


@pytest.fixture
def sage_comparison_utilities(sage_imports):
    """Utilities for comparing our results with Sage."""
    class SageComparison:
        def __init__(self):
            self.sage = sage_imports
        
        def compare_matrices(self, our_matrix, sage_matrix, tolerance=None):
            """Compare our matrix with Sage matrix."""
            if tolerance is None:
                # Exact comparison
                return our_matrix == sage_matrix
            else:
                # Approximate comparison (when unavoidable)
                diff = our_matrix - sage_matrix
                return all(abs(entry) < tolerance for row in diff for entry in row)
        
        def compare_numerical_properties(self, our_obj, sage_obj, properties):
            """Compare numerical properties between objects."""
            results = {}
            for prop in properties:
                our_val = getattr(our_obj, prop, None)
                sage_val = getattr(sage_obj, prop, None)
                
                if our_val is not None and sage_val is not None:
                    if callable(our_val):
                        our_val = our_val()
                    if callable(sage_val):
                        sage_val = sage_val()
                    
                    results[prop] = our_val == sage_val
                else:
                    results[prop] = None  # Property not available for comparison
            
            return results
        
        def compare_group_orders(self, our_group, sage_group):
            """Compare group orders."""
            our_order = getattr(our_group, 'order', lambda: None)()
            sage_order = getattr(sage_group, 'order', lambda: None)()
            
            if our_order is not None and sage_order is not None:
                return our_order == sage_order
            return None
        
        def compare_root_systems(self, our_rs, sage_rs):
            """Compare root systems comprehensively."""
            comparisons = {}
            
            # Compare basic properties
            comparisons['rank'] = our_rs.rank == sage_rs.rank()
            comparisons['cartan_type'] = our_rs.coxeter_type == list(sage_rs.cartan_type())
            
            # Compare root counts
            our_positive_roots = len(our_rs.positive_roots)
            sage_positive_roots = len(sage_rs.root_lattice().positive_roots())
            comparisons['positive_root_count'] = our_positive_roots == sage_positive_roots
            
            # Compare Gram matrices
            our_gram = our_rs.gram_matrix
            sage_gram = self.create_sage_gram_matrix_from_roots(sage_rs)
            comparisons['gram_matrix'] = self.compare_matrices(our_gram, sage_gram)
            
            return comparisons
        
        def create_sage_gram_matrix_from_roots(self, sage_root_system):
            """Extract Gram matrix from Sage root system."""
            simple_roots = sage_root_system.root_lattice().simple_roots()
            n = len(simple_roots)
            G = self.sage['matrix'](self.sage['QQ'], n, n)
            
            for i in range(n):
                for j in range(n):
                    G[i, j] = simple_roots[i+1].inner_product(simple_roots[j+1])
            
            return G
    
    return SageComparison


@pytest.fixture
def sage_reference_data(sage_imports):
    """Generate reference data using Sage for specific test cases."""
    class SageReferenceGenerator:
        def __init__(self):
            self.sage = sage_imports
            self.cache = {}
        
        def get_reference_gram_matrix(self, coxeter_type):
            """Get reference Gram matrix from Sage."""
            key = tuple(coxeter_type)
            if key not in self.cache:
                R = self.sage['RootSystem'](coxeter_type)
                simple_roots = R.root_lattice().simple_roots()
                n = len(simple_roots)
                G = self.sage['matrix'](self.sage['QQ'], n, n)
                
                for i in range(n):
                    for j in range(n):
                        G[i, j] = simple_roots[i+1].inner_product(simple_roots[j+1])
                
                self.cache[key] = G
            
            return self.cache[key]
        
        def get_reference_properties(self, coxeter_type):
            """Get reference properties from Sage."""
            key = f"props_{tuple(coxeter_type)}"
            if key not in self.cache:
                R = self.sage['RootSystem'](coxeter_type)
                W = self.sage['WeylGroup'](coxeter_type)
                
                props = {
                    'rank': R.rank(),
                    'is_finite': R.is_finite(),
                    'is_affine': R.is_affine(),
                    'is_crystallographic': R.cartan_type().is_crystallographic(),
                    'positive_root_count': len(R.root_lattice().positive_roots()),
                    'weyl_group_order': W.order() if R.is_finite() else None
                }
                
                self.cache[key] = props
            
            return self.cache[key]
        
        def get_all_finite_types(self):
            """Get all finite irreducible Coxeter types from Sage."""
            # This would use Sage's classification
            finite_types = [
                ['A', 1], ['A', 2], ['A', 3], ['A', 4], ['A', 5],
                ['B', 2], ['B', 3], ['B', 4], ['B', 5],
                ['C', 2], ['C', 3], ['C', 4], ['C', 5],
                ['D', 4], ['D', 5], ['D', 6], ['D', 7],
                ['E', 6], ['E', 7], ['E', 8],
                ['F', 4],
                ['G', 2],
                ['H', 3], ['H', 4],
                ['I', 5], ['I', 6], ['I', 8], ['I', 12]
            ]
            return finite_types
    
    return SageReferenceGenerator


@pytest.fixture
def sage_cross_validation():
    """Complete cross-validation framework."""
    def validate_implementation(our_implementation_module, coxeter_types):
        """Cross-validate our implementation against Sage."""
        results = {}
        
        for coxeter_type in coxeter_types:
            type_key = tuple(coxeter_type)
            results[type_key] = {}
            
            # Test each component
            try:
                # Test GramMatrix
                our_gram = our_implementation_module.GramMatrix.from_coxeter_type(coxeter_type)
                sage_gram = create_sage_gram_matrix(coxeter_type)
                results[type_key]['gram_matrix'] = our_gram.data == sage_gram
                
                # Test RootSystem  
                our_rs = our_implementation_module.RootSystem.from_coxeter_type(coxeter_type)
                sage_rs = sage_imports['RootSystem'](coxeter_type)
                results[type_key]['root_system'] = compare_root_systems(our_rs, sage_rs)
                
                # Test other components...
                
            except Exception as e:
                results[type_key]['error'] = str(e)
        
        return results
    
    return validate_implementation


@pytest.fixture(autouse=True) 
def sage_verification_markers(request):
    """Automatically apply sage verification marker."""
    if not any(mark.name == 'sage' for mark in request.node.iter_markers()):
        pytest.fail("Sage verification tests must be marked with @pytest.mark.sage")
    yield