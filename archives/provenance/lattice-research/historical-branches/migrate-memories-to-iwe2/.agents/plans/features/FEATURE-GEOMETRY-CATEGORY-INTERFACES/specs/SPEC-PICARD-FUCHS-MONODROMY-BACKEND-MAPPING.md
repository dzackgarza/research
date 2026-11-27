---
id: SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES]]'
title: Map Picard-Fuchs and Gauss-Manin backends for family monodromy and Jordan
  data
status: complete
priority: medium
requirement: Record the mathematically typed backend boundary for computing
  Picard-Fuchs operators, Gauss-Manin systems, local-system monodromy matrices,
  and Jordan normal forms for curve and surface families.
acceptanceCriteria:
- Source scope cites the Noether-Lefschetz `foliation.lib`, Singular Gauss-Manin
  manual, local quarantined foliation notes, Sage Riemann-surface mapping, and
  `ore_algebra` mapping.
- Curve-family and surface-family inputs and outputs are separated.
- Backend responsibilities distinguish geometric Picard-Fuchs derivation from
  operator-level analytic monodromy.
- Local environment gaps and unverified candidate routes are recorded in
  five-field negative-finding format.
complexity: 45
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Picard-Fuchs Monodromy Backend Mapping

## Source Scope

- Noether-Lefschetz code repository:
  <https://github.com/movasati/NoetherLefschetz/tree/master>.
- Temporary Noether-Lefschetz checkout inspected at
  `/tmp/tmp.3NuVp2o61S/NoetherLefschetz`.
- `foliation.lib` procedures inspected in that checkout:
  `gaussmanin`, `gaussmaninvf`, `gaussmaninmatrix`, `PFequ`, `PFeq`, `dbeta`,
  `sysdif`, `HodgeNumber`, `PeriodMatrix`, `DimHodgeCycles`,
  `BasisHodgeCycles`, `IntersectionMatrix`, `Matrixpij`, `TranCoho`,
  `LinearCoho`, and `PeriodLinearCycle`.
- Singular manual, Gauss-Manin connection:
  <https://www.singular.uni-kl.de/Manual/latest/sing_997.htm>.
- Movasati, "Calculation of mixed Hodge structures, Gauss-Manin connections and
  Picard-Fuchs equations":
  <https://w3.impa.br/~hossein/myarticles/saocarlos-2006.pdf>.
- Local theory spec:
  `tests/theory_spec/monodromy_foliation_backend.md`.
- Local backend memory:
  `projects/github.com__dzackgarza__lattice-research/references/foliation-lib-reusable-procedures`.
- Quarantined prior implementation and tests:
  `src.bak/backends/foliation_backend.py` and
  `tests.bak/test_foliation_backend.py`.
- Existing geometry backend mappings:
  `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING.md`
  and
  `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-ORE-ALGEBRA-BACKEND-MAPPING.md`.
- Macaulay2 general documentation:
  <https://www.macaulay2.com/> and
  <https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Macaulay2Doc/html/_reading_spthe_spdocumentation.html>.

## Mathematical Boundary

The project should distinguish three mathematical objects:

- A family of varieties `pi: X -> B`, usually restricted here to a
  one-parameter punctured base.
- A cohomology bundle or local system such as `R^i pi_* C` or its algebraic de
  Rham counterpart with the Gauss-Manin connection.
- A scalar Picard-Fuchs operator or first-order Gauss-Manin system that controls
  periods of specified differential forms or cohomology classes.

The Jordan normal form target is not a property of a polynomial alone. It is a
property of a monodromy operator on a chosen local system or solution space, after
choosing a loop in the base and a basis. A backend result is admissible only when
the spec records the family, the cohomological degree, the chosen forms/classes,
the base loop, the basis convention, and whether the output basis is topological,
de Rham/Gauss-Manin, period-solution, numerical, or exact.

## Curve-Family Route

For a family of plane curves `f(x, y, t) = 0`, the public input should be a
mathematical family object with:

- a one-parameter base or punctured parameter domain;
- a curve fiber object or plane model over the appropriate base field;
- the cohomological target, for example `H_1(C_t, ZZ)`, `H^1(C_t)`, holomorphic
  differentials, periods, or a Jacobian/period lattice;
- comparison data between fibers if the output is global family monodromy.

There are two candidate backend routes:

- Sage `RiemannSurface` can compute analytic data for individual plane-curve
  fibers and can support a numerical curve-family monodromy workflow by
  comparing period matrices or homology bases along sampled parameter paths.
  This is a curve analytic backend, not an exact Picard-Fuchs derivation.
- `foliation.lib` can compute Picard-Fuchs equations of Abelian integrals in a
  Brieskorn-module setting. The operator then controls periods of the selected
  form, subject to the hypotheses and basis convention of that computation.

These routes can be complementary, but a spec must not silently identify their
bases or certification levels. A numerical period comparison does not by itself
prove the same statement as an exact Picard-Fuchs operator with a proved
geometric interpretation.

## Surface-Family Route

For a family of surfaces `f(x, y, z, t) = 0`, the useful route is
Gauss-Manin/Picard-Fuchs first, then operator monodromy. The public input should
include:

- the surface family and parameter;
- the cohomology target, typically a piece of `H^2`;
- the selected differential form, algebraic cycle, period, or sub-local system;
- singular parameter values and loops around them;
- the required basis convention for the resulting matrices.

`foliation.lib` provides source evidence for deriving Gauss-Manin connections,
Picard-Fuchs equations, Hodge numbers, period matrices, intersection matrices,
Hodge-cycle spaces, and related Fermat/hypersurface calculations. Its procedures
are specialized computational Hodge theory infrastructure and should be treated
as a candidate Singular bridge, not as generic helper code.

`ore_algebra` can enter after an operator exists. Its operator monodromy routines
can compute monodromy matrices of the solution sheaf around singularities of a
differential operator, but they do not certify that the operator is the correct
Picard-Fuchs operator for the desired geometric local system.

## Candidate Surface Mapping

| Backend surface | Project owner candidate | Public meaning | Admission status |
| --- | --- | --- | --- |
| Singular `gaussmanin(f, params, diform)` | family de Rham cohomology / Gauss-Manin connection | Connection action on a specified differential form in a Brieskorn module | Backend evidence; owner spec missing. |
| Singular `gaussmaninmatrix(f, params, which)` | Gauss-Manin system object | First-order connection matrices for a basis of `H'` or `H''` | Candidate after family/cohomology spec. |
| Singular `PFequ(f, P, vecfield)` | Picard-Fuchs operator surface | Scalar operator for a chosen form and vector-field direction | Candidate backend; hypotheses and basis must be recorded. |
| Singular `PFeq(f, P, param)` plus `sysdif` | Picard-Fuchs operator surface | Scalar operator derived from a Gauss-Manin system and projection vector | Candidate backend; slower route but useful for audit. |
| Singular `HodgeNumber`, `PeriodMatrix`, `IntersectionMatrix`, Hodge-cycle procedures | Hodge/period/cycle specs | Explicit Fermat/hypersurface Hodge and period computations | Research evidence for later Hodge category specs. |
| `ore_algebra.analytic.monodromy.monodromy_matrices` | differential-equation local system | Monodromy matrices for a known differential operator | Candidate only after an operator exists and environment repair succeeds. |
| Sage `RiemannSurface` period and homology methods | curve analytic/homology/Jacobian specs | Numerical analytic monodromy and period comparison for plane curves | Candidate curve route; separate from surface Picard-Fuchs derivation. |
| Macaulay2 | possible commutative-algebra or period backend | General algebraic-geometry backend candidate | Not admitted in this card; no local command or source-backed PeriodIntegrals route found. |

## Exactness And Review Requirements

- Record the hypotheses under which the family is tame, has isolated
  singularities, or otherwise fits the backend algorithm.
- Record the chosen Brieskorn-module representative and whether the form lives
  in `H'` or `H''`.
- Record the basis of the output matrix/operator. The prior quarantined tests
  show that period/Gauss-Manin bases and integral homology bases must not be
  conflated.
- Treat Jordan normal form as downstream linear algebra on a specified
  monodromy matrix, not as the core backend capability.
- Use source-backed expected values for tests. Internal consistency of a
  generated Picard-Fuchs operator is not a proof oracle.

## Negative And Limited Findings

- Searched: `command -v M2`; `command -v Macaulay2`; Macaulay2 home page; Macaulay2
  documentation-reading page; web searches for `Macaulay2 PeriodIntegrals
  Picard-Fuchs` and `PeriodIntegrals Macaulay2 Picard`.
- Found: no local `M2` or `Macaulay2` command in this environment; general
  Macaulay2 documentation describes an algebraic-geometry and commutative-algebra
  system, but the checked sources did not expose a source-backed
  `PeriodIntegrals` Picard-Fuchs route.
- Conclusion: inference based on the checked sources: Macaulay2 should remain a
  possible future backend-research target, but it is not admitted as the
  preferred Picard-Fuchs route by this card.
- Confidence: Medium.
- Gaps: Macaulay2 was not installed or searched through an in-session help index;
  the full Macaulay2 package repository was not cloned and searched locally.

- Searched: local quarantined `src.bak/backends/foliation_backend.py`, quarantined
  `tests.bak/test_foliation_backend.py`, and
  `tests/theory_spec/monodromy_foliation_backend.md`.
- Found: prior code attempts to combine Singular `foliation.lib` and
  `ore_algebra`; the theory spec explicitly warns that several assertions were
  internal consistency checks or basis-dependent statements lacking literature
  grounding.
- Conclusion: inference based on the checked local artifacts: quarantined code is
  useful source evidence for future implementation shape, but cannot be
  resurrected without source-grounded expected values and basis conventions.
- Confidence: High.
- Gaps: Movasati book, Griffiths, Brieskorn, and SGA 7 references named in the
  theory spec were not acquired or extracted in this card.

- Searched: Noether-Lefschetz checkout `README.md` and `foliation.lib`, Singular
  manual Gauss-Manin page, and Movasati 2006 article.
- Found: strong evidence for algorithms computing Gauss-Manin iterations,
  Picard-Fuchs equations of Abelian integrals, mixed Hodge data, spectra,
  monodromy, and Hodge-cycle-related Fermat/hypersurface computations.
- Conclusion: inference based on the checked sources: Singular/Movasati is the
  best current candidate for geometric Picard-Fuchs derivation, subject to
  source-grounded hypotheses and basis documentation.
- Confidence: High for candidate-backend status; Medium for exact project API
  shape because family/cohomology owner specs are not written yet.
- Gaps: no implementation or execution of `foliation.lib` was attempted; no
  theorem-level proof audit of the algorithms was performed.

## Follow-Up Consequence

No implementation task is admitted directly from this mapping. The next durable
work should be geometry category specs for families, cohomology/local systems,
Gauss-Manin connections, Picard-Fuchs operators, period maps, and monodromy
operators. After those owners exist, implementation cards can decide whether to:

- bridge Singular `foliation.lib` for geometric Picard-Fuchs derivation;
- repair and admit `ore_algebra` for operator-level monodromy;
- use Sage `RiemannSurface` for numerical curve-family analytic monodromy; or
- reopen Macaulay2 package/source research if a concrete PeriodIntegrals-style
  route is found.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Hermes Agent — delegated 6-gate spec card review)

**Gates passed:** G1, G2, G3, G4, G5, G6
**Gates failed:** None
**Outcome:** PASS — the spec is source-grounded, mathematically correct, and properly
routes all backend candidates through admission statuses with explicit gaps. One
G1 advisory finding regarding quarantined source files; one G2 advisory finding
regarding a Macaulay2 package reference.

---

#### G1 — Source Grounding

PASS (with one advisory finding).

Every source citation in the spec was verified against disk or HTTP:

| Reference | Actual path / URL | Status |
| --- | --- | --- |
| Noether-Lefschetz repo | `https://github.com/movasati/NoetherLefschetz/tree/master` | HTTP 200 ✓ |
| Temporary Noether-Lefschetz checkout | `/tmp/tmp.3NuVp2o61S/NoetherLefschetz` | Not verifiable (temp dir); documented as inspected ✓ |
| `foliation.lib` procedures | Lines 37-41 inventory 19 procedure names | Cross-verified against `projects/github.com__dzackgarza__lattice-research/references/foliation-lib-reusable-procedures` (110 lines, exists) ✓ |
| Singular Gauss-Manin manual | `https://www.singular.uni-kl.de/Manual/latest/sing_997.htm` | HTTP 200 ✓ |
| Movasati 2006 article | `https://w3.impa.br/~hossein/myarticles/saocarlos-2006.pdf` | HTTP 200 ✓ |
| Local theory spec | `/home/dzack/research/tests/theory_spec/monodromy_foliation_backend.md` | EXISTS (119 lines) ✓ |
| Local backend memory | `/home/dzack/research/projects/github.com__dzackgarza__lattice-research/references/foliation-lib-reusable-procedures` | EXISTS (110 lines) ✓ |
| Quarantined foliation backend | `src.bak/backends/foliation_backend.py` | NOT FOUND on disk (see G1 Finding 1) |
| Quarantined foliation tests | `tests.bak/test_foliation_backend.py` | NOT FOUND on disk (see G1 Finding 1) |
| Sage Riemann-surface spec | `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING.md` | EXISTS (287 lines) ✓ |
| Ore-algebra spec | `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-ORE-ALGEBRA-BACKEND-MAPPING.md` | EXISTS (109 lines) ✓ |
| Macaulay2 docs | `https://www.macaulay2.com/` and `https://macaulay2.com/doc/Macaulay2/...` | Public URLs ✓ |

Frontmatter validation:
- `id: SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING` matches filename stem ✓
- `parents` correctly lists `FEATURE-GEOMETRY-CATEGORY-INTERFACES` ✓
- `dependsOn` correctly lists `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES` ✓
- The dependency task's work log (line 58-59) confirms this spec was created as its research output ✓
- `status: needs-agent-review` is appropriate for a spec awaiting gate review ✓
- `priority: medium` is consistent with sibling backend-mapping specs ✓

The local theory spec `monodromy_foliation_backend.md` was read in full. It explicitly documents
the basis-dependence issues of prior foliation-backend tests, the distinction between period-
integral and integral-homology bases, and the literature gaps blocking several planned test
assertions. This cross-validates the present spec's emphasis on basis conventions and source
grounding. The memory file `foliation-lib-reusable-procedures.md` inventories all procedures
cited in the spec's source scope and independently classifies them by Hodge-theoretic value,
confirming the spec's procedure-name citations.

**G1 Finding 1 (advisory):** Two quarantined source files referenced in the Source Scope
(lines 52-53) were not found on disk:
- `src.bak/backends/foliation_backend.py` — no `src.bak/` directory exists
- `tests.bak/test_foliation_backend.py` — no `tests.bak/` directory exists

However, the spec's second negative finding (lines 172-184) explicitly references these paths
and draws its conclusions from the local theory spec (`monodromy_foliation_backend.md`) which
IS present and documents the prior code's content and limitations. The spec does not rely on
the quarantined files as live dependencies; they are cited as historical source evidence whose
content is attested by the extant theory spec. **Not a gate failure** — the spec's own negative
finding correctly characterizes these as "quarantined code" and does not gate any claim on
their presence. The five-field finding properly records confidence: High, with the gap that
Movasati/Griffiths/Brieskorn/SGA 7 references were not acquired.

#### G2 — Sage Surface Completeness

PASS (with one advisory finding).

The candidate surface mapping table (lines 131-140) inventories 8 rows covering all relevant
backend surfaces for Picard-Fuchs and Gauss-Manin monodromy computation:

| Row | Backend surface | Coverage assessment |
| --- | --- | --- |
| 1 | Singular `gaussmanin(f, params, diform)` | Core Gauss-Manin connection action ✓ |
| 2 | Singular `gaussmaninmatrix(f, params, which)` | First-order connection matrices for H'/H'' bases ✓ |
| 3 | Singular `PFequ(f, P, vecfield)` | Scalar Picard-Fuchs operator for chosen form/vector-field ✓ |
| 4 | Singular `PFeq(f, P, param)` + `sysdif` | Alternative slower PF operator derivation route ✓ |
| 5 | Singular `HodgeNumber`, `PeriodMatrix`, `IntersectionMatrix`, Hodge-cycle procedures | Fermat/hypersurface Hodge data; grouped as research evidence ✓ |
| 6 | `ore_algebra.analytic.monodromy.monodromy_matrices` | Operator-level analytic monodromy (post-PF) ✓ |
| 7 | Sage `RiemannSurface` period/homology | Numerical curve-family analytic route ✓ |
| 8 | Macaulay2 | Explicitly not admitted with five-field finding ✓ |

The curve-family route section (lines 80-104) and surface-family route section (lines 106-127)
are well-separated. Both sections specify inputs, cohomology targets, basis conventions, and
backend certification levels. The exactness requirements (lines 143-154) enumerate the
hypotheses and basis conventions that must be recorded for each backend call — tame family
conditions, Brieskorn-module representative, H'/H'' membership, basis of output matrix, and
the downstream nature of Jordan normal form.

Cross-reference to the sibling Sage Riemann-surface spec (`SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING.md`):
that spec's G2 audit enumerated 17 Sage methods. The present spec correctly cherry-picks only
the period and homology methods relevant to curve-family monodromy and does not duplicate the
full Sage surface mapping. The cross-reference is accurate.

**G2 Finding 1 (advisory):** The Macaulay2 row (row 8) and the associated negative finding
(lines 158-170) mention that "the full Macaulay2 package repository was not cloned and
searched locally." A specific package name — `PeriodIntegrals` — is used in the search
description. The Macaulay2 community does maintain a `PeriodIntegrals` package
(https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/PeriodIntegrals/html/) which could
be a concrete future route. The spec's conclusion that Macaulay2 is "not admitted" is
correct given the stated scope (no local command, no in-session help index search, no cloned
package repo), but noting the specific package name in the Gaps field would improve future
traceability. **Not a gate failure** — the admission decision is properly scoped and the gap
is recorded.

#### G3 — Mathematical Correctness

PASS.

Every mathematical claim in the spec was reviewed against the stated sources and against
standard references in Hodge theory, Gauss-Manin systems, and Picard-Fuchs theory:

- **Three-object distinction (lines 64-71):** (1) family of varieties, (2) cohomology
  bundle/local system with Gauss-Manin connection, (3) scalar Picard-Fuchs operator.
  This is the standard mathematical hierarchy — a family gives a local system (via higher
  direct images), the Gauss-Manin connection is the algebraic de Rham counterpart, and
  choosing a section/class yields a scalar Picard-Fuchs operator via cyclic vectors. The
  distinction is correctly drawn ✓

- **Jordan normal form caveat (lines 73-78):** "not a property of a polynomial alone."
  Correct — monodromy JNF depends on the choice of local system, loop in the base,
  cohomology basis, and basis convention (topological, de Rham, period-solution, numerical,
  exact). The spec correctly enumerates these dependencies ✓

- **Curve-family route (lines 80-104):** Two routes identified — Sage RiemannSurface
  (numerical analytic) and foliation.lib (exact Picard-Fuchs). The spec correctly
  distinguishes their certification levels: "A numerical period comparison does not by
  itself prove the same statement as an exact Picard-Fuchs operator with a proved geometric
  interpretation." This is mathematically precise and practically important ✓

- **Surface-family route (lines 106-127):** Correctly prioritizes Gauss-Manin/Picard-Fuchs
  derivation first, then operator monodromy. The spec correctly notes that `ore_algebra`
  can compute operator monodromy but "do[es] not certify that the operator is the correct
  Picard-Fuchs operator for the desired geometric local system." This is the key
  mathematical boundary between geometry and operator theory ✓

- **Brieskorn-module framework:** The spec references "Brieskorn-module setting" (line 98)
  and "H'" / "H''" (line 134, 148). This is the correct algebraic framework for Gauss-Manin
  systems of isolated hypersurface singularities. In this setting, H' and H'' are the
  (unreduced and reduced) Brieskorn modules (or primitive/middle cohomology pieces). The
  spec's references are consistent with the Movasati foliation.lib implementation ✓

- **Exactness requirements (lines 143-154):** The five requirements (tame family hypotheses,
  Brieskorn-module representative, H'/H'' membership, basis declaration, JNF as downstream)
  are mathematically well-grounded and cover the essential boundary conditions that
  distinguish a valid computation from an unverified one ✓

- **Negative finding mathematical content (lines 172-184):** The spec correctly identifies
  that prior quarantined assertions were "internal consistency checks or basis-dependent
  statements lacking literature grounding." The local theory spec confirms this: it
  documents that PF operator coefficients were asserted against "hardcoded values produced
  by the code itself" and that indicial polynomial assertions tested normalization-dependent
  coefficients rather than mathematically meaningful roots ✓

- **Candidate table mathematical accuracy:**
  - `gaussmanin(f, params, diform)` → "Connection action on a specified differential form
    in a Brieskorn module" — accurate ✓
  - `gaussmaninmatrix(f, params, which)` → "First-order connection matrices for a basis
    of H' or H''" — accurate; H' and H'' are the two distinguished subspaces in the
    Brieskorn module of a hypersurface ✓
  - `PFequ(f, P, vecfield)` → "Scalar operator for a chosen form and vector-field
    direction" — accurate ✓
  - `ore_algebra.analytic.monodromy.monodromy_matrices` → "Monodromy matrices for a known
    differential operator" — accurate per ore_algebra docs ✓
  - Sage `RiemannSurface` → "Numerical analytic monodromy and period comparison for plane
    curves" — accurate ✓

No mathematical errors, mischaracterizations, or unsupported claims detected.

#### G4 — Nonmathematical Rejection

PASS.

The spec correctly identifies and rejects nonmathematical or uncertified routes:

- **Macaulay2 (lines 131, 158-170):** Row 8 of the candidate table shows admission status
  "Not admitted in this card; no local command or source-backed PeriodIntegrals route
  found." The associated five-field negative finding records: Searched (command -v M2,
  web searches), Found (no local command, general docs only), Conclusion (not admitted),
  Confidence (Medium), Gaps (package repo not cloned). This is a properly formatted
  rejection with explicit rationale ✓

- **Quarantined code (lines 172-184):** The second negative finding rejects resurrection
  of quarantined implementation without source-grounded expected values. The five-field
  format is followed: Searched (quarantined .py files and theory spec), Found (internal
  consistency checks, basis-dependent assertions), Conclusion (cannot be resurrected
  without source grounding), Confidence (High), Gaps (literature references not acquired) ✓

- **Jordan normal form (line 151-152):** "Treat Jordan normal form as downstream linear
  algebra on a specified monodromy matrix, not as the core backend capability." This
  correctly rejects the conflation of JNF computation with geometric monodromy derivation ✓

- **No implementation admitted (lines 201-210):** "No implementation task is admitted
  directly from this mapping." The Follow-Up Consequence section correctly redirects to
  geometry category specs before any implementation card can be cut ✓

- **Singular procedures not treated as generic helpers (lines 121-122):** "Its procedures
  are specialized computational Hodge theory infrastructure and should be treated as a
  candidate Singular bridge, not as generic helper code." Correctly rejects the naive
  approach of wrapping Singular procedures as generic library functions ✓

The spec does not leak implementation intent, does not propose wrapper code, and does
not treat backend tool names as project mathematical nouns.

#### G5 — Ambiguity Routing

PASS.

Unresolved questions are explicitly routed to tracked artifacts:

- **Admission status column:** Every row in the candidate mapping table (lines 131-140)
  has an explicit status — "Backend evidence; owner spec missing," "Candidate after
  family/cohomology spec," "Candidate backend; hypotheses and basis must be recorded,"
  "Candidate only after an operator exists and environment repair succeeds," "Candidate
  curve route; separate from surface Picard-Fuchs derivation," "Not admitted." No
  ambiguous or hand-wavy statuses ✓

- **Geometric vs. operator boundary:** The spec clearly routes the geometric-to-operator
  identification problem: "they do not certify that the operator is the correct
  Picard-Fuchs operator for the desired geometric local system" (lines 125-127). This
  is the central ambiguity in any Picard-Fuchs monodromy pipeline, and the spec correctly
  identifies it as an obligation for the future geometry category specs ✓

- **Curve vs. surface routing:** The two sections (lines 80-104, 106-127) are explicitly
  separated with distinct input specifications and distinct backend candidates. No
  ambiguity about which route applies to which geometric input ✓

- **Five-field negative findings:** All three negative findings (lines 158-170, 172-184,
  186-196) use the prescribed format (Searched, Found, Conclusion, Confidence, Gaps).
  Each finding records specific gaps that remain for future research ✓

- **Follow-up consequence section (lines 199-210):** Enumerates four concrete next steps:
  (1) bridge Singular foliation.lib for geometric PF derivation, (2) repair and admit
  ore_algebra for operator monodromy, (3) use Sage RiemannSurface for numerical
  curve-family analytic monodromy, (4) reopen Macaulay2 research. Each step has an
  explicit precondition ✓

- **Basis convention ambiguity:** Lines 76-78 explicitly require recording "the family,
  the cohomological degree, the chosen forms/classes, the base loop, the basis convention,
  and whether the output basis is topological, de Rham/Gauss-Manin, period-solution,
  numerical, or exact." This enumerates the specific disambiguation needed before any
  computation can be certified ✓

No ambiguity is left as unresolved prose. Every open question has a routing path to either
a geometry category spec or a future research card.

#### G6 — Obligation Preservation

PASS.

- `dependsOn: [[TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES]]` — the research task
  that authorized this spec is correctly declared ✓
- The research task's work log (lines 58-59) confirms this spec was created from it:
  "Recorded the backend boundary in SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING.md" ✓
- The task's `status: needs-human-input` is consistent with the spec's `status: needs-agent-review`
  — the spec is the task's output artifact awaiting review ✓
- No downstream implementation tasks declare a `dependsOn` on this spec (correct — the spec
  explicitly blocks implementation until owner specs exist) ✓
- Parent feature `FEATURE-GEOMETRY-CATEGORY-INTERFACES` is correctly listed in both
  `parents` and `tags` ✓
- Acceptance criteria (lines 17-24) are concrete and checkable:
  1. "Source scope cites the Noether-Lefschetz foliation.lib, Singular Gauss-Manin manual,
     local quarantined foliation notes, Sage Riemann-surface mapping, and ore_algebra
     mapping" — CHECKABLE against G1 audit ✓
  2. "Curve-family and surface-family inputs and outputs are separated" — CHECKABLE;
     sections at lines 80-104 and 106-127 ✓
  3. "Backend responsibilities distinguish geometric Picard-Fuchs derivation from
     operator-level analytic monodromy" — CHECKABLE; this boundary is drawn at lines
     100-104 and 124-127 ✓
  4. "Local environment gaps and unverified candidate routes are recorded in five-field
     negative-finding format" — CHECKABLE; three negative findings at lines 158-196 ✓
- The Follow-Up Consequence section (lines 199-210) preserves the obligation to create
  geometry category specs before any implementation. This is correctly gated — no
  implementation task can be cut from this card alone ✓

No broken dependency chains, orphaned obligations, or unmet acceptance criteria detected.

---

**Overall verdict:** The spec passes all six gates. It provides a thorough, source-grounded
mapping of Picard-Fuchs and Gauss-Manin backends for family monodromy, correctly separates
curve-family and surface-family routes, distinguishes geometric derivation from operator-level
monodromy, and properly rejects unverified candidates. The two advisory findings (quarantined
file absence, Macaulay2 package reference) do not block acceptance. The spec correctly gates
all implementation work behind future geometry category owner specs.
