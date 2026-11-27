---
id: SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY]]'
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
title: Recover exact indefinite form backend bridge contract
status: complete
priority: high
requirement: Historical Indefinite and polyhedral_common wrappers must be recovered
  as exact backend bridges with normalized matrix conventions and witness verification.
acceptanceCriteria:
- Indefinite isometry, automorphism group, orbit representative, isotropic subspace
  orbit, and stabilizer calls have documented mathematical domains.
- Backend row-action or right-action matrices are converted to the repo public action
  convention exactly once at the bridge boundary.
- Witnesses and generators are checked as lattice isometries or group elements before
  public methods return them.
- Missing binaries, unsupported signatures, and environment failures stop the backend
  call rather than silently substituting weaker evidence.
complexity: 85
tags:
- FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY
---
# Recover exact indefinite form backend bridge contract

## Source Provenance

- `src.bak/backends/external/README.md`: built binary list and limits.
- `src.bak/backends/external/py_polyhedral/binaries.py`:
  `INDEF_FORM_TestEquivalence`, `INDEF_FORM_AutomorphismGroup`,
  `INDEF_FORM_GetOrbitRepresentative`, `INDEF_FORM_GetOrbit_IsotropicKplane`,
  `INDEF_FORM_StabilizerVector`, and `INDEF_FORM_StabilizerIsotropicPlane`.
- `src.bak/backends/isometry_backend.py`: exact obstruction sequence and general
  indefinite witness branch.
- `.agents/memories/theory/backends/software-capability-map.md`: Indefinite.jl
  routing for indefinite forms, Oscar/Hecke routing for lattice invariants, and CARAT
  limitation to positive-definite or finite-matrix-group auxiliary work.
- `.agents/memories/theory-backend-routing.md`: repo method-to-backend routing and
  the warning that direct GAP-in-Sage loading of Indefinite.jl is not a drop-in route.
- `.agents/memories/theory/backends/indefinite-isometry.md`: verified upstream
  Indefinite.jl/GAP/C++ routes and local Julia 1.6.7 isolation requirement.
- `.agents/memories/theory/backends/indefinite-jl.md`: public Indefinite.jl function
  signatures and returned matrix equations.
- `.agents/memories/backend-environment-notes.md`: local `HOME` isolation needed to
  prevent the pinned Indefinite.jl GAP stack from reading the user `~/.gap` tree.

## Contract

The recovered bridge accepts exact presented form data from a public lattice or
formed-module object and calls a documented exact backend. Outputs are raw until the
public layer verifies them: an isometry witness must preserve the form and have the
claimed source/target behavior; group generators must be elements of the appropriate
Aut object; orbit representatives must be typed and verified.

The bridge owns backend conventions. If an upstream binary returns row-action matrices
or uses a right-action convention, the bridge converts them before they enter public
group semantics.

## Definition Grounding

- Mathematical object: a presented integral nondegenerate indefinite symmetric
  bilinear lattice or formed module over `ZZ`, represented to the backend by its exact
  Gram presentation.
- Public convention: matrices entering public Hom/Aut semantics use the repo's
  left-column action convention. A public automorphism generator `g in O(L)` verifies
  `g.T * gram(L) * g == gram(L)`. A public isometry witness `f: L -> M` verifies
  `f.T * gram(L) * f == gram(M)` with source and target recorded by the Hom parent.
- Backend convention: raw Indefinite.jl matrices are documented as satisfying
  `T^T Q1 T = Q2`. The historical `py_polyhedral` wrappers also record row/right-action
  conventions in stabilizer comments. The bridge must normalize whichever convention
  the selected route returns exactly once before public objects see the matrix.
- Completeness claim: a backend call is complete only for the documented exact backend
  domain. A missing binary, unsupported ring, unsupported signature, parse failure,
  Julia/GAP environment collision, or nonzero backend exit is not mathematical
  evidence; it is a bridge failure.

## Backend Routing Contract

The bridge must record the selected exact route for each operation:

| Operation family | Preferred route | Historical local route | Public owner |
| --- | --- | --- | --- |
| Indefinite form isometry | Indefinite.jl `INDEF_FORM_TestEquivalence(Q1, Q2)` | `INDEF_FORM_TestEquivalence` binary via `py_polyhedral` | formed-module Hom parent / lattice `is_isometric_to` |
| Indefinite automorphism generators | Indefinite.jl `INDEF_FORM_AutomorphismGroup(Q)` | `INDEF_FORM_AutomorphismGroup` binary | `L.Aut()` / orthogonal group |
| Norm-level orbit representatives | Indefinite.jl `INDEF_FORM_GetOrbitRepresentative(Q, norm)` | `INDEF_FORM_GetOrbitRepresentative` binary | `L.Aut().orbits(...)` or typed orbit surface |
| Isotropic k-plane and k-flag representatives | Indefinite.jl `INDEF_FORM_GetOrbit_IsotropicKplane` and `INDEF_FORM_GetOrbit_IsotropicKflag` | `INDEF_FORM_GetOrbit_IsotropicKplane` binary with `plane`/`flag` selector | orthogonal-group action on isotropic subobjects or flags |
| Vector and isotropic-subspace stabilizers | bridge-needed exact Indefinite/polyhedral route | `INDEF_FORM_StabilizerVector` and `INDEF_FORM_StabilizerIsotropicPlane` binaries | subgroup objects of `L.Aut()` |

Oscar/Hecke remains the preferred backend for lattice invariants, genera, local
conditions, discriminant groups, primitive embeddings, and centralizer images when the
operation is supported there. CARAT is not an indefinite lattice backend; it may appear
only as a positive-definite or finite-matrix-group auxiliary after the relevant group
is already known to be finite.

## Operation Contracts

### Isometry Witness

Input: two public nondegenerate indefinite integral formed objects `L` and `M` with
exact Gram presentations over `ZZ`.

Output: either no witness, or a public Hom element `f in L.Hom(M)` whose matrix has
been normalized to the public convention and verified by the Hom containment rule. The
backend matrix is not returned directly.

The historical obstruction ladder from `src.bak/backends/isometry_backend.py` is
admitted as early exact evidence, not as a proof substitute. Rank, signature,
determinant, discriminant group, discriminant-form isometry, rational isometry, local
isometry, and genus checks may reject early when source-backed and exact. If they do
not reject, the general indefinite branch must return and verify a witness before a
positive isometry result is accepted, except for a separately source-grounded theorem
branch such as the even indefinite 2-elementary Nikulin classification.

### Automorphism Generators

Input: a public nondegenerate indefinite integral formed object `L`.

Output: generators of a subgroup object of `L.Aut()` or the orthogonal group object.
Each raw generator must be normalized and checked for integrality, invertibility, parent
rank, and form preservation before it is admitted. A list of matrices is backend data
until every matrix is an element of the public Aut parent.

### Norm Orbit Representatives

Input: a public indefinite integral lattice `L` and an exact norm value in the form
codomain.

Output: typed elements of `L` or typed rational/metric-dual elements when the operation
is explicitly over an extended object. Each representative must be parent-constructed,
must have the requested norm, and must be accompanied by the backend route's
completeness claim. Exhaustive finite-window enumeration is not a replacement for the
backend orbit theorem.

### Isotropic Subspaces And Flags

Input: a public indefinite integral lattice `L`, an integer `k`, and optionally typed
subobjects or flags when testing equivalence or stabilizers.

Output: isotropic subobjects or flags with inclusion data, not row matrices. The bridge
must verify rank `k`, isotropy of the restricted form, and parent containment. For flag
operations, the nested inclusions are part of the object being stabilized or represented.

### Stabilizers

Input: a public group action by `L.Aut()` on an element, subobject, line, plane, or flag.

Output: a subgroup object with generators admitted through `L.Aut()` and verified to
fix the element pointwise or stabilize the subobject/flag setwise exactly as the public
method name states. Pointwise and setwise stabilizers are distinct surfaces; the bridge
must not blur them because a wrapper accepts a `plane`/`flag` string.

## Boundary Failures

The bridge must fail loudly at the boundary for:

- missing binary or missing Julia package;
- Julia/GAP environment collision, including the known user `~/.gap/pkg/JuliaInterface`
  conflict unless the subprocess isolates `HOME`;
- unsupported base ring, non-integral input, degenerate input where the backend
  requires nondegeneracy, or a signature outside the backend domain;
- parser failure, malformed matrix shape, rational entries where integral witnesses
  are required, or a matrix that fails public containment verification;
- backend nonzero exit, timeout, or stderr/error report.

These failures are not reasons to silently substitute Sage definite algorithms,
finite-window search, random search, or local bespoke matrix enumeration.

## Non-Preservation Boundaries

- Do not expose `run_and_check`, temporary files, or Python-literal parser details as
  part of the public contract.
- Do not make `M G M^T = G` and `G^T M G = M` both appear at call sites; normalize the
  convention at the bridge.
- Do not replace exact witness calls with finite-window enumeration.
- Do not mark an operation supported merely because a wrapper name exists; the binary
  or upstream package must be available and verified.
- Do not preserve `assert`-only validation from `py_polyhedral`; implementation work
  should raise typed backend errors and then verify public containment separately.

## Acceptance Criteria

- [x] Each backend operation records its domain, output, and completeness claim.
- [x] The spec requires raw output conversion to be centralized and tested against the
  public convention during implementation.
- [x] The spec requires public methods to verify returned witness/generator data before
  exposing it.
- [x] The spec requires unsupported or unavailable backend states to fail loudly at the
  bridge boundary.

## 6-Gate Protocol Review Log

### Review 2026-05-07 (6-Gate Spec Review)

**Gates passed:** G1, G2, G3, G4, G5, G6
**Outcome:** PASS with one notation

---

### Gate 1: Source Grounding

| Source Claimed | Exists? | Content Verified? | Notes |
|---|---|---|---|
| `src.bak/backends/external/README.md` | NO | N/A | `src.bak/` directory is absent from the repo. This path cannot be verified. |
| `src.bak/backends/external/py_polyhedral/binaries.py` | NO | N/A | Same — `src.bak/` directory absent. The claimed binaries (`INDEF_FORM_TestEquivalence`, `INDEF_FORM_AutomorphismGroup`, `INDEF_FORM_GetOrbitRepresentative`, `INDEF_FORM_GetOrbit_IsotropicKplane`, `INDEF_FORM_StabilizerVector`, `INDEF_FORM_StabilizerIsotropicPlane`) cannot be verified at this path. |
| `src.bak/backends/isometry_backend.py` | NO | N/A | Same — `src.bak/` directory absent. Historical obstruction ladder referenced in the spec cannot be verified at this location. |
| `.agents/memories/theory/backends/software-capability-map.md` | YES | YES | Line 43 confirms Indefinite.jl as preferred system for indefinite lattice isometry/orbit computations. Line 44 confirms CARAT positive-definite limitation. All spec claims about backend routing domain match this source. |
| `.agents/memories/theory-backend-routing.md` | YES | YES | Lines 14-15 confirm exact Indefinite.jl calls (`INDEF_FORM_AutomorphismGroup`, `INDEF_FORM_TestEquivalence`, `INDEF_FORM_GetOrbitRepresentative`, `INDEF_FORM_GetOrbit_IsotropicKplane`, `INDEF_FORM_GetOrbit_IsotropicKflag`). Line 57 confirms Julia 1.6.7 + isolated HOME requirement. Line 58 confirms direct GAP-in-Sage loading is not a drop-in route. All spec routing claims match. |
| `.agents/memories/theory/backends/indefinite-isometry.md` | YES | YES | Lines 117-150 confirm the working local route (Julia 1.6.7, isolated HOME, isolated `~/.gap`). Lines 97-114 confirm the GAP collision failure with `~/.gap/pkg/JuliaInterface`. Lines 166-184 confirm C++ backend exists but does not build locally. All spec environment claims verified. |
| `.agents/memories/theory/backends/indefinite-jl.md` | YES | YES | Lines 28-29 confirm `g^T * eGram * g == eGram` for automorphism. Line 57 confirms `T^T * eGram1 * T == eGram2` for isometry. Lines 175-179 confirm function reference table listing all five backend calls with exact signatures. |
| `.agents/memories/backend-environment-notes.md` | YES | YES | Lines 3-7 confirm HOME isolation is required to prevent `~/.gap/pkg/JuliaInterface` collision. Matches spec lines 160-162 exactly. |

**Gate 1 Verdict:** PASS with notation. 3 of 8 source references point to nonexistent `src.bak/` paths. These are historical provenance claims — the spec's mathematical contracts do not depend on being able to read the original `src.bak/` code, because the operation contracts are verified against the 5 existing memory files. The three dead paths are archival provenance, not current verification dependencies. The spec body's Operation Contracts, Backend Routing Contract, and Boundary Failures sections are all independently grounded in the verified sources. Notation: the `src.bak/` paths should be marked as historical/unavailable in the source provenance section to avoid misleading future reviewers.

---

### Gate 2: Contract Completeness

Each declared operation family has a documented contract with explicit input types, output types, and verification obligations:

| Operation Family | Input Specified | Output Specified | Verification Rule | Completeness |
|---|---|---|---|---|
| Isometry Witness (lines 100-115) | Yes — two public indefinite integral formed objects with exact Gram presentations over ZZ | Yes — public Hom element with normalized matrix | Yes — `f.T * gram(L) * f == gram(M)` via Hom containment | Complete |
| Automorphism Generators (lines 117-124) | Yes — public nondegenerate indefinite integral formed object | Yes — generators of subgroup of Aut(L) | Yes — integrality, invertibility, rank, form preservation per generator | Complete |
| Norm Orbit Representatives (lines 126-135) | Yes — indefinite integral lattice + exact norm value | Yes — typed elements of L or metric-dual | Yes — parent-constructed, norm-verified, completeness claim required | Complete |
| Isotropic Subspaces and Flags (lines 137-144) | Yes — lattice, integer k, optional subobjects/flags | Yes — isotropic subobjects/flags with inclusion data | Yes — rank k, isotropy, parent containment, nested inclusions for flags | Complete |
| Stabilizers (lines 146-153) | Yes — group action by Aut(L) on element/subobject | Yes — subgroup with generators in Aut(L) | Yes — pointwise/setwise distinction verified | Complete |

The Backend Routing Table (lines 84-90) maps each operation family to preferred route (Indefinite.jl), historical local route (py_polyhedral binary), and public owner (formed-module/lattice noun).

**Gate 2 Verdict:** PASS. All five operation families have complete input/output/verification contracts. No TBDs or unresolved parameters.

---

### Gate 3: Mathematical Correctness

**Contract semantics checked:**

- **Isometry convention (lines 67-70):** Public automorphism `g in O(L)` verifies `g.T * gram(L) * g == gram(L)`. Public isometry `f: L -> M` verifies `f.T * gram(L) * f == gram(M)`. These are correct left-action form-preservation equations. The transpose-gram-transpose pattern matches the standard definition of orthogonal transformations.

- **Backend convention (lines 71-73):** Indefinite.jl matrices satisfy `T^T Q1 T = Q2`. Verified at `indefinite-jl.md` line 57. This is the same left-action convention, so normalization is straightforward. The spec correctly notes that historical `py_polyhedral` wrappers may use row/right-action conventions requiring conversion.

- **Completeness claim (lines 74-78):** Correctly distinguishes between mathematical evidence (verified witness) and environmental failure (missing binary, unsupported signature, etc.). This is mathematically sound: a failure to execute a backend call is not evidence of non-isometry.

- **Historical obstruction ladder (lines 109-115):** The spec admits early exact checks (rank, signature, determinant, discriminant group, rational isometry, local isometry, genus) as fast-reject evidence but requires witness verification before positive isometry is accepted. This is correct — those invariants are necessary but not sufficient for integral isometry of indefinite forms.

- **Oscar/Hecke routing (lines 92-96):** Correctly routes lattice invariants, genera, local conditions, discriminant groups, and primitive embeddings to Oscar/Hecke, consistent with `theory-backend-routing.md` lines 13 and 55-56.

- **CARAT limitation (lines 95-97):** Correctly restricts CARAT to positive-definite or finite-matrix-group auxiliary work, consistent with `software-capability-map.md` line 44 and `theory-backend-routing.md` line 15.

- **Pointwise vs setwise stabilizers (lines 151-153):** The spec correctly distinguishes these as distinct surfaces. This is mathematically correct — pointwise and setwise stabilizers are different subgroups.

**Gate 3 Verdict:** PASS. All mathematical claims are correct when verified against the sourced definitions.

---

### Gate 4: Backend Routing Integrity

Checked the Backend Routing Contract table (lines 84-90) against all verified sources:

| Operation | Spec Claimed Preferred Route | Verified in Source? | Evidence |
|---|---|---|---|
| Indefinite form isometry | Indefinite.jl `INDEF_FORM_TestEquivalence` | YES | `theory-backend-routing.md` line 14, `indefinite-jl.md` lines 33-59 |
| Indefinite automorphism generators | Indefinite.jl `INDEF_FORM_AutomorphismGroup` | YES | `theory-backend-routing.md` line 14, `indefinite-jl.md` lines 11-29 |
| Norm-level orbit representatives | Indefinite.jl `INDEF_FORM_GetOrbitRepresentative` | YES | `theory-backend-routing.md` line 14, `indefinite-jl.md` lines 63-79 |
| Isotropic k-plane and k-flag representatives | Indefinite.jl `INDEF_FORM_GetOrbit_IsotropicKplane` and `INDEF_FORM_GetOrbit_IsotropicKflag` | YES | `theory-backend-routing.md` line 14, `indefinite-jl.md` lines 83-121 |
| Vector and isotropic-subspace stabilizers | bridge-needed exact Indefinite/polyhedral route | PARTIAL | `indefinite-jl.md` does not list `INDEF_FORM_StabilizerVector` or `INDEF_FORM_StabilizerIsotropicPlane` in its function reference (lines 171-179). These are claimed in the historical `py_polyhedral` binaries (dead path). The routing status is correctly marked as "bridge-needed" — the spec does not overclaim. |

Oscar/Hecke routing for lattice invariants confirmed at `theory-backend-routing.md` line 13. CARAT limitation confirmed at `software-capability-map.md` line 44.

**Gate 4 Verdict:** PASS. All routing claims with verified sources are accurate. The stabilizer routes are correctly marked as bridge-needed, not preferred-backend. No routing is claimed for unsupported backends.

---

### Gate 5: Boundary and Failure Handling

**Failure modes assessed (lines 157-166):**

| Failure Mode | Sound? | Evidence |
|---|---|---|
| Missing binary or Julia package | YES | `indefinite-isometry.md` lines 65-79 document dependency resolution failure on Julia 1.12 |
| Julia/GAP environment collision | YES | `indefinite-isometry.md` lines 97-114 document exact collision with `~/.gap/pkg/JuliaInterface`. `backend-environment-notes.md` lines 3-7 confirm |
| Unsupported base ring, non-integral input, degenerate input | YES | Standard mathematical domain restriction; backend requires nondegenerate integral forms |
| Parser failure, malformed matrix shape, rational entries where integral required | YES | Bridge should not silently coerce or truncate; correct discipline |
| Backend nonzero exit, timeout, stderr | YES | Standard process-failure boundary; correctly treated as bridge failure, not mathematical evidence |

**Non-Preservation Boundaries (lines 172-181):**

| Rule | Assessment |
|---|---|
| Do not expose `run_and_check`, temp files, parser details | Valid encapsulation — bridge internals are not public API |
| Normalize `M G M^T = G` vs `G^T M G = M` at bridge | Critical correctness — dual conventions must not leak |
| Do not replace exact witness calls with finite-window enumeration | Prevents cheapest-available-evidence poisoning |
| Do not mark operation supported based on wrapper name alone | Prevents phantom capability claims |
| Do not preserve `assert`-only validation from py_polyhedral | Requires typed backend errors + public containment verification |

**Gate 5 Verdict:** PASS. All failure modes are concrete and sourced. Non-preservation boundaries are sound architectural guardrails. The spec does not silently substitute weaker evidence.

---

### Gate 6: Acceptance Criteria and Self-Consistency

**Acceptance criteria status (lines 185-191):**

| Criterion | Status | Assessment |
|---|---|---|
| Each backend operation records domain, output, completeness claim | [x] | Backend Routing Contract table (lines 84-90) + Operation Contracts (lines 98-153) satisfy this |
| Raw output conversion centralized and tested against public convention | [x] | Spec requires this at lines 58-60 (bridge owns conventions) and lines 71-73 (normalize at bridge) |
| Public methods verify returned witness/generator data before exposing | [x] | Each Operation Contract (lines 100-153) includes explicit verification rules |
| Unsupported/unavailable backend states fail loudly at bridge boundary | [x] | Boundary Failures section (lines 155-168) enumerates failure modes |

All four criteria are substantively satisfied by the spec body. The `[x]` marks are appropriate.

**Internal consistency checks:**

- **Constructor ↔ Invariant alignment:** Not applicable — this is a bridge contract spec, not a lattice constructor spec.
- **dependsOn consistency:** YAML `dependsOn` lists `FEATURE-MODULES-WITH-FORMS-AND-LATTICES`. This is correct — the bridge receives formed-module/lattice objects from that feature's public API.
- **parents consistency:** YAML `parents` lists `FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY`. This is correct — the spec is a child of that feature card.
- **Parent acceptance criteria alignment:** Parent feature requires (1) explicit mathematical input/output contracts, (2) matrix action convention normalization, (3) returned data verified by public layer. The spec satisfies all three.
- **No contradictory claims:** The spec does not claim CARAT can handle indefinite forms, does not claim direct GAP loading works, and does not claim stabilizer binaries are verified — consistent with all evidence.
- **No circular definitions:** Contract definitions are grounded in independent mathematical objects (Gram presentation, orthogonal group, Hom containment).

**Gate 6 Verdict:** PASS. Acceptance criteria are met. The spec is internally consistent with no contradictions or circular dependencies.

---

### Overall Assessment

| Gate | Status |
|---|---|
| Gate 1: Source Grounding | PASS (notation: 3/8 src.bak/ paths dead, but 5/8 verified and contracts independently grounded) |
| Gate 2: Contract Completeness | PASS |
| Gate 3: Mathematical Correctness | PASS |
| Gate 4: Backend Routing Integrity | PASS |
| Gate 5: Boundary and Failure Handling | PASS |
| Gate 6: Acceptance Criteria and Self-Consistency | PASS |

**Notation:** The three `src.bak/` paths in Source Provenance (lines 31-33) are dead — the `src.bak/` directory does not exist in the current repo. This does not affect the spec's validity because all operational contracts, backend routes, and failure modes are independently grounded in the five verified memory files. Recommendation: add a note to the Source Provenance section marking the `src.bak/` references as "historical, not currently available in repo" to prevent future reviewers from flagging this repeatedly.

**Recommendation:** Approve. The spec is ready for plan authoring. The bridge contract is complete, mathematically correct, and properly scoped.
