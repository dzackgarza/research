# Computation Correctness Verification Report

**Date**: 2026-03-30\
**Scope**: Verification of mathematical correctness for all task groups (1.1-6.1)\
**Method**: Systematic comparison of verification note claims against actual computation
outputs

## Objective

Verify that computation outputs match the specific numerical claims made in verification
notes, ensuring no overclaims, numerical mismatches, or hidden failures.

## Methodology

For each task group:
1. Extract specific numerical/structural claims from `proofs/solved/taskX_Y*.md`
2. Read actual computation output from `computations/taskX_Y*results.txt`
3. Compare claims against output for exact matches
4. Check PASS/FAIL markers for accuracy
5. Identify any discrepancies, overclaims, or buried failures

## Verification Results

| Task | Claim from Verification Note | Actual Computation Output | Status |
| --- | --- | --- | --- |
| **1.1** | Exactly 10 singular points, all A₁ nodes | "Total found: 10, Nodes (A1): 10" | ✓ MATCH |
| **1.2** | S_Co Gram: diag(2, -2, ..., -2), T_Co signature (2,9), Nikulin (11,11,1) | Gram diagonal confirmed, signature (2,9), (r,a,δ) = (11,11,1) | ✓ MATCH |
| **1.3** | T_Co = S_Co^⊥ primitive embedding | "S_Co ⊥ T_Co: True", "T_Co → Λ_K3 primitive: True" | ✓ MATCH |
| **2.1** | Exactly 2 orbits: zero (size 1) + 527 nonzero isotropic | "Number of orbits: 2", "Orbit 0... Size: 1", "Orbit 1... Size: 527" | ✓ MATCH |
| **2.2** | All primitive isotropic have div(v)=2, exactly one O*(T)-orbit | "All primitive... div(v) = 2", "O*(T)-orbits of div=2 vectors: 1" | ✓ MATCH |
| **3.1** | Explicit generators fixing h_Co and commuting with θ | "All generators stabilize h_Co: True", "All generators commute with θ: True" | ✓ MATCH |
| **3.2** | Unique O(T_Co)-orbit of primitive isotropic planes, J⊥/J ≅ A₁^⊕7 | "All 15 primitive... SINGLE O(T_Co)-orbit", "J⊥/J isometric to A₁^⊕7", Gram = diag(-2,...,-2) | ✓ MATCH |
| **4.1** | Unique maximal B̃₇(2) subdiagram | "B̃₇(2): 1", "Maximal B̃₇(2): 1" | ✓ MATCH |
| **5.1** | θ² = I passes, θᵀGθ = G passes, eigenspace decomposition correct | "theta^2 = I: True", "theta^T G theta = G: True", eigenspace checks True | ✓ MATCH |
| **6.1** | Surgery vector ℓ = 0, all 5 slc conditions satisfied | "ℓ = (0, 0, 0, 0, 0, 0, 0, 0, 0)", all 5 conditions "SATISFIED" | ✓ MATCH |

## Detailed Findings

### Task 2.1: Isotropic Vector Orbits

- **Claim**: "exactly 2 orbits under O(q_T): zero vector (size 1) and all 527 nonzero
  isotropic vectors"
- **Output**: `task2_1_results.txt` lines 20-27 confirm exactly 2 orbits with sizes 1
  and 527
- **Verification**: EXACT MATCH

### Task 3.2: Isotropic Plane Uniqueness

- **Claim**: "unique primitive isotropic plane orbit"
- **Output**: `task3_2_results_full.txt` lines 246-248: "✓ VERIFIED: All 15 primitive
  isotropic planes are in a SINGLE O(T_Co)-orbit"
- **Verification**: EXACT MATCH (computation explicitly verified orbit uniqueness via
  Arf invariant)

### Task 4.1: Maximal B̃₇(2) Subdiagram

- **Claim**: "unique maximal B̃₇(2) subdiagram"
- **Output**: `task4_1_results.txt` lines 16-17: "B̃₇(2): 1" maximal instances
- **Verification**: EXACT MATCH

### Task 5.1: Involution Properties

- **Claim**: "θ² = I passes" and "θᵀGθ = G passes"
- **Output**: `task5_1_theta_results.txt` lines 16-17: "theta^2 = I: True", "theta^T G
  theta = G: True"
- **Verification**: EXACT MATCH with explicit PASS markers

### Task 2.2: Divisibility and Orbit Lifting

- **Claim**: "527 nonzero isotropic vectors" lift to "exactly one orbit under O*(T_Co)"
- **Output**: `task2_2_results.txt` lines 46-49 confirm single O*(T)-orbit of div=2
  vectors
- **Verification**: EXACT MATCH

## Critical Checks

### No Overclaims Detected

- All numerical claims (527 vectors, 15 planes, 1 orbit, 10 nodes) match output exactly
- No instances of verification notes claiming success when output shows failure
- No buried failures in summaries

### PASS/FAIL Markers Accurate

- Task 5.1: "PASS: exact theta verification succeeded" matches all checks returning True
- Task 3.2: "✓ VERIFIED" markers correspond to actual computational verification, not
  just theoretical prediction
- Task 6.1: All 5 slc conditions marked "SATISFIED" with explicit verification steps

### Numerical Precision

- Task 2.1: 527 nonzero isotropic vectors (not "approximately 527" or "about 500")
- Task 3.2: 15 primitive planes identified (not "several" or "multiple")
- Task 4.1: Exactly 1 maximal B̃₇(2) (not "at least one")

## Conclusion

**Status**: ✓ ALL VERIFICATIONS PASS

All 10 task groups show perfect alignment between verification note claims and actual
computation outputs.
No mathematical overclaims, numerical mismatches, or hidden failures detected.

**Confidence Level**: HIGH

The verification notes accurately document what the computations establish.
Specific numerical values, orbit counts, and structural properties match exactly between
claims and outputs.

## Files Verified

### Verification Notes

- `proofs/solved/task1_1_sextic.md`
- `proofs/solved/task1_2_gram_matrices.md`
- `proofs/solved/task1_3_embeddings.md`
- `proofs/solved/task2_1_isotropic_orbits.md`
- `proofs/solved/task2_2_orbit_lift.md`
- `proofs/solved/task3_1_stabilizer.md`
- `proofs/solved/task3_2_isotropic_planes.md`
- `proofs/solved/task4_1_coxeter_search.md`
- `proofs/solved/task5_1_involution.md`
- `proofs/solved/task6_1_slc_stability.md`

### Computation Outputs

- `computations/task1_1_example2_results.txt`
- `computations/task1_2_results.txt`
- `computations/task1_3_results.txt`
- `computations/task2_1_results.txt`
- `computations/task2_2_results.txt`
- `computations/task3_1_results.txt`
- `computations/task3_2_results.txt` and `task3_2_results_full.txt`
- `computations/task4_1_results.txt`
- `computations/task5_1_theta_results.txt`
- `computations/task6_1_results.txt`

* * *

**Verified by**: Automated systematic comparison\
**Date**: 2026-03-30\
**Session**: ses_2c0d4cabdffeQSec97r9jmPxIy
