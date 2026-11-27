# Coble Geometry Foundation Library Documentation

## Overview

The Coble Geometry Foundation Library (`coble_geometry_foundation.sage`) provides a
comprehensive mathematical foundation for Coble moduli computations.
It implements 9 layers of operations, organized from basic lattice constructions to
advanced group actions.

* * *

## Layer 1: Lattice Layer

**Purpose**: Construct fundamental lattices used in Coble geometry.

### Constructors

- **`rank_one_lattice(n)`**: Creates ⟨n⟩ lattice with Gram matrix [n]
- **`hyperbolic_plane()`**: Creates U with Gram matrix [[0,1],[1,0]]
- **`E8_lattice(scale=-1)`**: Creates E8(-1) root lattice (8-dimensional)
- **`S_Co_lattice()`**: Coble Picard lattice diag(2, -2¹⁰), signature (1,10)
- **`T_Co_lattice()`**: Coble transcendental diag(2,2,-2⁹), signature (2,9)
- **`T_En_lattice()`**: Enriques transcendental diag(2,2,-2⁸), signature (2,8)
- **`Lambda_K3_lattice()`**: K3 lattice U³⊕E8(-1)², signature (3,19)

### Operations

- **`lattice_signature(L)`**: Returns (p, q) signature tuple
- **`lattice_determinant(L)`**: Returns determinant of Gram matrix
- **`discriminant_group(L)`**: Returns A_L = L*/L as finite quadratic module
- **`discriminant_form(L)`**: Returns discriminant quadratic form
- **`primitive_embedding(S, L, M)`**: Checks if embedding is primitive (gcd=1)
- **`orthogonal_complement(S, L)`**: Computes S^⊥ in L
- **`is_primitive_embedding(S, L, M)`**: Validates primitive embedding

* * *

## Layer 2: Vector Layer

**Purpose**: Operations on vectors within lattices.

- **`inner_product(v, w, L)`**: Computes bilinear form v·w
- **`norm(v, L)`**: Computes v·v
- **`is_isotropic_vector(v, L)`**: Checks if v·v = 0
- **`divisibility(v, L)`**: Computes div(v) = gcd{v·w : w ∈ L}
- **`is_primitive_vector(v, L)`**: Checks if div(v) = 1
- **`vector_in_discriminant_group(v, L)`**: Maps v to A_L

* * *

## Layer 3: Subspace Layer

**Purpose**: Operations on subspaces of lattices.

- **`subspace_span(vectors, L)`**: Computes span of vectors in L
- **`subspace_dimension(J)`**: Returns dimension of subspace
- **`subspace_gram_matrix(J, L)`**: Returns Gram matrix of subspace
- **`is_isotropic_subspace(J, L)`**: Checks if all v·w = 0 for v,w ∈ J
- **`is_primitive_subspace(J, L)`**: Checks if J ∩ L = J
- **`orthogonal_complement_in_lattice(J, L)`**: Computes J^⊥ in L
- **`quotient_lattice(J_perp, J, L)`**: Computes J^⊥/J

* * *

## Layer 4: Isotropic Plane Layer

**Purpose**: Special handling for isotropic planes.

**Definition**: An isotropic plane J is a 2-dimensional subspace where v·w = 0 for all
v,w ∈ J.

- **`is_isotropic_plane(J, L)`**: Checks dimension=2 AND isotropy
- **`enumerate_isotropic_planes(L, max_search, primitive_only)`**: Enumerates isotropic
  planes
- **`isotropic_plane_to_discriminant_image(J, L)`**: Maps plane to A_L

* * *

## Layer 5: Discriminant Group Layer

**Purpose**: Discriminant group computations and GAP integration.

- **`discriminant_group_structure(L)`**: Returns A_L ≅ ℤ/d₁ℤ ⊕ ... ⊕ ℤ/dₙℤ
- **`discriminant_form_value(v, L)`**: Computes q_L(v) ∈ ℚ/ℤ
- **`discriminant_bilinear_form(v, w, L)`**: Computes b_L(v,w)
- **`orthogonal_group_discriminant(L)`**: Returns O(q_L) as GAP group
- **`compute_orbits_gap(group, elements)`**: Uses GAP's Orbits() for computation

* * *

## Layer 6: Group Action Layer

**Purpose**: Group actions on lattices and sets.

- **`stabilizer_subgroup(G, element)`**: Computes Stab_G(element)
- **`orbit_of_element(G, element)`**: Returns orbit under group action
- **`centralizer_subgroup(G, element)`**: Computes Z_G(element)
- **`group_action_on_set(G, S)`**: Defines action of G on set S

* * *

## Layer 7: Enumeration Layer

**Purpose**: Systematic enumeration of lattice elements.

- **`enumerate_isotropic_vectors(L, max_norm)`**: All vectors with v·v = 0
- **`enumerate_primitive_isotropic_vectors(L, max_norm)`**: Primitive isotropic vectors
- **`enumerate_vectors_bounded(L, bound)`**: All v with |v·v| ≤ bound
- **`enumerate_with_divisibility(L, div_value, max_norm)`**: Vectors with div(v) =
  div_value

All enumerations have explicit termination conditions.

* * *

## Layer 8: Verification Layer

**Purpose**: Verify mathematical correctness of computations.

- **`assert_lattice_invariants(L, expected_sig, expected_det)`**: Verify signature and
  determinant
- **`assert_primitive_embedding(S, L, M)`**: Verify embedding is primitive
- **`assert_orthogonal_complement(S, T, L)`**: Verify S ⊥ T = L
- **`assert_discriminant_form_properties(L)`**: Verify q_L properties
- **`compare_lattices_by_invariants(L1, L2)`**: Compare invariants

* * *

## Layer 9: Coding Standards Layer

**Purpose**: Safe printing and logging utilities.

- **`checked_print(assertion, message, value)`**: Print only if assertion passes
- **`mathematical_assertion(condition, error_message)`**: Assert with math context
- **`document_computation(description, inputs, outputs)`**: Structured logging

* * *

## Usage Example

```sage
load("coble_geometry_foundation.sage")

# Create lattices
U = hyperbolic_plane()
E8 = E8_lattice()

# Compute invariants
sig = lattice_signature(U)  # (1, 1)
det = lattice_determinant(E8)  # 1

# Work with vectors
e1 = vector(ZZ, [1, 0])
isotropic = is_isotropic_vector(e1, U)  # True

# Enumerate isotropic vectors
vectors = enumerate_isotropic_vectors(U, max_norm=10)

# Verify properties
assert_lattice_invariants(E8, (0, 8), 1)
```

* * *

## Mathematical Definitions

### Isotropic Plane

A 2-dimensional subspace J of lattice L is isotropic if v·w = 0 for all v,w ∈ J.

### Primitive Embedding

Embedding M: S → L is primitive if (S ⊗ ℚ) ∩ L = S, equivalently gcd of Smith form
diagonal entries = 1.

### Discriminant Group

A_L = L*/L where L* = {v ∈ L ⊗ ℚ : v·w ∈ ℤ for all w ∈ L}.

### Divisibility

div(v) = gcd{v·w : w ∈ L} = order of v in A_L.

* * *

## References

- Conway & Sloane, "Sphere Packings, Lattices and Groups"
- Nikulin, "Integer symmetric bilinear forms and some of their geometric applications"
