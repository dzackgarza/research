---
id: SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY]]'
dependsOn:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
title: Recover geometry nouns, morphisms, divisors, and Picard group surface
status: complete
priority: medium
requirement: Historical geometry nouns must be recovered as source-admitted category
  interfaces with backend ownership for schemes, varieties, morphisms, divisors, and
  Picard groups.
acceptanceCriteria:
- Variety, subvariety, morphism, curve, surface, divisor, line bundle, Picard group,
  blowup, and cover nouns have explicit owners and source grounding.
- Divisor pullback, pushforward, intersection, linear equivalence, Cartier/Q-Cartier/Weil
  predicates, and Picard group intersection matrices have backend routes.
- Blowups record centers, exceptional divisors, and induced Picard-group changes as
  maps and generators.
- Geometry specs do not assume Coble-specific outputs before the construction supplies
  them.
complexity: 80
tags:
- FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY
---
# Recover geometry nouns, morphisms, divisors, and Picard group surface

## Source Provenance

- `src.bak/varieties/varieties.py`: `Variety`, `Subvariety`, `VarietyMorphism`,
  `Curve`, `Surface`, `Divisor`, `LineBundle`, `PicardGroup`, `Blowup`, and
  `BranchedCover` abstract surfaces.
- `projects/github.com__dzackgarza__lattice-research/references/theory-backend-routing` and
  `projects/github.com__dzackgarza__lattice-research/references/software-capability-map`: Macaulay2, Singular,
  Sage, Oscar/Hecke, and commutative-algebra backend ownership for geometry methods.
- `projects/github.com__dzackgarza__lattice-research/references/abstract-to-external-mapping`: historical method
  to backend route table for varieties, curves, surfaces, divisors, Picard groups,
  covers, sheaves, and families.
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-SCHEMES-CATEGORY.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-VARIETIES-CATEGORY.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY.md`

## Contract

The recovered geometry layer must provide nouns and morphisms that make algebraic
geometry computations readable as geometry. Pullbacks, pushforwards, exceptional
divisors, Picard groups, intersection forms, canonical classes, Hilbert polynomials,
Hodge numbers, and singularity operations are methods on the relevant objects or maps,
with backend ownership recorded before implementation.

Blowups must expose the center, exceptional divisor data, induced divisor/Picard maps,
and any changes in intersection pairing as typed constructions. These are prerequisites
for later Coble work but are not themselves Coble claims.

## Owner Surface

The historical abstract classes are source material, not public API authority. The
recovered owners are mathematical category refinements:

| Noun or method family | Owner | Backend route | Notes |
| --- | --- | --- | --- |
| `Scheme`, `Spec(R)`, `Proj(S)`, `Hom(X,Y)`, points as `Spec(K)->X` | `Schemes()` and affine/projective/presented refinements | Sage schemes, Macaulay2 `Spec`/`Proj`, OSCAR schemes | A scheme is not a raw ideal or zero locus; presentations are constructors. |
| `Variety` | `Varieties(k)` as integral separated finite-type schemes over `k` | Sage presented schemes, Macaulay2/Oscar affine and projective varieties after hypothesis checks | Reducible or nonreduced algebraic sets stay under named scheme/presented refinements. |
| `Subvariety`, `singular_locus`, `smooth_locus`, `defining_ideal`, `equations` | embedded/presented scheme or variety refinements | Sage algebraic subschemes, Singular, Macaulay2 | `defining_ideal()` and equations are presentation data, not methods on all varieties. |
| `VarietyMorphism`, fibers, pullback/pushforward hooks | scheme/variety Hom surfaces | Sage scheme morphisms, backend-specific adapters | Points and rational points should route through Hom surfaces, not raw coordinate lists. |
| `Curve`, `Surface` | dimension-one and dimension-two variety refinements | Sage/Macaulay2/OSCAR under presentation hypotheses | They inherit broad invariants and add dimension-specific formulas or refinements. |
| `Divisor` | divisor objects over appropriate normal/smooth/presented scheme or variety refinements | Macaulay2 Divisor, Sage divisor surfaces where available, Singular for curve divisor computations | Weil, Cartier, and `Q`-Cartier predicates are separate surfaces. |
| `LineBundle`, `CoherentSheaf`, cohomology | sheaf category over a scheme/variety | Macaulay2 `HH`, `chi`, tangent/cotangent sheaves; Sage where available | Divisor-to-sheaf maps must be explicit. |
| `PicardGroup` | Picard group object of a scheme/variety | Sage Picard surfaces where available; Macaulay2/Oscar candidates | Picard group is not the Picard lattice. |
| Picard lattice/intersection form | smooth proper/projective surface refinements with admitted intersection pairing | Oscar/Hecke integer-lattice route after divisor basis and pairing are known | The divisor generators and maps producing the lattice must remain recoverable. |
| `blowup(center)` | scheme/noetherian or presented-scheme construction with surface-preserving refinements | Macaulay2 Schubert2 `blowup(i)`, Sage/Singular candidates | The blowup object owns center, exceptional divisor, and induced Picard maps. |
| branch/ramification cover data | finite morphism/branched-cover refinement | Sage weighted/projective constructors, Macaulay2/Singular support as audited | Cover claims must include branch divisor, ramification divisor, and canonical formulas. |

## Invariant Ownership

Global invariants such as arithmetic genus, geometric genus, Hodge numbers, Kodaira
dimension, holomorphic Euler characteristic, Hilbert polynomial, and canonical class
must be owned by the broadest source-backed scheme or variety refinement satisfying the
definition's hypotheses. Curves and surfaces may inherit these methods, add
dimension-specific formulas, and supply backend routes, but they do not own the names
merely because low-dimensional software exposes them prominently.

In particular, arithmetic genus and geometric genus are not curve-exclusive. Any
surface or higher-dimensional variety card that exposes these methods must state the
exact convention and hypotheses. Method docstrings should use the global category
diagnostic flag when a low-dimensional compatibility spelling could make users think a
curve-only formula or surface-only formula is being applied outside its hypothesis.

## Backend Routes

Implementation cards consuming this spec must record one of the software-wiring
statuses from `research-software-wiring`: `preferred-backend`, `bridge-needed`,
`candidate-backend`, `true-gap`, or `out-of-scope`.

Initial routing:

- Singular owns curve singularities, normalization, Brill-Noether/Riemann-Roch spaces,
  and polynomial solving for nodes or singular loci.
- Macaulay2 owns blowups, exceptional divisors, canonical divisors/bundles, Hilbert
  polynomials, tangent/cotangent sheaves, sheaf cohomology, and much divisor/intersection
  theory.
- Sage owns scheme orchestration, scheme morphisms, presented schemes, ambient spaces,
  and bridges into Singular or other exact backends.
- Oscar/Hecke owns integer-lattice outputs after geometry has produced the Picard
  group, divisor basis, and intersection pairing.
- No local bespoke geometry algorithm is admitted by this recovery card.

## Coble Boundary

Coble/K3 cards may depend on this geometry noun surface, but they must not shortcut it.
A later Coble construction must exhibit the rational sextic, nodes, blowup morphism,
exceptional divisors, Picard generators, cover map, branch and ramification data, and
Picard pullback before comparing a resulting lattice to a standard presentation.

## Non-Preservation Boundaries

- Do not preserve abstract methods as if they define accepted behavior without source
  and backend admission.
- Do not express Picard groups only as raw lattices; the divisor generators and maps
  that produce the lattice must be recoverable.
- Do not collapse Weil, Cartier, and `Q`-Cartier predicates.
- Do not assume a single backend owns all geometry operations.
- Do not move broad invariants such as genus, Hodge numbers, Kodaira dimension, Euler
  characteristics, or canonical data down to curves or surfaces when the source
  hypotheses are broader.
- Do not implement Picard lattices as raw matrices detached from divisor generators,
  intersection pairings, and the map from the surface to the Picard object.

## Acceptance Criteria

- [x] Each recovered noun has owner, definition source, and backend route.
- [x] Divisor and Picard operations are maps and objects, not detached matrices.
- [x] Blowup-induced Picard behavior is specified in a reusable form.
- [x] Coble-specific specs can depend on this surface without restating it.

## 6-Gate Protocol Review Log

### Gate 1: Source Grounding

| Claimed Source | Exists? | Verifiable Content? | Notes |
|---|---|---|---|
| `src.bak/varieties/varieties.py` | YES (879 lines) | YES | Contains `Variety`, `Subvariety`, `VarietyMorphism`, `Curve`, `Surface`, `Divisor`, `PicardGroup`, `Blowup`, `BranchedCover`. `LineBundle` is NOT present in this file — the spec claims it is. Minor inaccuracy. |
| `projects/github.com__dzackgarza__lattice-research/references/theory-backend-routing` | YES (65 lines) | YES | Maps abstract methods to backend tools (Macaulay2, Singular, Sage, Oscar/Hecke, etc.). Consistent with spec claims. |
| `projects/github.com__dzackgarza__lattice-research/references/software-capability-map` | YES | YES | Backend capability documentation exists. |
| `projects/github.com__dzackgarza__lattice-research/references/abstract-to-external-mapping` | YES (106 lines) | YES | Maps `Variety.blowup()` to Macaulay2 Schubert2, `Divisor.riemann_roch_space_dimension()` to Singular/Macaulay2, etc. All align with spec Owner Surface and Backend Routes. |
| `FEATURE-GEOMETRY-CATEGORY-INTERFACES.md` | YES | YES | Parent feature exists. |
| `TASK-INTEGRATE-SCHEMES-CATEGORY.md` | YES (237 lines) | YES | Status: `needs-human-input`. |
| `TASK-INTEGRATE-VARIETIES-CATEGORY.md` | YES (192 lines) | YES | Status: `needs-human-input`. Depends on schemes task. |
| `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY.md` | YES (183 lines) | YES | Status: `complete`. |

**Finding**: 7 of 8 sources are fully verifiable. One minor inaccuracy: `LineBundle` is listed in the Source Provenance as originating from `src.bak/varieties/varieties.py`, but no `LineBundle` class exists in that file (nor anywhere in `src.bak/`). The Owner Surface table correctly routes `LineBundle` under "sheaf category over a scheme/variety," and `Divisor.to_coherent_sheaf()` exists at line 442. This is a documentation discrepancy, not a mathematical error.

### Gate 2: Mathematical Correctness

**Owner Surface Table (lines 63-75)**:
- `Scheme`, `Spec(R)`, `Proj(S)`, `Hom(X,Y)`, points as `Spec(K)->X`: Correct. This is standard scheme-theoretic language (Hartshorne II.2, EGA I).
- `Variety` as "integral separated finite-type schemes over k": Correct. This matches the standard definition (Stacks Tag 01J0).
- Weil/Cartier/Q-Cartier predicates as separate surfaces: Correct. Weil divisors require normal schemes; Cartier divisors are locally principal; Q-Cartier means some integer multiple is Cartier. These are distinct concepts.
- "Picard group is not the Picard lattice": Correct. The Picard group is an abstract group Cl(X) modulo linear equivalence; the Picard lattice adds the intersection pairing on NS(X).
- `blowup(center)` owning center, exceptional divisor, and induced Picard maps: Correct. The blowup is a birational morphism σ: Bl_Z(X) → X with exceptional divisor E = σ^{-1}(Z). The induced map on Picard groups is Pic(X) ⊕ Z·[E] → Pic(Bl_Z(X)) (with appropriate relations).
- Branch/ramification cover data with branch divisor, ramification divisor, and canonical formulas: Correct. Riemann-Hurwitz: K_Y = f^*K_X + R where R is the ramification divisor. The `BranchedCover` class at line 654 implements these correctly.

**Invariant Ownership (lines 77-90)**:
- "arithmetic genus and geometric genus are not curve-exclusive": Correct. p_a(X) = (-1)^{dim X} (χ(O_X) - 1) for any projective variety. p_g(X) = dim H^{dim X}(X, O_X) for smooth varieties.
- Method docstrings should flag low-dimensional compatibility: Valid architectural guidance.

**Backend Routes (lines 92-109)**:
- Singular for curve singularities, normalization, Brill-Noether/Riemann-Roch: Aligned with Singular's `brnoeth.lib` and `resbin.lib`.
- Macaulay2 for blowups, exceptional divisors, canonical divisors, Hilbert polynomials, sheaf cohomology: Aligned with Macaulay2's Schubert2 and core packages.
- Sage for scheme orchestration: Appropriate.
- Oscar/Hecke for integer-lattice outputs: Correct — Oscar's `integer_lattice` and related facilities are the right tool.

**Coble Boundary (lines 111-116)**:
- "exhibit the rational sextic, nodes, blowup morphism, exceptional divisors, Picard generators, cover map, branch and ramification data, and Picard pullback before comparing a resulting lattice to a standard presentation": Mathematically sound. The Coble surface S is the blowup of P^2 at 10 nodes of a rational sextic, with Pic(S) ≅ I_{1,10}. The K3 double cover X → S produces a pullback lattice f^*Pic(S) ⊂ H^2(X,Z) of rank 11. This matches the source code at lines 602-651.

**Non-Preservation Boundaries (lines 118-130)**: All constraints are mathematically reasonable: Weil/Cartier/Q-Cartier must not be collapsed, Picard lattices must not be detached from divisor generators, broad invariants must not be moved down to curves/surfaces when hypotheses are broader.

### Gate 3: Architectural Consistency

- The `dependsOn` edge to `FEATURE-GEOMETRY-CATEGORY-INTERFACES` is appropriate — this spec needs scheme/variety category interfaces before its nouns can be realized.
- The `parents` edge to `FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY` is correct.
- The Coble Boundary section properly defers Coble-specific claims to downstream cards.

### Gate 4: Acceptance Criteria Status

The four acceptance criteria are marked `[x]` (complete), but the card status is `needs-agent-review`. This is inconsistent:
- `[x] Each recovered noun has owner, definition source, and backend route.` — The Owner Surface table is comprehensive. **PASS**.
- `[x] Divisor and Picard operations are maps and objects, not detached matrices.` — The source code shows `Divisor.pullback()`, `Divisor.pushforward()`, `PicardGroup.as_lattice()`. **PASS**.
- `[x] Blowup-induced Picard behavior is specified in a reusable form.` — The Blowup class has `center()` and `exceptional_divisor()`. The Owner Surface says "induced Picard maps." No explicit `induced_picard_map()` method exists in the source, but the spec requirement is met at the specification level. **PASS**.
- `[x] Coble-specific specs can depend on this surface without restating it.` — The Coble Boundary section enables this. **PASS**.

Given all criteria are substantively met, the `[x]` marks are justifiable if this review passes.

### Gate 5: Dependency Integrity

- Parent: `FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY` — verified exists.
- Depends on: `FEATURE-GEOMETRY-CATEGORY-INTERFACES` — verified exists. Its subtasks (schemes, varieties, surfaces) are in various states of completion. The surfaces task is `complete`, schemes and varieties are `needs-human-input`. This spec does not require those tasks to be complete — it defines requirements for them.

### Gate 6: Review Outcome

**Verdict**: PASS with one notation.

**Strengths**:
- Comprehensive Owner Surface table covering all key algebraic geometry nouns
- Correct mathematical definitions throughout
- Proper separation of Weil/Cartier/Q-Cartier concerns
- Clear Coble boundary specification
- Backend routing is well-grounded in existing memory files
- Non-preservation boundaries are sensible architectural guardrails

**Minor Issue**:
- `LineBundle` is listed in Source Provenance as originating from `src.bak/varieties/varieties.py` but does not exist in that file. The Owner Surface correctly routes `LineBundle` under sheaf category, and `Divisor.to_coherent_sheaf()` at line 442 provides the divisor-to-sheaf bridge. Recommendation: either remove `LineBundle` from the Source Provenance sentence, or note that it is planned but not yet present in the historical source.

**Recommendation**: Approve. The `LineBundle` discrepancy is cosmetic — the spec's own Owner Surface table correctly assigns it to the sheaf category, not the varieties module.
