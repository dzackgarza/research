# Documentation Pruning Plan

**Created**: 2026-03-30 **Status**: Active

## Context

Repo has accumulated 264K audit/, 92K plans/, 32K reports/ with 3593 lines of .txt
transcripts. Recent autonomous work spiraled into documentation churn instead of
mathematical progress.
Need to prune transient artifacts while preserving canonical notes.

## Canonical files to preserve

- `audit/literature_claim_map.md` — canonical claim map
- `audit/moduli_dimension_claim.md` — canonical moduli dimension statement
- `audit/task1_1_birationality_note.md` — canonical birationality note
- `audit/task1_1_exact_coordinate_note.md` — canonical exact coordinate note
- `audit/task5_1_exact_involution_note.md` — canonical involution scope note
- `audit/task5_1_route_reset.md` — canonical route order note
- `audit/carat_capability_audit.md` — CARAT capability reference

## Transient artifacts to archive

### audit/*.txt transcripts (3593 lines total)

- `audit/example1_final.txt` — superseded by task1_1_sextic.md
- `audit/example2_final.txt` — superseded by task1_1_sextic.md
- `audit/example3_final.txt` — superseded by task1_1_sextic.md
- `audit/final_full_run_audit.txt` — superseded by solved proof notes
- `audit/run-all-20260326-1837.txt` — superseded by solved proof notes
- `audit/run_all_audit.txt` — superseded by solved proof notes
- `audit/run_all_audit_v2.txt` — superseded by solved proof notes
- `audit/task1_3_audit.txt` — superseded by task1_3_embeddings.md
- `audit/task2_1_audit.txt` — superseded by task2_1_isotropic_orbits.md
- `audit/task2_2_audit.txt` — superseded by task2_2_orbit_lift.md
- `audit/task3_2_audit.txt` — superseded by task3_2_isotropic_planes.md
- `audit/task5_1_final_audit.txt` — superseded by task5_1_involution.md
- `audit/task5_1_final_v2.txt` — superseded by task5_1_involution.md
- `audit/task5_1_rerun_20260327T122004Z.txt` — superseded by task5_1_involution.md

### audit/*.md duplicates

- `audit/computational_audit_report.md` — superseded by solved proof notes
- `audit/final_audit_report.md` — superseded by solved proof notes

### reports/ duplicates

- `reports/desargues_thas_source_trace.md` — duplicates GAPS.md content
- `reports/task1_1_family_report_audit.md` — duplicates GAPS.md content

## Execution

### Phase 1: Archive transient transcripts ✓

- Created `audit/archive/` directory
- Moved all 14 .txt transcripts to archive
- Commit 36e9ba9: "chore: archive superseded audit transcripts"

### Phase 2: Archive duplicate reports ✓

- Moved audit/computational_audit_report.md to archive
- Moved audit/final_audit_report.md to archive
- Removed reports/ directory (content duplicates GAPS.md)
- Commit b3b3b6b: "chore: remove reports/ directory (content duplicates GAPS.md)"
- Commit 088395d: "chore: archive duplicate audit reports"

### Phase 3: Update PLAN.md ✓

- Removed documentation proliferation warning
- Updated documentation budget principle
- Commit b691918: "docs: update PLAN.md and GAPS.md after documentation pruning"

### Phase 4: Update GAPS.md ✓

- Removed "Repo cleanup gaps" section
- Commit 27ebe86: "docs: remove repo cleanup gap after pruning"

## Verification

- Canonical notes remain in audit/
- All transient artifacts archived
- proofs/solved/ untouched
- PLAN.md reflects clean state
