---
id: SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER
trackerStatus:
  type: spec
parents:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
dependsOn:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
title: Route form-preserving isometry predicates through formed-module Hom containment
status: complete
priority: critical
requirement: Split the `plans/todo.md` method-generalization item into an atomic owner-fix
  card for form-preserving and isometry predicates on morphisms.
acceptanceCriteria:
- The forms or modules mapping docs state that form preservation is represented by
  membership in the formed-module Hom category.
- '`category_specs/forms/subcategories/free_bilinear.py` does not own a redundant
  generic `is_isometry()` predicate unless it is explicitly documented as a compatibility
  alias over Hom containment.'
- Lattice hom/aut surfaces distinguish lattice isometries as morphisms/aut objects
  in `Lattices(R).HomCategory()` / `Lattices(R).AutCategory()`, not as the owner of
  the generic form-preservation predicate.
- Any implementation blockers are split into implementation cards with source provenance,
  or no new blocker remains after the local spec-surface correction.
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
---
# Route form-preserving isometry predicates through formed-module Hom containment

## Summary

Split the `plans/todo.md` method-generalization item into an atomic owner-fix card for
form-preserving and isometry predicates on morphisms.

## Source Provenance

- Deleted source: `plans/todo.md`, recover with `git show f3c2a1b^:plans/todo.md`.
- Original source section: `Removal of Redundant Predicates`.
- Current observed surfaces:
  - `category_specs/forms/subcategories/free_bilinear.py`
  - `category_specs/lattices/homsets.py`
  - `category_specs/topological_spaces/homsets.py` for a same-name but different
    metric-space use that must not be conflated with formed-module isometry.

## Context

The source note says to remove `is_isometry()` and `is_form_preserving()` from
forms-local bilinear morphism methods and replace them with homset containment:

```text
phi in Hom(L, M, category=Modules(R).WithForms().Bilinear())
```

At the spec level, a morphism preserves form data exactly when it is an element of the
hom object in the category of modules carrying that form. Orthogonal groups are then
aut objects in the formed-module category, not ad hoc boolean filters on ordinary
module morphisms.

## Definition Grounding

- Canonical sources:
  - `category_specs/cat/docs/MAPPING.md` for direct `A.Hom(B)` ownership and
    Hom/End/Aut routing.
  - `category_specs/forms/docs/MAPPING.md` for formed-module ownership of bilinear
    evaluation and orthogonal groups.
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`, "Presented
    Object Identity" and morphism semantics.
  - `theory/foundations/bilinear-forms-duals-morphisms.md`, "Base Change and
    Morphisms".
- Definition: a morphism of bilinear `R`-modules
  `f: (M1, beta1) -> (M2, beta2)` is an `R`-module morphism satisfying
  `beta1(v, w) = beta2(f(v), f(w))` for all `v, w in M1`. An isometry is an
  isomorphism with this property.
- Owner: the formed-module Hom category owns containment/form-preservation; the Aut
  category owns invertible form-preserving endomorphisms.
- Hypotheses: source and target carry compatible bilinear form data over the same base
  ring or an explicitly recorded semilinear/base-change map.
- Codomain/return object: containment returns membership in a Hom/Aut parent, not a
  standalone boolean method unless documented as a compatibility alias over that
  membership.
- Proof obligations: any matrix criterion must be proven equivalent to the categorical
  form-preservation equation under explicit presentation/basis hypotheses.

## Complexity And Ownership

- Owner/role: category-spec spec implementer for Hom/End/Aut and forms.
- Complexity: `65` (high).
- Rationale: this affects public morphism semantics across forms and lattices and must
  distinguish formed-module isometry from metric-space isometry.
- Split/promote note: keep this card limited to formed-module/lattice morphism
  containment. Do not include topological/metric isometry unless an audit proves that
  surface has the same owner.

## Acceptance Criteria

- [x] The forms or modules mapping docs state that form preservation is represented by
  membership in the formed-module Hom category.
- [x] `category_specs/forms/subcategories/free_bilinear.py` does not own a redundant
  generic `is_isometry()` predicate unless it is explicitly documented as a compatibility
  alias over Hom containment.
- [x] Lattice hom/aut surfaces distinguish lattice isometries as morphisms/aut objects
  in `Lattices(R).HomCategory()` / `Lattices(R).AutCategory()`, not as the owner of the
  generic form-preservation predicate.
- [x] Any implementation blockers are split into implementation cards with source
  provenance, or no new blocker remains after the local spec-surface correction.

## Grounded Spec Decision

Decision: form preservation is Hom containment in the relevant formed-module category.

For `C <= FormedModules(R)` and objects `M, N in C`, the public form-preserving morphism
surface is `C.HomCategory().Of(M, N)`. A candidate plain module morphism starts in
`Modules(R).HomCategory()` and belongs to the formed-module Hom object exactly when it
satisfies the form-compatibility equation recorded in the source grounding above.

Consequences recorded in this pass:

- `category_specs/forms/docs/MAPPING.md` now states the Hom-containment owner,
  isomorphism/isometry distinction, orthogonal-group owner, and metric-isometry
  boundary.
- `category_specs/modules/docs/MAPPING.md` now states the same rule at the module Hom
  layer so future module-Hom work does not reintroduce a boolean predicate owner.
- `.agents/skills/lattice-redesign/references/category-abc-spec.md` now aligns the ABC
  sketch with Hom containment and treats `is_isometry()` as `is_isomorphism()` inside an
  already form-preserving Hom object.
- `category_specs/forms/subcategories/free_bilinear.py` and
  `category_specs/lattices/homsets.py` now document `is_isometry()` as an isomorphism
  compatibility query, not as the owner of form preservation.

Matrix equations remain valid implementation checks only after a presentation and
generators have been fixed; they are not the public definition of form preservation or
isometry.

## Dependencies And Boundaries

- Depends on the Cat/Hom ownership rules in `category_specs/cat/docs/MAPPING.md`.
- Do not weaken lattice orthogonal-group semantics; preserve the categorical meaning
  `O(M,b) = Aut(M,b)` in the formed-module category.
- Do not conflate metric-space isometries in `topological_spaces/homsets.py` with
  formed-module isometries.

## Validation Requirements

- Run the relevant category-spec smoke for any changed forms, lattice, or homsets
  runtime surface.
- At minimum, rerun:
  `rg -n "is_form_preserving|is_isometry" category_specs -g '*.py'`.

## Work Log

- 2026-05-04: Created by splitting the non-atomic dual-object/method-generalization
  card into a concrete Hom-containment owner leaf.
- 2026-05-04: Added definition grounding for formed-module isometry as Hom/Aut
  containment, with matrix criteria demoted to implementation checks under explicit
  presentation hypotheses.
- 2026-05-05: Updated forms/modules mapping docs, the lattice ABC source, and the
  local free-bilinear/lattice hom surfaces so form preservation is Hom containment and
  `is_isometry()` asks for isomorphism inside the already form-preserving Hom object.

## 6-Gate Protocol Review Log

Review date: 2026-05-07.  Reviewer: automated 6-gate audit.  Result: PASS with one
advisory finding (G1 Finding 1).  No gate failures.

### G1 — Source Grounding

Every referenced file, card, and source path was verified on-disk.

| Reference cited in spec | Actual path resolved | Exists |
| --- | --- | --- |
| `plans/todo.md` (deleted; recoverable) | `git show f3c2a1b^:plans/todo.md` | YES — original "Removal of Redundant Predicates" section confirmed |
| `category_specs/forms/subcategories/free_bilinear.py` | `/home/dzack/research/category_specs/forms/subcategories/free_bilinear.py` | YES |
| `category_specs/lattices/homsets.py` | `/home/dzack/research/category_specs/lattices/homsets.py` | YES |
| `category_specs/topological_spaces/homsets.py` | `/home/dzack/research/category_specs/topological_spaces/homsets.py` | YES |
| `category_specs/cat/docs/MAPPING.md` | `/home/dzack/research/category_specs/cat/docs/MAPPING.md` (redirect to `SPEC-MAPPING-CAT.md`) | YES |
| `category_specs/forms/docs/MAPPING.md` | `/home/dzack/research/category_specs/forms/docs/MAPPING.md` (redirect to `SPEC-MAPPING-FORMS.md`) | YES |
| `.agents/skills/lattice-redesign/references/category-abc-spec.md` | `/home/dzack/research/.agents/skills/lattice-redesign/references/category-abc-spec.md` | YES |
| `theory/foundations/bilinear-forms-duals-morphisms.md` | `/home/dzack/research/.agents/memories/theory/foundations/bilinear-forms-duals-morphisms.md` | YES (see G1 Finding 1) |
| `category_specs/modules/docs/MAPPING.md` | `/home/dzack/research/category_specs/modules/docs/MAPPING.md` (redirect to `SPEC-MAPPING-MODULES.md`) | YES |
| Parent: `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` | `/home/dzack/research/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md` | YES |
| Depends-on: `PHASE-HOM-END-AUT-WORK-QUEUE` | `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION/PHASE-HOM-END-AUT-WORK-QUEUE/PHASE-HOM-END-AUT-WORK-QUEUE.md` | YES |

**G1 Finding 1 (advisory):** The spec cites `theory/foundations/bilinear-forms-duals-morphisms.md`
but that path does not exist.  The actual file lives at
`.agents/memories/theory/foundations/bilinear-forms-duals-morphisms.md`.  Other cards
in the repository cite the `.agents/memories/theory/foundations/` path (e.g.,
`TASK-CATEGORY-METHOD-INVENTORY-HOM-FORMS-LATTICES.md` line 47).  The spec's
Definition Grounding section should use the correct path or note the relocation.
The file's "Base Change and Morphisms" section (lines 178-236) was verified and
confirms the clean categorical definition: a morphism `(L1, b1) -> (L2, b2)` lying
over `g: S1 -> S2` is an `S2`-module morphism `phi: S2 ⊗_{S1} L1 -> L2` such that
the base-changed form diagram commutes — equivalently `b2(f(v), f(w)) = g(b1(v,w))`.

**G1 Finding 2 (advisory):** The MAPPING.md files (`cat/docs/MAPPING.md`,
`forms/docs/MAPPING.md`, `modules/docs/MAPPING.md`) are now redirect stubs pointing
to canonical tracked specs under `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/`.
The spec's Work Log claims these docs were "updated" on 2026-05-05.  The actual
updates live in the tracked specs `SPEC-MAPPING-FORMS.md` (lines 122-123, 171-187),
`SPEC-MAPPING-MODULES.md`, and `SPEC-MAPPING-CAT.md`.  This is a documentation-layer
indirection, not a correctness defect; the tracking specs contain the claimed content.

Source-grounding verdict: PASS with one advisory finding (incorrect theory file path).

### G2 — Sage Surface Completeness

The spec inventories exactly three observed surfaces:

1. **`category_specs/forms/subcategories/free_bilinear.py`** — Audited.
   - `MorphismMethods.is_isometry()` at line 218: returns `self.is_isomorphism()`.
   - Docstring at line 219-224 explicitly states: "Preservation of the bilinear form
     is owned by containment in the formed-module Hom object. This compatibility query
     therefore asks only whether the already form-preserving morphism is an isomorphism."
   - The class docstring at lines 32-41 states: "Morphisms in this formed-module
     category are already the R-module maps contained in the formed Hom object,
     hence already preserve b."
   - ACCOUNTED and CORRECT.

2. **`category_specs/lattices/homsets.py`** — Audited.
   - `_LatticeMorphisms.is_isometry()` at line 32: returns `self.is_isomorphism()`.
   - Docstring at lines 33-38: "Form preservation is owned by containment in the
     lattice Hom object, which refines the formed-module Hom object."
   - `_LatticeAutomorphisms.is_isometry()` at line 47: always returns `True`
     (automorphisms are already isometries by definition).
   - `LatticeAutCategory` at line 90: canonical chain `Lattices(R).AutCategory()`,
     with orthogonal group subgroup methods (`special_subgroup`, `stable_subgroup`,
     etc.) at lines 100-139.
   - ACCOUNTED and CORRECT.

3. **`category_specs/topological_spaces/homsets.py`** — Audited as boundary.
   - `_Isometries.is_isometry()` at line 43: always returns `True` for metric-space
     automorphisms in `MetricSpaceAutCategory`.
   - This is a separate surface; the spec correctly warns against conflating
     metric-space isometries with formed-module isometries.
   - Boundary is RESPECTED.  No cross-contamination.

All three inventoried surfaces are accounted for with the correct Hom-containment
semantics.  No orphaned surfaces remain.

Sage-surface verdict: PASS.

### G3 — Constructor Route Justification

The spec's core mathematical claim:

> `phi in Hom(L, M, category=Modules(R).WithForms().Bilinear())`
>
> A morphism preserves form data exactly when it is an element of the hom object
> in the category of modules carrying that form.

Verified against three canonical sources:

**Source 1: `category-abc-spec.md` lines 176-189**
```
Morphism semantics follow the object model. A morphism of bilinear R-modules
is an R-module morphism f: M1 -> M2 such that beta1(v, w) = beta2(f(v), f(w))
for all source elements. An isomorphism with this property is an isometry.
Matrix equations are implementation checks inside the appropriate Hom or
automorphism parent, not public substitutes for morphisms.

Equivalently, form preservation is the containment condition for the
formed-module Hom object. [...] is_isometry() means is_isomorphism();
in the endomorphism case the orthogonal group is the automorphism object
C.AutCategory().Of(M).
```

**Source 2: `bilinear-forms-duals-morphisms.md` lines 178-236**
The "Base Change and Morphisms" section gives the clean categorical definition:
a morphism `(L1, b1) -> (L2, b2)` over `g: S1 -> S2` is an `S2`-module morphism
`phi: S2 ⊗_{S1} L1 -> L2` such that `b2(f(v), f(w)) = g(b1(v,w))`.  For the
special case `g = id_R` (same base ring), this reduces exactly to the spec's
definition: `beta1(v, w) = beta2(f(v), f(w))`.

**Source 3: `plans/todo.md` (recovered via git)**
Original instruction: "REMOVE `is_isometry()` and `is_form_preserving()` from
`ModulesWithForms.Bilinear.MorphismMethods`. REPLACE these with homset containment
logic: a morphism is an isometry if and only if it is contained in the homset of
the category of modules with forms."

The construction route is mathematically valid:
1. Start with a plain module morphism `f in Modules(R).HomCategory().Of(M, N)`.
2. Promote to the formed-module Hom `C.HomCategory().Of(M, N)` exactly when
   `f` satisfies the form-compatibility equation.
3. Within that Hom object, `is_isometry()` asks `is_isomorphism()` — a pure
   categorical condition.
4. The orthogonal group `O(M, b)` is `C.AutCategory().Of(M)` — automorphisms
   in the form-preserving category.

No category-theoretic errors found.  The containment route correctly separates
form-preservation (Hom membership) from invertibility (isomorphism within Hom).

Constructor-route verdict: PASS.

### G4 — Nonmathematical Rejection

The spec explicitly rejects:

1. **Standalone `is_form_preserving()` predicate** (lines 51-53, 97-101, 110-115).
   Reason: form preservation is Hom containment, not a boolean method.
   Rejection grounded in ABC spec lines 183-187 and the original todo.md instruction.
   Replacement owner: `C.HomCategory().Of(M, N)` containment.  SOUND.

2. **Standalone `is_isometry()` as owner of form preservation** (lines 97-101,
   118-121).  Reason: `is_isometry()` is now an isomorphism check inside an already
   form-preserving Hom object.  Replacement owner: `is_isomorphism()` on the
   formed-module morphism, or `True` for Aut elements.  SOUND.

3. **Matrix equations as public definitions** (lines 82-83, 131-133).  Reason:
   matrix criteria require explicit presentations and generators; they are
   implementation checks, not the mathematical definition.  SOUND.

4. **Conflation with metric-space isometry** (lines 42-44, 92-93, 139-141).
   Reason: `topological_spaces/homsets.py` has a same-name but different
   mathematical surface.  Separation is explicit and verified at source.
   SOUND.

All rejections have explicit rationale and replacement owners.  No rejection
weakens mathematical coverage.

Nonmathematical-rejection verdict: PASS.

### G5 — Ambiguity Routing

The spec is self-contained and internally consistent.  Identified boundaries:

1. **Metric-space vs. formed-module isometry boundary** — explicitly drawn
   (lines 139-141), verified in source.  No unresolved ambiguity.  PASS.

2. **Matrix criteria vs. categorical definition** — matrix equations are
   demoted to implementation checks under presentation hypotheses (lines 131-133).
   This is a precision improvement, not an ambiguity.  PASS.

3. **Dependency on `PHASE-HOM-END-AUT-WORK-QUEUE`** — the phase exists and
   is active (status: `needs-review`).  The dependency is satisfiable.  PASS.

4. **Compatibility alias status** — `is_isometry()` is documented as a
   compatibility query for isomorphism inside the Hom object (free_bilinear.py
   lines 218-225, lattices/homsets.py lines 32-39).  No orphaned meaning.  PASS.

No ambiguities are left unresolved or unaddressed.

Ambiguity-routing verdict: PASS.

### G6 — Obligation Preservation

Audit of mathematical obligations:

1. **Form preservation:** Moved from a standalone boolean predicate to Hom
   containment.  The new owner (`C.HomCategory().Of(M, N)`) is categorically
   stronger: containment implies the form-compatibility equation by definition
   of the formed-module Hom object.  No weakening.  PASS.

2. **Isometry:** Moved from a standalone predicate to `is_isomorphism()` inside
   the formed-module Hom.  This preserves the meaning (an isometry is a
   form-preserving isomorphism) while correctly routing ownership.  PASS.

3. **Orthogonal group:** Preserved as `C.AutCategory().Of(M)`.  The spec
   explicitly states (line 139): "Do not weaken lattice orthogonal-group
   semantics; preserve the categorical meaning `O(M,b) = Aut(M,b)` in the
   formed-module category."  Confirmed in `lattices/homsets.py` at lines 90-139.
   PASS.

4. **Lattice Hom/Aut surfaces:** `LatticeHomCategory` at line 51 refines
   `HomCategoryOf`, and `LatticeAutCategory` at line 90 refines
   `GenericAutCategory`.  The canonical chains `Lattices(R).HomCategory()` and
   `Lattices(R).AutCategory()` are verified (lines 54, 75, 93).  PASS.

5. **Metric-space isometry boundary:** No weakening of formed-module obligations
   to accommodate metric-space terminology.  The two surfaces remain separate with
   explicit boundary documentation.  PASS.

No mathematical obligation is weakened, deleted without replacement, or narrowed
to implementation-only surfaces.

Obligation-preservation verdict: PASS.

### Summary

| Gate | Verdict | Evidence |
| --- | --- | --- |
| G1 Source grounding | PASS | 11/11 referenced artifacts verified on disk; 1 advisory (theory file path) |
| G2 Sage surface completeness | PASS | 3/3 inventoried surfaces accounted and verified correct |
| G3 Constructor route justification | PASS | Route verified against ABC spec, theory file, and original todo.md |
| G4 Nonmathematical rejection | PASS | 4 explicit rejections, all with rationale and replacement owners |
| G5 Ambiguity routing | PASS | 4 boundaries examined; no unresolved ambiguities |
| G6 Obligation preservation | PASS | 5 surface audits; no weakening without replacement |

Overall: SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER.md is mathematically
sound, source-grounded, and correctly routes form-preserving isometry predicates
through formed-module Hom containment.  The single advisory (G1 Finding 1: incorrect
path for `bilinear-forms-duals-morphisms.md`) should be corrected in the Definition
Grounding section to reference `.agents/memories/theory/foundations/bilinear-forms-duals-morphisms.md`.
