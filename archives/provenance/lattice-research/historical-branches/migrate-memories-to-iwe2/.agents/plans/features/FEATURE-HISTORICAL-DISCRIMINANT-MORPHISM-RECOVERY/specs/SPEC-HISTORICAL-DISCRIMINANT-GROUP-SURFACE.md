---
id: SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS]]'
title: Define the discriminant group as a finite torsion formed module
status: complete
priority: high
requirement: For a nondegenerate integral lattice L, define A_L = L#/L as a finite
  torsion formed-module quotient with explicit bilinear and quadratic structure.
acceptanceCriteria:
- A discriminant object constructed from a lattice records the source lattice, dual
  inclusion, quotient map, and descended form data.
- q and b evaluation, generators, cardinality, invariant factors, p-elementary checks,
  finite iteration, submodules, quotients, and orthogonal submodules are defined on
  the discriminant object or its category.
- Orthogonal groups of discriminant forms are Aut objects of the finite formed-module
  object, not raw Sage groups.
- Equality, isomorphism as groups, and isometry as forms are distinct public predicates.
complexity: 70
tags:
- FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY
---
# Define the Discriminant Group as a Finite Torsion Formed Module

## Source Provenance

- `category_specs/lattices/subcategories/constructions/discriminant_groups.py`: `DiscriminantGroup`, `DiscriminantGroupElement` abstract method obligations (active category-spec file)
- Sage 10.7 `sage/modules/torsion_quadratic_module.py`: `TorsionQuadraticModule` with `q`, `b`, `is_p_elementary`, `submodule`, `orthogonal_submodule_to`, `orthogonal_group` methods providing Sage source evidence
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`: quotient-valued
  torsion bilinear and quadratic module semantics.
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  discriminant dual distinction, quotient codomain rules, comparison-predicate
  placement, and validation rules for invariant-factor presentations.
- `projects/github.com__dzackgarza__lattice-research/context/bilinear-form-category-semantics`: `A_L = L^#/L` as a
  cokernel with coefficient-module data, not a matrix shortcut.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`:
  mapping rows for `discriminant_group`, torsion quadratic modules, quotient-valued
  form data, `is_p_elementary`, `normal_form`, `brown_invariant`, and discriminant
  Hom/End/Aut standard names.

## Contract

For a nondegenerate integral lattice `L`, the discriminant object is the finite torsion
module obtained from the dual inclusion together with descended quotient-valued form
data. The public object must expose the torsion carrier and the form as mathematical
structure, not as a Sage torsion module escape hatch.

The operations recovered from the old code must be defined with distinct meanings:
group invariants classify the underlying finite abelian group; form isometry classifies
the quotient-valued formed object; automorphisms are form-preserving automorphisms in
the discriminant category.

## Discriminant Construction

For an integral nondegenerate lattice `L`, the primary constructor is the categorical
discriminant descent:

```text
L  --i-->  L^#  --pi-->  A_L := coker(i).
```

The public discriminant object must record:

- `source_lattice()` or `lattice()` when the object is constructed from a lattice;
- the metric dual object `L^# = L.dual_lattice()`;
- `inclusion_morphism(): L -> L^#`;
- the quotient projection `pi: L^# -> A_L`;
- the underlying finite torsion module;
- the bilinear form `b_A: A_L tensor A_L -> K/R`;
- the quadratic refinement `q_A: A_L -> K/2R` when the source form and parity
  hypotheses make it descend.

The historical `from_invariants_and_gram(invariants, gram, modulus, quadratic_modulus)`
path is defined only as a constructor for a finite torsion formed module with explicit
quotient codomain data. It is not a replacement definition for `L.discriminant_group()`.
It must validate rank agreement, positive invariant factors, symmetry of the bilinear
or quadratic data, and the integrality compatibility `d_i*d_j*gram[i,j] in R` for the
chosen generator presentation.

## Torsion Module and Form Operations

The discriminant parent provides the finite torsion carrier and quotient-valued form data:

- `gens()`, `ngens()`, `invariants()`, `smith_form_gens()`, and `cardinality()` are
  finite torsion module operations.
- `zero()`, `__iter__()`, and finite listing/enumeration are defined because the
  carrier is finite; they must not become proof substitutes outside finite contexts.
- `gram_matrix_bilinear()` and `gram_matrix_quadratic()` are quotient-valued form
  presentation data, distinct from free-lattice Gram matrices.
- `b(x, y)` returns a value in `K/R`; `q(x)` returns a value in `K/2R` when quadratic
  data is present.
- `is_p_elementary(p)` is a finite torsion module predicate. `delta`, `coparity`, and
  `(r, a, delta)` are lattice theorem-context invariants, not discriminant-object
  methods.

Element operations are parent-local:

- `A.element_from(coordinates)` or `A(value)` constructs a discriminant element from
  coordinates in the selected finite generator presentation.
- `x.vector()` or coordinate readback is presentation data.
- `x.lift()` is public only when it returns an element of the recorded metric dual or
  rational source object; a bare Sage lift is interop/private.
- `x.q()`, `x.b(y)`, `x.is_isotropic()`, and `x.additive_order()` are element methods
  routed through the parent form and torsion module.

## Subobjects, Quotients, and Comparisons

Discriminant subobjects are finite torsion formed submodules, not raw lists of Sage
generators:

- `A.submodule(generators)` constructs a subobject with inclusion into `A`.
- `A.orthogonal_submodule_to(B)` requires `B` as a subobject or discriminant subgroup
  with parent data, and returns the orthogonal subobject for the quotient-valued
  bilinear form.
- `A / B` is defined only as the quotient/cokernel of the recorded inclusion
  `B -> A`, with descended form data when it exists.
- `primary_part(p)` is defined for prime-power primary decomposition; composite
  selectors require an explicit decomposition rule.

Comparison predicates must stay separated:

- `A == B` means equal presented discriminant formed objects, or a canonical equality
  criterion explicitly recorded by the implementation.
- `A.isomorphic_as_groups(B)` compares only the underlying finite abelian groups, for
  example via invariant factors.
- `A.is_isometric_to(B)` compares quotient-valued formed objects and must include the
  codomain data (`K/R` versus `K/2R`) and form values, not only the group invariants.
- `normal_form()` is implementation evidence for isometry only after its hypotheses and
  quotient codomain are stated.

## Hom, End, and Aut Objects

The discriminant Hom/End/Aut objects are the standard finite torsion formed-module
Hom, endomorphism, and automorphism objects:

- `A.Hom(B)` is the parent of discriminant morphisms `A -> B`.
- Hom constructors may accept generator images, dictionaries, callables, or matrices
  only through named Hom-parent constructors such as `from_images(...)` or
  `from_matrix(...)`.
- A morphism element has `kernel()`, `image()`, `cokernel()`, `lift()`,
  `is_injective()`, `is_surjective()`, `is_bijective()`, and `is_isomorphism()`.
- `A.End()` and `A.Aut()` are the endomorphism and automorphism parents; orthogonal
  groups are `Aut` objects in the discriminant formed-module category.
- Raw Sage automorphism groups and matrices are implementation witnesses or constructor
  inputs; they are not public automorphism elements until containment in `A.Aut()` has
  validated the torsion module and form preservation.

## Non-Preservation Boundaries

- Do not identify the group and form notions merely because the old code used one
  class for both.
- Do not expose Sage element classes, normal forms, or private modulus fields as public
  semantics.
- Do not treat `delta` or coparity as defined on the discriminant group when the current
  correction source says they are lattice invariants.
- Do not use iteration over all elements as proof of a general theorem unless the
  finite carrier and exhaustive enumeration are part of the stated contract.

## Acceptance Criteria

- [x] The source lattice, dual map, quotient map, and descended form data are explicit.
- [x] Group-level and form-level comparison predicates are separate.
- [x] Orthogonal-group access is routed through the standard Hom/End/Aut hierarchy.
- [x] Backend finite-torsion calls are encapsulated behind the discriminant noun.

## Source Review Log

**Review Date:** 2026-05-07
**Reviewer:** Hermes Agent (subagent, source review protocol)
**Spec ID:** SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE
**Spec Status Before Review:** needs-agent-review
**Spec Status After Review:** needs-revision (G1 source-grounding gap; G4 false-positive risk)

---

### Check 1 — Source Grounding

**Claim:** The spec cites 5 source references for provenance.

**Verified references (4/5 exist and are consistent):**

| Reference | Status | Verification |
|---|---|---|
| `.agents/skills/lattice-redesign/references/category-abc-spec.md` | EXISTS | Read; confirms quotient-valued torsion bilinear/quadratic module semantics in sections covering discriminant descent and cokernel form data. Consistent with spec contract. |
| `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md` | EXISTS | Read; confirms discriminant dual distinction, quotient codomain rules, comparison-predicate placement, and invariant-factor validation. Consistent. |
| `projects/github.com__dzackgarza__lattice-research/context/bilinear-form-category-semantics` | EXISTS | Read; confirms `A_L = L^#/L` as cokernel with coefficient-module data, not a matrix shortcut (line 15). Explicitly states `DiscriminantGroup/Form` represents torsion quadratic/bilinear module `L^#/L` (line 24). Consistent. |
| `SPEC-MAPPING-LATTICES.md` | EXISTS | Read; confirms mapping rows for `discriminant_group`, torsion quadratic modules, quotient-valued form data, `is_p_elementary`, `normal_form`, `brown_invariant`, and discriminant Hom/End/Aut standard names. The Torsion and Discriminant-Form Reconciliation table (lines 165-178) maps Sage `TorsionQuadraticModule` methods to the weakest categories that match this spec's claims. Consistent. |

**FAILED reference (1/5 does not exist):**

| Reference | Status | Detail |
|---|---|---|
| `src.bak/lattices/core/discriminant.py` | NOT FOUND | No file at this path. No `src.bak/` directory exists anywhere in the workspace. The active discriminant-group category spec lives at `category_specs/lattices/subcategories/constructions/discriminant_groups.py`, which was verified. The `SPEC-MAPPING-LATTICES.md` formal-negative-findings section (line 182-202) documents that old source material was migrated from `theory/spec_backups/` to `.agents/theory/spec-backups/lattices_written_spec_backup.py`, and that old `src/lattices/` paths are stale. However, none of these migrated paths contain a file named `discriminant.py` or a `DiscriminantGroup` class matching the spec's listing of methods: `DiscriminantGroup`, `DiscriminantGroupElement`, `from_invariants_and_gram`, `from_lattice`, `q`, `b`, `is_p_elementary`, `isomorphic_as_groups`, `is_isometric_to`, `submodule`, `orthogonal_submodule_to`, `orthogonal_group`. |

**G1 Finding:** The spec's primary source provenance (`src.bak/lattices/core/discriminant.py`) is unresolvable in the current workspace. The spec claims to recover methods from that file (line 31-34) but the file cannot be inspected to verify which methods existed, what their signatures were, or whether the recovered obligations are faithful to the historical code. The active category-spec file (`discriminant_groups.py`) provides abstract method stubs but no concrete implementation of the listed methods.

**G1 Recommendation:** Either (a) locate and attach the historical `discriminant.py` source as a tracked backup, or (b) replace the `src.bak` reference with the active category-spec file and the Sage 10.7 `torsion_quadratic_module.py` as the actual source ground. The latter is preferable since MAPPING.md already documents the Sage-to-spec mapping and the category-spec file is the authoritative active definition.

---

### Check 2 — Sage Method Coverage

**Claim:** The spec recovers discriminant group operations covering generators, cardinality, invariant factors, p-elementary checks, finite iteration, submodules, quotients, orthogonal submodules, form evaluation, and orthogonal groups.

**Coverage against Sage 10.7 `TorsionQuadraticModule` and active `discriminant_groups.py`:**

| Surface Element | In Spec? | In Sage? | In category-spec? | Notes |
|---|---|---|---|---|
| `q(x)`, `b(x,y)` element methods | Yes (lines 96-97, 109) | Yes (`torsion_quadratic_module.py:121,154`) | ElementMethods stub | Spec is consistent |
| `gens()`, `ngens()`, `invariants()`, `smith_form_gens()`, `cardinality()` | Yes (line 90-91) | Yes (via FGP_Module) | `invariants` abstract; others inherited | Covered |
| `zero()`, `__iter__()`, finite enumeration | Yes (line 92-93) | Yes (via FGP_Module) | Not explicit; inherited | Covered |
| `gram_matrix_bilinear()`, `gram_matrix_quadratic()` | Yes (line 94-95) | Yes (`torsion_quadratic_module.py:457,487`) | Abstract methods present | Covered |
| `is_p_elementary(p)` | Yes (line 98) | Yes (via Sage) | Not explicit | Covered by spec |
| `element_from(coordinates)`, `vector()`, `lift()` | Yes (lines 104-108) | Yes (FGP_Element) | `lift` abstract; others inherited | Covered |
| `additive_order(x)` | Yes (line 109) | Yes | Abstract method present | Covered |
| `submodule(generators)` | Yes (line 117) | Yes (`torsion_quadratic_module.py:363,1113`) | Not explicit | Covered by spec |
| `orthogonal_submodule_to(B)` | Yes (line 118-120) | Yes (`torsion_quadratic_module.py:890`) | Not explicit | Covered by spec |
| Quotient `A / B` | Yes (line 121-122) | Partial (Sage has cokernel machinery) | Not explicit | Covered by spec |
| `primary_part(p)` | Yes (line 123-124) | Yes (`torsion_quadratic_module.py:1149`) | `all_submodules` abstract; `primary_part` not explicit | Covered |
| Equality, `isomorphic_as_groups`, `is_isometric_to` | Yes (lines 128-133) | Partial in Sage | Not explicit | Covered by spec; Sage gap acknowledged |
| `normal_form()`, `brown_invariant()` | Mentioned (lines 44, 133-135) | Yes (`torsion_quadratic_module.py:408,939`) | `brown_invariant` abstract; `normal_form` not explicit | Acknowledged but not fully owned in spec body |
| `Hom(B)`, `End()`, `Aut()` morphism objects | Yes (lines 137-152) | Partial in Sage | Uses standard `ModulesHom/End/Aut` | Covered; Sage gap for cokernel with descended form noted |
| `source_lattice()`, `inclusion_morphism()`, quotient projection | Yes (lines 70-74) | Not in Sage directly | Not explicit | Project-owned construction data; correctly specified |
| `from_invariants_and_gram(...)` | Yes (lines 79-84) | `TorsionQuadraticForm(q)` exists but different path | Not explicit | Spec correctly includes this as an explicit-data constructor |

**Sage methods not explicitly addressed in spec:**

| Missing Surface | Sage Location | Risk |
|---|---|---|
| `value_module()` / `value_module_qf()` | `torsion_quadratic_module.py:1251,1271` | Low — these are quotient codomain accessors; spec references `K/R` and `K/2R` codomains throughout |
| `all_submodules()` | `torsion_quadratic_module.py` | Low — present in category-spec as abstract method; spec mentions finite iteration |
| `genus(signature_pair)`, `is_genus(...)` | `torsion_quadratic_module.py:539,743` | Acceptable — these are lattice-level theorem methods, not discriminant-group-owned (MAPPING.md line 173 confirms) |
| `twist(s)` | `torsion_quadratic_module.py:1207` | Low — form scaling; not core discriminant operation |
| `discriminant_action()` and related bridge methods | `torsion_quadratic_module.py:856` | Acceptable — these are lattice Aut methods, correctly excluded as non-discriminant-group-owned in spec line 98-100 |

**G2 Finding:** The spec covers the core discriminant-group Sage methods comprehensively. Three minor Sage methods (`value_module`, `value_module_qf`, `all_submodules`) are omitted from explicit spec text but are present in the active category-spec abstract methods and are implied by the codomain and finite-carrier discussions. The lattice-level comparison methods (`genus`, `discriminant_action`) are correctly excluded. No Sage method is incorrectly claimed or contradicted.

**G2 Recommendation:** Consider adding explicit mention of `value_module()` and `value_module_qf()` as quotient-codomain accessors, consistent with the spec's emphasis on `K/R` and `K/2R` codomains.

---

### Check 3 — Mathematical Correctness

**Claim verification against standard lattice theory (Nikulin, Miranda-Morrison, etc.):**

| Mathematical Claim | Location | Verdict | Evidence |
|---|---|---|---|
| `A_L = coker(L -> L^#)` as finite torsion module | Lines 62-66 | CORRECT | Standard definition; confirmed by `bilinear-form-category-semantics.md` line 15 and `category-abc-spec.md` discriminant descent sections |
| Bilinear form `b_A: A_L × A_L → K/R` | Line 75 | CORRECT | Standard quotient-valued bilinear form on discriminant group |
| Quadratic refinement `q_A: A_L → K/2R` | Lines 76-77 | CORRECT | Standard; requires parity hypotheses for descent (spec acknowledges this) |
| `from_invariants_and_gram` compatibility: `d_i * d_j * gram[i,j] ∈ R` | Line 84 | CORRECT | This is exactly the well-definedness condition for a bilinear form on a finite abelian group given by invariant factors `d_i` |
| Separation of group isomorphism vs form isometry | Lines 128-133 | CORRECT | Finite abelian group classification by invariant factors is strictly coarser than isometry classification of formed modules |
| Orthogonal group = Aut in formed-module category | Lines 148-152 | CORRECT | `O(A_L, q) = Aut(A_L, q)` as form-preserving automorphisms |
| `delta`, `coparity`, `(r,a,delta)` are lattice invariants, not discriminant-group methods | Lines 98-100, 160-161 | CORRECT | These are invariants of the lattice (rank, even/odd type, determinant), not of the discriminant group alone |
| `primary_part(p)` for prime-power decomposition | Lines 123-124 | CORRECT | Standard primary decomposition of finite abelian groups; composite selectors need explicit rule |
| `A / B` as cokernel of inclusion with descended form | Lines 121-122 | CORRECT | The quotient of a torsion formed submodule carries a descended form when the submodule is isotropic for the bilinear form; spec correctly requires `B -> A` inclusion data |
| Element `lift()` returns element of metric dual or rational source | Lines 107-108 | CORRECT | A discriminant element lifts to `L^#`, not to an arbitrary ambient vector space |
| `is_isotropic()` on elements | Line 109 | CORRECT | Standard: `q(x) = 0` in quotient codomain |
| Finite iteration caveat | Lines 92-93 | CORRECT | Finite carrier enumeration is valid; spec correctly warns against using it as proof substitute |

**Edge cases and hypotheses checked:**

- **Parity hypotheses for quadratic descent (line 76-77):** The spec correctly notes that `q_A` descends only when source form and parity hypotheses allow it. This is mathematically precise: for an even lattice, the bilinear form descends to `Q/Z` and the quadratic form to `Q/2Z`; for odd lattices the quadratic form on the discriminant group may not be well-defined without additional choices.
- **Nondegeneracy requirement:** The spec's contract (line 49) states "nondegenerate integral lattice L" — this is the correct hypothesis for `L^#/L` to be finite.
- **Symmetric bilinear form:** Implicit throughout; the descent from symmetric form on L to symmetric bilinear form on `A_L` is standard.
- **Coefficient ring scope:** Spec uses generic `R`/`K` language; the actual Sage implementation targets `ZZ`/`QQ`. This is acceptable generalization.

**G3 Finding:** All core mathematical claims are correct under standard lattice theory. The spec correctly distinguishes group-level from form-level invariants, correctly identifies the cokernel construction, correctly handles parity hypotheses, and correctly separates lattice-level invariants from discriminant-group-owned methods. No mathematical errors detected.

---

### Check 4 — Nonmathematical Rejection

**Items that should be rejected or reclassified as implementation details:**

| Item | Location | Classification | Action |
|---|---|---|---|
| "Raw Sage automorphism groups and matrices are backend witnesses" | Lines 150-152 | Already correctly classified as non-public | KEEP — Spec explicitly rejects exposing raw Sage groups as public API |
| "Sage element classes, normal forms, or private modulus fields" | Lines 158-159 | Already correctly classified | KEEP — Non-Preservation Boundaries section correctly rejects these |
| `delta` and `coparity` as discriminant-group methods | Lines 98-100 | Already correctly classified as lattice invariants | KEEP — Correctly owned by lattice, not discriminant group |
| Iteration-as-proof warning | Lines 162-163 | Already correctly classified | KEEP — Valid caveat |
| Sage `ambient`, `basis`, `inner_product_matrix` triple | Line 112 (MAPPING cross-ref) | Not in this spec but implicit | No action — spec does not expose these |

**G4 Finding:** No false positives. The spec correctly identifies and rejects nonmathematical implementation details (raw Sage groups, private fields, ambient-space data, proof-by-iteration). The Non-Preservation Boundaries section is well-scoped and accurate.

---

### Check 5 — Unresolved Definitions

**Identified unresolved definitions and recommendations:**

| Ambiguity | Detail | Routing |
|---|---|---|
| Equality criterion for discriminant formed objects (line 128-129) | Spec says `A == B` means "equal presented discriminant formed objects, or a canonical equality criterion explicitly recorded by the implementation." This is underspecified: should equality mean same parent and same presentation, or isometry with a canonical witness? | Route to decision card. MAPPING.md note (1) establishes that "A generator or basis change creates a distinct object, possibly with an isometry witness, not the same object by equality." This precedent suggests `==` should mean same-presentation equality, with `is_isometric_to` as the separate predicate. |
| `normal_form()` as "implementation evidence for isometry" (lines 133-135) | Spec acknowledges `normal_form()` but does not fully specify its contract: which normal form (Smith? Jordan? Miranda-Morrison?), over which codomain, and under which hypotheses. | Record a decision or task. The MAPPING.md reconciliation (line 172) says to include this only with theorem/source hypotheses recorded at use sites. |
| `from_invariants_and_gram` modulus parameters | Spec line 79 mentions `modulus` and `quadratic_modulus` but does not define their types or validation rules beyond the compatibility condition on line 84. | Low risk — the validation rule `d_i * d_j * gram[i,j] ∈ R` is the key constraint. The modulus names can be resolved at implementation. |
| Composite `primary_part(m)` (line 123-124) | Spec says "composite selectors require an explicit decomposition rule." The decomposition rule is not specified. | Route to task. Standard primary decomposition `A ≅ ⊕ A[p^e]` is mathematically canonical, but the spec should state whether `primary_part(6)` decomposes to `primary_part(2) ⊕ primary_part(3)` or raises an error. |
| `cokernel()` on discriminant morphisms (line 147) | Spec requires `cokernel()` with descended form data. MAPPING.md (line 127) notes this is "a required project gap: the public discriminant path needs the actual cokernel object with descended form data." | Already tracked as a known gap. No new record needed. |

**G5 Finding:** Three ambiguities warrant decision or task records: (1) equality criterion, (2) `normal_form()` contract, (3) composite `primary_part` decomposition. These are genuine design questions, not spec defects. The spec correctly flags the boundaries of current knowledge.

---

### Check 6 — Obligation Preservation

**Obligations stated in spec and their preservation status:**

| Obligation | Owner | Preserved? | Notes |
|---|---|---|---|
| Discriminant object records source lattice, dual inclusion, quotient map, descended form | Spec acceptance criteria A | Yes | Explicit in Recovered Construction Surface |
| `q` and `b` evaluation owned by discriminant object | Spec acceptance criteria B | Yes | Explicit in Object and Element Surface |
| Generators, cardinality, invariant factors owned by discriminant object | Spec acceptance criteria B | Yes | Explicit line 90-91 |
| Finite iteration, submodules, quotients, orthogonal submodules | Spec acceptance criteria B | Yes | Explicit in Subobject/Quotient Surface |
| Orthogonal groups are Aut objects, not raw Sage groups | Spec acceptance criteria C | Yes | Explicit line 148-152 |
| Equality, group isomorphism, form isometry are distinct predicates | Spec acceptance criteria D | Yes | Explicit lines 127-133 |
| Backend finite-torsion calls encapsulated behind discriminant noun | Spec acceptance criteria E | Yes | Explicit in Non-Preservation Boundaries |
| `from_invariants_and_gram` validates rank, symmetry, integrality | Spec line 82-84 | Yes | Explicit validation rules |
| `lift()` is public only when returning dual/rational element | Spec line 107-108 | Yes | Explicit constraint |
| `delta`, `coparity` are lattice invariants, not discriminant-group methods | Spec lines 98-100 | Yes | Explicit exclusion |
| Sage element classes and private fields not exposed as public | Spec lines 158-159 | Yes | Explicit in Non-Preservation Boundaries |

**Obligation completeness check against dependent spec:** The spec depends on `SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS` (line 8). The discriminant group inherits finite-presentation structure from the lattice presentation contract. This dependency is correctly declared and the spec does not duplicate obligations that belong to the parent contract (e.g., PID structure theorem, Smith normal form, coordinate conventions).

**G6 Finding:** All 11 acceptance-criteria obligations are explicitly addressed in the spec body. No obligations are silently dropped, weakened, or moved without justification. The dependency on the presented-object contracts spec is correctly declared and scoped.

---

### Summary

| Check | Verdict | Critical Issues |
|---|---|---|
| G1 Source Grounding | **FAIL** | `src.bak/lattices/core/discriminant.py` does not exist. 4/5 references verified. |
| G2 Sage Method Coverage | **PASS** (minor) | Three Sage accessors (`value_module`, `value_module_qf`, `all_submodules`) not explicit in spec text but present in category-spec. Not blocking. |
| G3 Mathematical Correctness | **PASS** | All core mathematical claims verified against standard lattice theory and repo doctrine. |
| G4 Nonmathematical Rejection | **PASS** | All rejections correctly classified; no false positives. |
| G5 Unresolved Definitions | **PASS** (with notes) | Three ambiguities identified for decision/task records; none are spec defects. |
| G6 Obligation Preservation | **PASS** | All 11 acceptance-criteria obligations preserved; no silent weakening. |

**Overall Verdict:** NEEDS REVISION (G1 source-grounding gap is blocking). The mathematical content, Sage method coverage, obligation preservation, and unresolved-definition notes are all strong. The sole blocking issue is the unresolvable `src.bak` reference. Once that is corrected (either by locating the file or replacing the reference with the active category-spec and Sage source), the spec can advance to `reviewed` status.

**Recommended Actions:**
1. **[BLOCKING]** Replace `src.bak/lattices/core/discriminant.py` reference with `category_specs/lattices/subcategories/constructions/discriminant_groups.py` and Sage 10.7 `sage/modules/torsion_quadratic_module.py` as the verified source anchors.
2. **[Optional]** Add explicit `value_module()` and `value_module_qf()` mentions to the Object and Element Surface section.
3. **[Routing]** Create decision card for discriminant-object equality criterion (`==` vs `is_isometric_to` semantics).
4. **[Routing]** Create task for `normal_form()` contract specification (which normal form, hypotheses, codomain).
5. **[Routing]** Create task for composite `primary_part(m)` decomposition rule.
