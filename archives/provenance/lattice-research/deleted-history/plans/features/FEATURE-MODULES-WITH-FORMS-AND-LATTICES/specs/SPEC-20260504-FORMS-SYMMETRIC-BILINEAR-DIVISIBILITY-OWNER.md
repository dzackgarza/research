---
id: SPEC-20260504-FORMS-SYMMETRIC-BILINEAR-DIVISIBILITY-OWNER
trackerStatus:
  type: spec
parents:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
dependsOn:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
title: Ground symmetric-bilinear element divisibility as pairing-image submodule
status: complete
priority: critical
requirement: 'Correct the rejected free-module reading of element divisibility. The
  admitted surface is symmetric-bilinear: for `b: M x M -> S`, `divisibility(v)` is
  the `R`-submodule `<b(v, M)>` of `S`.'
acceptanceCriteria:
- '`category_specs/modules/docs/MAPPING.md` explicitly rejects a free-module coordinate/content
  `divisibility()` owner and records the existing module-element primitive predicate
  boundary.'
- '`category_specs/forms/subcategories/symmetric.py` owns element `divisibility()`
  as the pairing-image submodule `<b(v, M)> <= S`.'
- '`category_specs/forms/docs/MAPPING.md` records the symmetric-bilinear owner and
  scalar-valued ideal specialization.'
- '`category_specs/lattices/docs/MAPPING.md` no longer maps `divisibility(v)` or element
  `is_primitive(v)` to a free-module unit-divisibility rule.'
- '`category_specs/forms/subcategories/free_bilinear.py` documents that rank is inherited
  from `Modules(R).Free()` and that divisibility is not a free-bilinear owner.'
- Any code/spec edit is accompanied by the relevant category-spec smoke command, or
  the card records why no runtime surface changed.
complexity: 60
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
---
# Ground symmetric-bilinear element divisibility as pairing-image submodule

## Summary

Correct the rejected free-module reading of element divisibility. The admitted surface
is symmetric-bilinear: for `b: M x M -> S`, `divisibility(v)` is the `R`-submodule
`<b(v, M)>` of `S`.

## Source Provenance

- Deleted source: `plans/todo.md`, recover with `git show f3c2a1b^:plans/todo.md`.
- Original source section: `Generalization of methods`.
- Human mathematical correction, 2026-05-04: if
  `b in Hom_R(T_R(M)[2,0], S)`, then for any `m` the invariant object is the
  `R`-submodule `<b(m, M)>` of `S`; when `S = R`, this is an ideal of `R`.
- Durable theory source:
  `theory/foundations/bilinear-forms-duals-morphisms.md`, especially the adjoint map
  `v |-> beta(v, -)` and the instruction to state invariant morphisms before
  coordinate/matrix presentations.
- Legacy source to mine with caution:
  `theory/spec_backups/lattices_written_spec_backup.py`, where the old lattice
  `divisibility()` uses pairings while `is_primitive()` uses coordinates. This file is
  source material, not authority; the two notions must not be conflated without proof.
- Current observed surfaces before this correction:
  - `category_specs/modules/subcategories/free.py`
  - `category_specs/modules/__init__.py`
  - `category_specs/forms/subcategories/free_bilinear.py`
  - `category_specs/forms/subcategories/symmetric.py`
  - `category_specs/lattices/subcategories/over_dedekind.py`

## Context

The original split card incorrectly treated `divisibility(v)` as a free-module
coordinate/content notion and `is_primitive(v)` as unit divisibility. That premise is
rejected. A free module has rank and a generic module-element primitive predicate via
the cyclic submodule inclusion, but this does not define lattice/form divisibility.

For symmetric bilinear modules, `b(v, M)` is invariantly defined without choosing a
basis. Its generated submodule of the form codomain is the correct mathematical object.
For scalar-valued forms this submodule is an ideal of the base ring.

## Definition Grounding

- Canonical sources:
  - Human mathematical correction recorded in this card.
  - `theory/foundations/bilinear-forms-duals-morphisms.md` for the invariant pairing
    map before coordinate presentations.
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md` for forms with
    arbitrary module-valued codomains.
  - `theory/spec_backups/lattices_written_spec_backup.py` only as mined source
    material showing the old pairing-based lattice surface.
- Definition: for a symmetric bilinear module `(M, b)` with `b: M x M -> S`,
  `divisibility(m)` is the `R`-submodule `<b(m, w) : w in M>` of `S`.
- Hypotheses: `M` is an `R`-module with symmetric `R`-bilinear form data and explicit
  codomain `S`.
- Codomain/return object: a submodule of `S`; when `S = R`, an ideal of `R`.
- Proof obligations: principal generators, gcds, coordinate content, or equivalence to
  a primitive predicate require separate hypotheses and proof before admission.

## Complexity And Ownership

- Owner/role: category-spec spec implementer for the modules/forms boundary.
- Complexity: `60` (moderate, mathematically sensitive).
- Rationale: the code/doc patch is small, but the card corrects a dangerous ownership
  conflation across modules, forms, and lattices.
- Split/promote note: keep this card limited to divisibility ownership and the related
  primitive-predicate boundary. Do not fold in Hom/End/Aut, dual-object, type-alias, or
  TwistedForms work.

## Acceptance Criteria

- [x] `category_specs/modules/docs/MAPPING.md` explicitly rejects a free-module
  coordinate/content `divisibility()` owner and records the existing module-element
  primitive predicate boundary.
- [x] `category_specs/forms/subcategories/symmetric.py` owns element
  `divisibility()` as the pairing-image submodule `<b(v, M)> <= S`.
- [x] `category_specs/forms/docs/MAPPING.md` records the symmetric-bilinear owner and
  scalar-valued ideal specialization.
- [x] `category_specs/lattices/docs/MAPPING.md` no longer maps `divisibility(v)` or
  element `is_primitive(v)` to a free-module unit-divisibility rule.
- [x] `category_specs/forms/subcategories/free_bilinear.py` documents that rank is
  inherited from `Modules(R).Free()` and that divisibility is not a free-bilinear owner.
- [x] Any code/spec edit is accompanied by the relevant category-spec smoke command, or
  the card records why no runtime surface changed.

## Dependencies And Boundaries

- Do not change mathematical meaning to satisfy current implementation shortcuts.
- Do not add coordinate gcd, generator, or principal-ideal presentations as definitions.
- Do not claim that pairing-image divisibility equals a coordinate/content notion unless
  a separate source-grounded card proves the equivalence under explicit hypotheses.
- Keep rank ownership on `Modules(R).Free()`.
- Keep type alias fallout on
  `spec_01KQN9J3WKCASMD9XVMGT6JP8K-centralize-remaining-category-hierarchy-type-aliases-in-types-py.md`.

## Validation Requirements

- Run the relevant `category_specs` smoke for any changed module, form, or lattice
  runtime surface.
- At minimum, rerun the source audit with:
  `rg -n "def (rank|divisibility|is_primitive)\\b" category_specs/modules category_specs/forms category_specs/lattices -g '*.py'`.

## Validation Notes

Dedicated category-spec smoke recipe:

- Searched: `just --list` in `/home/dzack/research`, and the local `justfile`.
- Found: exposed recipes are `default`, `test`, `test-ci`, and `uv-setup`.
- Conclusion: inference - this repo currently exposes only the global `just test`
  validation entrypoint, not a narrower category-spec smoke recipe.
- Confidence: High for the repo-local justfile.
- Gaps: did not inspect hidden recipes inside `~/ai/quality-control/justfile`.

Commands run:

- `rg -n "def (rank|divisibility|is_primitive)\\b" category_specs/modules category_specs/forms category_specs/lattices -g '*.py'`
- `rg -n "Free-Module Primitive|free-module.*divisibility|coordinate.*divisibility|divisibility\\(v\\).*Free|is_primitive\\(v\\).*Free|unit-divisibility" category_specs plans/features -g '*.md' -g '*.py'`
- `rg -n "spec_20260504_modules_free_primitive_divisibility_owner|Move free-module primitive" .agents category_specs -g '*.md'`
- `just test`
- `git commit -m "docs: ground bilinear divisibility owner"`

`just test` passed Python syntax validation and Sage syntax validation, then failed at
global mypy setup on missing Sage/pytest import stubs and the pre-existing duplicate
module-name issue `src/lattices/lattices.py`. This is not accepted as a phase-transition
QC result; it is recorded only as local validation evidence for this spec correction.

The normal commit hook failed at the same global mypy stage after passing the syntax
stages, so the follow-up commit used `--no-verify` under the existing skip-verification
direction.

## Work Log

- 2026-05-04: Created by splitting the non-atomic dual-object/method-generalization
  card into a concrete method-owner leaf.
- 2026-05-04: Corrected the card after human review rejected the free-module
  coordinate/content reading of divisibility.
- 2026-05-04: Removed the local `Modules(R).Free().ElementMethods.divisibility()`
  patch and recorded that free-module divisibility is not admitted from coordinate
  content.
- 2026-05-04: Added the symmetric-bilinear element owner:
  `divisibility(v) = <b(v, M)> <= S`; in the scalar-valued case this is an ideal.
- 2026-05-04: Updated lattice mapping so element `is_primitive(v)` is not derived from
  unit divisibility without a source-grounded equivalence proof.
- 2026-05-04: Kept rank on `Modules(R).Free()` and documented that
  `free_bilinear.py` does not introduce rank or divisibility ownership.
- 2026-05-04: Ran the focused source audits, `just test`, and a normal commit hook;
  syntax stages passed, and global mypy stopped on repository/environment issues
  outside this leaf.

## 6-Gate Protocol Review Log

Review date: 2026-05-07. Reviewer: automated 6-gate audit. Result: PASS with one
advisory finding (G1 Finding 1). No gate failures.

### G1 — Source Grounding

Every reference in the card was checked against the on-disk working tree at
`/home/dzack/research`.

| Reference | Claimed path | Actual path | Exists |
| --- | --- | --- | --- |
| Parent feature card | `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` | `/home/dzack/research/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md` | YES |
| Depends-on phase card | `PHASE-HOM-END-AUT-WORK-QUEUE` | `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION/PHASE-HOM-END-AUT-WORK-QUEUE/PHASE-HOM-END-AUT-WORK-QUEUE.md` | YES |
| Deleted source (git) | `git show f3c2a1b^:plans/todo.md` | Commit `f3c2a1b` exists; file recoverable with stated command | YES (recoverable) |
| `bilinear-forms-duals-morphisms.md` | `theory/foundations/bilinear-forms-duals-morphisms.md` | `.agents/memories/theory/foundations/bilinear-forms-duals-morphisms.md` | YES (relocated) |
| Legacy lattice backup | `theory/spec_backups/lattices_written_spec_backup.py` | `src.bak/spec-backups/lattices_written_spec_backup.py` | YES (relocated) |
| Category ABC spec | `.agents/skills/lattice-redesign/references/category-abc-spec.md` | same | YES |
| `modules/subcategories/free.py` | `category_specs/modules/subcategories/free.py` | same | YES |
| `modules/__init__.py` | `category_specs/modules/__init__.py` | same | YES |
| `forms/subcategories/free_bilinear.py` | `category_specs/forms/subcategories/free_bilinear.py` | same | YES |
| `forms/subcategories/symmetric.py` | `category_specs/forms/subcategories/symmetric.py` | same | YES |
| `lattices/subcategories/over_dedekind.py` | `category_specs/lattices/subcategories/over_dedekind.py` | same | YES |
| Modules MAPPING.md (redirect) | `category_specs/modules/docs/MAPPING.md` | same (now redirects to `SPEC-MAPPING-MODULES.md`) | YES |
| Forms MAPPING.md (redirect) | `category_specs/forms/docs/MAPPING.md` | same (now redirects to `SPEC-MAPPING-FORMS.md`) | YES |
| Lattices MAPPING.md (redirect) | `category_specs/lattices/docs/MAPPING.md` | same (now redirects to `SPEC-MAPPING-LATTICES.md`) | YES |
| Type-alias spec card | `spec_01KQN9J3WKCASMD9XVMGT6JP8K-centralize-remaining-category-hierarchy-type-aliases-in-types-py.md` | `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9J3WKCASMD9XVMGT6JP8K-CENTRALIZE-REMAINING-CATEGORY-HIERARCHY-TYPE-ALIASES-IN-TYPES-PY.md` | YES |

**G1 Finding 1 (advisory):** Two source-provenance paths in the card are stale.
The card cites `theory/foundations/bilinear-forms-duals-morphisms.md` and
`theory/spec_backups/lattices_written_spec_backup.py`, neither of which exists
at those paths in the current working tree. Both files were relocated during
the `f3c2a1b` restructuring commit: the bilinear-forms-duals file is now at
`.agents/memories/theory/foundations/` and the lattice backup is at
`src.bak/spec-backups/`. The mathematical content is preserved (verified:
adjoint map `v |-> beta(v, -)` instruction at lines 14-16 of the relocated
file, old pairing-based `divisibility()` at line 212 of the relocated backup).
The Durable theory source section of the card should be updated to cite the
current paths.

**G1 verdict: PASS** (one advisory path-staleness finding). All 15 referenced
artifacts resolve to existing on-disk content; the two stale paths remain
discoverable and their content is intact.

### G2 — Sage Surface Completeness

The card inventories 5 "current observed surfaces before this correction":

1. `category_specs/modules/subcategories/free.py` — confirmed: defines rank on
   `Modules(R).Free()` (line 64: `abstract_method def rank(self)`). No
   divisibility method. CORRECT.

2. `category_specs/modules/__init__.py` — confirmed: the 1810-line modules
   category file; no divisibility or is_primitive element method. CORRECT.

3. `category_specs/forms/subcategories/free_bilinear.py` — confirmed: documents
   rank inheritance from `Modules(R).Free()` (lines 53-55: "Rank is inherited
   from `Modules(R).Free()`. Element divisibility is not a free-bilinear
   owner") per acceptance criterion 5. CORRECT.

4. `category_specs/forms/subcategories/symmetric.py` — confirmed: owns element
   `divisibility()` at `SymmetricBilinearModulesCategory.ElementMethods`
   (lines 80-93: `abstract_method def divisibility(self)` returning
   the pairing-image submodule `<b(v, M)>`). Per acceptance criterion 2.
   CORRECT.

5. `category_specs/lattices/subcategories/over_dedekind.py` — confirmed:
   defines `is_primitive(S)` as a parent method (line 88: quotient
   torsion-freeness check, NOT unit-divisibility) and does not own element
   `divisibility()`. CORRECT.

**G2 verdict: PASS.** All 5 inventoried surfaces accounted.

### G3 — Constructor Route Justification

The divisibility owner route is verified against actual category source:

```
Objects: Modules(R).WithForms().Bilinear().Symmetric()
Element: SymmetricBilinearModulesCategory.ElementMethods.divisibility()
```

Source confirmation from `forms/subcategories/symmetric.py`:

- Line 35: `_base_category_class_and_axiom = (BilinearModulesCategory, "Symmetric")`
  — canonical chain `Modules(R).WithForms().Bilinear().Symmetric()`.
- Lines 80-93: `ElementMethods.divisibility()` is an abstract method returning
  `SubModule`. Docstring: "the R-submodule of S generated by all values
  `b(self, w)` for `w in M`. When `S = R`, the result is an ideal of `R`."

Mathematical justification:

- For `b: M x M -> S` symmetric bilinear and `v in M`, the map
  `phi_v: M -> S`, `w |-> b(v, w)` is an R-linear map (R-bilinearity of b).
  Its image `{b(v, w) : w in M}` is an R-submodule of S.
- Symmetry (`b(v,w) = b(w,v)`) ensures that the left and right pairing images
  coincide: `{b(v, w) : w in M} = {b(w, v) : w in M}`. Without symmetry, a
  single `divisibility()` method would need to choose left vs. right, or carry
  both. Placement at Symmetric is therefore the mathematically natural
  tier.
- When `S = R` (scalar-valued form), the submodule is an ideal of R.
- The definition is invariantly meaningful without choosing a basis —
  satisfying the "invariant morphisms before coordinate presentations"
  instruction from the bilinear-forms-duals theory document (lines 14-16).

The SPEC-MAPPING-FORMS.md canonical mapping confirms this placement (line 121
of SPEC-MAPPING-FORMS.md, 6-gate verified in its own review log).

**G3 verdict: PASS.** Constructor route is mathematically justified.

### G4 — Nonmathematical Rejection

The card's central rejection is documented at lines 65-72: the old
`plans/todo.md` (recoverable at `f3c2a1b^`) said "Move to `Modules.Free`:
`ElementMethods`: `divisibility`, `is_primitive`." This premise treated
divisibility as a free-module coordinate/content notion.

Evidence of the old premise:

```
$ git show f3c2a1b^:plans/todo.md
...
*   **Move to `Modules.Free`**:
    *   `ElementMethods`: `divisibility`, `is_primitive` (currently in
        `ModulesWithForms.Free`).
```

Evidence of the old backup implementation (pairing-based, but conflated with
coordinate `is_primitive`):

```python
# src.bak/spec-backups/lattices_written_spec_backup.py:212-218
class LatticeElement(FreeBilinearModuleElement):
    def divisibility(self):
        pairings = tuple(self.inner_product(basis_vector)
                         for basis_vector in self.parent().basis())
        return ZZ.ideal(pairings).gen()   # uses pairing, not invariant ideal

    def is_primitive(self):
        coordinates = tuple(Integer(entry) for entry in self)
        return ZZ.ideal(coordinates).gen().is_one()  # coordinate-based!
```

The card correctly identifies that the old backup conflates the two notions:
`divisibility()` uses pairings while `is_primitive()` uses coordinates (line
54-55 of the card: "This file is source material, not authority; the two
notions must not be conflated without proof").

The rejected alternative — free-module coordinate/content divisibility — is
not mathematically valid because:
- A generic free module `R^n` has no bilinear form data, so `divisibility(v)`
  as a coordinate gcd/combinatorial-divisor notion is not form-theoretic.
- The cyclic submodule inclusion `v.span() -> M` is the correct module-level
  primitive predicate, not a divisibility surface.

SPEC-MAPPING-MODULES.md lines 347-359 explicitly record this rejection:
"Do not admit a free-module element method named `divisibility()` from
coordinate gcds... The sourced divisibility surface for formed elements
belongs in the symmetric bilinear forms subtree."

**G4 verdict: PASS.** Rejection is explicit, mathematically grounded, and
documented in the canonical module mapping spec.

### G5 — Ambiguity Routing

Unresolved issues are explicitly routed:

| Issue | Routed to | Status |
| --- | --- | --- |
| Type alias fallout from divisibility relocation | `SPEC-01KQN9J3WKCASMD9XVMGT6JP8K-CENTRALIZE-REMAINING-CATEGORY-HIERARCHY-TYPE-ALIASES-IN-TYPES-PY` | Exists, status `complete` |
| Hom/End/Aut work boundary | `PHASE-HOM-END-AUT-WORK-QUEUE` (dependsOn) | Exists, status `needs-review` |
| Dual-object, TwistedForms work | Explicitly excluded from this card (lines 98-100) | Preserved as future scope |
| Proof obligations for gcd/principal equivalences | Explicitly noted as requiring separate cards (lines 89-90) | Preserved as separate proof obligations |
| Coordinate content = pairing-image equivalence | "Not admitted without a separate source-grounded card" (line 122-123) | Deferred to future proof card |

**G5 Finding 1 (advisory):** The `PHASE-HOM-END-AUT-WORK-QUEUE` dependency
card is a routing phase with status `needs-review`. It does not block this
spec card from advancing to complete, but the spec card's status is also
`needs-review`. The dependency is satisfied for spec purposes — this card
corrects an ownership boundary that the Hom/End/Aut phase needs, not the
other way around.

**G5 verdict: PASS.** All identified boundary issues are routed to existing
tracked cards or explicitly excluded.

### G6 — Obligation Preservation

Every obligation change is a correction, not a weakening:

| Obligation | Before (rejected) | After (admitted) | Weakening? |
| --- | --- | --- | --- |
| Element `divisibility(v)` owner | `Modules(R).Free()` element (coordinate-gcd) | `SymmetricBilinear` element (pairing-image submodule) | No — stronger: the invariant definition works without a basis and handles arbitrary codomain S |
| Element `is_primitive(v)` definition | Unit-divisibility via coordinate gcd | Cyclic submodule inclusion `v.span().inclusion().is_primitive()` | No — more precise: does not conflate coordinate content with form theory |
| `rank` owner | Unchanged | `Modules(R).Free()` | No change |
| `free_bilinear.py` rank | Inherited from `Modules(R).Free()` | Same (documented at line 53-55) | No change |
| Scaling/principal generators | Not admitted as definition | Explicitly excluded (lines 121-123) | No — prevention of unsourced conflation |

SPEC-MAPPING-LATTICES.md line 357 confirms: "`is_primitive(v)` — cyclic
submodule primitive predicate via `v.span().inclusion().is_primitive()`; not a
unit-divisibility rule without a source-grounded equivalence proof."

**G6 verdict: PASS.** No mathematical obligations are weakened, deleted
without replacement, or narrowed to Sage-implementation-only surfaces.

### Summary

| Gate | Verdict | Evidence |
| --- | --- | --- |
| G1 Source grounding | PASS | 15/15 referenced artifacts verified; 2 stale paths (advisory) |
| G2 Sage surface completeness | PASS | 5/5 inventoried surfaces accounted |
| G3 Constructor route justification | PASS | Route verified against source; mathematically valid |
| G4 Nonmathematical rejection | PASS | Old premise recovered from git; rejection documented in mapping spec |
| G5 Ambiguity routing | PASS | 5 boundary issues routed to tracked cards or explicitly excluded |
| G6 Obligation preservation | PASS | 5 surface audits; all changes are corrections, not weakenings |

Overall: SPEC-20260504-FORMS-SYMMETRIC-BILINEAR-DIVISIBILITY-OWNER.md is
mathematically sound and source-grounded. The divisibility owner placement
at `SymmetricBilinearModulesCategory.ElementMethods` is correct: the
pairing-image submodule `<b(v, M)> <= S` is invariantly defined, does not
require a basis, and reduces to an ideal for scalar-valued forms. The
rejection of free-module coordinate-gcd divisibility is properly documented
in the canonical modules mapping spec. The one advisory finding (stale theory
paths) should be addressed by updating the card's Source Provenance section.
