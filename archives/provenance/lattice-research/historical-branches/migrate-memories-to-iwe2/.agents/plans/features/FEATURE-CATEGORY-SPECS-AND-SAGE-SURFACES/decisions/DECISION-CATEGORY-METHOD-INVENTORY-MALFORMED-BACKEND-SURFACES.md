---
id: DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide public names for malformed backend-mapping source surfaces
status: decided
chosen: Reject malformed spellings and rename through source-grounded owners
options:
- name: Preserve malformed source spellings as public methods
  pros:
  - Literal migration from the old abstract map is mechanically complete.
  cons:
  - Corrupt names would poison the public API and downstream spec rows.
- name: Reject malformed spellings and rename through source-grounded owners
  pros:
  - Keeps public method names mathematical and reviewable.
  - Separates backend availability from source-file typo cleanup.
  cons:
  - Requires a small follow-up decision before implementation cards can use these rows.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide public names for malformed backend-mapping source surfaces

## Summary

`theory/backends/abstract-to-external-mapping.md` contains two source surfaces that
should not be normalized silently:

- `PicardeLattice.underlying_picard_group()`
- `Lattice.vinberg_sh姚()`

The backend inventory records rows for both surfaces so the source map is complete, but
it does not admit those literal spellings as public project API.

## Source Provenance

- Legacy references in cards name `theory/backends/*`; in this worktree those backend
  memory files are present under `the iwe2 vault (theory backend memories; iwe2 search)*`.
- `projects/github.com__dzackgarza__lattice-research/references/abstract-to-external-mapping`
- `projects/github.com__dzackgarza__lattice-research/references/software-capability-map`
- `projects/github.com__dzackgarza__lattice-research/advice/theory-backends-vinberg-algorithm`
- `projects/github.com__dzackgarza__lattice-research/references/oscar-lattices`
- `projects/github.com__dzackgarza__lattice-research/advice/library-integration`
- `category_specs/lattices/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`

## Context

The issue is not backend availability alone. Oscar/Hecke, Indefinite.jl, CARAT, GAP,
and Vinberg-specific notes all provide plausible backend routes for nearby
mathematical operations. The blocker is public method naming and owner placement:
malformed spellings must not be promoted into category specs or implementation tasks.

## Acceptance Criteria

- [ ] The decision states the replacement public surface or rejection for
  `PicardeLattice.underlying_picard_group()`.
- [ ] The decision states the replacement public surface or rejection for
  `Lattice.vinberg_sh姚()`.
- [ ] The chosen names cite the lattice/forms mapping docs or create the missing
  source-mining card if the current docs are insufficient.
- [ ] Any implementation card that depends on these methods links to this decision
  rather than relying on the malformed source spelling.

## Dependencies And Boundaries

- Do not implement either malformed method name.
- Do not treat this decision as approval for a local Vinberg implementation.
- Keep the backend rows in the method inventory as source-map coverage, but keep the
  public API blocked until this decision is resolved.

## Decision

Reject both malformed literal spellings as public API.

`PicardeLattice.underlying_picard_group()` is not admitted. The malformed owner spelling
`PicardeLattice` is rejected outright. The intended mathematical bridge, if admitted by
`[[DECISION-CATEGORY-METHOD-INVENTORY-PICARD-GROUP-LATTICE-OWNER]]`, must use the
correct noun spelling `PicardLattice.underlying_picard_group()` on a Picard-lattice
owner and must return the underlying `PicardGroup` object. Until that Picard
group/lattice decision is made, the backend row remains source-map coverage only and is
not implementation permission.

`Lattice.vinberg_sh姚()` is not admitted and has no direct replacement public spelling
from the backend map. The only source-grounded direction is Vinberg-algorithm work that
returns named mathematical output: simple roots, Coxeter matrix, Gram matrix, and the
control vector/chamber data recorded by the Vinberg backend notes. Public surfaces for
that work must be admitted in the Phase 05 lattice/Coxeter cards and must route through
Oscar/Vinberg reference implementations before any bespoke implementation. This
decision only rejects the malformed spelling and confirms that it cannot appear in
category specs, category-obligation tests, or implementation tasks.

## Inventory Updates

- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` now marks the malformed
  Picard row as rejected under the literal spelling and routes the corrected bridge
  spelling through the Picard group/lattice owner decision.
- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` now marks the malformed
  Vinberg row as rejected under the literal spelling and routes future Vinberg surfaces
  to named algorithm-result outputs under the lattice/Coxeter Phase 05 cards.

## Work Log

- 2026-05-06: Created while translating backend method rows for the literal method
  ownership inventory.
- 2026-05-06: Rejected both malformed literal spellings as public API and recorded
  source-grounded replacement routing.
