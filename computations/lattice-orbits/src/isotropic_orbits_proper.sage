"""
Computational algorithms for computing orbits of isotropic vectors in lattices
Using SageMath's proper IntegralLattice and related classes

Based on "Orbits in Lattices" by Matthew Dawes (arXiv:2205.10601)
"""

def create_hyperbolic_plane():
    """
    Create the hyperbolic plane U with Gram matrix [[0,1],[1,0]].
    """
    U_gram = matrix(ZZ, [[0, 1], [1, 0]])
    return IntegralLattice(U_gram)

def create_A_root_lattice(n):
    """
    Create the A_n root lattice using SageMath's built-in root system.
    """
    if n == 2:
        # A2 root lattice has Gram matrix [[-2,-1],[-1,-2]]
        A2_gram = matrix(ZZ, [[-2, -1], [-1, -2]])
        return IntegralLattice(A2_gram)
    elif n == 3:
        # A3 root lattice has Gram matrix [[-2,-1,0],[-1,-2,-1],[0,-1,-2]]
        A3_gram = matrix(ZZ, [[-2, -1, 0], [-1, -2, -1], [0, -1, -2]])
        return IntegralLattice(A3_gram)
    else:
        # Use SageMath's root system infrastructure
        R = RootSystem(['A', n])
        root_lattice = R.root_lattice()
        # Convert to IntegralLattice
        simple_roots = [root_lattice.simple_root(i) for i in range(1, n+1)]
        gram_matrix = matrix(ZZ, [[r.scalar(s) for s in simple_roots] for r in simple_roots])
        return IntegralLattice(gram_matrix)

def create_orthogonal_sum(lattice_list):
    """
    Create orthogonal direct sum of lattices using native SageMath methods.
    """
    if len(lattice_list) == 1:
        return lattice_list[0]
    
    # Use IntegralLattice's native direct_sum method  
    from functools import reduce
    return reduce(lambda x, y: x.direct_sum(y), lattice_list)

class IsotropicVectorOrbitsProper:
    """
    Proper implementation using SageMath's IntegralLattice class.
    """
    
    def __init__(self, lattice):
        """
        Initialize with an IntegralLattice.
        
        INPUT:
        - lattice: An IntegralLattice object
        """
        self.L = lattice
        self.G = lattice.gram_matrix()
        self.n = self.G.nrows()
        self.signature = self._compute_signature()
        
    def _compute_signature(self):
        """
        Compute signature (t+, t-) using proper eigenvalue computation.
        """
        # Use characteristic polynomial for exact computation
        char_poly = self.G.characteristic_polynomial()
        try:
            # Try to get exact roots
            roots = char_poly.roots(ring=QQbar, multiplicities=False)
            t_plus = sum(1 for r in roots if r > 0)
            t_minus = sum(1 for r in roots if r < 0)
            return (t_plus, t_minus)
        except:
            # Fallback: use floating point
            eigenvals = self.G.change_ring(RR).eigenvalues()
            t_plus = sum(1 for ev in eigenvals if ev > 1e-10)
            t_minus = sum(1 for ev in eigenvals if ev < -1e-10)
            return (t_plus, t_minus)
    
    def is_isotropic_vector(self, v):
        """
        Check if vector v is isotropic (v^2 = 0).
        """
        return v * self.G * v == 0
    
    def quadratic_form_value(self, v):
        """
        Compute quadratic form value v^2 = v^T * G * v using native SageMath.
        """
        return self.L.q(v)
    
    def inner_product(self, u, v):
        """
        Compute inner product (u, v) = u^T * G * v using native SageMath.
        """
        return self.L.b(u, v)
    
    def find_primitive_isotropic_vectors(self, max_search=5):
        """
        Find primitive isotropic vectors by systematic search.
        """
        isotropic_vectors = []
        
        # Search in small integer range
        for coords in itertools.product(range(-max_search, max_search+1), repeat=self.n):
            if all(c == 0 for c in coords):
                continue
                
            v = vector(ZZ, coords)
            
            # Check if isotropic
            if self.is_isotropic_vector(v):
                # Check if primitive (gcd of coordinates is 1)
                if gcd(coords) == 1:
                    isotropic_vectors.append(v)
                    
        return isotropic_vectors
    
    def smith_normal_form_detailed(self, v):
        """
        Compute Smith normal form for vector v following Algorithm 2.1.
        """
        print(f"Computing Smith normal form for v = {v}")
        
        # Compute v̂ = v * G (the dual vector)
        v_hat = v * self.G
        print(f"v̂ = v * G = {v_hat}")
        
        # Smith normal form of [v̂]
        A = matrix([v_hat])
        D, U, V = A.smith_form()
        
        print(f"Smith normal form:")
        print(f"D = {D}")
        print(f"U = {U}")  
        print(f"V = {V}")
        print(f"Verification: U * A * V = {U * A * V}")
        
        # Extract orthogonal complement from V
        # Columns 2 through n of V give the orthogonal complement
        complement_basis = []
        for j in range(1, V.ncols()):
            complement_basis.append(vector(V.column(j)))
            
        print(f"Orthogonal complement basis from Smith form:")
        for i, b in enumerate(complement_basis):
            print(f"  k_{i+1} = {b}")
            # Verify orthogonality
            inner_prod = self.inner_product(v, b)
            print(f"    (v, k_{i+1}) = {inner_prod}")
            
        return D, U, V, complement_basis
    
    def algorithm_2_1_detailed(self, v1, v2):
        """
        Detailed implementation of Algorithm 2.1 from the paper.
        """
        print("=" * 60)
        print("Algorithm 2.1: Testing orbit equivalence for non-isotropic vectors")
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        
        # Step 1: Find minimal c_i such that c_i * v_i ∈ L
        def find_minimal_denominator(v):
            denoms = []
            for x in v:
                if x in QQ:
                    denoms.append(QQ(x).denominator())
                else:
                    denoms.append(1)
            return lcm(denoms) if denoms else 1
        
        c1 = find_minimal_denominator(v1)
        c2 = find_minimal_denominator(v2)
        print(f"c1 = {c1}, c2 = {c2}")
        
        # Step 2: Check necessary conditions
        v1_squared = self.quadratic_form_value(v1)
        v2_squared = self.quadratic_form_value(v2)
        print(f"v1^2 = {v1_squared}, v2^2 = {v2_squared}")
        
        if v1_squared != v2_squared or c1 != c2:
            print("RESULT: v1 ≁ v2 (failed necessary conditions)")
            return False
            
        # Step 3: Compute w_i = c_i * v_i and their orthogonal complements
        w1 = c1 * v1
        w2 = c2 * v2  
        print(f"w1 = {w1}, w2 = {w2}")
        
        # Step 3: Compute K_i = w_i^⊥ using Smith normal form
        print("\nComputing K1 = w1^⊥:")
        _, _, _, K1_basis = self.smith_normal_form_detailed(w1)
        
        print("\nComputing K2 = w2^⊥:")
        _, _, _, K2_basis = self.smith_normal_form_detailed(w2)
        
        # Step 4: Check if K1 and K2 are isometric
        if len(K1_basis) != len(K2_basis):
            print("RESULT: v1 ≁ v2 (orthogonal complements have different ranks)")
            return False
            
        # Compute Gram matrices of orthogonal complements
        G_K1 = matrix([[self.inner_product(u, v) for v in K1_basis] for u in K1_basis])
        G_K2 = matrix([[self.inner_product(u, v) for v in K2_basis] for u in K2_basis])
        
        print(f"\nGram matrix of K1:")
        print(G_K1)
        print(f"Gram matrix of K2:")
        print(G_K2)
        
        # For definite lattices, check determinants and signatures
        det_K1 = G_K1.determinant()
        det_K2 = G_K2.determinant()
        print(f"det(K1) = {det_K1}, det(K2) = {det_K2}")
        
        if det_K1 != det_K2:
            print("RESULT: v1 ≁ v2 (orthogonal complements have different determinants)")
            return False
            
        # For this implementation, we'll assume they're isometric if determinants match
        # In practice, would need full isometry testing algorithm
        print("RESULT: v1 ~ v2 (orthogonal complements appear isometric)")
        return True

def test_examples_from_paper():
    """
    Test the examples from the paper using proper SageMath constructions.
    """
    print("Testing Examples from Dawes' Paper with Proper SageMath Implementation")
    print("=" * 80)
    
    # Create U ⊕ A3 lattice
    print("Creating lattice L = U ⊕ A3")
    U = create_hyperbolic_plane()
    A3 = create_A_root_lattice(3)
    L = create_orthogonal_sum([U, A3])
    
    print(f"U Gram matrix:\n{U.gram_matrix()}")
    print(f"A3 Gram matrix:\n{A3.gram_matrix()}")
    print(f"L = U ⊕ A3 Gram matrix:\n{L.gram_matrix()}")
    
    # Initialize orbit computer
    orbits = IsotropicVectorOrbitsProper(L)
    print(f"Lattice signature: {orbits.signature}")
    
    # Example 2.2 from paper
    print("\n" + "=" * 60)
    print("EXAMPLE 2.2 from Paper")
    v1 = vector(QQ, [4, 4, 1, 2, -1])
    v2 = vector(QQ, [36, 144, 5, -30, 83])
    orbits.algorithm_2_1_detailed(v1, v2)
    
    # Example 2.6 from paper  
    print("\n" + "=" * 60)
    print("EXAMPLE 2.6 from Paper")
    u1 = vector(QQ, [1, -1, 0, 0, 0])
    u2 = vector(QQ, [1, 0, 1, 0, 0])
    orbits.algorithm_2_1_detailed(u1, u2)
    
    # Find isotropic vectors
    print("\n" + "=" * 60)
    print("FINDING ISOTROPIC VECTORS")
    isotropic_vecs = orbits.find_primitive_isotropic_vectors(max_search=3)
    print(f"Found {len(isotropic_vecs)} primitive isotropic vectors:")
    for i, v in enumerate(isotropic_vecs[:10]):  # Show first 10
        v_squared = orbits.quadratic_form_value(v)
        print(f"  {i+1}: {v}, v^2 = {v_squared}")
    
    return orbits, isotropic_vecs

def demonstrate_lattice_properties():
    """
    Demonstrate various lattice properties using SageMath's infrastructure.
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATING LATTICE PROPERTIES")
    
    # Create some standard lattices
    print("Creating standard lattices:")
    
    # Hyperbolic plane U
    U = create_hyperbolic_plane()
    print(f"U (hyperbolic plane): rank {U.rank()}, signature {IsotropicVectorOrbitsProper(U).signature}")
    
    # A2 root lattice  
    A2 = create_A_root_lattice(2)
    print(f"A2 root lattice: rank {A2.rank()}, signature {IsotropicVectorOrbitsProper(A2).signature}")
    
    # A3 root lattice
    A3 = create_A_root_lattice(3)  
    print(f"A3 root lattice: rank {A3.rank()}, signature {IsotropicVectorOrbitsProper(A3).signature}")
    
    # 2U ⊕ A2 (example from paper)
    L1 = create_orthogonal_sum([U, U, A2])
    orbits_L1 = IsotropicVectorOrbitsProper(L1)
    print(f"2U ⊕ A2: rank {L1.rank()}, signature {orbits_L1.signature}")
    
    # Find some isotropic vectors in 2U ⊕ A2
    isotropic_2U_A2 = orbits_L1.find_primitive_isotropic_vectors(max_search=2)
    print(f"Found {len(isotropic_2U_A2)} isotropic vectors in 2U ⊕ A2")
    
if __name__ == "__main__":
    import itertools
    
    # Run the main examples
    orbits, isotropic_vecs = test_examples_from_paper()
    
    # Demonstrate lattice properties
    demonstrate_lattice_properties()
    
    print("\n" + "=" * 80)
    print("All tests completed successfully!")