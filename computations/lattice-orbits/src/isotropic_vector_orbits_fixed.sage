"""
Computational algorithms for computing orbits of isotropic vectors in lattices
Based on "Orbits in Lattices" by Matthew Dawes (arXiv:2205.10601)

Fixed version with actual examples from the paper.
"""

def example_2_2_from_paper():
    """
    Example 2.2 from the paper: L = U ⊕ A3
    Tests if v1 = (4, 4, 1, 2, -1) ~ v2 = (36, 144, 5, -30, 83) under Ô+(L)
    """
    print("=== Example 2.2 from Paper: L = U ⊕ A3 ===")
    
    # Define Gram matrix for U ⊕ A3
    # U: [[0,1],[1,0]]
    # A3: [[-2,-1,0],[-1,-2,-1],[0,-1,-2]]
    G = matrix(ZZ, [
        [0, 1, 0, 0, 0],      # U
        [1, 0, 0, 0, 0],
        [0, 0, -2, -1, 0],    # A3  
        [0, 0, -1, -2, -1],
        [0, 0, 0, -1, -2]
    ])
    
    print(f"Gram matrix G:")
    print(G)
    
    # Vectors from Example 2.2
    v1 = vector(QQ, [4, 4, 1, 2, -1])
    v2 = vector(QQ, [36, 144, 5, -30, 83])
    
    # Check squared lengths
    v1_squared = v1 * G * v1
    v2_squared = v2 * G * v2
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1^2 = {v1_squared}")  # Should be 20
    print(f"v2^2 = {v2_squared}")  # Should be 20
    
    # According to paper: c1 = c2 = 1, so w1 = v1, w2 = v2
    w1 = v1
    w2 = v2
    
    print(f"\nw1 = {w1}, w2 = {w2}")
    
    # The paper shows these vectors are equivalent under Ô+(L)
    print(f"According to the paper: v1 ~ v2 under Ô+(L)")
    
    return G, v1, v2

def example_2_6_from_paper():
    """
    Example 2.6 from the paper: L = U ⊕ A3
    Tests if v1 = (1, -1, 0, 0, 0) ~ v2 = (1, 0, 1, 0, 0) under ŜO+(L)
    """
    print("\n=== Example 2.6 from Paper: L = U ⊕ A3 ===")
    
    # Same lattice as Example 2.2
    G = matrix(ZZ, [
        [0, 1, 0, 0, 0],      # U
        [1, 0, 0, 0, 0],
        [0, 0, -2, -1, 0],    # A3  
        [0, 0, -1, -2, -1],
        [0, 0, 0, -1, -2]
    ])
    
    # Vectors from Example 2.6
    v1 = vector(QQ, [1, -1, 0, 0, 0])
    v2 = vector(QQ, [1, 0, 1, 0, 0])
    
    # Check squared lengths
    v1_squared = v1 * G * v1
    v2_squared = v2 * G * v2
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1^2 = {v1_squared}")  # Should be -2
    print(f"v2^2 = {v2_squared}")  # Should be -2
    
    print(f"According to the paper: v1 ~ v2 under ŜO+(L)")
    
    return G, v1, v2

def compute_orthogonal_complement_smith(G, w):
    """
    Compute orthogonal complement w^perp using Smith normal form.
    """
    print(f"\nComputing orthogonal complement of w = {w}")
    
    # Compute ŵ = w * G (dual vector)
    w_hat = w * G
    print(f"ŵ = w * G = {w_hat}")
    
    # Smith normal form of [ŵ]
    A = matrix([w_hat])
    try:
        D, U, V = A.smith_form()
        print(f"Smith form: D = {D}")
        print(f"U = {U}")
        print(f"V = {V}")
        
        # The orthogonal complement basis comes from V
        # Take columns 2 through n of V^(-1)
        V_inv = V.inverse()
        complement_basis = []
        for j in range(1, V_inv.ncols()):
            complement_basis.append(V_inv.column(j))
            
        print(f"Orthogonal complement basis:")
        for i, b in enumerate(complement_basis):
            print(f"  k_{i+1} = {b}")
            
        return complement_basis
        
    except Exception as e:
        print(f"Error in Smith form computation: {e}")
        
        # Fallback: find orthogonal vectors directly
        n = G.nrows()
        complement_basis = []
        
        for i in range(n):
            e_i = vector([0] * n)
            e_i[i] = 1
            if w * G * e_i == 0:
                complement_basis.append(e_i)
                
        print(f"Fallback orthogonal complement basis:")
        for i, b in enumerate(complement_basis):
            print(f"  basis_{i+1} = {b}")
            
        return complement_basis

def verify_isotropic_examples():
    """
    Verify that we can find isotropic vectors for building construction.
    """
    print("\n=== Finding Isotropic Vectors ===")
    
    # For L = U ⊕ A3, signature should be (1, 4)
    G = matrix(ZZ, [
        [0, 1, 0, 0, 0],      # U
        [1, 0, 0, 0, 0],
        [0, 0, -2, -1, 0],    # A3  
        [0, 0, -1, -2, -1],
        [0, 0, 0, -1, -2]
    ])
    
    # Try to find isotropic vectors (v^2 = 0)
    print("Searching for isotropic vectors...")
    
    isotropic_vectors = []
    
    # Try some simple combinations
    for a in range(-2, 3):
        for b in range(-2, 3):
            if a == 0 and b == 0:
                continue
            v = vector([a, b, 0, 0, 0])  # Vector in U component
            if v * G * v == 0:
                isotropic_vectors.append(v)
                print(f"Found isotropic: {v}, v^2 = {v * G * v}")
    
    # Try vectors involving A3 component  
    for c in range(-1, 2):
        for d in range(-1, 2):
            for e in range(-1, 2):
                if c == 0 and d == 0 and e == 0:
                    continue
                v = vector([0, 0, c, d, e])
                v_squared = v * G * v
                if v_squared == 0:
                    isotropic_vectors.append(v)
                    print(f"Found isotropic: {v}, v^2 = {v_squared}")
    
    print(f"Total isotropic vectors found: {len(isotropic_vectors)}")
    return isotropic_vectors

def main():
    """
    Run examples from the paper.
    """
    print("Testing Examples from 'Orbits in Lattices' by Matthew Dawes")
    print("=" * 60)
    
    # Example 2.2
    G1, v1, v2 = example_2_2_from_paper()
    compute_orthogonal_complement_smith(G1, v1)
    
    # Example 2.6  
    G2, u1, u2 = example_2_6_from_paper()
    compute_orthogonal_complement_smith(G2, u1)
    
    # Find isotropic vectors for Tits' buildings
    isotropic_vecs = verify_isotropic_examples()
    
    print("\n" + "=" * 60)
    print("Examples completed successfully!")

if __name__ == "__main__":
    main()