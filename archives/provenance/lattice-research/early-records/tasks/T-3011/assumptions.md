# Assumptions

- Canonical task backlog source is
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md).
- Local grounding must come from [GOAL.md](/home/dzack/research/GOAL.md),
  [REFERENCES.md](/home/dzack/research/REFERENCES.md), and the listed theory notes.
- Trusted shared code must follow the shared-code boundary in
  [AGENTS.md](/home/dzack/research/AGENTS.md#L176).

## Mathematical Assumptions

1. **Involution definition**: θ is an involution if θ^2 = I (identity matrix).
   It is an isometry if θ^T * G * θ = G where G is the Gram matrix.

2. **Eigenspace definition**: For an involution θ on a lattice, the +1 eigenspace is Λ^θ
   = {v ∈ Λ | θ(v) = v} = ker(θ - I). The -1 eigenspace is Λ^-θ = {v ∈ Λ | θ(v) = -v} =
   ker(θ + I).

3. **Sign involution**: The "sign involution" on Λ_K3 is the involution that acts as +1
   on T_Co and -1 on S_Co (or vice versa), making these the invariant and coinvariant
   sublattices.

4. **Discriminant group action**: The action of θ on A_Λ = Λ^*/Λ must be compatible with
   the quadratic form; for Λ_K3 (unimodular), this is the sign involution on the
   22-torsion.

5. **Distinguished vectors**: h_Co is the Coble polarization (in T_Co) and h_En is the
   Enriques polarization (in T_En). The involution θ maps h_Co to h_En.

6. **2-elementary property**: Both eigenspaces Λ_K3^θ and Λ_K3^-θ are 2-elementary
   lattices (their discriminant groups are (Z/2Z)^a for some a).
