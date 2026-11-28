# Project State Assessment (2026-03-30)

## Computational Work Inventory

### Task 1: Sextic Construction and Lattice Structure

**Task 1.1: Explicit rational sextic construction**
- Scripts: task1_1_sextic.sage, task1_1_sextic_example2.sage,
  task1_1_sextic_example3.sage (3 scripts)
- Proof note: task1_1_sextic.md ✓
- Status: COMPLETE - 3 parametrizations produce irreducible degree-6 curves with 10
  ordinary nodes
- Literature connection: Independent from Thas (1994), see
  audit/thas_vs_task1_1_comparison.md
- Gap: Not connected to other literature sources (Coble 1917, Coolidge)

**Task 1.2: Gram matrices and Nikulin invariants**
- Scripts: task1_2_gram_matrices.sage, task1_2_gram_matrices_fixed.sage,
  task1_2b_discriminant_forms.sage (3 scripts)
- Proof note: task1_2_gram_matrices.md ✓
- Status: COMPLETE - Bug fixed (T_Co Gram diagonal now correct)
- Literature connection: Dolgachev-Kondō 2013 (S_Co/T_Co structure)
- Gap: None

**Task 1.3: Primitive embedding matrices**
- Scripts: task1_3_embeddings.sage, task1_3_embeddings_fixed.sage,
  task1_3_embeddings_primitive.sage (3 scripts)
- Proof note: task1_3_embeddings.md ✓
- Status: COMPLETE - Verified NOT A BUG (discriminant form correct)
- Literature connection: Nikulin 1979 (primitive embedding theorem)
- Gap: None

### Task 2: Isotropic Orbit Classification

**Task 2.1: Isotropic vector orbits in discriminant group**
- Scripts: task2_1_isotropic_orbits.sage (1 script)
- Proof note: task2_1_isotropic_orbits.md ✓
- Status: COMPLETE - 2 orbits (zero vector + 527 nonzero isotropic)
- Literature connection: Nikulin Prop 1.5.2 (surjectivity), Sterk 1991 (cusp
  classification)
- Gap: None

**Task 2.2: Orbit lifting to primitive vectors**
- Scripts: task2_2_orbit_lift.sage (1 script)
- Proof note: task2_2_orbit_lift.md ✓
- Status: COMPLETE - All primitive isotropic have div=2, single O*(T)-orbit
- Literature connection: Nikulin Prop 1.5.2
- Gap: None

### Task 3: Stabilizer and Isotropic Planes

**Task 3.1: Stabilizer group generators**
- Scripts: task3_1_stabilizer.sage, task3_1_generators.sage (2 scripts)
- Proof note: task3_1_stabilizer.md ✓
- Status: COMPLETE - 9 generators preserve T_En Gram, fix h_Co, commute with θ
- Literature connection: Arithmetic groups for lattices
- Gap: None

**Task 3.2: Primitive isotropic planes**
- Scripts: task3_2_isotropic_planes.sage (1 script)
- Proof note: task3_2_isotropic_planes.md ✗ INVALID
- Status: INVALID - Used "Arf invariant" which doesn't exist over Z
- Literature connection: Nikulin 1979 (theoretical prediction), AEGS 2023
- Gap: CRITICAL - Needs complete redo with GAP orbit computation

### Task 4: Coxeter Diagram Analysis

**Task 4.1: Maximal parabolic subdiagrams**
- Scripts: task4_1_coxeter_search.sage (1 script)
- Proof note: task4_1_coxeter_search.md ✓
- Status: COMPLETE - Unique maximal B̃₇(2) on nodes (0,1,2,3,4,5,6,7)
- Literature connection: AEGS 2023 Section 3 (0-cusp description)
- Gap: None

### Task 5: Involution Construction

**Task 5.1: Sign involution on K3 lattice**
- Scripts: task5_1_involution.sage (1 script)
- Proof note: task5_1_involution.md ✓
- Status: COMPLETE - Glued lattice model with primitive decomposition Λ = S_Co ⊕ T
- Literature connection: Nikulin 1979 (primitive embeddings), Dolgachev-Kondō 2013
- Gap: None (old route resolved)

### Task 6: Stability Verification

**Task 6.1: slc stability conditions**
- Scripts: task6_1_monodromy.sage (1 script)
- Proof note: task6_1_slc_stability.md ✓
- Status: COMPLETE - Surgery vector ℓ = 0, all 5 slc conditions satisfied
- Literature connection: Moduli theory
- Gap: None

### Utilities

**Shared computation infrastructure**
- Scripts: coble_geometry.sage, compare_stabilizers.sage (2 scripts)
- Proof note: utilities_note.md ✓
- Status: COMPLETE - Canonical lattice definitions and verification utilities
- Gap: PROCESS - Lattice constructions should use direct sums, not diagonal matrices

## Summary Statistics

- Total computation scripts: 20
- Total proof notes: 11 (10 task-specific + 1 utilities)
- Complete and verified: 9 tasks (1.1, 1.2, 1.3, 2.1, 2.2, 3.1, 4.1, 5.1, 6.1)
- Invalid: 1 task (3.2)
- Verification rate: 90% (9/10 tasks)

## GOAL.md Priority Assessment

### Priority 1: Centralize canonical literature — 80% COMPLETE

**Complete**:
- REFERENCES.md established with 13 canonical sources
- 3 sources acquired locally (Dolgachev-Kondō 2013, AEGS 2023, Thas 1994)
- Canonical claim notes created (literature_claim_map.md, moduli_dimension_claim.md,
  etc.)

**Gaps**:
- Task 1.1 sextics not connected to Coble 1917 or Coolidge literature
- J. Thas primary source for uniqueness claim unresolved
- Coolidge stronger theorem wording needs primary-text extraction
- 10/13 sources remain unavailable (institutional access, purchase, not found)

**Next actions**:
- Connect task1_1 sextics to Coble/Coolidge if possible
- Document remaining literature gaps as blocked on external access

### Priority 2: Numerical evidence aligned with literature — 90% COMPLETE

**Complete**:
- 9/10 tasks have verified proof notes
- All computational claims linked to literature via proof notes
- Exact numerical evidence preserved

**Gaps**:
- Task 3.2 INVALID (Arf invariant issue)
- Lattice constructions inconsistent (ad-hoc diagonal matrices vs canonical direct sums)

**Next actions**:
- Redo task3_2 with GAP orbit computation
- Standardize lattice constructions in coble_geometry.sage
- Audit all scripts for non-standard constructions

### Priority 3: Open computational blocks — 100% COMPLETE

**Complete**:
- Task 5.1 involution resolved with glued lattice model
- All computational blocks resolved

**Gaps**: None

**Next actions**: None

### Priority 4: Lean formalization — 0% COMPLETE (SECONDARY)

**Status**:
- Lean toolchain available (source ~/.envrc)
- 3 Lean files exist (IsotropicPlanes.lean with 3 sorry, NodeCriteria.lean complete,
  Basic.lean stub)
- Formalization is secondary per GOAL.md

**Gaps**:
- No formalization work planned until literature and computations stable

**Next actions**: None (secondary priority)

## Critical Path to Completion

1. **Fix task3_2** (Priority 2, CRITICAL)
   - Delegate GAP orbit computation to Prover
   - Update computation script
   - Update proof note

2. **Standardize lattice constructions** (Priority 2, PROCESS)
   - Update coble_geometry.sage with direct sum constructors
   - Audit all scripts for non-standard constructions
   - Update scripts to use standardized constructors

3. **Document remaining literature gaps** (Priority 1, DOCUMENTATION)
   - Explicitly mark J. Thas, Coolidge, institutional sources as blocked
   - Document task1_1 as independent construction unless connected to literature

4. **Optional: Lean formalization** (Priority 4, SECONDARY)
   - Only if explicitly requested or after Priorities 1-3 complete

## Estimated Completion

- Priority 1: 80% → 90% (document remaining gaps as blocked)
- Priority 2: 90% → 100% (fix task3_2, standardize constructions)
- Priority 3: 100% (complete)
- Priority 4: 0% (secondary, not planned)

**Overall project completion**: 90% → 95% after critical path tasks
