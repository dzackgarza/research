"""
Smith normal form utilities for computing orthogonal complements using proper SageMath methods.
"""

def compute_orthogonal_complement_smith(lattice, vector):
    """
    Compute orthogonal complement of vector using Smith normal form.
    
    INPUT:
    - lattice: IntegralLattice object
    - vector: vector in the lattice
    
    OUTPUT:
    - basis for orthogonal complement as list of vectors
    - Smith normal form data (D, U, V)
    """
    G = lattice.gram_matrix()
    
    # Compute dual vector v̂ = v * G  
    v_hat = vector * G
    
    # Smith normal form of [v̂]
    A = matrix([v_hat])
    D, U, V = A.smith_form()
    
    # Extract orthogonal complement from V
    # Columns 2 through n of V give the orthogonal complement
    complement_basis = []
    for j in range(1, V.ncols()):
        complement_basis.append(V.column(j))
    
    return complement_basis, (D, U, V)

def verify_orthogonal_complement(lattice, original_vector, complement_basis):
    """
    Verify that the complement basis is indeed orthogonal to the original vector.
    
    INPUT:
    - lattice: IntegralLattice object
    - original_vector: the vector whose complement we computed
    - complement_basis: list of vectors forming the complement basis
    
    OUTPUT:
    - True if all inner products are zero, False otherwise
    """
    G = lattice.gram_matrix()
    
    for k in complement_basis:
        # Use manual computation for rational vectors from Smith normal form
        inner_product = original_vector * G * k
        if inner_product != 0:
            print(f"Error: (v, k) = {inner_product} ≠ 0 for k = {k}")
            return False
    
    return True

def compute_complement_gram_matrix(lattice, complement_basis):
    """
    Compute Gram matrix for the orthogonal complement sublattice.
    
    INPUT:
    - lattice: IntegralLattice object
    - complement_basis: basis vectors for the complement
    
    OUTPUT:
    - Gram matrix of the complement as a sublattice
    """
    if not complement_basis:
        return matrix(QQ, 0, 0)
    
    G = lattice.gram_matrix()
    
    # Compute inner products between basis vectors
    # Use manual computation for rational vectors from Smith normal form
    complement_gram = matrix(QQ, len(complement_basis), len(complement_basis))
    for i, u in enumerate(complement_basis):
        for j, v in enumerate(complement_basis):
            complement_gram[i, j] = u * G * v
    
    return complement_gram

def analyze_orthogonal_complement(lattice, vector, verbose=True):
    """
    Complete analysis of orthogonal complement including Smith form and verification.
    
    INPUT:
    - lattice: IntegralLattice object  
    - vector: vector to find complement of
    - verbose: whether to print detailed information
    
    OUTPUT:
    - dictionary with complement_basis, gram_matrix, smith_data, determinant
    """
    if verbose:
        print(f"Analyzing orthogonal complement of v = {vector}")
    
    # Compute complement using Smith normal form
    complement_basis, smith_data = compute_orthogonal_complement_smith(lattice, vector)
    D, U, V = smith_data
    
    if verbose:
        print(f"Smith normal form: D = {D}")
        print(f"Found {len(complement_basis)} basis vectors for v⊥")
    
    # Verify orthogonality
    is_orthogonal = verify_orthogonal_complement(lattice, vector, complement_basis)
    if verbose:
        print(f"Orthogonality verified: {is_orthogonal}")
    
    # Compute Gram matrix of complement
    complement_gram = compute_complement_gram_matrix(lattice, complement_basis)
    if verbose and complement_gram.nrows() > 0:
        print(f"Gram matrix of v⊥:")
        print(complement_gram)
        print(f"Determinant: {complement_gram.determinant()}")
    
    return {
        'complement_basis': complement_basis,
        'gram_matrix': complement_gram, 
        'smith_data': smith_data,
        'determinant': complement_gram.determinant() if complement_gram.nrows() > 0 else 1,
        'is_orthogonal': is_orthogonal
    }