"""
Independent verification - using exact algebraic approach.
Load coble_geometry and replicate node finding.
"""

load("coble_geometry.sage")

# ============================================================================
# Step 1: Define the parametrization 
# ============================================================================
R.<s,t> = PolynomialRing(QQ)

f0 = s^6 + 2*s^5*t - s^4*t^2 + 3*s^3*t^3 + s^2*t^4 - 2*s*t^5 + t^6
f1 = 2*s^6 - s^5*t + 3*s^4*t^2 + 2*s^3*t^3 - s^2*t^4 + 3*s*t^5 + 2*t^6
f2 = 3*s^6 + s^5*t + 2*s^4*t^2 - s^3*t^3 + 3*s^2*t^4 + s*t^5 + t^6

print("Parametrization:")
print(f"  f0 = {f0}")
print(f"  f1 = {f1}")
print(f"  f2 = {f2}")

# ============================================================================
# Step 2: Compute implicit equation
# ============================================================================
R_xyz.<x,y,z> = PolynomialRing(QQ)
W.<s> = PolynomialRing(R_xyz)

f0_s = f0.substitute(t=1)
f1_s = f1.substitute(t=1)
f2_s = f2.substitute(t=1)

f0_W = W(f0_s)
f1_W = W(f1_s)
f2_W = W(f2_s)

poly1 = x * f1_W - y * f0_W
poly2 = x * f2_W - z * f0_W

print("\nComputing resultant...")
F = poly1.resultant(poly2)
F = R_xyz(F)

# Extract degree-6 factor
factors = F.factor()
F_sextic = None
for f, mult in factors:
    if f.total_degree() == 6:
        F_sextic = f
        break

F = F_sextic

print(f"Implicit equation degree: {F.total_degree()}")
print(f"Is irreducible: {len(F.factor()) == 1 and F.factor()[0][1] == 1}")
print(f"Is squarefree: {F.is_squarefree()}")

# ============================================================================
# Step 3: Find singular points
# ============================================================================
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

print("\nSolving in affine chart z=1...")
sols_affine = I_aff.variety(K)

# Check at infinity
F_inf = to_affine(F.substitute(z=0), R_xy)
Fx_inf = to_affine(Fx.substitute(z=0), R_xy)
Fy_inf = to_affine(Fy.substitute(z=0), R_xy)
Fz_inf = to_affine(Fz.substitute(z=0), R_xy)

I_inf = ideal([F_inf, Fx_inf, Fy_inf, Fz_inf])
try:
    sols_inf = I_inf.variety(K)
except:
    sols_inf = []

all_singular = []
for sol in sols_affine:
    all_singular.append((sol[X], sol[Y], K(1)))
for sol in sols_inf:
    pt = (sol[X], sol[Y], K(0))
    if any(c != 0 for c in pt):
        all_singular.append(pt)

all_singular = deduplicate_projective_points_exact(all_singular)

print(f"Total singular points: {len(all_singular)}")

# ============================================================================
# Step 4: Verify each is a node
# ============================================================================
print("\nVerifying nodes...")
nodes = []
for idx, pt in enumerate(all_singular):
    if is_node_at_point(F, pt):
        nodes.append(pt)
        print(f"  p{idx+1}: ✓ NODE (A1)")
    else:
        print(f"  p{idx+1}: ✗ NOT A NODE")

print(f"\nTotal nodes: {len(nodes)}")

# ============================================================================
# Step 5: Verify one node with full detail
# ============================================================================
if nodes:
    pt = nodes[0]
    px, py, pz = pt
    
    print("\n" + "=" * 60)
    print("DETAILED VERIFICATION OF FIRST NODE")
    print("=" * 60)
    
    print(f"\nPoint coordinates: ({px}, {py}, {pz})")
    print(f"\nApproximate: ({complex(px):.8f}, {complex(py):.8f}, {complex(pz):.8f})")
    
    F_val = F(px, py, pz)
    Fx_val = Fx(px, py, pz)
    Fy_val = Fy(px, py, pz)
    Fz_val = Fz(px, py, pz)
    
    print(f"\nSingularity conditions:")
    print(f"  F(p)  = {F_val}")
    print(f"  Fx(p) = {Fx_val}")
    print(f"  Fy(p) = {Fy_val}")
    print(f"  Fz(p) = {Fz_val}")
    
    is_zero = (F_val == 0 and Fx_val == 0 and Fy_val == 0 and Fz_val == 0)
    print(f"\n  All zero (exact): {is_zero}")
    
    H = matrix([[F.derivative(x_gen, x_gen), F.derivative(x_gen, y_gen), F.derivative(x_gen, z_gen)],
                [F.derivative(y_gen, x_gen), F.derivative(y_gen, y_gen), F.derivative(y_gen, z_gen)],
                [F.derivative(z_gen, x_gen), F.derivative(z_gen, y_gen), F.derivative(z_gen, z_gen)]])
    
    H_val = H(px, py, pz)
    print(f"\nHessian matrix at p:")
    print(H_val)
    
    H_rank = H_val.rank()
    print(f"\nHessian rank: {H_rank}")
    print(f"Is A1 (rank 2): {H_rank == 2}")
    
    print("\n" + "=" * 60)
    if is_zero and H_rank == 2:
        print("✓ VERIFICATION PASSED")
        print("  Point is a mathematically verified A1 singularity (node)")
    else:
        print("✗ VERIFICATION FAILED")
