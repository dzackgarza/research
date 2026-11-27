---
id: SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT]]'
- '[[SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE]]'
title: Recover Vinberg algorithm input and enumeration contract
status: complete
priority: medium
requirement: Vinberg algorithm recovery must specify exact typed inputs, root enumeration
  semantics, backend ownership, integrality checks, and termination evidence.
acceptanceCriteria:
- Inputs are a hyperbolic lattice, control vector or chamber seed, root predicate,
  and exact backend route.
- Root candidates are lattice elements satisfying sourced norm, angle, integrality,
  and chamber constraints.
- Enumeration states whether it is complete for the reported distance shell or chamber
  and records the backend/theorem that proves completeness.
- Number-field and rational/integral coordinate systems are explicit when a backend
  diagonalizes over a fraction field.
complexity: 90
tags:
- FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
---
# Recover Vinberg algorithm input and enumeration contract

## Source Provenance

- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/README.md`
  and docs: Julia/Hecke implementation, number-field support, root iteration.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/README.md`: Sage
  implementation route and examples.
- `src.bak/backends/external/vinbergs_algorithm/references/AlVin/README.md`: C++
  reference implementation pointer.
- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/vinbergs_algo.jl`:
  distance ordering, diagonal-coordinate search, integrality checks, and partial
  continuation state.
- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/quad_forms.jl`:
  root-length and integral-root predicates in the Julia/Hecke route.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/docs/vin-alg-pseudocode-old.txt`
  and `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/vinal.py`:
  Sage route through original lattice coordinates and positive-definite equations in
  the control-vector orthogonal complement.
- `projects/github.com__dzackgarza__lattice-research/advice/theory-backends-vinberg-algorithm`: integrality checks,
  diagonal-coordinate versus original-coordinate enumeration, reference examples, and
  positive-definite subproblem notes.
- `projects/github.com__dzackgarza__lattice-research/references/theory-backend-routing` and
  `projects/github.com__dzackgarza__lattice-research/advice/library-integration`: repo backend route says
  `Lattice.vinberg_*()` uses Oscar `vinberg_algorithm` or a verified Vinberg backend,
  not ad hoc enumeration.
- `theory/foundations/reflective-two-elementary-lattices.md`: definitions of root,
  reflection, reflection group, Coxeter diagram, parabolic diagram, fundamental
  polyhedron, Lanner subgraph, and Vinberg's algorithm.
- `.agents/skills/vinberg-algorithm/SKILL.md`: local workflow trigger.

## Mathematical Objects

The public target is the reflection group `W(L)` of a hyperbolic lattice `L`, generated
by reflections in roots of `L`. A control vector or chamber seed chooses the Weyl
chamber returned by the algorithm; it does not define a different group.

For this spec, a root is a non-isotropic lattice element `v in L` such that the
reflection

```text
s_v(x) = x - (2 * b(x, v) / b(v, v)) * v
```

preserves `L`. Equivalently, the integrality condition
`2 * b(x, v) / b(v, v) in ZZ` must hold for every `x in L`. Norm-and-divisibility
shortcuts such as `v^2 = -2`, or `v^2 = -4` with divisibility `2`, are theorem-backed
specializations for even two-elementary lattices; they are not the general definition of
root.

## Public Contract

The recovered Vinberg surface is owned by the lattice/reflection-group layer, with a
compatibility spelling such as `L.vinberg_*()` only if it delegates to the semantic
reflection-group operation. Inputs are:

- a typed hyperbolic lattice or formed module whose form, signature convention, basis,
  base ring, and exact coordinate system are recorded;
- a control vector or chamber seed in the positive/timelike cone, with the sign
  convention stated by the lattice form;
- a root predicate, including root-length restrictions only when they are source-backed
  for the category of `L`;
- an exact backend route and any backend-specific coordinate transform.

The result is a typed Vinberg search result. It records:

- `lattice`: the parent lattice;
- `reflection_group`: the target `W(L)` or requested reflection subgroup;
- `control_vector`: the chamber seed actually used;
- `root_predicate`: the sourced predicate used to admit roots;
- `roots`: simple-root candidates as elements of `L`, not raw coordinate rows;
- `reflections`: elements of `L.Aut()` induced by the roots;
- `ordering`: exact distance or shell ordering used by the backend;
- `backend`: the exact route, version/source, and limitations;
- `coordinate_maps`: original lattice coordinates, diagonal/number-field coordinates if
  used, and the proof that converted candidates lie in `L`;
- `search_state`: enough continuation state to resume a partial backend search;
- `completeness_status`: one of partial-prefix, shell-complete, chamber-complete,
  nonreflective/does-not-terminate with evidence, or unsupported;
- `termination_evidence`: backend certificate or theorem branch proving the reported
  completeness status.

Docstrings defining public Vinberg surfaces must mention the global diagnostic flag for
surprise logging. When the flag is enabled, returning a partial prefix, changing
coordinate systems over a fraction field, applying a special root-length theorem, or
detecting an unsupported termination branch should log the precise condition and tell
the user which mathematical object was returned.

## Backend Routing

Preferred route: Oscar/Hecke `vinberg_algorithm` when its documented domain supports
the input lattice and requested root predicate.

Candidate audited backends:

- VinbergsAlgorithmNF: Julia/Hecke number-field route. It may diagonalize over a field
  of fractions or number field, enumerate in diagonal coordinates, then check that each
  candidate converts back to integral canonical lattice coordinates.
- VinAl/vinal: Sage route that works in original lattice coordinates and reduces root
  search to positive-definite equations in the orthogonal complement of the control
  vector.
- AlVin: C++ reference/candidate route for rational, quadratic, and selected cyclotomic
  coefficient settings, pending a bridge audit.
- Normaliz, polymake, LattE, 4ti2, Sage, and related polyhedral libraries are only
  candidate owners for bounded cone or Hilbert-basis subproblems, not replacements for
  Vinberg termination proofs.

If none of these routes supports the requested input, the implementation task must
create a backend-gap card with the exact lattice category, coefficient ring, root
predicate, termination need, and candidate software checked. It must not begin a local
bespoke enumeration by default.

## Enumeration and Evidence

If a backend diagonalizes over a field of fractions or number field, the bridge must
record:

- the original lattice basis and form;
- the diagonal or backend coordinate system;
- the transformation maps in both directions;
- the ring in which coordinates are allowed;
- the integrality check proving a candidate is an element of `L`;
- the exact distance or shell key used to sort candidates.

Root candidates are admitted only after checking all active obligations: membership in
`L`, the root predicate, chamber-side inequality with the control vector, acute-angle
inequalities with previously accepted simple roots, and any backend-specific
coordinate-integrality condition.

Completeness claims must be tied to the backend algorithm or a stated theorem branch.
A finite window, fixed number of roots, timeout, or diagram shape alone is not
evidence of chamber completeness. A bounded prefix is useful only as a partial search
state.

## Non-Preservation Boundaries

- Do not hand-roll root enumeration before checking Oscar, VinbergsAlgorithmNF, AlVin,
  VinAl, Sage, Normaliz, and polyhedral backends.
- Do not hide the coordinate system used by the backend.
- Do not return raw vectors without parent lattice and root predicate evidence.
- Do not call a finite prefix of roots a fundamental domain unless the termination
  criterion is satisfied.
- Do not treat special two-elementary root classifications as the definition of root in
  arbitrary lattices.
- Do not treat the control vector as changing the reflection group; it selects the
  chamber for `W(L)`.
- Do not present a Coxeter diagram match, plotted polyhedron, or copied reference
  output as a certificate unless the typed roots, reflections, and chamber evidence are
  verified.

## Acceptance Criteria

- [x] Inputs and root predicates are typed and source-grounded.
- [x] Candidate enumeration records integrality and completeness evidence.
- [x] Backend routes are documented with exact domains and limitations.
- [x] The result object distinguishes partial search state from complete chamber data.

## 6-Gate Protocol Review Log

Review date: 2026-05-07.  Reviewer: Hermes Agent (subagent, 6-gate spec review).
Result: PASS with findings (G2 Finding 1, G5 Finding 1).  No gate failures.
Status before review: needs-human-input.  Status after review: needs-human-input
(review complete; human acceptance still pending).

---

### G1 — Source Grounding

The spec cites 12 source references plus 2 dependency specs in Source Provenance.
All 14 references were verified on disk.

**Historical source files (7/7 exist):**

| Reference | Status |
|---|---|
| `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/README.md` | EXISTS |
| `src.bak/backends/external/vinbergs_algorithm/references/vinal/README.md` | EXISTS |
| `src.bak/backends/external/vinbergs_algorithm/references/AlVin/README.md` | EXISTS |
| `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/vinbergs_algo.jl` | EXISTS |
| `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/quad_forms.jl` | EXISTS |
| `src.bak/backends/external/vinbergs_algorithm/references/vinal/docs/vin-alg-pseudocode-old.txt` | EXISTS |
| `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/vinal.py` | EXISTS |

**Memory/theory/skill files (5/5 exist):**

| Reference | Status |
|---|---|
| `projects/github.com__dzackgarza__lattice-research/advice/theory-backends-vinberg-algorithm` | EXISTS |
| `projects/github.com__dzackgarza__lattice-research/references/theory-backend-routing` | EXISTS |
| `projects/github.com__dzackgarza__lattice-research/advice/library-integration` | EXISTS |
| `theory/foundations/reflective-two-elementary-lattices.md` | EXISTS |
| `.agents/skills/vinberg-algorithm/SKILL.md` | EXISTS |

**Dependency specs (2/2 exist):**

| Reference | Resolved path | Status |
|---|---|---|
| `SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT` | `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md` | EXISTS |
| `SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE` | `plans/features/FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY/specs/SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE.md` | EXISTS |

**Content consistency verification (spot-checked):**

| Claim in spec | Verified against | Consistent? |
|---|---|---|
| "Julia/Hecke implementation, number-field support, root iteration" (line 33) | `VinbergsAlgorithmNF/README.md` lines 1-11: "WIP implementation of Vinberg's algorithm over number fields...using Hecke.jl" | YES |
| "diagonal-coordinate search, integrality checks, and partial continuation state" (lines 39-41) | `vinbergs_algo.jl` lines 10-16: `diagonal_basis`, `diagonal_values`, `scaling`, `diagonal_change`, `diagonal_change_inv` | YES |
| "root-length and integral-root predicates" (line 42) | `quad_forms.jl` (verifies integral root norm computation) | YES |
| "Sage route through original lattice coordinates and positive-definite equations in the control-vector orthogonal complement" (lines 44-46) | `vin-alg-pseudocode-old.txt` lines 1-15: diagonal form D, coordinate change T, positive-definite subproblem in v0^⊥ | YES |
| "L.vinberg_*() uses Oscar vinberg_algorithm or a verified Vinberg backend" (lines 52-53) | `theory-backend-routing.md` line 47: "L.vinberg_*() -> Oscar vinberg_algorithm or a verified Vinberg backend, not an ad hoc implementation" | YES |
| "Do not implement Vinberg's algorithm manually" | `library-integration.md` line 13: "Do NOT: Implement Vinberg's algorithm manually" | YES |
| "definitions of root, reflection, reflection group, Coxeter diagram, parabolic diagram..." (lines 54-56) | `reflective-two-elementary-lattices.md` lines 78-81: defines W(L), W₂(L), W_r(L); extensive Coxeter/parabolic definitions throughout | YES |
| "The control vector...does not define a different group" (line 63) | `vinberg-algorithm.md` lines 13-15: "Different choices of w yield polytopes that are W(L)-equivalent" | YES |

**G1 Finding 1 (advisory):** The spec's Source Provenance lists the two dependency specs by their bare IDs (`SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT`, `SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE`) rather than full wiki-link paths. Both resolve correctly and exist on disk, so this is a presentation preference, not a defect. No action required.

Source-grounding verdict: PASS. All 14 references exist on disk and their content is consistent with the spec's claims.

---

### G2 — Sage Surface Completeness

The spec defines a `VinbergSearchResult` typed object (lines 92-108) with the following
surface elements. Comparison against current Sage surfaces:

**Vinberg search result surface — not yet surfaced in Sage:**

| Surface element | In spec? | In category_specs? | In Sage? | Notes |
|---|---|---|---|---|
| `result.lattice` (parent lattice) | Yes (line 94) | Generic lattice objects exist | N/A | Lattice noun exists |
| `result.reflection_group` (target W(L)) | Yes (line 95) | Not explicit | N/A | W(L) as reflection subgroup of Aut needs realization |
| `result.control_vector` (chamber seed) | Yes (line 96) | Not explicit | N/A | New surface |
| `result.root_predicate` (sourced predicate) | Yes (line 97) | Not explicit | N/A | New surface |
| `result.roots` (elements of L) | Yes (line 98) | Lattice element surface exists | N/A | Element surface exists |
| `result.reflections` (L.Aut() elements) | Yes (line 99) | Aut element surface exists (lattices/homsets.py) | N/A | Aut surface exists |
| `result.ordering` (distance/shell ordering) | Yes (line 100) | Not explicit | N/A | New surface |
| `result.backend` (route, version, limits) | Yes (line 101) | Not explicit | N/A | New metadata surface |
| `result.coordinate_maps` (original↔diagonal) | Yes (line 102) | Not explicit | N/A | New surface |
| `result.search_state` (continuation state) | Yes (line 104) | Not explicit | N/A | New surface |
| `result.completeness_status` (enum) | Yes (lines 105-106) | Not explicit | N/A | New surface |
| `result.termination_evidence` (certificate) | Yes (line 107) | Not explicit | N/A | New surface |
| `L.vinberg_*()` compatibility spelling | Yes (line 81) | Not explicit | N/A | Delegated to lattice noun |

**Dependent surfaces (exist or are spec'd elsewhere):**

| Surface | Owner | Status |
|---|---|---|
| Hyperbolic lattice with form, signature, basis, base ring | category_specs/lattices/ | EXISTS (lattice noun) |
| L.Att() — automorphism group | category_specs/lattices/homsets.py | EXISTS (LatticeAutCategory) |
| Orthogonal group via formed-module Aut | SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE | SPEC'D (status: complete) |
| Backend bridge with matrix normalization | SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT | SPEC'D (status: complete) |

**G2 Finding 1 (advisory):** The `VinbergSearchResult` surface is entirely new — none of
its 12 fields exist in current Sage surfaces or category_specs. This is expected and
acceptable because:
(a) The parent feature card (`FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY.md`, line 21)
    states "This feature does not authorize an ad hoc local Vinberg implementation."
(b) The spec is a recovery contract — it records what must exist when the lattice and
    orthogonal-group layers can express them.
(c) All dependent surfaces (lattice, Aut, orthogonal group, backend bridge) are either
    in active spec or implementation state.

No Sage surface is incorrectly claimed, contradicted, or missed. The gap between the
spec's aspirational surface and current Sage realization is the point of the recovery
feature.

Sage-surface verdict: PASS. All surface gaps are documented and aligned with the
recovery contract's purpose.

---

### G3 — Mathematical Correctness

Audit of mathematical claims in the spec:

**1. Root definition (lines 65-76):**

The spec defines a root as a non-isotropic element v ∈ L such that the reflection
`s_v(x) = x - (2 * b(x, v) / b(v, v)) * v` preserves L, with integrality condition
`2 * b(x, v) / b(v, v) ∈ ZZ` for every x ∈ L.

Verified against:
- `theory/foundations/reflective-two-elementary-lattices.md` lines 78-81: defines
  W(L) as the reflection subgroup generated by reflections in roots. The reflection
  formula is standard.
- `vinberg-algorithm.md` lines 120-124: root correctness checks confirm
  `(r_i, r_i) > 0` (non-isotropic) and primitivity requirements.

The spec correctly distinguishes this general definition from theorem-backed
specializations for even two-elementary lattices (v² = -2, or v² = -4 with
divisibility 2). This is mathematically precise: in a general hyperbolic lattice,
roots can have arbitrary negative norm satisfying the integrality condition; the
norm restrictions are consequences of Nikulin's classification for 2-elementary
lattices, not the definition of root.

**Verdict:** CORRECT.

**2. Control vector semantics (lines 61-63, 86-87):**

The spec states the control vector "chooses the Weyl chamber returned by the
algorithm; it does not define a different group." Verified against:
- `vinberg-algorithm.md` lines 13-15: "Different choices of w yield polytopes that
  are W(L)-equivalent: if w' = g·w for some g ∈ W(L), then the corresponding
  fundamental polytopes are related by the same group element."
- `vinberg-algorithm/SKILL.md` line 17: "The control vector selects a Weyl chamber;
  it does not define a different group."

**Verdict:** CORRECT.

**3. Reflection group = W(L) (line 61):**

The spec targets the full hyperbolic reflection group W(L) generated by reflections
in roots of L. This is the canonical target of Vinberg's algorithm. Verified against:
- `vinberg-algorithm.md` line 11: "All three reference implementations target W(L):
  the full hyperbolic reflection group generated by reflections in roots of L."
- `reflective-two-elementary-lattices.md` line 78: "W(L): the reflection subgroup
  (generated by reflections in roots)."

**Verdict:** CORRECT.

**4. Backend diagonalization and integrality (lines 122-124, 140-155):**

The spec describes that VinbergsAlgorithmNF "may diagonalize over a field of
fractions or number field, enumerate in diagonal coordinates, then check that each
candidate converts back to integral canonical lattice coordinates." Verified against:
- `vinbergs_algo.jl` lines 10-16: the `VinbergData` struct carries `diagonal_basis`,
  `diagonal_values`, `scaling`, `diagonal_change`, and `diagonal_change_inv` —
  exactly the coordinate transform machinery the spec describes.
- `vin-alg-pseudocode-old.txt` lines 7-11: "We change the basis of V in such a way
  that G would have a rational diagonal form D... T is a coordinate change matrix."

**Verdict:** CORRECT.

**5. Completeness taxonomy (lines 105-106):**

The spec defines five completeness states: partial-prefix, shell-complete,
chamber-complete, nonreflective/does-not-terminate with evidence, or unsupported.
This taxonomy accurately reflects the algorithmic realities of Vinberg's algorithm:
- partial-prefix: bounded search without termination proof
- shell-complete: all roots at a given distance level found
- chamber-complete: termination criterion satisfied (finite volume or Lanner
  obstruction)
- nonreflective: proved that no finite-covolume reflection subgroup exists
- unsupported: backend cannot handle the input

These correspond to the known termination behavior of VinbergsAlgorithmNF
(which records `das` internal Coxeter-diagram continuation state and has a
finite-volume check) and AlVin (which distinguishes nontermination from
nonreflectivity).

**Verdict:** CORRECT.

**6. Root candidate admission checks (lines 152-155):**

The spec requires membership in L, root predicate, chamber-side inequality with
control vector, acute-angle inequalities with previously accepted simple roots,
and any backend-specific coordinate-integrality condition. These are the standard
checks performed by all three reference implementations:
- VinbergsAlgorithmNF: `vinbergs_algo.jl` lines 300-400+ (stem enumeration with
  integrality and chamber-side checks)
- vinal: `vin-alg-pseudocode-old.txt` (FundCone procedure with acute-angle checks)
- AlVin: similar constraints documented in mainpage.dox

**Verdict:** CORRECT.

**7. Rejection of Coxeter diagram match as standalone certificate (line 174-176):**

The spec requires "typed roots, reflections, and chamber evidence" to be verified,
not just a diagram match. This is mathematically sound: a Coxeter diagram records
pairwise inner products but does not independently prove that the listed vectors
are simple roots for a fundamental chamber of W(L).

**Verdict:** CORRECT.

No mathematical errors found.

Mathematical-correctness verdict: PASS.

---

### G4 — Nonmathematical Rejection

The spec has an explicit Non-Preservation Boundaries section (lines 162-176) with
seven rejections. Each has a clear rationale and replacement owner:

| # | Rejection | Rationale | Replacement |
|---|---|---|---|
| 1 | Do not hand-roll root enumeration before checking Oscar, VinbergsAlgorithmNF, AlVin, VinAl, Sage, Normaliz, and polyhedral backends (line 164) | Prevents ad hoc implementation; routes to audited backends | Backend routing section (lines 117-138) |
| 2 | Do not hide the coordinate system used by the backend (line 166) | Prevents opaque results; ensures audibility | coordinate_maps field (line 102), enumeration evidence section (lines 140-150) |
| 3 | Do not return raw vectors without parent lattice and root predicate evidence (line 167) | Prevents untyped output; ensures mathematical coherence | roots as elements of L (line 98), root_predicate field (line 97) |
| 4 | Do not call a finite prefix of roots a fundamental domain unless the termination criterion is satisfied (line 168) | Prevents false completeness claims | completeness_status taxonomy (lines 105-106), termination_evidence field (line 107) |
| 5 | Do not treat special two-elementary root classifications as the definition of root in arbitrary lattices (lines 170-171) | Prevents scope narrowing to special cases | Mathematical Objects section (lines 65-76) with general root definition |
| 6 | Do not treat the control vector as changing the reflection group (line 172) | Prevents group misidentification | Lines 61-63: "it selects the chamber for W(L)" |
| 7 | Do not present a Coxeter diagram match, plotted polyhedron, or copied reference output as a certificate (lines 174-176) | Prevents evidentiary shortcuts | Verification requirements tied to typed roots, reflections, chamber evidence |

All seven rejections are mathematically grounded, have clear replacement owners
within the spec body, and preserve the spec's integrity by preventing common
implementation shortcuts.

**Additional non-surface items correctly excluded from the spec:**

- The spec does not prescribe a specific coordinate representation (matrix vs
  tensor vs basis). It requires the coordinate system to be recorded.
- The spec does not require a specific programming language or bridge technology.
  It requires the backend route to be documented.
- The spec does not mandate specific performance targets. It requires
  completeness evidence, not speed.
- Implementation details like the "global diagnostic flag for surprise logging"
  (line 110) are mentioned as docstring requirements, not as spec-level surface
  elements. This is correctly scoped as an implementation guideline.

Nonmathematical-rejection verdict: PASS.

---

### G5 — Ambiguity Routing

Identified design boundaries and their resolution status:

**1. "Root predicate" scope (lines 88-89, 97):**

The spec says the root predicate includes "root-length restrictions only when they
are source-backed for the category of L." The general root predicate is the
integrality condition `2 * b(x, v) / b(v, v) ∈ ZZ ∀ x ∈ L`. The spec correctly
leaves the exact admissible predicates to be determined by the lattice category and
backend, which is appropriate for a contract spec.

**G5 Finding 1 (advisory):** The spec does not define a concrete type or interface
for the `root_predicate` field. It is described as "the sourced predicate used to
admit roots" (line 97) but whether this is a callable, a data structure, or a
reference to a theorem is not specified. This is a genuine design question that
should be resolved at implementation time. **Recommendation:** Create a task or
decision card to specify the root predicate interface when the lattice layer is
ready to receive it. Not blocking for spec acceptance.

**2. Backend route selection (lines 117-138):**

The spec correctly prioritizes Oscar/Hecke `vinberg_algorithm` as the preferred
route and lists four candidate audited backends with their documented domains.
The fallback behavior (create a backend-gap card) is explicitly specified.

**Verdict:** Well-routed. PASS.

**3. Coordinate transform across fraction fields (lines 122-124, 142-150):**

The spec requires that when a backend diagonalizes over a field of fractions,
the bridge must record the transformation maps in both directions and the
integrality check proving a candidate is an element of L. This correctly
identifies the boundary where representation choices (diagonal coordinates)
meet mathematical requirements (lattice membership).

**Verdict:** Well-scoped. PASS.

**4. "completeness_status" enum values:**

The five values (partial-prefix, shell-complete, chamber-complete,
nonreflective/does-not-terminate with evidence, unsupported) are clearly defined.
The distinction between "nonreflective" and "does-not-terminate" is correctly
preserved — these are mathematically different outcomes.

**Verdict:** Well-defined. PASS.

**5. "surprise logging" flag (lines 110-114):**

The spec mentions a "global diagnostic flag for surprise logging" without defining
where it lives or how it is configured. This is an implementation-level detail,
not a spec ambiguity. The spec correctly scopes this as a docstring requirement.

**Verdict:** Acceptable implementation guidance. PASS.

**6. Relationship to sibling spec SPEC-HISTORICAL-COXETER-FUNDAMENTAL-DOMAIN-OUTPUT:**

The sibling spec depends on this one and covers Coxeter diagram, chamber, and
fundamental domain output contracts. The boundary between the two is clean: this
spec covers algorithm inputs, root enumeration, and the search result object; the
sibling spec covers what to do with the results (Coxeter diagram construction,
chamber verification, parabolic classification). The sibling spec's line 8
declares `dependsOn: SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT`, confirming
this spec is upstream.

**Verdict:** Correctly routed. PASS.

**7. YAML `acceptanceCriteria` vs body acceptance criteria:**

The YAML frontmatter (lines 15-24) and body (lines 179-183) both list the same
four acceptance criteria, all checked [x]. The card status is `needs-human-input`.
This is a minor presentation finding — the checked boxes suggest the spec author
believes the criteria are met, but the `needs-human-input` status indicates human
approval is still required. This is not a logical contradiction (a spec can meet
its own criteria while still needing human sign-off), but it may cause confusion
in automated status tracking.

**Recommendation:** Consider leaving acceptance criteria unchecked until human
approval is granted, or add a note clarifying that the checked boxes indicate
author self-assessment, not final approval.

Ambiguity-routing verdict: PASS with one advisory finding (root predicate interface).

---

### G6 — Obligation Preservation

Audit of mathematical obligations transferred from historical references to the
spec contract:

**Obligations stated in acceptance criteria and their preservation status:**

| Obligation | Source evidence | Preserved in spec body? |
|---|---|---|
| Inputs are a hyperbolic lattice, control vector, root predicate, and backend route | Historical references (VinbergsAlgorithmNF README, vinal README, AlVin README) all take Gram matrix + control vector as input | YES — Public Contract lines 80-90 |
| Root candidates are lattice elements satisfying sourced norm, angle, integrality, and chamber constraints | vinbergs_algo.jl integrality checks, vinal pseudocode acute-angle checks, AlVin root validation | YES — Enumeration and Evidence lines 140-155 |
| Enumeration states completeness for reported distance shell or chamber and records backend/theorem | VinbergsAlgorithmNF `das` continuation state, AlVin nontermination/nonreflectivity distinction | YES — completeness_status taxonomy (lines 105-106), termination_evidence (line 107) |
| Number-field and rational/integral coordinate systems are explicit when backend diagonalizes over fraction field | vinbergs_algo.jl diagonal_change/diagonal_change_inv, vinal diagonal form D with coordinate change T | YES — coordinate_maps field (line 102), Enumeration and Evidence lines 140-150 |

**Additional obligations preserved from historical code:**

| Historical obligation | Spec preservation | Strengthened? |
|---|---|---|
| VinbergsAlgorithmNF: distance ordering and diagonal-coordinate search | `ordering` field (line 100), Enumeration and Evidence section | Yes — typed as exact distance/shell key, not raw iteration index |
| VinbergsAlgorithmNF: partial continuation state | `search_state` field (line 104) | Yes — explicit continuation state sufficient to resume |
| vinal: positive-definite subproblem in control-vector orthogonal complement | Backend Routing section (lines 126-128): "reduces root search to positive-definite equations" | Yes — documented as backend route characteristic |
| AlVin: output distinction between roots, CoxIter graph files, finite-volume data | Non-Preservation Boundary #7 (lines 174-176): graph files are backend artifacts, not public API | Yes — prevents treating backend file formats as public API |
| All three: root list without termination status is insufficient | Non-Preservation Boundary #4 (line 168): "Do not call a finite prefix of roots a fundamental domain" | Yes — explicit rejection with replacement |
| Historical: W(L) as target group | Lines 61-63: explicit statement that control vector selects chamber, not group | Yes — prevents group misidentification |
| Oscar `vinberg_algorithm` as preferred route | Backend Routing (line 118): "Preferred route: Oscar/Hecke vinberg_algorithm" | Yes — documents the canonical route |
| library-integration.md: "Do NOT implement Vinberg's algorithm manually" | Non-Preservation Boundary #1 (line 164): "Do not hand-roll root enumeration" | Yes — reinforced with backend-gap card creation requirement (lines 135-138) |

**Obligation completeness check against dependency specs:**

- `SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT`: This spec correctly
  delegates backend matrix normalization and witness verification to the bridge
  contract. The bridge contract's acceptance criteria (witnesses verified as
  lattice isometries, backend matrices normalized at bridge boundary) are the
  correct owners for these obligations. The Vinberg spec does not duplicate them.
- `SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE`: The Vinberg spec's
  `reflections` field returns `L.Aut()` elements (line 99). This correctly
  delegates Aut membership, action conventions, and generator provenance to
  the orthogonal group spec. The Vinberg spec does not re-specify Aut semantics.

**G6 Finding:** All 4 acceptance-criteria obligations and 8 additional historical
obligations are explicitly addressed in the spec body. No obligations are silently
dropped, weakened, or moved without justification. The dependency chain is intact:
backend bridge handles matrix conventions, orthogonal group spec handles Aut
membership, and this spec handles the Vinberg-specific search result contract.

One historical obligation is notably strengthened: the spec requires
`termination_evidence` as a typed certificate or theorem branch (line 107), whereas
the historical references often relied on internal flags (`das` in
VinbergsAlgorithmNF) without exposing the mathematical justification. This is a
positive strengthening.

Obligation-preservation verdict: PASS.

---

### Summary

| Gate | Verdict | Evidence |
|---|---|---|
| G1 Source grounding | **PASS** | 14/14 references exist on disk; content consistency verified for 8 spot-checked claims; all match |
| G2 Sage surface completeness | **PASS** (advisory) | VinbergSearchResult is an aspirational surface with 12 new fields; all dependent surfaces (lattice, Aut, orthogonal group, bridge) are spec'd or implemented; gaps are expected for a recovery contract |
| G3 Mathematical correctness | **PASS** | 7 mathematical claims audited against theory files and reference source code; no errors found |
| G4 Nonmathematical rejection | **PASS** | 7 explicit rejections, all with grounded rationale and replacement owners; no interface leakage |
| G5 Ambiguity routing | **PASS** (advisory) | 7 boundaries examined; 1 advisory on root predicate interface; all other boundaries well-scoped |
| G6 Obligation preservation | **PASS** | 4 acceptance-criteria obligations + 8 historical obligations preserved; 1 strengthened; no weakening |

**Overall: SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT.md passes all six gates.**
The spec is mathematically sound, source-grounded, and correctly routes the Vinberg
algorithm contract through the dependency chain (backend bridge → orthogonal group →
lattice). It records the required mathematical objects and backend candidates without
authorizing ad hoc implementation.

**Findings requiring attention:**

1. **G2 Finding 1 (advisory):** The `VinbergSearchResult` surface (12 fields) is
   entirely new with no current Sage representation. This is expected for a recovery
   spec and does not block acceptance. Implementation should be deferred until
   dependent lattice and orthogonal-group layers are stable.
2. **G5 Finding 1 (advisory):** The `root_predicate` field lacks a concrete type or
   interface specification. Create a task or decision card to resolve this when the
   lattice layer is ready. Not blocking for spec acceptance.

**Recommended actions:**
1. **[Optional]** Create a task card for `root_predicate` interface specification,
   gated on lattice layer readiness.
2. **[Process]** Human reviewer should verify the spec's mathematical claims against
   their own knowledge of Vinberg's algorithm before marking `accepted`.
3. **[Status]** Once human approval is granted, update card status from
   `needs-human-input` to `accepted` (or `complete` per project convention).
