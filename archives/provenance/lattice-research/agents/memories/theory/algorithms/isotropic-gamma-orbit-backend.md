# Plan: isotropic `\Gamma`-orbit backend for lines, planes, and flags

## Overview

This plan adds subgroup-aware isotropic orbit computation to the existing lattice
API by following the Dutour-Sikirić/Hulek method from arXiv:2302.01679 and the
vendored `polyhedral_common` backend, rather than extending the non-isotropic
Dawes backend.

The key idea is:

- compute ambient isotropic line/plane/flag orbits and ambient stabilizers in
  `O(L)` using existing Dutour-Sikirić binaries,
- compute the finite image of the target subgroup `\Gamma` in an explicit finite
  quotient of the ambient orthogonal group,
- split each ambient orbit into `\Gamma`-orbits by finite double-coset
  computation,
- lift quotient representatives back to ambient isometries and apply them to the
  ambient orbit representative.

This plan also removes manual error raising from the relevant code paths and
replaces it with asserted hypotheses and asserted execution preconditions.

## Goal and Defect Statement

### Current defect

The repo currently has:

- ambient isotropic line/plane/flag orbit representatives under full `O(L)`,
- ambient isotropic stabilizers under full `O(L)`,
- subgroup-aware non-isotropic vector equivalence,
- condition-set subgroup nouns,
- finite discriminant-group orthogonal groups,
- OSCAR helpers for centralizer image computations.

But it does not yet have:

- subgroup-aware isotropic orbit splitting,
- a backend for `\Gamma`-orbits of primitive isotropic lines, planes, or flags,
- a finite-quotient lifting layer that turns finite double-coset output into
  actual ambient isometries,
- Sterk/degree-2 Enriques fixtures in the test suite,
- assertion-only failure surfaces in the affected modules.

### Target state

At the end of this work:

- `LatticeOrthogonalGroup` and `LatticeOrthogonalSubgroup` can compute isotropic
  line, plane, and flag orbit representatives for structured subgroups `\Gamma`,
- the implementation is concentrated in a new private backend module,
- the backend uses ambient Dutour-Sikirić isotropic binaries plus finite
  quotient splitting,
- subgroup representation does not require explicit generators of the infinite
  arithmetic subgroup as a primary object,
- the degree-2 Enriques case reproduces the paper's Case 1 counts:
  `5` zero-cusps and `9` one-cusps,
- Sterk's five primitive isotropic representatives are fixtures in the test suite
  and are checked for pairwise non-equivalence modulo the implemented
  `\Gamma_{En,2}`,
- no relevant code path raises `NotImplementedError`, `ValueError`,
  `RuntimeError`, or `FileNotFoundError`; the code asserts hypotheses and fails
  there.

## Constraints

- Do not create a new public `Gamma` noun.
- Keep the public API on the existing nouns:
  `Lattice`, `LatticeOrthogonalGroup`, `LatticeOrthogonalSubgroup`,
  `DiscriminantGroup`, `DiscriminantOrthogonalGroup`,
  `DiscriminantOrthogonalSubgroup`.
- Do not add a second subgroup representation beside the current `ConditionSet`
  model.
- Do not require explicit generators of the infinite subgroup `\Gamma` unless a
  specific constructor can already supply them lazily.
- Do not reimplement algorithms already present in `polyhedral_common`, GAP,
  Sage, or OSCAR.
- Do not add `just` recipes or task-local command-surface pollution.
- Do not use manual `raise` statements in the affected mathematical code. Branch
  assumptions, backend availability, and execution preconditions must be
  asserted.
- Do not silently broaden the scope to arbitrary opaque subgroups without a
  computable finite quotient image. Such cases must assert their missing
  assumptions.

## Canonical Sources

### Literature

- Dutour-Sikirić, Hulek, *Moduli of polarized Enriques surfaces -- computational
  aspects*, arXiv:2302.01679
  - subgroup cusp splitting by double cosets:
    `Enriques_compu_rev.tex#L1172`
  - reduction to finite quotient:
    `Enriques_compu_rev.tex#L1202`
  - primitive isotropic vector algorithm:
    `Enriques_compu_rev.tex#L1637`
  - isotropic `k`-plane stabilizer/equivalence:
    `Enriques_compu_rev.tex#L1665`
  - isotropic `k`-plane orbit algorithm:
    `Enriques_compu_rev.tex#L1784`
  - degree-2 Enriques Case 1 counts:
    `Enriques_compu_rev.tex#L709`
    and
    `Enriques_compu_rev.tex#L1282`
- Sterk, *Compactifications of the period space of Enriques surfaces Part I*
- AEGS Definition 2.6 and Lemma 3.2:
  `theory/references/literature/aegs_2023.md#L164`,
  `theory/references/literature/aegs_2023.md#L274`

### Vendored backend docs and code

- [polyhedral_common binary targets](../external/dutsik_polyhedral/polyhedral_common/BINARIES)
- `src/external/dutsik_polyhedral/polyhedral_common/src_indefinite/INDEF_FORM_GetOrbit_IsotropicKplane.cpp`
- `src/external/dutsik_polyhedral/polyhedral_common/src_indefinite/INDEF_FORM_StabilizerIsotropicPlane.cpp`
- `src/external/dutsik_polyhedral/polyhedral_common/src_group/GRP_DoubleCoset.h`
- `src/external/dutsik_polyhedral/polyhedral_common/src_group/GRP_OrbitSplitting.cpp`
- `src/external/dutsik_polyhedral/polyhedral_common/src_group/GRP_LinearSpace_Stabilizer_DoubleCoset.cpp`

### Existing repo integration points

- `src/coble_geometry_foundation.py`
- `src/external/py_polyhedral/binaries.py`
- `src/research/dawes_orbit_backend.py`
- `computations/oscar_centralizer.py`
- `tests/test_sterk_cusps.py`

## Public API Target

Keep the public surface minimal and group-centered.

Add to both `LatticeOrthogonalGroup` and `LatticeOrthogonalSubgroup`:

- `isotropic_line_orbits()`
- `isotropic_plane_orbits()`
- `isotropic_flag_orbits(k)`
- `isotropic_lines_are_equivalent(v1, v2)`
- `isotropic_planes_are_equivalent(basis1, basis2)`

Semantics:

- on the full ambient orthogonal group, these methods may delegate directly to
  the installed Dutour-Sikirić binaries or to the subgroup backend with
  `\Gamma = O(L)`,
- on a structured subgroup, these methods use ambient orbits plus finite
  quotient splitting,
- on an opaque subgroup lacking the required finite quotient data, they assert
  the missing assumption.

Do not move the existing ambient lattice helpers yet. The lattice-level ambient
methods may remain and eventually delegate to `L.orthogonal_group()`.

## Private Backend Target

Add a new private module:

- `src/research/isotropic_gamma_orbit_backend.py`

The existing `dawes_orbit_backend` remains non-isotropic.

### Private nouns

- `_IsotropicOrbitProblem`
  - lattice
  - subgroup
  - orbit type: line / plane / flag
  - structured subgroup metadata
- `_FiniteQuotientSpec`
  - ambient group chosen for splitting
  - stable kernel contained in the subgroup
  - finite quotient group
  - image of the target subgroup in the quotient
  - paired quotient generators and ambient lifts
- `_AmbientOrbitData`
  - ambient representative
  - ambient stabilizer generators
  - image of the ambient stabilizer in the finite quotient
- `_QuotientWordLift`
  - word evaluator from quotient elements to ambient isometries

### Private verbs

- `_compile_isotropic_subgroup_spec`
- `_choose_ambient_group_for_isotropic_split`
- `_finite_quotient_spec`
- `_ambient_isotropic_line_orbits`
- `_ambient_isotropic_plane_orbits`
- `_ambient_isotropic_flag_orbits`
- `_ambient_stabilizer_of_isotropic_object`
- `_stabilizer_image_in_finite_quotient`
- `_double_coset_representatives`
- `_lift_quotient_element_to_ambient`
- `_split_ambient_orbit_into_gamma_orbits`
- `_isotropic_objects_are_equivalent`

## Mathematical Dispatch

### Regime 1: ambient full-group orbit computation

Use existing Dutour-Sikirić binaries for:

- ambient isotropic line orbits,
- ambient isotropic plane orbits,
- ambient isotropic flag orbits,
- ambient stabilizers of isotropic lines, planes, or flags.

These are already exposed or directly available in `polyhedral_common`.

### Regime 2: subgroup splitting by finite quotient

Use the Dutour-Sikirić/Hulek method:

- let `G_0` be the chosen ambient arithmetic group for the moduli problem,
- let `x` be an ambient orbit representative,
- let `G_x` be the ambient stabilizer of `x`,
- let `\Gamma \subset G_0` be the target subgroup,
- compute double cosets `G_x \backslash G_0 / \Gamma` in a finite quotient,
- choose representatives `h_i`,
- the `\Gamma`-orbit representatives are `x h_i`.

### Regime 3: equivalence testing

Two isotropic objects are `\Gamma`-equivalent if and only if they lie in the
same split orbit class under the same double-coset computation.

For pairwise equivalence, do not enumerate all ambient objects if one stabilizer
double-coset computation suffices.

## Structured subgroup assumptions

This backend applies to structured subgroups for which the following data are
computable:

- a chosen ambient arithmetic group `G_0`,
- a finite quotient of `G_0`,
- the image of `\Gamma` in that finite quotient,
- and a lift map from quotient generators back to ambient generators.

Initial supported structured families:

- `O(L)`
- `SO(L)`
- `O^+(L)`
- `SO^+(L)`
- preimages of finite discriminant subgroups
- intersections of the above
- Enriques-style groups obtained as preimages of finite image subgroups
  coming from the centralizer/stabilizer construction

Initial excluded family:

- arbitrary opaque `ConditionSet` subgroups with no explicit finite quotient
  image

For excluded inputs, assert the missing structured quotient data.

## Quotient design

The decisive abstraction is not the infinite subgroup `\Gamma`, but its finite
image.

### Required quotient operations

- finite quotient group construction,
- subgroup construction inside the quotient,
- ambient stabilizer image inside the quotient,
- double-coset decomposition in the quotient,
- membership and equality in the quotient,
- word expressions in quotient generators,
- replay of quotient words on ambient generator lifts.

### Preferred implementation

Use Sage/GAP finite-group functionality for the double-coset computations and
word handling.

Reason:

- the quotient groups are finite,
- the repo already uses Sage/GAP for discriminant-group orthogonal groups,
- this avoids adding wrappers for more `src_group` binaries unless needed,
- it keeps the Python surface small and mathematically transparent.

### Optional backend expansion

If GAP word extraction or double-coset handling proves insufficient for a needed
case, add thin wrappers for the relevant `src_group` binaries from
`polyhedral_common`, but only after the GAP route is shown to be the blocker.

## Generator policy

Do not compute infinite subgroup generators for `\Gamma` merely to satisfy the
API.

What must be generated:

- ambient `O(L)` generators, already available,
- ambient isotropic stabilizer generators, already available,
- finite quotient subgroup generators,
- quotient generator lifts to ambient matrices.

What does not need to be generated as a first-class object:

- the infinite arithmetic subgroup `\Gamma` itself.

Membership in `\Gamma` remains encoded by the existing `ConditionSet`-style
subgroup object.

## Enriques-specific construction

The first concrete target is `\Gamma_{En,2}` in the degree-2 Enriques case.

Use:

- the lattice `N = U + U(2) + E_8(-2)`,
- the finite image `\bar\Gamma_h` from the paper,
- the ambient plus group `O^+(N)`,
- the stable-plus kernel as the normal subgroup for quotient reduction.

Do not define `\Gamma_{En,2}` by ambient infinite generators.

Instead:

- compute or encode its finite image in the discriminant quotient,
- define `\Gamma_{En,2}` as the preimage of that finite image intersected with
  the plus condition,
- use finite double-coset splitting for isotropic orbits.

## Error cleanup plan

Replace manual error raising in the affected modules with assertions.

### Files to clean

- `src/coble_geometry_foundation.py`
- `src/external/py_polyhedral/binaries.py`
- `computations/oscar_centralizer.py`
- the new isotropic backend module

### Required changes

- `NotImplementedError` branches become asserted backend preconditions,
- subgroup `gens()` without a generator function becomes an asserted invariant,
- binary existence and subprocess success become asserted execution preconditions,
- missing Julia script / failed Julia command become asserted execution
  preconditions,
- no new `raise` statements are introduced in the backend or wrappers.

### Non-goal

Do not perform global repo-wide raise cleanup in this task. Restrict it to the
backend and direct backend dependencies.

## Phases

### Phase 1: quotient-capable subgroup metadata

Where:

- `src/coble_geometry_foundation.py`

Changes:

- extend private subgroup metadata so isotropic backend dispatch can determine:
  - ambient group choice,
  - quotient regime,
  - finite image subgroup when already known symbolically,
  - whether stable kernel containment is part of the subgroup contract.
- add private support for paired quotient generators and ambient lifts.

Dependencies:

- existing `ConditionSet` subgroup model,
- existing discriminant-group orthogonal group nouns.

Done when:

- every structured subgroup constructor used in the Enriques pipeline carries
  enough metadata to compile a finite quotient problem,
- opaque predicates are marked opaque and assert when isotropic orbit
  enumeration is requested.

Validation:

- unit tests that inspect the compiled private spec for:
  `O(L)`, `SO(L)`, `O^+(L)`, `SO^+(L)`, kernel-of-discriminant, and a
  preimage subgroup.

### Phase 2: finite quotient and lifting layer

Where:

- `src/research/isotropic_gamma_orbit_backend.py`

Changes:

- build the finite quotient image of the ambient group from ambient generators,
- compute the target subgroup image in that quotient,
- preserve quotient words and replay them on ambient generators.

Dependencies:

- discriminant-action code already present,
- structured subgroup metadata from Phase 1.

Done when:

- the backend can turn a quotient element or quotient double-coset
  representative into an actual ambient isometry matrix.

Validation:

- assert that every lifted quotient generator maps back to the intended quotient
  element,
- assert that replayed words in ambient generators and quotient generators have
  matching quotient images.

### Phase 3: isotropic ambient-orbit splitting backend

Where:

- `src/research/isotropic_gamma_orbit_backend.py`

Changes:

- wrap ambient isotropic line/plane/flag orbits,
- compute ambient stabilizers,
- map stabilizers to the finite quotient,
- split ambient orbits into subgroup orbits by finite double cosets,
- expose pairwise equivalence tests for lines and planes.

Dependencies:

- Phase 2 finite quotient/lifting layer,
- existing ambient isotropic Dutour-Sikirić binaries.

Done when:

- `\Gamma`-orbit representatives of isotropic lines, planes, and flags are
  produced as actual lattice vectors/matrices,
- pairwise isotropic subgroup equivalence tests are available.

Validation:

- regression tests that ambient `O(L)` results agree with the current ambient
  helper methods,
- tests that `O(L)` split by `O^+(L)` behaves as expected in known fixtures,
- tests that subgroup orbit representatives are primitive and isotropic.

### Phase 4: Enriques degree-2 specialization

Where:

- `computations/`
- `tests/`

Changes:

- implement the structured `\Gamma_{En,2}` construction needed for the
  degree-2 case,
- add Sterk's five primitive isotropic representatives as fixtures,
- compute the five `0`-cusp and nine `1`-cusp counts for Case 1.

Dependencies:

- previous phases,
- extracted Sterk representatives.

Done when:

- the backend reproduces Case 1 of the Dutour-Sikirić/Hulek table,
- the backend proves Sterk's five line representatives are pairwise
  non-equivalent modulo `\Gamma_{En,2}`.

Validation:

- assertions against the paper values `#I_1 = 5` and `#I_2 = 9`,
- assertions that the five Sterk vectors are primitive isotropic,
- assertions that every pair is non-equivalent modulo `\Gamma_{En,2}`.

### Phase 5: assertion cleanup

Where:

- `src/coble_geometry_foundation.py`
- `src/external/py_polyhedral/binaries.py`
- `computations/oscar_centralizer.py`
- `src/research/isotropic_gamma_orbit_backend.py`

Changes:

- replace manual raises with assertions,
- ensure new code uses asserted preconditions only.

Dependencies:

- none beyond file ownership.

Done when:

- `rg -n '\\braise\\b|NotImplementedError|ValueError|RuntimeError|FileNotFoundError'`
  over the targeted files returns nothing.

Validation:

- explicit grep in the targeted files,
- test suite still passes.

## Testing strategy

### Paper-backed fixtures

Add exact fixtures sourced from the literature:

- unpolarized Enriques ambient case:
  - `2` isotropic line orbits,
  - `2` isotropic plane orbits,
  - explicit representatives `L_1`, `L_2`, `P_1`, `P_2`.
- degree-2 polarized Enriques Case 1:
  - `5` isotropic line orbits,
  - `9` isotropic plane orbits.
- Sterk's five explicit primitive isotropic representatives:
  - each primitive,
  - each isotropic,
  - pairwise non-equivalent modulo `\Gamma_{En,2}`.

### Backend-owned correctness tests

- quotient lift correctness,
- ambient stabilizer image correctness,
- double-coset splitting counts in finite quotient,
- ambient/subgroup consistency:
  subgroup splitting of full ambient group returns the ambient orbit set.

### Verification commands

Use the repo test suite, not ad hoc task recipes.

Primary checks:

- focused pytest file for the isotropic subgroup backend,
- focused pytest file for Sterk/Enriques fixtures,
- `python -m py_compile` on edited Python files,
- grep check for forbidden `raise` usage in targeted files.

## Stop conditions

Stop and replan if any of the following becomes true:

- the quotient image of the target subgroup cannot be computed from the existing
  structured metadata,
- the lifting layer cannot recover ambient matrices from quotient words,
- the subgroup in question is only an opaque `ConditionSet` with no finite image
  data,
- reproducing Case 1 requires a new shared mathematical noun or public interface
  not covered by the current base.

In those cases, do not patch locally with ad hoc helpers. Split the missing base
work into its own task.

## Acceptance surface

This plan is complete only if the implementation yields all of the following:

- subgroup isotropic line/plane/flag orbits exposed on the orthogonal-group
  nouns,
- degree-2 Enriques Case 1 reproduces `5` zero-cusps and `9` one-cusps,
- Sterk's five line representatives are pairwise non-equivalent modulo
  `\Gamma_{En,2}`,
- the backend and direct dependencies contain no manual `raise` statements in
  the targeted files,
- no new `just` recipes or top-level process artifacts are introduced.
