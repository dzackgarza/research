# T-0004: assumptions.md

## Mathematical Assumptions

1. **T_Co structure**: T_Co ≅ diag(2, 2, -2, ..., -2) (rank 11, signature (2, 9), det =
   -2048). This is the transcendental lattice of a terminal Coble surface of K3 type.

2. **Discriminant group**: A_T = T_Co^*/T_Co ≅ (Z/2Z)^11. The isomorphism is canonical
   for 2-elementary lattices.

3. **Discriminant form**: q_T: A_T → Q/2Z is given by q_T(x) = (1/2)(x_1 + x_2 - x_3 -
   ... - x_11) mod 2Z. This follows from T_Co = diag(2, 2, -2^9): for x = (x_1, ...,
   x_11) ∈ F_2^11, q_T(x) = (1/2)(x_1^2 + x_2^2 - x_3^2 - ... - x_11^2) mod 2Z =
   (1/2)(x_1 + x_2 - x_3 - ... - x_11) mod 2Z since x_i^2 ≡ x_i mod 2. **Critical:** The
   signs CANNOT be dropped.
   While -1 ≡ 1 (mod 2) as integers, -(1/2) ≡ 3/2 (mod 2Z) ≠ 1/2 (mod 2Z). So q_T(x) ≠
   (1/2)(x_1 + ... + x_11) mod 2Z.

4. **Isotropic elements**: x ∈ A_T is isotropic iff q_T(x) = 0 mod 2Z, i.e., x_1 + x_2 -
   x_3 - ... - x_11 ≡ 0 (mod 4). There are exactly 528 isotropic elements (verified in
   T-0003: q_T distribution {0: 528, 1/2: 528, 1: 496, 3/2: 496}).

5. **Orthogonal group**: O(q_T) = {g ∈ GL(11, F_2) : q_T(g·x) = q_T(x) for all x ∈ A_T}.
   This is the orthogonal group of the quadratic form q_T over F_2.

6. **GAP availability**: GAP 4 is available and can construct matrix groups over finite
   fields and compute orbits.

## Conventions

- Vectors in A_T are represented as lists of 0s and 1s (F_2 elements).
- The quadratic form q_T is computed as (1/2)(x_1 + x_2 - x_3 - ... - x_11) mod 2Z,
  returning 0, 1/2, 1, or 3/2 mod 2Z.
- Orbit representatives are given as F_2^11 vectors.
