# STATUS.md — 2026-05-08

221/251 cards complete. 7 cards in `needs-human-input`. No `needs-review`, `unstarted` (without unmet deps), or `revision-required` cards remain.

---

## State

Current phase: category-spec and semantic-vocabulary (`.agents/current-goal-phase.md`).

All category-spec subsystems are complete: Sets, Posets, TopologicalSpaces, Modules, Rings, Algebras, TensorAlgebraComponents, Forms, Lattices, Homsets, End/Aut. Method ownership inventories, constructor admission rules, and Sage source maps are documented for each. Six historical recovery features preserved useful code from `src.bak/` as specs. The lattice/modules-with-forms implementation roadmap is drafted and approved but gated behind the spec→implementation phase transition.

Remaining work is 7 decisions the agent cannot make independently.

---

## Decisions

### 1. Tensor-component placeholder methods

**Card:** `TASK-1777748120751-VP7D5V-FIX-TENSOR-COMPONENT-PLACEHOLDER-METHODS-AND-TYPE-LEAKS`

**What was done:** The concrete `lift_from_product(...)` placeholder in `TensorAlgebraComponents.ParentMethods` was replaced with an abstract requirement inherited from `Modules(R).TensorProducts().ParentMethods`. Return types on `structure_constants()` and internal coordinate extraction were changed from raw Sage slices to typed tuples. Missing `@final` annotations were added.

**Why it needs a human:** The card's grounding cites `category_specs/modules/subcategories/constructions/tensor_products.py` and `SPEC-MAPPING-MODULES` as the source for `lift_from_product` ownership. The abstract-routing approach treats tensor-component lifting as inherited tensor-product vocabulary rather than a tensor-component-specific public method. This is a design decision about method ownership boundaries — whether `lift_from_product` belongs to the tensor-product parent or the tensor-component child. The agent cannot adjudicate between these two ownership models because both are consistent with the spec corpus; the choice determines which category's ParentMethods carry the obligation.

**Downstream:** This card blocks `PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING` → `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` → `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES`.

### 2. Algebra construction boundary

**Card:** `TASK-1777748120716-ZUYAHM-MOVE-NONTRIVIAL-ALGEBRA-CONSTRUCTION-OUT-OF-CATEGORY-CONSTRUCTORS`

**What was done:** Analysis of `category_specs/algebras/__init__.py` found the current algebra constructor surface routes through named lightweight Sage-backed methods (`FreeAlgebra`, source-category `S.algebra(R, category=...)`, `FiniteDimensionalAlgebra` via tensor-component construction). No direct constructor routes for `Zmod`, cyclotomic fields, or number fields were found. The `SPEC-MAPPING-ALGEBRAS` spec already defines the boundary: heavy constructors belong to their ring/field owners or to tensor-component interop before algebra construction.

**Why it needs a human:** The negative finding asserts the current surface is compliant, but the analysis scope was limited to `category_specs/algebras/`. Other subtrees may still reference these constructors for their own module/ring/field surfaces. The question is whether a broader audit is needed, or whether the algebra-constructor boundary as analyzed is sufficient. The agent cannot determine the acceptable scope of the compliance check — this is a product-scope decision about how thorough the audit must be.

**Downstream:** Same chain as #1.

### 3. Static category refinement order

**Card:** `PLAN-STATIC-CATEGORY-REFINEMENT-ORDER`

**What it defines:** Every `super_categories()` return must be a documented, justified edge. Constructor interception order must not depend on unstable categories. Has an admitted-edges table covering Algebras, Modules, Posets, Sets, and TensorAlgebraComponents.

**Why it needs a human:** The admitted-edges table needs approval before decomposition into enforcement tasks. The edges represent mathematical specialization claims (e.g., Fields → IntegralDomains → Rings) that determine which methods are inherited where. Adding or removing an edge changes the method surface of every subcategory below it. The agent cannot approve these claims because they are mathematical assertions about the category hierarchy.

**Downstream:** This plan defines the category graph that all constructor routing, method inheritance, and smoke tests depend on. Until it's approved, no new category edges can be added with confidence.

### 4. Smoke audit uniformity stabilization

**Card:** `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`

**What it defines:** Groups smoke-frontier, audit, variadic-signature, import-hygiene, wrapper, type, and anti-slop compliance under one plan. Two phases: variadic signature closure audit, duck-type object-shape probe audit.

**Why it needs a human:** The plan's success criteria include routing smoke failures to spec/implementation/research/decision cards by mathematical cause, and ensuring the global QC whitelist (`/home/dzack/ai/quality-control/vulture_whitelist.py`) remains tooling support rather than a planning document. Approval requires deciding whether the grouped scope is correct (are all audit concerns captured?) and whether the phase decomposition is sufficient. The agent cannot determine whether audit coverage is adequate for the phase transition — this is a quality-bar decision.

**Downstream:** Smoke audit results feed into the phase-transition gate. Incomplete or misrouted audit findings would allow implementation to proceed on an unverified spec surface.

### 5. Varieties category integration

**Card:** `TASK-INTEGRATE-VARIETIES-CATEGORY`

**What it does:** Research card for integrating varieties into the category-spec hierarchy. Depends on `TASK-INTEGRATE-SCHEMES-CATEGORY` (complete). Must identify the mathematical definition, survey Sage/backend surfaces, determine relationships to existing categories, and create follow-up cards.

**Why it needs a human:** The schemes integration is complete but the variety category surface depends on design choices about how abstract the geometry layer should be. Options include: defer until schemes vocabulary is fully settled, define a minimal interface now that can be refined later, or postpone until the Coble phase when concrete geometric objects are needed. The agent cannot make this call because it depends on the downstream research plan.

**Downstream:** Blocks `PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH` → `PLAN-GEOMETRIC-SOURCE-ADMISSION` → `FEATURE-GEOMETRY-CATEGORY-INTERFACES`.

### 6. Coble isotropic orbit enumeration

**Card:** `SPEC-COBLE-ISOTROPIC-ORBIT-ENUMERATION`

**What it asks:** Can existing software (GAP, Sage, Oscar/Hecke) compute O(A,q)-orbits of isotropic elements for the Coble discriminant group A ≅ (Z/2Z)^11 (order 2048)? If not, can character theory/Burnside give the orbit count without full enumeration?

**Why it needs a human:** This is a mathematical research question — surveying computational capabilities for a specific finite quadratic form. The agent does not have the mathematical training to evaluate GAP's orbit algorithms, Sage's `QuadraticForm.automorphism_group()` correctness, or Burnside's lemma applicability to this specific group. The `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES` dependency provides the discriminant-form method surface this spec needs to consume; the gap is the actual orbit computation capability.

**Downstream:** This is downstream-phase work (gated behind the spec→implementation transition). Does not block any current-phase cards.

### 7. Coble lifting theorem verification

**Card:** `SPEC-COBLE-LIFTING-THEOREM-VERIFICATION`

**What it asks:** Do Nikulin 1.5.2 (surjectivity of O(L) → O(A_L)) and the Eichler criterion (spinor norm kernel transitivity on primitive vectors) apply to the Coble lattice T_Co? T_Co is rank 11, signature (2,9), 2-elementary discriminant A ≅ (Z/2Z)^11, even.

**Why it needs a human:** Verifying theorem hypotheses for a specific lattice requires mathematical expertise. The agent cannot check whether the spinor norm is surjective for T_Co, whether the Eichler criterion's rank ≥ 3 and indefinite conditions are satisfied, or whether the isotropic orbit bijection holds. These are theorem-verification tasks, not implementation tasks.

**Downstream:** Same as #6 — downstream-phase, gated behind spec→implementation transition.

---

## Cascading completion

Once decisions 1-5 resolve:
- `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` → complete (its last 4 non-decided children resolve; 16 decisions are already recorded)
- `FEATURE-GEOMETRY-CATEGORY-INTERFACES` → complete (its last non-decided child resolves)
- DAG reaches 243/251 complete

Decisions 6-7 unblock `FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION` when resolved, but this feature is gated behind the phase transition regardless.

The lattice roadmap (`PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP`, `approved-and-unstarted`) is gated behind the spec→implementation phase transition. Its work log records: "Blocked by the repo's current category-spec and semantic-vocabulary phase."

---

## Pre-read

- `.agents/current-goal-phase.md` — active phase policy, what's blocked by default
- Card bodies for decisions 1-7 (paths in `plans/features/`)
- `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP.md` — implementation roadmap (gated, for forward planning)
