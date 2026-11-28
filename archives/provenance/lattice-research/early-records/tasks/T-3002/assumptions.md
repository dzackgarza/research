# Assumptions

- Canonical task backlog source is
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md).
- Local grounding must come from [GOAL.md](/home/dzack/research/GOAL.md),
  [REFERENCES.md](/home/dzack/research/REFERENCES.md), and the listed theory notes.
- Trusted shared code must follow the shared-code boundary in
  [AGENTS.md](/home/dzack/research/AGENTS.md#L176).

## Mathematical Assumptions

1. **Lattice definition**: S_Co and T_Co are integral lattices ( bilinear form takes
   integer values on lattice vectors).

2. **Signature convention**: Signatures are given as (p, n) where p = number of positive
   eigenvalues, n = number of negative eigenvalues.

3. **Nikulin (r,a,δ) definition**:
   - r = rank of the lattice
   - a = length of the discriminant group (number of generators)
   - δ = 0 or 1 depending on the discriminant form type

4. **Discriminant form**: For a lattice L, the discriminant form is the finite quadratic
   form on A_L = L^*/L.

5. **Genus uniqueness condition**: For 2-elementary lattices with r > a, Nikulin's
   classification guarantees a unique isometry class in the genus.

6. **Complement embedding**: If S_Co and T_Co are orthogonal complements in Λ_K3, then
   S_Co = T_Co^⊥_Λ_K3 and vice versa.
