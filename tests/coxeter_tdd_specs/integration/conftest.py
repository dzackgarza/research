"""
Integration test specific fixtures.

Integration tests use real implementations to test component interactions.
"""

import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def sage_available():
    """Check if Sage is available for integration tests."""
    try:
        import sage.all
        return True
    except ImportError:
        return False


@pytest.fixture
def skip_if_no_sage(sage_available):
    """Skip test if Sage is not available."""
    if not sage_available:
        pytest.skip("Sage not available for integration testing")


@pytest.fixture
def real_gram_matrix_constructor():
    """Real GramMatrix constructor (once implemented)."""
    def create_gram_matrix(coxeter_type):
        """Create real GramMatrix instance."""
        # This will import our actual implementation
        try:
            from coxeter_matrices import GramMatrix
            return GramMatrix.from_coxeter_type(coxeter_type)
        except ImportError:
            pytest.skip("GramMatrix implementation not yet available")
    
    return create_gram_matrix


@pytest.fixture
def real_root_system_constructor():
    """Real RootSystem constructor (once implemented)."""
    def create_root_system(coxeter_type):
        """Create real RootSystem instance."""
        try:
            from root_systems import RootSystem
            return RootSystem.from_coxeter_type(coxeter_type)
        except ImportError:
            pytest.skip("RootSystem implementation not yet available")
    
    return create_root_system


@pytest.fixture
def real_coxeter_group_constructor():
    """Real CoxeterGroup constructor (once implemented).""" 
    def create_coxeter_group(coxeter_type):
        """Create real CoxeterGroup instance."""
        try:
            from coxeter_groups import CoxeterGroup
            return CoxeterGroup.from_coxeter_type(coxeter_type)
        except ImportError:
            pytest.skip("CoxeterGroup implementation not yet available")
    
    return create_coxeter_group


@pytest.fixture
def integration_workflow():
    """Helper for testing complete integration workflows."""
    class WorkflowTester:
        def __init__(self):
            self.steps = []
            self.results = {}
        
        def add_step(self, name, func, *args, **kwargs):
            """Add a workflow step."""
            self.steps.append((name, func, args, kwargs))
        
        def execute(self):
            """Execute the complete workflow."""
            for name, func, args, kwargs in self.steps:
                try:
                    result = func(*args, **kwargs)
                    self.results[name] = result
                except Exception as e:
                    self.results[name] = {'error': str(e)}
            return self.results
        
        def verify_consistency(self):
            """Verify results are mathematically consistent."""
            # Add consistency checks between components
            return True
    
    return WorkflowTester


@pytest.fixture
def component_interaction_data():
    """Data for testing component interactions."""
    return {
        'constructor_chains': [
            # RootSystem → CoxeterGroup → WeylGroup
            {
                'start': 'root_system',
                'chain': ['coxeter_group', 'weyl_group'],
                'coxeter_type': ['A', 2]
            },
            # GramMatrix → RootSystem → CoxeterGroup
            {
                'start': 'gram_matrix', 
                'chain': ['root_system', 'coxeter_group'],
                'coxeter_type': ['B', 3]
            }
        ],
        'property_consistency': {
            # These properties should be consistent across components
            'rank': ['gram_matrix', 'root_system', 'coxeter_group', 'weyl_group'],
            'type': ['root_system', 'coxeter_group', 'weyl_group'],
            'order': ['coxeter_group', 'weyl_group']  # When finite
        }
    }


@pytest.fixture
def mathematical_consistency_checker():
    """Helper for verifying mathematical consistency between components."""
    class ConsistencyChecker:
        def __init__(self):
            self.checks = []
        
        def check_rank_consistency(self, *objects):
            """Verify all objects have same rank."""
            ranks = [getattr(obj, 'rank', None) for obj in objects]
            ranks = [r for r in ranks if r is not None]
            return len(set(ranks)) <= 1
        
        def check_type_consistency(self, *objects):
            """Verify all objects have same Coxeter type."""
            types = [getattr(obj, 'coxeter_type', None) for obj in objects]
            types = [t for t in types if t is not None] 
            return len(set(map(tuple, types))) <= 1
        
        def check_order_consistency(self, coxeter_group, weyl_group):
            """Verify Coxeter and Weyl groups have same order."""
            if hasattr(coxeter_group, 'order') and hasattr(weyl_group, 'order'):
                return coxeter_group.order == weyl_group.order
            return True  # Skip if orders not available
        
        def check_gram_determinant_type(self, gram_matrix):
            """Verify Gram matrix determinant matches type classification."""
            det = gram_matrix.determinant()
            type_class = gram_matrix.type
            
            if type_class == 'finite':
                return det > 0
            elif type_class == 'affine':
                return det == 0
            elif type_class == 'hyperbolic':
                return det < 0
            return True
    
    return ConsistencyChecker


@pytest.fixture(autouse=True)
def integration_test_markers(request):
    """Automatically apply integration test marker."""
    if not any(mark.name == 'integration' for mark in request.node.iter_markers()):
        pytest.fail("Integration tests must be marked with @pytest.mark.integration")
    yield