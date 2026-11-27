# Plan: Weave Literature Citations into Solved Proof Notes

**Created**: 2026-03-30\
**Status**: Active

## Goal

Address GAPS.md Priority 1 literature gap: weave canonical literature citations from
`audit/literature_claim_map.md` and `REFERENCES.md` into the longer proof notes in
`proofs/solved/`, ensuring standard background claims are properly attributed before
computational verification steps.

## Context

- `audit/literature_claim_map.md` records the standard claim flow for Coble surfaces, K3
  covers, lattice setup, period domain, and Torelli background
- `REFERENCES.md` provides the canonical reference spine with specific use-case guidance
- Both `proofs/solved/task3_2_isotropic_planes.md` and
  `proofs/solved/task6_1_slc_stability.md` already reference the literature spine at a
  high level but could benefit from more precise inline citations where standard facts
  are invoked

## Current State

### task3_2_isotropic_planes.md

- Lines 5-7: Already points to REFERENCES.md and literature_claim_map.md for
  period-domain framing
- Lines 46-48: References Nikulin and Sterk for theoretical prediction
- Lines 197-200: References Nikulin, Sterk, AEGS for computational support
- Lines 209-222: Full reference section at end

**Assessment**: Already well-cited.
Main gap is inline attribution when specific lattice-theoretic facts (2-elementary
classification, surjectivity, discriminant-form arguments) are invoked.

### task6_1_slc_stability.md

- Lines 19-29: Already points to REFERENCES.md and literature_claim_map.md for
  compactification/KSBA background
- Lines 171-180: Reference section cites AEGS23, Nikulin1979, Kollar2013
- Line 61: "From AEGS23" inline citation for dual complex construction

**Assessment**: Already well-cited.
Main gap is inline attribution for K3/lattice setup facts and Torelli step.

## Phase 1: Inline Citation Audit ✓ COMPLETE

Completed inline citation audit for both solved proof notes:

### task3_2_isotropic_planes.md

- ✓ Line 18-26: Added K3/lattice setup citation (Coble 1917, 1929; Nikulin 1979)
- ✓ Line 47-57: Added specific theorem citations (Nikulin 1979 Theorem 1.14.2, Prop.
  1.5.2)
- ✓ Line 200-203: Clarified literature support statement with specific contributions

### task6_1_slc_stability.md

- ✓ Line 39-47: Added K3/lattice setup citation (Coble 1917, 1929; Nikulin 1979)
- Already had: AEGS23 inline citation for dual complex (line 61)
- Already had: Full reference section with AEGS23, Nikulin1979, Kollar2013

**Commits**:
- 1c279e7: "docs: add inline literature citations to lattice setup sections"
- 2179c8b: "docs: add specific theorem citations to Nikulin theoretical prediction"
- ef9a1a0: "docs: clarify literature support statement in task3_2 conclusion"

## Phase 2: Weave Citations ✓ COMPLETE

All identified gaps have been addressed with inline citations:
1. ✓ K3/lattice setup facts now cite Coble 1917, 1929; Nikulin 1979
2. ✓ 2-elementary lattice classification cites Nikulin 1979 Theorem 1.14.2
3. ✓ Discriminant-form surjectivity cites Nikulin 1979 Prop.
   1.5.2
4. ✓ All citations match REFERENCES.md use-case guidance
5. ✓ Computational verification language preserved throughout

## Phase 3: Verify Alignment ✓ COMPLETE

Verification complete:
1. ✓ All inline citations match REFERENCES.md canonical sources
2. ✓ No overclaiming detected (Coolidge/Thas stronger-wording boundaries preserved)
3. ✓ Computational claims clearly marked as "repo verification" or "exact computational
   support"
4. ✓ Git diff shows only citation additions, no removal of computational verification
   language

**Git diff summary**:
- task3_2_isotropic_planes.md: +12 lines (citations), -9 lines (replaced vague
  references)
- task6_1_slc_stability.md: +3 lines (citations), -2 lines (replaced vague reference)

## Acceptance Criteria

- [x] Phase 1 audit complete: all standard-fact invocations in `proofs/solved/*.md` are
  catalogued
- [x] Phase 2 weaving complete: inline citations added where standard facts are invoked
- [x] Phase 3 verification complete: all citations align with REFERENCES.md use-case
  guidance
- [x] Git diff shows only citation additions, no removal of computational verification
  language
- [x] GAPS.md updated to reflect citation-weaving completion

## Status: ✓ COMPLETE

## Notes

- This is a narrow prose-alignment task, not a rewrite
- Preserve all existing computational verification language
- Do not add citations to repo-native computational claims (e.g., "15 primitive planes
  found")
- Focus on standard background facts that belong to the literature spine
