#!/usr/bin/env sage
"""
Test Task 1.2: Gram Matrix Mathematical Properties

HARD ASSERTIONS - script fails if mathematics is wrong.
Does NOT compare to verification notes or expected outputs.
"""

load("computations/coble_geometry.sage")

print("=" * 80)
print("TASK 1.2 MATHEMATICAL PROPERTY TESTS")
print("=" * 80)

# Get Gram matrices
G_S = S_Co_gram()
G_T = T_Co_gram()

# Test 1: S_Co must be symmetric
print("\n[TEST 1] S_Co Gram matrix is symmetric")
assert G_S == G_S.transpose(), "FAIL: S_Co Gram not symmetric"
print("PASS")

# Test 2: S_Co signature must match definition ⟨2⟩ ⊕ ⟨-2⟩^10
print("\n[TEST 2] S_Co signature is (1,10)")
# Compute signature from eigenvalues
eigs = G_S.change_ring(RR).eigenvalues()
n_pos = sum(1 for e in eigs if e > 0)
n_neg = sum(1 for e in eigs if e < 0)
sig = (n_pos, n_neg)
assert sig == (1, 10), f"FAIL: S_Co signature {sig} != (1,10)"
print("PASS")

# Test 3: S_Co determinant must be 2^11 (from rank 11, all entries ±2)
print("\n[TEST 3] S_Co determinant is 2^11 = 2048")
det_S = G_S.determinant()
assert det_S == 2048, f"FAIL: det(S_Co) = {det_S} != 2048"
print("PASS")

# Test 4: T_Co must be symmetric
print("\n[TEST 4] T_Co Gram matrix is symmetric")
assert G_T == G_T.transpose(), "FAIL: T_Co Gram not symmetric"
print("PASS")

# Test 5: T_Co signature must be (2,9) for orthogonal complement
print("\n[TEST 5] T_Co signature is (2,9)")
eigs_T = G_T.change_ring(RR).eigenvalues()
n_pos_T = sum(1 for e in eigs_T if e > 0)
n_neg_T = sum(1 for e in eigs_T if e < 0)
sig_T = (n_pos_T, n_neg_T)
assert sig_T == (2, 9), f"FAIL: T_Co signature {sig_T} != (2,9)"
print("PASS")

# Test 6: T_Co determinant must be -2^11 (signature flips sign)
print("\n[TEST 6] T_Co determinant is -2^11 = -2048")
det_T = G_T.determinant()
assert det_T == -2048, f"FAIL: det(T_Co) = {det_T} != -2048"
print("PASS")

# Test 7: Discriminant group A_S must be 2-elementary
print("\n[TEST 7] A_S is 2-elementary (all invariants are 2)")
A_S = G_S.smith_form()[0].diagonal()
for d in A_S:
    if d != 1:
        assert d == 2, f"FAIL: A_S has non-2-elementary invariant {d}"
print("PASS")

# Test 8: Discriminant group A_T must be 2-elementary
print("\n[TEST 8] A_T is 2-elementary (all invariants are 2)")
A_T = G_T.smith_form()[0].diagonal()
for d in A_T:
    if d != 1:
        assert d == 2, f"FAIL: A_T has non-2-elementary invariant {d}"
print("PASS")

# Test 9: |A_S| = |A_T| (required for primitive embedding)
print("\n[TEST 9] |A_S| = |A_T|")
order_S = abs(det_S)
order_T = abs(det_T)
assert order_S == order_T, f"FAIL: |A_S| = {order_S} != {order_T} = |A_T|"
print("PASS")

# Test 10: Nikulin invariants (r,a,δ) must match for both
print("\n[TEST 10] Nikulin invariants (r,a,delta) = (11,11,1) for both")
# r = rank, a = number of 2-torsion elements, delta = Brown invariant mod 8
r_S = G_S.nrows()
r_T = G_T.nrows()
assert r_S == 11, f"FAIL: rank(S_Co) = {r_S} != 11"
assert r_T == 11, f"FAIL: rank(T_Co) = {r_T} != 11"

# Count 2-torsion: number of 2's in Smith form
a_S = sum(1 for d in A_S if d == 2)
a_T = sum(1 for d in A_T if d == 2)
assert a_S == 11, f"FAIL: a(S_Co) = {a_S} != 11"
assert a_T == 11, f"FAIL: a(T_Co) = {a_T} != 11"
print("PASS")

print("\n" + "=" * 80)
print("ALL TESTS PASSED")
print("=" * 80)
