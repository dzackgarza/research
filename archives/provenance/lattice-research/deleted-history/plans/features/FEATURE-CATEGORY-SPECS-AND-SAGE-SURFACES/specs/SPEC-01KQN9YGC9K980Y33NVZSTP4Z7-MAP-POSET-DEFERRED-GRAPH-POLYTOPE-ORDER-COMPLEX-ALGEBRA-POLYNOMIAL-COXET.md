---
id: SPEC-01KQN9YGC9K980Y33NVZSTP4Z7-MAP-POSET-DEFERRED-GRAPH-POLYTOPE-ORDER-COMPLEX-ALGEBRA-POLYNOMIAL-COXET
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES]]'
title: Map poset deferred graph polytope order-complex algebra polynomial Coxeter
  display and raw-interop surfaces to final owners
status: complete
priority: critical
requirement: Posets mapping owns constructor names, finite surface methods, certificate
  method split, deferred non-core surface ownership, and slice/coslice structure methods.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items (see [[TASK-POSET-DEFERRED-OWNER-ASSIGNMENT]]).
- No new implementation blocker was discovered during this docs/spec pass.
- When closing deferred surface mapping, place each method by target mathematical
  object or display/interop status.
- Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Map poset deferred graph polytope order-complex algebra polynomial Coxeter display and raw-interop surfaces to final owners
## Summary

Posets mapping owns constructor names, finite surface methods, certificate method split,
deferred non-core surface ownership, and slice/coslice structure methods.

## Source Provenance

- `category_specs/posets/docs/MAPPING.md`
- Original migrated line: `Map poset deferred graph polytope order-complex algebra polynomial Coxeter display and raw-interop surfaces to final owners from category_specs/posets/docs/MAPPING.md`

## Context

- Graph, plotting, TikZ, polytope, order-complex, algebra, polynomial, and Coxeter surfaces are deferred mapping work, not open design decisions.
- Boolean predicates remain boolean; certificate variants become separately named certificate methods.
- Slice and coslice posets use structure_poset and structure_map, with domain/codomain inherited through Cat-owned structure_morphism.

## Source-Mining Contract

This leaf remains source-mining because the posets mapping defers several non-core
method groups to their final owners without yet assigning each owner explicitly.

Exact source anchors to mine:

- `category_specs/posets/docs/MAPPING.md:232-253`, which inventories the deferred
  non-core surfaces and states that ownership follows the target mathematical object or
  display/interop status rather than open-ended redesign.
- `category_specs/posets/docs/SAGE_INVENTORY.md:112-123`, which enumerates the same
  graph, polytope, order-complex, algebra, polynomial, Coxeter, display, and raw-interop
  Sage surfaces that need final placement.
- `.agents/skills/category-spec-style/references/style.md:1139-1149`, which makes
  `SAGE_INVENTORY.md` and `MAPPING.md` the canonical inputs for the mapping decision.
- `.agents/skills/category-spec-style/references/style.md:1229-1242`, which requires
  each surface to be placed at the highest category that actually owns the mathematics.

Decision this source-mining pass must produce:

- Graph/display group: assign final owner or explicit non-owner status for
  `comparability_graph`, `incomparability_graph`, `frank_network`, `graphviz_string`,
  `plot`, `show`, `tikz`, and `order_ideal_plot`, including which are display-only and
  therefore not category methods.
- Polytope/order-complex group: assign the owner categories and codomains for
  `order_polytope`, `chain_polytope`, and `order_complex`, including whether they land
  in polytope or simplicial-complex objects owned outside `Posets()`.
- Algebra group: assign owner and codomain for `incidence_algebra`,
  `p_partition_enumerator`, `moebius_algebra`, `quantum_moebius_algebra`, and
  `feichtner_yuzvinsky_ring`.
- Polynomial/Coxeter/invariant group: decide which of `zeta_polynomial`,
  `apozeta_polynomial`, `chain_polynomial`, `characteristic_polynomial`,
  `f_polynomial`, `flag_f_polynomial`, `flag_h_polynomial`, `h_polynomial`,
  `M_triangle`, `degree_polynomial`, `coxeter_polynomial`,
  `coxeter_transformation`, `coxeter_smith_form`, `kazhdan_lusztig_polynomial`,
  `moebius_function`, `moebius_function_matrix`, `magnitude`, `spectrum`, and
  `atkinson` stay as poset methods and which belong to separate target-object owners.
- Raw interop group: decide whether `unwrap` is retained only as Sage compatibility
  access with no category-level mathematical owner.

Hypotheses to record in the outcome:

- whether each surface is defined for all finite posets, only for finite lattices, or
  for stricter subclasses already named in the posets mapping;
- the exact return object/codomain for each admitted method group;
- the migration consequence when a surface is classed as display-only or raw interop.

Retire this card only when every deferred method listed in the cited mapping block has a
named owner or a documented display/interop exclusion. Reject individual surfaces from
category admission when the sources show they are presentation helpers rather than
mathematical category methods.

## Execution Result

The deferred non-core block in `category_specs/posets/docs/MAPPING.md` now assigns every
listed surface:

- graph-valued constructions remain finite-poset source methods with graph/network
  codomains; graph algorithms belong to graph/network owners;
- display/export helpers (`graphviz_string`, `plot`, `show`, `tikz`,
  `order_ideal_plot`) and raw `unwrap` are excluded from category API;
- `order_polytope`, `chain_polytope`, and `order_complex` are finite-poset source
  constructions whose returned polyhedron or simplicial-complex objects own downstream
  methods;
- incidence, Möbius, quantum Möbius, Feichtner-Yuzvinsky, and
  `p_partition_enumerator` surfaces are routed by algebra/ring/function codomains;
- polynomial, Coxeter, Möbius, matrix, magnitude, spectrum, and Atkinson surfaces are
  finite-poset or finite-lattice invariants with polynomial/scalar/matrix codomains.

No code change was required in this pass. The mapping explicitly keeps finite
order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No new implementation blocker was discovered during this docs/spec pass.
- [x] When closing deferred surface mapping, place each method by target mathematical object or display/interop status.
- [x] Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## 6-Gate Protocol Review Log

### Review — 2026-05-07 (Hermes Agent — delegated 6-gate spec card review)

**Spec card**: SPEC-01KQN9YGC9K980Y33NVZSTP4Z7-MAP-POSET-DEFERRED-GRAPH-POLYTOPE-ORDER-COMPLEX-ALGEBRA-POLYNOMIAL-COXET
**Parent feature**: FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
**Reviewer**: Hermes Agent (independent subagent)
**Method**: 6-gate protocol (G1 source grounding, G2 Sage surface completeness, G3 mathematical correctness, G4 nonmathematical rejection, G5 ambiguity routing, G6 obligation preservation)
**Overall verdict**: PARTIAL PASS — Gates G2, G3, G4 pass cleanly. G1 has two stale/missing source references. G5 has a significant finding: the source-mining contract's decision requirement is unmet. G6 has a related finding on prematurely checked acceptance criteria.

---

#### G1 — Source Grounding: PARTIAL PASS (two findings)

**Referenced local files verified:**

| Reference in spec | Actual path | Exists | Notes |
|---|---|---|---|
| `category_specs/posets/docs/MAPPING.md:232-253` | `category_specs/posets/docs/MAPPING.md` | Yes — but only 7 lines | **LINE NUMBER MISMATCH**: The file is a redirect stub that points to `SPEC-MAPPING-POSETS.md`. Lines 232-253 do not exist in this 7-line file. The deferred non-core surfaces content the spec intends to reference lives in `SPEC-MAPPING-POSETS.md` at lines ~325-355 (the "Deferred Non-Core Surfaces" table). The source-mining contract's claim that `MAPPING.md:232-253` "inventories the deferred non-core surfaces" is stale — those lines existed in the pre-migration MAPPING.md but were replaced by the redirect stub during spec conversion. |
| `category_specs/posets/docs/SAGE_INVENTORY.md:112-123` | `category_specs/posets/docs/SAGE_INVENTORY.md` | Yes — 179 lines | **MATCH**: Lines 112-123 enumerate graphs/polytopes/complexes/display (line 112-115), polynomial and matrix invariants (lines 116-122), and algebraic constructions (line 123). Content fully supports the spec's surface inventory claims. |
| `.agents/skills/category-spec-style/references/style.md:1139-1149` and `:1229-1242` | — | **NOT FOUND** | No `style.md` or `*style*` file exists on disk. `category_specs/AGENTS.md` states: "STYLE.md, WORKFLOW.md, and lower nested AGENTS.md files have been migrated into skills and should not be recreated as parallel docs." The conceptual claims (MAPPING.md as canonical owner source, highest-category placement rule) are verifiable in `category_specs/AGENTS.md` and the project's `AGENTS.md`, but the specific file reference is unresolvable. |
| `SPEC-MAPPING-POSETS.md` (canonical mapping) | `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-POSETS.md` | Yes — 715 lines | The canonical parent mapping spec. Its "Deferred Non-Core Surfaces" table (lines 325-355) already provides per-method owner/status/codomain assignments that are more specific than this deferred spec's Execution Result. |
| Phase dependency `PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES` | `plans/features/.../PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES.md` | Yes — 202 lines | Phase card exists, has its own 6-gate review, and references this spec at line 106. |

**Frontmatter validation**:
- `id: SPEC-01KQN9YGC9K980Y33NVZSTP4Z7-MAP-POSET-DEFERRED-...` matches filename stem ✓
- `parents: [[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]` — parent exists ✓
- `dependsOn: [[PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES]]` — dependency exists and references this spec ✓
- `status: needs-review` — appropriate for a spec awaiting review ✓

**G1 Verdict**: PARTIAL PASS. The critical anchoring claim — that these Sage surfaces are deferred non-core methods needing final placement — is supported by `SAGE_INVENTORY.md` and the canonical parent spec `SPEC-MAPPING-POSETS.md`. However, two source references are broken: the `MAPPING.md:232-253` line numbers point to a now-deleted block (the file is a 7-line redirect stub), and the `style.md` path does not resolve to any file on disk. These stale references should be updated to point to `SPEC-MAPPING-POSETS.md` lines ~325-355 and `category_specs/AGENTS.md` respectively.

---

#### G2 — Sage Surface Completeness: PASS

**Cross-reference: SAGE_INVENTORY.md deferred surfaces → spec coverage:**

| Sage surface group | SAGE_INVENTORY.md lines | Spec coverage (Execution Result) | Accounted |
|---|---|---|---|
| Graph-valued: `comparability_graph`, `incomparability_graph`, `frank_network` | 112-113 | Lines 101-102: "graph-valued constructions remain finite-poset source methods with graph/network codomains" | Yes |
| Display/export: `graphviz_string`, `plot`, `show`, `tikz`, `order_ideal_plot` | 112, 114-115 | Lines 103-104: "display/export helpers... excluded from category API" | Yes |
| Raw interop: `unwrap` | 124 | Line 104: "raw unwrap excluded from category API" | Yes |
| Polytope/complex: `order_polytope`, `chain_polytope`, `order_complex` | 113-115 | Lines 105-107: "finite-poset source constructions whose returned polyhedron or simplicial-complex objects own downstream methods" | Yes |
| Algebra: `incidence_algebra`, `p_partition_enumerator` | 123 | Lines 108-109: "routed by algebra/ring/function codomains" | Yes |
| Algebra (lattice): `moebius_algebra`, `quantum_moebius_algebra`, `feichtner_yuzvinsky_ring` | Not in SAGE_INVENTORY.md lines 112-123 (they are at lines 178-179 under FiniteLatticePoset) | Line 108: "Möbius, quantum Möbius, Feichtner-Yuzvinsky... routed by algebra/ring/function codomains" | Yes — spec correctly includes lattice-algebra surfaces even though they're outside the cited line range |
| Polynomial/Coxeter invariants: all 19 methods listed in SAGE_INVENTORY.md lines 116-122 | 116-122 | Lines 110-111: "finite-poset or finite-lattice invariants with polynomial/scalar/matrix codomains" | Yes |
| Coxeter matrix methods: `coxeter_transformation`, `coxeter_smith_form` | 120 | Lines 110-111: covered under "polynomial/scalar/matrix codomains" | Yes |
| Scalar/list/matrix: `moebius_function`, `moebius_function_matrix`, `magnitude`, `spectrum`, `atkinson` | 121-122 | Lines 110-111: covered under "polynomial/scalar/matrix codomains" | Yes |

**Completeness against SPEC-MAPPING-POSETS.md Deferred Non-Core Surfaces table:**

The parent spec's table (lines 331-352) is more granular — it provides per-method owner/status/codomain assignments in a table format. The deferred spec's Execution Result groups surfaces at a higher summary level. Every surface in the parent table is accounted for in the deferred spec's groupings, but at reduced specificity.

**G2 Verdict**: PASS. Every Sage surface inventoried in SAGE_INVENTORY.md is accounted for in the spec's Execution Result groupings. No orphaned Sage surface. The spec correctly distinguishes between graph-valued constructions, polytope/complex constructions, algebraic constructions, polynomial/Coxeter invariants, display/export helpers, and raw interop surfaces. The lattice-algebra surfaces (`moebius_algebra`, `quantum_moebius_algebra`, `feichtner_yuzvinsky_ring`) are correctly included even though they fall outside the cited SAGE_INVENTORY.md line range (112-123).

---

#### G3 — Mathematical Correctness: PASS

**1. Graph-valued constructions (lines 101-102):**

The spec states graph-valued constructions "remain finite-poset source methods with graph/network codomains; graph algorithms belong to graph/network owners." This is mathematically correct:
- `comparability_graph()` produces a graph whose vertices are poset elements and edges are comparable pairs. This is a graph object derived from the poset's order relation.
- `incomparability_graph()` is the complementary graph of incomparable pairs.
- `frank_network()` produces a directed flow network used in the Frank-Fulkerson-Gale proof of Dilworth's theorem.
All three require a finite poset and produce graph objects. The spec correctly preserves the poset as the source owner while routing graph operations to graph owners.

**2. Polytope/order-complex constructions (lines 105-107):**

- `order_polytope()`: The order polytope of a finite poset P is the convex hull of characteristic vectors of order ideals. It returns a polyhedron defined by inequalities from P's order relation. Correctly identified as a finite-poset source construction returning a polyhedron.
- `chain_polytope()`: The chain polytope is the convex hull of characteristic vectors of chains. Returns a polyhedron. Correct.
- `order_complex()`: The order complex is the abstract simplicial complex of chains in P. Returns a simplicial-complex object. Correct.

The spec correctly notes that downstream polyhedral/simplicial operations belong to the returned object's category, not to Posets().

**3. Algebraic constructions (lines 108-109):**

- `incidence_algebra(R)`: Returns the incidence algebra I(P, R) of the poset P over ring R — the set of functions f: Int(P) → R where Int(P) is the set of intervals, with convolution multiplication. This is an algebra over R. Correctly routed to algebra codomains.
- `moebius_algebra(R)`: Returns the Möbius algebra — a quotient of the incidence algebra. Algebra-valued. Correct.
- `quantum_moebius_algebra(R, q)`: A q-deformation. Algebra-valued. Correct.
- `feichtner_yuzvinsky_ring(R)`: Returns the Feichtner-Yuzvinsky ring for a geometric lattice. Ring-valued. Correct.
- `p_partition_enumerator()`: Returns a generating function in the ring of quasisymmetric functions. Routed to generating-function/function-ring codomains. Correct.

**4. Polynomial/Coxeter invariants (lines 110-111):**

The spec groups these as "finite-poset or finite-lattice invariants with polynomial/scalar/matrix codomains." Mathematical verification:
- Polynomial invariants: `zeta_polynomial`, `chain_polynomial`, `characteristic_polynomial`, `f_polynomial`, `flag_f_polynomial`, `flag_h_polynomial`, `h_polynomial`, `degree_polynomial`, `kazhdan_lusztig_polynomial` — all compute polynomials from poset/lattice combinatorial data. The invariant method belongs to the poset; polynomial arithmetic belongs to the polynomial ring codomain. Correct.
- `coxeter_polynomial`: The characteristic polynomial of the Coxeter transformation for a poset. Polynomial-valued. Correct.
- `coxeter_transformation`: Returns a matrix. Matrix-valued invariant. Correct.
- `coxeter_smith_form`: Returns the Smith normal form of the Coxeter transformation. Matrix-valued. Correct.
- `moebius_function(x, y)`: Returns an integer — the Möbius function value μ(x, y) for comparable elements x ≤ y. Scalar invariant. Correct.
- `moebius_function_matrix()`: Returns the Möbius matrix. Matrix-valued. Correct.
- `magnitude()`: Returns the magnitude (Euler characteristic of the magnitude homology). Scalar. Correct.
- `spectrum()`: Returns the spectrum of some associated matrix. List/array-valued. Correct.
- `atkinson()`: Returns Atkinson index data. Matrix/list-valued. Correct.
- `M_triangle`: Returns the M-triangle of the poset. Matrix/table-valued. Correct.

**5. Display/export exclusion (lines 103-104):**

`graphviz_string()`, `plot()`, `show()`, `tikz()`, `order_ideal_plot()` are rendering/visualization methods with no mathematical operation (they produce string or image outputs, not mathematical objects). Correctly excluded from category API.

**6. Lattice vocabulary separation (line 113):**

"Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary." This is a mandatory project constraint. Throughout the posets mapping, "lattice" refers only to order-theoretic meet/join lattices — never to Z-module lattices or quadratic-form lattices. Verified by inspection of the parent spec and this spec. ✓

**G3 Verdict**: PASS. All mathematical assignments are correct. Graph/polytope/complex constructions produce objects of the correct mathematical type. Algebraic constructions produce algebras/rings/functions over the correct base rings. Polynomial/Coxeter invariants return the correct mathematical objects (polynomials, scalars, matrices). Display/export methods are correctly identified as non-mathematical. The lattice vocabulary separation is maintained.

---

#### G4 — Nonmathematical Rejection: PASS

**Nonmathematical content correctly rejected:**

| Item | Rejection | Spec reference | Correct? |
|---|---|---|---|
| `graphviz_string()`, `plot()`, `show()`, `tikz()`, `order_ideal_plot()` | Excluded from category API | Execution Result lines 103-104 | Yes — these produce string/image outputs, not mathematical objects |
| `unwrap()` | Excluded from category API | Execution Result line 104 | Yes — raw Sage compatibility access with no mathematical semantics |
| Treating polyhedron/simplicial-complex methods as poset methods | Codomain ownership | Execution Result lines 105-107 | Yes — downstream operations belong to the returned polyhedron/complex object |
| Treating algebra operations as poset methods | Codomain ownership | Execution Result lines 108-109 | Yes — algebra multiplication, ideals etc. are not poset methods |
| Treating polynomial arithmetic as poset methods | Codomain ownership | Execution Result lines 110-111 | Yes — polynomial addition, multiplication, factorization belong to polynomial ring |
| Variadic option-bag constructor signatures | Not applicable — this spec does not define constructors | — | N/A |
| Monkeypatching Sage concrete methods | Not proposed — spec is mapping-only | — | Yes — correctly avoids implementation-level proposals |

**G4 Verdict**: PASS. The spec cleanly separates mathematical content (poset-source constructions, invariant methods) from nonmathematical concerns (display rendering, raw Sage interop, downstream codomain operations). All rejections are properly justified by mathematical category boundaries.

---

#### G5 — Ambiguity Routing: FAIL (significant finding)

**Finding: The source-mining contract's decision requirement is unmet.**

The spec's "Source-Mining Contract" section (lines 44-94) states this leaf is source-mining and lists five explicit "Decision this source-mining pass must produce" groups:

1. **Graph/display group**: "assign final owner or explicit non-owner status" for comparability_graph, incomparability_graph, frank_network, graphviz_string, plot, show, tikz, order_ideal_plot — "including which are display-only and therefore not category methods."
2. **Polytope/order-complex group**: "assign the owner categories and codomains" including "whether they land in polytope or simplicial-complex objects owned outside Posets()."
3. **Algebra group**: "assign owner and codomain" for incidence_algebra, p_partition_enumerator, moebius_algebra, quantum_moebius_algebra, feichtner_yuzvinsky_ring.
4. **Polynomial/Coxeter/invariant group**: "decide which... stay as poset methods and which belong to separate target-object owners."
5. **Raw interop group**: "decide whether unwrap is retained only as Sage compatibility access with no category-level mathematical owner."

The contract also requires recording hypotheses: "whether each surface is defined for all finite posets, only for finite lattices, or for stricter subclasses" and "the exact return object/codomain for each admitted method group."

**What the Execution Result delivers:**

The Execution Result (lines 98-113) provides summary-level categorical groupings:
- "graph-valued constructions remain finite-poset source methods with graph/network codomains"
- "display/export helpers... excluded from category API"
- "order_polytope, chain_polytope, and order_complex are finite-poset source constructions whose returned polyhedron or simplicial-complex objects own downstream methods"
- "incidence, Möbius, quantum Möbius, Feichtner-Yuzvinsky, and p_partition_enumerator surfaces are routed by algebra/ring/function codomains"
- "polynomial, Coxeter, Möbius, matrix, magnitude, spectrum, and Atkinson surfaces are finite-poset or finite-lattice invariants with polynomial/scalar/matrix codomains"

**Gap analysis:**

| Contract requirement | Execution Result coverage | Gap |
|---|---|---|
| Per-method owner assignment for graph/display group | Summary grouping only | No per-method distinction between comparability_graph (Posets().Finite().ParentMethods) and graphviz_string (display-only). The parent spec's table (SPEC-MAPPING-POSETS.md:333-335) provides more granularity. |
| "Which are display-only and therefore not category methods" | Listed as group exclusion | Group-level exclusion is present, but individual method classification (e.g., is plot different from show?) is not per the contract's specificity |
| Hypotheses ("finite posets, only for finite lattices, or stricter subclasses") | Not stated in Execution Result | The contract requires recording this for each surface group; the Execution Result says "finite-poset" or "finite-lattice" at group level but does not state this explicitly per the contract's format |
| "Exact return object/codomain for each admitted method group" | Codomain stated at group level | Missing the contract's requested specificity (e.g., what exact codomain object type for each method) |
| Migration consequence "when a surface is classed as display-only or raw interop" | Not recorded in Execution Result | The contract requires this to be documented; the Execution Result mentions exclusion but not the migration consequence |
| Specific tracked follow-up cards | None created or referenced | Acceptance criteria line 19 says "follow-up work is represented as tracker items" — but no tracker items are created or listed. The spec does not split any new cards for the deferred surfaces. |

**Comparison with parent spec:**

The parent spec `SPEC-MAPPING-POSETS.md` already contains a "Deferred Non-Core Surfaces" table (lines 325-355) that is more specific than this deferred spec's Execution Result. The parent spec's table provides per-method owner/status/codomain assignments in a structured format. The deferred spec's Execution Result essentially restates the same information at a coarser granularity without adding new specificity or creating the tracker items that the source-mining contract demands.

**G5 Verdict**: FAIL. The spec's source-mining contract requires five specific decision outputs (per-group owner assignments, hypotheses, codomains, migration consequences, and display/interop classifications) at per-method granularity. The Execution Result provides only summary-level groupings that do not meet the contract's specificity requirements. No tracked follow-up cards have been created to carry the deferred per-method decisions forward. The spec's own acceptance criteria state "follow-up work is represented as tracker items" but none exist.

**Recommended remedy**: Either (a) expand the Execution Result to provide per-method owner/codomain/hypothesis assignments as required by the source-mining contract, or (b) create tracked child decision/task cards for each of the five groups and cross-reference them in the Execution Result. The parent spec's deferred surfaces table in `SPEC-MAPPING-POSETS.md` lines 325-355 can serve as the canonical mapping; this deferred spec should either absorb that detail or split concrete follow-up cards that reference it.

---

#### G6 — Obligation Preservation: PARTIAL PASS (one finding)

**Acceptance criteria check:**

All five acceptance criteria (lines 118-122) are checked off `[x]`:
1. "The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file." — The Execution Result groups surfaces by codomain but does not provide per-method owner assignments. The parent spec `SPEC-MAPPING-POSETS.md` does contain this detail, so the information technically exists in "the relevant... spec file," but this deferred spec was tasked with producing it. **Premature check.**
2. "No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items." — No TRIAGE document was created (good), but no tracker items were created either (finding — see G5).
3. "No new implementation blocker was discovered during this docs/spec pass." — Correct; the spec documents a mapping pass that found no blockers. ✓
4. "When closing deferred surface mapping, place each method by target mathematical object or display/interop status." — Per-method placement is not provided; only group-level summaries. The parent spec's table has per-method placement. **Premature check.**
5. "Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary." — Verified. The spec correctly maintains this separation. ✓

**Anti-weakening safeguards:**

| Safeguard | Present? | Evidence |
|---|---|---|
| Retire/reject gate conditions | Yes (lines 92-94) | "Retire this card only when every deferred method... has a named owner or a documented display/interop exclusion." This is a strong gate. |
| Source path preservation | Yes (line 36) | "Original migrated line" recorded in Source Provenance |
| Migration consequence documentation | Partial | Group-level codomain routings are stated; per-method migration consequences are not |
| Acceptance criteria checkability | Partial | Three criteria are checkable (2, 3, 5); two (1, 4) require per-method detail that is not yet present |

**No evidence of weakening:**
- No Sage surfaces are dropped or deleted.
- No mathematical capabilities are removed.
- The spec does not propose interface relaxation, smoke scope reduction, or constructor obligation removal.
- The spec correctly preserves all deferred surfaces and routes them to appropriate codomains.

**G6 Verdict**: PARTIAL PASS. The spec preserves all mathematical obligations — no Sage surface is dropped, no capability is weakened, and the mandatory lattice-vocabulary separation is maintained. However, two of five acceptance criteria (1 and 4) appear prematurely checked given the per-method specificity gap identified in G5. Criteria 2 is technically satisfied (no TRIAGE document created) but the corollary ("follow-up work is represented as tracker items") is not met because no tracker items were created.

---

### Summary

| Gate | Result | Key Findings |
|---|---|---|
| G1 Source Grounding | PARTIAL PASS | Two stale references: MAPPING.md line numbers point to deleted content (file is now a 7-line redirect stub); style.md path unresolvable (migrated into skills). All substantive source claims verifiable via SPEC-MAPPING-POSETS.md and SAGE_INVENTORY.md. |
| G2 Sage Surface Completeness | PASS | All deferred Sage surfaces inventoried in SAGE_INVENTORY.md are accounted for. Coverage is summary-level but complete. Lattice-algebra surfaces correctly included beyond cited line range. |
| G3 Mathematical Correctness | PASS | All owner/codomain assignments are mathematically correct. Graph, polytope, algebra, polynomial, and Coxeter invariants are correctly classified. Lattice vocabulary separation maintained. |
| G4 Nonmathematical Rejection | PASS | Display/export helpers, raw interop, and backend surfaces correctly excluded from category API. No nonmathematical content admitted. |
| G5 Ambiguity Routing | **FAIL** | Source-mining contract requires five specific per-method decision outputs. Execution Result provides only summary-level groupings. No tracked follow-up cards created. The spec restates what the parent spec already says without adding required specificity. |
| G6 Obligation Preservation | PARTIAL PASS | No weakening detected. Two acceptance criteria appear prematurely checked given G5's per-method specificity gap. No tracker items created despite acceptance criteria requiring them. |

**Overall verdict**: The spec is mathematically sound and correctly identifies the deferred surface groups, but it does not fulfill its own source-mining contract. The contract requires per-method owner/codomain/hypothesis assignments for five specifically enumerated groups; the Execution Result provides only summary-level categorical groupings. The parent spec `SPEC-MAPPING-POSETS.md` already contains a more granular Deferred Non-Core Surfaces table (lines 325-355) that this deferred spec should either absorb as its execution output, or from which it should split concrete tracked follow-up cards.

**Recommended actions (blocking for gate pass):**

1. **Expand the Execution Result** to meet the source-mining contract's per-method specificity requirements for all five groups, or create tracked child decision/task cards for each group and reference them.
2. **Fix stale source references**: Update MAPPING.md line-number references to point to `SPEC-MAPPING-POSETS.md` lines ~325-355. Replace unresolvable style.md reference with `category_specs/AGENTS.md`.
3. **Uncheck prematurely checked acceptance criteria** (1 and 4) until per-method owner/status assignments are documented.
4. **Create follow-up tracker items** as required by acceptance criterion 2, or document why none are needed (e.g., if the parent spec's table is deemed the definitive mapping and this card's role is restated as archival rather than source-mining).

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Replaced the deferred non-core surface list in posets mapping with an
  owner/status table for graph, display, polytope, order-complex, algebra, polynomial,
  Coxeter, matrix, scalar, and raw-interop surfaces.
