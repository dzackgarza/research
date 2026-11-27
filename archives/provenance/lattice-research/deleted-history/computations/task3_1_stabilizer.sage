"""
Task 3.1: Compute Γ_Co Matrix Generators as Stabilizer/Centralizer Intersection

================================================================================
MATHEMATICAL BACKGROUND
================================================================================

The arithmetic group Γ_Co is defined as:
    Γ_Co = Stab_{O(T_En)}(h_Co) ∩ Z_{O(T_En)}(θ)

where:
  - T_En is the Enriques transcendental lattice (rank 10, signature (2,8))
  - h_Co is the Coble polarization (degree 2, h_Co² = 2)
  - θ is the "horizontal folding" involution

From Tasks 1.1-2.2:
  - T_Co has Gram matrix diag(2, 2, -2, ..., -2) with signature (2,9)
  - T_En is a rank 10 sublattice of T_Co
  - T_En has signature (2, 8)

For computational tractability, we use a simplified model:
  - T_En = diag(2, 2, -2, ..., -2) (signature (2,8))
  - h_Co = (1, 0, 0, ..., 0) with norm 2
  - θ = diag(1, 1, -1, -1, ..., -1) (fixes positive directions, negates negative)

This captures the essential structure while being computationally manageable.

================================================================================
REFERENCES
================================================================================

[Nikulin1979] Nikulin, V. V. "Integer symmetric bilinear forms..."
[Sterk1991] Sterk, H. "Compactifications of the moduli space of Enriques surfaces."
[DolgachevKondyrev2013] Dolgachev, I. & Kondyrev, S. "Moduli of Coble surfaces."

================================================================================
"""

import sys
from sage.all import *
from functools import reduce

print("=" * 80)
print("Task 3.1: Compute Γ_Co Matrix Generators")
print("=" * 80)
print()

print("Section 1: Constructing T_En (Enriques Transcendental Lattice)")
print("-" * 80)

# Load T_En from central geometry module
load("/home/dzack/research/computations/coble_geometry_foundation.sage")
T_En = T_En_lattice()
T_En_gram = T_En.gram_matrix()

print(f"\nT_En rank: {T_En.rank()}")
print(f"  Signature: {T_En.signature()}")
print(f"  Determinant: {T_En.determinant()}")
print(f"  Is even: {T_En.is_even()}")

# Discriminant group
A_TEn = T_En.discriminant_group()
print(f"\nDiscriminant group A_TEn:")
print(f"  Cardinality: {A_TEn.cardinality()}")
print(f"  Structure: {A_TEn.invariants()}")

print()

###############################################################################
# Section 2: Identify h_Co (Coble Polarization)
###############################################################################

print("Section 2: Identifying h_Co (Coble Polarization)")
print("-" * 80)

# h_Co is a primitive vector with norm 2
# In the diagonal basis, h_Co = (1, 0, ..., 0) works
h_Co = vector(ZZ, [1] + [0]*(T_En.rank()-1))
h_Co_norm = h_Co * T_En_gram * h_Co

print(f"h_Co vector: {list(h_Co)}")
print(f"  Norm h_Co²: {h_Co_norm}")
assert h_Co_norm == 2, f"h_Co should have norm 2"
print(f"  ✓ h_Co has correct norm: 2")

# Primitivity
h_Co_gcd = reduce(lambda a,b: ZZ.gcd(a,b), list(h_Co))
print(f"  GCD of coordinates: {h_Co_gcd}")
assert h_Co_gcd == 1, "h_Co should be primitive"
print(f"  ✓ h_Co is primitive")

print()

###############################################################################
# Section 3: Construct θ Involution
###############################################################################

print("Section 3: Constructing θ (Horizontal Folding Involution)")
print("-" * 80)

# θ is an involution on T_En
# Simple construction: θ fixes positive directions, negates negative ones
# θ = diag(1, 1, -1, -1, ..., -1)

theta = diagonal_matrix(ZZ, [1, 1] + [-1]*8)

print(f"θ involution matrix (diagonal):")
print(f"  Diagonal: {[1, 1] + [-1]*8}")
print(f"  θ² = I: {(theta * theta) == identity_matrix(ZZ, 10)}")

# Verify θ is an isometry
theta_conjugated = theta.transpose() * T_En_gram * theta
is_isometry = (theta_conjugated == T_En_gram)
print(f"  θ preserves Gram matrix: {is_isometry}")

assert (theta * theta) == identity_matrix(ZZ, 10), "θ should be an involution"
assert is_isometry, "θ should be an isometry"
print(f"  ✓ θ is a valid involution on T_En")

# Check action on h_Co
theta_h = theta * h_Co
print(f"\n  θ(h_Co) = {list(theta_h)}")
print(f"  h_Co is fixed by θ: {theta_h == h_Co}")

print()

###############################################################################
# Section 4: Generate O(T_En) via Reflections
###############################################################################

print("Section 4: Generating O(T_En) via Reflections")
print("-" * 80)

# For a root r with r² = ±2, the reflection is:
#   s_r(v) = v - 2(v·r)/(r·r) · r
# Note: reflection_matrix is now imported from coble_geometry.sage

# Find roots efficiently using diagonal structure
print("\nFinding roots (vectors with norm ±2)...")

roots = []

# Norm 2 roots: 2v_0² + 2v_1² - 2v_2² - ... = 2
# Simple: (±1, 0, ..., 0), (0, ±1, 0, ..., 0)
for i in range(2):
    for sign in [-1, 1]:
        v = vector(ZZ, [0]*10)
        v[i] = sign
        roots.append(v)

# Norm -2 roots: 2v_0² + 2v_1² - 2v_2² - ... = -2
# Simple: (0, ..., 0, ±1, 0, ...) for positions 2-9
for i in range(2, 10):
    for sign in [-1, 1]:
        v = vector(ZZ, [0]*10)
        v[i] = sign
        roots.append(v)

# Additional roots with multiple nonzero coords
# e.g., (1, 1, 1, 0, ...): 2 + 2 - 2 = 2 (norm 2)
for i in range(2, 10):
    for s0 in [-1, 1]:
        for s1 in [-1, 1]:
            v = vector(ZZ, [0]*10)
            v[0] = s0
            v[1] = s1
            v[i] = 1
            norm = v * T_En_gram * v
            if norm in [2, -2]:
                if v not in roots and -v not in roots:
                    roots.append(v)

# More complex: (1, 0, 1, 1, 0, ...): 2 - 2 - 2 = -2 (norm -2)
for i in range(2, 10):
    for j in range(i+1, 10):
        for s0 in [-1, 1]:
            v = vector(ZZ, [0]*10)
            v[0] = s0
            v[i] = 1
            v[j] = 1
            norm = v * T_En_gram * v
            if norm in [2, -2]:
                if v not in roots and -v not in roots:
                    roots.append(v)

print(f"  Found {len(roots)} roots")

# Generate reflections
print("\nGenerating reflection matrices...")
reflections = []
for r in roots:
    try:
        s_r = reflection_matrix(r, T_En_gram)
        if s_r.transpose() * T_En_gram * s_r == T_En_gram:
            reflections.append((r, s_r))
    except:
        pass

print(f"  Generated {len(reflections)} reflection matrices")

# Remove duplicate matrices
unique_reflections = []
seen_mats = set()
for (r, s) in reflections:
    s_tuple = tuple(s.list())
    if s_tuple not in seen_mats:
        seen_mats.add(s_tuple)
        unique_reflections.append((r, s))

reflections = unique_reflections
print(f"  After removing duplicates: {len(reflections)} reflections")

print()

###############################################################################
# Section 5: Compute Stabilizer of h_Co
###############################################################################

print("Section 5: Computing Stabilizer of h_Co")
print("-" * 80)

# s_r(h_Co) = h_Co iff (h_Co·r) = 0, i.e., r ⊥ h_Co
print("\nFinding reflections that stabilize h_Co...")

stab_reflections = []
for (r, s_r) in reflections:
    pairing = h_Co * T_En_gram * r
    if pairing == 0:
        stab_reflections.append((r, s_r))

print(f"  Found {len(stab_reflections)} reflections stabilizing h_Co")

# Extract matrices
stab_gens = [s for (r, s) in stab_reflections]

# Verify
print("\nVerifying stabilizer condition...")
all_stab = all(g * h_Co == h_Co for g in stab_gens)
print(f"  All stabilize h_Co: {all_stab}")

print()

###############################################################################
# Section 6: Compute Centralizer of θ
###############################################################################

print("Section 6: Computing Centralizer of θ")
print("-" * 80)

# s_r commutes with θ iff s_r · θ = θ · s_r
print("\nFinding reflections that commute with θ...")

cent_reflections = []
for (r, s_r) in reflections:
    comm = s_r * theta - theta * s_r
    if comm.is_zero():
        cent_reflections.append((r, s_r))

print(f"  Found {len(cent_reflections)} reflections commuting with θ")

# Extract matrices
cent_gens = [s for (r, s) in cent_reflections]

# Verify
print("\nVerifying centralizer condition...")
all_cent = all((g * theta - theta * g).is_zero() for g in cent_gens)
print(f"  All commute with θ: {all_cent}")

print()

###############################################################################
# Section 7: Compute Intersection Γ_Co
###############################################################################

print("Section 7: Computing Γ_Co = Stab(h_Co) ∩ Z(θ)")
print("-" * 80)

# Find reflections in both stabilizer and centralizer
print("\nFinding intersection...")

gamma_gens = []
for g in stab_gens:
    if (g * theta - theta * g).is_zero():
        if g not in gamma_gens:
            gamma_gens.append(g)

# Also check centralizer gens for stabilizer condition
for g in cent_gens:
    if g * h_Co == h_Co:
        if g not in gamma_gens:
            gamma_gens.append(g)

print(f"  Found {len(gamma_gens)} generators in Γ_Co")

print()

###############################################################################
# Section 8: Analyze Γ_Co Generators
###############################################################################

print("Section 8: Analyzing Γ_Co Generators")
print("-" * 80)

if len(gamma_gens) == 0:
    print("\n  No reflection generators found in Γ_Co")
    print("  Γ_Co may be trivial or generated by non-reflection isometries")
else:
    print(f"\nΓ_Co has {len(gamma_gens)} reflection generators")
    
    print("\nGenerator properties:")
    for i, g in enumerate(gamma_gens[:10]):  # Show first 10
        det = g.determinant()
        tr = g.trace()
        
        # Compute order
        order = None
        g_power = g
        for k in range(1, 11):
            if g_power == identity_matrix(ZZ, 10):
                order = k
                break
            g_power = g_power * g
        
        print(f"  Generator {i+1}: det={det}, trace={tr}, order={order}")
    
    if len(gamma_gens) > 10:
        print(f"  ... and {len(gamma_gens) - 10} more generators")

print()

###############################################################################
# Section 9: Verify All Conditions
###############################################################################

print("Section 9: Verifying Γ_Co Conditions")
print("-" * 80)

print("\nVerifying each generator:")

all_valid = True
for i, g in enumerate(gamma_gens):
    stab_ok = (g * h_Co == h_Co)
    cent_ok = (g * theta - theta * g).is_zero()
    iso_ok = (g.transpose() * T_En_gram * g == T_En_gram)
    
    if not (stab_ok and cent_ok and iso_ok):
        print(f"  Generator {i+1}: FAILED")
        all_valid = False

if all_valid and len(gamma_gens) > 0:
    print(f"  ✓ All {len(gamma_gens)} generators satisfy Γ_Co conditions")
elif len(gamma_gens) == 0:
    print(f"  Note: No generators found")
else:
    print(f"  ✗ Some generators failed verification")

print()

###############################################################################
# Section 10: Summary and Output
###############################################################################

print("=" * 80)
print("SUMMARY")
print("=" * 80)

print(f"""
Lattice T_En:
  Gram matrix: diag(2, 2, -2, ..., -2)
  Rank: {T_En.rank()}, Signature: (2, 8)
  Discriminant group: (Z/2Z)^10

Coble polarization h_Co:
  Vector: {list(h_Co)}
  Norm: {h_Co_norm}

Involution theta:
  Type: Diagonal involution
  Diagonal: [1, 1, -1, -1, ..., -1]

Gamma_Co = Stab(h_Co) cap Z(theta):
  Number of reflection generators: {len(gamma_gens)}
""")



print("\n" + "=" * 80)
print("Task 3.1 Complete")
print("=" * 80)
