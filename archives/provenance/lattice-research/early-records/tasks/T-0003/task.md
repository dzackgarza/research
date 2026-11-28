# Task T-0003: Composable Embedding Primitives

## Status

Selected in Wave A. TASK_SPECIFICATION complete as of 2026-04-02.

## Tier

Tier 0.

## Origin

- GOAL.md source: line 27 "Derive the explicit primitive embedding matrices for T_Co →
  T_En → T_dP → Λ_K3"
- GOAL.md line 22: "the primitivity of the lattice embeddings"
- GOAL.md line 82: "verify the embedding T_Co → Λ_K3 is primitive"
- GOAL.md Task 1.3: explicit primitive embedding matrices

## Objective

Expose composable embedding primitives backed by Oscar/Hecke:
- embed_lattice(source, target, basis_matrix) → embedded lattice with map
- compose_embeddings(f: A→B, g: B→C) → A→C composition
- image_lattice(embedding) → sublattice image of source
- orthogonal_complement(L, S) → L⊥ within L containing S
- matrix_export(embedding) → integer matrix of the embedding map
- is_primitive_embedding(embedding) → Boolean (cokernel is torsion-free)
- saturated_lattice(L) → saturation of L in its ambient lattice
- primitive_closure(L, ambient) → minimal primitive overlattice

## Deliverable Type

shared tool — reusable primitives with explicit contracts.

## Acceptance Criteria

1. **Embedding construction**: Given source lattice S and target lattice T with integer
   matrix M (size rank(T)×rank(S)), produce an embedding if M preserves the bilinear
   form

2. **Complement computation**: Given lattice L and sublattice S ⊂ L, compute L⊥∩S⊥
   correctly

3. **Primitivity test**: Verify that an embedding has torsion-free cokernel

4. **Composition**: Compose two embeddings and verify the composite preserves forms

5. **Matrix export**: Extract the exact integer matrix of any embedding

6. **Test cases**: Embed A_1 → E8, U → Λ_K3, T_Co → Λ_K3 produce correct invariants

7. **Import test**: All functions importable from coble_geometry_foundation

## Non-Goals

- Does not prove existence of embedding for specific (r,a,δ) combinations (theorem
  claim)
- Does not compute automorphism groups or stabilizers (T-0004)
- Does not enumerate indefinite isotropic planes (T-0005)
- Does not construct involutions (T-0008)
- Does not compute Vinberg chambers (T-0006)

## Allowed Dependencies

- Prerequisite tasks: T-0001 (uses its lattice constructors)
- Local sources:
  - src/coble_geometry_foundation.sage (extend with embeddings)
  - theory/oscar_lattices.md (Oscar embedding API)
  - theory/library_integration.md

## Required Conventions

- Function naming: `<operation>_embedding()` or `<operation>_lattice()`
- Embedding returns a named tuple or dict with: matrix, source, target, is_primitive
- Matrix is Integer matrix preserving bilinear form
- All functions raise on invalid input (non-integral, wrong dimensions, form mismatch)

## Failure Conditions

1. If embedding construction fails on valid source/target/matrix → fail
2. If complement computation returns wrong lattice → fail
3. If primitivity test gives incorrect result for known primitive/non-primitive → fail
4. If composition produces non-composable embeddings → fail
5. If matrix export doesn't match input matrix exactly → fail
6. If any function raises exception on valid input → fail

## Parent Sufficiency Map

Supplies embedding infrastructure for:
- T-2003: gates embedding primitives using fixtures
- T-3003: constructs T_Co → Λ_K3 embedding
- T-3004: constructs embedding chain through T_En, T_dP
- T-3011: uses embedding to extract θ eigenspaces
- T-3007: computes finite-discriminant centralizer data

Discharges no GOAL.md burden by itself.
