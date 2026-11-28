# T-0004: PRE_AUDIT Report

## Pre-Audit Checklist

### 1. Is the task mathematically well-defined?

**PASS.** The task is to compute orbits of isotropic vectors in A_T ≅ (Z/2Z)^11 under
O(q_T). The quadratic form q_T(x) = (1/2)·wt(x) mod 2Z is explicitly defined.
Isotropic means q_T(x) = 0 mod 2Z, equivalent to even Hamming weight.
This is a standard finite group orbit computation.

### 2. Are all objects, conventions, and ambient assumptions fixed?

**PASS.** T_Co = diag(2, 2, -2^9) is fixed.
A_T ≅ F_2^11 is fixed.
q_T is explicitly given.
O(q_T) is the standard orthogonal group of this quadratic form over F_2.

### 3. Is the task specifically tied to GOAL.md or an explicit prerequisite?

**PASS.** Directly implements GOAL.md §2, Task 2.1.

### 4. Are acceptance criteria objective and unambiguous?

**PASS.** Seven explicit criteria: O(q_T) construction, enumeration of 2048 elements,
isotropic identification, GAP Orbits computation, orbit data recording, sum
verification, cross-check of isotropic count = 1024.

### 5. Does the task hide a major undeclared algorithmic problem?

**PASS.** GAP has built-in orthogonal group construction and orbit computation.
No algorithm needs to be implemented from scratch.

### 6. Are the necessary algorithms already available and audited?

**PASS.** GAP `Orbits`, `Stabilizer`, and orthogonal group construction are standard,
well-tested GAP functions.
theory/gap_orbits.md provides usage patterns.

### 7. Are all dependencies local and available?

**PASS.** GAP is available via sage env.
coble_geometry_foundation.sage is restored.
theory/gap_orbits.md exists.

### 8. Is the task file scope bounded and isolation feasible?

**PASS.** scope.yml restricts modifications to tasks/T-0004/implementation/*. Worktree
isolation specified.

### 9. Is there a plausible exact verification path?

**PASS.** GAP computation is exact (finite field arithmetic).
Verification: sum of orbit sizes = 1024, each orbit element is isotropic, group order
matches |O^±(11, 2)|.

## Hidden Prerequisite Check

**None identified.** The task is self-contained: finite group orbit computation over
F_2.

## Risk Assessment

**Low risk.** This is a straightforward finite computation.
The only potential issue is GAP's ability to construct O(q_T) efficiently for n=11, but
|O^±(11, 2)| ≈ 2^55 is manageable for orbit computation on a set of size 1024.

## Audit Plan for Implementation

- Verify O(q_T) construction: check group order against known formula
- Verify isotropic count: must be exactly 1024
- Verify orbit partition: sum of orbit sizes = 1024, no overlaps
- Verify each orbit representative is isotropic
- Check that GAP `Orbits` was used (not hand-rolled code)

## Verdict

**PRE_AUDIT PASS.** Task is well-defined, scoped correctly, and executable using trusted
local resources. Proceed to IMPLEMENT.
