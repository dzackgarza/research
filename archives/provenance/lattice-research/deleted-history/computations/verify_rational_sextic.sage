#!/usr/bin/env sage
r"""
Construct and verify a rational sextic with exactly 10 A1 nodes.

This script verifies that the curve defined by the implicit equation obtained
from the parametrization [P(t):R(t):Q(t)] has exactly 10 ordinary double
points (nodes/A1 singularities) and no other singularities.

Parametrization:
    [x : y : z] = [P(t) : R(t) : Q(t)]

where:
    P(t) = t^6 - t^5 - t^4 + t
    R(t) = -t^6 - t^5 + t^4 + t^2 - 1
    Q(t) = -t^6 + t^5 + t^3 - t^2 + 1

Verification checklist (all must pass):
    1. The curve is rational (image of P^1 under this parametrization).
    2. The implicit equation in P^2 is irreducible (a degree-6 form).
    3. There are exactly 10 singular points in the affine chart z = 1.
    4. There are no singular points at infinity (z = 0).
    5. Each singular point has nondegenerate Hessian => type A1 (node).
    6. The parametrization has exactly 20 ordered self-intersection pairs,
       which gives 10 unordered nodes. (Cusps would give fewer.)

The implicit equation was originally computed in SymPy via:
    import sympy as sp
    t, x, y = sp.symbols('t x y')
    P = t**6 - t**5 - t**4 + t
    R = -t**6 - t**5 + t**4 + t**2 - 1
    Q = -t**6 + t**5 + t**3 - t**2 + 1
    F = sp.expand(sp.resultant(P - x*Q, R - y*Q, t))

The result was:
    F = 137*x^6 - 79*x^5*y - 61*x^5*z - 244*x^4*y^2 - 423*x^4*y*z
        - 134*x^4*z^2 - 438*x^3*y^3 - 585*x^3*y^2*z - 128*x^3*y*z^2
        + 19*x^3*z^3 - 279*x^2*y^4 - 606*x^2*y^3*z - 395*x^2*y^2*z^2
        - 61*x^2*y*z^3 + 7*x^2*z^4 - 137*x*y^5 - 386*x*y^4*z
        - 550*x*y^3*z^2 - 479*x*y^2*z^3 - 212*x*y*z^4 - 34*x*z^5
        + 9*y^6 - 54*y^5*z - 256*y^4*z^2 - 385*y^3*z^3 - 276*y^2*z^4
        - 97*y*z^5 - 13*z^6
"""

# ===========================================================================
# Setup: define the parametrization polynomials
# ===========================================================================

# Create polynomial ring in t and define the parametrization
R_t.<t> = PolynomialRing(QQ)

# Parametrization: P^1 -> P^2 given by [P(t):R(t):Q(t)]
# These are homogeneous degree-6 polynomials in t
P = t^6 - t^5 - t^4 + t
R = -t^6 - t^5 + t^4 + t^2 - 1
Q = -t^6 + t^5 + t^3 - t^2 + 1

print("Parametrization [P(t):R(t):Q(t)] with:")
print(f"  P(t) = {P}")
print(f"  R(t) = {R}")
print(f"  Q(t) = {Q}")

# ===========================================================================
# Step 1: Compute the implicit equation by eliminating the parameter t
# ===========================================================================

# We eliminate t from the equations:
#     P - x*Q = 0   (i.e., [x:y:1] = [P:Q])
#     R - y*Q = 0
# The resultant with respect to t gives the implicit equation in x,y.

print("\n" + "="*60)
print("Step 1: Compute implicit equation via resultant")
print("="*60)

# Build the polynomial ring QQ[x,y][t]
Rxy.<x,y> = PolynomialRing(QQ, 2)
Rxyt.<t> = PolynomialRing(Rxy, 't')

# Convert P, R, Q to Rxyt
P_t = Rxyt(P)
R_t = Rxyt(R)
Q_t = Rxyt(Q)

# Form the equations: P - x*Q = 0 and R - y*Q = 0
# (In affine coordinates, we dehomogenize by dividing by Q)
Px = P_t - Rxyt(x)*Q_t
Rx = R_t - Rxyt(y)*Q_t

# Compute resultant to eliminate t
# This gives a polynomial in x,y of degree 6
F_affine = Px.resultant(Rx)
print(f"  Resultant degree in (x,y): {F_affine.total_degree()}")

# ===========================================================================
# Step 2: Verify the implicit equation is irreducible
# ===========================================================================

print("\n" + "="*60)
print("Step 2: Check irreducibility")
print("="*60)

factors = F_affine.factor()
print(f"  Number of irreducible factors: {len(factors)}")
for f, mult in factors:
    print(f"    degree {f.total_degree()}, multiplicity {mult}")

# Must be a single degree-6 factor with multiplicity 1
assert len(factors) == 1 and factors[0][1] == 1, "Curve is NOT irreducible!"
print("  PASS: implicit equation is irreducible")

# ===========================================================================
# Step 3: Homogenize and count singular points in chart z = 1
# ===========================================================================

print("\n" + "="*60)
print("Step 3: Count singular points in affine chart z = 1")
print("="*60)

# Homogenize to get a homogeneous polynomial in P^2
R3.<X,Y,Z> = PolynomialRing(QQ, 3)
F = R3(F_affine).homogenize(Z)
d = F.total_degree()
print(f"  Homogeneous degree: {d}")

# Dehomogenize by setting Z = 1 to work in affine chart
R2.<u,v> = PolynomialRing(QQ, 2)
f = R2(F.subs({X: u, Y: v, Z: 1}))

# Singular points satisfy f = df/du = df/dv = 0
# Solve via Groebner basis
I = Ideal([f, f.derivative(u), f.derivative(v)])
V = I.variety(QQbar)

print(f"  Singular points found: {len(V)}")
for i, pt in enumerate(V):
    print(f"    Point {i+1}: (u,v) = ({pt[u]}, {pt[v]})")

assert len(V) == 10, f"Expected 10 singular points, found {len(V)}"
print("  PASS: exactly 10 singular points in chart z=1")

# ===========================================================================
# Step 4: Verify no singularities at infinity (Z = 0)
# ===========================================================================

print("\n" + "="*60)
print("Step 4: Check for singularities at infinity")
print("="*60)

# At infinity, Z = 0. The polynomial restricted to Z = 0 is a binary form.
F_infinity = F.subs({Z: 0})
print(f"  Binary form at infinity: {F_infinity}")

# A singular point at infinity corresponds to a multiple root of this binary form.
# Check this by computing gcd(F_infinity(y,1), d/dy F_infinity(y,1)).
# If the gcd has degree > 0, there are multiple roots.
R1.<w> = PolynomialRing(QQ)
F_inf = R1(F_infinity.subs({X: w, Y: 1}))
g = F_inf.gcd(F_inf.derivative(w))
print(f"  gcd(F_inf(w), F_inf'(w)) = {g} (degree {g.degree()})")

assert g.degree() == 0, "Found multiple roots at infinity!"
print("  PASS: no singularities at infinity")

# ===========================================================================
# Step 5: Verify each singularity is A1 (nondegenerate Hessian)
# ===========================================================================

print("\n" + "="*60)
print("Step 5: Verify each singularity is type A1")
print("="*60)

# For a singularity to be A1 (a node), the quadratic term must be nondegenerate.
# This is equivalent to the Hessian determinant being nonzero.
f_uu = f.derivative(u, 2)
f_vv = f.derivative(v, 2)
f_uv = f.derivative(u).derivative(v)
hessian = f_uu * f_vv - f_uv^2

all_A1 = True
for i, pt in enumerate(V):
    u0 = pt[u]
    v0 = pt[v]
    h_val = QQbar(hessian.subs({u: u0, v: v0}))
    is_nonzero = h_val != 0
    print(f"  Point {i+1}: Hessian det = {h_val}, nondegenerate = {is_nonzero}")
    if not is_nonzero:
        all_A1 = False

assert all_A1, "Not all singularities are A1!"
print("  PASS: all 10 singularities are A1 (nondegenerate quadratic term)")

# ===========================================================================
# Step 6: Count self-intersections in the parametrization
# ===========================================================================

print("\n" + "="*60)
print("Step 6: Count self-intersection pairs in the parametrization")
print("="*60)

# The rational map P^1 -> P^2 has self-intersections where the same point
# on the curve corresponds to two different parameter values t ≠ s.
# Two points [P(t):R(t):Q(t)] and [P(s):R(s):Q(s)] in P^2 are equal
# iff all three 2×2 minors vanish:
#     det([P,R; P',R']) = P*R' - P'*R
#     det([P,Q; P',Q']) = P*Q' - P'*Q
#     det([R,Q; R',Q']) = R*Q' - R'*Q

S2.<t,s> = PolynomialRing(QQ, 2)

# Define P, R, Q as polynomials in t and in s
P_t = t^6 - t^5 - t^4 + t
R_t = -t^6 - t^5 + t^4 + t^2 - 1
Q_t = -t^6 + t^5 + t^3 - t^2 + 1

P_s = s^6 - s^5 - s^4 + s
R_s = -s^6 - s^5 + s^4 + s^2 - 1
Q_s = -s^6 + s^5 + s^3 - s^2 + 1

# The three 2×2 minors
minor_PR = P_t * R_s - P_s * R_t
minor_PQ = P_t * Q_s - P_s * Q_t
minor_RQ = R_t * Q_s - R_s * Q_t

# The diagonal t = s makes all three minors zero (trivially).
# Factor out (t - s) to exclude this case.
minor_PR_off = minor_PR // (t - s)
minor_PQ_off = minor_PQ // (t - s)
minor_RQ_off = minor_RQ // (t - s)

# Solve the system: all three minors = 0 with t ≠ s
I_self = Ideal([minor_PR_off, minor_PQ_off, minor_RQ_off])
V_self = I_self.variety(QQbar)

print(f"  Ordered self-intersection pairs (t,s) with t ≠ s: {len(V_self)}")

# Each unordered node corresponds to 2 ordered pairs (t,s) and (s,t).
# 10 nodes => 20 ordered pairs.
assert len(V_self) == 20, f"Expected 20 ordered pairs (10 nodes), found {len(V_self)}"
print("  PASS: 20 ordered pairs => 10 unordered nodes, no cusps")

# ===========================================================================
# Summary
# ===========================================================================

print("\n" + "="*60)
print("ALL VERIFICATION CHECKS PASSED")
print("="*60)
print("\nImplicit equation (homogenized):")
print(F)
print("\nThis polynomial can be used directly in variety_interface_spec.sage.")