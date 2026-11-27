---
id: SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION
trackerStatus:
  type: spec
parents:
- '[[FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION]]'
dependsOn:
- '[[SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES]]'
- '[[DECISION-TCO-DEFINITION-AND-SIGNATURE]]'
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
title: Research isotropic orbit enumeration in finite discriminant groups
status: unstarted
priority: medium
requirement: The Coble cusp workflow must have an exact route for enumerating isotropic discriminant-form orbits in the relevant 2-elementary finite quadratic group.
acceptanceCriteria:
- The output records which backend or theorem route can compute O(A,q)-orbits for the specific Coble discriminant group.
- The recommendation states feasibility, expected inputs, and any blockers for implementation without replacing exhaustive orbit work by bounded search.
complexity: 30
tags:
- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
---
# Spec: Isotropic orbit enumeration in finite discriminant groups

## Summary

Survey existing software capabilities for computing orbits of isotropic (norm-0)
elements under the orthogonal group O(A, q) of a finite quadratic form over Z/2^kZ,
specifically for discriminant groups of 2-elementary lattices A ≅ (Z/2Z)^11.

## Input

- A finite quadratic form q: A → Q/2Z on A ≅ (Z/2Z)^11 (order 2048).
- The orthogonal group O(A, q) as a finite matrix group.
- The set of isotropic elements {x ∈ A : q(x) = 0 mod 2Z} (known count: 528
  elements for the standard form).

## Questions

1. **GAP**: Can `OrbitsDomain(O, elements)` handle a group of size |O(A,q)| on 528
   points? Is the group small enough to compute directly? What's the expected orbit
   count and stabilizer structure?

2. **Sage**: Does `QuadraticForm.automorphism_group()` produce the full O(q)?
   Can its output be used with Sage's `PGroup` or `MatrixGroup` orbit methods?

3. **Oscar/Hecke**: What discriminant-form orbit methods exist?

4. **Burnside**: Can the orbit count be derived from character theory or invariant
   theory without enumerating the full group?

## Output

A brief report (theory note or decision card body) recording:
- Which backends handle this computation for the specific discriminant group
- Feasibility (can we compute all orbits directly, or do we need theory)
- Recommended implementation route

## Dependency Status

This is not a human decision or an optional deferral. The work is downstream because it
must consume the category, lattice/discriminant, geometry, and `T_Co` vocabulary rather
than rebuilding the computation from raw matrices or ad hoc finite quadratic forms.
Keep this spec `unstarted` until the declared dependencies and active phase gate allow
the Coble orbit survey to run.

---

## 6-Gate Protocol Review Log

### Review 2026-05-07 (6-Gate Spec Review)

**Gates passed:** G1, G2
**Gates not passed:** G3, G4, G5, G6
**Outcome:** DO NOT PROMOTE — research work not executed

---

### Gate 1: Card Structure Correctness

| Check | Status | Evidence |
|---|---|---|
| Frontmatter valid YAML | PASS | `id`, `trackerStatus.type: spec`, `parents`, `dependsOn`, `title`, `status`, `priority`, `requirement`, `acceptanceCriteria`, `complexity`, `tags` all present and well-formed |
| `id` matches filename stem | PASS | `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` matches filename |
| `parents` records containment | PASS | Parent `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` is the owning feature card |
| `dependsOn` records prerequisites | PASS | `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` is correctly listed as the dependency providing the discriminant-form method surface |
| Status reflects actual state | PASS | `needs-human-input` is correct — this is a research survey spec requiring human investigation of backend capabilities |
| Tags present | PASS | `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` tag anchors to owning feature |

**Gate 1 Verdict:** PASS. Card structure follows the planning workspace conventions exactly.

---

### Gate 2: Acceptance Criteria Clarity

| Criterion | Clear? | Measurable? | Assessment |
|---|---|---|---|
| "The output records which backend or theorem route can compute O(A,q)-orbits for the specific Coble discriminant group" | YES | YES — requires named backends with yes/no/partial determination | Well-scoped; the Coble discriminant group is A ≅ (Z/2Z)^11 |
| "The recommendation states feasibility, expected inputs, and any blockers for implementation without replacing exhaustive orbit work by bounded search" | YES | YES — requires explicit feasibility statement, input requirements, and blocker list | Critical: explicitly forbids bounded-search-as-exhaustive substitution |

Additional clarity from the spec body:
- Input contract is explicit: A ≅ (Z/2Z)^11 (order 2048), quadratic form q_T, O(A,q) group, 528 isotropic elements
- Output format is explicit: brief report (theory note or decision card body)
- Four concrete research questions for GAP, Sage, Oscar/Hecke, and Burnside

**Gate 2 Verdict:** PASS. Acceptance criteria are clear, measurable, and properly scoped.

---

### Gate 3: Dependency Resolution

| Dependency | Status | Impact |
|---|---|---|
| `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` | `needs-review` (DAG shows `needs-review`) | BLOCKER — this spec specifies the missing method surfaces (`orthogonal_group()`, `isotropic_orbits()`, `lift_orbit_to_lattice()`) on `DiscriminantGroup` that the Coble orbit enumeration research depends on. Until Phase 4 discriminant-group methods are specified and the orbit surface spec is approved, a backend survey cannot determine whether the required methods exist or need new implementation. |
| `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` (parent) | `in-progress` | Informational — parent feature is active and this spec is one of its children |
| `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` (transitive via feature) | in-progress | The lattice/discriminant-form infrastructure this spec surveys against is still under construction |

DAG edges confirmed at `plans/plan-dag.md` line 848:
```
SPEC_DISCRIMINANT_FORM_ORBIT_SURFACES --> SPEC_COBLE_ISOTROPIC_ORBIT_ENUMERATION
```
This is a correct dependency: the method surface must exist before backends can be surveyed for it.

**Gate 3 Verdict:** NOT PASSED. The prerequisite `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` has not been reviewed/approved. The research survey cannot be executed against an unspecified method surface. This is a genuine dependency block, not a formal one.

---

### Gate 4: Content Quality / Work Completeness

| Deliverable | Present? | Assessment |
|---|---|---|
| GAP capability survey | NO | Question posed but unanswered: "Can `OrbitsDomain(O, elements)` handle a group of size \|O(A,q)\| on 528 points?" No GAP session, benchmark, or literature reference present. |
| Sage capability survey | NO | Question posed but unanswered: "Does `QuadraticForm.automorphism_group()` produce the full O(q)? Can its output be used with Sage's `PGroup` or `MatrixGroup` orbit methods?" No Sage session or API documentation reference present. |
| Oscar/Hecke capability survey | NO | Question posed but unanswered: "What discriminant-form orbit methods exist?" No Oscar/Hecke API survey present. |
| Burnside/character-theory analysis | NO | Question posed but unanswered: "Can the orbit count be derived from character theory or invariant theory without enumerating the full group?" No theoretical analysis present. |
| Feasibility determination | NO | No statement on whether direct computation, theory, or hybrid approach is needed. |
| Recommended implementation route | NO | No route proposed. |
| Blocker documentation | NO | No blockers documented beyond the formal dependency. |

The spec body is a well-structured research questionnaire. The questionnaire has not been answered. The card defines *what* research to do, but no research output exists. The acceptance criteria require a report containing backend determinations, feasibility, and a recommended route — none of which are present.

The 528 isotropic-element count is stated without derivation or verification. The group size |O(A,q)| is not estimated, which is critical for feasibility analysis.

**Gate 4 Verdict:** NOT PASSED. Research work has not been executed. The card is a valid research spec but contains no research output.

---

### Gate 5: Feasibility / Blockers Assessment

| Factor | Assessment |
|---|---|
| Mathematical complexity | Moderate. A ≅ (Z/2Z)^11 is a finite vector space of size 2048 over F_2. The orthogonal group O(A,q) is a finite classical group over F_2. Orbit enumeration of 528 isotropic elements under this finite group is, in principle, computationally tractable — GAP handles far larger permutation groups. The unknown is whether the specific quadratic form q_T (induced from the Coble lattice discriminant) has any pathological properties that complicate the group structure. |
| Prerequisite dependency | `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` must be approved first so the method surface is defined. |
| Backend availability | GAP is available via Sage; Sage's `QuadraticForm.automorphism_group()` handles finite forms; Oscar/Hecke have discriminant-form APIs. All three are plausible routes. |
| Blockers | (1) Prerequisite spec not approved. (2) No one has executed the GAP/Sage/Oscar survey. (3) The actual Coble discriminant form q_T has not been computed/passed from the lattice pipeline — the spec assumes the form exists. |
| Human input required | YES — this is inherently a research card. Evaluating GAP's orbit performance on a specific group, testing Sage's automorphism_group on a specific finite quadratic form, and surveying Oscar/Hecke APIs all require interactive mathematical software work. |

**Gate 5 Verdict:** NOT PASSED. Genuine blockers exist. Research requires human mathematical-software work that has not been performed. The card is correctly marked `needs-human-input`.

---

### Gate 6: Readiness for Promotion

| Criterion | Status |
|---|---|
| Acceptance criteria met | NO — no backend report, no feasibility statement, no recommended route |
| Dependency resolved | NO — `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` still `needs-review` |
| No blockers from lower gates | NO — Gates 3, 4, 5 all have unresolved issues |
| Card internal consistency | YES — the spec is internally consistent (questions flow from input to output logically) |
| No contradictory claims | N/A — no claims made (research not done) |

**Gate 6 Verdict:** NOT PASSED. The card is not ready for promotion. It is a well-formed research spec awaiting execution.

---

### Overall Assessment

| Gate | Status |
|---|---|
| Gate 1: Card Structure Correctness | PASS |
| Gate 2: Acceptance Criteria Clarity | PASS |
| Gate 3: Dependency Resolution | NOT PASSED — prerequisite spec unreviewed |
| Gate 4: Content Quality / Work Completeness | NOT PASSED — research not executed |
| Gate 5: Feasibility / Blockers | NOT PASSED — genuine blockers exist |
| Gate 6: Readiness for Promotion | NOT PASSED |

**Recommendation:** DO NOT PROMOTE. The spec card is well-structured (Gates 1-2 pass) and defines clear, valuable research questions. However, the actual research work has not been done. The card's four backend questions (GAP, Sage, Oscar/Hecke, Burnside) remain unanswered. The dependency `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` must be reviewed/approved before the method surface is defined for the backend survey.

**Next steps:**
1. Resolve `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` (review/approve) to define the discriminant-form orbit method surface.
2. A human researcher must execute the GAP, Sage, Oscar/Hecke, and Burnside surveys against the actual Coble discriminant form (once computed).
3. The research output should be recorded as a theory note under `theory/foundations/` or directly in this card body, satisfying all three acceptance criteria.
4. After research output is recorded, re-review for promotion.
