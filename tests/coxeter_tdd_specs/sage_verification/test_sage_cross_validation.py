"""
Cross-validation tests comparing our implementations with Sage.

These tests verify our results match Sage's canonical implementations exactly.
"""

import pytest


@pytest.mark.sage
@pytest.mark.medium
@pytest.mark.verification
@pytest.mark.requires_sage
@pytest.mark.not_implemented
class TestSageGramMatrixValidation:
    """Validate our GramMatrix implementation against Sage."""
    
    def test_gram_matrix_a_series_validation(self, sage_gram_matrix_factory, sage_comparison_utilities):
        """Validate A-series Gram matrices against Sage."""
        try:
            from coxeter_matrices import GramMatrix
            
            comp = sage_comparison_utilities()
            
            for n in range(1, 6):  # A1 through A5
                coxeter_type = ['A', n]
                
                # Create our Gram matrix
                our_gram = GramMatrix.from_coxeter_type(coxeter_type)
                
                # Create Sage reference
                sage_gram = sage_gram_matrix_factory(coxeter_type)
                
                # Compare matrices exactly
                assert comp.compare_matrices(our_gram.data, sage_gram), \
                    f"A{n} Gram matrix doesn't match Sage"
                
                # Compare determinants
                assert our_gram.determinant() == sage_gram.determinant(), \
                    f"A{n} determinant doesn't match Sage"
                
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_gram_matrix_exceptional_types_validation(self, sage_gram_matrix_factory, sage_comparison_utilities):
        """Validate exceptional type Gram matrices against Sage."""
        try:
            from coxeter_matrices import GramMatrix
            
            comp = sage_comparison_utilities()
            exceptional_types = [['E', 6], ['E', 7], ['E', 8], ['F', 4], ['G', 2]]
            
            for coxeter_type in exceptional_types:
                # Create our Gram matrix
                our_gram = GramMatrix.from_coxeter_type(coxeter_type)
                
                # Create Sage reference
                sage_gram = sage_gram_matrix_factory(coxeter_type)
                
                # Compare exactly
                assert comp.compare_matrices(our_gram.data, sage_gram), \
                    f"{coxeter_type} Gram matrix doesn't match Sage"
                
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_gram_matrix_field_extensions_validation(self, sage_imports):
        """Validate Gram matrices requiring field extensions."""
        try:
            from coxeter_matrices import GramMatrix
            
            # H3 requires golden ratio field
            our_gram_h3 = GramMatrix.from_coxeter_type(['H', 3])
            
            # Create Sage reference in appropriate field
            R_h3 = sage_imports['RootSystem'](['H', 3])
            simple_roots = R_h3.root_lattice().simple_roots()
            
            # Build Sage Gram matrix
            n = len(simple_roots)
            sage_gram_h3 = sage_imports['matrix'](sage_imports['QuadraticField'](5), n, n)
            for i in range(n):
                for j in range(n):
                    sage_gram_h3[i, j] = simple_roots[i+1].inner_product(simple_roots[j+1])
            
            # Compare in the field
            assert our_gram_h3.data == sage_gram_h3, "H3 Gram matrix doesn't match Sage"
            
        except ImportError:
            pytest.skip("Implementations not yet available")


@pytest.mark.sage
@pytest.mark.medium
@pytest.mark.verification
@pytest.mark.requires_sage
@pytest.mark.not_implemented
class TestSageRootSystemValidation:
    """Validate our RootSystem implementation against Sage."""
    
    def test_root_system_basic_properties_validation(self, sage_root_system_factory, sage_comparison_utilities):
        """Validate basic root system properties against Sage."""
        try:
            from root_systems import RootSystem
            
            comp = sage_comparison_utilities()
            test_types = [['A', 2], ['B', 3], ['C', 3], ['D', 4], ['G', 2]]
            
            for coxeter_type in test_types:
                # Create our root system
                our_rs = RootSystem.from_coxeter_type(coxeter_type)
                
                # Create Sage reference
                sage_rs = sage_root_system_factory(coxeter_type)
                
                # Compare basic properties
                comparisons = comp.compare_root_systems(our_rs, sage_rs)
                
                # All comparisons should pass
                for prop, matches in comparisons.items():
                    assert matches, f"{coxeter_type} property {prop} doesn't match Sage"
                
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_root_system_positive_roots_validation(self, sage_root_system_factory):
        """Validate positive root enumeration against Sage."""
        try:
            from root_systems import RootSystem
            
            test_types = [['A', 3], ['B', 2], ['G', 2]]
            
            for coxeter_type in test_types:
                # Create our root system
                our_rs = RootSystem.from_coxeter_type(coxeter_type)
                
                # Create Sage reference
                sage_rs = sage_root_system_factory(coxeter_type)
                sage_positive_roots = sage_rs.root_lattice().positive_roots()
                
                # Compare positive root counts
                assert len(our_rs.positive_roots) == len(sage_positive_roots), \
                    f"{coxeter_type} positive root count doesn't match Sage"
                
                # Compare individual roots (in coordinates)
                our_coords = [root.coordinates for root in our_rs.positive_roots]
                sage_coords = [root.to_vector() for root in sage_positive_roots]
                
                # Sort both lists for comparison
                our_coords_sorted = sorted(our_coords)
                sage_coords_sorted = sorted(sage_coords)
                
                assert our_coords_sorted == sage_coords_sorted, \
                    f"{coxeter_type} positive roots don't match Sage"
                
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_root_system_simple_root_inner_products(self, sage_root_system_factory):
        """Validate simple root inner products against Sage."""
        try:
            from root_systems import RootSystem
            
            for coxeter_type in [['A', 2], ['B', 3], ['C', 3], ['D', 4]]:
                # Create our root system
                our_rs = RootSystem.from_coxeter_type(coxeter_type)
                
                # Create Sage reference
                sage_rs = sage_root_system_factory(coxeter_type)
                sage_simple_roots = sage_rs.root_lattice().simple_roots()
                
                # Compare all pairwise inner products
                n = len(our_rs.simple_roots)
                for i in range(n):
                    for j in range(n):
                        our_inner = our_rs.simple_roots[i].inner_product(our_rs.simple_roots[j])
                        sage_inner = sage_simple_roots[i+1].inner_product(sage_simple_roots[j+1])
                        
                        assert our_inner == sage_inner, \
                            f"{coxeter_type} inner product ({i},{j}) doesn't match Sage"
                
        except ImportError:
            pytest.skip("Implementations not yet available")


@pytest.mark.sage
@pytest.mark.medium
@pytest.mark.verification
@pytest.mark.requires_sage
@pytest.mark.not_implemented
class TestSageWeylGroupValidation:
    """Validate our WeylGroup implementation against Sage."""
    
    def test_weyl_group_orders_validation(self, sage_weyl_group_factory, expected_finite_orders):
        """Validate Weyl group orders against Sage."""
        try:
            from weyl_groups import WeylGroup
            
            for coxeter_type_tuple, expected_order in expected_finite_orders.items():
                coxeter_type = list(coxeter_type_tuple)
                
                # Create our Weyl group
                our_wg = WeylGroup.from_coxeter_type(coxeter_type)
                
                # Create Sage reference
                sage_wg = sage_weyl_group_factory(coxeter_type)
                
                # Compare orders
                assert our_wg.order == sage_wg.order(), \
                    f"{coxeter_type} Weyl group order doesn't match Sage"
                
                # Also compare with expected value
                assert our_wg.order == expected_order, \
                    f"{coxeter_type} order doesn't match literature value"
                
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_weyl_group_longest_element_validation(self, sage_weyl_group_factory):
        """Validate longest element computation against Sage."""
        try:
            from weyl_groups import WeylGroup
            
            test_types = [['A', 2], ['B', 2], ['G', 2]]
            
            for coxeter_type in test_types:
                # Create our Weyl group
                our_wg = WeylGroup.from_coxeter_type(coxeter_type)
                
                # Create Sage reference
                sage_wg = sage_weyl_group_factory(coxeter_type)
                
                # Compare longest element properties
                our_longest = our_wg.longest_element
                sage_longest = sage_wg.long_element()
                
                # Compare lengths
                assert our_longest.length == sage_longest.length(), \
                    f"{coxeter_type} longest element length doesn't match Sage"
                
                # Compare action on simple roots
                for i, simple_root in enumerate(our_wg.simple_roots):
                    our_action = our_longest.act_on_root(simple_root)
                    sage_action = sage_longest.action(sage_wg.simple_roots()[i+1])
                    
                    assert our_action.coordinates == sage_action.to_vector(), \
                        f"{coxeter_type} longest element action doesn't match Sage"
                
        except ImportError:
            pytest.skip("Implementations not yet available")


@pytest.mark.sage
@pytest.mark.slow
@pytest.mark.verification
@pytest.mark.requires_sage
@pytest.mark.comprehensive
@pytest.mark.not_implemented
class TestSageComprehensiveValidation:
    """Comprehensive cross-validation with Sage across all components."""
    
    def test_comprehensive_finite_types_validation(self, sage_cross_validation, sage_reference_data):
        """Comprehensively validate all finite types against Sage."""
        try:
            import coxeter_project  # Our complete implementation module
            
            # Get all finite types from Sage
            ref_gen = sage_reference_data()
            finite_types = ref_gen.get_all_finite_types()
            
            # Cross-validate our entire implementation
            validation_results = sage_cross_validation(coxeter_project, finite_types)
            
            # All validations should pass
            failed_types = []
            for type_key, results in validation_results.items():
                if 'error' in results:
                    failed_types.append((type_key, results['error']))
                    continue
                
                for component, passed in results.items():
                    if not passed:
                        failed_types.append((type_key, f"{component} validation failed"))
            
            assert not failed_types, f"Validation failures: {failed_types}"
            
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_numerical_precision_validation(self, sage_imports):
        """Validate numerical precision against Sage."""
        try:
            from coxeter_matrices import GramMatrix
            
            # Test cases requiring high precision
            precision_test_cases = [
                (['H', 3], 'golden_ratio'),  # Requires √5
                (['H', 4], 'golden_ratio'),  # Requires √5
                (['I', 5], 'cyclotomic_5'),  # Requires cos(π/5)
                (['I', 12], 'cyclotomic_12') # Requires cos(π/12)
            ]
            
            for coxeter_type, field_name in precision_test_cases:
                # Create our Gram matrix
                our_gram = GramMatrix.from_coxeter_type(coxeter_type)
                
                # Create Sage reference with exact arithmetic
                R = sage_imports['RootSystem'](coxeter_type)
                simple_roots = R.root_lattice().simple_roots()
                n = len(simple_roots)
                
                # Determine appropriate field
                if field_name == 'golden_ratio':
                    field = sage_imports['QuadraticField'](5)
                elif field_name.startswith('cyclotomic_'):
                    k = int(field_name.split('_')[1])
                    field = sage_imports['CyclotomicField'](k)
                else:
                    field = sage_imports['QQ']
                
                sage_gram = sage_imports['matrix'](field, n, n)
                for i in range(n):
                    for j in range(n):
                        sage_gram[i, j] = simple_roots[i+1].inner_product(simple_roots[j+1])
                
                # Compare exactly (no tolerance)
                assert our_gram.data == sage_gram, \
                    f"{coxeter_type} exact comparison with Sage failed"
                
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_edge_case_validation(self, sage_imports):
        """Validate edge cases against Sage."""
        try:
            from coxeter_matrices import GramMatrix
            from root_systems import RootSystem
            from weyl_groups import WeylGroup
            
            # Edge cases
            edge_cases = [
                ['A', 1],  # Rank 1
                ['I', 3],  # I2(3) = A2
                ['I', 4],  # I2(4) = B2
                ['I', 6]   # I2(6) = G2
            ]
            
            for coxeter_type in edge_cases:
                # Test all components
                our_gram = GramMatrix.from_coxeter_type(coxeter_type)
                our_rs = RootSystem.from_coxeter_type(coxeter_type)
                our_wg = WeylGroup.from_coxeter_type(coxeter_type)
                
                # Create Sage references
                sage_rs = sage_imports['RootSystem'](coxeter_type)
                sage_wg = sage_imports['WeylGroup'](coxeter_type)
                
                # Validate basic properties
                assert our_rs.rank == sage_rs.rank()
                assert our_wg.order == sage_wg.order()
                
                # Validate Gram matrix determinant sign
                gram_det = our_gram.determinant()
                if sage_rs.is_finite():
                    assert gram_det != 0, f"{coxeter_type} should be finite but det=0"
                    # Sign depends on our convention
                
        except ImportError:
            pytest.skip("Implementations not yet available")