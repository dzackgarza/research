"""
Integration tests for constructor interactions.

Tests how our constructors work together to build consistent mathematical objects.
"""

import pytest


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.tdd
@pytest.mark.not_implemented
@pytest.mark.constructor_integration
class TestGramMatrixRootSystemIntegration:
    """Test integration between GramMatrix and RootSystem constructors."""
    
    def test_gram_to_root_system_A2(self, skip_if_no_sage):
        """Test creating RootSystem from GramMatrix for A2."""
        try:
            from coxeter_matrices import GramMatrix
            from root_systems import RootSystem
            
            # Create GramMatrix
            gram = GramMatrix.from_coxeter_type(['A', 2])
            
            # Create RootSystem from GramMatrix
            root_system = RootSystem.from_gram_matrix(gram)
            
            # Verify consistency
            assert root_system.rank == gram.rank
            assert root_system.coxeter_type == ['A', 2]
            assert root_system.gram_matrix.data == gram.data
            
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_root_system_to_gram_matrix_consistency(self, skip_if_no_sage):
        """Test that RootSystem→GramMatrix→RootSystem is consistent."""
        try:
            from root_systems import RootSystem
            from coxeter_matrices import GramMatrix
            
            # Start with RootSystem
            rs1 = RootSystem.from_coxeter_type(['B', 3])
            
            # Extract GramMatrix
            gram = rs1.gram_matrix
            
            # Create new RootSystem from GramMatrix
            rs2 = RootSystem.from_gram_matrix(gram)
            
            # Should be mathematically equivalent
            assert rs1.rank == rs2.rank
            assert rs1.positive_root_count == rs2.positive_root_count
            assert rs1.gram_matrix.data == rs2.gram_matrix.data
            
        except ImportError:
            pytest.skip("Implementations not yet available")


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.tdd
@pytest.mark.not_implemented
@pytest.mark.constructor_integration
class TestRootSystemCoxeterGroupIntegration:
    """Test integration between RootSystem and CoxeterGroup."""
    
    def test_root_system_to_coxeter_group_A3(self, skip_if_no_sage):
        """Test creating CoxeterGroup from RootSystem for A3."""
        try:
            from root_systems import RootSystem
            from coxeter_groups import CoxeterGroup
            
            # Create RootSystem
            root_system = RootSystem.from_coxeter_type(['A', 3])
            
            # Create CoxeterGroup from RootSystem
            coxeter_group = CoxeterGroup.from_root_system(root_system)
            
            # Verify consistency
            assert coxeter_group.rank == root_system.rank
            assert coxeter_group.coxeter_type == root_system.coxeter_type
            assert coxeter_group.order == 24  # |S₄| = 24
            
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_coxeter_group_weyl_group_equivalence(self, skip_if_no_sage):
        """Test that CoxeterGroup and WeylGroup are equivalent for crystallographic types."""
        try:
            from coxeter_groups import CoxeterGroup
            from weyl_groups import WeylGroup
            
            coxeter_type = ['D', 4]
            
            # Create both groups
            coxeter_group = CoxeterGroup.from_coxeter_type(coxeter_type)
            weyl_group = WeylGroup.from_coxeter_type(coxeter_type)
            
            # Should have same order for crystallographic types
            assert coxeter_group.order == weyl_group.order
            assert coxeter_group.rank == weyl_group.rank
            
        except ImportError:
            pytest.skip("Implementations not yet available")


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.tdd
@pytest.mark.not_implemented
@pytest.mark.mathematical_consistency
class TestMathematicalConsistency:
    """Test mathematical consistency across components."""
    
    def test_rank_consistency_across_components(self, skip_if_no_sage):
        """Test that rank is consistent across all components."""
        try:
            from coxeter_matrices import GramMatrix
            from root_systems import RootSystem
            from coxeter_groups import CoxeterGroup
            from weyl_groups import WeylGroup
            
            coxeter_type = ['E', 6]
            
            # Create all components
            gram = GramMatrix.from_coxeter_type(coxeter_type)
            root_system = RootSystem.from_coxeter_type(coxeter_type)
            coxeter_group = CoxeterGroup.from_coxeter_type(coxeter_type)
            weyl_group = WeylGroup.from_coxeter_type(coxeter_type)
            
            # All should have same rank
            ranks = [gram.rank, root_system.rank, coxeter_group.rank, weyl_group.rank]
            assert len(set(ranks)) == 1  # All ranks equal
            assert ranks[0] == 6
            
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    @pytest.mark.parametrize("coxeter_type,rank", [
        (['A', 2], 2), (['B', 3], 3), (['C', 4], 4), 
        (['D', 5], 5), (['E', 7], 7), (['F', 4], 4), (['G', 2], 2)
    ])
    def test_type_consistency_finite_crystallographic(self, coxeter_type, rank, skip_if_no_sage):
        """Test type consistency for finite crystallographic types."""
        try:
            from coxeter_matrices import GramMatrix
            from root_systems import RootSystem
            from coxeter_groups import CoxeterGroup
            from weyl_groups import WeylGroup
            
            # Create components
            gram = GramMatrix.from_coxeter_type(coxeter_type)
            root_system = RootSystem.from_coxeter_type(coxeter_type)
            coxeter_group = CoxeterGroup.from_coxeter_type(coxeter_type)
            weyl_group = WeylGroup.from_coxeter_type(coxeter_type)
            
            # All should be finite
            assert gram.type == 'finite'
            assert root_system.is_finite == True
            assert coxeter_group.is_finite == True
            assert weyl_group.is_finite == True
            
            # Groups should have same order
            assert coxeter_group.order == weyl_group.order
            
            # Verify rank
            assert gram.rank == rank
            assert root_system.rank == rank
            
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_gram_matrix_determinant_type_correspondence(self, mathematical_consistency_checker):
        """Test correspondence between Gram matrix determinant and type."""
        try:
            from coxeter_matrices import GramMatrix
            
            test_cases = [
                (['A', 2], 'finite', lambda det: det > 0),
                (['A', 1, 1], 'affine', lambda det: det == 0),
                # Would need hyperbolic example
            ]
            
            for coxeter_type, expected_type, det_condition in test_cases:
                if expected_type == 'hyperbolic':
                    continue  # Skip until we have hyperbolic examples
                
                gram = GramMatrix.from_coxeter_type(coxeter_type)
                
                assert gram.type == expected_type
                assert det_condition(gram.determinant())
            
        except ImportError:
            pytest.skip("Implementations not yet available")


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.tdd
@pytest.mark.not_implemented
@pytest.mark.data_flow
class TestDataFlowIntegration:
    """Test data flow between components."""
    
    def test_complete_construction_chain(self, integration_workflow):
        """Test complete constructor chain from Coxeter type to all objects.""" 
        try:
            from coxeter_matrices import GramMatrix
            from root_systems import RootSystem
            from coxeter_groups import CoxeterGroup
            from weyl_groups import WeylGroup
            from dynkin_diagrams import DynkinDiagram
            
            coxeter_type = ['B', 4]
            
            # Set up workflow
            workflow = integration_workflow()
            
            # Step 1: Create GramMatrix
            workflow.add_step(
                'gram_matrix',
                lambda: GramMatrix.from_coxeter_type(coxeter_type)
            )
            
            # Step 2: Create RootSystem from GramMatrix  
            workflow.add_step(
                'root_system',
                lambda: RootSystem.from_gram_matrix(workflow.results['gram_matrix'])
            )
            
            # Step 3: Create CoxeterGroup from RootSystem
            workflow.add_step(
                'coxeter_group', 
                lambda: CoxeterGroup.from_root_system(workflow.results['root_system'])
            )
            
            # Step 4: Create WeylGroup
            workflow.add_step(
                'weyl_group',
                lambda: WeylGroup.from_coxeter_type(coxeter_type)
            )
            
            # Step 5: Create DynkinDiagram
            workflow.add_step(
                'dynkin_diagram',
                lambda: DynkinDiagram.from_coxeter_type(coxeter_type)
            )
            
            # Execute workflow
            results = workflow.execute()
            
            # Verify all steps succeeded
            for step_name, result in results.items():
                assert 'error' not in result, f"Step {step_name} failed: {result.get('error')}"
            
            # Verify consistency
            assert workflow.verify_consistency()
            
        except ImportError:
            pytest.skip("Implementations not yet available")
    
    def test_alternative_construction_paths(self, skip_if_no_sage):
        """Test that different construction paths give equivalent results."""
        try:
            from coxeter_matrices import GramMatrix
            from root_systems import RootSystem
            from coxeter_groups import CoxeterGroup
            
            coxeter_type = ['C', 3]
            
            # Path 1: Type → GramMatrix → RootSystem → CoxeterGroup
            gram1 = GramMatrix.from_coxeter_type(coxeter_type)
            rs1 = RootSystem.from_gram_matrix(gram1)
            cg1 = CoxeterGroup.from_root_system(rs1)
            
            # Path 2: Type → RootSystem → CoxeterGroup
            rs2 = RootSystem.from_coxeter_type(coxeter_type)
            cg2 = CoxeterGroup.from_root_system(rs2)
            
            # Path 3: Type → CoxeterGroup directly
            cg3 = CoxeterGroup.from_coxeter_type(coxeter_type)
            
            # All CoxeterGroups should be equivalent
            assert cg1.order == cg2.order == cg3.order
            assert cg1.rank == cg2.rank == cg3.rank
            
            # All RootSystems should be equivalent
            assert rs1.rank == rs2.rank
            assert rs1.positive_root_count == rs2.positive_root_count
            
        except ImportError:
            pytest.skip("Implementations not yet available")