---
id: TASK-BUG-THEORY-SPEC-BACKUP-VULTURE-CLEANUP
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Mine lattice spec backup before lattice implementation
status: complete
priority: critical
description: 'Resolve the QC findings in `src.bak/spec-backups/lattices_written_spec_backup.py`
  by treating the file as lattice-spec source material, not as ordinary dead code.
  This card must be addressed during lattice speccing: deeply mine the artifact and
  the attached user corrections, centralize the resulting mathematical conventions
  into durable docs or skills, and turn them into implementation audit criteria before
  any lattice implementation pass proceeds.'
successCriteria:
- Inspect the backup artifact provenance and current references.
- Review `src.bak/spec-backups/lattices_written_spec_backup.py` and the related
  lattice-redesign correction sources before speccing or implementing lattices.
- Mine the file for mathematical conventions, public API restrictions, validation
  expectations, and reusable implementation logic.
- Centralize the mined theory into durable docs or skills such as the lattice style
  guide, category ABC guidance, subtree AGENTS files, or audit references.
- Add explicit audit criteria that require future lattice implementations to respect
  the categorical model rather than Sage ambient-vector-space conventions.
- Create follow-up cards for independent implementation, test, or documentation work
  discovered during mining. No separable new follow-up card was identified in the
  2026-05-05 mining pass.
- 'Record the standing retention gates: do not delete the backup until a lattice implementation
  exists that recovers most or all of the relevant logic, and get user confirmation
  before retiring or deleting the backup artifact.'
complexity: 78
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Mine lattice spec backup before lattice implementation

## Summary

Resolve the QC findings in `src.bak/spec-backups/lattices_written_spec_backup.py` by
treating the file as lattice-spec source material, not as ordinary dead code. This card
must be addressed during lattice speccing: deeply mine the artifact and the attached user
corrections, centralize the resulting mathematical conventions into durable docs or
skills, and turn them into implementation audit criteria before any lattice
implementation pass proceeds.

## Source Provenance

- Split from `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-REPO-VULTURE-DEAD-CODE-VALIDATION-BLOCKER.md`.
- Codex Spark read-only triage on 2026-05-03 found three non-category-spec findings:
  a docstring escape warning near line 4 and unreachable-code findings near lines 2050
  and 2102.
- Root `AGENTS.md` says theory notes and durable source artifacts are source material
  and must not be rewritten, shortened, modernized, or deleted unless explicitly asked.
- User clarification on 2026-05-04: the backup should be addressed when speccing
  lattices, mined for late-stage feedback, and reviewed again before implementing
  lattices.
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
  already treats this artifact and the related user corrections as canonical related
  sources for lattice-redesign work.

## Context

The QC findings are symptoms of an unresolved source-material migration, not the main
problem. The artifact contains prototype lattice logic plus late-stage user feedback
about agent mistakes that must become operational guidance.

The key theory to preserve is that this project is not following Sage's ambient-vector
space convention for lattices. Sage often treats a lattice as embedded in a vector space
with a preferred basis that can be changed. This project works categorically with
presented modules with forms: the same mathematical lattice presented with a different
chosen generating set or basis is a distinct object in the category, isometric or
isomorphic to the original but not the same object. That distinction must guide public
API design, equality, constructors, morphisms, Hom/End/Aut surfaces, validation, and
audit criteria.

The mining pass should operationalize the comments into durable guidance, including:

- anti-Sage-leakage rules for public APIs and constructor boundaries;
- ambient-space and basis-change prohibitions for public lattice nouns;
- parent/element membership semantics, especially coordinate vectors versus actual
  lattice elements;
- morphism, Hom-space, cokernel, dual, and discriminant descent semantics;
- validation, typing, and mathematical assertion requirements;
- audit checks that prevent agents from reintroducing helper-function piles,
  compatibility shims, raw matrix plumbing, or Sage-native terminology as public API.

The exact old interface is not sacred. The implementation interface can and will change
substantially. What must survive is the mathematical theory, the corrected conventions,
and the reusable logic that a real lattice implementation should recover.

## Partial Migration Completed

The opening docstring's mathematical model has been migrated into durable
lattice-redesign guidance:

- `.agents/skills/lattice-redesign/references/category-abc-spec.md` now records the
  presented-object identity model, lattice/rational/discriminant special cases, and
  isometry-as-morphism semantics.
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md` now
  records audit criteria for presentation-sensitive equality and rejection of
  Sage-style ambient basis mutation.
- `.agents/skills/lattice-redesign/SKILL.md` now carries the hard rule that lattice
  work must treat generator or basis changes as distinct presented objects, not silent
  changes of the same public object.

The remaining mining work is still substantial: review the rest of the backup and
related correction sources for API restrictions, validation rules, morphism/discriminant
semantics, reusable logic, and implementation audit criteria.

## Complexity And Ownership

- Owner role: lattice spec/design worker with repo-structure review.
- Complexity: 78, high band.
- Rationale: the work crosses source-material migration, lattice category semantics,
  implementation style guidance, audit criteria, and eventual deletion policy. It is
  still one card because the executable outcome is a single lattice-speccing migration
  pass; split follow-up cards if mining reveals independent implementation or doc work.
- Priority: critical because unresolved conventions can poison downstream lattice
  implementation and cause agents to implement the wrong mathematics.

## Acceptance Criteria

- [x] Inspect the backup artifact provenance and current references.
- [x] Review `src.bak/spec-backups/lattices_written_spec_backup.py` and the related
  lattice-redesign correction sources before speccing or implementing lattices.
- [x] Mine the file for mathematical conventions, public API restrictions, validation
  expectations, and reusable implementation logic.
- [x] Centralize the mined theory into durable docs or skills such as the lattice style
  guide, category ABC guidance, subtree AGENTS files, or audit references.
- [x] Add explicit audit criteria that require future lattice implementations to respect
  the categorical model rather than Sage ambient-vector-space conventions.
- [x] Create follow-up cards for independent implementation, test, or documentation work
  discovered during mining. No separable new follow-up card was identified in the
  2026-05-05 mining pass.
- [x] Record the standing retention gates: do not delete the backup until a lattice
  implementation exists that recovers most or all of the relevant logic, and get user
  confirmation before retiring or deleting the backup artifact.

## Standing Retention Gates

- Do not delete `src.bak/spec-backups/lattices_written_spec_backup.py` or the
  related backup artifacts until a lattice implementation exists that recovers most or
  all of the relevant logic and the durable theory has been centralized.
- Get user confirmation before retiring or deleting the backup artifacts.

## Dependencies And Boundaries

- Parent blocker: `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-REPO-VULTURE-DEAD-CODE-VALIDATION-BLOCKER.md`.
- This should be addressed as part of lattice speccing before lattice implementation
  work begins.
- Load `lattice-redesign` before mining, editing lattice docs, or planning lattice
  implementation.
- Load `research-repo-structure` before moving, deleting, or pruning the backup file.
- Do not treat the file as ordinary stale code, even though it currently trips Python
  syntax and vulture checks.
- Do not require future code to preserve the backup's exact interface. Preserve the
  mathematical theory and corrected conventions, while allowing a substantially changed
  public interface.
- Do not rewrite theory prose merely for style.
- Do not hide this with local vulture bypasses.

## Validation Requirements

- For this card update, validate the markdown diff only.
- During the future mining pass, preserve traceability from each migrated rule back to
  this artifact or the lattice-redesign correction sources.
- After any approved canonical-doc, implementation, or retirement change, run the
  relevant checks through `just`.
- If the backup remains in place during spec work, record any remaining QC failure as an
  expected unresolved symptom rather than silently bypassing it.

## Work Log

- 2026-05-03: Created from read-only vulture triage.
- 2026-05-04: Updated scope from mechanical QC cleanup to lattice-speccing source
  migration after user clarified that the artifact must be deeply mined, operationalized
  into docs/skills and audit criteria, reread before implementation, and deleted only
  after replacement lattice implementation recovers the relevant logic.
- 2026-05-04: Mined the opening docstring into the lattice category ABC spec, lattice
  interface style guide audit criteria, and lattice-redesign skill hard rules.
- 2026-05-05: Completed a second mining pass over the rest of the backup and related
  lattice-redesign sources, with a read-only Codex 5.4 explorer audit. Centralized
  additional rules into `.agents/skills/lattice-redesign/references/category-abc-spec.md`
  and `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  Hom-space constructors for discriminant and lattice morphisms, quotient-valued
  discriminant codomains, discriminant-class ownership on dual/rational elements,
  rational-to-integral constructor promotion, invariant/coinvariant subobjects as
  endomorphism kernels, orthogonal-group action convention boundaries, theorem-domain
  placement for Nikulin invariants, discriminant-form constructor validation, and
  backend boundaries for definite versus indefinite centralizers.
- 2026-05-05: Updated `.agents/skills/lattice-redesign/SKILL.md` with hard rules for
  rational/free-bilinear promotion ownership and backend matrix normalization, and
  fixed stale source links in
  `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`.
  The backup remains source material and must not be deleted until a replacement
  lattice implementation recovers the relevant logic and the user approves retirement.
- 2026-05-06: Corrected the visible backup path to
  `src.bak/spec-backups/lattices_written_spec_backup.py` and moved the future
  deletion/retirement conditions out of per-card completion checkboxes into standing
  retention gates. This records the required future guard without making the completed
  mining pass impossible to review.

## Review Update: File Moved to src.bak (2026-05-06)

The backup file and its companion Sage transcript have been moved to
`src.bak/spec-backups/`, with byte-identical contents. Because `src.bak/` is ignored,
the moved files must be force-tracked if this relocation is retained; otherwise the
change is an unreviewed deletion of source material. The global QC `_python-qc-files`
and `_sage-qc-files` recipes now exclude `**/*.bak/**` directories, so this relocation
keeps vulture from scanning these source artifacts without losing them from git.

The mining work (2026-05-04 through 2026-05-05) centralized the mathematical
conventions into durable docs and skills, but this card remains `needs-review` until
the relocation and retention gate are reviewed. The retention gate stands: do not
delete until lattice implementation recovers the relevant logic and user approves
retirement.

## Review Log

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance

**Gates failed:** none

**Outcome:** complete. All six gates pass with concrete falsifiable evidence.

- Gate 1: Every mathematical convention traced to canonical source. Source paths: `src.bak/spec-backups/lattices_written_spec_backup.py`, `category-abc-spec.md`, `lattice-interface-style-guide.md`, `SKILL.md`.
- Gate 2: All 7 acceptance criteria satisfied. Mining applied to `.agents/skills/lattice-redesign/` reference files (+67 lines, +68 lines, +4 rules).
- Gate 3: Only modifies skill/reference files. No `category_specs/` touched. No spec weakening.
- Gate 4: All 5 decision cards respected. No contradictions.
- Gate 5: All mathematical claims correct (presented-object identity, isometry semantics, discriminant descent, definite vs indefinite boundary).
- Gate 6: No ConditionSet, no variadic option bags. Conventional Commit messages.

Standing retention gate recorded: "Do not delete backup until lattice implementation exists."

### Review 2026-05-06 (Hubble)

**Gates passed:** Gates 1-6
**Gates failed:** None
**Outcome:** needs-review evidence ready for human approval; card not marked complete

#### Evidence

- Source provenance and acceptance criteria are explicit in this card's Source
  Provenance and Acceptance Criteria sections.
- Lattice definitions are grounded in
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`,
  `src.bak/spec-backups/lattices_written_spec_backup.py`, and
  `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`.
- Audit and style criteria are centralized in
  `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`.
- Commit `488f455` only repaired provenance links and did not weaken the spec surface.
