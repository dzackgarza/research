"""
Central Geometry Module for Coble Project
================================================================================

This module provides common lattice constructions and verification functions
used across the Coble moduli space project.

Lattices:
  - U: Hyperbolic plane
  - E8: E8 root lattice (Cartan matrix)
  - Lambda_K3: K3 lattice U^3 + E8(-1)^2
  - S_Co: Coble Picard lattice diag(2, -2^10)
  - T_Co: Coble transcendental lattice diag(2^2, -2^9)

Utilities:
  - is_primitive_embedding: Check if M is a primitive embedding
  - is_node: Verify A1 singularity using 3x3 Hessian rank
"""

from sage.all import *

def hyperbolic_plane():
    """Hyperbolic plane U with Gram matrix [[0,1],[1,0]]."""
    return matrix(ZZ, [[0, 1], [1, 0]])

def E8_lattice(negative=True):
    """E8 root lattice with Cartan matrix, optionally negated."""
    E8_cartan = matrix(ZZ, [
        [ 2, -1,  0,  0,  0,  0,  0,  0],
        [-1,  2, -1,  0,  0,  0,  0,  0],
        [ 0, -1,  2, -1,  0,  0,  0,  0],
        [ 0,  0, -1,  2, -1,  0,  0,  0],
        [ 0,  0,  0, -1,  2, -1,  0, -1],
        [ 0,  0,  0,  0, -1,  2, -1,  0],
        [ 0,  0,  0,  0,  0, -1,  2,  0],
        [ 0,  0,  0,  0, -1,  0,  0,  2]
    ])
    return -E8_cartan if negative else E8_cartan

def K3_lattice():
    """K3 lattice Λ_K3 = U^3 + E8(-1)^2."""
    U = hyperbolic_plane()
    E8_neg = E8_lattice(negative=True)
    return block_diagonal_matrix([U, U, U, E8_neg, E8_neg])

def S_Co_gram():
    """Coble Picard lattice Gram matrix diag(2, -2, ..., -2)."""
    return diagonal_matrix(ZZ, [2] + [-2]*10)

def T_Co_gram():
    """Coble transcendental lattice expected Gram matrix diag(2, 2, -2, ..., -2)."""
    return diagonal_matrix(ZZ, [2, 2] + [-2]*9)

def get_Lambda_K3():
    """Return Λ_K3 as an IntegralLattice."""
    return IntegralLattice(K3_lattice())

def get_S_Co():
    """Return S_Co as an IntegralLattice."""
    return IntegralLattice(S_Co_gram())

def get_T_Co():
    """Return T_Co as an IntegralLattice."""
    return IntegralLattice(T_Co_gram())

def get_T_En():
    """Return T_En as an IntegralLattice."""
    # Enriques transcendental lattice has signature (2,8)
    return IntegralLattice(diagonal_matrix(ZZ, [2, 2] + [-2]*8))

def reflection_matrix(r, G):
    """Compute reflection matrix for root r in lattice with Gram matrix G.
    
    Formula: s_r(v) = v - 2*(v·r)/(r·r) * r
    In matrix form: s_r[i,j] = delta[i,j] - 2 * r[i] * (G*r)[j] / r_norm
    
    Args:
        r: Root vector (must be non-isotropic)
        G: Gram matrix of the lattice
        
    Returns:
        Reflection matrix as an integer matrix
    """
    n = G.nrows()
    r_norm = int(r * G * r)
    
    if r_norm == 0:
        raise ValueError("Root must be non-isotropic")
    
    s_r = matrix(QQ, n, n)
    Gr = G * r
    for i in range(n):
        for j in range(n):
            s_r[i,j] = (1 if i == j else 0) - QQ(2 * r[i] * Gr[j]) / r_norm
    return s_r.change_ring(ZZ)

def stabilizer_reflection_generators(T_En_gram, h_Co, theta):
    """Find reflection generators in the stabilizer Γ_Co of the Coble polarization."""
    n = T_En_gram.nrows()

    # Search for -2 roots
    roots = []
    for i in range(n):
        v = zero_vector(ZZ, n); v[i] = 1; roots.append(v)
    
    # Simple search for short roots (norm -2) in Enriques transcendental
    gamma_gens = []
    for r in roots:
        try:
            s_r = reflection_matrix(r, T_En_gram)
            if s_r.transpose() * T_En_gram * s_r == T_En_gram:
                if (s_r * h_Co == h_Co) and (s_r * theta == theta * s_r):
                    if s_r not in gamma_gens:
                        gamma_gens.append(s_r)
        except: pass
    return gamma_gens

def is_primitive_embedding(M):
    """Check if integer matrix M defines a primitive embedding into a lattice."""
    S, U, V = M.smith_form()
    # The Smith diagonal should have as many 1s as the rank (number of columns)
    diagonal = [S[i,i] for i in range(min(S.nrows(), S.ncols()))]
    return all(d == 1 for d in diagonal)

def saturate_embedding(M, L_gram):
    """
    Saturate the sublattice spanned by columns of M in lattice with L_gram.
    Returns a basis for (span(M) \otimes Q) \cap Z^n.
    """
    # M is n x k
    n, k = M.nrows(), M.ncols()
    D, U, V = M.smith_form()
    # M = U^-1 * D * V^-1
    U_inv = U.inverse()
    # Ensure it is integer matrix
    return U_inv.change_ring(ZZ)[:, :k]

def normalize_projective_point_exact(coords):
    """Return an exactly normalized projective point over QQbar."""
    P2 = ProjectiveSpace(QQbar, 2)
    pt = P2([QQbar(c) for c in coords])
    pt.normalize_coordinates()
    return pt

def deduplicate_projective_points_exact(coords_list):
    """Deduplicate projective points by exact projective equality."""
    unique_points = []
    for coords in coords_list:
        pt = normalize_projective_point_exact(coords)
        if not any(pt == existing for existing in unique_points):
            unique_points.append(pt)
    return unique_points

def point_over_minimal_number_field(pt, name='a'):
    """Base change an exact QQbar projective point to a small embedded number field."""
    K, coords, _ = number_field_elements_from_algebraics(list(pt), minimal=True,
                                                         embedded=True, name=name)
    P2 = ProjectiveSpace(K, 2)
    nf_pt = P2(coords)
    nf_pt.normalize_coordinates()
    return nf_pt

def sage_input_expression(obj):
    """Return the final exact expression line from Sage's algebraic renderer."""
    rendered = str(sage_input(obj))
    for line in reversed(rendered.splitlines()):
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            return stripped
    return rendered.strip()

def compact_exact_algebraic_expression(coord):
    """Render a QQbar element via its minpoly and isolating interval."""
    from sage.rings.qqbar import isolating_interval

    if coord in QQ:
        return sage_input_expression(QQ(coord))

    minpoly = coord.minpoly()
    interval = isolating_interval(lambda prec: ComplexIntervalField(prec)(coord), minpoly)
    root = QQbar.polynomial_root(AA.common_polynomial(minpoly), interval)
    return sage_input_expression(root)

def format_exact_projective_point(pt, name='a'):
    """Format a projective point using compact exact QQbar expressions."""
    normalized = normalize_projective_point_exact(tuple(pt))
    coords = [compact_exact_algebraic_expression(coord) for coord in normalized]
    return f"[{coords[0]} : {coords[1]} : {coords[2]}]"

def is_node_at_point(F, pt):
    """
    Verify if a singular point is a node (A1) using 3x3 Hessian rank.
    
    A point p is a node of a plane curve F(x,y,z)=0 iff rank(H(F)(p)) = 2.
    """
    R = F.parent()
    x, y, z = R.gens()
    
    px, py, pz = pt
    
    # Second partial derivatives
    H = matrix(QQbar, 3, 3)
    vars = [x, y, z]
    for i in range(3):
        for j in range(3):
            H[i,j] = F.derivative(vars[i], vars[j]).substitute(x=px, y=py, z=pz)
    
    return H.rank() == 2

def get_signature(L):
    """Return the (p, n) signature vector of an IntegralLattice."""
    G = L.gram_matrix()
    p, n, z = QuadraticForm(G).signature_vector()
    return (p, n)

def dehomogenize_at_one(poly, var, target_ring):
    """
    Dehomogenize a bivariate polynomial by setting one variable to 1.
    
    Args:
        poly: A polynomial in two variables
        var: The variable to keep (the other is set to 1)
        target_ring: The target polynomial ring for the result
    
    Returns:
        Univariate polynomial in target_ring
    """
    result = target_ring(0)
    for (i, j), coeff in poly.dict().items():
        result += target_ring(coeff) * var^i
    return result

def to_affine(poly, target_ring):
    """
    Convert homogeneous polynomial to affine form by setting z=1.
    
    Args:
        poly: A homogeneous polynomial in three variables (x, y, z)
        target_ring: The target polynomial ring (typically in two variables)
    
    Returns:
        Affine polynomial in target_ring
    
    Example:
        R.<x,y,z> = PolynomialRing(QQ)
        R_xy.<X,Y> = PolynomialRing(QQ)
        F = x^2 + y^2 + z^2
        F_aff = to_affine(F, R_xy)  # Returns X^2 + Y^2 + 1
    """
    result = target_ring(0)
    X, Y = target_ring.gens()
    
    # Substitute z=1 and extract coefficients
    poly_dehom = poly.substitute({poly.parent().gens()[2]: 1})
    
    for exponents, c in poly_dehom.dict().items():
        # exponents might be (i, j) or (i, j, 0) depending on the ring
        i = exponents[0]
        j = exponents[1]
        result += c * X^i * Y^j
    
    return result
