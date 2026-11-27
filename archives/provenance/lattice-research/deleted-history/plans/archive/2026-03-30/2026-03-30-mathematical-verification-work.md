# Plan: Mathematical Verification Work

**Created**: 2026-03-30 **Status**: Active

## Context

Recent autonomous work spiraled into documentation churn (15 commits of citation
weaving, canonical statement creation) with zero mathematical progress.
The repo has substantial computational results but only 2 solved proof notes (task3_2,
task6_1) despite multiple tasks having output files.

## Mathematical State Assessment

From computational artifacts in `computations/`:

**Tasks with results files but no solved proof notes**:
- Task 1.1-1.3: Sextic construction, Gram matrices, embeddings
- Task 2.1-2.2: Isotropic orbits, orbit lift
- Task 3.1: Generators, stabilizer (task3_2 has solved note)
- Task 4.1: Coxeter search (found 1 maximal B̃₇(2) subdiagram)
- Task 5.1: Involution construction (verified on glued lattice model)

**Tasks with solved proof notes**:
- Task 3.2: Isotropic planes classification (229 lines)
- Task 6.1: slc stability verification

## Priority Targets

### Phase 1: Task 4.1 Coxeter Verification Note

**Why**: Clean computational result (1 unique maximal B̃₇(2) subdiagram), clear
mathematical claim, no literature ambiguity.

**Acceptance criteria**:
- Solved proof note in `proofs/solved/task4_1_coxeter_search.md`
- States the computational claim: unique maximal B̃₇(2) parabolic subdiagram
- Links to literature context (Nikulin, Sterk, AEGS for Coxeter diagram structure)
- Documents verification method (exhaustive search over node subsets)
- Includes exact result: nodes (0,1,2,3,4,5,6,7)

### Phase 2: Task 2.1 Isotropic Orbit Verification Note

**Why**: Foundational for Task 3.2 (already has solved note), clear orbit classification
result.

**Acceptance criteria**:
- Solved proof note in `proofs/solved/task2_1_isotropic_orbits.md`
- States O(T_Co)-orbit classification for primitive isotropic vectors
- Links to Nikulin 2-elementary lattice theory
- Documents computational verification method
- Cross-references to task3_2 (which depends on this result)

### Phase 3: Task 5.1 Involution Verification Note

**Why**: Already has canonical note `audit/task5_1_exact_involution_note.md`, needs
solved proof note.

**Acceptance criteria**:
- Solved proof note in `proofs/solved/task5_1_involution.md`
- States the verified claim: sign involution θ on glued lattice model
- Documents primitive embedding + orthogonal complement route
- Includes integrality and isometry verification results
- Cross-references canonical note for exact construction details

## Non-goals

- No new canonical documentation notes
- No citation weaving into existing notes
- No literature source audits
- No plan proliferation

## Verification

After each phase:
- `git diff` to verify only solved proof note was created/modified
- Check that note separates literature facts from computational verification
- Confirm no documentation churn in audit/, plans/, reports/
