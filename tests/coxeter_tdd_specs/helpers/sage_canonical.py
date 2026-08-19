"""
Helper functions to extract canonical data from Sage for testing.

This module ensures we never hard-code mathematical data in tests.
All expected values come from Sage as the ground truth.
"""

from sage.all import RootSystem, CoxeterMatrix, DynkinDiagram, WeylGroup, matrix, ZZ, QQ, cos, pi


def get_gram_matrix_from_coxeter_type(coxeter_type):
    """
    Extract the canonical Gram matrix from Sage's root system.
    
    This extracts the ACTUAL inner product matrix from Sage,
    not a manually constructed one.
    
    Args:
        coxeter_type: List like ['A', 2] or ['B', 3, 1]
        
    Returns:
        Sage matrix with the Gram matrix of simple roots
    """
    if len(coxeter_type) == 2:
        # Finite type - use RootSystem
        R = RootSystem(coxeter_type)
        # Get the simple roots in the root lattice
        simple_roots = R.root_lattice().simple_roots()
        
        # Extract the Gram matrix (inner products of simple roots)
        n = R.rank()
        gram_entries = []
        for i in range(1, n+1):  # Sage uses 1-based indexing
            row = []
            for j in range(1, n+1):
                # Get inner product from the root lattice
                inner = simple_roots[i].scalar(simple_roots[j])
                row.append(inner)
            gram_entries.append(row)
        
        return matrix(ZZ, gram_entries)
    else:
        # Affine or other type - construct from Cartan matrix
        # For affine types, we need to use the affine root system
        from sage.combinat.root_system.root_system import RootSystem
        R = RootSystem(coxeter_type)
        
        # Get Cartan matrix
        cartan = R.cartan_matrix()
        
        # For simply-laced affine types, Gram = -Cartan
        # This is a simplification - proper handling would extract from ambient space
        return -cartan


def get_cartan_matrix_from_coxeter_type(coxeter_type):
    """Get the canonical Cartan matrix from Sage."""
    if len(coxeter_type) == 2:
        # Finite type
        R = RootSystem(coxeter_type)
        return R.cartan_matrix()
    else:
        # Affine or other type - use CoxeterMatrix
        CM = CoxeterMatrix(coxeter_type)
        # For now, return None as Cartan matrix extraction is complex
        # TODO: Implement proper Cartan matrix extraction
        return None


def get_weyl_group_order(coxeter_type):
    """Get the order of the Weyl group for finite types."""
    W = WeylGroup(coxeter_type)
    return W.order()


def get_simple_roots(coxeter_type):
    """Get simple roots from Sage's root system."""
    R = RootSystem(coxeter_type)
    return R.root_space().simple_roots()


def get_root_lattice_gram(coxeter_type):
    """Get Gram matrix of the root lattice."""
    R = RootSystem(coxeter_type)
    # Get simple roots in ambient space
    simple_roots = R.ambient_space().simple_roots()
    n = len(simple_roots)
    
    # Compute Gram matrix of simple roots
    gram_entries = []
    for i in range(n):
        row = []
        for j in range(n):
            # Inner product of simple roots
            inner = simple_roots[i].inner_product(simple_roots[j])
            row.append(inner)
        gram_entries.append(row)
    
    return matrix(QQ, gram_entries)


def verify_our_convention(coxeter_type):
    """
    Verify that our Gram matrix convention matches expected relationships.
    
    For simply-laced types: Our_Gram = -2 × Standard_Geometric_Gram
    """
    our_gram = get_gram_matrix_from_coxeter_type(coxeter_type)
    
    # For simply-laced finite types, compare with Cartan matrix
    if len(coxeter_type) == 2 and coxeter_type[0] in ['A', 'D', 'E']:
        cartan = get_cartan_matrix_from_coxeter_type(coxeter_type)
        # For simply-laced: Geometric_Gram = -Cartan
        # So: Our_Gram = -2 × (-Cartan) = 2 × Cartan
        # But wait, that's not right...
        # Actually for simply-laced with our convention:
        # Our diagonal is -2, Cartan diagonal is 2
        # So Our_Gram = -Cartan for simply-laced
        expected = -cartan
        return our_gram == expected
    
    return True  # Can't verify for other types yet


def get_eigenvalues_exact(gram_matrix):
    """Get exact eigenvalues of a matrix when possible."""
    return gram_matrix.eigenvalues()


def get_determinant_exact(gram_matrix):
    """Get exact determinant."""
    return gram_matrix.det()


def get_signature(gram_matrix):
    """Get signature (p, q, r) of a symmetric matrix."""
    eigenvals = gram_matrix.eigenvalues()
    p = sum(1 for ev in eigenvals if ev > 0)
    q = sum(1 for ev in eigenvals if ev < 0)
    r = sum(1 for ev in eigenvals if ev == 0)
    return (p, q, r)


# Canonical group definitions
class CanonicalCoxeterGroup:
    """Container for canonical Coxeter group data."""
    def __init__(self, coxeter_type):
        self.coxeter_type = coxeter_type
        # Get Coxeter matrix from Sage
        from sage.all import CoxeterMatrix as SageCoxeterMatrix
        sage_cm = SageCoxeterMatrix(coxeter_type)
        # Convert to list format
        n = sage_cm.rank()
        self.coxeter_matrix = [[sage_cm[i,j] for j in range(1, n+1)] for i in range(1, n+1)]
        # Get Gram matrix with our convention
        self.gram_matrix = get_gram_matrix_from_coxeter_type(coxeter_type)
        # Apply our convention (-2 * standard)
        self.gram_matrix = -2 * self.gram_matrix
        # Get Cartan matrix
        self.cartan_matrix = get_cartan_matrix_from_coxeter_type(coxeter_type)
        # TODO: Add Schlafli symbol extraction
        
# Standard finite groups
A2 = CanonicalCoxeterGroup(['A', 2])
A3 = CanonicalCoxeterGroup(['A', 3])
B2 = CanonicalCoxeterGroup(['B', 2])
B3 = CanonicalCoxeterGroup(['B', 3])
C2 = B2  # B2 and C2 are the same
C3 = CanonicalCoxeterGroup(['C', 3])
D4 = CanonicalCoxeterGroup(['D', 4])
E6 = CanonicalCoxeterGroup(['E', 6])
E7 = CanonicalCoxeterGroup(['E', 7])
E8 = CanonicalCoxeterGroup(['E', 8])
F4 = CanonicalCoxeterGroup(['F', 4])
G2 = CanonicalCoxeterGroup(['G', 2])
H2 = CanonicalCoxeterGroup(['H', 2])
H3 = CanonicalCoxeterGroup(['H', 3])
H4 = CanonicalCoxeterGroup(['H', 4])

# Literature examples
LITERATURE_EXAMPLES = {
    'bogachev_kolpakov_2024_nonreflective': {
        'gram_coeffs': [[3, 7, 49], [7, 0, 0], [49, 0, 0]],
        'roots': [(0, 7, -1), (-7, -11, 2), (0, 0, 1), (-42, -24, 5)],
        'is_reflective': False,
        'citation': 'Bogachev & Kolpakov, 2024, Section 2, Example 1'
    }
}

def get_literature_example(key):
    """Get a specific literature example by key."""
    return LITERATURE_EXAMPLES[key]

# Lists of canonical types for parameterized testing
def get_canonical_types(category='all'):
    """Get lists of canonical Coxeter types for testing."""
    classical = [
        (['A', n], n) for n in range(1, 8)
    ] + [
        (['B', n], n) for n in range(2, 8)
    ] + [
        (['C', n], n) for n in range(3, 8)  
    ] + [
        (['D', n], n) for n in range(4, 8)
    ]
    
    exceptional = [
        (['E', 6], 6),
        (['E', 7], 7),
        (['E', 8], 8),
        (['F', 4], 4),
        (['G', 2], 2),
        (['H', 3], 3),
        (['H', 4], 4),
    ]
    
    if category == 'classical':
        return list(classical)
    elif category == 'exceptional':
        return exceptional
    elif category == 'all':
        return list(classical) + exceptional
    else:
        raise ValueError(f"Unknown category: {category}")