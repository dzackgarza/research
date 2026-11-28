# Candidate Admission Target

## Exact Candidate Surface

The only surface eligible for admission under `T-0011` is the symbol-level inventory
below. Unless a later replan says otherwise, the current public shared surface is the
exported `__all__` list in `src/coble_geometry_foundation.sage`. Any
implementation output outside the admitted-candidate symbols below or inside the
explicit exclusion list requires `REPLAN_REQUIRED` before further work.

## Candidate admitted-item ledger

### Constructors

- `rank_one_lattice`
- `hyperbolic_plane`
- `Lambda_K3_lattice`

### Invariant and discriminant extractors

- `lattice_signature`
- `lattice_determinant`
- `discriminant_group`

## Explicitly excluded symbol surface

### Task-shaped or proof-surface helpers

- `assert_lattice_invariants`
- `assert_primitive_embedding`
- `assert_orthogonal_complement`
- `assert_discriminant_form_properties`
- `checked_print`
- `mathematical_assertion`
- `document_computation`

### Bounded-search stand-ins and heuristic surrogates

- `enumerate_isotropic_planes`
- `enumerate_isotropic_vectors`
- `enumerate_primitive_isotropic_vectors`
- `enumerate_vectors_bounded`
- `enumerate_with_divisibility`
- `compare_lattices_by_invariants`

## Ambiguous symbols requiring explicit exclusion or later replan

The symbols below are not part of the admitted candidate surface for the current
pre-audit package. They remain blocked unless a later replan pins exact local provenance
and exact routed backend support symbol-by-symbol.

- `T_dP_lattice`
- `S_En_lattice`
- `S_Co_lattice`
- `T_Co_lattice`
- `T_En_lattice`
- `is_primitive_embedding`
- `orthogonal_complement`
- `compute_orbits_gap`
- `stabilizer_subgroup`
- `orbit_of_element`
- `A1_lattice`
- `E8_lattice`
- `divisibility`
- `discriminant_form`
- `discriminant_group_structure`
- `discriminant_form_value`
- `discriminant_bilinear_form`
- `primitive_embedding`
- `vector_in_discriminant_group`
- `centralizer_subgroup`
- `group_action_on_set`
- `orthogonal_group_discriminant`
- `inner_product`
- `norm`
- `is_isotropic_vector`
- `subspace_span`
- `subspace_dimension`
- `subspace_gram_matrix`
- `is_isotropic_subspace`
- `is_primitive_subspace`
- `orthogonal_complement_in_lattice`
- `quotient_lattice`

## Exclusion rationale

- task-shaped `assert_*` or `verify_*` helpers are excluded from the trusted shared
  base;
- bounded enumeration is excluded wherever it stands in for exact orbit, isotropic,
  embedding, or quotient algorithms;
- print/logging/prose proof surfaces are excluded;
- fail-open exception paths around mathematical obligations are excluded;
- raw ad hoc constructor code is excluded where the theory docs route the task to mature
  exact backends;
- helper APIs whose only purpose is to hide theorem burden or downgrade exact claims
  into heuristic surrogates are excluded.
- symbols whose local docs fix only mathematical intent or predicate meaning, but not an
  exact symbol-level backend binding, are excluded from the current admitted surface
  until a later replan pins that provenance explicitly.
- wrapper symbols whose semantics still depend on cover/group/element-level presentation
  choices, rather than one exact admitted backend operation, are excluded from the
  current admitted surface until a later replan pins those conventions explicitly.
- symbols whose operation name is pinned but whose exact mathematical input/action
  contract or replay certificate obligation is not yet frozen are excluded from the
  current admitted surface until a later replan pins that contract explicitly.

## Trust-budget movement

- Burden moved into the trusted base, if admission succeeds: exact object construction,
  exact coercion, exact transform, and exact invariant extraction for this frozen
  surface.
- Burden not moved: theorem-level classification, uniqueness, exhaustiveness, embedding
  existence proofs, or any downstream claim in `T-0001`, `T-0002`, `T-0003`, `T-0005`,
  `T-0006`, or `T-0008`.
- Prior admissions relied on: only the external mature backends named in
  `tasks/T-0011/dependencies.md` and documented in the local theory notes.
- Coercion status: the current public surface exposes no admitted coercion symbol.
  Any future coercion primitive requires a prior replan that adds the exact symbol name,
  routed backend operation, and certificate route before implementation.
