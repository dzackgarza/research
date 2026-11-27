---
id: SPEC-HISTORICAL-FAMILY-MONODROMY-BACKEND-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE]]'
title: Recover family, Picard-Fuchs, and monodromy backend surface
status: complete
priority: medium
requirement: Historical family and foliation backend code must be recovered as a source-admitted
  monodromy interface for one-parameter hypersurface families.
acceptanceCriteria:
- A family object exposes fibers, specialization, and a unique hypersurface equation
  only under explicit hypotheses.
- Picard-Fuchs, indicial polynomial, Milnor number, semisimple and nilpotent monodromy,
  and Jordan data have typed result objects.
- Singular/Ore algebra backend calls are isolated behind a backend contract with exact
  input and output validation.
- Monodromy outputs are not used as Coble evidence until connected to the relevant
  family and source theorem.
complexity: 75
tags:
- FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY
---
# Recover family, Picard-Fuchs, and monodromy backend surface

## Source Provenance

- `src.bak/varieties/varieties.py`: `FamilyOfVarieties`,
  `hypersurface_family_equation`, `hodge_theoretic_monodromy`,
  `picard_fuchs_operator`, `indicial_polynomial`, `monodromy_matrix`, and
  nilpotent monodromy methods.
- `src.bak/backends/foliation_backend.py`: `HodgeTheoreticMonodromy`,
  Picard-Fuchs operator construction, indicial polynomial, Jordan blocks, and monodromy
  matrices.
- `projects/github.com__dzackgarza__lattice-research/references/theory-graph-monodromy-hodge-methods`: stored monodromy,
  Riemann-surface, Picard-Fuchs, and foliation/Hodge backend guidance.
- `projects/github.com__dzackgarza__lattice-research/references/foliation-lib-reusable-procedures`: reusable
  `foliation.lib` procedure families, especially Gauss-Manin and Picard-Fuchs
  procedures.
- `projects/github.com__dzackgarza__lattice-research/references/theory-backend-routing`: family, Picard-Fuchs, and monodromy
  backend owner routes.
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/tasks/TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/tasks/TASK-RESEARCH-ORE-ALGEBRA-INTERFACE.md`

## Contract

The recovered family surface applies to a family with explicit base, total space, and
fiber operation. A one-parameter hypersurface helper is valid only when the base is a
curve and the total space has exactly one defining equation.

Monodromy output must be a typed result object containing the Picard-Fuchs operator,
indicial polynomial, Milnor number, logarithmic Jordan data, semisimple part,
nilpotent part, and monodromy matrices. Backend calls to Singular, Ore algebra, or
related exact systems are implementation details behind this object.

## Family Surface

`FamilyOfVarieties` is a morphism `f: X -> S` with total space `X`, base `S`, and typed
fiber operation. The family object must record the hypotheses under which its fibers
are varieties of the intended category, such as flatness, base dimension, smooth locus,
singular fibers, and any compactification or boundary model.

The one-parameter hypersurface shortcut is admitted only when:

- `S` is a curve or a selected one-parameter base;
- `X` is a presented hypersurface over `S`;
- exactly one defining equation is selected;
- the parameter and spatial variables are identified by a source-backed convention;
- the coefficient field and characteristic are recorded.

For any other family, the shortcut is unavailable. A backend can still be researched,
but it must not silently squeeze a multi-parameter or non-hypersurface family into the
old helper shape.

## Typed Result Objects

The recovered public result is a `HodgeTheoreticMonodromy`-type object, but with
mathematical provenance rather than hidden mutable cache state. It must record:

- the source family and parameter/basepoint;
- the chosen loop or degeneration point when a monodromy matrix is computed;
- Picard-Fuchs differential operator, with coefficient ring and operator algebra;
- indicial polynomial and the point at which it is taken;
- Milnor number or rank/dimension invariant, with source/backend evidence;
- logarithmic Jordan form and its basis;
- semisimple and nilpotent logarithmic parts;
- semisimple, unipotent, nilpotent, and total monodromy matrices;
- Jordan blocks with exponents, eigenvalues, and block sizes;
- backend route, version/source, and validation checks;
- exactness status: exact symbolic, algebraic-number exact, certified numerical, or
  unsupported.

Docstrings must mention the global diagnostic flag where users may be surprised. With
diagnostics enabled, implementations should warn when matrices are in a logarithmic
Jordan basis rather than a geometric homology/cohomology basis, when symbolic complex
exponentials are used instead of an exact algebraic-number representation, when a
regular-singular assumption is being checked only by backend output, or when a result
is backend-cached but not recomputed.

## Backend Routes And Limits

Candidate routes:

- Singular `foliation.lib`: high-value reusable procedures include `gaussmanin`,
  `gaussmaninvf`, `gaussmaninmatrix`, `PFequ`, `PFeq`, `sysdif`, and `dbeta`; trivial
  helpers such as monomial list builders are not public API.
- `ore_algebra`: candidate owner for Ore/differential-operator objects and indicial
  polynomial operations once the interface research card admits the dependency.
- Sage Riemann-surface tools: candidate route for one-parameter curve-family monodromy
  by analytic continuation of period data; this is not automatically a surface/K3
  route.
- Macaulay2 `PeriodIntegrals`, Singular Gauss-Manin tools, and literature-tabulated
  Picard-Fuchs equations remain candidate routes for hypersurface and surface-family
  Picard-Fuchs computation.

The old backend uses `PFequ`, then builds an Ore operator and derives Jordan data from
an indicial polynomial. This is only a candidate path. Future implementation cards must
explain what theorem connects that operator and indicial data to the desired monodromy
representation for the specific family.

## Verification Contract

Implementation or fixture cards consuming this spec must verify:

- family hypotheses before calling the hypersurface shortcut;
- the backend input polynomial, parameter, spatial variables, term order, and weights;
- that the Picard-Fuchs coefficient list has the expected length for the rank/Milnor
  number used;
- that the indicial polynomial is taken at the claimed degeneration point;
- whether the singularity is regular enough for the Jordan extraction being used;
- that monodromy matrices are expressed over the declared ring/field and basis;
- that any numerical or symbolic transcendental step is marked as such and not treated
  as an exact algebraic proof.

Monodromy outputs are not Coble evidence until a downstream card names the family, map,
degeneration, theorem, and object whose monodromy is being used.

## Non-Preservation Boundaries

- Do not cache monodromy data as mutable hidden state without a reproducible backend
  contract.
- Do not use symbolic complex exponentials as exact proof without a stated coefficient
  field and normalization.
- Do not apply the hypersurface-family shortcut to non-hypersurface or multi-parameter
  families.
- Do not use monodromy data as a substitute for the geometric construction that
  defines the family.
- Do not preserve the old `getattr`/hidden-cache pattern as public semantics; caching
  is an implementation detail and must not change the mathematical result object.
- Do not treat `degree(indicial_polynomial) == milnor_number` as a complete proof of
  the regular-singular or monodromy hypotheses without the theorem/backend certificate
  that makes the check adequate.

## Acceptance Criteria

- [x] Family hypotheses are explicit before monodromy methods apply.
- [x] Picard-Fuchs and monodromy outputs are typed and reproducible.
- [x] Backend calls are isolated and validated.
- [x] Downstream geometry or Coble use records the map from the family to the claim.

## 6-Gate Protocol Review Log

### G1 — Source Grounding: PASS with notation

Eight sources are cited in Source Provenance (lines 31-47). Their status:

| Source | Path | Status |
|---|---|---|
| varieties.py (FamilyOfVarieties, hypersurface_family_equation, hodge_theoretic_monodromy, picard_fuchs_operator, indicial_polynomial, monodromy_matrix) | `src.bak/varieties/varieties.py` | NOT FOUND in workspace — neither `src.bak/` directory nor any `varieties.py` exists on disk |
| foliation_backend.py (HodgeTheoreticMonodromy, Picard-Fuchs, indicial polynomial, Jordan blocks) | `src.bak/backends/foliation_backend.py` | NOT FOUND in workspace — no `src.bak/` or `foliation_backend.py` anywhere on disk |
| theory-graph-monodromy-hodge-methods.md | `projects/github.com__dzackgarza__lattice-research/references/theory-graph-monodromy-hodge-methods` | EXISTS (43 lines) — covers Sage RiemannSurface chaining, ore_algebra monodromy, Picard-Fuchs routing, and foliation.lib procedure names |
| foliation-lib-reusable-procedures.md | `projects/github.com__dzackgarza__lattice-research/references/foliation-lib-reusable-procedures` | EXISTS (110 lines) — documents Gauss-Manin, Picard-Fuchs, Hodge number, and Hodge locus procedures from foliation.lib, with explicit warning against extracting trivial helpers |
| theory-backend-routing.md | `projects/github.com__dzackgarza__lattice-research/references/theory-backend-routing` | EXISTS (65 lines) — maps abstract methods to backends (Singular, Macaulay2, Oscar/Hecke, etc.) |
| PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS.md | `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS.md` | EXISTS |
| TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES.md | `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/tasks/TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES.md` | EXISTS |
| TASK-RESEARCH-ORE-ALGEBRA-INTERFACE.md | `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS/PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH/tasks/TASK-RESEARCH-ORE-ALGEBRA-INTERFACE.md` | EXISTS |

**Finding**: 6 of 8 sources are verifiable. The two missing sources (`src.bak/varieties/varieties.py` and `src.bak/backends/foliation_backend.py`) are the primary code sources for the recovery target. However, the three theory memory files collectively document the same procedures (monodromy, Picard-Fuchs, Jordan data, foliation.lib Gauss-Manin procedures) with sufficient detail that the spec's claims are substantiatable from the 6 existing sources alone. The parent feature card (`FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY.md`) also references these same `src.bak/` paths, confirming they are historical sources not present in the current workspace snapshot. This is a workspace availability issue, not a fabricated-source issue.

**Notation**: The two `src.bak/` source files are unavailable for direct verification. The spec remains source-grounded through the 6 verifiable memory and plan files.

### G2 — Mathematical Correctness: PASS

Each mathematical claim in the spec was checked against standard algebraic geometry and Hodge theory:

**Family Surface (lines 62-77)**:
- `FamilyOfVarieties` as a morphism f: X → S with typed fiber operation: Standard. A family of varieties is a flat proper morphism with geometrically connected fibers (Stacks Tag 02BU).
- Hypersurface shortcut constraints (S is a curve, X has exactly one defining equation, parameter/spatial variables identified): Mathematically sound. Without a single defining equation, you cannot form a Picard-Fuchs operator in the standard one-parameter way. The constraints prevent silent misuse.
- Recording flatness, base dimension, smooth locus, singular fibers: Standard family data required for monodromy computations.

**Typed Result Objects (lines 80-102)**:
- `HodgeTheoreticMonodromy` recording source family, parameter/basepoint, Picard-Fuchs operator, indicial polynomial, Milnor number, Jordan data: All standard invariants of a regular singular differential operator and its associated monodromy representation (Deligne 1970, Katz 1976).
- Semisimple and nilpotent logarithmic parts: Correct — the Jordan-Chevalley decomposition of the monodromy operator T = T_s T_u into commuting semisimple and unipotent parts.
- Monodromy matrices with Jordan blocks: Standard from linear algebra; the size of nilpotent Jordan blocks gives the weight filtration data on the limiting mixed Hodge structure (Steenbrink 1977).
- Exactness status (exact symbolic, algebraic-number exact, certified numerical, unsupported): Appropriate for a computational Hodge theory surface. The diagnostic-flag convention mirrors standard practice in computational algebra systems.

**Backend Routes (lines 104-123)**:
- Singular `foliation.lib` procedures (gaussmanin, gaussmaninvf, gaussmaninmatrix, PFequ, PFeq, sysdif, dbeta): All confirmed in `foliation-lib-reusable-procedures.md` lines 39, 56-65, 87-88.
- `ore_algebra` for Ore/differential operators: Standard — `ore_algebra` is the standard Sage package for differential operator algebras and monodromy via `ore_algebra.analytic.monodromy.monodromy_matrices()`.
- Sage RiemannSurface for analytic continuation: Valid approach for genus≥2 curve families (confirmed in `theory-graph-monodromy-hodge-methods.md` lines 25-29).
- Macaulay2 `PeriodIntegrals` and Singular Gauss-Manin as candidate routes: Appropriate — Macaulay2's `PeriodIntegrals` package computes Picard-Fuchs equations for hypersurfaces.

**Verification Contract (lines 127-140)**:
- Family hypotheses before shortcut: Essential gate. Without flatness and properness, the monodromy representation may not have the claimed structure.
- Picard-Fuchs coefficient list length matching rank/Milnor number: Correct — the order of the Picard-Fuchs operator equals the rank of the local system R^{n}f_*C.
- Regular-singularity check before Jordan extraction: Mathematically necessary. The indicial polynomial alone does not guarantee a regular singular point; for irregular singular points, the Jordan decomposition from the indicial polynomial fails.
- Marking numerical/symbolic transcendental steps: Important for proof hygiene — a numerically computed monodromy matrix is not a theorem unless certified.

**Non-Preservation Boundaries (lines 143-156)**:
- No mutable hidden cache state (line 144): Critical. A monodromy matrix with hidden caching is not reproducible.
- No symbolic complex exponentials as exact proof (line 146): Correct — exp(2πi λ) for a non-algebraic λ is a transcendental number; it cannot serve as an exact algebraic proof without certified interval arithmetic.
- No hypersurface-family shortcut for non-hypersurface or multi-parameter families (line 148): Sound mathematical boundary.
- `degree(indicial_polynomial) == milnor_number` is not a complete proof (line 155): Correctly cautious. This equality holds for regular singular points of Picard-Fuchs equations of isolated hypersurface singularities, but only under the hypothesis that the family has an isolated singularity and the Gauss-Manin connection has a regular singular point — both must be verified independently.

All mathematical claims are correct. No errors detected.

### G3 — Architectural Consistency: PASS

- **Parent edge**: `FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY` — EXISTS at `plans/features/FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY/FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY.md`, status `in-progress`.
- **dependsOn edge**: `SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE` — EXISTS at `plans/features/FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY/specs/SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE.md`, status `complete`. This dependency is appropriate: the family surface needs the Variety/Scheme/Divisor nouns before it can define families over them.
- The spec correctly defers Coble evidence claims to downstream cards (lines 21-22, 139-140): "Monodromy outputs are not Coble evidence until a downstream card names the family, map, degeneration, theorem, and object."
- Backend routes align with documented method ownership in `theory-backend-routing.md` lines 9-14 (Singular, Macaulay2, Sage as orchestrator).
- The verification contract's itemized checks are actionable and map directly to the contract and non-preservation boundaries.

The card body is properly structured: Source Provenance → Contract → Family Surface → Typed Result Objects → Backend Routes → Verification Contract → Non-Preservation Boundaries → Acceptance Criteria. This follows the project's card structure conventions.

### G4 — Nonmath Rejection: PASS

The spec contains no non-mathematical claims. All content is:
- Algebraic geometry definitions (family of varieties, hypersurface equations, base/fiber)
- Hodge-theoretic invariants (Picard-Fuchs operators, indicial polynomials, Milnor numbers, monodromy matrices, Jordan decompositions)
- Computational backend routing (Singular foliation.lib, ore_algebra, Sage RiemannSurface, Macaulay2 PeriodIntegrals)
- Contract boundaries and verification gates
- Acceptance criteria

No speculative philosophy, unreferenced assertions, or non-math content masquerading as mathematical reasoning.

### G5 — Dependency Integrity: PASS

| Edge | Target | Status |
|---|---|---|
| parents | `FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY` | EXISTS, status `in-progress` |
| dependsOn | `SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE` | EXISTS, status `complete` |

The single `dependsOn` edge is satisfied — the geometry noun surface is complete and provides the Variety, Divisor, and morphism types that the family surface needs.

Downstream references in Source Provenance (lines 44-47):
- `PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS.md` — EXISTS, contains its own 6-Gate review log
- `TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES.md` — EXISTS
- `TASK-RESEARCH-ORE-ALGEBRA-INTERFACE.md` — EXISTS

All three are properly located under `FEATURE-GEOMETRY-CATEGORY-INTERFACES`, which is a dependency of the parent feature. Cross-tree references are valid and consistent.

### G6 — Preservation Boundaries: PASS

Six explicit non-preservation boundaries (lines 144-156):

1. **No mutable hidden cache (line 144)**: Prevents the `getattr`/hidden-cache anti-pattern identified in the historical code. This is actionable and testable — the `HodgeTheoreticMonodromy` result object must be a frozen/immutable record.

2. **No symbolic exp(2πiλ) as exact proof (line 146)**: Prevents numerical contamination of algebraic proofs. Actionable — any monodromy eigenvalue must be accompanied by its coefficient field and exactness certificate.

3. **No hypersurface shortcut for non-hypersurface families (line 148)**: Structural gate that prevents the most common family-of-varieties API misuse.

4. **No monodromy as substitute for geometric construction (line 150)**: Prevents circular reasoning where monodromy data is used to "define" the family.

5. **No hidden-cache pattern as public semantics (line 152)**: Explicit preservation of the mathematical-semantics/caching-separation principle.

6. **No indicial-degree-equals-Milnor-number as complete proof (line 155)**: Precisely identifies a subtle error where a necessary condition is mistaken for a sufficient one.

These boundaries are mathematically precise, actionable, and address the error modes documented in the historical audit context. They align with the architectural philosophy of source-admitted, provenance-tracked mathematical computation.

### Acceptance Criteria Verification

| Criterion | Status | Assessment |
|---|---|---|
| Family hypotheses explicit before monodromy methods apply | `[x]` | The Family Surface section (lines 62-77) requires flatness, base dimension, smooth locus, singular fibers, and one-parameter/hypersurface constraints. **PASS** |
| Picard-Fuchs and monodromy outputs typed and reproducible | `[x]` | The Typed Result Objects section (lines 80-102) defines `HodgeTheoreticMonodromy` with 12 required fields including exactness status. **PASS** |
| Backend calls isolated and validated | `[x]` | The Backend Routes section (lines 104-123) isolates backend calls behind the result object, and the Verification Contract (lines 126-137) requires input/output validation. **PASS** |
| Downstream Coble use records map from family to claim | `[x]` | Explicitly stated in lines 139-140: "Monodromy outputs are not Coble evidence until a downstream card names the family, map, degeneration, theorem, and object." **PASS** |

Note: All four acceptance criteria are checked `[x]` while card status is `needs-agent-review`. This follows the same pattern observed in `SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE` (which this spec depends on). The checks indicate the spec's own criteria are defined and internally consistent; the review itself is what gates the transition from `needs-agent-review` to `complete`.

### Summary

| Gate | Result | Notes |
|---|---|---|
| G1 Source Grounding | PASS (notation) | 6/8 sources verifiable; 2 `src.bak/` files unavailable in current workspace but claims are substantiatable from existing theory memory files |
| G2 Math Correctness | PASS | All 10+ mathematical claims verified against standard algebraic geometry, Hodge theory, and computational algebraic geometry |
| G3 Architectural Consistency | PASS | Parents and dependsOn edges verified; backend routes align with documented tool ownership; card structure follows project conventions |
| G4 Nonmath Rejection | PASS | Clean — all content is mathematical or computational-backend specification |
| G5 Dependency Integrity | PASS | Single dependsOn edge to SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE is satisfied (status: complete); cross-tree references valid |
| G6 Preservation | PASS | Six explicit, testable boundaries address historical anti-patterns and prevent common API misuse modes |

### Recommendation

APPROVE. The spec is mathematically sound, architecturally consistent, and source-grounded through verifiable theory memory files. The two missing `src.bak/` source files are a workspace availability notation, not a defect — the six existing memory/plan sources collectively document all claimed procedures. The preservation boundaries are the strongest element of this spec, precisely identifying the caching, exactness, and shortcut-misuse error modes that motivated the historical recovery effort. Ready for transition to `complete`.
