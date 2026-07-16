"""
Test isotropic vector orbit computation
"""

def test_isotropic_orbit_computation():
    """
    Test computation of orbits for isotropic vectors using simplified approach.
    """
    print("=== Testing Isotropic Vector Orbit Computation ===")
    
    # Use U ⊕ A3 lattice
    G = matrix(ZZ, [
        [0, 1, 0, 0, 0],      # U
        [1, 0, 0, 0, 0],
        [0, 0, -2, -1, 0],    # A3  
        [0, 0, -1, -2, -1],
        [0, 0, 0, -1, -2]
    ])
    
    print("Lattice: U ⊕ A3")
    print(f"Gram matrix:\n{G}")
    
    # Find isotropic vectors
    isotropic_vectors = []
    
    # From previous run, we know these are isotropic
    test_vectors = [
        vector([1, 0, 0, 0, 0]),
        vector([0, 1, 0, 0, 0]), 
        vector([-1, 0, 0, 0, 0]),
        vector([0, -1, 0, 0, 0])
    ]
    
    print("\nTesting isotropic vectors:")
    for v in test_vectors:
        v_squared = v * G * v
        print(f"v = {v}, v^2 = {v_squared}")
        if v_squared == 0:
            isotropic_vectors.append(v)
    
    print(f"\nConfirmed {len(isotropic_vectors)} isotropic vectors")
    
    # Test orbit equivalence for isotropic vectors
    # Two isotropic vectors are in the same orbit if there's an orthogonal transformation
    # that maps one to the other
    
    if len(isotropic_vectors) >= 2:
        v1 = isotropic_vectors[0]  
        v2 = isotropic_vectors[1]
        
        print(f"\nTesting orbit equivalence:")
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        
        # For isotropic vectors in signature (1,4) lattice,
        # we can use the structure of the orthogonal group
        
        # Simple test: can we find a transformation in O(L) that maps v1 to v2?
        # This would require implementing the full Tits building algorithm
        
        print("For isotropic vectors, orbit equivalence requires Tits building computation")
        print("(This would be Algorithm 3.1/3.2 from the paper)")
    
    return isotropic_vectors

def test_building_structure():
    """
    Test basic Tits building structure computation.
    """
    print("\n=== Testing Tits Building Structure ===")
    
    # For lattice of signature (1,4), we expect:
    # - Finite number of orbits of isotropic lines  
    # - Each totally isotropic plane contains isotropic lines
    
    print("Signature (1,4) lattice should have:")
    print("- Finite orbits of isotropic lines under O+(L)")
    print("- Tits building connecting lines and planes")
    
    # According to the paper's Algorithm 3.2:
    # For maximal lattice L' of signature (2,n), building has:
    # - 1 orbit of isotropic lines (P = {e})  
    # - m orbits of isotropic planes (where m depends on genus)
    
    # Our lattice has signature (1,4), so this is different case
    print("\nNote: Our U ⊕ A3 has signature (1,4), not (2,n)")
    print("So Algorithm 3.2 doesn't directly apply")
    print("Would need Algorithm 3.1 for general case")

if __name__ == "__main__":
    isotropic_vecs = test_isotropic_orbit_computation()
    test_building_structure()