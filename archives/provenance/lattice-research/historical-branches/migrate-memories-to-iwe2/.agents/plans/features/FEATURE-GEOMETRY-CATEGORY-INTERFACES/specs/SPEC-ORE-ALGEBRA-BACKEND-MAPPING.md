---
id: SPEC-ORE-ALGEBRA-BACKEND-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[TASK-RESEARCH-ORE-ALGEBRA-INTERFACE]]'
title: Map ore_algebra as an Ore-operator and D-finite backend for Picard-Fuchs
  and monodromy work
status: complete
priority: medium
requirement: Record the upstream `ore_algebra` capability surface, local import
  limitation, and project owner boundaries before any wrapper or dependency
  admission is proposed.
acceptanceCriteria:
- Upstream repository, docs, and source paths are cited.
- Supported mathematical objects and operations are mapped to project owner candidates.
- Picard-Fuchs and monodromy relevance is stated without pretending the package
  computes Picard-Fuchs equations from geometry by itself.
- Local environment failures are recorded in five-field negative-finding format.
complexity: 45
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# ore_algebra Backend Mapping

## Source Scope

- Upstream repository: <https://github.com/mkauers/ore_algebra>.
- Upstream generated documentation: <http://www.algebra.uni-linz.ac.at/people/mkauers/ore_algebra>.
- Upstream monodromy documentation:
  <https://www.algebra.uni-linz.ac.at/people/mkauers/ore_algebra/generated/generated/ore_algebra.analytic.monodromy.html>.
- Temporary source checkout inspected at `/tmp/tmp.EtH8Hu3zIu/ore_algebra`.
- Local memory: `theory-graph-monodromy-hodge-methods`, which records
  `ore_algebra.analytic.monodromy.monodromy_matrices(dop, base)` as the candidate
  route when a Picard-Fuchs differential operator is already known.

## Backend Boundary

`ore_algebra` is a Sage package for Ore algebras, Ore polynomials, and D-finite
functions. Upstream README evidence lists arithmetic/actions, gcrd/lclm, D-finite
closure properties, creative telescoping, transformations between related algebras,
guessing, desingularization, polynomial/rational/generalized-series solvers, and
analytic solution computation for univariate differential operators with rigorous
error bounds.

The package is therefore a candidate backend for algebraic differential operators and
their analytic continuation. It is not, by itself, a geometry backend that derives
Picard-Fuchs operators from a family of curves or surfaces. The geometric-to-operator
step belongs to separate Gauss-Manin/Picard-Fuchs source work, likely via Singular,
Macaulay2, literature tables, or a future family-of-varieties spec.

## Candidate Surface Mapping

| Upstream surface | Project owner candidate | Public meaning | Admission status |
| --- | --- | --- | --- |
| `OreAlgebra(...)`, `DifferentialOperators(...)` | future differential-operator or D-module category | Parent objects for noncommutative Ore operator rings | Backend evidence only; owner spec missing. |
| Ore operators with `gcrd`, `lclm`, desingularization, solution methods | differential-operator category element methods | Algebraic operations on linear differential/recurrence operators | Candidate after operator category design. |
| D-finite function support and closure properties | D-finite function/sequence category | Functions or sequences represented by annihilating operators and initial data | Candidate after D-finite noun spec. |
| Creative telescoping | period/integral or D-module workflow | Produce differential/recurrence equations for parameterized integrals or sums | Candidate backend; geometry inputs and certificates still need spec work. |
| `ore_algebra.analytic.monodromy.monodromy_matrices(dop, base, eps, algorithm)` | local system / differential equation monodromy surface | Matrices for analytic continuation of solutions around singularities of a differential operator | Candidate once a Picard-Fuchs operator is already available. |
| `numerical_transition_matrix`, analytic continuation path utilities | local system parallel transport | Transition matrices along paths for a differential operator's solution space | Candidate backend; numerical/certified status must be audited. |

## Picard-Fuchs And Monodromy Consequence

For curve or surface families, this backend should enter after a Picard-Fuchs
operator has been constructed or sourced. It can then compute local monodromy matrices
of the operator's solution sheaf around singular points, and those matrices can feed
Jordan-normal-form and nilpotent-monodromy analysis. It does not replace the
geometric derivation of the operator, the choice of cohomology bundle/local system, or
the proof that the operator controls the desired periods.

## Negative Findings

- Searched: local Sage import check `sage -python -c "import ore_algebra"`; upstream
  repository README; upstream source checkout under `/tmp/tmp.EtH8Hu3zIu/ore_algebra`;
  local memory `theory-graph-monodromy-hodge-methods`.
- Found: local import fails with `ImportError: cannot import name Category`; upstream
  sources and documentation still expose the relevant Ore-operator, D-finite, analytic
  continuation, and monodromy APIs.
- Conclusion: inference based on the checked local environment: the package is not
  currently usable as an installed backend in this Sage environment without an
  environment/compatibility repair pass.
- Confidence: High for the observed local import failure; Medium for the exact repair
  path because installation was not attempted in this research card.
- Gaps: no installation or compatibility fix was attempted; no package test suite was
  run; Sage-version compatibility issues were not triaged beyond the import failure.

- Searched: upstream README, generated documentation index, `src/ore_algebra/analytic/monodromy.py`,
  `src/ore_algebra/ore_algebra.py`, and local monodromy/Hodge memory.
- Found: `ore_algebra` computes with Ore operators and can compute monodromy matrices
  for an input differential operator, but the checked sources do not provide a complete
  project-level route from an arbitrary algebraic family to the correct Picard-Fuchs
  operator.
- Conclusion: inference based on the checked source corpus: integration is relevant
  for Picard-Fuchs monodromy after the operator exists, but it should not be admitted
  as a one-stop family-monodromy or geometry backend.
- Confidence: High.
- Gaps: Noether-Lefschetz/Singular material and Macaulay2 PeriodIntegrals-style routes
  remain for the separate Picard-Fuchs/JNF research card.

## Follow-Up Consequence

No wrapper or dependency-admission card is warranted yet. The concrete next work is the
existing Picard-Fuchs/JNF research card, which should decide how Picard-Fuchs operators
are constructed or sourced. If that card selects `ore_algebra` for operator-level
monodromy, it should file a separate environment/compatibility task before any
implementation depends on local imports.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate spec card review)

**Gates passed:** G1, G2, G3, G4, G5, G6
**Gates failed:** None
**Outcome:** PASS — the spec is source-grounded, mathematically correct, and properly
routes all ambiguity to tracked follow-up cards. Two advisory findings noted under G2.

---

#### G1 — Source Grounding

PASS.

Every source citation in the spec was verified on disk or via public URL:

| Reference | Actual path | Exists |
| --- | --- | --- |
| Upstream repository | `https://github.com/mkauers/ore_algebra` | YES (public URL) |
| Upstream generated docs | `http://www.algebra.uni-linz.ac.at/people/mkauers/ore_algebra` | YES (public URL) |
| Upstream monodromy docs | `https://www.algebra.uni-linz.ac.at/people/mkauers/ore_algebra/generated/generated/ore_algebra.analytic.monodromy.html` | YES (public URL) |
| Temp source checkout | `/tmp/tmp.EtH8Hu3zIu/ore_algebra` | YES (contains README, src/, setup.py) |
| Upstream `ore_algebra.py` | `/tmp/tmp.EtH8Hu3zIu/ore_algebra/src/ore_algebra/ore_algebra.py` | YES (69747 bytes) |
| Upstream `monodromy.py` | `/tmp/tmp.EtH8Hu3zIu/ore_algebra/src/ore_algebra/analytic/monodromy.py` | YES (29632 bytes) |
| Upstream README | `/tmp/tmp.EtH8Hu3zIu/ore_algebra/README.md` | YES (4228 bytes) |
| Local memory | `/home/dzack/research/projects/github.com__dzackgarza__lattice-research/references/theory-graph-monodromy-hodge-methods` | YES (5201 bytes, 43 lines) |
| Parent feature | `/home/dzack/research/plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md` | YES |
| Dependency task | `.../tasks/TASK-RESEARCH-ORE-ALGEBRA-INTERFACE.md` | YES |
| Cross-referenced spec | `.../specs/SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING.md` | YES (references this spec at line 57) |

Frontmatter validation:
- `id: SPEC-ORE-ALGEBRA-BACKEND-MAPPING` matches filename stem ✓
- `parents` correctly lists `FEATURE-GEOMETRY-CATEGORY-INTERFACES` ✓
- `dependsOn` correctly lists `TASK-RESEARCH-ORE-ALGEBRA-INTERFACE` ✓
- The dependency task's work log (line 57-60) confirms this spec was created as its
  output: "Created `[[SPEC-ORE-ALGEBRA-BACKEND-MAPPING]]` with capability mapping,
  Picard-Fuchs boundary, and local import negative finding" ✓

Source content verification:
- README.md confirms listed features: arithmetic/actions, gcrd/lclm, D-finite closure,
  creative telescoping, transformations, guessing, desingularization, solvers, analytic
  solutions ✓
- `monodromy_matrices(dop, base, eps, sing, **kwds)` confirmed at line 554 of
  `monodromy.py` ✓
- `numerical_transition_matrix(self, path, eps, **kwds)` confirmed at line 1493 of
  `differential_operator_1_1.py` (method on the univariate differential operator class) ✓
- `analytic_continuation(dop, path, eps, ctx, ini, post, ...)` confirmed at line 288 of
  `analytic_continuation.py` ✓

No orphan references, dead links, or missing source paths detected.

#### G2 — Sage Surface Completeness

PASS with two advisory findings.

The spec's candidate surface mapping table (lines 56-63) inventories 6 rows covering
the major mathematical surfaces. Source-method audit:

| Upstream surface | Source location | Spec table coverage |
| --- | --- | --- |
| `OreAlgebra(...)` / `DifferentialOperators(...)` | `ore_algebra.py` L1057 (`OreAlgebra_generic`) | Row 1 ✓ |
| Ore operators with gcrd/lclm/desingularization | `ore_operator.py`, `ore_algebra.py` | Row 2 ✓ |
| D-finite function support | `dfinite_function.py` | Row 3 ✓ |
| Creative telescoping | `ore_algebra.py` | Row 4 ✓ |
| `monodromy_matrices(dop, base, eps, algorithm)` | `monodromy.py` L554 | Row 5 ✓ |
| `numerical_transition_matrix(path, eps)` | `differential_operator_1_1.py` L1493 | Row 6 ✓ |

**G2 Finding 1 (advisory):** The `guessing` module (`guessing.py`) provides `guess()`,
`guess_rec()`, `guess_deq()`, `guess_qrec()`, `guess_raw()`, `guess_hp()`, and
`guess_mult()` — a significant upstream capability for inferring differential equations
or recurrences from sequence data. This is mathematically relevant for Picard-Fuchs work
(guessing the operator from series expansions of periods). The Backend Boundary section
(line 44) mentions "guessing" in passing, but the candidate surface mapping table has no
row for it. Not a gate failure — the spec's scope is backend mapping for
Picard-Fuchs/monodromy pipeline work, and guessing is a supporting tool rather than a
core geometry backend. The existing rows already cover the primary pipeline.

**G2 Finding 2 (advisory):** The upstream README lists "natural transformations between
related algebras" (e.g., `to_S()`, `to_F()`, `to_T()`, `to_D()`, `to_Q()`, `to_J()`
operators that convert between shift, differential, theta, and q-operator algebras).
The Backend Boundary section (line 44) acknowledges "transformations between related
algebras" but no explicit table row maps them to a project owner. This could be relevant
for converting Picard-Fuchs operators between different bases (e.g., xD vs. D
formalisms). Not a gate failure — the spec correctly treats algebra transformations as
backend evidence that feeds into operator-level work once category specs exist.

The spec's verbose "Backend Boundary" prose section (lines 41-52) provides a summary of
capabilities beyond the table, which mitigates both findings.

#### G3 — Mathematical Correctness

PASS.

Every mathematical claim was cross-checked against upstream source evidence:

- **"ore_algebra is a Sage package for Ore algebras, Ore polynomials, and D-finite
  functions"** — confirmed by README.md description ✓
- **"arithmetic/actions, gcrd/lclm, D-finite closure properties, creative telescoping,
  transformations between related algebras, guessing, desingularization,
  polynomial/rational/generalized-series solvers, and analytic solution computation for
  univariate differential operators with rigorous error bounds"** — all confirmed by
  README.md feature list and source module structure ✓
- **"It is not, by itself, a geometry backend that derives Picard-Fuchs operators from
  a family of curves or surfaces"** — correct; ore_algebra operates on known
  differential/recurrence operators, it does not accept curve/surface family definitions
  and produce Picard-Fuchs operators ✓
- **"The geometric-to-operator step belongs to separate Gauss-Manin/Picard-Fuchs source
  work, likely via Singular, Macaulay2, literature tables, or a future
  family-of-varieties spec"** — correct; confirmed by the companion spec
  `SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING.md` which maps `foliation.lib` and
  Singular as the geometric-to-operator route ✓
- **"`monodromy_matrices(dop, base, eps, algorithm)` — Matrices for analytic
  continuation of solutions around singularities of a differential operator"** —
  confirmed by `monodromy.py` lines 554-646; the function computes monodromy by
  analytic continuation of a fundamental solution matrix along loops around
  singularities ✓
- **"`numerical_transition_matrix` — Transition matrices along paths for a differential
  operator's solution space"** — confirmed at `differential_operator_1_1.py` L1493;
  computes the parallel transport matrix of the solution space along a specified
  path ✓
- **"For curve or surface families, this backend should enter after a Picard-Fuchs
  operator has been constructed or sourced"** — correct architectural assessment;
  the local memory file (line 29) states the same: "the stored tool is
  `ore_algebra.analytic.monodromy.monodromy_matrices(dop, base)`, but ore_algebra was
  not installed" ✓
- **"It can then compute local monodromy matrices of the operator's solution sheaf
  around singular points, and those matrices can feed Jordan-normal-form and
  nilpotent-monodromy analysis"** — correct; monodromy matrices can be factored into
  Jordan normal form, and the nilpotent part (N = log(T_unipotent)) encodes the weight
  filtration ✓
- **"It does not replace the geometric derivation of the operator, the choice of
  cohomology bundle/local system, or the proof that the operator controls the desired
  periods"** — correct; these are geometric responsibilities that lie upstream ✓

Negative findings verification:
- Local import failure `ImportError: cannot import name Category` is recorded without
  speculating about root cause ✓
- "No installation or compatibility fix was attempted" — consistent with the research
  task card's boundary: "Do not vendor or wrap ore_algebra in this card" ✓
- "The checked sources do not provide a complete project-level route from an arbitrary
  algebraic family to the correct Picard-Fuchs operator" — confirmed by source audit;
  ore_algebra accepts differential operators as input, not algebraic families ✓

No mathematical errors, mischaracterizations, or unsupported claims detected.

#### G4 — Nonmathematical Rejection

PASS.

The spec correctly identifies and rejects non-mathematical surfaces:

- The "Backend Boundary" section (lines 48-52) explicitly states: "It is not, by itself,
  a geometry backend" — correctly blocks treating ore_algebra as a one-stop geometry
  solution ✓
- Candidate surface mapping table admission statuses: "Backend evidence only; owner spec
  missing", "Candidate after operator category design", "Candidate after D-finite noun
  spec", "Candidate backend; geometry inputs and certificates still need spec work",
  "Candidate once a Picard-Fuchs operator is already available" — all statuses correctly
  defer admission to future specs ✓
- The "Follow-Up Consequence" section explicitly states: "No wrapper or
  dependency-admission card is warranted yet" — correctly blocks premature
  implementation ✓
- Two negative findings follow the five-field format (Searched, Found, Conclusion,
  Confidence, Gaps) ✓
- The spec does not propose wrapper code, dependency pinning, or import paths ✓
- The spec does not leak implementation intent or treat Sage helper names as project
  mathematical nouns ✓

The boundary between source evidence and implementation permission is correctly
maintained.

#### G5 — Ambiguity Routing

PASS.

Unresolved questions are explicitly routed to tracked follow-up cards:

- **Operator naming ambiguity:** Table rows 1-2 use "future differential-operator or
  D-module category" and "Candidate after operator category design" — correctly defers
  naming and ownership to future category specs ✓
- **Picard-Fuchs derivation ambiguity:** "The geometric-to-operator step belongs to
  separate Gauss-Manin/Picard-Fuchs source work" (lines 51-52) — correctly routes to
  the companion spec `SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING.md` ✓
- **Implementation gate:** "If that card selects `ore_algebra` for operator-level
  monodromy, it should file a separate environment/compatibility task before any
  implementation depends on local imports" (lines 107-109) — concrete routing:
  Picard-Fuchs/JNF card → environment repair task → implementation ✓
- **Follow-up consequence** explicitly links to the "existing Picard-Fuchs/JNF research
  card" (`TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES`) ✓
- **Admission status column:** Each table row has an explicit, non-ambiguous status —
  no "maybe" or "TBD" without a routing path ✓

No ambiguity is left as unresolved prose; every open question has a concrete routing
path to a tracked card.

#### G6 — Obligation Preservation

PASS.

- `dependsOn: [[TASK-RESEARCH-ORE-ALGEBRA-INTERFACE]]` — the authorizing research task
  is correctly declared ✓
- The research task's work log (line 57-60) confirms this spec was created from it and
  that the task status was moved to `needs-agent-review` upon spec creation ✓
- The research task's `successCriteria` are all satisfied by this spec: upstream
  docs/sources cited ✓, project nouns mapped ✓, Picard-Fuchs/monodromy relevance stated
  without overclaim ✓, negative findings in five-field format ✓
- Acceptance criteria (lines 16-21) are concrete and checkable:
  1. "Upstream repository, docs, and source paths are cited" — CHECKABLE against G1
     audit ✓
  2. "Supported mathematical objects and operations are mapped to project owner
     candidates" — CHECKABLE; candidate surface mapping table (lines 56-63) ✓
  3. "Picard-Fuchs and monodromy relevance is stated without pretending the package
     computes Picard-Fuchs equations from geometry by itself" — CHECKABLE; Backend
     Boundary section ✓
  4. "Local environment failures are recorded in five-field negative-finding format" —
     CHECKABLE; two negative findings (lines 75-101) in correct format ✓
- The Follow-Up Consequence (lines 103-109) preserves the obligation to handle
  environment repair before any implementation ✓
- The spec is cross-referenced by the companion spec
  `SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING.md` at line 57, confirming it is tracked
  in the broader backend mapping landscape ✓

No broken dependency chains, orphaned obligations, or unmet acceptance criteria
detected.

---

**Overall verdict:** The spec passes all six gates. It is a well-grounded,
mathematically accurate mapping of ore_algebra functionality into the project's
category-spec vocabulary. The spec correctly places ore_algebra as a downstream
operator/monodromy backend that should enter only after Picard-Fuchs operators are
sourced or computed via geometric methods. Two advisory G2 findings note that the
guessing module and algebra transformation methods are acknowledged in prose but not
mapped to explicit table rows — these are not blocking issues given the spec's scoped
focus on Picard-Fuchs/monodromy pipeline relevance. No gate failures. No blocking
findings.
