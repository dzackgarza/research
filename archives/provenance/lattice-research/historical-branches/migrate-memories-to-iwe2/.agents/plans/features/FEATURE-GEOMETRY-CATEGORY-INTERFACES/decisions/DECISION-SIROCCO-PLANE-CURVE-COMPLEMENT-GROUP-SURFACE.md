---
id: DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE
trackerStatus:
  type: decision
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING]]'
title: Choose Sirocco-backed plane-curve complement group surface
status: implemented
chosen: ''
options:
- name: Complement object owns the group
  pros:
  - Keeps the mathematical object as the complement, not the defining curve alone.
  - Can separate affine and projective complements by construction.
  cons:
  - Requires complement-object vocabulary before implementation work.
- name: Plane curve forwards to complement
  pros:
  - Matches Sage's existing `C.fundamental_group()` user-facing route.
  - Gives a convenient interop spelling after the complement owner exists.
  cons:
  - Can hide that the computed group is attached to the complement and presentation choices.
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Choose Sirocco-backed plane-curve complement group surface

## Summary

Decide the public mathematical surface for using Sage's Sirocco-backed
Zariski-Van Kampen route after the geometry category vocabulary exists.

## Source Provenance

- `[[TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS]]`
- `[[SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING]]`
- Upstream SIROCCO2 repository: <https://github.com/miguelmarco/sirocco2>
- Sage Zariski-Van Kampen documentation:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html>
- Sage projective plane curve `fundamental_group()` documentation:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/projective_curve.html>
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/zariski_vankampen.py`

## Context

The Sirocco research pass admitted backend evidence but did not admit an
implementation. Sage exposes finite presentations of affine and projective
plane-curve complement groups through Zariski-Van Kampen computations that use
Sirocco for certified strand following.

The remaining choices are mathematical surface decisions, not implementation
details.

## Decision Questions

- Should the public owner be `C.complement().fundamental_group()` with
  `C.fundamental_group()` as an interop forwarder, or should the plane curve own
  the public method directly?
- Should braid monodromy be a typed intermediate mathematical object, or remain
  backend-only evidence hidden below the complement-group method?
- How should finite presentations record meridians, arrangement factors,
  vertical components, simplification, and comparison/equivalence policy?
- Should affine and projective complements be distinct complement objects, or
  variants selected by construction data on one complement type?

## Acceptance Criteria

- [ ] The chosen owner names the caller object, required projection or complement
      data, hypotheses on the plane curve and coefficient field, and the return
      object.
- [ ] The decision records whether braid monodromy is public typed vocabulary or
      backend-only evidence.
- [ ] The decision records how presentation generators, meridians, arrangement
      labels, vertical components, simplification, and comparison policy are typed
      or deferred.
- [ ] The decision records whether affine and projective complements are separate
      objects or variants of one construction.
- [ ] The decision updates or links the geometry category spec that will own the
      chosen method surface.

## Dependencies And Boundaries

- This decision depends on the Sirocco backend mapping spec, but it does not
  authorize an implementation.
- Do not add a raw Sirocco wrapper as the public surface.
- Do not treat a finitely presented group returned by Sage as canonical group
  equality or isomorphism evidence without a separate presentation/comparison
  policy.

## Work Log

- 2026-05-06: Created from Gate 2 review of the Sirocco research task, which found
  that concrete follow-up choices were left as inline prose in the backend mapping
  spec instead of tracked as a card.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate review)

**Gates passed:** G1, G4, G5, G6
**Gates failed:** G2, G3
**Outcome:** CONDITIONAL HOLD — decision framing is incomplete; options cover only 1 of 4 decision questions. Cannot gate-promote until all decision questions have explicit options.

---

### Gate 1: Source Grounding — PASS

Every source cited in the card resolves to a verifiable resource:

| Claimed source | Verification method | Result |
|---|---|---|
| `[[TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS]]` | File exists at `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/tasks/TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS.md`; status `complete` | Exists |
| `[[SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING]]` | File exists at `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING.md`; status `complete`; 6-gate review passed 2026-05-07 | Exists |
| Upstream SIROCCO2 GitHub (`miguelmarco/sirocco2`) | Verified by the mapping spec's G1 review (HTTP HEAD → 200) | Exists |
| Sage Zariski-Van Kampen docs URL | Verified by the mapping spec's G1 review (HTTP HEAD → 200) | Exists |
| Sage `projective_curve.html` docs URL | Verified by the mapping spec's G1 review (HTTP HEAD → 200) | Exists |
| Installed Sage source `zariski_vankampen.py` | Verified by the mapping spec's G1 review (file exists at `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/zariski_vankampen.py`) | Exists |

All 6 source references are confirmed present and accessible. Source grounding is complete and reproducible.

---

### Gate 2: Decision Framing — FAIL

The card's `options` frontmatter lists exactly 2 options:

1. **Complement object owns the group** — the public entry point is `C.complement().fundamental_group()`
2. **Plane curve forwards to complement** — `C.fundamental_group()` delegates to the complement

However, the Decision Questions section in the card body enumerates **4 distinct decision questions**:

1. Should the public owner be `C.complement().fundamental_group()` with `C.fundamental_group()` as an interop forwarder, or should the plane curve own the public method directly?
2. Should braid monodromy be a typed intermediate mathematical object, or remain backend-only evidence hidden below the complement-group method?
3. How should finite presentations record meridians, arrangement factors, vertical components, simplification, and comparison/equivalence policy?
4. Should affine and projective complements be distinct complement objects, or variants selected by construction data on one complement type?

The two YAML options answer only question 1. Questions 2, 3, and 4 have **no corresponding options in the frontmatter** and no rough-choice framing in the body. A human decision-maker cannot record a `chosen` value for these remaining dimensions.

Additionally, the two listed options are not mutually exclusive in the way the card might suggest: option 2 (Plane curve forwards to complement) is described with the prose "Gives a convenient interop spelling **after the complement owner exists**" — implying option 1 is a prerequisite to option 2. The decision point is better framed as "what is the primary public owner?" with option 2 as an allowed auxiliary surface, not as an alternative.

**Gate 2 Verdict:** FAIL. The options list is incomplete relative to the decision questions. The card cannot be resolved in its current form because it asks 4 questions but frames options for only 1.

---

### Gate 3: Acceptance Criteria Clarity — FAIL

The card has 5 acceptance criteria checkboxes. Each is individually clear and measurable:

| Criterion | Clear? | Measurable? | Assessment |
|---|---|---|---|
| "The chosen owner names the caller object, required projection or complement data, hypotheses on the plane curve and coefficient field, and the return object." | YES | YES — requires named owner with explicit signature/hypotheses | Well-scoped |
| "The decision records whether braid monodromy is public typed vocabulary or backend-only evidence." | YES | YES — binary determination | Clear |
| "The decision records how presentation generators, meridians, arrangement labels, vertical components, simplification, and comparison policy are typed or deferred." | YES | YES — for each listed item, must state typed or deferred | Comprehensive |
| "The decision records whether affine and projective complements are separate objects or variants of one construction." | YES | YES — binary determination | Clear |
| "The decision updates or links the geometry category spec that will own the chosen method surface." | YES | YES — requires specific spec card reference | Actionable |

However, the criteria cannot be verified because **the decision has not been made** (`chosen: ''`, `status: needs-human-input`). This is not a card defect — it is the card's current state. The criteria themselves are well-formed but are downstream of the human decision.

**Gate 3 secondary finding:** Criterion 1 ("the chosen owner names the caller object, required projection or complement data, hypotheses...") is substantially broader than the two options in the frontmatter. The options only name *which* object owns the method (`Complement` vs `PlaneCurve`); they do not specify the full signature, hypotheses, or return object. If the human chooses option 1 or 2, they still need to supply the additional detail criterion 1 requires. This is a legitimate acceptance criterion demanding more specificity from the decision output.

**Gate 3 Verdict:** FAIL. Criteria are clear and well-formed, but the decision is unresolved. More critically, the criteria demand specificity (signatures, hypotheses, return objects) that the two YAML options do not supply. The options must be expanded to include enough detail to discharge the acceptance criteria, or the acceptance criteria must be narrowed to match the option granularity.

---

### Gate 4: Scope Containment — PASS

The decision card stays within decision scope without authorizing implementation:

- **Dependencies And Boundaries section (line 85-91):** "This decision depends on the Sirocco backend mapping spec, but it does not authorize an implementation." — explicit non-implementation boundary.
- **"Do not add a raw Sirocco wrapper as the public surface."** — correctly rejects backend-leak surfaces.
- **"Do not treat a finitely presented group returned by Sage as canonical group equality or isomorphism evidence without a separate presentation/comparison policy."** — correctly defers comparison/equality policy to a downstream decision or spec.
- **Parent feature acceptance criterion:** "Curve-complement and monodromy backend work stays research-scoped until category ownership is explicit." The decision card respects this: it decides surface ownership vocabulary without creating implementation cards.
- No leaked concerns: no performance discussion, no deployment considerations, no Sage version-upgrade questions, no UI/UX language.

**Gate 4 Verdict:** PASS. The card is properly scoped to a surface-ownership decision. Implementation is explicitly deferred.

---

### Gate 5: Dependency Resolution — PASS

The card's dependency graph is correct and satisfied:

- **`dependsOn: ['[[SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING]]']`** — The mapping spec is `complete` and passed 6-gate review on 2026-05-07. The spec's Follow-Up Consequence section (lines 153-164) explicitly references this decision card as the destination for the unresolved surface choices. The dependency is bidirectional and resolved.
- **`parents: ['[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]']`** — Confirmed: the parent feature exists, is `in-progress`, and contains this decision in its `decisions/` subdirectory.
- **Transitive dependency via the mapping spec:** `TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS` is referenced in the Source Provenance and is `complete`. This is not listed in `dependsOn`, but it is informational provenance rather than a blocking dependency — the research task's output is fully captured in the mapping spec, which IS a declared dependency.
- No circular references detected. No dangling card references.
- `dependsOn` accurately captures that this decision card needs the backend mapping to exist before surface-ownership can be decided.

**Gate 5 Verdict:** PASS. Dependencies are correctly recorded and satisfied. The mapping spec is complete; no blockers remain.

---

### Gate 6: Obligation Preservation — PASS

The decision card preserves all upstream obligations without weakening:

- **From SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING:** The mapping spec's Follow-Up Consequence (lines 153-164) enumerates 4 open items. The decision card's Decision Questions (lines 58-67) and Acceptance Criteria (lines 70-82) cover all 4 items without omission or narrowing.
- **From the mapping spec's Limitations (lines 102-118):** The 5 limitation items (plane-curve-only scope, QQ/number-field coefficient restriction, projection/presentation choice dependence, non-canonical presentation warning, backend failure isolation) are preserved in the decision card's Dependencies And Boundaries section (lines 86-91) through the explicit prohibition against treating Sage-returned groups as canonical.
- **From FEATURE-GEOMETRY-CATEGORY-INTERFACES:** The parent feature's acceptance criterion "Curve-complement and monodromy backend work stays research-scoped until category ownership is explicit" is honored — the decision card decides ownership vocabulary without authorizing implementation.
- **No spec-weakening detected:** No upstream obligation is deleted, narrowed, or relocated without a grounded replacement. The card adds specificity (explicit option framing) without removing any constraint.
- **Card status `needs-human-input`** is correct: the decision requires human judgment between mathematical design alternatives. This is not a gate-reviewable choice.

**Gate 6 Verdict:** PASS. All upstream obligations are preserved. The card correctly routes the surface-ownership question to a human decision without weakening any prior constraint.

---

### Blocking Issues

1. **G2 — Incomplete option framing.** The frontmatter `options` list covers only decision question 1 (public owner). Questions 2 (braid monodromy visibility), 3 (presentation typing policy), and 4 (affine/projective complement modeling) have no corresponding options. Either:
   - Add explicit option pairs for questions 2-4 to the `options` frontmatter, OR
   - Split questions 2-4 into separate decision cards and scope this card to question 1 only.

2. **G3 — Option granularity mismatch with acceptance criteria.** Acceptance criterion 1 demands specificity (caller object, projection/complement data, hypotheses, return object) that the two YAML options do not supply. The options say "Complement object" vs "Plane curve forwards" — they do not name the method signature, required hypotheses, or return type. Either expand the options to include this detail or narrow criterion 1 to match the granularity of the options.

### Non-blocking Observations

- The two listed options are not strictly alternatives: option 2 explicitly depends on option 1 ("after the complement owner exists"). This should be clarified in the card body — the real decision is "who is the primary owner?" with option 2 as a permitted auxiliary surface on the plane curve, not a replacement for option 1.
- The card's Source Provenance duplicates several URLs already verified in the mapping spec's G1 review. This is acceptable for a standalone decision card (reviewers should not need to chase upstream cards for source verification), but the card could note that sources were independently verified in SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING.
- Recommendation: resolve the two blocking issues (expand options to cover all 4 decision questions; align option granularity with acceptance criteria), then re-submit for review. The card's structure, scope, and dependency management are otherwise sound.

### Summary

| Gate | Verdict | Notes |
|---|---|---|
| G1 — Source Grounding | PASS | All 6 source references verified |
| G2 — Decision Framing | FAIL | Options cover 1 of 4 decision questions |
| G3 — Acceptance Criteria Clarity | FAIL | Criteria demand detail not supplied by options; decision unresolved |
| G4 — Scope Containment | PASS | Stays in decision scope; no implementation creep |
| G5 — Dependency Resolution | PASS | Dependencies satisfied; no dangling references |
| G6 — Obligation Preservation | PASS | All upstream obligations preserved without weakening |

**Overall: CONDITIONAL HOLD.** The decision card is well-grounded (G1, G4, G5, G6 pass), but the framing is incomplete — it asks 4 decision questions while only providing options for 1. The human cannot record a `chosen` value without options for the remaining 3 questions. Resolve the two blocking issues before re-review.
