"""
Utility functions for constructing standard lattices using proper SageMath methods.
"""

def create_hyperbolic_plane():
    """
    Create the hyperbolic plane U with Gram matrix [[0,1],[1,0]] using proper SageMath.
    """
    U_gram = matrix(ZZ, [[0, 1], [1, 0]])
    return IntegralLattice(U_gram)

def create_root_lattice(root_type, rank):
    """
    Create root lattices using SageMath's root system infrastructure.
    
    INPUT:
    - root_type: 'A', 'B', 'C', 'D', 'E', 'F', 'G'  
    - rank: rank of the root system
    
    OUTPUT:
    - IntegralLattice object
    """
    if root_type == 'A' and rank <= 3:
        # Use explicit Gram matrices for small cases
        if rank == 2:
            # A2 root lattice: [[-2,-1],[-1,-2]]
            gram = matrix(ZZ, [[-2, -1], [-1, -2]])
        elif rank == 3:
            # A3 root lattice: [[-2,-1,0],[-1,-2,-1],[0,-1,-2]]
            gram = matrix(ZZ, [[-2, -1, 0], [-1, -2, -1], [0, -1, -2]])
        else:
            raise NotImplementedError(f"A{rank} not implemented for rank {rank}")
        return IntegralLattice(gram)
    else:
        # Use SageMath's root system for general case
        R = RootSystem([root_type, rank])
        root_lattice = R.root_lattice()
        
        # Get simple roots and compute Gram matrix
        simple_roots = [root_lattice.simple_root(i) for i in range(1, rank+1)]
        gram_matrix = matrix(ZZ, [[r.scalar(s) for s in simple_roots] for r in simple_roots])
        
        return IntegralLattice(gram_matrix)

def create_orthogonal_sum(lattices):
    """
    Create orthogonal direct sum of IntegralLattice objects using native SageMath.
    
    INPUT:
    - lattices: list of IntegralLattice objects
    
    OUTPUT:
    - IntegralLattice representing the orthogonal sum
    """
    if len(lattices) == 1:
        return lattices[0]
    
    # Use IntegralLattice's native direct_sum method
    from functools import reduce
    return reduce(lambda x, y: x.direct_sum(y), lattices)

def get_lattice_signature(lattice):
    """
    Get signature (t+, t-) using native SageMath IntegralLattice methods.
    
    INPUT:
    - lattice: IntegralLattice object
    
    OUTPUT:
    - tuple (t_plus, t_minus) of positive and negative eigenvalue counts
    """
    return lattice.signature_pair()