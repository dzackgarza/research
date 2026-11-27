# Plan: Create Clean Literature-Backed Moduli Dimension Statement

**Created**: 2026-03-30\
**Status**: Active

## Goal

Address GAPS.md Priority 1 literature gap: create a clean literature-backed statement of
the precise variant of the moduli claim used by this repo, specifically the
9-dimensional period-domain description for Coble surfaces.

## Context

From `audit/literature_claim_map.md` and `REFERENCES.md`:
- The standard claim: once the K3 lattice has signature (2,9), the associated Type IV
  period domain has complex dimension 9
- Canonical sources: Scattone (1987) for Type IV/Baily-Borel on K3 side, Sterk (1991)
  for Enriques period-space, Dolgachev-Kondō (2013) for Coble/nodal Enriques moduli
- The repo should cite this standard period-domain framing before any local restatement

Current state:
- `proofs/solved/task3_2_isotropic_planes.md` references the period-domain framing at
  high level (lines 5-7)
- `proofs/solved/task6_1_slc_stability.md` references the compactification/KSBA
  background (lines 19-29)
- No standalone canonical statement exists in repo prose that precisely states the
  moduli dimension claim with full literature attribution

## Phase 1: Locate Appropriate File

Determine where the canonical moduli dimension statement should live:
- Option A: Create new `audit/moduli_dimension_claim.md` as standalone canonical note
- Option B: Extend `audit/literature_claim_map.md` with more detailed moduli section
- Option C: Add to existing solved proof notes as a "Background" subsection

**Decision**: Option A (new canonical note) — keeps the claim isolated and reusable,
follows the pattern of `audit/task1_1_birationality_note.md` and
`audit/task5_1_exact_involution_note.md`

## Phase 2: Draft Canonical Statement

Create `audit/moduli_dimension_claim.md` with:
1. Precise statement of the moduli dimension claim
2. Full literature attribution chain (Scattone, Sterk, Dolgachev-Kondō, Friedman)
3. Explicit separation of what is standard literature vs.
   what is repo-specific computation
4. Use-case guidance for when to cite this note vs.
   the original sources

## Phase 3: Update Cross-References

Update files that invoke the moduli dimension claim:
- `proofs/solved/task3_2_isotropic_planes.md`: add inline citation to new canonical note
- `proofs/solved/task6_1_slc_stability.md`: add inline citation to new canonical note
- `audit/literature_claim_map.md`: add pointer to new canonical note in "Period domain
  and dimension count" section

## Phase 4: Update GAPS.md

Remove the completed moduli dimension statement gap from GAPS.md

## Acceptance Criteria

- [x] Phase 1 complete: file location determined
- [x] Phase 2 complete: `audit/moduli_dimension_claim.md` created with full literature
  attribution
- [x] Phase 3 complete: cross-references updated in solved proof notes and
  literature_claim_map.md
- [x] Phase 4 complete: GAPS.md updated to reflect completion
- [x] All citations match REFERENCES.md use-case guidance
- [x] Statement clearly separates standard literature from repo-specific computation

## Status: ✓ COMPLETE

**Commits**:
- 7306b22: "docs: create plan for moduli dimension canonical statement"
- 1de754d: "docs: create canonical moduli dimension claim note"
- 5ff5c6a: "docs: add pointer to moduli_dimension_claim.md in literature_claim_map"
- dcd5b85: "docs: add moduli_dimension_claim.md cross-references to solved proofs"
- eb41c4c: "docs: add moduli_dimension_claim.md reference to task6_1"
- [pending]: "docs: remove completed moduli dimension statement gap from GAPS.md"

## Notes

- This is a narrow documentation task, not new research
- The claim itself is standard; the gap is lack of a clean canonical statement in repo
  prose
- Focus on precision and reusability for future citations
