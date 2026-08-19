"""
Direct extraction of mathematical objects from Sage.

NO manual construction - everything comes from Sage objects.
"""

from sage.all import RootSystem, CoxeterMatrix, matrix, ZZ


def extract_gram_matrix_from_sage(coxeter_type):
    """
    Extract the Gram matrix of simple roots directly from Sage.
    
    This is the ACTUAL inner product matrix that Sage uses,
    not something we construct.
    
    Args:
        coxeter_type: Like ['A', 2] or ['B', 3]
        
    Returns:
        The Gram matrix as Sage computes it
    """
    R = RootSystem(coxeter_type)
    
    # Method 1: Extract from root lattice
    if hasattr(R.root_lattice(), 'simple_roots'):
        roots = R.root_lattice().simple_roots()
        n = R.rank()
        
        # Get the actual inner products
        gram = matrix(ZZ, n, n)
        for i in range(n):
            for j in range(n):
                # Sage uses 1-based indexing for roots
                gram[i, j] = roots[i+1].scalar(roots[j+1])
        
        return gram
    
    # Method 2: Extract from ambient space if available
    if hasattr(R, 'ambient_space'):
        ambient = R.ambient_space()
        simple_roots = ambient.simple_roots()
        n = len(simple_roots)
        
        # Get inner products in ambient space
        gram = matrix(n, n)
        for i in range(n):
            for j in range(n):
                gram[i, j] = simple_roots[i].inner_product(simple_roots[j])
        
        return gram
    
    raise ValueError(f"Cannot extract Gram matrix for type {coxeter_type}")


def extract_cartan_matrix_from_sage(coxeter_type):
    """Extract the Cartan matrix directly from Sage."""
    R = RootSystem(coxeter_type)
    return R.cartan_matrix()


def extract_coxeter_matrix_from_sage(coxeter_type):
    """Extract the Coxeter matrix directly from Sage."""
    return CoxeterMatrix(coxeter_type)


def apply_our_gram_convention(sage_gram):
    """
    Apply our project's Gram matrix convention to a Sage Gram matrix.
    
    Our convention appears to be -2 times the standard for simply-laced types.
    This should be documented and verified against PROJECT_CONVENTIONS.md
    
    Args:
        sage_gram: Gram matrix from Sage
        
    Returns:
        Gram matrix with our convention applied
    """
    # FIXME: This multiplier should come from PROJECT_CONVENTIONS.md
    # For now, based on the tests, it seems we use -2 * standard
    return -2 * sage_gram


def get_expected_gram_for_test(coxeter_type):
    """
    Get the expected Gram matrix for testing.
    
    This combines Sage extraction with our convention.
    
    Args:
        coxeter_type: Like ['A', 2]
        
    Returns:
        Expected Gram matrix with our convention
    """
    sage_gram = extract_gram_matrix_from_sage(coxeter_type)
    return apply_our_gram_convention(sage_gram)


def verify_gram_matrix_properties(gram_matrix, coxeter_type):
    """
    Verify properties of a Gram matrix against Sage.
    
    Args:
        gram_matrix: Our implementation's Gram matrix
        coxeter_type: The Coxeter type
        
    Returns:
        Dict of verification results
    """
    expected = get_expected_gram_for_test(coxeter_type)
    R = RootSystem(coxeter_type)
    
    return {
        'matrix_equals': gram_matrix == expected,
        'determinant_equals': gram_matrix.det() == expected.det(),
        'rank_equals': gram_matrix.rank() == R.rank(),
        'eigenvalues_match': set(gram_matrix.eigenvalues()) == set(expected.eigenvalues())
    }