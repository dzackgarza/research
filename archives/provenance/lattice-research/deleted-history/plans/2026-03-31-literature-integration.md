# Literature Integration Implementation Plan

**Date**: 2026-03-31\
**Goal**: Integrate Pieroni 2026 and Huybrechts K3 Lectures findings across repository\
**Status**: Analysis complete (`audit/new_literature_connections.md`), 1/11 proof notes
updated\
**Timeframe**: Single session

## Overview

Connections identified in `audit/new_literature_connections.md`:
- **Task 1.1 (Sextic)**: EXTENDS Pieroni's theoretical framework (lines 752-759,
  1225-1280)
- **Task 3.2 (Isotropic)**: MATCHES Pieroni Theorem 46 (line 1209)
- **Task 5.1 (Involutions)**: EXTENDS Pieroni Theorem 72 (line 2068)
- **Lattice structure**: MATCHES Pieroni E₁₀ framework (lines 146, 483-493)
- **Huybrechts**: BACKGROUND/context for lattice theory

## Task-by-Task Integration Requirements

### 1. Update Proof Notes (`proofs/solved/*.md`, 11 files)

| File | Connection | Update Required |
| --- | --- | --- |
| `task1_1_sextic.md` | Already has Pieroni citation (lines 55-59) | Add full Pieroni reference with quote/line numbers |
| `task3_2_isotropic_planes.md` | Matches Pieroni Theorem 46 | Add Theorem 46 citation with proof note |
| `task5_1_involution.md` | Extends Pieroni Theorem 72 | Add classification of involutions as Bertini lifts |
| `task1_2_gram_matrices.md` | Lattice structure matches Pieroni E₁₀ | Add E₁₀ = Num(X) connection |
| `task1_3_embeddings.md` | Lattice context | Add Pieroni/Huybrechts as background |
| `task2_1_isotropic_orbits.md` | Uses isotropic sequences | Add Pieroni isotropic sequence theory |
| `task2_2_orbit_lift.md` | Orbit theory | Add Pieroni lattice context |
| `task3_1_stabilizer.md` | Stabilizer computations | Add Pieroni lattice automorphism context |
| `task4_1_coxeter_search.md` | Coxeter groups | Add Pieroni Nikulin reference [28] |
| `task6_1_slc_stability.md` | Moduli theory | Add Pieroni moduli dimension context |
| `utilities_note.md` | General lattice utilities | Add Pieroni/Huybrechts lattice background |

**Update pattern for each proof note**:
1. Add relevant Pieroni/Huybrechts citations inline with precise references
2. Update "Literature" or "Mathematical Context" section
3. Distinguish MATCH vs EXTEND vs CONTEXT
4. Add audit trail comment

### 2. Update Computation Scripts (`computations/task*.sage`)

Scripts requiring documentation updates:

| Script | Connection | Update Required |
| --- | --- | --- |
| `task1_1_sextic.sage` | Pieroni lines 752-759 | Add docstring citing Pieroni theoretical context |
| `task1_1_sextic_example2.sage` | Same as above | Add citation header |
| `task1_1_sextic_example3.sage` | Same as above | Add citation header |
| `task3_2_isotropic_planes.sage` | Pieroni Theorem 46 | Add theorem reference |
| `task5_1_involution.sage` | Pieroni Theorem 72 | Add Bertini involution classification |
| `coble_geometry.sage` / `coble_geometry_foundation.sage` | General lattice framework | Add Pieroni E₁₀ framework citation |
| `task1_2_gram_matrices.sage` | Lattice structure | Add Pieroni E₁₀ = Num(X) connection |
| `task1_3_embeddings.sage` | Lattice embeddings | Add Pieroni/Huybrechts context |

**Update pattern**:
1. Add documentation header with precise Pieroni/Huybrechts references
2. Add inline comments linking code sections to theorems
3. Update function docstrings where applicable
4. Maintain backward compatibility

### 3. Update Foundational Docs (`audit/` files)

Key files requiring updates:

| File | Update Required |
| --- | --- |
| `literature_claim_map.md` | Add Pieroni as canonical source for Coble surface theory, Huybrechts as K3 background |
| `verification_process.md` | Add literature validation step: check against Pieroni/Huybrechts |
| `literature_connection_audit.md` | Incorporate new literature findings |
| `task3_2_status.md` | Update with Pieroni Theorem 46 connection |

**Update pattern**:
1. Incorporate Pieroni/Huybrechts into canonical reference spine
2. Add explicit connections: Pieroni E₁₀ = S_Co, Theorem 46 = isotropic sequences, etc.
3. Update verification checklist to include literature alignment
4. Add audit trail documenting integration

### 4. Update Summary Docs

| File | Update Required |
| --- | --- |
| `GAPS.md` | Mark literature integration as completed |
| `PLAN.md` | Update project completion status (currently 98%) |
| `CHANGELOG.md` | Add entry for literature integration |
| `REFERENCES.md` | Ensure Pieroni 2026, Huybrechts K3 Lectures included |

## Acceptance Criteria

1. **All 11 proof notes** updated with relevant Pieroni/Huybrechts citations
2. **All referenced Sage scripts** have documentation headers citing literature
3. **Foundational audit files** incorporate new sources
4. **Summary docs** reflect completed integration
5. **No regressions**: All Sage scripts still run correctly
6. **Citation precision**: All references include exact line numbers/theorem numbers

## Verification Checklist

- [ ] Proof notes: Check each `proofs/solved/*.md` for Pieroni/Huybrechts citations
- [ ] Computation scripts: Run `sage computations/*.sage` to ensure no errors
- [ ] Foundational docs: Verify `audit/literature_claim_map.md` includes Pieroni
- [ ] Summary docs: Verify `CHANGELOG.md` has integration entry
- [ ] Git hygiene: All changes committed with clear messages

## Implementation Order

1. **Create verification checklist** (this file)
2. **Update proof notes** (11 files, systematic batch)
3. **Update computation scripts** (documentation only)
4. **Update foundational docs** (audit files)
5. **Update summary docs** (GAPS.md, PLAN.md, CHANGELOG.md)
6. **Run verification** (execute Sage scripts, check references)
7. **Final commit** with integration summary

## Constraints

- **Preserve correctness**: Don't break existing functionality
- **Precise citations**: Always include exact line/theorem numbers
- **Distinguish relationships**: MATCH vs EXTEND vs CONTEXT
- **Minimal changes**: Focus on integration, not rewriting
- **Git hygiene**: Frequent commits with descriptive messages

## Expected Outcome

Repository fully reflects literature connections identified in
`audit/new_literature_connections.md`, with:
- Proof notes citing relevant theorems
- Computation scripts documented with literature context
- Foundational docs updated with new canonical sources
- Project status updated to reflect completed integration

**Time estimate**: Single session (2-3 hours)

<｜DSML｜function_calls> <｜DSML｜invoke name="bash"> <｜DSML｜parameter name="command"
string="true">grep -l "task.*.sage" proofs/solved/*.md
