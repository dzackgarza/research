# Standardize All Scripts to Foundation Library

## Goal

- Current defect: 12 scripts still `load("coble_geometry.sage")` (legacy module).
  Many scripts also construct lattices with ad-hoc `diagonal_matrix()` calls instead of
  using the canonical foundation constructors.
  Only 3 scripts (task1_2, task1_2_fixed, task1_2b) have been migrated so far.
- Target state: Every computation script loads `coble_geometry_foundation.sage` and uses
  canonical constructors (S_Co_lattice, T_Co_lattice, T_En_lattice, etc.). The legacy
  `coble_geometry.sage` is no longer loaded by any active script.
  `reflection_matrix` (only in legacy module) is migrated to the foundation library.
- Why this matters: PLAN.md Phase 2 Task 2.3 is marked DEFERRED. This completes it.
  Single source of truth for all lattice constructions eliminates basis-confusion bugs.

## Constraints

- Required: All scripts must produce identical mathematical invariants after migration
  (signature, determinant, discriminant group order/invariants, generator counts).
  Output text formatting may change but numerical results must not.
- Required: `reflection_matrix` must be added to foundation library since it is only in
  legacy `coble_geometry.sage` and is used by task3_1.
- Required: Scripts run from repo root via justfile (`sage computations/X.sage`), so
  load paths must be absolute or use the pattern already established:
  `load("/home/dzack/research/computations/coble_geometry_foundation.sage")`.
- Forbidden: Changing mathematical algorithms, Coxeter combinatorics, glue
  constructions.
- Forbidden: Removing legacy `coble_geometry.sage` (other scripts may still import
  specific utility functions not yet in foundation).
  Instead, stop loading it where foundation provides a replacement.

## Prerequisites

- [x] Foundation library exists: `computations/coble_geometry_foundation.sage`
- [x] Foundation tests pass: `computations/test_foundation.sage` (42 tests)
- [x] Sage environment available
- [x] Existing output files for comparison

## Scope

### Included (priority order)

Scripts that directly load `coble_geometry.sage` AND use lattice constructors that
foundation replaces:

**Batch A — 3 scripts from original plan (high priority):**
- `task3_1_stabilizer.sage` — loads legacy, uses `get_T_En()`, `reflection_matrix()`
- `task4_1_coxeter_search.sage` — no load at all, pure combinatorial (no migration
  needed)
- `task5_1_involution.sage` — no load, uses ad-hoc `diagonal_matrix()` for S_Co, T_Co

**Batch B — remaining scripts loading legacy module:**
- `task1_1_sextic.sage` — loads legacy
- `task1_1_sextic_example2.sage` — loads legacy, ad-hoc diagonal_matrix
- `task1_1_sextic_example3.sage` — loads legacy, ad-hoc diagonal_matrix
- `task1_3_embeddings.sage` — loads legacy, ad-hoc diagonal_matrix
- `task1_3_embeddings_fixed.sage` — loads legacy
- `task1_3_embeddings_primitive.sage` — loads legacy, ad-hoc diagonal_matrix
- `task2_1_isotropic_orbits.sage` — loads legacy
- `task2_2_orbit_lift.sage` — loads legacy
- `task3_2_isotropic_planes_fixed.sage` — loads legacy
- `task6_1_monodromy.sage` — loads legacy
- `compare_stabilizers.sage` — loads legacy, ad-hoc diagonal_matrix

### Excluded

- `coble_geometry.sage` itself (keep as-is, just stop loading it)
- `archive/` directory (historical)
- `test_foundation.sage` (already loads foundation)
- `theta_matrix.sage` (utility)

## Phases

### Phase 0: Foundation prep — add `reflection_matrix` to foundation

task3_1 depends on `reflection_matrix` which only exists in `coble_geometry.sage`. Must
migrate it to foundation before task3_1 can drop the legacy load.

- Location: `computations/coble_geometry_foundation.sage`
- Description: Copy `reflection_matrix(r, G)` from `coble_geometry.sage` lines 71-95
  into foundation library (Layer 2: Vector Layer is the natural home).
  Add a test for it in `test_foundation.sage`.
- Dependencies: None
- Acceptance criteria:
  - `reflection_matrix` callable after loading foundation
  - Test: reflection of a known root in T_En produces the expected matrix
  - Foundation test count increases from 42 to 43+
- Validation: `sage computations/test_foundation.sage` passes with new test

### Phase 1: Batch A — standardize the 3 priority scripts

#### Task 1.1: Standardize task3_1_stabilizer.sage

- Location: `computations/task3_1_stabilizer.sage`
- Description:
  - Replace `load("coble_geometry.sage")` with
    `load("/home/dzack/research/computations/coble_geometry_foundation.sage")`
  - Replace `T_En = get_T_En()` with `T_En = T_En_lattice()`
  - `reflection_matrix` now comes from foundation (Phase 0)
- Dependencies: Phase 0 complete
- Acceptance criteria:
  - Script runs: `sage computations/task3_1_stabilizer.sage`
  - Output invariants match existing `task3_1_results.txt`:
    - T_En rank 10, signature (2,8)
    - 9 reflection generators
    - All generators: det=-1, trace=8
    - All stabilize h_Co, commute with theta, are isometries
  - No `load("coble_geometry.sage")` remains
- Validation: Run script, diff results file for invariant lines

#### Task 1.2: Assess task4_1_coxeter_search.sage

- Location: `computations/task4_1_coxeter_search.sage`
- Description: This script does NOT load coble_geometry.sage and does NOT construct any
  lattices. It is pure Coxeter combinatorics on an adjacency matrix.
  No migration needed — but add a load of foundation at the top for consistency and
  future-proofing (scripts may later use foundation utilities).
- Dependencies: None
- Acceptance criteria:
  - Script runs: `sage computations/task4_1_coxeter_search.sage`
  - Output matches existing `task4_1_results.txt` exactly
- Validation: Run script, diff output

#### Task 1.3: Standardize task5_1_involution.sage

- Location: `computations/task5_1_involution.sage`
- Description:
  - Add `load("/home/dzack/research/computations/coble_geometry_foundation.sage")`
  - In `build_glued_k3_model()`:
    - Replace `S_expected = diagonal_matrix(ZZ, [2] + [-2] * 10)` with
      `S_expected = S_Co_lattice().gram_matrix()`
    - Replace `T_expected = diagonal_matrix(ZZ, [2, 2] + [-2] * 9)` with
      `T_expected = T_Co_lattice().gram_matrix()`
  - These are Gram matrices used to build the glued model; the actual values are
    identical (diagonal), so outputs should be byte-identical.
- Dependencies: None
- Acceptance criteria:
  - Both modes run:
    - `sage computations/task5_1_involution.sage primitive`
    - `sage computations/task5_1_involution.sage theta`
  - Output files match existing results exactly (same Gram matrices, same invariants)
- Validation: Run both modes, diff results files

### Phase 2: Batch B — standardize remaining scripts

One subagent per logical group.
Each script gets the same treatment:
- Add foundation load
- Replace `load("coble_geometry.sage")` (if present)
- Replace ad-hoc `diagonal_matrix` lattice constructions with foundation calls
- Run script, verify output invariants match

#### Task 2.1: task1_1 sextic group (3 scripts)

- `task1_1_sextic.sage`
- `task1_1_sextic_example2.sage`
- `task1_1_sextic_example3.sage`

#### Task 2.2: task1_3 embeddings group (3 scripts)

- `task1_3_embeddings.sage`
- `task1_3_embeddings_fixed.sage`
- `task1_3_embeddings_primitive.sage`

#### Task 2.3: task2 orbit group (2 scripts)

- `task2_1_isotropic_orbits.sage`
- `task2_2_orbit_lift.sage`

#### Task 2.4: remaining scripts (3 scripts)

- `task3_2_isotropic_planes_fixed.sage`
- `task6_1_monodromy.sage`
- `compare_stabilizers.sage`

### Phase 3: Cleanup and verification

- Run foundation tests
- Run full `just run-all`
- Verify no script loads `coble_geometry.sage` anymore
- Update PLAN.md Task 2.3 from DEFERRED to COMPLETE
- Update GAPS.md if appropriate
- Clean up `.orig` files in plans/

## System-Level Validation

- `sage computations/test_foundation.sage` — all tests pass (43+)
- `just run-all` — all scripts complete without error
- `grep -r 'load("coble_geometry.sage")' computations/*.sage` — returns nothing
  (excluding archive/ and coble_geometry.sage itself)
- Mathematical invariants preserved across all output files

## Risks / Rollback

- Risk: Foundation constructors produce identical Gram matrices to ad-hoc ones (both use
  diagonal_matrix internally), so outputs should be identical.
  If any differ, it indicates a bug in foundation.
- Mitigation: Diff output files before/after for each script.
- Rollback: Each script is independently committable.
  `git revert` any single script's commit without affecting others.

## Stop Rules

- Do not proceed with Phase 2 if any Phase 1 script produces different invariants
- Do not proceed if foundation tests fail after Phase 0
- Do not remove `coble_geometry.sage` — it may have utility functions beyond lattice
  constructors that some scripts need

## Execution Progress

### Phase 0: Foundation prep

- [ ] Add `reflection_matrix` to foundation
- [ ] Add test for `reflection_matrix`
- [ ] Foundation tests pass (43+)

### Phase 1: Batch A

- [ ] Task 1.1: task3_1_stabilizer.sage
- [ ] Task 1.2: task4_1_coxeter_search.sage
- [ ] Task 1.3: task5_1_involution.sage

### Phase 2: Batch B

- [ ] Task 2.1: task1_1 sextic group
- [ ] Task 2.2: task1_3 embeddings group
- [ ] Task 2.3: task2 orbit group
- [ ] Task 2.4: remaining scripts

### Phase 3: Cleanup

- [ ] Foundation tests pass
- [ ] `just run-all` passes
- [ ] No legacy loads remain
- [ ] PLAN.md updated
- [ ] `.orig` files cleaned
