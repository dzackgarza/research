"""
Examples from Dawes' paper implemented using the modular, idiomatic SageMath components.
"""

load("lattice_utils.sage")
load("smith_normal_form_utils.sage") 
load("vector_orbit_algorithms.sage")

def run_example_2_2():
    """
    Example 2.2 from Dawes' paper: L = U ⊕ A₃
    Tests if v₁ = (4, 4, 1, 2, -1) ~ v₂ = (36, 144, 5, -30, 83) under Ô⁺(L)
    """
    print("Example 2.2 from Dawes' Paper")
    print("="*50)
    
    # Create lattice L = U ⊕ A₃
    U = create_hyperbolic_plane()
    A3 = create_root_lattice('A', 3)
    L = create_orthogonal_sum([U, A3])
    
    print(f"Lattice L = U ⊕ A₃:")
    print(f"Rank: {L.rank()}")
    print(f"Gram matrix:\n{L.gram_matrix()}")
    
    # Initialize analyzer
    analyzer = VectorOrbitAnalyzer(L)
    print(f"Signature: {analyzer.signature}")
    
    # Test vectors from paper
    v1 = vector(QQ, [4, 4, 1, 2, -1])
    v2 = vector(QQ, [36, 144, 5, -30, 83])
    
    # Run Algorithm 2.1
    result = analyzer.algorithm_2_1_orbit_test(v1, v2, verbose=True)
    
    return L, analyzer, result

def run_example_2_6():
    """
    Example 2.6 from Dawes' paper: L = U ⊕ A₃
    Tests if v₁ = (1, -1, 0, 0, 0) ~ v₂ = (1, 0, 1, 0, 0) under ŜO⁺(L)
    """
    print("\n\nExample 2.6 from Dawes' Paper")
    print("="*50)
    
    # Same lattice as Example 2.2
    U = create_hyperbolic_plane()
    A3 = create_root_lattice('A', 3)
    L = create_orthogonal_sum([U, A3])
    
    analyzer = VectorOrbitAnalyzer(L)
    
    # Test vectors from paper  
    v1 = vector(QQ, [1, -1, 0, 0, 0])
    v2 = vector(QQ, [1, 0, 1, 0, 0])
    
    # Run Algorithm 2.1
    result = analyzer.algorithm_2_1_orbit_test(v1, v2, verbose=True)
    
    return L, analyzer, result

def demonstrate_isotropic_vector_analysis():
    """
    Demonstrate isotropic vector finding and analysis using modular components.
    """
    print("\n\nIsotropic Vector Analysis")
    print("="*50)
    
    # Create lattice L = U ⊕ A₃
    U = create_hyperbolic_plane()
    A3 = create_root_lattice('A', 3)
    L = create_orthogonal_sum([U, A3])
    
    # Find isotropic vectors
    finder = IsotropicVectorFinder(L)
    isotropic_vectors = finder.find_primitive_isotropic_vectors(search_bound=2)
    
    print(f"Found {len(isotropic_vectors)} primitive isotropic vectors")
    
    # Show first few examples
    for i, v in enumerate(isotropic_vectors[:5]):
        v_squared = finder.orbit_analyzer.quadratic_form_value(v)
        print(f"  {i+1}: {v}, v² = {v_squared}")
    
    # Classify into orbits (placeholder)
    orbit_data = finder.classify_isotropic_orbits(isotropic_vectors, verbose=True)
    
    return finder, isotropic_vectors, orbit_data

def demonstrate_lattice_constructions():
    """
    Demonstrate proper SageMath lattice constructions.
    """
    print("\n\nLattice Construction Demonstrations")
    print("="*50)
    
    # Individual lattices
    print("Standard lattice constructions:")
    
    U = create_hyperbolic_plane()
    print(f"U (hyperbolic plane): rank {U.rank()}")
    print(f"  Signature: {get_lattice_signature(U)}")
    
    A2 = create_root_lattice('A', 2)
    print(f"A₂ root lattice: rank {A2.rank()}")  
    print(f"  Signature: {get_lattice_signature(A2)}")
    
    A3 = create_root_lattice('A', 3)
    print(f"A₃ root lattice: rank {A3.rank()}")
    print(f"  Signature: {get_lattice_signature(A3)}")
    
    # Orthogonal sums
    print("\nOrthogonal sum constructions:")
    
    L1 = create_orthogonal_sum([U, A2])
    print(f"U ⊕ A₂: rank {L1.rank()}, signature {get_lattice_signature(L1)}")
    
    L2 = create_orthogonal_sum([U, U, A2])  
    print(f"2U ⊕ A₂: rank {L2.rank()}, signature {get_lattice_signature(L2)}")
    
    return {
        'U': U, 'A2': A2, 'A3': A3,
        'U_plus_A2': L1, '2U_plus_A2': L2
    }

def main():
    """
    Run all examples and demonstrations.
    """
    print("Modular Implementation of Dawes' Isotropic Vector Orbit Algorithms")
    print("="*80)
    
    # Run paper examples
    L1, analyzer1, result1 = run_example_2_2()
    L2, analyzer2, result2 = run_example_2_6()
    
    # Demonstrate isotropic vector analysis
    finder, isotropic_vecs, orbit_data = demonstrate_isotropic_vector_analysis()
    
    # Demonstrate lattice constructions
    lattices = demonstrate_lattice_constructions()
    
    print("\n" + "="*80)
    print("All examples completed successfully!")
    print(f"Example 2.2 result: {result1}")
    print(f"Example 2.6 result: {result2}")
    print(f"Found {len(isotropic_vecs)} isotropic vectors")
    
    return {
        'example_2_2': (L1, analyzer1, result1),
        'example_2_6': (L2, analyzer2, result2),
        'isotropic_analysis': (finder, isotropic_vecs, orbit_data),
        'lattice_constructions': lattices
    }

if __name__ == "__main__":
    results = main()