# Dependencies

## Prerequisite Tasks

- none

## Local Sources

- src/coble_geometry_foundation.sage
- AGENTS.md
- STATE_MACHINE.md
- PROOF_AUDITING.md
- tasks/goal_expansion.md
- theory/library_integration.md
- theory/oscar_lattices.md
- theory/gap_orbits.md
- theory/indefinite_jl.md
- theory/buildings.md
- justfile
- tasks/T-0011/conventions.md
- tasks/T-0011/admission_target.md
- tasks/T-0011/attack_surface.md
- tasks/T-0011/replay_contract.md

## Required Tools / Backends

- Oscar/Hecke for exact lattice constructors, discriminant-side operations, embeddings,
  and invariant/coinvariant lattice operations
- GAP for finite exact orbit and stabilizer computations
- Indefinite.jl and/or buildings.sage for indefinite isotropic orbit primitives
- Sage only as the orchestrating host language around the admitted backend calls

## Primitive-to-backend routing ledger

### Oscar/Hecke-routed constructor and invariant symbols

- `rank_one_lattice` → `integer_lattice(gram = matrix(ZZ, [n]))`
- `hyperbolic_plane` → `hyperbolic_plane_lattice`
- `Lambda_K3_lattice` → `k3_lattice`
- `lattice_signature` → `signature_tuple`
- `lattice_determinant` → `det`
- `discriminant_group` → `discriminant_group`

### Symbols not routed in the current pre-audit package

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

Any future attempt to admit one of these symbols requires a prior replan that pins exact
local provenance and exact routed backend operations symbol-by-symbol.

## Admission Burden

- The candidate admitted item is frozen in `tasks/T-0011/admission_target.md` before
  implementation.
- The only theorem burden permitted to move into the trusted base is exact object-level
  construction, coercion, transform, and invariant extraction for the frozen candidate
  surface; no theorem-level classification or exhaustiveness burden moves here.
- Prior admissions relied on are limited to the external mature backends documented in
  the local theory notes; no prior repo-local shared-code admission is assumed.
- Anti-laundering condition: if any admitted primitive still depends on poisoned helper
  semantics, bounded search, print theater, fail-open control flow, or hidden shared
  helpers, the task fails rather than silently shrinking or relabeling the burden.

## Affected Downstream Tasks

- T-0001
- T-0002
- T-0003
- T-0005
- T-0006
- T-0008
