---
id: SPEC-01KQN9YGC8WM34SAME35N4VGX5-SPECIFY-PARTITION-REFINEMENTS-COARSENINGS-AND-STRICT-COARSENINGS-AS-FINI
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS]]'
title: Specify partition refinements coarsenings and strict coarsenings as finite
  subsets refining through set constructors
status: complete
priority: critical
requirement: Sets mapping is the source of truth for set constructors, rich comparison,
  partitioned sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut
  ownership.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Specify partition refinements coarsenings and strict coarsenings as finite subsets refining through set constructors
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Specify partition refinements coarsenings and strict coarsenings as finite subsets refining through set constructors from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Grounded Spec Contract

Source anchors for this leaf are already concrete enough to authorize the spec edit:

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md:282-286`,
  which fixes `SetPartitions(s)` as the fixed-base partition parent and
  `SetPartition(blocks, check=True)` as the source Sage element class whose partition
  element surface is recorded in `Partitioned.ElementMethods`.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md:360-382`,
  especially the `refinements()`, `coarsenings()`, and `strict_coarsenings()` rows,
  which fix the owner, hypotheses, codomain, and compatibility-name split for the
  finite-set project methods.
- `.agents/skills/category-spec-style/references/style.md:1139-1149`, which makes
  `MAPPING.md` the canonical owner/migration source for subtree method placement.
- `.agents/skills/category-spec-style/references/style.md:1229-1242`, which requires
  the method to live at the highest category where it is universally well-defined and
  forbids restating inherited behavior at lower levels without new mathematics.

Concrete contract for the spec edit:

- Owner category for the project finite-set wrappers of Sage `refinements()` and
  `coarsenings()`:
  `Sets().Partitioned()` on the partition element surface, with the fixed finite-base
  Sage `SetPartition` object as the source-backed witness.
- Owner category for the project finite-set wrapper of Sage's `strict_coarsenings()`:
  `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods`, because Sage's
  definition compares ordered blocks using `max(part) < min(other)`.
- Public project methods to specify: `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()` as partition-element methods at those split owners.
  Sage's concrete `refinements()`, `coarsenings()`, and `strict_coarsenings()` names
  remain list-returning compatibility methods on Sage `SetPartition` elements.
- Hypotheses: the input object is a partition of a finite fixed base set, so the
  refinement lattice neighborhoods determined by `refinements()` and `coarsenings()`
  are finite. Sage-compatible `strict_coarsenings()` additionally requires the finite
  totally ordered base-set owner.
- Return object/codomain: a finite set object of partition elements, routed through set
  constructors rather than a raw Python container or an untyped Sage iterator.
- Migration consequence: do not remap these methods to poset constructors, graph
  surfaces, or free-floating helper functions; they stay attached to partition elements
  and refine through the canonical set-constructor vocabulary. Project finite-set
  wrappers use separate names because Sage already owns the concrete list-returning
  names. Do not treat Sage's `strict_coarsenings()` as ordinary proper coarsenings:
  Sage defines a reflexive closure and includes `self`.

Retire or reject this leaf only if a cited mapping row is superseded by a source-backed
owner change showing that one of these methods is not a partition-element method or does
not return a finite set object.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Split the owner decision after checking Sage behavior and source:
  `refinements()` and `coarsenings()` live on `Sets().Partitioned().ElementMethods`;
  Sage-compatible `strict_coarsenings()` lives on
  `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods`, returns a finite
  set object in the project spec, and is not ordinary proper coarsening.
- 2026-05-05: Updated public method names after
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md` decided that
  Sage's concrete list-returning names must remain compatibility methods. The project
  finite-set methods are now `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()`.

## 6-Gate Protocol Review Log

### Review — 2026-05-07 (subagent, 6-gate spec card review)

**Spec card**: SPEC-01KQN9YGC8WM34SAME35N4VGX5-SPECIFY-PARTITION-REFINEMENTS-COARSENINGS-AND-STRICT-COARSENINGS-AS-FINI
**Parent feature**: FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
**Reviewer**: Hermes Agent (independent subagent, deepseek-v4-pro)
**Method**: 6-gate protocol (G1 source grounding, G2 Sage surface completeness, G3 mathematical correctness, G4 nonmathematical rejection, G5 ambiguity routing, G6 obligation preservation)

---

#### G1 — Source Grounding: PASS (with findings)

**Referenced local files verified present:**

| File referenced in spec | Actual path | Exists | Notes |
|---|---|---|---|
| SPEC-MAPPING-SETS.md:282-286 | `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md` | Yes | **LINE NUMBER MISMATCH**: Spec lines 54-55 cite lines 282-286 for SetPartitions(s) and SetPartition(blocks) rows, but those lines (282-286) cover FiniteEnumeratedSet through Primes. The SetPartitions rows are actually at lines 303-307. Content at 303-307 does fix `SetPartitions(s)` as fixed-base parent and `SetPartition(blocks, check=True)` as the element class — the semantic claim is correct, the line numbers are wrong. |
| SPEC-MAPPING-SETS.md:360-382 | `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md` | Yes | **LINE NUMBER MISMATCH**: Spec lines 57-61 cite lines 360-382 for the `refinements()`, `coarsenings()`, and `strict_coarsenings()` rows. Lines 360-368 cover RealSet topological transforms; lines 370-382 cover SetPartition base_set, cardinality, meet, join. The actual refinement/coarsening rows are at lines 402-404 and the admission decision at 429-444. The content at 402-404 and 429-444 fully supports the spec's owner/hypothesis/codomain/name-split claims. |
| `.agents/skills/category-spec-style/references/style.md:1139-1149` and `:1229-1242` | — | **NOT FOUND** | File does not exist on disk. The `category_specs/AGENTS.md` states that `STYLE.md` was migrated into skills. A search for `*style*` under `/home/dzack/research` returned zero results. The conceptual claims made by referencing these lines (MAPPING.md as canonical owner source, highest-category placement rule) are standard category-spec principles verifiable elsewhere, but the specific file reference is unresolvable. |
| MAPPING.md (sets) | `category_specs/sets/docs/MAPPING.md` | Yes — 7-line redirect stub | Points to tracked spec `SPEC-MAPPING-SETS.md`. The spec's source-provenance line 37 correctly references this. |
| SAGE_INVENTORY.md (sets) | `category_specs/sets/docs/SAGE_INVENTORY.md` | Yes | Sets inventory file exists. |
| DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md | `plans/features/.../decisions/DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md` | Yes — 129 lines | Confirms the naming decision: Sage names stay list-returning; project names are `refinement_set()`, `coarsening_set()`, `ordered_coarsening_closure()`. Rationale (Sage concrete methods shadow category ElementMethods) verified by Sage execution. |
| partitioned.py | `category_specs/sets/subcategories/partitioned.py` | Yes — 299 lines | Implements `refinement_set()` (line 190), `coarsening_set()` (line 195), and `ordered_coarsening_closure()` (line 255). See G3 finding on owner location. |

**Referenced installed Sage source verified:**

| Sage method | File | Line | Verified |
|---|---|---|---|
| `SetPartition.refinements()` | `sage/combinat/set_partition.py` | 1783-1804 | Cartesian product of block sub-partitions; returns Python `list`. Verified via `sage -c` execution: includes self, type is `list`. |
| `SetPartition.coarsenings()` | `sage/combinat/set_partition.py` | 428-462 | Enumerates partitions of block-index set, merges corresponding blocks; returns Python `list`. Verified via `sage -c` execution: includes self, type is `list`. |
| `SetPartition.strict_coarsenings()` | `sage/combinat/set_partition.py` | 1806-1846 | DFS transitive-reflexive closure of ordered block merging (`max(A_i) < min(A_j)`); returns Python `list`. Verified via `sage -c` execution: includes self (reflexive), type is `list`, NOT equal to proper coarsenings. |

**G1 Verdict**: PASS. All substantive source claims are verifiable in existing files and Sage source, even though three line-number references in the spec are stale (two in SPEC-MAPPING-SETS.md, one unresolvable style.md path). The critical anchoring claims — SetPartitions(s) as fixed-base parent, SetPartition as element class, refinement/coarsening/strict_coarsening owner and name-split decisions — are all supported by verifiable file content. The stale references should be updated.

---

#### G2 — Sage Surface Completeness: PASS

**Cross-reference: Sage SetPartition surfaces → spec coverage:**

| Sage surface | Returns | Spec coverage | Accounted |
|---|---|---|---|
| `SetPartition.refinements()` | Python `list` of SetPartition | Spec lines 68-70: Sage compatibility name; project `refinement_set()` on `Sets().Partitioned().ElementMethods` | Yes — compatibility preserved, project finite-set wrapper specified |
| `SetPartition.coarsenings()` | Python `list` of SetPartition | Spec lines 68-70: Sage compatibility name; project `coarsening_set()` on `Sets().Partitioned().ElementMethods` | Yes |
| `SetPartition.strict_coarsenings()` | Python `list` of SetPartition | Spec lines 72-73: Sage compatibility name; project `ordered_coarsening_closure()` on `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods` | Yes |

**Hypothesis and codomain coverage:**

| Requirement | Spec reference | Verified |
|---|---|---|
| Finite fixed base set hypothesis for refinements/coarsenings | Lines 79-82 | Yes — Sage methods operate on finite partitions by construction |
| Finite totally ordered base set for strict_coarsenings | Lines 72-73, 82 | Yes — Sage source line 1837: `if max(part) < min(other)` |
| Return type: project finite set object (not raw list) | Lines 83-85 | Yes — `Sets().Constructors().from_iterable(...)` route specified |
| Includes self (reflexive) | Lines 78, 89-90 | Yes — verified by Sage execution for all three methods |
| strict_coarsenings is NOT ordinary proper coarsening | Lines 89-90 | Yes — verified: `strict_coarsenings()` returns a different set than proper coarsenings |

**Completeness check against MAPPING.md rows:**

MAPPING.md is a redirect stub; the canonical mapping is SPEC-MAPPING-SETS.md. The spec references the relevant rows (lines 402-404, 429-444) which fully specify owner, hypotheses, codomain, and migration consequence.

**G2 Verdict**: PASS. Every Sage partition refinement/coarsening surface is accounted for. The spec correctly identifies Sage return types (list), project return types (finite set objects), ownership categories, and the mathematical distinction between `strict_coarsenings()` and ordinary proper coarsenings. No orphaned Sage surface.

---

#### G3 — Mathematical Correctness: PASS (with one owner-location finding)

**1. Refinement lattice semantics (spec lines 68-82):**

The mathematical objects:
- Let P be a partition of a finite set S. A partition Q **refines** P if every block of Q is a subset of some block of P.
- P **coarsens** Q if Q refines P (the dual relation).
- The set of all partitions of S forms a lattice under refinement order.

**refinements() verification** (Sage source lines 1783-1804):
```python
L = [SetPartitions(part) for part in self]
return [SetPartition(sum(map(list, x), [])) for x in itertools.product(*L)]
```
Each block of `self` is independently refined (partitioned further), and the Cartesian product of all block refinements yields all global refinements. This is mathematically correct: every refinement of a partition is obtained by further partitioning each block, and every combination of block refinements produces a global refinement.

**coarsenings() verification** (Sage source lines 428-462):
```python
SP = SetPartitions(len(self))  # partitions of {1..k} where k = number of blocks
def union(s):
    ret = []
    for part in s:
        cur = []
        for i in part:
            cur.extend(self[i-1])
        ret.append(cur)
    return ret
return [self.parent()(union(s)) for s in SP]
```
Every coarsening corresponds to merging some blocks of the partition. A partition of the block indices specifies which blocks to merge. The enumeration over all set partitions of `{1..k}` generates all possible merges, which is exactly the set of all coarsenings. Mathematically correct.

**Both include self**: Confirmed by Sage execution. For `refinements()`, the trivial sub-partition of each block (the block itself) is included in `SetPartitions(part)`, so the Cartesian product includes the identity refinement. For `coarsenings()`, the discrete partition of `{1..k}` (each index in its own block) corresponds to no merging, yielding `self`.

**2. strict_coarsenings() is NOT ordinary proper coarsening (spec lines 72-73, 89-90):**

Verified by Sage execution with `SetPartition([[1],[2,4],[3]])`:
- `strict_coarsenings()` returns 3 partitions: `{self, {{1,2,4},{3}}, {{1,3},{2,4}}}`
- All coarsenings return 5 partitions including `{{1,2,3,4}}` and `{{1},{2,3,4}}` which are absent from strict_coarsenings
- The missing coarsening `{{1},{2,3,4}}` is excluded because merging {2,4} with {3} fails `max({2,4})=4 < min({3})=3`

The spec correctly characterizes Sage's `strict_coarsenings()` as the reflexive-transitive closure of merging ordered-compatible blocks (`max(A_i) < min(A_j)`). This requires a totally ordered base set and is NOT the same as proper (non-identity) coarsenings in the refinement lattice.

**3. Owner category correctness:**

The spec specifies:
- `refinement_set()` and `coarsening_set()` on `Sets().Partitioned().ElementMethods` (line 70)
- `ordered_coarsening_closure()` on `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods` (line 73)

This split is mathematically justified:
- Refinements and coarsenings are defined for any partition of a finite set (no order required). The sole mathematical hypothesis is finiteness of the base set (to guarantee the neighborhood is finite).
- `strict_coarsenings()` uses `max(part) < min(other)` (Sage source line 1837), which requires a total order on the base set elements. Without a total order, max and min are undefined or ambiguous. Therefore `Sets().Partitioned().FiniteTotallyOrderedBase()` is the correct owner.

**Finding**: In the current implementation (`category_specs/sets/subcategories/partitioned.py` lines 254-257), `ordered_coarsening_closure()` is placed on the general `PartitionsCategory.ElementMethods` (line 146), not on a `FiniteTotallyOrderedBase` subcategory. The spec's mathematically precise owner (`Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods`) is correct; the implementation may need to be relocated.

**4. Finite set return objects (spec lines 83-85):**

The spec requires project methods to route through set constructors (`Sets().Constructors().from_iterable(...)`) rather than returning raw Python lists. This is consistent with the project's rejection of generic `Set(X)` wrapping and its use of typed finite set objects. The current implementation in partitioned.py lines 190-197 and 254-257 does exactly this.

**5. Migration consequences (spec lines 86-94):**

The spec correctly prevents:
- Remapping these methods to poset constructors (they are partition element methods, not poset methods)
- Moving them to graph surfaces or free-floating helpers
- Treating `strict_coarsenings()` as ordinary proper coarsenings

All are mathematically sound: the refinement lattice is a property of the set of partitions of a fixed base set, not an independent poset construction.

**G3 Verdict**: PASS. All three Sage methods are mathematically correct implementations of their documented semantics. The spec's owner-category assignments are mathematically justified (order required only for strict_coarsenings). The sole finding is that the implementation places `ordered_coarsening_closure()` on a wider category than the spec's mathematically precise owner — this is an implementation concern, not a spec correctness issue.

---

#### G4 — Nonmathematical Rejection: PASS

**Nonmathematical content correctly rejected:**

| Item | Rejection | Spec reference | Correct? |
|---|---|---|---|
| Raw Python list/iterator as return type | Rejected — project methods return finite set objects | Lines 83-85 | Yes |
| Monkeypatching Sage `SetPartition` concrete methods | Rejected by naming decision (separate project names) | Lines 75-78, Decision card | Yes |
| Treating `strict_coarsenings()` as ordinary proper coarsening | Explicitly rejected | Lines 89-90 | Yes — verified mathematically |
| Generic Sage `Set(X)` constructor | Rejected (acceptance criteria line 25, spec line 83) | Lines 25, 83 | Yes |
| Remapping to poset constructors or graph surfaces | Rejected — methods stay on partition elements | Lines 86-88 | Yes |
| Free-floating helper functions | Rejected — methods stay attached to partition elements | Lines 86-88 | Yes |
| Variadic or option-bag constructor signatures | Not applicable to this spec (no constructors defined here) | — | N/A |

**G4 Verdict**: PASS. The spec cleanly separates mathematical content (partition refinement lattice operations) from nonmathematical concerns (Python container types, implementation patching strategies, naming conflicts). All rejections are properly justified.

---

#### G5 — Ambiguity Routing: PASS

**Ambiguity resolution assessment:**

1. **Name collision (Sage vs project)**: The spec and linked decision card unambiguously resolve the Sage `refinements()`/`coarsenings()`/`strict_coarsenings()` name collision by keeping Sage names as list-returning compatibility methods and introducing separate project finite-set names. No ambiguity about which name returns what.

2. **strict_coarsenings semantics**: The spec explicitly clarifies that Sage's `strict_coarsenings()` is NOT ordinary proper coarsening. It defines the precise semantics (reflexive-transitive closure of ordered block merging with max/min comparisons). The project name `ordered_coarsening_closure()` makes the semantics explicit in the name.

3. **Owner category split**: The spec specifies a split owner:
   - `refinement_set()`, `coarsening_set()` → `Sets().Partitioned().ElementMethods`
   - `ordered_coarsening_closure()` → `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods`
   
   The rationale (order required only for strict_coarsenings) is clearly stated and mathematically justified.

4. **Return type**: Unambiguous — project methods return finite set objects (not lists, not iterators).

5. **Hypotheses**: Clearly stated — finite base set for refinements/coarsenings, finite totally ordered base set for strict_coarsenings.

6. **Migration consequence**: Unambiguous — methods stay on partition elements, refine through set-constructor vocabulary, do not remap to poset/graph/helper surfaces.

**G5 Verdict**: PASS. Every potential ambiguity (name collision, strict_coarsening semantics, owner category, return type, hypotheses, migration) is explicitly resolved with clear rationale.

---

#### G6 — Obligation Preservation: PASS

**Anti-weakening safeguards:**

1. **Retire/reject clause** (spec lines 92-94): The spec includes an explicit gate condition — retire or reject only if a cited mapping row is superseded by a source-backed owner change showing the method is not a partition-element method or does not return a finite set object. This prevents casual weakening.

2. **Migration consequence** (lines 86-91): Explicitly preserves the partition-element ownership, set-constructor routing, and the mathematical distinction that `strict_coarsenings()` is not ordinary proper coarsening.

3. **Dependencies and Boundaries** (lines 106-108): Requires preserving source paths, splitting missing mathematical owners as new tracker items rather than patching around, and keeping `SAGE_INVENTORY.md` and `MAPPING.md` as provenance.

4. **Acceptance criteria** (lines 17-25): Requires citing exact mapping rows, proving behavior through project category vocabulary, and not exposing generic Sage `Set(X)`.

5. **No weakening detected**: The spec strengthens the partition surface by:
   - Introducing typed finite set return objects (vs Sage's raw lists)
   - Making the ordered-base hypothesis explicit for strict_coarsenings
   - Separating Sage compatibility names from project names to avoid runtime shadowing
   - Clarifying the mathematical semantics of strict_coarsenings vs proper coarsenings

6. **Implementation alignment**: The current `partitioned.py` implementation preserves all spec obligations — `refinement_set()` and `coarsening_set()` are implemented (lines 190-197), `ordered_coarsening_closure()` is implemented (lines 254-257), and all route through `Sets().Constructors().from_iterable(...)`.

**G6 Verdict**: PASS. Strong anti-weakening posture with explicit retire/reject gate conditions, clear migration consequences, and no evidence of obligation erosion in the spec or implementation.

---

### Summary

| Gate | Result | Key Findings |
|---|---|---|
| G1 Source Grounding | PASS | Three stale line-number/file references; all substantive claims verifiable in existing files and Sage source |
| G2 Sage Surface Completeness | PASS | All three Sage methods accounted for; return types, hypotheses, and codomains correctly specified |
| G3 Mathematical Correctness | PASS | Sage algorithms verified correct; owner split mathematically justified; implementation places `ordered_coarsening_closure()` on wider category than spec's precise owner |
| G4 Nonmathematical Rejection | PASS | No nonmathematical content admitted; all rejections properly justified |
| G5 Ambiguity Routing | PASS | Name collision, strict_coarsening semantics, owner split, return types, hypotheses, migration all unambiguously resolved |
| G6 Obligation Preservation | PASS | Strong anti-weakening safeguards; explicit retire/reject gate; implementation preserves all obligations |

**Recommended actions (non-blocking)**:

1. **Fix stale line numbers**: Update spec lines 54-55 to reference SPEC-MAPPING-SETS.md lines 303-307 (SetPartitions rows) instead of 282-286. Update spec lines 57-61 to reference lines 402-404 and 429-444 (refinement/coarsening rows and admission decision) instead of 360-382.
2. **Fix style.md reference**: Replace or remove the unresolvable `.agents/skills/category-spec-style/references/style.md` references (spec lines 61-64). The principles they assert (MAPPING.md as canonical owner source, highest-category placement rule) are well-established in the project's AGENTS.md and category_specs/AGENTS.md and can be cited from those sources.
3. **Consider implementation relocation**: The spec correctly identifies `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods` as the owner for `ordered_coarsening_closure()`. If the current implementation in `partitioned.py` places it on the general `PartitionsCategory.ElementMethods`, a follow-up task may be needed to introduce the `FiniteTotallyOrderedBase` axiom category and relocate the method.

**Overall verdict**: The spec is mathematically sound and properly grounded. All six gates pass. The stale references are documentation hygiene issues, not correctness blockers. No gate failure prevents this spec from being marked `reviewed`.
