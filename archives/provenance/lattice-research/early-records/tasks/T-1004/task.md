# Task T-1004: Primitive-Embedding Fixtures

## Status

Selected in Wave A. TASK_SPECIFICATION complete as of 2026-04-02.

## Tier

Tier 1.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - GOAL.md line 27: "Derive the explicit primitive embedding matrices for
    $T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}}
    \hookrightarrow \Lambda_{\mathrm{K3}}$."
  - GOAL.md line 22: "The **primitivity of the lattice embeddings** lack rigorous
    derivation in terms of coordinate bases."
  - GOAL.md Task 1.3: "Derive the explicit primitive embedding matrices for
    $T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}}
    \hookrightarrow \Lambda_{\mathrm{K3}}$."
- GOAL linkage: Fixture support for T-0003, T-2003, T-2008, T-3003, and T-3011

## Objective

Assemble primitive-embedding fixtures with known complements or uniqueness properties,
using standard examples and Oscar documentation-backed cases.
The fixture package must include:

1. **T_Co → T_En fixture**: 11×12 embedding matrix with known complement lattice
   (orthogonal complement in T_En has rank 1)
2. **T_En → T_dP fixture**: 12×20 embedding matrix with known complement (rank 8 even
   lattice)
3. **T_dP → Λ_K3 fixture**: 20×22 embedding matrix with known complement (rank 2)
4. **A_1 → E_8 fixture**: Canonical primitive embedding of the root lattice A_1 into E_8
   with complement E_8
5. **U → E_8 fixture**: Hyperbolic plane embedding with known signature and discriminant
6. **Complement lattice data**: For each embedding, the exact discriminant group and
   signature of the orthogonal complement
7. **Uniqueness test cases**: Examples where the primitive embedding is unique up to
   automorphisms (per Nikulin's theorems)

## Parent Sufficiency Map

Provides exact expected outcomes for embedding primitives and gates; does not verify
them by itself.

## Deliverable Type

fixture data

## Current Dependencies

- Prerequisite tasks: none
- Local sources:
- theory/oscar_lattices.md
- REFERENCES.md

## Acceptance Criteria

1. **T_Co → T_En matrix**: The embedding matrix must be a 11×12 integer matrix
   preserving the bilinear form and inducing an injection with torsion-free cokernel
   (primitive)
2. **T_En → T_dP matrix**: The embedding matrix must be a 12×20 integer matrix with
   primitive image
3. **T_dP → Λ_K3 matrix**: The embedding matrix must be a 20×22 integer matrix
   completing the chain to the K3 lattice
4. **Complement verification**: For each embedding, the orthogonal complement must have
   the documented rank and discriminant form
5. **A_1 → E_8 verification**: The embedding must map the A_1 root lattice injectively
   into E_8 with even integral image
6. **U → E_8 verification**: The hyperbolic plane embedding must have signature (1,1)
   and discriminant -1
7. **Serialization roundtrip**: Fixtures serialized to JSON and re-loaded must produce
   identical data structures

## Non-Goals

1. **No algorithmic embedding search**: This task provides pre-computed fixtures;
   algorithmic verification is T-0003
2. **No primitivity proof**: The fixture data assumes primitivity; formal proof is
   T-0003
3. **No complement computation**: Fixtures provide complement data; computation is
   T-0003
4. **No uniqueness proof**: The fixture tests uniqueness; formal proof is mathematical
   work
5. **No full automorphism group computation**: Only provides canonical embeddings;
   automorphism groups are T-0002

## Allowed Dependencies

- **Prerequisite tasks**: none (this is T-1 foundation)
- **Local sources** (must cite specific sections):
  - theory/oscar_lattices.md — Oscar lattice construction patterns
  - REFERENCES.md — Nikulin (1979) for primitive embedding classification

## Required Conventions

1. **Matrix convention**: All embedding matrices use the standard basis ordering from
   T-1001 and T-1002
2. **Primitivity definition**: An embedding $i: L \to M$ is primitive if $M/i(L)$ is
   torsion-free
3. **Complement computation**: Orthogonal complement is computed in the ambient lattice
   with respect to the induced bilinear form
4. **Embedding direction**: All embeddings are specified as matrices $M_{source \to
   target}$ where rows index source basis elements
5. **Fixture naming**: Use pattern `embed_<source>_<target>` for embedding matrices,
   `comp_<source>_<target>` for complements
6. **Export format**: All matrices in JSON as integer arrays

## Failure Conditions

1. **Non-primitive embedding**: If $M/i(L)$ has nontrivial torsion, the fixture is
   rejected
2. **Form preservation failure**: If the embedding does not preserve the bilinear form
   ($B(i(u), i(v)) = B(u, v)$), the fixture is rejected
3. **Missing complement data**: If any embedding lacks complete complement lattice
   specification, the fixture is rejected
4. **Incorrect rank**: If complement rank does not match expected value (rank(target) -
   rank(source)), the fixture is rejected
5. **Serialization failure**: If the fixture cannot be serialized and deserialized
   correctly, it is rejected
