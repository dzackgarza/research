#!/usr/bin/env sage
"""
Search for a rational sextic with exactly 10 A1 nodes.

Strategy:
1. Sample small integer coefficients for three homogeneous sextics f0, f1, f2
2. Reject cases with common factor or non-birational image
3. Compute the image curve via elimination
4. Keep the first candidate whose singular locus has 10 reduced points, all A1
5. Output the implicit polynomial
"""

def sample_sextic_coeffs(max_coeff=3):
    """Generate random small integer coefficients for a homogeneous sextic."""
    coeffs = [randint(-max_coeff, max_coeff) for _ in range(7)]
    # Ensure not all zero
    if all(c == 0 for c in coeffs):
        coeffs[0] = 1
    return coeffs

def coeffs_to_poly(coeffs, s, t):
    """Convert coefficient list [a0,...,a6] to a0*s^6 + a1*s^5*t + ... + a6*t^6."""
    return sum(coeffs[i] * s^(6-i) * t^i for i in range(7))

def has_common_factor(f0, f1, f2):
    """Check if three polynomials have a common factor."""
    g = gcd(gcd(f0, f1), f2)
    return g != 1

def compute_implicit_curve(f0, f1, f2):
    """
    Compute implicit equation of the curve parametrized by [f0:f1:f2].
    Eliminate s,t from the system: x*f2 - z*f0 = 0, y*f2 - z*f1 = 0.
    """
    # Create polynomial ring with lex order to eliminate s,t
    S = PolynomialRing(CC, 's,t,x,y,z', order='lex')
    s, t, x, y, z = S.gens()

    # f0, f1, f2 are already in S, just use them directly
    eq1 = x * f2 - z * f0
    eq2 = y * f2 - z * f1

    # Compute Groebner basis
    G = S.ideal([eq1, eq2]).groebner_basis()

    # Find the polynomial not involving s,t
    for g in G:
        if s not in g.variables() and t not in g.variables():
            return g

    return None

def check_curve_properties(F):
    """Check if the curve defined by F has the desired properties."""
    try:
        C = Variety(F)

        # Check degree
        if C.degree() != 6:
            return False, "degree != 6"

        # Check normalization is P^1
        if not C.normalization().is_isomorphic_to(PP^1(CC)):
            return False, "normalization not P^1"

        # Check singular locus
        C_sing = C.singular_locus()

        if not C_sing.is_finite():
            return False, "singular locus not finite"

        if C_sing.cardinality() != 10:
            return False, f"wrong number of singularities: {C_sing.cardinality()}"

        # Check all singularities are A1
        for p in C_sing.points():
            if p.singularity_type() != Singularity("A1"):
                return False, f"non-A1 singularity: {p.singularity_type()}"

        return True, "valid"

    except Exception as e:
        return False, f"error: {e}"

def search(max_attempts=1000, max_coeff=3):
    """Search for a valid rational sextic."""
    for attempt in range(max_attempts):
        if attempt % 100 == 0:
            print(f"Attempt {attempt}/{max_attempts}")

        # Create polynomial ring for parametrization
        R.<s,t> = PolynomialRing(CC, 2)

        # Sample three sextics
        coeffs0 = sample_sextic_coeffs(max_coeff)
        coeffs1 = sample_sextic_coeffs(max_coeff)
        coeffs2 = sample_sextic_coeffs(max_coeff)

        f0 = coeffs_to_poly(coeffs0, s, t)
        f1 = coeffs_to_poly(coeffs1, s, t)
        f2 = coeffs_to_poly(coeffs2, s, t)

        # Check for common factor
        if has_common_factor(f0, f1, f2):
            continue

        # Compute implicit curve
        F = compute_implicit_curve(f0, f1, f2)

        if F is None:
            continue

        # Check properties
        valid, msg = check_curve_properties(F)

        if valid:
            print(f"\nFound valid curve at attempt {attempt}!")
            print(f"Parametrization:")
            print(f"  f0 = {f0}")
            print(f"  f1 = {f1}")
            print(f"  f2 = {f2}")
            print(f"\nImplicit equation:")
            print(f"  F = {F}")
            return F, (f0, f1, f2)
        else:
            if attempt % 100 == 0:
                print(f"  Rejected: {msg}")

    print("\nNo valid curve found")
    return None, None

if __name__ == "__main__":
    F, param = search()
    if F is not None:
        print("\n" + "="*60)
        print("SUCCESS: Valid rational sextic found")
        print("="*60)
        print(f"\nPaste this into variety_interface_spec.sage:")
        print(f"F = {F}")
