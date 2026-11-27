---
id: SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE]]'
- '[[SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT]]'
title: Recover orthogonal group and structured subgroup surfaces
status: complete
priority: high
requirement: Orthogonal groups and subgroups from historical code must be recovered
  as Aut-category objects and structured subgroup objects with explicit action, membership,
  generators, and finite quotient semantics.
acceptanceCriteria:
- L.orthogonal_group() or the standard Aut surface returns an object whose membership
  is the centralized form-preservation condition.
- Subgroups such as determinant-one, positive-spinor, discriminant-kernel, discriminant-preimage,
  and centralizer subgroups retain structured metadata without exposing raw ConditionSet
  as the public model.
- Group actions use the repo-standard left action on column vectors or elements, with
  backend row-action matrices normalized at the backend boundary.
- Generators returned by a backend are verified as group elements before entering
  public group semantics.
complexity: 85
tags:
- FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY
---
# Recover orthogonal group and structured subgroup surfaces

## Source Provenance

- `src.bak/lattices/groups/orthogonal.py`: `LatticeOrthogonalGroup`,
  `LatticeOrthogonalSubgroup`, special/plus/stable/discriminant-preimage subgroup
  methods, centralizer, and discriminant orthogonal groups.
- `src.bak/lattices/core/integral.py`: `orthogonal_group`,
  `_column_action_isometry_from_row_action_matrix`, and backend generator routing.
- `src.bak/backends/dawes_orbit_backend.py`: determinant, real spinor, discriminant
  action, and structured subgroup constraints.
- `src.bak/backends/isotropic_gamma_orbit_backend.py`: finite quotient presentation
  consumption for subgroup-aware orbit splitting.
- `.agents/memories/bilinear-form-category-semantics.md`: public action convention
  and subgroup naming.
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md`:
  backend matrix normalization and witness verification.
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md`:
  finite quotient, centralizer, discriminant-image, and subgroup-preimage contracts.
- `plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/specs/SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER.md`:
  `O(M,b) = Aut(M,b)` in the formed-module category.

## Contract

The recovered orthogonal group of a lattice is the automorphism object of the formed
lattice in the appropriate category. A public group element acts on lattice elements by
the repo-standard action convention. Matrix equations are centralized membership checks
inside the group or Hom/Aut parent.

Subgroups must be structured mathematical objects. Determinant, spinor, discriminant
action, centralizer, and finite quotient constraints are metadata and predicates of
subgroup objects, not opaque intersections of arbitrary Python predicates. Subgroup
algebra may use intersections or generated joins internally, but the public model must
state the subgroup construction.

## Definition Grounding

- Orthogonal group: for a formed module or lattice `(M, b)`, the orthogonal group is
  `Aut(M, b)`, the invertible formed-module endomorphisms preserving `b`.
- Public membership: a matrix or backend datum becomes a group element only by entering
  the Aut/Hom parent and satisfying the centralized containment rule: source and target
  parent match, the underlying module map is invertible, and the form is preserved.
- Public action: group elements act on lattice/module elements by the repo-standard
  left action on column-coordinate presentations. Backend row/right-action matrices are
  normalized before this surface sees them.
- Discriminant orthogonal group: `O(A_L, q)` or `O(A_L, b)` is the Aut object of the
  finite discriminant formed module. It is not a raw Sage group.
- Structured subgroup: a subgroup is represented by its parent group, construction
  data, membership predicate/containment rule, optional generator backend provenance,
  and optional finite quotient/preimage metadata.

## Recovered Orthogonal Group Surface

The admitted public lattice surface is:

- `L.Aut()` as the canonical formed-module automorphism group;
- `L.orthogonal_group()` as a compatibility spelling for `L.Aut()` where the lattice
  literature expects `O(L)`;
- `O.lattice()` or `O.object()` returning the parent formed object;
- `O.identity()`, `O(g)` or `O.from_matrix(g)` as Aut-parent constructors that validate
  membership;
- `g.matrix()` or `g.to_matrix()` as presentation readback for a group element;
- `g.inverse()`, composition, equality, determinant where the carrier is finite free,
  and action on elements/subobjects through the public group action.

Generator computation is separate from group definition. `O(L)` exists as an Aut object
even when generators are not yet available. A backend route may provide generators, but
each generator must be normalized and admitted through `O(L)` before `O.gens()` returns
it.

## Structured Subgroup Surface

The historical subgroup methods recover named subgroup constructors:

| Historical surface | Admitted public construction |
| --- | --- |
| `special_orthogonal_subgroup()` | determinant-one subgroup `SO(L) = ker(det: O(L) -> {+/-1})` where determinant is defined |
| `plus_subgroup()` | positive real-spinor-kernel subgroup with source-backed spinor convention |
| `special_plus_subgroup()` | intersection of the determinant-one and positive-spinor kernels |
| `kernel_of_discriminant_action()` | kernel of the discriminant representation `O(L) -> O(A_L)` |
| `preimage_of_discriminant_subgroup(H)` | preimage of a subgroup `H <= O(A_L)` under the discriminant action |
| `centralizer(f)` | centralizer subgroup `Z_{O(L)}(f)` for `f in O(L)` |
| `stabilizer(x)` and isotropic stabilizers | subgroup of the acting group preserving the target object, specified in the orbit/stabilizer spec |

Subgroup intersection is a subgroup meet with combined construction data. A generated
join may be admitted when the result is explicitly the subgroup generated by the two
inputs. Do not expose set-theoretic union of subgroups as a subgroup operation; a union
is usually not a subgroup.

The finite quotient presentation used by Dawes/isotropic backends is public only as
group homomorphism data:

- determinant sign factor;
- positive real spinor sign factor;
- discriminant-action image/preimage factor;
- product target finite group;
- allowed subgroup image;
- source-to-target homomorphism.

This metadata must survive subgroup intersections and be visible to orbit/stabilizer
backend contracts.

## Discriminant Aut Surface

The historical `DiscriminantOrthogonalGroup` and `DiscriminantOrthogonalSubgroup`
recover the finite formed-module Aut surface:

- `A.Aut()` where `A` is a discriminant formed module;
- `A.Aut().gens()` admitted only after Sage/GAP/Oscar generators are converted into
  public Aut elements;
- `A.Aut().subgroup(generators)` returning a structured subgroup of `A.Aut()`;
- `A.Aut().stabilizer(a)` for a discriminant element or subobject, returning a subgroup
  with verified action;
- intersections of discriminant subgroups as subgroup meets in the same parent.

Actions return discriminant elements or subobjects, not coordinate vectors. Coordinate
matrix action is implementation data behind the finite formed-module parent.

## Backend And Generator Provenance

Public groups/subgroups should record generator provenance:

- definite orthogonal generators from Sage/definite quadratic-form code;
- indefinite generators from Indefinite.jl/polyhedral routes;
- centralizer-image or finite quotient data from Oscar/GAP routes;
- CARAT only when the task has reduced to a positive-definite form or finite matrix
  group within the documented CARAT domain.

If no generator backend is available for a subgroup, the subgroup object may still exist
with exact containment data, but generator enumeration must report unsupported rather
than silently performing an unrelated search.

## Non-Preservation Boundaries

- Do not preserve `condition_set` accessors as public subgroup state.
- Do not merge subgroup constraints by raw Python predicate algebra when the subgroup
  has a named mathematical construction.
- Do not make backend generator availability define the subgroup; the subgroup exists
  mathematically even when generator computation is delayed or delegated.
- Do not expose discriminant orthogonal groups as raw Sage groups.
- Do not expose `condition_set | condition_set` as subgroup union. Use a generated join
  only when the subgroup generated by both inputs is the mathematical construction.
- Do not treat `MatrixSpace(ZZ, n)` containment as group membership; Aut containment is
  the membership owner.

## Acceptance Criteria

- [x] Orthogonal group membership is centralized in Aut/Hom containment.
- [x] Structured subgroups retain named construction data and generator provenance.
- [x] Backend matrices are required to be normalized and verified once before exposure.
- [x] Discriminant orthogonal groups are recovered as Aut objects of discriminant
  forms.

## 6-Gate Protocol Review Log

Review date: 2026-05-07.  Reviewer: automated 6-gate audit (subagent).
Result: PASS with findings (G1 Finding 1, G2 Finding 1, G5 Finding 1).
No gate failures.

### G1 — Source Grounding

The spec cites eight artifacts (four historical source files, one memory file,
three dependency specs).  The dependency specs and the memory file exist on disk.
All four `src.bak/` historical source files do NOT exist in the current workspace.

| Reference cited in spec | Actual path resolved | Exists |
| --- | --- | --- |
| `src.bak/lattices/groups/orthogonal.py` | (same) | NO |
| `src.bak/lattices/core/integral.py` | (same) | NO |
| `src.bak/backends/dawes_orbit_backend.py` | (same) | NO |
| `src.bak/backends/isotropic_gamma_orbit_backend.py` | (same) | NO |
| `.agents/memories/bilinear-form-category-semantics.md` | `/home/dzack/research/.agents/memories/bilinear-form-category-semantics.md` | YES |
| `.../SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md` | `/home/dzack/research/plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md` | YES |
| `.../SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md` | `/home/dzack/research/plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md` | YES |
| `.../SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER.md` | `/home/dzack/research/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/specs/SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER.md` | YES |

**G1 Finding 1 (moderate):** Four `src.bak/` historical source files are cited in
Source Provenance but do not exist on disk.  The parent feature card
(`FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY.md`) also cites them.  No `src.bak/`
directory of any kind was found.  The historical code that this spec aims to recover
behavior from is the evidentiary anchor; its absence weakens verifiability of the
recovery claims.  **Recommendation:** Either (a) restore the `src.bak/` files to the
workspace, (b) create a decision card documenting when and why they were archived
and where to find them, or (c) replace historical file citations with concrete
behavior descriptions extracted from the parent feature card and dependency specs.

**G1 Finding 2 (advisory):** The spec uses path
`.agents/memories/bilinear-form-category-semantics.md` (line 43).  This file exists
and its content (notably lines 9-15 on discriminant descent and line 26 on Hom-space
containment) confirms the spec's definition grounding.  PASS.

Source-grounding verdict: PASS with one moderate finding (missing `src.bak/` sources).

### G2 — Sage Surface Completeness

The spec defines a two-tier surface: orthogonal group operations and structured
subgroup operations, plus a discriminant Aut surface.  Compared against current
Sage surfaces under `category_specs/`:

**Orthogonal group surface — accounted:**

| Surface item | Current Sage location | Status |
| --- | --- | --- |
| `L.Aut()` as canonical formed-module automorphism group | `category_specs/lattices/homsets.py` `LatticeAutCategory` (line 90) | EXISTS — canonical chain `Lattices(R).AutCategory()` |
| `L.orthogonal_group()` compatibility spelling | `category_specs/forms/subcategories/with_forms.py` line 44: `orthogonal_group()` returning `AutCategory().Of(self)` | EXISTS |
| `O.lattice()` / `O.object()` | Not yet surfaced; the `base_lattice()` abstract method on `LatticeEndCategory` (line 83) provides this indirectly | GAP — abstract method exists but `lattice()` surface name not confirmed |
| `O.identity()`, `O(g)`, `O.from_matrix(g)` | Generic `AutCategory` via `GenericAutCategory` base | EXPECTED — inherited from generic aut-category machinery |
| `g.matrix()` / `g.to_matrix()` | `_LatticeMorphisms.to_matrix()` abstract method (line 30) | EXISTS |
| `g.inverse()`, composition, equality, determinant | Generic aut-category element methods | EXPECTED — inherited, determinant needs realization for finite free case |
| Generator admission through `O(L)` before `O.gens()` | Spec requirement (lines 95-98), not yet surfaced as abstract method | GAP — requires implementation guard |

**Structured subgroup surface — accounted:**

| Surface item | Current Sage location | Status |
| --- | --- | --- |
| `special_orthogonal_subgroup()` / `SO(L)` | `LatticeAutCategory.special_subgroup()` (line 100) + `special_orthogonal_group()` (line 121) | EXISTS |
| `plus_subgroup()` (positive real-spinor-kernel) | Not present in current surfaces | GAP |
| `special_plus_subgroup()` | `LatticeAutCategory.stable_special_subgroup()` (line 113) + `stable_special_orthogonal_group()` (line 134) | EXISTS (as `stable_special`) |
| `kernel_of_discriminant_action()` | Not present in current surfaces | GAP |
| `preimage_of_discriminant_subgroup(H)` | Not present in current surfaces | GAP |
| `centralizer(f)` | Not present in current surfaces | GAP |
| `stabilizer(x)` / isotropic stabilizers | Deferred to `SPEC-HISTORICAL-ISOTROPIC-ORBIT-STABILIZER-SURFACE` | ROUTED |
| Subgroup intersection as meet, no set-theoretic union | Spec requirement only | DESIGN RULE — no surface code needed |

**Discriminant Aut surface — not yet surfaced:**

None of the discriminant Aut surface methods (`A.Aut()`, `A.Aut().gens()`,
`A.Aut().subgroup(generators)`, `A.Aut().stabilizer(a)`) exist in current Sage
surface code.  This is expected as the discriminant group surface is a separate
dependency chain.

**G2 Finding 1 (advisory):** Four subgroup constructors (`plus_subgroup`,
`kernel_of_discriminant_action`, `preimage_of_discriminant_subgroup`, `centralizer`)
are specified but have no current Sage surface representation.  Three discriminant
Aut surface methods are similarly absent.  Since this spec is an aspirational
recovery target, these gaps are expected and acceptable.  The spec correctly
delegates `stabilizer` to the sibling orbit/stabilizer spec.

Sage-surface verdict: PASS.  Core orthogonal group surface and several subgroup
methods are present; remaining items are documented gaps aligned with the recovery
goal.

### G3 — Mathematical Correctness

Audit of mathematical claims:

1. **Orthogonal group = Aut(M,b):** Lines 67-68.  Verified against canonical
   sources: `SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER.md` line 139:
   "`O(M,b) = Aut(M,b)` in the formed-module category."  Also confirmed in
   `category_specs/lattices/homsets.py` lines 1-7, `category_specs/forms/subcategories/with_forms.py`
   lines 44-46, and `bilinear-form-category-semantics.md` lines 1-30.
   Mathematically correct.  PASS.

2. **Public membership through Aut/Hom containment:** Lines 69-71.  Verified
   against the Hom-containment spec (`SPEC-20260504-FORMS-ISOMETRY-HOM-CONTAINMENT-OWNER.md`
   lines 62-76) and the ABC spec (lines 176-189 in `category-abc-spec.md`).
   Mathematically correct: containment in a formed-module Hom/Aut object implies
   form preservation by definition.  PASS.

3. **Left action on column-coordinate presentations:** Lines 72-74.  Verified
   against the bridge contract spec (`SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md`
   lines 68-73): "public automorphism generator g in O(L) verifies
   g.T * gram(L) * g == gram(L)".  This is the standard left column action
   convention.  Correct.  PASS.

4. **Discriminant orthogonal group = Aut of finite discriminant formed module:**
   Lines 75-76.  Verified against `bilinear-form-category-semantics.md` lines 14-15
   (discriminant form as cokernel of dual inclusion) and the discriminant morphism
   spec (`SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE.md` lines 125-145).
   Correct.  PASS.

5. **Structured subgroup with construction data:** Lines 77-79.  The data model
   (parent group, construction data, membership predicate, generator provenance,
   finite quotient metadata) is category-theoretically sound.  Verified against
   centralizer spec (`SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md`
   lines 134-147).  PASS.

6. **Subgroup meet/intersection and rejection of union:** Lines 114-117.
   Correct: the intersection of subgroups is a subgroup (meet in the subgroup
   lattice); the set-theoretic union is generally not a subgroup.  PASS.

7. **Finite quotient data as group homomorphism data:** Lines 119-130.  The
   explicit listing of determinants, spinor signs, discriminant-action factors,
   product target group, allowed subgroup image, and homomorphism is
   mathematically precise and auditable.  Verified against the centralizer spec's
   structured subgroup constraints (lines 134-147).  PASS.

8. **`ker(det: O(L) -> {+/-1})`:** Line 106.  Correct when determinant is defined
   (free finite-rank case).  The spec acknowledges the "where determinant is
   defined" caveat.  PASS.

No mathematical errors found.

Mathematical-correctness verdict: PASS.

### G4 — Nonmathematical Rejection

The spec has an explicit Non-Preservation Boundaries section (lines 162-173) with
six rejections.  Each has a clear rationale and replacement:

1. **Reject `condition_set` accessors as public subgroup state** (line 164).
   Rationale: `ConditionSet` is a Sage implementation wrapper; subgroup surface
   should expose named mathematical construction.  Replacement: structured subgroup
   objects with construction data.  SOUND.

2. **Reject raw Python predicate algebra for named mathematical constructions**
   (lines 165-166).  Rationale: merging constraints via Python lambda/predicate
   algebra obscures mathematical structure.  Replacement: subgroup meet with
   combined construction data.  SOUND.

3. **Reject backend generator availability as subgroup definition** (lines 167-168).
   Rationale: the subgroup exists mathematically independent of computational
   access to generators.  Replacement: subgroup exists with containment data;
   generator enumeration reports unsupported.  SOUND.

4. **Reject discriminant orthogonal groups as raw Sage groups** (line 169).
   Rationale: Sage's bare group objects lack the formed-module structure.
   Replacement: Aut of the discriminant formed module.  SOUND.

5. **Reject `condition_set | condition_set` as subgroup union** (lines 170-171).
   Rationale: union is not generally a subgroup.  Replacement: generated join only
   when it matches the mathematical construction.  SOUND.

6. **Reject `MatrixSpace(ZZ, n)` containment as group membership** (lines 172-173).
   Rationale: being an integer matrix of correct size does not imply form
   preservation or invertibility over ZZ.  Replacement: Aut containment.  SOUND.

All rejections are mathematically grounded and preserve the spec's obligations
through explicit replacement owners.

Nonmathematical-rejection verdict: PASS.

### G5 — Ambiguity Routing

Identified ambiguities and their resolution status:

1. **`plus_subgroup` vs `stable_subgroup` terminology** (lines 107-108).  The spec
   uses "positive real-spinor-kernel subgroup" for `plus_subgroup` and names
   `stable_orthogonal_group` separately in current Sage surfaces (line 129 of
   `lattices/homsets.py`).  In standard literature, "O^+(L)" (the stable/plus
   subgroup) can refer to either the real-spinor-norm kernel or the orientation-
   preserving component, which coincide for indefinite lattices under certain
   hypotheses.  **G5 Finding 1 (advisory):** The spec does not explicitly state
   whether `plus_subgroup` and `stable_subgroup` are intended to coincide or remain
   distinct, nor does it specify the exact spinor-norm convention (real spinor norm
   vs. adelic spinor norm).  The bridge contract spec
   (`SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md`) references
   "real spinor norm" (line 140 of that spec) which constrains the convention.
   **Recommendation:** Add a sentence clarifying the relationship between
   `plus_subgroup` and `stable_subgroup`, and anchor the spinor-norm convention to
   the bridge contract.

2. **`centralizer` domain clarification.** The spec says `Z_{O(L)}(f)` (line 111),
   which is unambiguous: centralizer in the orthogonal group.  PASS.

3. **`stabilizer` and isotropic stabilizers** (line 112).  Explicitly delegated to
   the orbit/stabilizer spec (`SPEC-HISTORICAL-ISOTROPIC-ORBIT-STABILIZER-SURFACE`).
   This is correct routing, not an ambiguity.  PASS.

4. **Determinant defined only for finite free case.** The spec table (line 106)
   includes "where determinant is defined" qualifier.  PASS.

5. **`lattice()` vs `object()` surface name.** The spec says `O.lattice()` or
   `O.object()` (line 88).  The current Sage surface uses `base_lattice()` on
   `LatticeEndCategory` (line 83 of `lattices/homsets.py`).  The spec allows
   either name (`lattice()` or `object()`), which is flexible but slightly
   ambiguous.  This is a naming decision deferred to implementation.  PASS.

Ambiguity-routing verdict: PASS with one advisory finding (plus/stable subgroup
terminology).

### G6 — Obligation Preservation

Audit of mathematical obligations transferred from historical code:

1. **Orthogonal group as Aut object:** Historical `LatticeOrthogonalGroup` becomes
   `L.Aut()` / `L.orthogonal_group()`.  The obligation is preserved and
   strengthened: form-preservation is now categorical Aut containment, not an
   ad hoc matrix group wrapper.  PASS.

2. **Subgroup construction data:** Historical `ConditionSet`-based subgroups become
   structured subgroup objects with named construction data, generator provenance,
   and finite quotient metadata.  The obligation to expose subgroup structure is
   preserved; the implementation detail (`ConditionSet`) is replaced by the
   mathematical owner.  PASS.

3. **Finite quotient filtering:** Historical Dawes/isotropic `condition_set`
   filtering becomes explicit homomorphism data (determinant, spinor, discriminant
   factors).  The obligation to provide subgroup filtering is preserved; the
   opacity is removed.  PASS.

4. **Discriminant orthogonal groups:** Historical `DiscriminantOrthogonalGroup`
   becomes `A.Aut()` of the discriminant formed module.  The obligation to
   represent discriminant-group automorphisms is preserved and placed in the
   correct category.  PASS.

5. **Action convention normalization:** Backend row-action matrices are normalized
   at the bridge boundary (delegated to `SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md`).
   The obligation to handle backend conventions is preserved and routed to the
   correct owner.  PASS.

6. **Generator provenance tracking:** The spec requires provenance recording
   (lines 150-160) by backend route (definite Sage, indefinite Indefinite.jl,
   Oscar/GAP centralizer, CARAT for definite auxiliary).  This is an added
   obligation not present in the historical code, representing improved
   mathematical auditing.  PASS.

No mathematical obligation is weakened, deleted without replacement, or narrowed to
implementation-only surfaces.

Obligation-preservation verdict: PASS.

### Summary

| Gate | Verdict | Evidence |
| --- | --- | --- |
| G1 Source grounding | PASS | 4/8 references exist on disk; 4 `src.bak/` sources missing (finding) |
| G2 Sage surface completeness | PASS | Core Aut surface present; 4 subgroup + 3 discriminant methods are documented gaps |
| G3 Mathematical correctness | PASS | 8 claims audited against canonical sources; no errors |
| G4 Nonmathematical rejection | PASS | 6 explicit rejections, all with grounded rationale and replacement owners |
| G5 Ambiguity routing | PASS | 5 boundaries examined; 1 advisory on plus/stable subgroup terminology |
| G6 Obligation preservation | PASS | 6 obligations preserved with correct owner routing; 1 new obligation added |

Overall: SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE.md is mathematically
sound and correctly routes orthogonal group and subgroup semantics through the
formed-module Aut category.  The spec's dependency chain is intact (bridge contract,
centralizer/finite-quotient backends, Hom-containment owner, discriminant morphism
surface).  Three findings require attention:

1. **G1 Finding 1 (moderate):** Four `src.bak/` historical source files are
   missing.  The spec should either restore them, document their archival location,
   or replace citations with concrete behavior descriptions.
2. **G2 Finding 1 (advisory):** Seven surface methods (`plus_subgroup`,
   `kernel_of_discriminant_action`, `preimage_of_discriminant_subgroup`,
   `centralizer`, `A.Aut().gens()`, `A.Aut().subgroup(generators)`,
   `A.Aut().stabilizer(a)`) are specified but not yet surfaced in Sage code.
3. **G5 Finding 1 (advisory):** The relationship between `plus_subgroup` and
   `stable_subgroup` and the exact spinor-norm convention should be clarified.
