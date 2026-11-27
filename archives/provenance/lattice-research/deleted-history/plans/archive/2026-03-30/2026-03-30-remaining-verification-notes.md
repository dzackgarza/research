# Plan: Remaining Verification Notes

**Created**: 2026-03-30 **Status**: Active

## Context

Repo has 20 computation scripts but only 5 solved proof notes.
Gap analysis shows 5 task groups need verification notes:
- task1_1: sextic construction (3 script variants)
- task1_2: gram matrices (3 script variants)
- task1_3: embeddings (3 script variants)
- task2_2: orbit lift
- task3_1: generators/stabilizer (2 scripts)

## Goal

Create verification notes for remaining computational tasks, following the same
structure as existing solved notes (task2_1, task3_2, task4_1, task5_1, task6_1).

## Phases

### Phase 1: Task 1.1 sextic construction verification note

- [x] Review task1_1_sextic.sage, task1_1_sextic_example2.sage,
  task1_1_sextic_example3.sage
- [x] Create proofs/solved/task1_1_sextic.md documenting verified claim
- [x] Separate literature facts (Coble construction, genus formula) from computational
  verification
- [x] Cross-reference audit/task1_1_birationality_note.md and
  audit/task1_1_exact_coordinate_note.md

### Phase 2: Task 1.2 gram matrices verification note

- [x] Review task1_2_gram_matrices.sage, task1_2_gram_matrices_fixed.sage,
  task1_2b_discriminant_forms.sage
- [x] Create proofs/solved/task1_2_gram_matrices.md documenting verified claim
- [x] Literature context: Nikulin (r,a,δ) invariants, discriminant form theory

### Phase 3: Task 1.3 embeddings verification note

- [x] Review task1_3_embeddings.sage, task1_3_embeddings_fixed.sage,
  task1_3_embeddings_primitive.sage
- [x] Create proofs/solved/task1_3_embeddings.md documenting verified claim
- [x] Literature context: Nikulin primitive embedding theory

### Phase 4: Task 2.2 orbit lift verification note

- [x] Review task2_2_orbit_lift.sage
- [x] Create proofs/solved/task2_2_orbit_lift.md documenting verified claim
- [x] Cross-reference task2_1 (uses orbit classification from task2_1)

### Phase 5: Task 3.1 generators/stabilizer verification note

- [x] Review task3_1_generators.sage, task3_1_stabilizer.sage
- [x] Create proofs/solved/task3_1_stabilizer.md documenting verified claim
- [x] Literature context: orthogonal group structure, reflection groups

## Verification

After each phase:
- git diff to confirm only solved proof note added
- Check literature citations match REFERENCES.md
- Verify computational verification language separates from literature facts

## Success criteria

All 20 computation scripts have corresponding verification notes in proofs/solved/
