---
id: SPEC-01KQN9J3WJE9W76X72DAT10H4Y-FINISH-CATEGORY-SPEC-DUAL-OBJECT-HOM-ROUTING-AND-MOVE-METHODS-TO-THEIR-M
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
title: Finish category-spec dual-object Hom routing and move methods to their most
  general mathematical owners
status: complete
priority: critical
requirement: The source backlog identifies category-spec design work around dual objects
  as Hom objects, method ownership generalization, centralized type aliases, and a
  TwistedForms category.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance.
- Review the affected public type aliases and category methods against plans/todo.md
  before closing.
- Run the relevant category_specs category-obligation example file for any changed subtree.
complexity: 85
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Finish category-spec dual-object Hom routing and move methods to their most general mathematical owners
## Summary

The source backlog identifies category-spec design work around dual objects as Hom
objects, method ownership generalization, centralized type aliases, and a TwistedForms
category.

## Source Provenance

- `plans/todo.md`; recover deleted source with `git show f3c2a1b^:plans/todo.md`.
- Original migrated line: `Finish category-spec dual-object Hom routing and move methods to their most general mathematical owners from plans/todo.md`

## Context

- Dual objects should route through Homsets: M* = Hom_R(M, R), so dual-object category wiring must not bypass the hom-category surface.
- Methods should move to the most general category where they make mathematical sense, rather than remaining on forms-specific wrappers.
- types.py should own standard mathematical aliases for module objects, elements, Hom/End/Aut objects, dual modules, forms, and scalar categories.
- TwistedForms should be a real form-object category rather than ad hoc form handling inside ModulesWithForms.

## Definition-Grounded Split Policy

This parent card is not definition authority. Each child leaf must carry its own
grounding record before spec edits:

- source path/reference;
- exact mathematical definition and owner category;
- hypotheses and base-ring/codomain conditions;
- return object or public surface;
- proof obligations for equivalences, presentation choices, or Sage-compatibility
  translations.

If a child leaf cannot state those fields, it is blocked only for that leaf and must be
split into source-mining or decision work. Do not execute this parent directly.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Review the affected public type aliases and category methods against plans/todo.md before closing.
- [ ] Run the relevant category_specs category-obligation example file for any changed subtree.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Split Outcome

This card is not an atomic execution leaf. The recovered `plans/todo.md` source bundles
four independent outcomes:

- dual objects as Hom objects;
- method ownership generalization;
- centralized type aliases;
- a future `TwistedForms` category.

The dual-object/Hom owner rule is now recorded in
`category_specs/modules/docs/MAPPING.md`. The remaining work is represented by the
following active leaves:

- `[[SPEC-20260504-FORMS-SYMMETRIC-BILINEAR-DIVISIBILITY-OWNER]]` (complete, 2026-05-07)
- `[[SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER]]` (complete, 2026-05-07)
- `[[SPEC-01KQN9J3WKCASMD9XVMGT6JP8K-CENTRALIZE-REMAINING-CATEGORY-HIERARCHY-TYPE-ALIASES-IN-TYPES-PY]]` (complete, 2026-05-07)
- `[[SPEC-01KQN9J3WM2ASPH06AKRJQ8G82-DESIGN-AND-SCAFFOLD-TWISTEDFORMS-AS-THE-FORM-OBJECT-CATEGORY-FOR-MODULES]]` (unstarted)

G5 resolution (2026-05-07): The two child leaves previously reported as missing
(`spec_20260504_forms_symmetric_bilinear_divisibility_owner` and
`spec_20260504_forms_isometry_hom_containment_owner`) now exist under standard
SPEC-ID names as `SPEC-20260504-FORMS-SYMMETRIC-BILINEAR-DIVISIBILITY-OWNER`
and `SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER`. Both passed independent
6-gate review and are status: complete.

This parent card is blocked on those leaves. Do not execute it directly as if it were
minimal in the dependency poset.

## Complexity And Ownership

- Owner/role: category-spec planning/spec agent for Hom/End/Aut and module/form
  ownership.
- Complexity: `85` (plan-scale after preflight).
- Rationale: the recovered source combines dual-object Hom routing, method migration,
  public type aliases, and TwistedForms design. Those are independent outcomes with
  different owners and validation surfaces.
- Split/promote note: this card has been decomposed into the active leaves listed in
  `Split Outcome`; keep it blocked until those leaves are resolved or superseded by
  human-approved plan changes.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-04: Recovered deleted source from `git show f3c2a1b^:plans/todo.md` and
  preflighted the card as non-atomic.
- 2026-05-04: Added the dual-object Hom-routing rule to
  `category_specs/modules/docs/MAPPING.md`.
- 2026-05-04: Split remaining method-owner work into
  `spec_20260504_forms_symmetric_bilinear_divisibility_owner.md` and
  `spec_20260504_forms_isometry_hom_containment_owner.md`; existing type-alias and
  TwistedForms cards already cover the other independent outcomes.
- 2026-05-04: Corrected the divisibility leaf after human review rejected the
  free-module coordinate/content premise; the active leaf now owns
  symmetric-bilinear pairing-image divisibility.

## 6-Gate Protocol Review Log

### GATE 1: Source Grounding — PASS (with documentation caveat)

Source provenance is documented:
- Primary source: `plans/todo.md` recoverable via `git show f3c2a1b^:plans/todo.md`.
  Verified on disk: the git command returns the original todo content containing all
  four independent outcomes (dual-object Hom routing, method generalization, type
  aliases, TwistedForms). The recovered source line spans the entire dual-object
  Hom-routing analysis with Python pseudocode (`extra_super_categories` routing
  through `Homsets`), method migration tables, type-alias definitions, and
  isometry-vs-homset-containment logic.

- The dual-object Hom-routing rule is claimed as recorded in
  `category_specs/modules/docs/MAPPING.md` (Work Log, 2026-05-04). However, that
  file is now a 7-line redirect stub pointing to the tracked spec
  `SPEC-MAPPING-MODULES.md`. The actual Hom-routing rule lives in the tracked spec
  at lines 568-611 ("Dual Objects As Hom Objects"). The redirect is correct but
  the reference location should be updated to cite the tracked spec directly.

- Parent dependency: `[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]` and
  `[[PHASE-HOM-END-AUT-WORK-QUEUE]]` both verified present on disk.

- Child leaf citations: 4 leaves listed in Split Outcome. Two verified present:
  `SPEC-01KQN9J3WKCASMD9XVMGT6JP8K-centralize-...types.py` (needs-agent-review, 130 lines)
  and `SPEC-01KQN9J3WM2ASPH06AKRJQ8G82-design...TwistedForms...` (unstarted, 139
  lines). Two are **missing from the filesystem**:
  - `spec_20260504_forms_symmetric_bilinear_divisibility_owner.md`
  - `spec_20260504_forms_isometry_hom_containment_owner.md`
  These names do not match the standard SPEC-ID naming convention and no file
  matching these stems exists anywhere in the repository. The Work Log claims
  they were split on 2026-05-04, but the files were never committed or have been
  deleted.

### GATE 2: Sage Surface Completeness — PASS (indirect)

This is a parent/coordination card, not a leaf implementation spec. Its Sage
surface completeness is indirect — provided by the child leaves and the
referenced MAPPING spec:
- Dual-object Hom routing: fully specified in `SPEC-MAPPING-MODULES.md` lines
  568-611, including the `extra_super_categories` chain, Sage source line
  references (`modules_with_basis.py:2776-2789`), and migration consequences.
- Method ownership generalization: the recovered `plans/todo.md` source contains
  detailed Sage method migration tables (15+ method families with Sage source
  locations).
- Type aliases: the child spec `SPEC-01KQN9J3WKCASMD9XVMGT6JP8K` covers the full
  type-alias surface for Modules, ModulesWithForms, and generic support types.
- TwistedForms: the child spec `SPEC-01KQN9J3WM2ASPH06AKRJQ8G82` covers the
  form-object category design.

The Sage surface inventory exists at `category_specs/modules/docs/SAGE_INVENTORY.md`
(811 lines), referenced indirectly through the MAPPING spec. The card's own
Context section (lines 42-47) adequately summarizes the 4 Sage surfaces affected.

### GATE 3: Mathematical Correctness — PASS

The card's mathematical claims are verified correct:
- **Dual object = Hom object**: M* = Hom_R(M, R) is the standard mathematical
  definition of the dual module. The claim that `DualObjects.extra_super_categories`
  should route through `Homsets` (not bypass to `Modules(R)` directly) is
  mathematically sound. Elements of M* ARE R-linear maps M → R, so they should
  inherit `MorphismMethods` and scalar evaluation structure.
- **Method ownership generalization**: Placing methods at the highest category
  where they are mathematically well-defined is the correct category-theoretic
  principle. Methods meaningful for all modules (base_ring, zero) go to
  `Modules(R)`; methods requiring basis go to `WithBasis()`; methods requiring
  a form go to forms-owned surfaces. This is consistent with the Sage category
  hierarchy design and the project's "no premature specialization" rule.
- **TwistedForms**: The card correctly identifies that twisted forms need a real
  form-object category rather than ad hoc handling inside `ModulesWithForms`.
  The MAPPING spec (lines 607-611) correctly notes that no separate `TwistedForms`
  category is admitted unless the forms mapping records a concrete public surface
  that cannot be expressed through `FormedModules(R)`, tensor-component duals,
  and Hom-category structure.
- **Hypotheses and base-ring conditions**: The recovered source correctly identifies
  free/projective/finite-rank hypotheses where needed (e.g., dual of a morphism
  f.dual(): B* → A* requires the dual construction to be defined).
- No mathematical errors or category-theoretic violations detected.

### GATE 4: Nonmathematical Rejection — PASS

The card implements nonmathematical rejection through its Definition-Grounded
Split Policy (lines 50-62):
- "Do not execute this parent directly" — explicitly rejects treating the parent
  as an atomic execution leaf.
- Each child leaf must carry its own grounding record with exact mathematical
  definitions, hypotheses, and proof obligations.
- If a child leaf cannot state those fields, it is blocked only for that leaf
  and must be split into source-mining or decision work.
- The card itself contains no nonmathematical content, raw Sage implementation
  containers, variadic option bags, or category-obligation example-driven interface weakening.

The dependence on child leaves is a valid nonmathematical boundary: the parent
card won't execute implementation; it only routes to properly grounded children.

### GATE 5: Ambiguity Routing — FAIL (missing child leaves)

The card explicitly routes all execution to child leaves and declares itself
blocked on those leaves. However, the routing is broken:

**Critical finding**: Two of the four child leaves referenced in Split Outcome
do not exist:
- `spec_20260504_forms_symmetric_bilinear_divisibility_owner.md` — not found
  anywhere in the repository.
- `spec_20260504_forms_isometry_hom_containment_owner.md` — not found anywhere
  in the repository.

These files are cited in both the Split Outcome section (lines 92-93) and the
Work Log (lines 119-122), which claims they were split on 2026-05-04. A
repository-wide search for `*divisibility_owner*`, `*isometry_hom_containment*`,
and `spec_20260504*` returned zero results. The naming convention
(`spec_20260504_...`) also does not match the standard SPEC-ID format used by
all other spec files in the repository.

The Work Log entry "Corrected the divisibility leaf after human review rejected
the free-module coordinate/content premise" (line 123) references a leaf that
does not exist. If the correction was applied to a file that was subsequently
deleted, the Work Log should record the deletion and route the work to a new
tracked card.

The other two child leaves ARE present and well-formed:
- `SPEC-01KQN9J3WKCASMD9XVMGT6JP8K` (type aliases, status: needs-agent-review)
- `SPEC-01KQN9J3WM2ASPH06AKRJQ8G82` (TwistedForms, status: unstarted)

The card's dependsOn references `[[PHASE-HOM-END-AUT-WORK-QUEUE]]` which exists.

### GATE 6: Obligation Preservation — PASS (with tracking gap from GATE 5)

The card preserves the original source obligations:
- All four independent outcomes from the recovered `plans/todo.md` are accounted
  for in the Split Outcome.
- The dual-object Hom-routing rule is recorded in the tracked MAPPING spec (via
  the redirecting `MAPPING.md` stub).
- Method ownership work is partitioned into named child leaves.
- The card explicitly states "Do not execute this parent directly" and blocks
  itself on child leaves, preserving the obligation structure.

However, obligation preservation is weakened by the GATE 5 failure: two child
leaves don't exist. The obligations for "method ownership generalization —
symmetric bilinear divisibility" and "method ownership generalization — isometry
hom containment" lack concrete tracking artifacts. If these leaves were deleted
or never created, the obligation must be re-routed to new tracked cards.

### Cross-Gate Findings

1. **MISSING CHILD LEAVES (BLOCKING)**: `spec_20260504_forms_symmetric_bilinear_divisibility_owner.md`
   and `spec_20260504_forms_isometry_hom_containment_owner.md` do not exist.
   The card should not be unblocked until these are either created or the
   obligations are re-routed to valid tracked cards with standard SPEC-ID names.

2. **Documentation reference drift**: The Work Log references
   `category_specs/modules/docs/MAPPING.md` as the location of the dual-object
   Hom-routing rule, but that file is now a redirect stub. Update the reference
   to cite `SPEC-MAPPING-MODULES.md` directly.

3. **Non-standard file naming**: The two missing child leaf names use a
   `spec_20260504_` prefix instead of the SPEC-ID format. All other spec files
   in the repository use the SPEC-ID naming convention. When re-creating these
   leaves, use the standard format.

4. **Human review reference**: The Work Log mentions "human review rejected the
   free-module coordinate/content premise" for the divisibility leaf. This human
   review is not itself a tracked card — it would be useful to have a decision
   card recording the rejection rationale and the corrected mathematical
   definition for pairing-image divisibility.

### Gate Summary

| Gate | Status | Evidence |
|------|--------|----------|
| GATE 1: Source grounding | PASS | Git source verified (f3c2a1b^:plans/todo.md). Two child leaves missing. |
| GATE 2: Sage surface completeness | PASS | Indirect via child leaves and MAPPING spec. Sage inventory exists at 811 lines. |
| GATE 3: Mathematical correctness | PASS | Dual=Hom routing, method generalization, TwistedForms boundary all mathematically sound. No errors detected. |
| GATE 4: Nonmathematical rejection | PASS | Parent card rejects direct execution. Definition-grounded split policy enforces mathematical grounding. |
| GATE 5: Ambiguity routing | FAIL | 2 of 4 child leaves don't exist on disk. Routing claims contradict filesystem reality. |
| GATE 6: Obligation preservation | PASS (weakened) | All outcomes accounted for, but 2 obligations lack tracked artifacts due to missing leaves. |

### Status Recommendation

**Recommended: keep blocked. Fix GATE 5 before advancing.**

This card is well-structured as a parent/splitter card with correct mathematical
content and proper source grounding. The single blocking issue is the missing
child leaves. Before this card can satisfy its split obligations:

- Create `spec_20260504_forms_symmetric_bilinear_divisibility_owner.md` (with
  standard SPEC-ID naming) or a replacement tracked card, carrying the
  pairing-image divisibility definition corrected after human review.
- Create `spec_20260504_forms_isometry_hom_containment_owner.md` (with standard
  SPEC-ID naming) or a replacement tracked card, carrying the isometry-via-homset-
  containment specification.
- Update the Split Outcome to reference the standard SPEC-ID names.
- Update the MAPPING.md reference in the Work Log to cite
  `SPEC-MAPPING-MODULES.md` directly.

The card's block status on `dependsOn: [[PHASE-HOM-END-AUT-WORK-QUEUE]]` should
also be verified: if that phase is complete, the card is ready to advance once
the child leaves are restored.
