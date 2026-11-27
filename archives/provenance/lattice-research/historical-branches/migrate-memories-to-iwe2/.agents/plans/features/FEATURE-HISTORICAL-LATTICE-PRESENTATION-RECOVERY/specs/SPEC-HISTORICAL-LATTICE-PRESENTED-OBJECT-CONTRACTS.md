---
id: SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY]]'
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
title: Recover presented lattice object and element contracts from src.bak
status: complete
priority: high
requirement: The historical presented-lattice object model must be recovered as category-correct
  presented modules with forms, not as Sage ambient lattices.
acceptanceCriteria:
- Lattice objects distinguish selected generators, Gram presentation, equality of
  presentations, and isometry by a morphism witness.
- Coordinate vectors enter a lattice only through a semantic element constructor such
  as element_from; raw vectors are not public elements.
- Dual and rational lattice objects are actual formed-module objects with explicit
  maps, not matrices masquerading as objects.
- Subobjects, spans, and primitive checks are specified through generators and morphisms
  rather than rows, ambient spans, or ad hoc coordinate helpers.
complexity: 70
tags:
- FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY
---
# Recover presented lattice object and element contracts from src.bak

## Source Provenance

- `src.bak/lattices/core/rational.py`: `RationalLattice`, `from_gram`, `dual`,
  `signature_pair`, and root Gram construction.
- `src.bak/lattices/core/integral.py`: `Lattice`, `element_from`, `dual`,
  `overlattice`, `scale`, `is_even`, and conversion between raw backend matrices and
  column-action public matrices.
- `src.bak/lattices/core/elements.py`: element coordinate conversion and primitive
  coordinate ideal check.
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`: presented object
  identity and morphism semantics.
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  parent-owned element construction, subobject/morphism discipline, and lattice API
  audit rules.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`:
  Sage-source reconciliation for `dual_lattice`, `discriminant_group`, element
  divisibility, subobjects, and formed-module method ownership.

## Contract

A recovered lattice object is a presented free bilinear module. Its public identity
contains the carrier, form data, and chosen generators. Changing generators returns a
new presented object and, when appropriate, an explicit isometry or isomorphism witness.

Elements belong to a fixed parent. A coordinate vector is not an element until the
parent constructs it through a method such as `element_from`. Element methods may expose
coordinates relative to the selected generators, but public algorithms must consume
elements and morphisms rather than free-floating vectors.

The rational, dual, and integral specializations must be expressed as category objects:
codomain extension to `Frac(R)`, dual objects, and integral promotion are mathematical
constructions with maps. A matrix may represent one of these maps after generators are
chosen, but the matrix is not the public object.

## Recovered Presented-Object Surface

The historical `Lattice.from_gram(gram, generator_names=...)` and
`RationalLattice.from_gram(gram, generator_names=...)` paths recover a constructor
from a finite selected generating set and a symmetric Gram presentation. The admitted
surface is not "a matrix is a lattice"; it is:

- a free finitely generated carrier module `M` over `R`;
- selected generators `B = (b_i)` as presentation data;
- a bilinear form `beta: M tensor_R M -> S`, where `S = R` for integral lattices and
  `S = K = Frac(R)` for rational lattices;
- `gram_matrix()` as the matrix of `beta` in the selected generators;
- `gens()`, `gen(i)`, `ngens()`, and `rank()` as presentation-owned generator access;
- `base_ring()` for `R` and `form_codomain()` or `value_ring()` for `S`.

Changing `B`, reducing a basis, canonicalizing a backend presentation, or passing
through Sage's ambient lattice model returns a new presented object. If the new object
is meant to represent the same mathematical object up to isometry, the construction
must return or record an explicit isometry witness in the formed-module Hom/Aut
surface. Equality remains presentation-sensitive; isometry is witnessed.

## Recovered Element Surface

The historical `element_from` and element classes recover the following contract:

- `L.element_from(coordinates)` is the only public conversion from coordinates in the
  selected generators to an element of `L`.
- Raw Sage vectors, rows, coordinate lists, or ambient vectors are not elements until a
  parent constructs them.
- `x.parent()`, `x.coordinates()` or `x.to_coordinates()`, and `x.to_vector()` are
  presentation readback methods, not membership substitutes.
- Element addition, subtraction, negation, and scalar multiplication are parent-local
  module operations.
- `x.b(y)` or `x.bilinear_product_with(y)` is defined only for elements in the same
  formed parent, or through an explicitly declared pairing with a dual object.
- `x.span()` constructs the subobject generated by `x` together with its inclusion
  morphism.
- `x.perp()` is shorthand for the orthogonal subobject to `x` only in a symmetric
  formed-module context; morphisms do not have perpendiculars.
- `x.divisibility()` is the ideal or submodule generated by `{beta(x, m): m in M}` in
  the form codomain. Coordinate gcds are backend witnesses only under stated
  hypotheses.
- `x.is_primitive()` for a free integral presentation is a coordinate-ideal predicate
  relative to the selected generators; primitive subobject predicates are owned by the
  inclusion or quotient surface and must not be conflated with element divisibility.

## Recovered Dual And Discriminant Surface

The recovered spec must separate three constructions that old names and Sage examples
can blur:

- `M.dual()` for a plain module is the Hom dual `Hom_R(M, R)`, an evaluation-bearing
  object in `Modules(R).DualObjects()`.
- `L.dual_lattice()` is the metric dual
  `L^# = {x in L_K : beta(x, L) subset R}` inside scalar extension to `K = Frac(R)`.
  Elements of `L^#` are not functionals by definition.
- A nondegenerate form may transport `x in L^#` to a functional
  `beta(x, -) in Hom_R(L, R)`; this is a recorded map/isomorphism under hypotheses,
  not an identity of constructions.

The historical `DualLattice` class therefore recovers the metric-dual object and its
maps, not the category-theoretic `DualObjects()` contract. Its admissible public
surface is:

- `source_lattice()` or `primal_lattice()` as provenance for the construction;
- `inclusion_morphism(): L -> L^#`;
- `element_from_primal_coordinates(...)` and `element_from_dual_coordinates(...)` as
  presentation-aware constructors;
- `primal_coordinates_of(x)` as coordinate readback for the selected presentation;
- `discriminant_class(x)` as the cokernel projection `L^# -> L^#/L`.

`L.discriminant_group()` must be the cokernel object of `L -> L^#`, with descended
quotient-valued bilinear or quadratic form data when the hypotheses hold. It is not
only a Smith-normal-form invariant package. For ordinary `v in L`, the discriminant
class is zero after inclusion into `L^#`; nonzero discriminant classes come from the
metric-dual/rational side.

Any implementation docstring for `dual_lattice()`, lattice-side `dual()` compatibility
spellings, or `discriminant_class()` must mention the global disabled-by-default
category diagnostic flag from `SPEC-MAPPING-CAT` and state when to warn about Hom-dual
versus metric-dual confusion. In particular, if a lattice compatibility spelling such
as `L.dual()` returns `L^#`, then in degenerate cases such as the isotropic rank-one
sublattice `L = <e>` of a hyperbolic plane, the docstring must say that diagnostics
should warn that `L^#` is being returned, not the evaluation-bearing Hom dual
`Hom_R(L, R)`.

## Recovered Subobject And Morphism Surface

Subobjects are generated by elements and carry inclusion morphisms. Historical row,
ambient-span, and Sage escape-hatch code is implementation evidence only. The admitted
surface is:

- `L.span(elements)` or `L.subobject_generated_by(elements)` returning a subobject with
  an inclusion morphism into `L`;
- `i: A -> B` as a formed-module morphism whose containment check owns
  form-preservation;
- `i.kernel()`, `i.image()`, and `i.cokernel()` as actual categorical objects with
  projection/lift structure where applicable;
- `B / A` only as notation for the cokernel of a recorded inclusion `A -> B`;
- `is_primitive()` for a subobject/inclusion as quotient torsion-freeness, not as a
  coordinate heuristic.

Matrices may construct morphisms through Hom parents such as `L.Hom(M).from_matrix(A)`.
They do not become public morphisms until Hom containment validates domain, codomain,
and form compatibility.

## Non-Preservation Boundaries

- Do not preserve `inner_product_matrix` as a public semantic name for indefinite
  lattices; use form or Gram vocabulary approved by the lattice specs.
- Do not preserve row-based submodule constructors. Subobjects are generated by
  elements and represented with embedding morphisms.
- Do not preserve `_sage_like` or backend escape hatches as public API.
- Do not use ambient-module membership to decide lattice element membership.

## Acceptance Criteria

- [x] The spec surface states the presented-object identity data and equality/isometry
  distinction.
- [x] Element construction and coordinate extraction are parent-owned and presentation
  explicit.
- [x] Dual/rational/integral promotion has named maps and return objects.
- [x] Any backend canonicalization that changes presentation returns a witness.

## 6-Gate Protocol Review Log

**Reviewer**: automated 6-gate spec review
**Date**: 2026-05-07
**Protocol**: Source grounding verification, mathematical correctness audit, boundary and consistency review
**Result**: PASS with advisory findings (G2 Findings 1-3). No gate failures.

### Gate 1: Source Path Existence

Every source path cited in the Source Provenance section was verified
against the on-disk working tree at `/home/dzack/research`.

| Source Claimed | Exists? | Notes |
|---|---|---|
| `src.bak/lattices/core/rational.py` | YES | Verified. Contains `RationalLattice`, `from_gram` (line 23), `dual` (line 41), `signature_pair` (line 44), `DualLattice` (line 70), root Gram construction `_neg_root_gram_qq` (line 52). |
| `src.bak/lattices/core/integral.py` | YES | Verified. Contains `Lattice` (line 29), `from_gram` (line 42), `element_from` (line 60), `dual` (inherited), `overlattice` (line 91), `scale` (line 101), `is_even` (line 107), and Sage backend conversion methods. |
| `src.bak/lattices/core/elements.py` | YES | Verified. Contains `FreeBilinearModuleElement` with `to_vector` (line 23), `to_coordinates` (line 28), `bilinear_product_with` (line 34), `span` (line 49), `perp` (line 52), `LatticeElement` with `is_primitive` (line 143), `divisibility` (line 137), and element arithmetic (lines 64-88). |
| `.agents/skills/lattice-redesign/references/category-abc-spec.md` | YES | Verified (938 lines). Contains presented-object identity and morphism semantics at lines 176-189, category hierarchy at lines 208-230. |
| `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md` | YES | Verified (1399 lines). Contains parent-owned element construction, subobject/morphism discipline, lattice API audit rules, design goals for a mathematical DSL. |
| `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md` | YES | Verified (870 lines). Sage-source reconciliation spec for dual_lattice, discriminant_group, element divisibility, subobjects, and formed-module method ownership. |

**Gate 1 Verdict**: PASS. All 6 source references are verified on-disk with exact file paths.

### Gate 2: Source Content Match

For each source, the spec's claims were checked against actual file content:

- **rational.py**: The spec claims `RationalLattice.from_gram(gram, generator_names=...)` as a constructor path. Confirmed at line 23. The `from_gram` classmethod at lines 23-29 indeed checks integrality of the Gram matrix and promotes to `Lattice` when possible, matching the spec's description of integral promotion. The `dual()` method at line 41 returns `RationalLattice(self.gram_matrix().inverse(), ...)`, confirming the matrix-inverse dual construction. `signature_pair()` at line 44 extracts `(n_+, n_-)` from `QuadraticForm.signature_vector()`, matching the spec's presentation of signature data.

- **integral.py**: The spec claims `Lattice`, `element_from`, `overlattice`, `scale`, `is_even`, and conversion between backend matrices and public matrices. Confirmed. `Lattice.__init__` at line 36 wraps `IntegralLattice(presentation.gram)` as `self._sage_lattice` (backend), while the public surface uses the presentation's Gram. `element_from` at line 60 constructs `LatticeElement` from coordinates through `IntegralCoordinatePresentation`. `is_even` at line 107 checks `b(x,x) ∈ 2R`. The dual-layer architecture (backend Sage lattice vs. public presentation) is the historical evidence for the spec's requirement that matrices are not public objects.

- **elements.py**: The spec claims element construction is parent-owned (`element_from`), raw vectors are not public elements, and element methods include `parent()`, `coordinates()`, `span()`, `perp()`, `divisibility()`, `is_primitive()`. Confirmed. `FreeBilinearModuleElement.__init__` (line 13) wraps a Sage element in the parent. `to_vector()` and `to_coordinates()` (lines 23-29) are readback methods. `span()` at line 49 delegates to `parent().span((self,))`, satisfying the subobject-by-generators contract. `is_primitive()` at line 143 uses coordinate-ideal check relative to selected generators (the spec correctly identifies this as presentation-relative). `divisibility()` at line 137 uses pairing-image ideal, matching the spec's form-codomain definition.

- **category-abc-spec.md**: The spec cites this for "presented object identity and morphism semantics." Confirmed at lines 176-189: "Morphism semantics follow the object model. A morphism of bilinear R-modules is an R-module morphism f: M1 -> M2 such that beta1(v, w) = beta2(f(v), f(w))... Matrix equations are implementation checks inside the appropriate Hom or automorphism parent, not public substitutes for morphisms." The category hierarchy at lines 208-230 confirms `Lattices(R) := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()`, matching the spec's requirement that recovered lattice objects are presented free bilinear modules, not Sage ambient lattices.

- **lattice-interface-style-guide.md**: The spec cites this for "parent-owned element construction, subobject/morphism discipline, and lattice API audit rules." Confirmed. The style guide opens with "The goal is a domain-specific language for lattice theory in algebraic geometry" (line 18) and states "The internal Sage/Julia objects are calculation engines, not the public interface" (line 69), corroborating the spec's non-preservation boundary against `_sage_like` escapes and ambient-module membership.

- **SPEC-MAPPING-LATTICES.md**: The spec cites this for "Sage-source reconciliation for dual_lattice, discriminant_group, element divisibility, subobjects, and formed-module method ownership." Confirmed. The mapping spec is the canonical tracked inventory of lattice methods, their category placement, and Sage-source mapping. It provides the authoritative source coverage ledger that the spec relies on for distinguishing Hom-dual from metric-dual, and for routing element methods to formed-module owners.

**G2 Findings (advisory)**:

1. **rational.py `dual()` is presentation-simple**: The historical `RationalLattice.dual()` at line 41 returns a new `RationalLattice` with `gram_matrix().inverse()`. This is a presentation-level inversion, not the category-theoretic `Hom_R(M, R)` dual. The spec correctly distinguishes these (lines 109-121), but the historical code does not carry explicit inclusion/evaluation maps. The spec's requirement that dual objects carry explicit maps is a strengthening of the historical surface, not a recovery of it. This is an improvement, not a defect.

2. **elements.py `is_primitive()` is coordinate-based**: The historical `LatticeElement.is_primitive()` at line 143 checks `ZZ.ideal(tuple(Integer(entry) for entry in self.to_vector())).gens()[0] == 1` — a coordinate-content check, not the quotient-torsion-freeness definition the spec requires at line 106. The spec correctly differentiates element `is_primitive()` (coordinate-ideal, presentation-relative) from subobject/inclusion `is_primitive()` (quotient torsion-freeness). The historical code conflates them, confirming the spec's boundary is well-motivated.

3. **elements.py `divisibility()` is pairing-based but principal-restricted**: The historical `LatticeElement.divisibility()` at line 137 computes `ZZ.ideal(pairings).gens()[0]` — it correctly uses pairing images (form-theoretic), not coordinate gcds, but it restricts to principal ideals. The spec's definition at line 102 ("ideal or submodule generated by {beta(x, m): m in M} in the form codomain") is more general and correct.

**Gate 2 Verdict**: PASS. The spec's claims are corroborated by the source material. The three advisory findings document improvements the spec makes over the historical code, not gaps in the spec.

### Gate 3: Mathematical Correctness — Presented-Object Surface

| Claim | Assessment | Source Evidence |
|---|---|---|
| Lattice object identity contains carrier, form data, and chosen generators | CORRECT | category-abc-spec.md lines 208-230: `Lattices(R) := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()`. The carrier is the free module, the form is the bilinear data, generators are presentation data. |
| Changing generators returns a new presented object with an isometry witness | CORRECT | category-abc-spec.md lines 176-179: "An isomorphism with this property is an isometry." The spec correctly requires a witness, not just equality of invariants. |
| `gram_matrix()` is presentation data, not an abstract invariant | CORRECT | The matrix of `beta` in the selected generators. Changing generators changes the Gram matrix; isometry (not equality) is the right equivalence. |
| `gens()`, `gen(i)`, `ngens()`, `rank()` as presentation-owned generator access | CORRECT | These are properties of the chosen generating set for the free carrier, consistent with the category-abc-spec free-module foundation. |
| `base_ring()` for `R` and `form_codomain()` or `value_ring()` for `S` | CORRECT | For integral lattices `R = S = ZZ`; for rational lattices `R = ZZ`, `S = QQ`. The distinction is mathematically necessary for the metric dual construction (lines 114-118). |
| "a matrix is not a lattice" — the admitted surface is the full presented-object structure | CORRECT | The style guide (line 69) explicitly states internal Sage objects are calculation engines, not the public interface. The category-abc-spec requires the formed-module object, not a bare Gram matrix. |

**Gate 3 Verdict**: PASS. All presented-object claims are mathematically correct and consistent with category-theoretic conventions for formed modules.

### Gate 4: Mathematical Correctness — Element, Dual, and Subobject Surfaces

**Element Surface:**

| Claim | Assessment | Notes |
|---|---|---|
| `element_from(coordinates)` is the only public conversion from coordinates | CORRECT | Ensures parent ownership; coordinates alone lack the bilinear-form context. Confirmed in source at `rational.py:31`, `integral.py:60`. |
| Raw vectors are not elements until a parent constructs them | CORRECT | category-abc-spec lines 176-179 require morphisms, not free-floating vectors. The element constructor enforces this discipline. |
| `parent()`, `coordinates()`, `to_vector()` are readback methods, not membership substitutes | CORRECT | elements.py lines 23-32. Presentation-dependent; do not define element identity. |
| Element arithmetic is parent-local module operations | CORRECT | elements.py lines 64-88: `__add__`, `__sub__`, `__neg__` all assert same parent. |
| `x.b(y)` or `x.bilinear_product_with(y)` defined only for same formed parent | CORRECT | elements.py line 35: `assert type(other) is type(self) and other.parent() is self.parent()`. |
| `x.span()` constructs subobject with inclusion morphism | CORRECT | elements.py line 49 delegates to `parent().span((self,))`. The spec requires inclusion morphism; source confirms span returns subobject. |
| `x.perp()` is orthogonal subobject shorthand, symmetric context only | CORRECT | elements.py line 52: `parent().orthogonal_submodule_to((self,))`. Correctly scoped to symmetric formed-module. |
| `x.divisibility()` is ideal/submodule of pairing images in form codomain | CORRECT | Matches elements.py line 137 pairing-based implementation. Spec's generalization to non-principal ideals (line 102) is mathematically sound. |
| `x.is_primitive()` is coordinate-ideal predicate relative to selected generators | ADVISORY | elements.py line 143 uses coordinate gcd. The spec correctly distinguishes this from subobject primitive (quotient torsion-freeness), but the historical conflation should be noted in implementation. |

**Dual and Discriminant Surface:**

| Claim | Assessment | Notes |
|---|---|---|
| `M.dual()` for plain module is `Hom_R(M, R)`, evaluation-bearing | CORRECT | Standard category-theoretic definition. The spec correctly separates this from the metric dual. |
| `L.dual_lattice()` is metric dual `L^# = {x in L_K : beta(x, L) subset R}` | CORRECT | Standard lattice-theoretic definition. Includes `inclusion_morphism(): L -> L^#`. |
| Nondegenerate form transports metric-dual elements to functionals via `beta(x, -)` | CORRECT | This is the isomorphism `L^# ≅ Hom_R(L, R)` under the nondegeneracy hypothesis. The spec correctly requires it as a recorded map, not an identity. |
| `source_lattice()` / `primal_lattice()` as provenance | CORRECT | Confirmed in rational.py line 88. |
| `inclusion_morphism(): L -> L^#` | CORRECT | rational.py line 91 returns `source.hom(self).element_from_matrix(gram)`. |
| `element_from_primal_coordinates()` and `element_from_dual_coordinates()` | CORRECT | rational.py lines 107-117. Presentation-aware constructors. |
| `primal_coordinates_of(x)` as coordinate readback | CORRECT | rational.py line 119. |
| `discriminant_class(x)` as cokernel projection `L^# -> L^#/L` | CORRECT | rational.py line 124 delegates to `discriminant_group()(element)`. |
| `discriminant_group()` is cokernel of `L -> L^#`, not just Smith-normal-form | CORRECT | The spec requires quotient-valued bilinear/quadratic form data, which is the correct mathematical structure. |
| Hom-dual vs. metric-dual warning for degenerate cases | CORRECT | The isotropic rank-one sublattice example (line 145) is mathematically sound: `Hom_R(L, R)` and `L^#` differ in degenerate cases. |

**Subobject and Morphism Surface:**

| Claim | Assessment | Notes |
|---|---|---|
| Subobjects are generated by elements and carry inclusion morphisms | CORRECT | elements.py line 49 shows span returning subobject. category-abc-spec lines 176-189 require morphisms with form compatibility. |
| `i: A -> B` as formed-module morphism with form-preservation owned by containment | CORRECT | category-abc-spec lines 183-187: "form preservation is the containment condition for the formed-module Hom object." |
| `i.kernel()`, `i.image()`, `i.cokernel()` as categorical objects | CORRECT | Standard category-theoretic definitions. The spec requires projection/lift structure. |
| `B / A` only as notation for cokernel of recorded inclusion | CORRECT | Prevents abuse of quotient notation on unrecorded subobjects. |
| `is_primitive()` for subobject/inclusion as quotient torsion-freeness | CORRECT | Mathematically correct: a submodule inclusion `A -> B` is primitive iff `B/A` is torsion-free. |
| Matrices construct morphisms through Hom parents, validated for domain/codomain/form compatibility | CORRECT | category-abc-spec lines 180-181: "Matrix equations are implementation checks inside the appropriate Hom or automorphism parent." |

**Gate 4 Verdict**: PASS. All element, dual, discriminant, and subobject claims are mathematically correct. The advisory on `is_primitive()` conflation is a well-documented boundary in the spec itself.

### Gate 5: Boundary and Non-Preservation Rules

| Rule | Assessment |
|---|---|
| Do not preserve `inner_product_matrix` as public semantic name for indefinite lattices | SOUND. The style guide (line 45) explicitly warns about the "definiteness trap" — Sage code written for definite forms may silently fail on indefinite inputs. Using form/Gram vocabulary avoids this conflation. |
| Do not preserve row-based submodule constructors | SOUND. Subobjects generated by elements with embedding morphisms are categorically cleaner. Row-based constructors are presentation-dependent and conflate coordinates with elements. |
| Do not preserve `_sage_like` or backend escape hatches as public API | SOUND. The style guide (line 69) states internal Sage objects are "calculation engines, not the public interface." The elements.py `_sage_like()` at line 20 is a private method; the spec correctly prohibits promoting it. |
| Do not use ambient-module membership to decide lattice element membership | SOUND. Lattice elements belong to a formed-module parent. Ambient membership bypasses the bilinear-form context and the presentation discipline. |
| Hom-dual vs. metric-dual diagnostic flag requirement | SOUND. The isotropic rank-one example (lines 143-147) demonstrates a real case where conflating the two would be a mathematical error. The requirement for docstring warnings and a global diagnostic flag is appropriate. |

**Gate 5 Verdict**: PASS. All boundary and non-preservation rules are mathematically sound and consistent with the project's design goals.

### Gate 6: Self-Consistency and Completeness

- **Presented-object ↔ Element coherence**: The presented-object identity (carrier + form + generators) directly supports the element surface: elements are constructed by the parent via `element_from`, coordinates are relative to the selected generators, and bilinear products require the same formed parent. No circularities.

- **Dual construction chain**: `L -> L^# -> L^#/L` (discriminant group) is a well-formed categorical chain. The spec correctly separates the metric dual from the Hom dual and requires explicit maps at each step. The discriminant group as cokernel (not just Smith-normal-form) is mathematically precise.

- **Subobject/morphism discipline**: Subobjects are generated by elements (not rows), carry inclusion morphisms (not ambient spans), and primitive checks belong to the inclusion/quotient surface (not element coordinates). This forms a closed, consistent system.

- **Acceptance criteria**: All 5 criteria are verifiable and internally consistent with the body text:
  1. Presented-object identity data and equality/isometry distinction: covered in lines 49-82.
  2. Element construction and coordinate extraction parent-owned: covered in lines 53-56, 84-107.
  3. Dual/rational/integral promotion with named maps: covered in lines 109-147.
  4. Backend canonicalization returns witness: stated at line 52, confirmed throughout the subobject/morphism surface.
  (Note: acceptance criterion 5 in the frontmatter references "Subobjects, spans, and primitive checks are specified through generators and morphisms" — covered in lines 149-167.)

- **Dependency chain**: The spec depends on `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` (parent feature providing the category infrastructure) and references `SPEC-MAPPING-LATTICES.md` (canonical Sage-source mapping). Both dependencies are satisfied.

- **No internal contradictions**: The spec consistently distinguishes:
  - Presented object vs. bare matrix
  - Element vs. coordinate vector
  - Metric dual vs. Hom dual
  - Element primitive (coordinate) vs. subobject primitive (torsion-freeness)
  - Equality (presentation-sensitive) vs. isometry (witnessed)

**Gate 6 Verdict**: PASS. The spec is internally consistent and complete. All claims are traceable to source evidence, all boundaries are explicitly drawn, and no mathematical obligations are weakened without replacement.

### Overall Assessment

| Gate | Status | Evidence |
|---|---|---|
| Gate 1: Source Path Existence | PASS | 6/6 source paths verified on-disk |
| Gate 2: Source Content Match | PASS | Spec claims corroborated by source; 3 advisory findings documenting improvements over historical code |
| Gate 3: Presented-Object Correctness | PASS | 6/6 claims mathematically correct |
| Gate 4: Element/Dual/Subobject Correctness | PASS | 25/25 claims verified; 1 advisory on `is_primitive()` conflation |
| Gate 5: Boundary Rules | PASS | 5/5 non-preservation rules sound |
| Gate 6: Self-Consistency | PASS | No internal contradictions; all acceptance criteria satisfied |

**Summary**: SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS.md is mathematically sound, source-grounded, and internally consistent. All 6 source references in the Source Provenance section are verified on-disk at correct paths. The spec correctly recovers the historical presented-lattice object model as category-correct presented modules with forms, distinguishing lattice objects (with selected generators, Gram presentation, equality of presentations, and isometry witnesses) from Sage ambient lattices (bare matrices). The spec appropriately strengthens the historical surface by requiring explicit isometry witnesses for presentation changes, explicit maps for dual/rational/integral constructions, and categorical subobject/morphism discipline. The three G2 advisory findings document areas where the historical code is less rigorous than the spec — these are improvements, not defects. No gate failures. Recommendation: advance to active implementation.
