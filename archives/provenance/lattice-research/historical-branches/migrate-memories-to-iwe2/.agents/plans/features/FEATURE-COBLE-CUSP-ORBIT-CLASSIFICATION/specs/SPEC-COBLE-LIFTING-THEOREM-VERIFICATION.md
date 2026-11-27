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

The isotropic orbit analysis asks when finite `O(q_T)`-orbits in `A_{T_Co}` determine
orbits of primitive isotropic vectors in `T_Co`.  This is not a single theorem.

The source-backed part now established for the Dolgachev-Kondo standard Coble target is:

```text
N = <2> + E_10(2)
```

Dolgachev-Kondo identify the K3 orthogonal complement `N_X` with this lattice and state
that it is two-elementary of signature `(2,9)` with `q_N=-q_M`.  Nikulin's Theorem
3.6.3 then gives surjectivity

```text
O(N) -> O(q_N).
```

The source-level target identification is no longer open.  Dolgachev-Kondo construct
the K3 cover `X`, identify the divisor classes `e_0,...,e_10` as generating
`M_X ~= <2> + <-2>^10`, and define `N_X = M_X^\perp <= H^2(X,Z)`.  The repo decision
identifies this `M_X` with the project pullback lattice `S_Co=f^*Pic(S)` and therefore
identifies `T_Co=S_Co^\perp` with `N_X ~= N=<2>+E_10(2)`.

For the full orthogonal group, the remaining lifting problem is now resolved by the
split maximal lattice theorem below.  The unresolved part is narrower: stable-kernel,
real-spinor, stabilizer, centralizer, or Coble arithmetic-subgroup orbit claims still
require their own subgroup image or orbit theorem.

For the standard target, the primitive-vector divisibility is also determined:

```text
N = <2> + E_10(2) = 2(<1> + E_10).
```

With the repo convention `E_10=U+E_8(-1)`, the lattice `<1>+E_10` is unimodular.
Therefore a primitive vector `v in N` pairs with `N` in the ideal `2Z`, so
`div_N(v)=2`.  Via the source-level identification `T_Co ~= N`, this is the
primitive-vector divisibility for the project Coble target.

## Hypothesis check

For the standard target `N=<2>+E_10(2)`, the following hypotheses are source-backed:

- rank `11` and signature `(2,9)`;
- even and indefinite;
- two-elementary discriminant group, inherited from the K3 complement statement
  `q_N=-q_M` where `A_M=(Z/2Z)^11`;
- discriminant form `q_N : A_N -> Q/2Z`.

Therefore Nikulin Theorem 3.6.3 applies to the standard target: `O(N)->O(q_N)` is
surjective.

This does not yet prove the desired Coble primitive-isotropic orbit statement.  The
following hypotheses or witness data are still required:

- an implementation-level construction of `T_Co=(f^*Pic(S))^\perp <= Lambda_K3` if the
  later code must build the lattice from geometric input rather than use the accepted
  source-level target `N`;
- the subgroup of `O(T_Co)` used in the Coble quotient, if it is smaller than the full
  orthogonal group, e.g. stable kernel, real-spinor subgroup, stabilizer, or
  centralizer;
- for the project notation `Gamma_Co`, the ambient lattice, stabilized polarization
  class, involution, restriction to `T_Co`, and image in `O(A_T,q_T)`;
- for the source-backed Enriques-side candidate
  `Gamma_Co^En(delta) = im(Stab_{Gamma_En,2}(Z delta)->O(delta^perp))`, a chosen
  Heegner line `Z delta`, a `Gamma_En,2`-orbit statement for that line, the restriction
  image in `O(T_Co)`, and the induced image in `O(A_T,q_T)`;
- a primitive-isotropic orbit theorem/backend for that smaller subgroup.  The cited
  Eichler criterion requiring a copy of `2U` does not apply to `T_Co ~= N=2B`, because
  all pairings in `2B` are divisible by `2`, so `T_Co` cannot contain a hyperbolic plane
  `U` with pairing `1`.

## Full orthogonal group primitive-isotropic orbit

Let

```text
N = T_Co = 2B,  B=<1>+U+E_8(-1).
```

Then `O(N)=O(B)`: an integral automorphism preserves the Gram form `2B(-,-)` exactly
when it preserves `B(-,-)`.  The lattice `B` is odd, unimodular, and has signature
`(2,9)`.  Milnor's theorem, quoted in Nikulin, says that parity and signature determine
the isomorphism class of an indefinite unimodular lattice.  Hence `B` is the standard
odd unimodular lattice `I_{2,9}`.

Dawes's isotropic-vector section applies to lattices of signature `(2,n)`.  It defines
maximal lattices by the absence of nontrivial totally isotropic subgroups in the
discriminant group, and records the Attwell-Duval result that maximal lattices of
signature `(2,n)` split as `2U+L_0` for `n>=5`.  Since `B` is unimodular, `D(B)=0`, so
`B` is maximal; since `n=9`, it is split.

Dawes Algorithm 4.4 states that if `L` is split maximal and `x,y in L` are primitive
isotropic, then there exists `tau(x,y) in O^+(L)` with `tau(x,y)x=y`.  Applying this to
`B` gives one primitive-isotropic vector orbit under `O^+(B)`, hence under `O(B)`.
Transporting through `O(N)=O(B)` gives:

```text
PrimIso(T_Co)/O^+(T_Co) has one orbit,
PrimIso(T_Co)/O(T_Co) has one orbit.
```

This statement is about primitive isotropic vectors, not only their lines: Algorithm
4.4 sends the vector `x` to the vector `y`.  It is also independent of the finite
discriminant-form orbit computation, except that the two are compatible: every primitive
vector in `N=2B` has divisibility `2`, and its class `v/2+N` is a nonzero isotropic
class in `A_N`; the finite computation shows all such nonzero isotropic classes lie in
one `O(A_N,q_N)`-orbit.

## Questions

- For the standard target `N=<2>+E_10(2)`, Nikulin surjectivity for
  `O(N)->O(q_N)` is answered yes by Theorem 3.6.3.
- For the project lattice `T_Co`, the same conclusion is available by the
  Dolgachev-Kondo source identification recorded in the decision card.
- For the standard target `N`, every primitive vector has divisibility `2`, because
  `N=2B` for the unimodular lattice `B=<1>+E_10`.
- For the standard target, `Iso(A_N,q_N)` has `528` elements, including the zero class,
  and full `O(A_N,q_N)` has two orbits on it: the zero class and one orbit of the `527`
  nonzero isotropic classes.
- Surjectivity of the full orthogonal group does not decide stable-kernel,
  real-spinor, stabilizer, centralizer, or Coble arithmetic-subgroup orbits.  Each such
  subgroup requires its own image or orbit theorem.
- Dolgachev-Kondo source the full quotient `D(N)/O(N)` for the Coble target and the
  birational Heegner-divisor quotient by `O(U+E_10(2))`.  These source statements do
  not define the project subgroup `Gamma_Co` as a stabilizer-centralizer intersection
  with specified `theta`, stabilized class, restriction to `T_Co`, or discriminant-form
  image.
- AEGS source the degree-2 Enriques group `Gamma_En,2` and the `(-2)` discriminant
  divisor in `D(T_En)/Gamma_En`.  This supports the Enriques-side subgroup
  `Gamma_Co^En(delta)` for a chosen Heegner line, but it does not by itself identify
  that subgroup with the project `theta`-centralizer notation or prove its
  primitive-isotropic orbit structure.
- In the sourced decomposition `T_En = U + U(2) + E_8(2)`, choose a standard basis
  `u,v` of the unimodular `U` summand.  Then `delta=u-v` has square `-2`, and
  `delta^perp = Z(u+v) + U(2) + E_8(2) ~= <2> + E_10(2) = T_Co`.  The Heegner line can
  therefore be represented explicitly; its `Gamma_En,2`-orbit remains unresolved.
- The finite image of `Gamma_En,2` can be formulated through discriminant gluing:
  `g_T in O(T_En)` lies in `Gamma_En,2` exactly when its action on `A_TEn` matches,
  under the anti-isometry `A_SEn ~= A_TEn`, the action of some
  `g_S in O(S_En)` fixing the polarization vector `h`.  This reduces the finite
  discriminant-image part of the subgroup problem to
  `Stab_{O(S_En)}(h) -> O(A_SEn,q_SEn)`.
- The script `theory/computations/coble_enriques_degree2_discriminant_stabilizer.sage`
  computes the finite container `Stab_{O(A_SEn,q)}(h/2)`: the full finite
  discriminant-form orthogonal group has order `46998591897600`, the class `h/2` has
  `Q(h) mod 4 = 2`, and its finite stabilizer has order `94755225600`.  Since
  `Stab_{O(S_En)}(h)` has order `2|W(E_8)| = 1393459200`, this finite stabilizer is a
  container larger than the integral group by a factor of `68`.  The same computation
  constructs the actual mod-2 image of `Stab_{O(S_En)}(h)`, generated by the `U` swap
  fixing `h` and the simple-root reflections in `E_8(-1)`; its order is `696729600`,
  so the finite container is larger than the actual image by a factor of `136`.
- For the explicit Coble Heegner complement
  `delta^perp = Z(u+v) + U(2) + E_8(2) = 2(<1> + U + E_8(-1))`, the same script
  constructs the induced finite image on `A_TCo`.  This image fixes the `<1>`
  coordinate and acts through the actual Enriques stabilizer image on the
  `U+E_8(-1)` coordinates.  Its order is `696729600`; on the `528` isotropic classes
  in `A_TCo`, the orbit lengths are `[1, 2, 120, 135, 270]`, with bitmask
  representatives `[0, 2, 14, 40, 42]`.  This finite-orbit split is not a
  primitive-isotropic lattice orbit theorem for the smaller subgroup.
- The same script computes the finite line-stabilizer image relevant to the negative
  Heegner root.  Since `T_En` is the overlattice of `Z delta + delta^perp` obtained by
  adjoining `(delta+eta)/2`, extension over the line forces preservation of `eta/2` in
  `A_TCo`.  The full finite stabilizer of `eta/2` in `O(A_TCo,q_T)` has order
  `46998591897600`, and its image on the lower discriminant group
  `A_TEn ~= A_{U(2)+E_8(2)}` also has order `46998591897600`.  Thus the finite
  double-coset split of the full `O(T_En)` `(-2)`-root orbit by the preimage subgroup
  `Gamma_En,2` is trivial.
- Dawes Algorithm 2.2 supplies the non-isotropic vector criterion for this root-line
  conclusion.  For `O_A(L)={g in O(L) | bar(g) in A}`, with `A<=O(D(L))`, it determines
  vector equivalence when the vector is non-isotropic, its orthogonal complement is
  indefinite, and `O(L)->O(D(L))` is surjective, by checking the discriminant gluing of
  the rank-one generated lattices and their orthogonal complements.  Applying it with
  `L=T_En`, `A=im(Gamma_En,2 -> O(A_TEn))`, and `delta=u-v` is legitimate because
  `delta^2=-2`, `delta^perp=T_Co` has signature `(2,9)`, and the Kneser/Nikulin
  single-genus condition cited by Dawes gives surjectivity for `T_En`.  Together with
  the AEGS/Namikawa full `O(T_En)` `(-2)`-root orbit and the singleton finite
  double-coset split above, this gives one `Gamma_En,2`-orbit of `(-2)` Heegner lines
  represented by `Z delta`.
- AEGS Corollary 3.12 identifies five `Gamma_En,2`-orbits of primitive isotropic lines
  in `T_En`, equivalently the five Baily-Borel 0-cusps of `F_En,2`.  That statement is
  not a substitute for the separate `Gamma_En,2`-orbit statement for the negative
  Heegner lines `Z delta` with `delta^2=-2`.
- The cited Eichler criterion is unavailable for `T_Co`: it requires a copy of `2U`,
  but `T_Co ~= 2(<1>+E_10)` has all pairings divisible by `2`.
- A one-orbit theorem for full `O(T_Co)` and full `O^+(T_Co)` is available through
  `O(T_Co)=O(B)` and Dawes Algorithm 4.4 for split maximal lattices.
- A bijection between finite isotropic classes in `A_T` and primitive isotropic lattice
  orbits for smaller subgroups is not admitted from finite enumeration alone.  It
  requires the representative existence, divisibility, subgroup image, and
  subgroup/kernel-action statements above.

## Output

A theory note under `theory/foundations/` recording:
- The relevant theorem statements
- The verification (or blocking issues) for T_Co
- The orbit-count prediction and its theoretical basis
- The distinction between full `O(T_Co)` surjectivity and any stable, spinor, stabilizer,
  centralizer, or Coble arithmetic-subgroup orbit claim

## Dependency Status

This is not a human deferral decision.  The full primitive-isotropic orbit conclusion
cannot proceed until the subgroup choice, subgroup image when needed, lattice-lifting
theorem/backend, and active mathematical vocabulary are available through the repo's
typed category/lattice definitions.  Keep this spec `unstarted` under its declared
dependencies rather than asking for human input to bypass the phase order.

The theorem sourcing above is still valid prerequisite information: it answers the
full-orthogonal-group surjectivity question for the standard target, but it does not
discharge the downstream orbit-lifting conclusion.

## Source Evidence

- `theory/references/literature/dolgachev_kondo_2013.md:97-101`: the Coble K3
  orthogonal complement is two-elementary of signature `(2,9)`, has `q_N=-q_M`, and is
  isomorphic to `N=<2>+E(2)`.
- `.agents/plans/features/FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION/decisions/DECISION-TCO-DEFINITION-AND-SIGNATURE.md:40-43`:
  the project convention rewrites the target as `<2>+U(2)+E_8(-2)` using
  `E_10=U+E_8(-1)`.
- `theory/references/literature/nikulin1979integral.md:1595-1597`: for an even
  indefinite two-elementary lattice `S`, the homomorphism `O(S)->O(q_S)` is surjective.
- `theory/foundations/reflective-two-elementary-lattices.md:372-385`: Eichler criterion
  source used only under its stated hyperbolic-summand and subgroup hypotheses.
- `theory/references/literature/nikulin1979integral.md:42-50`: Nikulin quotes Milnor's
  theorem that an indefinite unimodular lattice is determined up to isomorphism by
  parity and signature.
- `theory/references/literature/dawes2022orbits_source_notes.md`: checked source notes
  for Dawes's maximal-lattice split statement, Algorithm 4.4 primitive-isotropic
  transport in `O^+(L)`, and Algorithm 2.2 non-isotropic vector equivalence in
  discriminant-preimage subgroups `O_A(L)`.
- `theory/foundations/coble-standard-target-discriminant-form.md`: exact enumeration of
  the standard-target finite discriminant form gives `528` isotropic classes in `A_N`
  and full standard-target orbit sizes `[1, 527]`.
- `theory/foundations/coble-task-background.md`, section `Task 3.1`: records the
  current distinction between the Dolgachev-Kondo full orthogonal quotient, the
  source-backed Enriques-side subgroup `Gamma_Co^En(delta)`, and the unresolved project
  stabilizer-centralizer subgroup `Gamma_Co`.
- `theory/references/literature/aegs_2023.md:122-172`: AEGS definitions of the K3
  lattice, involutions, Enriques period lattice, degree-2 polarization vector, and
  `Gamma_En,2`.
- `theory/references/literature/aegs_2023.md:136-143`: AEGS decomposition
  `T_En ~= U + U(2) + E_8(2)`, giving the explicit representative
  `delta=u-v` in the `U` summand and complement
  `delta^perp ~= <2> + E_10(2)`.
- `theory/references/literature/aegs_2023.md:174-186`: AEGS discriminant divisor
  statement for a `(-2)` vector in `T_En` and its rational Coble-surface
  interpretation.
- `theory/references/literature/nikulin1979integral.md:262-274`: Nikulin's
  primitive-unimodular embedding statement and discriminant-form anti-isometry
  criterion.
- `theory/computations/coble_enriques_degree2_discriminant_stabilizer.sage`: exact
  Sage/GAP computation of `O(A_SEn,q_SEn)`, the stabilizer of `h/2`, the actual
  integral-stabilizer image, and the induced finite image on `A_TCo` for the explicit
  Heegner complement, including the gluing-class stabilizer image used for the
  negative-root finite double-coset calculation.
- `theory/references/literature/aegs_2023.md:394-452`: AEGS folded-diagram and
  Corollary 3.12 source for the five `Gamma_En,2` 0-cusps, i.e. primitive isotropic
  line orbits, not negative Heegner-root orbits.
- `theory/computations/coble_standard_target_discriminant_orbits.sage`: exact
  GAP/Sage witness computing `O(A_N,q_N)` as the stabilizer of the four
  `Q(v)=B(v,v) mod 4` fibers in `GL(B/2B)`.
- `.agents/plans/features/FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION/decisions/DECISION-TCO-DEFINITION-AND-SIGNATURE.md`:
  accepted repo convention identifying `S_Co` with the K3 pullback lattice `M_X` and
  `T_Co` with Dolgachev-Kondo's `N_X ~= <2>+E_10(2)`.

## Non-Evidence

`lean/CobleResearchLean/IsotropicPlanes.lean` is not an implementation witness for the
Coble primitive-plane or lifting claim.  It cites
`computations/task3_2_isotropic_planes.sage`, but a repo-wide search found no file with
that name and the repository has no `computations/` directory.  It also presents
`T_Co` by the diagonal form `diag(2,2,-2,...,-2)`, while the sourced
Dolgachev-Kondo target recorded here is `N=<2>+E_10(2)`.

Therefore that Lean file may be treated only as an unresolved formalization draft until
the missing computation witness is supplied and the lattice presentation is reconciled
with the sourced Coble target.

## Historical Review Log

The review below predates the source evidence recorded above.  It remains a record of
the earlier card state, not the current mathematical status.  The current mathematical
status is: Nikulin full-orthogonal-group surjectivity is sourced for the
Dolgachev-Kondo standard target, standard-target primitive-vector divisibility is `2`,
full standard-target finite discriminant-form orbit sizes are `[1, 527]`, and the
source-level identification `T_Co ~= N` is recorded in the decision card.  The subgroup
image and Eichler/backend lattice-lifting obligations remain unresolved.

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
