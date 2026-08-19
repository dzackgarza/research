# Plan: Correct super_categories() Immediate-Parent Hierarchy

**Goal:** Every `category_specs` category with 2+ declared parents in
`super_categories()` lists only mathematically immediate parents.
Build a validator that computes transitive closure and rejects transitive/wrong edges.
All 69 multi-parent categories pass zero-issue validator, `just plan-validate` passes.

**Date:** 2026-05-28

* * *

## Scope summary

| Metric | Count |
| --- | --- |
| Files with `super_categories()` defs | 125 |
| Multi-parent (2+) categories | 69 |
| Single-parent (verification only) | 55 |
| Zero-parent (needs fix) | 1 |
| Dynamic body (matrix_algebras.py — skip) | 1 |
| Subtree dimensions | rings (largest), sets, algebras, modules, lattices, posets, topological_spaces, tensor_algebra_components |

* * *

## Phase 1: Build the extraction & transitive-closure tool

**Output:** `category_specs/_tools/super_validator.py` — reads the python AST, builds
the DAG, computes transitive closure, reports:

- Transitive edges (parent P is reachable from another declared parent Q)
- Zero-parent categories
- Categories that never appear AS parents (suspicious)
- Unknown references (names not resolvable in the graph)

**Design constraints:**
- Operates on AST, not import resolution — avoids circular import and Sage LazyImport
  issues
- Treats Sage interop parents (`SageX()`) as leaf nodes (their internals are
  unobservable)
- Treats `self.base_category()` (dynamic) as an opaque reference — skip the file; the
  enclosing category will still report missing edges
- Groups issues by subtree

**This phase does NOT edit any spec file.** It produces a report.

**Files created:** `category_specs/_tools/super_validator.py`

**Verification:** Run against current (uncorrected) tree to produce baseline report.
Confirm it finds the known issues.

* * *

## Phase 2: Correct the hierarchy — ring subtree

The largest and most complex subtree.
Known issues from the user:

### 2a: `_Fields` (8 parents → immediate only)

Current:
`[SageFields(), _CommutativeRings(), _DivisionRings(), _EuclideanDomains(), _IntegrallyClosedDomains(), _NoetherianRings(), _ReducedRings(), Rings().KrullDimension(0)]`

Mathematical chain: Field ⊂ Euclidean ⊂ PID ⊂ UFD ⊂ GCD ⊂ IntegralDomain ⊂
CommutativeRing. But also: Field ⊂ DivisionRing ⊂ Ring.
And trivially: Field ⊂ IntegrallyClosed, Field ⊂ Noetherian, Field ⊂ Reduced, Field has
KrullDim 0.

**Decision needed per parent:**

| Parent | Immediate? | Reasoning |
| --- | --- | --- |
| `SageFields()` | YES | Sage interop |
| `_CommutativeRings()` | YES | Direct axiom: Fields is axiom on CommutativeRings |
| `_DivisionRings()` | YES | Every field is a division ring; Fields ⊂ DivisionRings directly |
| `_EuclideanDomains()` | YES | Every field is trivially Euclidean (all nonzeros are units) |
| `_IntegrallyClosedDomains()` | TRANSITIVE | Fields ⊂ Euclidean ⊂ PID ⊂ UFD ⊂ GCD ⊂ IntegralDomain ⊂ IntegrallyClosed → path exists through Euclidean |
| `_NoetherianRings()` | TRANSITIVE | Fields ⊂ CommutativeRings → but Noetherian is axiom on CommutativeRings. Fields are Noetherian, but this is reachable via _CommutativeRings → Noetherian? No — Noetherian is a refinement of CommutativeRings, not a supercategory. Actually: Fields ⊂ Euclidean ⊂ PID ⊂ Noetherian (PID ⊂ Noetherian). So transitive through the chain. |
| `_ReducedRings()` | TRANSITIVE | Fields ⊂ IntegralDomains ⊂ ReducedRings; reachable through any chain |
| `Rings().KrullDimension(0)` | ? | Krull dim 0 is a property, not a parent category — this might be a Sage pattern. Need to check |

**Tentative correction:**
`[SageFields(), _CommutativeRings(), _DivisionRings(), _EuclideanDomains()]`

Wait — but `_EuclideanDomains` declares `_PrincipalIdealDomains()` as parent.
So the chain is Euclidean → PID → UFD → GCD → IntegralDomain.
Fields → Euclidean would make PID, UFD, etc.
reachable from Fields through Euclidean.
That's correct and intentional.

But there's a subtlety: in Sage, EuclideanDomains is not necessarily a supercategory of
Fields. The axiom chain is `CommutativeRings().Field()`, not
`IntegralDomains().Euclidean().Field()`. So listing EuclideanDomains as a parent means
we're asserting Fields ⊂ EuclideanDomains as an extra structure, not as part of the
refinement chain. This is correct mathematically but might interact poorly with Sage's
category infrastructure.
We should check.

For now, treat this as needing decision: either keep EuclideanDomains (correct math,
correct immediate) or drop it if Sage chokes.
Given the user's directive to preserve Sage-backed method surfaces, keep it.

### 2b: `_NumberFields` and `_GlobalFields` — verify hierarchy

Current state already encodes NumberFields ⊂ GlobalFields ⊂ Fields:
- `_NumberFields.super_categories()` = [SageNumberFields(), _GlobalFields(), _Fields()]
- `_GlobalFields.super_categories()` = [_Fields()]

This is already correct!
`_Fields` in NumberFields is transitive (via GlobalFields → Fields).
Remove it.

**Correction:** `_NumberFields.super_categories()` →
[SageNumberFields(), _GlobalFields()]

### 2c: `_QQ` (rational_field.py, 4 parents)

Current: `[_Fields(), _FractionFields(), _NumberFields(), Rings().Characteristic(0)]`

Mathematically: QQ is a field, a fraction field (of ZZ), and a number field (it is, in
Sage's classification).
Each is immediate. Rings().Characteristic(0) is a property category — need to check
whether this is a Sage parent pattern.

**Keep all 4** unless validator flags transitive edges.

Wait — but if we remove `_Fields()` from NumberFields (making it transitive via
GlobalFields → Fields), then QQ needs explicit `_Fields()` since QQ ⊂ NumberFields ⊂
GlobalFields ⊂ Fields, but QQ declaring Fields directly is the immediate parent that
NumberFields no longer provides directly.
Actually, the immediate parent relationship is QQ → NumberFields (direct) and QQ →
Fields (also direct, since QQ is a field regardless of number field status).
QQ → FractionFields is also direct (QQ = Frac(ZZ)). So this is fine.

### 2d: `_CompleteDiscreteValuationFields` (4 parents)

Current:
`[SageCDVF(), _CompleteDiscreteValuationObjects(), _CompleteRings(), _DiscreteValuationFields()]`

Check: `_DiscreteValuationFields` declares `[_Fields(), _DiscreteValuationRings()]`. So
DVF → Fields is reachable via DVF → CDVO → ... wait, let me trace:
- CDVF → DVF → Fields (path exists: CDVF.parents = [..., DVF], DVF.parents =
  [Fields, DVR])
- CDVF → CompleteRings (immediate)
- CDVF → CDVO → [CompleteRings, ValuedRings]

So `_CompleteRings()` is reachable via CDVO (CDVO → CompleteRings).
That makes `_CompleteRings()` transitive in CDVF. Remove it.

**Correction:**
`[SageCDVF(), _CompleteDiscreteValuationObjects(), _DiscreteValuationFields()]`

### 2e: `_PAdicRings` (3 parents)

Current: `[ApproximateRingsCategory(), _CompleteRings(), _ValuedRings()]`

Check: ApproximateRingsCategory — need to check its parents.
Approximate is a custom category; if it doesn't list CompleteRings or ValuedRings, all
three are immediate.

### 2f: `_Qp` (p_adic_field, 3 parents)

Current: `[_PAdicRings(), _CompleteDiscreteValuationFields(), _LocalFields()]`

`_CompleteDiscreteValuationFields` is a field category, so LocalFields is also a field
category. Need to check whether LocalFields → CDVF or vice versa.
LocalFields declares `[_Fields(), _TopologicalRings()]` — so LocalFields does NOT list
CDVF. Thus both CDVF and LocalFields are immediate parents of Qp.
Correct as-is.

### 2g: Remaining ring multi-parent categories

The remaining 40+ ring subcategory multi-parents need individual review.
Most are 2-parent (Sage interop + one local parent), which are likely correct.
The validator will catch any transitive edges.

* * *

## Phase 3: Correct the hierarchy — algebras subtree

Algebras: `[AssociativeAlgebras(R), Rings().RingsUnder(R), Modules(R), SageAlgebras(R)]`

- AssociativeAlgebras → MagmaticAlgebras → Modules(R) is the chain
- So `Modules(R)` is transitive (via AssociativeAlgebras → MagmaticAlgebras → Modules)

Need to check: `Rings().RingsUnder(R)` — is this reachable through any other parent?
Unlikely; it's likely immediate.

**Correction:** Remove `Modules(R)`. Result:
`[AssociativeAlgebras(R), Rings().RingsUnder(R), SageAlgebras(R)]`

All 2-parent algebra subcategories (commutative, semisimple, with_basis) are likely
correct (Sage interop + parent algebra).

* * *

## Phase 4: Correct the hierarchy — remaining subtrees

### 4a: Modules (2 parents)

`Modules: [Sets(), SageBimodules(R, R)]` — both immediate.
Likely correct.

### 4b: Posets `_FiniteLatticePosets` (4 parents)

Current:
`[_LatticePosets(), _FiniteMeetSemilatticePosets(), _FiniteJoinSemilatticePosets(), SageFiniteLatticePosets()]`

Chain: _FiniteLatticePosets axiom is on _LatticePosets. _LatticePosets declares
[_MeetSemilatticePosets, _JoinSemilatticePosets].

Now: _FiniteMeetSemilatticePosets declares [_MeetSemilatticePosets, Posets().Finite()].
_FiniteJoinSemilatticePosets declares [_JoinSemilatticePosets, Posets().Finite()].

Is _FiniteMeetSemilatticePosets reachable from _LatticePosets? _LatticePosets →
_MeetSemilatticePosets. But _FiniteMeetSemilatticePosets adds the Finite axiom.
If the path is: _FiniteLatticePosets → _LatticePosets → _MeetSemilatticePosets, that
doesn't give us _FiniteMeetSemilatticePosets (which is _MeetSemilatticePosets + Finite
axiom), unless the category infrastructure automatically refines.
This is the key question: does listing _LatticePosets as parent automatically make
_FiniteMeetSemilatticePosets a supercategory?
No — _LatticePosets doesn't carry the "Finite" axiom, so the chain stops at
_MeetSemilatticePosets, not _FiniteMeetSemilatticePosets.

Thus all 4 parents are likely immediate.
This needs verification through the validator.

### 4c: Sets subtree

Multi-parent sets categories are mostly 2-parent (Sage interop + local).
The 3-parent cases:
- `_RealSetSets`: 3 parents — need review
- `_CountableSets`: 3 parents — Infinite + Countable + SageInfiniteEnumerated — check if
  Countable → Infinite exists

### 4d: Topological spaces, tensor_algebra_components

These are small subtrees.
The construction categories use `self.base_category()` which is dynamic — the validator
will flag these as skips.

* * *

## Phase 5: Build the committed validator

**Output:** `category_specs/validators/super_categories_validator.py` (or integrated
into test suite)

**Behavior:**
1. Parses every `super_categories()` return value via AST
2. Builds a directed graph G where edges are declared parents
3. Computes transitive closure of G
4. For each category, checks each declared parent P: is P reachable from any OTHER
   declared parent Q? If yes, P is transitive → ERROR
5. Reports categories with 0 parents → WARNING
6. Reports categories with dynamic/unparseable bodies → INFO (skip)
7. Reports categories whose declared parents include names not found as any category →
   WARNING (possible typo)

**Exit code:** Non-zero if any ERROR-level issue found.

**Integration:** Run as `just validate-super-categories` and as a gate in
`just plan-validate`.

* * *

## Phase 6: Verify and commit

1. Run validator → zero errors on entire tree
2. Run `just plan-validate` → passes
3. Create branch, commit corrected files + validator
4. Final report of all changes made

* * *

## Files to create

| File | Purpose |
| --- | --- |
| `category_specs/_tools/super_validator.py` | Extraction, graph building, transitive-closure, and reporting tool (Phase 1) |
| `category_specs/validators/super_categories_validator.py` | Committed validator using the same logic, integrated into test/QC (Phase 5) |

## Files to edit (~69 multi-parent categories)

All multi-parent `super_categories()` return lists.
Key clusters:
- `category_specs/rings/subcategories/field.py` — 8→~4 parents
- `category_specs/rings/subcategories/number_field.py` — 3→2 parents
- `category_specs/rings/subcategories/complete_discrete_valuation_field.py` — 4→3
  parents
- `category_specs/rings/subcategories/complete_discrete_valuation_ring.py` — 4→? parents
- `category_specs/rings/subcategories/dedekind_domain.py` — 5→? parents
- `category_specs/rings/subcategories/discrete_valuation_field.py` — 3→? parents
- `category_specs/rings/subcategories/discrete_valuation_ring.py` — 3→? parents
- `category_specs/algebras/__init__.py` — 4→3 parents
- `category_specs/posets/subcategories/finite_lattice.py` — 4→? parents
- ~50 more 2-parent categories — mostly Sage interop + one local parent, likely correct,
  but all need transitive-closure check

## Risks and open questions

1. **Mathematical edge cases:** Some "transitive" parents might be mathematically
   necessary for Sage's category framework to resolve structure properly (e.g., Fields
   declaring EuclideanDomains ensures Euclidean methods are available).
   The validator can't distinguish these; human review of each flagged edge is required.

2. **Dynamic bodies:** `matrix_algebras.py` returns `super().super_categories()` via
   cast. These are unparseable by AST and will be skipped — recorded for manual review.

3. **Sage parent references:** `SageFields()`, `SageRings()`, etc.
   are treated as leaf nodes.
   If a Sage parent resolves to a Sage category that itself has Sage supercategories, we
   can't observe those edges, so we might fail to detect some transitive edges through
   Sage categories. Acceptable risk — Sage categories are beyond our control.

4. **Property categories:** `Rings().KrullDimension(0)`, `Rings().Characteristic(0)`,
   `ApproximateRingsCategory()` — these may be property-like categories rather than
   structural parents. Need to verify they should remain as declared parents.

5. **Method surface preservation:** Removing a transitive parent might change which
   ParentMethods/ElementMethods are inherited.
   The Sage category framework inherits from ALL supercategories, not just immediate
   ones, so removing transitive parents from the declaration should NOT weaken the
   method surface (they're still reachable through the chain).
   But we must verify this after each edit.

6. **`_QQ` declaring `_NumberFields()`:** Mathematically, QQ is a number field in Sage's
   classification. If we decide QQ should NOT be under NumberFields (user's "number
   fields ⊂ global fields" comment), this needs source grounding — check Sage's
   NumberFields category definition for whether QQ ∈ NumberFields.

* * *

## Task decomposition for execution

This plan decomposes into 7 sequential phases.
Each phase except Phase 6 produces a verifiable artifact.
Phase 6 (commit) gates on zero errors from the validator.

**Execution order is sequential** — the validator tool (Phase 1) must exist before
corrections (Phases 2–4) can be verified.
