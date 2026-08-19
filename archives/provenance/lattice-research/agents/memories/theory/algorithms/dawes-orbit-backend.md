# Plan: `INDEF_FORM_TestEquivalenceVector` and `dawes_orbit_backend`

## Overview

This plan adds a subgroup-aware non-isotropic vector orbit backend to the existing
lattice API without introducing a second public group hierarchy.

The current repo already has:

- full-form indefinite isometry via `INDEF_FORM_TestEquivalence`,
- full `O(L)` generators via `INDEF_FORM_AutomorphismGroup`,
- vector stabilizers via `INDEF_FORM_StabilizerVector`,
- isotropic orbit/stabilizer tools,
- finite discriminant-group orthogonal groups via Sage/GAP,
- a condition-set model for arbitrary subgroups of `O(L)`,
- OSCAR helpers for discriminant images of centralizers.

The missing pieces are:

- the installed binary and wrapper for `INDEF_FORM_TestEquivalenceVector`,
- a private backend that composes Dawes Algorithms 2.1-2.3 with the existing
  `LatticeOrthogonalGroup` / `LatticeOrthogonalSubgroup` objects,
- first-class subgroup constructors matching Dawes's arithmetic subgroup notation,
- one minimal public interface for vector-orbit equivalence under a chosen subgroup.

The implementation should stay concentrated in
`src/research/dawes_orbit_backend.py`, with only thin public hooks added to the
existing lattice/group nouns.

## Goal and Defect Statement

### Current defect

The repo can test lattice equivalence and compute full orthogonal groups and
stabilizers, but it cannot yet ask the natural subgroup-sensitive question:

> do `v1` and `v2` lie in the same orbit under a chosen subgroup `Gamma ⊂ O(L)`?

It also does not expose Dawes-style subgroup constructors such as `SO(L)`,
`O^+(L)`, `SO^+(L)`, or `O_A(L)` in a way that composes with the current
condition-set model.

### Target state

At the end of this work:

- `src/external/bin` contains `INDEF_FORM_TestEquivalenceVector`,
- `src/external/py_polyhedral` wraps it,
- the repo has a private `dawes_orbit_backend` module that dispatches between:
  - the full `O(L)` Dutour-Sikirić binary,
  - Dawes Algorithm 2.1 for arbitrary subgroups when `v_1^\perp` is definite,
  - Dawes Algorithms 2.2/2.3 for structured arithmetic subgroups when
    `v_1^\perp` is indefinite,
- subgroup objects can express Dawes's standard arithmetic subgroups by
  composing membership conditions,
- the public API remains centered on the existing nouns:
  `Lattice`, `LatticeOrthogonalGroup`, `LatticeOrthogonalSubgroup`,
  `DiscriminantOrthogonalGroup`, `DiscriminantOrthogonalSubgroup`.

## Constraints

- Do not add a new public `Gamma` class. The canonical public subgroup nouns stay
  `LatticeOrthogonalGroup` and `LatticeOrthogonalSubgroup`.
- Do not reimplement computations that already exist in Dutour-Sikirić binaries,
  OSCAR, Sage, GAP, or existing repo helpers.
- Keep subgroup membership OSOT in the existing `ConditionSet` model.
- Treat generator computation as optional and lazy. Membership is mandatory;
  generators are opportunistic.
- Keep the new public surface minimal. Most logic belongs in
  `src/research/dawes_orbit_backend.py`.
- Use Dawes's actual meaning of `O^+`: the kernel of the real spinor norm.
  Do not define `O^+` by positive-cone preservation in general. A positive-cone
  shortcut is only admissible as a documented special case after proof.
- For indefinite-complement problems with an opaque custom predicate and no extra
  arithmetic structure, do not pretend the backend can solve more than Dawes
  actually allows.

## Canonical Sources

### Literature and repo docs

- Dawes, *Orbits in lattices*, §2.1, Algorithms 2.1-2.3, Theorem 2.3,
  Lemmas 2.4-2.5.
- [Dawes non-isotropic vector orbits](dawes-nonisotropic-vector-orbits)
- [Indefinite isometry backend](../backends/indefinite-isometry)
- `src/external/README.md`
- [polyhedral_common indefinite methods](../external/dutsik_polyhedral/polyhedral_common/notes/indefinite_methods)
- [Oscar lattices](../backends/oscar-lattices)

### Online backend docs

- `MathieuDutSik/polyhedral_common`
  - `src_indefinite/INDEF_FORM_TestEquivalenceVector.cpp`
  - `CMakeLists.txt`
- `MathieuDutSik/Indefinite.jl`
- OSCAR docs, `NumberTheory/QuadFormAndIsom/latwithisom`
  - `image_centralizer_in_Oq`
  - `discriminant_representation`
  - `rational_spinor_norm`

## Backend Delegation Map

| Computation | Primary backend | Why |
| --- | --- | --- |
| Full `O(L)` pairwise vector equivalence | `INDEF_FORM_TestEquivalenceVector` | Exact existing witness search for the ambient orthogonal group |
| Full `O(L)` automorphism group | `INDEF_FORM_AutomorphismGroup` | Already wired and exact |
| Full `O(L)` vector stabilizer | `INDEF_FORM_StabilizerVector` | Already wired and exact |
| Full `O(L)` orbit reps at fixed norm | `INDEF_FORM_GetOrbitRepresentative` | Already installed; useful as a helper, not the subgroup solver |
| Definite complement isometry in Dawes 2.1 | Sage definite quadratic-form isometry | Already integrated, exact, and sufficient for phase 1 |
| Finite `O(D(L))` and subgroup membership | existing `DiscriminantGroup.orthogonal_group()` and GAP | Already present and finite |
| Image of a finitely generated subgroup on `D(L)` | OSCAR `discriminant_representation` | Reuse instead of reimplementing action bookkeeping |
| Image of `O(L,f)` in `O(D_L,D_f)` | OSCAR `image_centralizer_in_Oq` | Existing repo tool already targets this |
| Real spinor norm of a candidate isometry | OSCAR `rational_spinor_norm` | Canonical documented route |
| Stable subgroup `\widetilde O(L)` | existing `kernel_of_discriminant_action()` | Already present |

### Design rule

Use the full `O(L)` binary whenever it is decisive. Use Dawes only when subgroup
restrictions make the ambient binary insufficient.

That means:

- if `INDEF_FORM_TestEquivalenceVector` returns `None`, then no subgroup of `O(L)`
  can relate the vectors;
- if it returns a witness already in `Gamma`, accept immediately;
- if it returns a witness outside `Gamma`, then the ambient `O(L)` route has not
  solved the subgroup problem, so the code must proceed to a mathematically valid
  Dawes branch.

## Public API Shape

### Public nouns

No new public nouns.

The public API continues to revolve around:

- `Lattice`
- `LatticeOrthogonalGroup`
- `LatticeOrthogonalSubgroup`
- `DiscriminantOrthogonalGroup`
- `DiscriminantOrthogonalSubgroup`

### Public verbs to add

Add these methods on both `LatticeOrthogonalGroup` and
`LatticeOrthogonalSubgroup`:

- `special_orthogonal_subgroup()`
  - membership predicate: `det(M) = 1`
  - intended meaning: `SO(L)` or `Gamma ∩ SO(L)`
- `plus_subgroup()`
  - membership predicate: `sn_R(M) = 1`
  - intended meaning: `O^+(L)` or `Gamma^+`
- `special_plus_subgroup()`
  - composition of the two previous filters
- `preimage_of_discriminant_subgroup(A)`
  - membership predicate: `bar(M) ∈ A`
  - intended meaning:
    - on `O(L)`: `O_A(L)`
    - on a subgroup `Gamma`: `Gamma_A`
- `find_vector_isometry(v1, v2)`
  - returns a witness matrix in the subgroup, or `None`
- `vectors_are_equivalent(v1, v2)`
  - boolean wrapper around `find_vector_isometry`

### Why these verbs

They give the smallest surface that still matches Dawes's notation and composes
with the existing condition-set model:

- `L.orthogonal_group().special_orthogonal_subgroup()` gives `SO(L)`,
- `L.orthogonal_group().plus_subgroup()` gives `O^+(L)`,
- `L.orthogonal_group().preimage_of_discriminant_subgroup(A)` gives `O_A(L)`,
- intersections remain ordinary subgroup intersections,
- arbitrary `Gamma` is still any condition-set-defined subgroup.

No new convenience methods on `Lattice` are required in phase 1. Users already
start from `L.orthogonal_group()`.

## Wiring into Existing Code

The implementation should touch exactly four layers.

- `src/external/bin`
  - installed binary artifact only
- `src/external/py_polyhedral/binaries.py`
  and `src/external/py_polyhedral/__init__.py`
  - raw subprocess wrapper layer only
- `src/research/dawes_orbit_backend.py`
  - all backend dispatch, subgroup-spec compilation, and Dawes logic
- `src/coble_geometry_foundation.py`
  - thin public methods on the existing orthogonal-group nouns

It should not introduce a second semantic integration path through
`src/research/isometry_backend.py`.
That module stays responsible for whole-lattice isometry. Vector-orbit
equivalence belongs on the orthogonal-group objects in
`src/coble_geometry_foundation.py`.

## Private API Shape

All new orchestration logic lives in
`src/research/dawes_orbit_backend.py`.

### Private nouns

- `_OrbitProblem`
  - lattice, subgroup, input vectors, normalized integral data
- `_SubgroupOrbitSpec`
  - structured metadata extracted from a subgroup:
    - ambient lattice
    - determinant restriction
    - real-spinor restriction
    - discriminant-subgroup restriction
    - whether the subgroup is only a black-box predicate
- `_DawesOrbitBackend`
  - dispatcher and backend coordinator

### Private verbs

- `_normalize_nonisotropic_pair`
- `_test_full_orthogonal_equivalence`
- `_induced_discriminant_action`
- `_compile_subgroup_spec`
- `_check_real_spinor_norm`
- `_solve_algorithm_21`
- `_solve_algorithm_22`
- `_solve_algorithm_23`
- `_search_definite_complement_isometries`
- `_assemble_witness_from_complement_data`

These stay private because they are backend orchestration, not mathematical nouns
the rest of the repo should import directly.

## Required Metadata on Subgroup Objects

The current `ConditionSet` model is enough for membership, but not enough for
backend dispatch. A Dawes solver needs to know whether a subgroup is:

- plain `SO`,
- plain `O^+`,
- a discriminant preimage `Gamma_A`,
- an intersection of those structured conditions,
- or an opaque custom predicate.

Plan:

- attach a private `_dawes_spec` or equivalent metadata object to every
  `LatticeOrthogonalGroup` / `LatticeOrthogonalSubgroup`,
- merge that metadata through structured constructors and intersections whenever
  possible,
- mark user-supplied opaque predicates as `black_box`.

This preserves the current public subgroup type while letting the backend detect
when Algorithms 2.2/2.3 are available.

## Subgroup Construction Plan

### `SO(L)` and `Gamma ∩ SO(L)`

- Implement as condition-set filters using `det(M) = 1`.
- No special backend is needed for membership.
- Generator computation is optional. Do not promise a generator routine in phase 1.

### `O^+(L)` and `Gamma^+`

- Implement as condition-set filters using the real spinor norm.
- Primary backend: OSCAR `rational_spinor_norm` on the corresponding lattice with
  isometry.
- For Lorentzian shortcuts already justified in repo literature, allow an
  optimized helper later, but keep the canonical definition spinorial.

### `O_A(L)` and `Gamma_A`

- Implement as condition-set filters using the induced action
  `bar(M) ∈ A`, where `A` is a `DiscriminantOrthogonalSubgroup`.
- Reuse the existing discriminant-group nouns. Do not add a parallel
  discriminant-subgroup representation.
- For explicit image computations of finitely generated groups, defer to OSCAR
  `discriminant_representation` when that is genuinely useful; do not make it a
  hard dependency of the basic membership test.

### `\widetilde O(L)` and descendants

- Keep `kernel_of_discriminant_action()` as the canonical public verb.
- Do not add a duplicate `stable_orthogonal_subgroup()` method.
- Compose it with the new subgroup constructors:
  - `kernel_of_discriminant_action().plus_subgroup()`
  - `kernel_of_discriminant_action().special_orthogonal_subgroup()`

## Solver Dispatch Plan

### Fast ambient route

Use `INDEF_FORM_TestEquivalenceVector` first for the ambient orthogonal group.

This gives:

- an immediate rejection when no ambient equivalence exists,
- an immediate acceptance when the returned witness already satisfies the subgroup
  predicate,
- a cheap initial witness candidate for later subgroup checks.

### Dawes Algorithm 2.1 route

Use this when `v_1^\perp` is definite.

Properties:

- valid for arbitrary `Gamma ⊂ O(L)`,
- only requires subgroup membership, not subgroup generators or arithmetic image
  data,
- therefore it is the general black-box subgroup branch when `v_1^\perp` is
  definite.

Implementation plan:

- compute the normalized integral vectors `w_i`,
- build `K_i` and `\iota_i`,
- enumerate `Iso(K_1,K_2)` using the definite-lattice backend,
- assemble candidates `theta`,
- accept the first candidate that lies in `Gamma`.

### Dawes Algorithms 2.2/2.3 route

Use this only when:

- `v_1^\perp` is indefinite,
- the subgroup spec is structured enough to identify a Dawes arithmetic subgroup,
- the required surjectivity and discriminant-data prerequisites are available.

Properties:

- this is the structured indefinite-complement route,
- it should not run for opaque custom predicates,
- it is the right place to reuse discriminant-group data, gluing data, and
  spinor filters.

Implementation plan:

- use Algorithm 2.2 as the conceptual route,
- use Algorithm 2.3 as the machine-oriented data extraction route,
- keep the coordinate/SNF details private inside the backend.

### Precondition boundary

If `v_1^\perp` is indefinite and the subgroup is only a black-box predicate,
then no Dawes branch is available from the stated assumptions.

The code should assert the branch hypotheses before attempting Algorithms 2.2/2.3
and fail there if they are false. It should not weaken the problem to ambient
`O(L)`.

## File-Level Plan

### Phase 0: Install the missing binary

Files:

- `src/external/bin`

Work:

- build or copy `INDEF_FORM_TestEquivalenceVector` from the canonical
  `polyhedral_common` source,
- verify that the installed binary uses the same `gmp` and `PYTHON` conventions as
  the other indefinite wrappers.

Acceptance:

- `src/external/bin/INDEF_FORM_TestEquivalenceVector` exists and runs.

Validation:

- execute the binary on a known positive case and a known negative case.

### Phase 1: Wrap the raw binary

Files:

- `src/external/py_polyhedral/binaries.py`
- `src/external/py_polyhedral/__init__.py`

Work:

- add `indefinite_form_test_equivalence_vector(M, v1, v2)`,
- mirror the existing temp-file wrapper style,
- request `PYTHON` output so the wrapper receives either a matrix literal or
  `None`,
- preserve the current matrix/vector conventions explicitly in the docstring.

Acceptance:

- the wrapper returns a witness matrix or `None` with the same conventions as the
  raw binary.

Validation:

- wrapper-level integration test against the installed binary.

### Phase 2: Scaffold the private backend

Files:

- `src/research/dawes_orbit_backend.py`

Work:

- add normalization and invariant checks,
- add subgroup-spec compilation from existing group/subgroup objects,
- add ambient binary fast path,
- add complement-building helpers,
- add branch-precondition assertions.

Acceptance:

- the module can accept a lattice, subgroup object, and vector pair and then
  either return a witness matrix, return `None`, or fail on false branch
  assumptions, without touching the public API yet.

Validation:

- direct module-level tests using real lattices and vectors.

### Phase 3: Add structured subgroup constructors

Files:

- `src/coble_geometry_foundation.py`

Work:

- add `special_orthogonal_subgroup`,
- add `plus_subgroup`,
- add `special_plus_subgroup`,
- add `preimage_of_discriminant_subgroup`,
- attach structured private metadata for backend dispatch.

Acceptance:

- these methods return subgroup objects that preserve current membership semantics
  and compose via `&`.

Validation:

- exact membership checks on explicit matrices,
- metadata merge tests for structured intersections,
- proof that old subgroup methods still behave identically.

### Phase 4: Implement Dawes Algorithm 2.1

Files:

- `src/research/dawes_orbit_backend.py`

Work:

- implement the general definite-complement route,
- keep it subgroup-agnostic beyond membership,
- reuse Sage for definite complement isometries,
- do not expose the complement machinery as new public helpers.

Acceptance:

- arbitrary subgroup objects can solve the definite-complement case.

Validation:

- Dawes Example 2.2 and additional small definite-complement fixtures.

### Phase 5: Implement Dawes Algorithms 2.2/2.3

Files:

- `src/research/dawes_orbit_backend.py`
- possibly one small OSCAR-facing internal helper if direct reuse of existing
  scripts is not enough

Work:

- implement the structured indefinite-complement route,
- reuse existing discriminant-group objects and OSCAR helpers where they are the
  right tool,
- keep all Smith-normal-form and gluing-data extraction private,
- assert the Dawes hypotheses before entering this route.

Acceptance:

- structured arithmetic subgroups such as `O_A(L)`, `SO_A(L)`, `O_A^+(L)`,
  `SO_A^+(L)` work when the Dawes hypotheses are satisfied.

Validation:

- Dawes Example 2.6,
- subgroup-specific fixtures from the extracted sidecar.

### Phase 6: Wire in the public orbit interface

Files:

- `src/coble_geometry_foundation.py`

Work:

- add `find_vector_isometry(v1, v2)` and `vectors_are_equivalent(v1, v2)` to the
  orthogonal-group nouns,
- delegate immediately to `dawes_orbit_backend`,
- keep `Lattice` itself unchanged unless a later caller proves a real need for a
  convenience shim.

Acceptance:

- subgroup objects become the public entry point for vector-orbit equivalence.

Validation:

- end-to-end tests through the actual public methods, not the backend internals.

## Testing Strategy

### Wrapper tests

- ambient positive case for `INDEF_FORM_TestEquivalenceVector`
- ambient negative case
- regression on output parsing and matrix convention

### Subgroup constructor tests

- `SO(L)` membership on explicit determinant `±1` witnesses
- `O_A(L)` membership on explicit induced discriminant actions
- `O^+(L)` membership on matrices with known real spinor norm
- composition tests such as `SO(L) ∩ O_A(L)` and `\widetilde O(L) ∩ O^+(L)`

### Orbit solver tests

- ambient `O(L)` cases resolved directly by the binary
- Algorithm 2.1 cases with custom black-box subgroup predicates
- Algorithm 2.2/2.3 cases using Dawes Examples 2.2 and 2.6 as exact fixtures

### Public API tests

- `L.orthogonal_group().vectors_are_equivalent(v1, v2)`
- `L.orthogonal_group().special_orthogonal_subgroup().vectors_are_equivalent(...)`
- `L.orthogonal_group().preimage_of_discriminant_subgroup(A).vectors_are_equivalent(...)`

## Risks and Stop Rules

### Risk: build/install drift in the external binary toolchain

Mitigation:

- treat `src/external/README.md` plus upstream `polyhedral_common` as the install
  contract,
- verify the binary before touching the semantic API.

Stop rule:

- do not proceed past phase 0 until the binary actually runs.

### Risk: spinor-norm route is harder to operationalize than expected

Mitigation:

- use OSCAR's documented `rational_spinor_norm` as the canonical route,
- scope phase 3 membership to what can be verified exactly,
- treat Lorentzian positive-cone shortcuts as optional later optimizations only.

Stop rule:

- do not merge a `plus_subgroup()` API that guesses `O^+` from an unjustified
  surrogate.

### Risk: subgroup metadata is too weak after arbitrary intersections

Mitigation:

- mark such subgroups as `black_box`,
- let Algorithm 2.1 continue to work when the complement is definite,
- assert branch hypotheses before entering the indefinite-complement route.

Stop rule:

- do not silently treat a black-box subgroup as if it were `O_A(L)` or `SO_A^+(L)`.

### Risk: pressure to add helper-shaped public functions

Mitigation:

- keep orbit testing on the orthogonal-group nouns,
- keep Dawes orchestration private,
- keep discriminant finite-group logic on the existing discriminant nouns.

Stop rule:

- do not add free functions whose natural receiver is already a lattice or
  orthogonal-group object.

## Explicit Non-Goals

- No new public general-purpose `Gamma` object.
- No public exposure of Dawes's internal `K_i`, `\iota_i`, gluing groups, or
  Smith-normal-form machinery.
- No promise of subgroup generator computation for every structured subgroup in
  phase 1.
- No replacement of existing `kernel_of_discriminant_action()` or current
  isotropic-orbit APIs.
- No implementation of the plan in this document.
