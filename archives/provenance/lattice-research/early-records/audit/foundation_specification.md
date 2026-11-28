# Mathematical Foundation Library Specification

## Purpose

Provide canonical, verified implementations of all mathematical operations needed for
Coble moduli computations.
Agents compose these primitives instead of reimplementing, preventing mathematical
errors.

## Coding Standards

**MANDATORY**:
- Every print statement must be preceded by an assertion
- Every function must have docstring with mathematical definition
- Every function must validate inputs with assertions
- All mathematical concepts must match formal definitions

## Required Layers

### 1. Lattice Layer

**Constructors**:
- `rank_one_lattice(n)` - ⟨n⟩ lattice
- `hyperbolic_plane()` - U lattice
- `E8_lattice(scale=-1)` - E₈(-1) lattice
- `S_Co_lattice()` - ⟨2⟩ ⊕ ⟨-2⟩¹⁰ via direct_sum
- `T_Co_lattice()` - ⟨2⟩ ⊕ U ⊕ E₈(-1) via direct_sum
- `T_En_lattice()` - ⟨2⟩² ⊕ ⟨-2⟩⁸ via direct_sum
- `Lambda_K3_lattice()` - U³ ⊕ E₈(-1)² via direct_sum

**Operations**:
- `lattice_signature(L)` - (p, q) signature
- `lattice_determinant(L)` - determinant
- `discriminant_group(L)` - A_L with structure
- `discriminant_form(L)` - q_L: A_L → ℚ/ℤ or ℚ/2ℤ
- `primitive_embedding(S, L)` - embed S primitively in L, return embedding matrix
- `orthogonal_complement(S, L)` - T = S^⊥ in L
- `is_primitive_embedding(S, L, embedding_matrix)` - check gcd = 1

### 2. Vector Layer

**Operations**:
- `inner_product(v, w, L)` - v·w in lattice L
- `norm(v, L)` - v·v
- `is_isotropic_vector(v, L)` - check v·v = 0
- `divisibility(v, L)` - div(v) = gcd{v·w : w ∈ L}
- `is_primitive_vector(v, L)` - check div(v) = 1
- `vector_in_discriminant_group(v, L)` - image of v in A_L

### 3. Subspace Layer

**Operations**:
- `subspace_span(vectors, L)` - span of vectors in L
- `subspace_dimension(J)` - dimension
- `subspace_gram_matrix(J, L)` - Gram matrix of J
- `is_isotropic_subspace(J, L)` - check all v,w ∈ J satisfy v·w = 0
- `is_primitive_subspace(J, L)` - check J ∩ L = J (no denominators needed)
- `orthogonal_complement_in_lattice(J, L)` - J^⊥ in L
- `quotient_lattice(J_perp, J, L)` - J^⊥/J with Gram matrix

### 4. Isotropic Plane Layer

**Definition**: An isotropic plane J is a 2-dimensional subspace where all v,w ∈ J
satisfy v·w = 0

**Operations**:
- `is_isotropic_plane(J, L)` - check dimension = 2 AND isotropic
- `enumerate_isotropic_planes(L, max_search=None)` - enumerate all isotropic planes
  - Must use correct definition: span of two mutually orthogonal isotropic vectors
  - Must handle termination properly
  - Must return primitive planes only if requested
- `isotropic_plane_to_discriminant_image(J, L)` - map J to image in A_L

### 5. Discriminant Group Layer

**Operations**:
- `discriminant_group_structure(L)` - A_L ≅ (ℤ/d₁ℤ) ⊕ ... ⊕ (ℤ/dₙℤ)
- `discriminant_form_value(v, L)` - q_L(v) ∈ ℚ/ℤ or ℚ/2ℤ
- `discriminant_bilinear_form(v, w, L)` - b_L(v,w)
- `orthogonal_group_discriminant(L)` - O(q_L) as GAP group
- `compute_orbits_gap(group, elements)` - GAP orbit computation wrapper
  - Must use GAP's Orbits() function
  - Must return orbit count and orbit representatives

### 6. Group Action Layer

**Operations**:
- `stabilizer_subgroup(G, element)` - Stab_G(element)
- `orbit_of_element(G, element)` - orbit under group action
- `centralizer_subgroup(G, element)` - Z_G(element)
- `group_action_on_set(G, S)` - define action of G on set S

### 7. Enumeration Layer

**Operations**:
- `enumerate_isotropic_vectors(L, max_norm=None)` - all v with v·v = 0
- `enumerate_primitive_isotropic_vectors(L, max_norm=None)` - primitive isotropic
- `enumerate_vectors_bounded(L, bound)` - all v with |v·v| ≤ bound
- `enumerate_with_divisibility(L, div_value)` - all v with div(v) = div_value

**Requirements**:
- All enumerations must have termination conditions
- Must document search bounds and completeness
- Must distinguish exhaustive vs bounded search

### 8. Verification Layer

**Operations**:
- `assert_lattice_invariants(L, expected_sig, expected_det)` - verify signature,
  determinant
- `assert_primitive_embedding(S, L, M)` - verify embedding is primitive
- `assert_orthogonal_complement(S, T, L)` - verify S ⊥ T and S ⊕ T = L
- `assert_discriminant_form_properties(L)` - verify q_L properties
- `compare_lattices_by_invariants(L1, L2)` - compare signature, det, disc group

### 9. Coding Standards Layer

**Utilities**:
- `checked_print(assertion, message, value)` - print only if assertion passes
- `mathematical_assertion(condition, error_message)` - assertion with math context
- `document_computation(description, inputs, outputs)` - structured logging

## Acceptance Criteria

- All functions have docstrings with mathematical definitions
- All functions validate inputs with assertions
- All print statements preceded by assertions
- All mathematical concepts match formal definitions from literature
- All GAP operations use standard library functions
- All enumerations have explicit termination conditions
- Test suite verifies all functions on small examples

## Deliverables

1. `coble_geometry_foundation.sage` - complete implementation
2. `test_foundation.sage` - test suite with small examples
3. Documentation explaining each layer and function
