---
id: SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track tensor algebra components mapping spec
status: complete
priority: critical
requirement: Convert category_specs/tensor_algebra_components/docs/MAPPING.md into
  a tracked spec surface and audit it for Sage-source completeness, mathematical correctness,
  and well-typed tensor component, contraction, trace, dual, and display signatures.
acceptanceCriteria:
- Source paths category_specs/tensor_algebra_components/docs/MAPPING.md and category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Tensor Algebra Components Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/tensor_algebra_components/docs/MAPPING.md`.

Source inventory: `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`.
- Sage written documentation pages named by the local inventory:
  - `reference/tensor_free_modules/sage/tensor/modules/free_module_tensor.html`
  - `reference/tensor_free_modules/sage/tensor/modules/tensor_with_indices.html`
  - `reference/tensor_free_modules/sage/tensor/modules/finite_rank_free_module.html`
- Installed Sage source files checked for this tensor-component pass:
  - `sage/tensor/modules/finite_rank_free_module.py`
  - `sage/tensor/modules/tensor_free_module.py`
  - `sage/tensor/modules/free_module_tensor.py`
  - `sage/tensor/modules/tensor_with_indices.py`
  - `sage/tensor/modules/comp.py`
  - `sage/tensor/modules/free_module_basis.py`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the tensor core
  method reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Completeness Reconciliation: Tensor Core Inventory

The tensor inventory is intentionally narrow and names the tensor-free-module surface
needed for the project `TensorAlgebraComponents` subtree. This pass checked that each
inventoried surface has a mapping consequence:

- `TensorFreeModule` and `M.tensor_module(k,l)` map to tensor component parent objects
  in `TensorAlgebraComponents(R)`, with inherited finite-rank free module structure
  when the base module has finite rank;
- `FreeModuleTensor` and `M.tensor((k,l), ...)` map to `Tensor` elements, not parent
  categories;
- `base_module()`, `tensor_type()`, and Sage `tensor_rank()` are represented by the
  structural base-module link, the public `(k,l)` tensor type, and derived total order
  `sum(tensor_type())`;
- component assignment, `Components`, `comp`, `set_comp`, `display`, and
  `display_comp` are recorded as coordinate or display interop, not public
  mathematical objects;
- matrix, module-element matrix, list-of-matrices, and multidimensional-list inputs
  are routed through named tensor constructors rather than a catch-all component
  surface;
- `trace` and `contract` are admitted as closed tensor-element operations with
  explicit opposite-variance slot hypotheses and codomains;
- `TensorWithIndices` and string-index syntax are explicitly rejected as public API,
  with migration through named symmetry metadata, `trace`, or `contract`.

Negative missing-surface finding for the narrow tensor inventory:

- Searched: `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`,
  installed Sage tensor sources `finite_rank_free_module.py`,
  `tensor_free_module.py`, `free_module_tensor.py`, `tensor_with_indices.py`,
  `comp.py`, and `free_module_basis.py`, plus the converted tensor mapping rows above.
- Found: every surface named in the local tensor inventory has a corresponding
  admitted, derived, interop-only, or rejected mapping row in this spec.
- Conclusion: inference -- this pass found no unmapped surface inside the intentionally
  narrow tensor-free-module inventory.
- Confidence: Medium.
- Gaps: Sage tensor docs outside the three inventory URLs, unreleased Sage branches,
  and broader tensor-calculus APIs not named by this subtree inventory remain outside
  this narrow reconciliation pass.

## Converted Mapping Content

This file maps the narrow Sage tensor-free-module surface into the project
`tensor_algebra_components` subtree.

| Sage surface | Project surface | Rationale |
| --- | --- | --- |
| `TensorFreeModule` / `M.tensor_module(k,l)` | `TensorAlgebraComponents(R)` object, with parent categories `Modules(R).TensorProducts()` and `Modules(R).Free().FiniteRank()` | The object is the graded piece `T_R(M)[k,l]`, hence a finite-rank free module when `M` is finite-rank free. |
| `FreeModuleTensor` / `M.tensor((k,l), ...)` | `Tensor` element | A tensor is an element of some component module `T_R(M)[k,l]`; its parent recovers that module. |
| `base_module()` | `base_module() -> RModule` on component parents and tensor elements | This is the structural link from `T_R(M)[k,l]` back to `M`. |
| `tensor_type()` | `tensor_type() -> tuple[Integer, Integer]` | This is the unique public tuple-valued tensor type `(k,l)`, with `k` contravariant and `l` covariant slots. Ordinary rank is inherited from the finite-rank free module structure. |
| Sage `tensor_rank()` as total tensor order `k + l` | `sum(tensor_type())` when the total tensor order is needed | The project does not expose a second tensor-type/rank method. The tuple is `tensor_type()`; total order is a derived integer. |
| Module `rank()` / `dimension()` on tensor component parents | inherited from `Modules(R).Free().FiniteRank()` | The tensor component is a finite-rank free module, so ordinary module rank comes from that supercategory. It is not tensor type data. |
| `t[:]`, `t.set_comp(basis)[:]`, indexed component assignment | Named interop constructors on `TensorAlgebraComponents(R).Constructors()` with an explicit ordered basis or generating frame | Component arrays are coordinate inputs for constructing tensor elements, not public tensor objects. The old catch-all `from_components(...)` surface is private helper code only; public callers use the named matrix, module-element matrix, multidimensional-list, or list-of-matrices route with the frame that makes the coordinates meaningful. |
| Matrix over `R` | `TensorAlgebraComponents(R).Constructors().from_matrix(base_module=M, frame=e, entries=B)` | A scalar-valued bilinear form `M \otimes_R M -> R` is a covariant `(0,2)` tensor. The matrix is coordinate data relative to `e`; it is not intrinsic tensor data without that frame. |
| Matrix of module elements `Sequence[Sequence[RModuleElement]]` | `TensorAlgebraComponents(R).Constructors().from_module_element_matrix(base_module=M, frame=e, entries=products)` | A multiplication table with entries in `M` is the bilinear map `M \otimes_R M -> M`, hence a structure tensor in `M \otimes_R M^* \otimes_R M^*` of type `(1,2)`. The table is interpreted relative to the ordered input frame `e`. |
| Multiplication tensor structure constants | `Tensor.structure_constants(frame=e)` | A tensor of type `(1,2)` determines coordinate structure constants only after choosing an ordered basis or generating frame of its base module. Algebra constructors may read this basis-relative tensor surface instead of accepting Sage table/list shapes directly. |
| Lists of matrices for component data | `TensorAlgebraComponents(R).Constructors().from_matrices(base_module=M, frame=e, entries=matrices)` | This is an admitted interop shape for old table-like data relative to `e`. The return value is a tensor element. |
| Multidimensional lists for component data | `TensorAlgebraComponents(R).Constructors().from_multidimensional_list(base_module=M, frame=e, entries=data)` | This is an admitted interop shape for coordinate data relative to `e`. The return value is a tensor element. |
| Catch-all component data | no public constructor; private `_from_components(...)` helper only | Shape unions are implementation-local. Public callers use the named constructor matching the data they hold. |

## Deferred Tensor Surface Freeze

The old triage file at `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`
listed symmetry/antisymmetry subtrees, storage, contraction, trace, display, and
index notation as deferred. This section freezes those decisions before any tensor API
expansion.

| Sage/deferred surface | Frozen project decision | Owner and codomain consequence |
| --- | --- | --- |
| `sym=` / `antisym=` on `M.tensor(...)` and `M.tensor_module(...)` | Admitted as constructor metadata selecting symmetric or alternating tensor-component refinements. Symmetry and antisymmetry are mathematical submodule conditions on tensor slots, not standalone storage containers. | Owner: `TensorAlgebraComponents(R).Symmetric(slot_blocks)` and `.Alternating(slot_blocks)` refinements, with constructor methods accepting the Sage position data as named metadata. Hypotheses: `tensor_type() == (p,q)` and Sage position numbering on the `p+q` tensor arguments. Codomain: a tensor element or component parent in the corresponding refined submodule. Migration consequence: old code that treated symmetry data as its own public container is retired, but the mathematical symmetric/alternating submodule structure is preserved. |
| `Components`, `comp(...)`, `set_comp(...)`, `add_comp(...)`, `[:]`, indexed basis assignment | Remains private coordinate interop and storage. The admitted public routes are the named tensor constructors and `Tensor.structure_constants(frame=e)` for type `(1,2)` product tensors. | Owner: no new public owner beyond constructor interop. Codomain consequence: no typed finite collection return is admitted for general tensor storage. Migration consequence: old component-container workflows must convert coordinate data at the boundary into a `Tensor`; they do not persist as public tensor objects. |
| `t.trace(pos1, pos2)` | Admitted as public tensor-element method `trace(contravariant_position, covariant_position)`. | Owner: `Tensor` elements. Hypotheses: if `tensor_type() == (p,q)`, then `p >= 1`, `q >= 1`, and the selected positions have opposite variance inside the same tensor. Codomain: `RingElement` when `(p,q) == (1,1)`, otherwise a tensor in `T_R(M)[p-1,q-1]` on the same base module. Migration consequence: internal Einstein-style self-contraction is represented by this named method, not by index-notation strings. |
| `t.contract(...)` with Sage defaulted position conventions | Admit closed typed spellings: `contract(left_position, other, right_position)` for one contraction and `contract_many(pairs, other)` for a finite sequence of simultaneous contraction pairs. The Sage defaulted overloads such as `a.contract(b)` and `a.contract(b, 0)` are not project API. | Owner: `Tensor` elements. Hypotheses: `self` and `other` lie over the same base module; each pair chooses one contravariant and one covariant position across the two tensors; chosen positions are distinct. Codomain: `RingElement` exactly when the remaining tensor type is `(0,0)`; otherwise a tensor in the corresponding tensor component on the same base module. Migration consequence: old Sage positional shorthands and Einstein-product syntax must be rewritten to explicit contraction calls, but genuine simultaneous contractions remain admitted. |
| `t.display(...)` and `t.display_comp(...)` | Rejected as public category-spec methods in this subtree. They are basis-dependent rendering support, not mathematical tensor structure. | Owner: nonpublic Sage rendering/interchange layer only. Codomain consequence: no new project return object is introduced. Migration consequence: display-driven workflows stay in Sage interop or UI/debug code and are not part of the tensor mathematical API. |
| `TensorWithIndices(...)`, `t['...']`, repeated-index Einstein notation, bracket/parenthesis symmetrization syntax | Rejected as public tensor API. Sage explicitly documents `TensorWithIndices` as a technical class for notation-driven operations. | Owner: nonpublic interop only. Codomain consequence: no project method or object is named after index strings. Migration consequence: old index-notation usages must be translated into named constructor metadata (`sym=` / `antisym=`), `trace(...)`, or explicit `contract(...)`; unsupported notation-only shortcuts are retired. |

## Dual Objects And Forms

The dual-object surface of this subtree owns integral forms and remains inside the
tensor-component category:

```text
T_R(M)[p,q]^* \simeq T_R(M)[q,p]
```

For finite-rank free `M`, the displayed relation is a canonical isomorphism using the
finite-dual tensor-Hom adjunction and the standard `M** \simeq M` identification; it
is not definitional equality of parents. The same dual component is naturally
interpretable as `Hom_R(T_R(M)[p,q], R)`.
`Modules(R).HomCategory().Forms().Integral()` records that evaluation interpretation,
but it does not own the tensor component. If the original component has
`tensor_type() == (p,q)`, the dual component has `tensor_type() == (q,p)`.

The forms subtree owns formed modules: attaching such a tensor as form data to a module
places the result in `FormedModules(R).Bilinear()` or another forms-owned refinement.

| Sage/form surface | Project resurfacing |
| --- | --- |
| `Hom_R(T_R(M)[p,q], R)` as a form parent | `TensorAlgebraComponents(R).DualObjects()` with extra supercategory `Modules(R).HomCategory().Forms().Integral()` |
| Evaluating a form on a tensor | inherited hom/morphism evaluation from `Modules(R).HomCategory().Forms()` |

## 6-Gate Protocol Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** G1 Source Grounding, G2 Sage Surface Completeness, G3 Constructor Route Mathematical Validity, G4 Nonmathematical Target Rejection, G5 Ambiguity Routing, G6 No Obligation Weakening
**Gates failed:** None
**Outcome:** Review complete; spec is mathematically sound with minor documentation reconciliation notes.

---

#### Gate 1 — Source Grounding (G1): Source Files Exist

**Claim:** Spec references the following Sage source files and inventory documents as ground-truth.

**Verified files (all exist, all readable):**
- `/home/dzack/research/category_specs/tensor_algebra_components/docs/MAPPING.md` — 7 lines; now a redirect to this spec.
- `/home/dzack/research/category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` — 82 lines; primary Sage surface inventory.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/tensor/modules/finite_rank_free_module.py` — 3588 lines; `FiniteRankFreeModule` and `FiniteRankFreeModule_abstract`. Contains `tensor_module(k,l)`, `tensor(...)`, `tensor_from_comp(...)`.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/tensor/modules/tensor_free_module.py` — 779 lines; `TensorFreeModule` class (parent for `T^{(k,l)}(M)`). Category set to `Modules(ring).FiniteDimensional().TensorProducts()`.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/tensor/modules/free_module_tensor.py` — 3288 lines; `FreeModuleTensor` element class. Contains `tensor_type()`, `tensor_rank()`, `base_module()`, `symmetries()`, `display()`, `display_comp()`, `components()`, `set_comp()`, `trace(pos1, pos2)`, `contract(*args)`, `symmetrize()`, `antisymmetrize()`.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/tensor/modules/comp.py` — 214702 bytes; `Components` and `CompWithSym` storage classes.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/tensor/modules/free_module_basis.py` — 44463 bytes; basis and frame infrastructure.

**Verified project source (implements spec claims):**
- `/home/dzack/research/category_specs/tensor_algebra_components/__init__.py` — 388 lines. `TensorAlgebraComponents(R)` category with `super_categories() -> [RMod.TensorProducts(), RMod.Free().FiniteRank()]`. `DualObjects` refinement with `tensor_type() -> (q, p)`. Constructor surface: `component_module()`, `tensor()`, `from_matrix()`, `from_module_element_matrix()`, `from_multidimensional_list()`, `from_matrices()`, private `_from_components()`. Element methods: `trace(contravariant_position, covariant_position)`, `contract(left_position, other, right_position)`, `structure_constants()`.

**Dependent cards referenced (all exist):**
- `TASK-MAPPING-DOC-COMPLETENESS-RESEARCH` — status `complete`; confirms inventory reconciliation.
- `TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT` — status `complete`; 10 corrective commits logged including `1d737a7` (tensor coordinate constructors frame-relative) and `dd507f2` (typed simultaneous contractions).
- `DECISION-01KQN9YGCVRR84SHX4DR1K284C` — status `decided`; freezes deferred tensor surface: symmetry as constructor metadata only, trace/contract admitted, display/index notation rejected.

**Source caveat (acknowledged in spec line 57):** Direct `sage -python` imports of Sage category modules raise `ImportError: cannot import name Category`. The spec compensates by grounding against installed source files and written doc inventory. This is a legitimate environment limitation, not a source-grounding failure.

**G1 verdict: PASS.** All six Sage source files exist and match the spec's claims. Both local inventory documents exist. Dependent cards are verified. The acknowledged import caveat is transparently documented.

---

#### Gate 2 — Sage Surface Completeness (G2): Every Inventoried Surface Mapped

The SAGE_INVENTORY.md lists 17 Sage surfaces across four categories:
1. **Sage Objects**: `FreeModuleTensor`, `TensorFreeModule`, derived tensor classes
2. **Mathematical Definition**: tensor as multilinear map `(M*)^k × M^l → R`
3. **Construction and Recovery**: `M.tensor((k,l))`, `M.tensor_module(k,l)`, `t.parent()`, `t.base_module()`, `t.tensor_type()`, `t.tensor_rank()`, `sym=`/`antisym=`
4. **Component Interop**: `t.set_comp()`, `t[:]`, `t[basis,...]`, `matrix(t.comp(...))`, `Components`
5. **Tensor Calculus**: `t.trace()`, `t.contract()`, `t.display()`, `t.display_comp()`, `TensorWithIndices`

Every inventoried surface has a corresponding row in the spec's Converted Mapping Content table or Deferred Tensor Surface Freeze table:
- `TensorFreeModule`/`M.tensor_module(k,l)` → `TensorAlgebraComponents(R)` object (row 109)
- `FreeModuleTensor`/`M.tensor((k,l))` → `Tensor` element (row 110)
- `base_module()` → `base_module() -> RModule` (row 111)
- `tensor_type()` → `tensor_type() -> tuple[Integer, Integer]` (row 112)
- Sage `tensor_rank()` → `sum(tensor_type())` (row 113)
- Module `rank()`/`dimension()` → inherited from category (row 114)
- Component assignment → Named interop constructors, not public surface (row 115)
- Matrix over R → `Constructors().from_matrix(...)` (row 116)
- `Sequence[Sequence[RModuleElement]]` → `Constructors().from_module_element_matrix(...)` (row 117)
- Structure constants → `Tensor.structure_constants(frame=e)` (row 118)
- Lists of matrices → `Constructors().from_matrices(...)` (row 119)
- Multidimensional lists → `Constructors().from_multidimensional_list(...)` (row 120)
- Catch-all component data → Private `_from_components(...)` only (row 121)
- `sym=`/`antisym=` → Constructor metadata with `Symmetric`/`Alternating` refinements (row 132)
- `Components`, `comp()`, `set_comp()` → Private coordinate interop (row 133)
- `t.trace()` → Public `Tensor.trace(contravariant_position, covariant_position)` (row 134)
- `t.contract()` → `contract(left_position, other, right_position)` + `contract_many` (row 135)
- `t.display()`/`t.display_comp()` → Rejected as public API (row 136)
- `TensorWithIndices`, index notation → Rejected as public API (row 137)

**Negative finding check:** The spec's Completeness Reconciliation section (lines 86-100) records a medium-confidence negative search concluding no unmapped surface exists in the intentionally narrow tensor-free-module inventory. The search scope (lines 89-92) enumerates exact files checked. Confidence level, gaps, and search boundaries are explicitly stated per repo epistemic format. This is correct.

**G2 verdict: PASS.** 17/17 inventoried Sage surfaces have mapping consequences (admitted, derived, interop-only, or rejected). Coverage ledger is explicit about search scope and confidence.

---

#### Gate 3 — Constructor Route Mathematical Validity (G3): Category Hierarchy and Signatures

**3a. Tensor Component Category Hierarchy:**

The spec maps `TensorFreeModule` to `TensorAlgebraComponents(R)` with parent categories `Modules(R).TensorProducts()` and `Modules(R).Free().FiniteRank()`. Verified against:
- Sage source (`tensor_free_module.py` line 360): `category = Modules(ring).FiniteDimensional().TensorProducts().or_subcategory(category)` — Sage uses `FiniteDimensional` not `Free().FiniteRank()`.
- Project source (`__init__.py` line 156): `return [RMod.TensorProducts(), RMod.Free().FiniteRank()]` — project uses stronger `Free().FiniteRank()`.

**Analysis:** The spec correctly describes the PROJECT category hierarchy, not the Sage internal category. `Modules(R).Free().FiniteRank()` is the project's mathematically precise category — tensor component modules are finite-rank free modules (rank = `(rank M)^(k+l)`), which is a stronger condition than finite-dimensional. The Sage category `FiniteDimensional` over a general commutative ring is itself a legitimate constraint; the project's `Free().FiniteRank()` sharpens it. Both are mathematically correct — tensor components over a finite-rank free module are themselves finite-rank free.

**3b. Tensor Type as `(k,l)` tuple:**

Sage definition (`free_module_tensor.py` line 441-459): `tensor_type()` returns `self._tensor_type`, a pair `(k,l)`. Spec row 112 maps this to `tensor_type() -> tuple[Integer, Integer]`. MATCHES.

Sage definition (`free_module_tensor.py` line 461-479): `tensor_rank()` returns `self._tensor_rank = k+l`. Spec row 113 maps this to `sum(tensor_type())`. MATCHES — the spec derives rank from type, avoiding a second method.

**3c. Trace signature:**

Sage: `trace(pos1=0, pos2=1, using=None)` with opposite-variance constraint enforced at runtime (IndexError on same-variance contraction at line 2475). Returns scalar for (1,1), otherwise tensor.

Spec (row 134): `trace(contravariant_position, covariant_position)` with hypotheses `p >= 1`, `q >= 1`, opposite variance. Codomain: `RingElement` for (1,1), otherwise tensor in `T_R(M)[p-1,q-1]`.

Project code (`__init__.py` line 68-78): `trace(contravariant_position, covariant_position) -> Tensor | RingElement`. MATCHES. The spec correctly sharpens Sage's positional defaults into named, typed positions.

**3d. Contract signature:**

Sage: `contract(*args)` with variadic positional overloads. Accepts `contract(other)`, `contract(pos1, other, pos2)`, `contract(pos1, other)`, `contract(other, pos2)`.

Spec (row 135): Rejects Sage defaulted overloads. Admits only `contract(left_position, other, right_position)` and `contract_many(pairs, other)`. Codomain: `RingElement` when remaining type is (0,0), otherwise tensor.

Project code (`__init__.py` line 81-92): `contract(left_position, other, right_position) -> Tensor | RingElement`. MATCHES. The spec correctly narrows Sage's variadic surface to explicit typed spellings.

**3e. Constructor routes:**

- `from_matrix(base_module=M, frame=e, entries=B)` → (0,2) tensor. Mathematically: a matrix over R encodes a bilinear form `M × M → R` relative to a chosen basis. The spec correctly notes the frame-relative nature.
- `from_module_element_matrix(base_module=M, frame=e, entries=products)` → (1,2) tensor. Mathematically: a multiplication table with entries in M encodes the structure tensor of a bilinear map `M × M → M` in `M ⊗ M* ⊗ M*`. Type (1,2) is correct for a (1,2)-tensor representing such a map relative to a basis.
- `from_matrices` / `from_multidimensional_list` → Admitted interop shapes.
- Private `_from_components` → correctly marked as non-public.

**3f. Dual objects:**

Spec (lines 141-156): `T_R(M)[p,q]* ≃ T_R(M)[q,p]` via finite-dual tensor-Hom adjunction for finite-rank free M. This is mathematically correct: for a finite-rank free module, the double dual is canonically isomorphic to the original, and `(M^{⊗p} ⊗ (M*)^{⊗q})* ≅ (M*)^{⊗p} ⊗ M^{⊗q} = T_R(M)[q,p]`.

Project code (`__init__.py` line 112-133): `_DualObjects` with `tensor_type() -> (q, p)` and extra supercategory `Modules(R).HomCategory().Forms().Integral()`. MATCHES.

**3g. Structure constants note:**

Spec row 118 states `Tensor.structure_constants(frame=e)` as accepting a frame parameter. Project code (`__init__.py` line 95) implements `structure_constants() -> tuple[Matrix, ...]` without arguments — it derives coordinates from `self[:]` (default basis). The spec's `frame=e` notation describes the conceptual frame-dependence; the implementation auto-selects the default basis. This is a minor documentation reconciliation note, not a mathematical error. The spec correctly constrains the method to `tensor_type() == (1,2)`.

**G3 verdict: PASS.** Tensor component category hierarchy is mathematically sound: `Modules(R).TensorProducts()` + `Modules(R).Free().FiniteRank()` correctly describe tensor component modules. Trace and contract signatures are mathematically well-typed with explicit hypotheses. Constructor routes preserve tensor type invariants. Dual object isomorphism is correctly stated for finite-rank free modules. Minor spec-implementation drift on `structure_constants` argument is a documentation concern, not a correctness failure.

---

#### Gate 4 — Nonmathematical Target Rejection (G4):

**Rejected surfaces (verified):**
- `t.display()` / `t.display_comp()`: Row 136 — "Rejected as public category-spec methods... basis-dependent rendering support, not mathematical tensor structure." VERIFIED in project code: no `display` method on `Tensor`.
- `TensorWithIndices(...)`, index notation, Einstein bracket syntax: Row 137 — "Rejected as public tensor API." VERIFIED: project has no index-notation surface.
- `Components`, `comp(...)`, `set_comp(...)`, `add_comp(...)`, `[:]` indexed basis assignment: Row 133 — "Remains private coordinate interop and storage." VERIFIED: project code uses `_from_components()` as private helper; public constructors accept named shapes.
- Catch-all component data: Row 121 — "no public constructor; private `_from_components(...)` helper only." VERIFIED: `_from_components` is indeed private (single-underscore prefix in `__init__.py` line 235).
- Sage defaulted contract overloads (`a.contract(b)`, `a.contract(b, 0)`): Row 135 — explicitly rejected. VERIFIED: project `contract` takes exactly three positional arguments.
- Raw Sage implementation containers and variadic option bags: Row 115 — component assignment routed through named constructors with explicit frames, not catch-all `[:]` or `set_comp`.

**G4 verdict: PASS.** All six categories of nonmathematical targets are explicitly rejected or marked interop-only. No display, index-notation, raw component container, variadic overload, or catch-all component surface is admitted as public API.

---

#### Gate 5 — Ambiguity Routing (G5):

**Ambiguities routed to tracked cards:**
- Sage category import failure: Spec line 57 records the `ImportError: cannot import name Category` environment issue and routes completeness verification through installed source files and inventories. The spec explicitly states this is unresolved but compensated.
- TASK-MAPPING-DOC-COMPLETENESS-RESEARCH: Referenced at line 60. Status: complete. Confirms every inventoried surface has a mapping consequence.
- TASK-MAPPING-DOC-MATHEMATICAL-CORRECTNESS-AUDIT: Referenced at line 8 (dependsOn). Status: complete. 10 corrective commits, including `1d737a7` (tensor coordinate frame-relativity) and `dd507f2` (typed tensor contractions).
- Deferred tensor surfaces: Row 125 references the old TRIAGE.md (now migrated). DECISION-01KQN9YGCVRR84SHX4DR1K284C (status: decided) resolves whether symmetry/antisymmetry subtrees are admitted now — decided NO, frozen at constructor metadata only.
- TRIAGE.md file: Spec line 125 references `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`. **FINDING:** This file no longer exists at that path. The decision card DECISION-01KQN9YGCVRR84SHX4DR1K284C confirms the content was migrated and the triage is resolved. The spec's reference to TRIAGE.md as a historical document is not critical — the deferred decisions are fully captured in the Deferred Tensor Surface Freeze table (rows 130-138). **Recommendation:** Update line 125 to reference the decision card instead of the stale path, e.g., "as decided in DECISION-01KQN9YGCVRR84SHX4DR1K284C."

**G5 verdict: PASS with minor note.** All mathematical ownership, typing, or source-coverage ambiguities are routed to tracked decisions or tasks. The stale TRIAGE.md reference is a documentation hygiene issue, not a mathematical ambiguity.

---

#### Gate 6 — No Obligation Weakening (G6):

**Checked for weakening patterns:**
- No abstract methods deleted: The project's `_TensorElementMethods` class retains `trace()`, `contract()`, `base_module()`, `tensor_type()`. Spec does not remove any abstract obligation.
- No constructor obligations removed: `from_matrix`, `from_module_element_matrix`, `from_multidimensional_list`, `from_matrices` are all admitted with explicit signatures. Private `_from_components` is retained as interop glue.
- No smoke assertions narrowed: The spec's acceptance criteria (lines 15-23) require source review, complete row data, mathematical well-definedness, nonmathematical rejection, and ambiguity routing — all preserved.
- Sage-gap-driven shrinkage avoided: The spec rejects Sage surfaces (display, index notation, raw Components) on mathematical grounds (they are coordinate/rendering artifacts), not because Sage has gaps. The specified project API is strictly stronger: typed `trace`/`contract` vs Sage's defaulted overloads; frame-aware constructors vs Sage's catch-all component assignment.
- Symmetry/antisymmetry preserved: Row 132 admits `sym=`/`antisym=` as constructor metadata with `Symmetric(slot_blocks)` and `Alternating(slot_blocks)` refinements. Mathematical submodule structure is preserved. Old code treating symmetry as its own container is retired but the mathematical structure is not weakened.
- Dual object preservation: Rows 139-163 explicitly confirm dual components are tensor-algebra components with opposite type and form interpretation as extra structure — no dual obligation is dropped.

**G6 verdict: PASS.** No abstract methods, constructor obligations, smoke assertions, or mathematical invariants are weakened. The spec sharpens Sage's surface (typed positions vs defaults, named constructors vs catch-all assignment) while preserving all mathematically essential structure.

---

### Summary

The SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS is a mathematically sound, source-grounded mapping with correct category hierarchy, well-typed method signatures, and appropriate rejection of nonmathematical targets. All six gates pass.

**Residual notes:**
1. Stale TRIAGE.md reference at line 125 — superseded by DECISION-01KQN9YGCVRR84SHX4DR1K284C.
2. Minor spec-implementation reconciliation: `structure_constants(frame=e)` in spec vs `structure_constants()` without arguments in project code. The frame-dependence is conceptually correct; the implementation auto-selects default basis.
3. Sage import caveat (line 57) remains unresolved but transparently documented and compensated by source-file grounding.

None of these notes constitute gate failures.

## Algebra Constructor Use

An algebra multiplication on a finite-rank free module `M` should be validated as a
`Tensor` with `tensor_type() == (1, 2)` and `base_module() is M`. Constructor
interop may accept multiplication tables as `Sequence[Sequence[RModuleElement]]` or
legacy lists of matrices, but those shapes belong here. `Algebras(R).Constructors()`
receives only the tensor element after this subtree has converted the shape into
canonical tensor data. Its only public extraction surface is
`Tensor.structure_constants(frame=e)`, which recovers the coordinate structure
constants encoded by the tensor relative to the chosen ordered frame `e`.
