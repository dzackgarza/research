---
id: SPEC-COBLE-LIFTING-THEOREM-VERIFICATION
trackerStatus:
  type: spec
parents:
- '[[FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION]]'
dependsOn:
- '[[SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES]]'
- '[[SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION]]'
- '[[DECISION-TCO-DEFINITION-AND-SIGNATURE]]'
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
title: Verify Nikulin 1.5.2 and Eichler criterion for lattice T_Co
status: unstarted
priority: medium
requirement: The Coble cusp workflow must verify the theorem hypotheses needed to lift discriminant-form isotropic orbits to primitive isotropic vector orbits in T_Co.
acceptanceCriteria:
- A durable theory note records the exact Nikulin and Eichler statements, their hypotheses, and whether they apply to the computed Coble lattice.
- Any orbit-lifting conclusion states the required group, divisibility, discriminant class, and remaining blockers without relying on notation alone.
complexity: 35
tags:
- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
---
# Spec: Verify Nikulin surjectivity and orbit lifting for T_Co

## Summary

The isotropic orbit analysis (Tasks 2.1-2.2) requires lifting O(q_T)-orbits in
the discriminant group A_{T_Co} to O^*(T_Co)-orbits of primitive isotropic vectors
in the lattice T_Co. This uses Nikulin's surjectivity theorem (Prop. 1.5.2)
and the Eichler criterion. Verify that the hypotheses hold for T_Co.

## Hypothesis check

T_Co has the following known/expected properties:
- Rank 11, signature (2, 9)
- 2-elementary discriminant group A ≅ (Z/2Z)^11
- Even lattice (all inner products even)
- Discriminant form q_T: A → Q/2Z

Nikulin 1.5.2 gives conditions under which the map O(L) → O(A_L, q_L) is
surjective. For an even 2-elementary lattice:

1. The spinor norm on O(L) must be computed (or its image in O(A) via the
   connecting homomorphism).
2. The Eichler criterion states that for an indefinite lattice of rank ≥ 3,
   the spinor norm kernel acts transitively on primitive vectors of given
   divisibility and given discriminant class, provided the discriminant class
   is nonzero. For T_Co of rank 11 ≥ 3, this should apply.

## Questions

1. Does Nikulin 1.5.2 apply to T_Co given its signature (2, 9) and (r, a, δ)?
   What are the precise conditions?

2. Is the spinor norm surjectivity known for the Coble lattice? Is O(T_Co) →
   O(A_{T_Co}) surjective, and if not, what is the image?

3. Does the Eichler criterion apply to vectors of divisibility 2 in T_Co?
   (The predicted divisibility for primitive isotropic vectors in the even model.)

4. Are the isotropic orbits in A_{T_Co} in bijection with the O^*(T_Co)-orbits
   of primitive isotropic vectors with divisibility 2? Or does the stable
   orthogonal group O^* need more careful definition here?

## Output

A theory note under `theory/foundations/` recording:
- The relevant theorem statements
- The verification (or blocking issues) for T_Co
- The orbit-count prediction and its theoretical basis

## Dependency Status

This is not a human deferral decision. The theorem-verification work cannot proceed
until the Coble lattice, discriminant-form orbit surface, orbit-enumeration input, and
active mathematical vocabulary are available through the repo's typed category/lattice
surface. Keep this spec `unstarted` under its declared dependencies rather than asking
for human input to bypass the phase order.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (6-Gate Spec Review)

**Gates passed:** G1, G2
**Gates not passed:** G3, G4, G5, G6
**Outcome:** DO NOT PROMOTE — research work not executed; two prerequisite specs unreviewed

---

### Gate 1: Card Structure Correctness

| Check | Status | Evidence |
|---|---|---|
| Frontmatter valid YAML | PASS | `id`, `trackerStatus.type: spec`, `parents`, `dependsOn`, `title`, `status`, `priority`, `requirement`, `acceptanceCriteria`, `complexity`, `tags` all present and well-formed |
| `id` matches filename stem | PASS | `SPEC-COBLE-LIFTING-THEOREM-VERIFICATION` matches filename |
| `parents` records containment | PASS | Parent `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` is the owning feature card |
| `dependsOn` records prerequisites | PASS | `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` (provides discriminant-form method surface) and `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` (provides orbit-count input) are correctly listed. DAG edges confirmed at `plans/plan-dag.md` lines 849-850 |
| Status reflects actual state | PASS | `needs-human-input` is correct — this is a theorem-verification research card requiring human mathematical investigation of Nikulin and Eichler references |
| Tags present | PASS | `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` tag anchors to owning feature |

**Gate 1 Verdict:** PASS. Card structure follows the planning workspace conventions exactly.

---

### Gate 2: Acceptance Criteria Clarity

| Criterion | Clear? | Measurable? | Assessment |
|---|---|---|---|
| "A durable theory note records the exact Nikulin and Eichler statements, their hypotheses, and whether they apply to the computed Coble lattice" | YES | YES — requires explicit theorem statements with hypothesis verification for T_Co | Well-scoped; T_Co has known properties (rank 11, signature (2,9), 2-elementary discriminant) that make the hypothesis check concrete |
| "Any orbit-lifting conclusion states the required group, divisibility, discriminant class, and remaining blockers without relying on notation alone" | YES | YES — requires explicit group names, numerical divisibility, and blocker enumeration | Critical: forbids hand-waving answers like "the group acts transitively" without specifying which group |

Additional clarity from the spec body:
- The four concrete questions (Nikulin applicability, spinor norm surjectivity, Eichler criterion for divisibility 2, orbit bijection) provide a clear research protocol
- Output destination is explicit: `theory/foundations/`
- The spec identifies exact properties of T_Co to check against theorem hypotheses

**Gate 2 Verdict:** PASS. Acceptance criteria are clear, measurable, and properly scoped. The four research questions form an actionable checklist.

---

### Gate 3: Dependency Resolution

| Dependency | Status | Impact |
|---|---|---|
| `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` | `needs-human-input` (unreviewed) | BLOCKER — this spec specifies the `orthogonal_group()`, `isotropic_orbits()`, and `lift_orbit_to_lattice()` method surfaces on `DiscriminantGroup`. Until these methods exist, the lifting theorem cannot be verified computationally against the concrete Coble discriminant form. The theorem statements themselves can be collected from literature independently, but the *verification against T_Co* requires the computed discriminant form. |
| `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` | `needs-human-input` (reviewed, not passed — G3-G6 not passed) | BLOCKER — this spec provides the orbit-count input needed to check whether the lifting theorem predicts the correct number of primitive isotropic vector orbits. Without knowing how many discriminant-form orbits exist, the lifting conclusion cannot state a specific orbit count. |
| `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` (parent) | `in-progress` | Informational — parent feature is active and this spec is one of its children |
| `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` (transitive via feature) | in-progress | The lattice/discriminant-form infrastructure this spec verifies against is still under construction |

DAG edges confirmed at `plans/plan-dag.md`:
```
SPEC_DISCRIMINANT_FORM_ORBIT_SURFACES --> SPEC_COBLE_LIFTING_THEOREM_VERIFICATION  (line 849)
SPEC_COBLE_ISOTROPIC_ORBIT_ENUMERATION --> SPEC_COBLE_LIFTING_THEOREM_VERIFICATION (line 850)
```

Both edges are correct: the lifting theorem verification requires (a) the discriminant-form method surface to be defined so the form can be computed, and (b) the orbit enumeration to be done so the lifting prediction can be checked against actual orbit counts.

**Gate 3 Verdict:** NOT PASSED. Both prerequisite specs are unreviewed/incomplete. The verification cannot proceed against an unspecified method surface and unknown orbit count. This is a genuine dependency block, not a formal one.

---

### Gate 4: Content Quality / Work Completeness

| Deliverable | Present? | Assessment |
|---|---|---|
| Nikulin 1.5.2 statement recording | NO | The spec body mentions "Nikulin 1.5.2 gives conditions under which the map O(L) → O(A_L, q_L) is surjective" but does not state the precise conditions, the theorem's hypotheses, or provide a reference with page/edition. No literature excerpt or translation is recorded. |
| Eichler criterion statement recording | NO | The spec body sketches the Eichler criterion ("for an indefinite lattice of rank ≥ 3, the spinor norm kernel acts transitively on primitive vectors of given divisibility and discriminant class, provided the discriminant class is nonzero") but this is a paraphrase, not a precise statement with hypotheses, domain restrictions, and a verifiable source reference. |
| Hypothesis verification for T_Co | NO | Known properties of T_Co are listed (rank 11, signature (2,9), even, 2-elementary discriminant (Z/2Z)^11), but no verification against Nikulin/Eichler conditions has been performed. The four research questions are posed but unanswered. |
| Spinor norm surjectivity determination | NO | Question posed: "Is the spinor norm surjectivity known for the Coble lattice? Is O(T_Co) → O(A_{T_Co}) surjective, and if not, what is the image?" No computation, literature reference, or determination present. |
| Eichler criterion applicability for divisibility 2 | NO | Question posed: "Does the Eichler criterion apply to vectors of divisibility 2 in T_Co?" No verification present. |
| Orbit bijection conclusion | NO | Question posed: "Are the isotropic orbits in A_{T_Co} in bijection with the O^*(T_Co)-orbits of primitive isotropic vectors with divisibility 2?" No conclusion present; the question itself is well-formed but unanswered. |
| Theory note under `theory/foundations/` | NO | No theory note exists anywhere under the repo. The spec correctly identifies the output destination but no output has been produced. |

The spec body is a well-structured research questionnaire with precisely formulated mathematical questions. The questionnaire has not been answered. The card defines *what* research to do, but no research output exists.

The property list for T_Co (rank 11, signature (2,9), 2-elementary discriminant) is stated without derivation from the geometric construction of the Coble lattice. The spec does not cite a specific source for these lattice invariants (e.g., a computation from the K3 cover or Coble surface construction). The (r, a, δ) Nikulin invariants for T_Co are not stated — this is critical because Nikulin 1.5.2's applicability depends on these invariants.

**Gate 4 Verdict:** NOT PASSED. Research work has not been executed. The card is a valid research spec but contains no research output. None of the four questions are answered. No theory note exists.

---

### Gate 5: Feasibility / Blockers Assessment

| Factor | Assessment |
|---|---|
| Mathematical complexity | High. Nikulin's surjectivity theorem (Prop. 1.5.2) involves spinor norm computations on indefinite lattices, the connecting homomorphism from O(L) to O(A_L, q_L), and delicate conditions on the discriminant form. The Eichler criterion requires understanding of the spinor norm kernel's transitivity on primitive vectors, which depends on the genus of the lattice. For T_Co of signature (2,9), the orthogonal group is an arithmetic group with potentially complicated spinor norm image. |
| Prerequisite dependency | Both `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` and `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` must be resolved first. The former defines the method surface for computing the discriminant form; the latter provides the orbit-count baseline to verify against the lifting prediction. |
| Literature accessibility | Nikulin's "Integral symmetric bilinear forms and some of their applications" (Math. USSR Izvestija, 1980) is a standard reference. The Eichler criterion appears in standard lattice-theory texts (e.g., Miranda-Morrison). The mathematical literature is accessible, but the verification requires expert interpretation of Nikulin's conditions for the specific (r,a,δ) invariants of T_Co. |
| Backend requirements | Verifying the lifting theorem computationally requires Sage's `QuadraticForm.automorphism_group()` for the discriminant form and potentially GAP for the orthogonal group structure. These backends are available but the SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES must define the method surface first. |
| Blockers | (1) Both prerequisite specs unreviewed/incomplete. (2) No one has located and excerpted the precise Nikulin 1.5.2 statement with page reference. (3) No one has verified the (r,a,δ) invariants of T_Co against Nikulin's conditions. (4) The Eichler criterion's "discriminant class nonzero" condition has not been checked against the specific isotropic vectors in T_Co. (5) The theory note does not exist. |
| Human input required | YES — this is inherently a research card. Locating and interpreting Nikulin's theorem, computing spinor norm images, and verifying the Eichler criterion against the specific Coble lattice all require expert mathematical work. Automated tools cannot substitute for theorem-verification judgment. |

**Gate 5 Verdict:** NOT PASSED. Genuine blockers exist at multiple levels: dependency, literature verification, and mathematical computation. The card is correctly marked `needs-human-input`.

---

### Gate 6: Readiness for Promotion

| Criterion | Status |
|---|---|
| Acceptance criteria met | NO — no theory note, no theorem statement recording, no hypothesis verification, no orbit-lifting conclusion |
| Dependencies resolved | NO — both `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` and `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` are unreviewed/incomplete |
| No blockers from lower gates | NO — Gates 3, 4, 5 all have unresolved issues |
| Card internal consistency | YES — the spec is internally consistent: the four research questions flow logically from the summary through the hypothesis check to the expected output |
| No contradictory claims | N/A — no claims made (research not done) |

**Gate 6 Verdict:** NOT PASSED. The card is not ready for promotion. It is a well-formed research spec awaiting execution.

---

### Overall Assessment

| Gate | Status |
|---|---|
| Gate 1: Card Structure Correctness | PASS |
| Gate 2: Acceptance Criteria Clarity | PASS |
| Gate 3: Dependency Resolution | NOT PASSED — both prerequisite specs unreviewed |
| Gate 4: Content Quality / Work Completeness | NOT PASSED — research not executed; no theory note; no theorem statements recorded |
| Gate 5: Feasibility / Blockers | NOT PASSED — genuine blockers at multiple levels |
| Gate 6: Readiness for Promotion | NOT PASSED |

**Recommendation:** DO NOT PROMOTE. The spec card is well-structured (Gates 1-2 pass) and defines clear, valuable research questions for verifying the Nikulin-Eichler lifting theorem for T_Co. However, the actual research work has not been done. The card's four questions (Nikulin applicability, spinor norm surjectivity, Eichler criterion for divisibility 2, orbit bijection) remain unanswered. Both dependencies (`SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` and `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION`) must be resolved before the verification can proceed. No theory note exists under `theory/foundations/`.

**Notable gap beyond the research questions:** The spec's property list for T_Co does not state the Nikulin (r, a, δ) invariants of the Coble lattice. These invariants are essential input to Nikulin 1.5.2's applicability conditions. The spec should either compute or cite a computation of these invariants before the Nikulin hypothesis check can begin.

**Next steps:**
1. Resolve `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` (review/approve) to define the discriminant-form method surface.
2. Resolve `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION` (execute the GAP/Sage/Oscar/Burnside survey, record orbit counts).
3. Compute or verify the (r, a, δ) Nikulin invariants for T_Co from the geometric construction.
4. A human researcher must locate the precise Nikulin 1.5.2 statement (with page/edition reference), excerpt it, and verify its hypotheses against the computed T_Co invariants.
5. The same researcher must state the Eichler criterion precisely, verify its conditions for T_Co, and determine whether primitive isotropic vectors of divisibility 2 satisfy the required discriminant-class condition.
6. Produce the orbit-lifting conclusion stating the relevant group (O^*(T_Co) or the spinor norm kernel), the divisibility, the discriminant class, and any remaining blockers.
7. Record all findings in a durable theory note under `theory/foundations/`.
8. After research output is recorded, re-review for promotion.
