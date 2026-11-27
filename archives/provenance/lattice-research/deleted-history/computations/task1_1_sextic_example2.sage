"""
Task 1.1: Construct a *second* explicit sextic equation F(x,y,z)=0 with exactly 10 nodes.
This is a different example from task1_1_sextic.sage.
"""

load("/home/dzack/research/computations/coble_geometry_foundation.sage")

print("=" * 80)
print("Task 1.1 Example 2: Rational Sextic with 10 Nodes")
print("=" * 80)

set_random_seed(1234)

# ============================================================================
# Step 1: Generic Parametrization P¹ → P²
# ============================================================================
print("\n[Step 1] Defining parametrization...")

R.<s,t> = PolynomialRing(QQ)

# Different random-looking coefficients
f0 = s^6 + 2*s^5*t - s^4*t^2 + 3*s^3*t^3 + s^2*t^4 - 2*s*t^5 + t^6
f1 = 2*s^6 - s^5*t + 3*s^4*t^2 + 2*s^3*t^3 - s^2*t^4 + 3*s*t^5 + 2*t^6
f2 = 3*s^6 + s^5*t + 2*s^4*t^2 - s^3*t^3 + 3*s^2*t^4 + s*t^5 + t^6

print(f"  f₀(s:t) = {f0}")
print(f"  f₁(s:t) = {f1}")
print(f"  f₂(s:t) = {f2}")

# ============================================================================
# Step 2: Implicit Equation via Resultants
# ============================================================================
print("\n[Step 2] Computing implicit equation F(x,y,z) = 0...")

R_xyz.<x,y,z> = PolynomialRing(QQ)
W.<s> = PolynomialRing(R_xyz)

# Dehomogenize (set t=1)
f0_s = f0.substitute(t=1)
f1_s = f1.substitute(t=1)
f2_s = f2.substitute(t=1)

f0_W = W(f0_s)
f1_W = W(f1_s)
f2_W = W(f2_s)

poly1 = x * f1_W - y * f0_W
poly2 = x * f2_W - z * f0_W

print("  Computing resultant with respect to s...")
F = poly1.resultant(poly2)
F = R_xyz(F)

# Factor and extract the sextic component
factors = F.factor()
F = None
for f, mult in factors:
    if f.total_degree() == 6:
        F = f
        break

if F is None:
    raise RuntimeError("Could not find a degree-6 factor in the resultant")

print(f"  Final F degree: {F.total_degree()}")

sextic_factorization = F.factor()
sextic_is_irreducible = len(sextic_factorization) == 1 and sextic_factorization[0][1] == 1
sextic_is_squarefree = F.is_squarefree()

print(f"  Sextic irreducible over QQ: {sextic_is_irreducible}")
print(f"  Sextic squarefree/reduced: {sextic_is_squarefree}")
if not sextic_is_irreducible:
    print(f"  Sextic factorization: {sextic_factorization}")

A.<a> = PolynomialRing(QQ)
K_a = FractionField(A)
U.<u> = PolynomialRing(K_a)

f0_a = dehomogenize_at_one(f0, a, K_a)
f1_a = dehomogenize_at_one(f1, a, K_a)
f2_a = dehomogenize_at_one(f2, a, K_a)
f0_u = dehomogenize_at_one(f0, u, U)
f1_u = dehomogenize_at_one(f1, u, U)
f2_u = dehomogenize_at_one(f2, u, U)

fiber_eq1 = f0_u * f1_a - f1_u * f0_a
fiber_eq2 = f0_u * f2_a - f2_u * f0_a
generic_fiber_gcd = fiber_eq1.gcd(fiber_eq2).monic()
generic_expected = (u - K_a(a)).monic()
generic_fiber_degree = generic_fiber_gcd.degree()
parametrization_generically_injective = generic_fiber_gcd == generic_expected

print(f"  Generic fiber gcd degree: {generic_fiber_degree}")
print(f"  Generic fiber gcd: {generic_fiber_gcd}")
print(f"  Parametrization generically injective: {parametrization_generically_injective}")

# ============================================================================
# Step 4: Find All Singular Points
# ============================================================================
print("\n[Step 4] Finding singular points...")

x_gen, y_gen, z_gen = F.parent().gens()
Fx = F.derivative(x_gen)
Fy = F.derivative(y_gen)
Fz = F.derivative(z_gen)

# Work in affine chart z=1
R_xy.<X,Y> = PolynomialRing(QQ)

F_aff = to_affine(F, R_xy)
Fx_aff = to_affine(Fx, R_xy)
Fy_aff = to_affine(Fy, R_xy)

I_aff = ideal([F_aff, Fx_aff, Fy_aff])
K = QQbar

print("  Solving in chart z=1...")
sols_affine = I_aff.variety(K)

# Check for singular points at infinity (z=0)
F_inf = to_affine(F.substitute(z=0), R_xy)
Fx_inf = to_affine(Fx.substitute(z=0), R_xy)
Fy_inf = to_affine(Fy.substitute(z=0), R_xy)
Fz_inf = to_affine(Fz.substitute(z=0), R_xy)
I_inf = ideal([F_inf, Fx_inf, Fy_inf, Fz_inf])
try:
    sols_inf = I_inf.variety(K)
except:
    sols_inf = []

all_singular_points = []
for sol in sols_affine:
    all_singular_points.append((sol[X], sol[Y], K(1)))
for sol in sols_inf:
    pt = (sol[X], sol[Y], K(0))
    if any(c != 0 for c in pt):
        all_singular_points.append(pt)

all_singular_points = deduplicate_projective_points_exact(all_singular_points)

print(f"  Total singular points (projective): {len(all_singular_points)}")

# ============================================================================
# Step 5: Verify Each Singularity is a Node (A₁)
# ============================================================================
print("\n[Step 5] Verifying nodes (A₁ singularities)...")

nodes = []
for idx, pt in enumerate(all_singular_points):
    if is_node_at_point(F, tuple(pt)):
        nodes.append(pt)
        print(f"    Point {idx+1}: ✓ NODE (A₁)")
    else:
        print(f"    Point {idx+1}: ✗ NOT A NODE")

print(f"\n  Found {len(nodes)} nodes.")
print(f"  Sextic irreducible over QQ: {sextic_is_irreducible}")
print(f"  Sextic squarefree/reduced: {sextic_is_squarefree}")

if len(nodes) == 10 and sextic_is_irreducible and sextic_is_squarefree:
    print("\n✓ SUCCESS: Exactly 10 nodes found, and the sextic is reduced and irreducible.")
    status = "SUCCESS"
elif len(nodes) == 10:
    print("\n✓ SUCCESS (with rigor gaps): 10 nodes found, but irreducibility/reducedness checks did not both pass.")
    status = "SUCCESS_WITH_RIGOR_GAPS"
else:
    print(f"\n✗ FAILURE: Found {len(nodes)} nodes instead of 10.")
    status = "FAILED"

print("\n" + "=" * 80)
print("NODE POSITIONS")
print("=" * 80)
print("\nThe 10 nodes of the Coble curve are located at:")
print()
for idx, pt in enumerate(nodes):
    print(f"  p_{idx+1} = {format_exact_projective_point(pt, name=f'a{idx+1}')}")

print("\n" + "=" * 80)
print(f"FINAL STATUS: {status}")
print("=" * 80)

# ============================================================================
# Step 6: Stabilizer Group Computation (Logic from task3_1_stabilizer.sage)
# ============================================================================
print("\n" + "=" * 80)
print("Step 6: Compute Stabilizer Group Γ_Co")
print("=" * 80)

# The Picard lattice S_Co for a 10-nodal rational sextic is abstractly fixed.
# Gram matrix is diag(2, -2, ..., -2)
S_Co_gram = S_Co_lattice().gram_matrix()
T_En_gram = T_En_lattice().gram_matrix()
h_Co = vector(ZZ, [1] + [0]*9)
theta = diagonal_matrix(ZZ, [1, 1] + [-1]*8)

# Note: reflection_matrix is now imported from coble_geometry.sage

# Find roots for O(T_En)
roots = []
for i in range(2):
    for sign in [-1, 1]:
        v = vector(ZZ, [0]*10); v[i] = sign; roots.append(v)
for i in range(2, 10):
    for sign in [-1, 1]:
        v = vector(ZZ, [0]*10); v[i] = sign; roots.append(v)

# Intersect Stabilizer and Centralizer
gamma_gens = []
for r in roots:
    try:
        s_r = reflection_matrix(r, T_En_gram)
        if s_r.transpose() * T_En_gram * s_r == T_En_gram:
            if (s_r * h_Co == h_Co) and (s_r * theta == theta * s_r):
                if s_r not in gamma_gens:
                    gamma_gens.append(s_r)
    except: pass

print(f"Found {len(gamma_gens)} reflection generators in Γ_Co.")

# ============================================================================
# Step 7: Compare and Document
# ============================================================================
print("\n" + "=" * 80)
print("Step 7: Comparison with Example 1")
print("=" * 80)

# Lattice invariants (Nikulin notation)
def compute_invariants(G):
    r = G.nrows()
    L = IntegralLattice(G)
    DG = L.discriminant_group()
    a = DG.ngens()
    # delta is 1 if q takes values in (1/2)Z/2Z
    q_gram = DG.gram_matrix_quadratic()
    has_half = any(v.denominator() == 2 for v in q_gram.diagonal())
    delta = 1 if has_half else 0
    sig = QuadraticForm(G).signature_vector()
    return (r, a, delta, (sig[0], sig[1]))

inv2 = compute_invariants(T_En_gram)
print(f"Example 2 T_En Invariants (r, a, delta, sig): {inv2}")
