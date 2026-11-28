# SELF_CHECK for T-0004 v2: Orbit Enumeration in A_T

## Checklist

### 1. Deliverable matches contract

**PASS** — Script computes O(q_T)-orbits of isotropic vectors in A_T ≅ (Z/2Z)^11 with
q_T(x) = (1/2)(x_1 + x_2 - x_3 - ... - x_11) mod 2Z. Signs are preserved via
`signs = [1, 1] + [-1] * (n - 2)`.

### 2. Scope compliance

**FAIL** — Two issues:
- **File scope**: PASS — Only
  `tasks/T-0004/implementation/task2_1_orbit_enumeration.sage` was modified (1 file
  changed, 137 insertions).
- **Prohibited: hand-rolled orbit code**: FAIL — The script uses a custom BFS orbit
  computation (lines 74-94) instead of GAP `Orbits` or Sage's orbit/group action
  facilities as required by `scope.yml` prohibited list and task.md acceptance criterion
  #4.

### 3. All claimed results present

**PASS** — Script outputs:
- Orbit representatives (as F_2^11 vectors)
- Orbit sizes (2 orbits: size 1 and size 527)
- Stabilizer sizes (computed from group order formula)
- Verification that sum of orbit sizes = 528

### 4. Exact reproducibility

**PASS** — Script ran successfully with `/home/dzack/miniforge3/envs/sage/bin/sage` and
exited cleanly with all assertions passing.

### 5. No unresolved placeholders

**PASS** — No TODO, FIXME, XXX, HACK, mock, or placeholder patterns found in the script.

### 6. Correct q_T formula

**PASS** — The script uses `qT_val(x)` which computes
`sum(signs[i] * x[i] for i in range(n)) % 4` with
`signs = [1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1]`. This correctly implements q_T(x) =
(1/2)(x_1 + x_2 - x_3 - ... - x_11) mod 2Z. Transvections verified to preserve q_T with
correct signs.

### 7. Assertions pass

**PASS** — All assertions passed:
- Isotropic count = 528 ✓
- Sum of orbit sizes = 528 ✓
- All orbit representatives verified isotropic ✓
- Transvections preserve q_T ✓
- Orbit sizes divide group order ✓

## Additional Observations

- The script computes the group order |O(q_T)| using the formula for |O(2m+1, F_2)|
  rather than constructing the group explicitly and computing its order.
  This is mathematically correct but not an explicit construction as required by
  acceptance criterion #1.
- The orbit computation uses transvections as generators with BFS, which is
  mathematically equivalent to computing orbits under the group they generate, but does
  not use GAP `Orbits` as specified.
- Results: 2 orbits found — trivial orbit {0} (size 1) and one non-trivial orbit (size
  527).

## Verdict: NEEDS REMEDIATION

### Failures:

1. **Hand-rolled orbit code** — The BFS orbit computation (lines 74-94) violates the
   `scope.yml` prohibition on "Hand-rolled orbit code (must use Sage's orbit/group
   action facilities or GAP Orbits)" and task.md acceptance criterion #4 which requires
   "Orbits of isotropic elements under O(q_T) are computed using GAP `Orbits`".
