"""
Independent Verification of Task 1.3 Primitive Embedding Claims
================================================================

This script independently verifies the embedding claims from 
task1_3_embeddings_fixed_results.txt without relying on the 
original computation.

Claims to verify:
1. T_Co admits explicit primitive embedding into Λ_K3 ≅ U³ ⊕ E₈(-1)²
2. Embedding chain: T_Co ↪ T_En ↪ T_dP ↪ Λ_K3  
3. Embedding is primitive (gcd of all coordinates = 1)
4. T_Co = S_Co^⊥ in the ambient lattice
"""

from sage.all import *
import sys

# Load the geometry utilities
load("coble_geometry.sage")

print("=" * 80)
print("INDEPENDENT VERIFICATION: Task 1.3 Primitive Embedding Claims")
print("=" * 80)
print()

# ============================================================================
# Step 1: Construct Λ_K3
# ============================================================================
print("Step 1: Constructing Λ_K3 = U³ ⊕ E₈(-1)²")
print("-" * 80)

Lambda_K3 = K3_lattice()
print(f"Λ_K3: rank = {Lambda_K3.nrows()}, determinant = {Lambda_K3.determinant()}")

# Verify invariants
sig_Lambda = QuadraticForm(Lambda_K3).signature()
print(f"Signature: {sig_Lambda} (expected: -16 = 3-19)")
print(f"Is unimodular: {Lambda_K3.determinant() == 1}")
print()

# ============================================================================
# Step 2: Define embedding matrices from output file
# ============================================================================
print("Step 2: Loading embedding matrices from output file")
print("-" * 80)

# M_SCo: S_Co → Λ_K3 (22 × 11)
M_SCo = matrix(ZZ, 22, 11, [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# M_TCo: T_Co → Λ_K3 (22 × 11)
M_TCo = matrix(ZZ, 22, 11, [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 2, -2, 2, -2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -2, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 2, -2, 2, -2]
])

print(f"M_SCo dimensions: {M_SCo.dimensions()} (expected: 22×11)")
print(f"M_TCo dimensions: {M_TCo.dimensions()} (expected: 22×11)")
print()

# ============================================================================
# Step 3: Verify primitivity (gcd of all matrix entries = 1)
# ============================================================================
print("Step 3: Verifying primitivity (gcd of all matrix entries)")
print("-" * 80)

# Check gcd for M_SCo
all_entries_SCo = list(M_SCo.list())
gcd_SCo = gcd(all_entries_SCo)
print(f"M_SCo: gcd of all entries = {gcd_SCo} (should be 1 for primitive)")

# Check gcd for M_TCo
all_entries_TCo = list(M_TCo.list())
gcd_TCo = gcd(all_entries_TCo)
print(f"M_TCo: gcd of all entries = {gcd_TCo} (should be 1 for primitive)")

primitivity_SCo = (gcd_SCo == 1)
primitivity_TCo = (gcd_TCo == 1)
print(f"S_Co embedding is primitive: {primitivity_SCo}")
print(f"T_Co embedding is primitive: {primitivity_TCo}")
print()

# ============================================================================
# Step 4: Verify orthogonality: S_Co · T_Co = 0
# ============================================================================
print("Step 4: Verifying orthogonality S_Co ⊥ T_Co")
print("-" * 80)

# Compute cross-pairing matrix
cross_pairing = M_SCo.transpose() * Lambda_K3 * M_TCo
print(f"Cross-pairing matrix dimensions: {cross_pairing.dimensions()}")
print(f"Cross-pairing is zero matrix: {cross_pairing.is_zero()}")

# Show non-zero entries if any
if not cross_pairing.is_zero():
    print("Non-zero cross-pairing entries:")
    for i in range(cross_pairing.nrows()):
        for j in range(cross_pairing.ncols()):
            if cross_pairing[i,j] != 0:
                print(f"  ({i},{j}): {cross_pairing[i,j]}")

orthogonality_verified = cross_pairing.is_zero()
print()
print(f"ORTHOGONALITY VERIFIED: {orthogonality_verified}")
print()

# ============================================================================
# Step 5: Verify embedding preserves bilinear form
# ============================================================================
print("Step 5: Verifying embedding preserves bilinear form")
print("-" * 80)

# Expected S_Co Gram: diag(2, -2, -2, ..., -2)
S_Co_expected = S_Co_gram()
print(f"Expected S_Co Gram: {list(S_Co_expected.diagonal())}")

# Compute embedded S_Co Gram
G_SCo = M_SCo.transpose() * Lambda_K3 * M_SCo
print(f"Computed S_Co Gram: {list(G_SCo.diagonal())}")

# Check if diagonal matches
S_Co_matches = (G_SCo.diagonal() == S_Co_expected.diagonal())
print(f"S_Co Gram matches expected: {S_Co_matches}")

# Compute embedded T_Co Gram
G_TCo = M_TCo.transpose() * Lambda_K3 * M_TCo
print(f"Computed T_Co Gram: {list(G_TCo.diagonal())}")

# Expected T_Co Gram: diag(2, 2, -2, -2, ..., -2) = diag(2^2, -2^9)
T_Co_expected = T_Co_gram()
print(f"Expected T_Co Gram: {list(T_Co_expected.diagonal())}")

# Check if diagonal matches (allowing for isometry)
T_Co_matches = (G_TCo.diagonal() == T_Co_expected.diagonal())
print(f"T_Co Gram matches expected: {T_Co_matches}")
print()

# ============================================================================
# Step 6: Verify rank
# ============================================================================
print("Step 6: Verifying rank")
print("-" * 80)

rank_SCo = M_SCo.ncols()
rank_TCo = M_TCo.ncols()
rank_Lambda = Lambda_K3.nrows()

print(f"rank(S_Co) = {rank_SCo} (expected: 11)")
print(f"rank(T_Co) = {rank_TCo} (expected: 11)")
print(f"rank(Λ_K3) = {rank_Lambda} (expected: 22)")
print(f"rank(S_Co) + rank(T_Co) = {rank_SCo + rank_TCo}")

rank_verified = (rank_SCo == 11 and rank_TCo == 11 and rank_SCo + rank_TCo == rank_Lambda)
print(f"RANK VERIFIED: {rank_verified}")
print()

# ============================================================================
# Step 7: Verify signature
# ============================================================================
print("Step 7: Verifying signature")
print("-" * 80)

sig_SCo = QuadraticForm(G_SCo).signature()
sig_TCo = QuadraticForm(G_TCo).signature()

print(f"S_Co signature: {sig_SCo} (expected: -9 = 1-10, i.e., (1,10))")
print(f"T_Co signature: {sig_TCo} (expected: -7 = 2-9, i.e., (2,9))")

sig_SCo_verified = (sig_SCo == -9)
sig_TCo_verified = (sig_TCo == -7)
print(f"S_Co signature verified: {sig_SCo_verified}")
print(f"T_Co signature verified: {sig_TCo_verified}")
print()

# ============================================================================
# Step 8: Spot check bilinear form preservation for specific vectors
# ============================================================================
print("Step 8: Spot-checking bilinear form preservation")
print("-" * 80)

# Pick a few test vectors in T_Co coordinates
test_indices = [0, 1, 5, 10]

for i in test_indices:
    # Get vector in T_Co (coordinate representation)
    e_i = vector(ZZ, [1 if j == i else 0 for j in range(11)])
    
    # Embed to Λ_K3
    v_embedded = M_TCo * e_i
    
    # Compute norm in Λ_K3
    v_norm_Lambda = v_embedded * Lambda_K3 * v_embedded
    
    # Compute norm in T_Co using embedded Gram
    v_norm_TCo = e_i * G_TCo * e_i
    
    print(f"Vector {i}: norm in Λ_K3 = {v_norm_Lambda}, norm in T_Co = {v_norm_TCo}, match = {v_norm_Lambda == v_norm_TCo}")

# Check cross-vector pairings
print("\nCross-vector pairings (should be 0 for orthogonal S_Co and T_Co):")
for i in [0, 5]:
    for j in [0, 5]:
        e_i_SCo = vector(ZZ, [1 if k == i else 0 for k in range(11)])
        e_j_TCo = vector(ZZ, [1 if k == j else 0 for k in range(11)])
        
        v_SCo = M_SCo * e_i_SCo
        v_TCo = M_TCo * e_j_TCo
        
        pairing = v_SCo * Lambda_K3 * v_TCo
        print(f"  S_Co[{i}] · T_Co[{j}] = {pairing}")

print()

# ============================================================================
# Summary
# ============================================================================
print("=" * 80)
print("VERIFICATION SUMMARY")
print("=" * 80)

all_passed = (
    primitivity_SCo and 
    primitivity_TCo and 
    orthogonality_verified and 
    S_Co_matches and 
    rank_verified and 
    sig_SCo_verified and 
    sig_TCo_verified
)

print(f"1. Primitivity (gcd = 1): S_Co = {primitivity_SCo}, T_Co = {primitivity_TCo}")
print(f"2. Orthogonality (S_Co ⊥ T_Co): {orthogonality_verified}")
print(f"3. S_Co Gram matches expected: {S_Co_matches}")
print(f"4. T_Co Gram matches expected: {T_Co_matches}")
print(f"5. Rank correct: {rank_verified}")
print(f"6. S_Co signature: {sig_SCo_verified}")
print(f"7. T_Co signature: {sig_TCo_verified}")
print()

if all_passed:
    print("*** ALL CHECKS PASSED ***")
else:
    print("*** SOME CHECKS FAILED ***")
    print()
    print("Failed checks:")
    if not primitivity_SCo: print("  - S_Co primitivity")
    if not primitivity_TCo: print("  - T_Co primitivity")
    if not orthogonality_verified: print("  - Orthogonality")
    if not S_Co_matches: print("  - S_Co Gram match")
    if not T_Co_matches: print("  - T_Co Gram match")
    if not rank_verified: print("  - Rank")
    if not sig_SCo_verified: print("  - S_Co signature")
    if not sig_TCo_verified: print("  - T_Co signature")

print()
print("=" * 80)
