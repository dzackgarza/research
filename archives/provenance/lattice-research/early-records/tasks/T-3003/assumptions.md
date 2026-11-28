# Assumptions

- Canonical task backlog source is
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md).
- Local grounding must come from [GOAL.md](/home/dzack/research/GOAL.md),
  [REFERENCES.md](/home/dzack/research/REFERENCES.md), and the listed theory notes.
- Trusted shared code must follow the shared-code boundary in
  [AGENTS.md](/home/dzack/research/AGENTS.md#L176).

## Mathematical Assumptions

1. **Primitive embedding definition**: An embedding i: L → M of integral lattices is
   primitive if the cokernel M/i(L) is torsion-free (equivalently, if L is a direct
   summand of M).

2. **Gram matrix preservation**: For embedding M: L → M_ambient, the induced map
   preserves the bilinear form if M^T * G_ambient * M = G_L, where G_* are Gram
   matrices.

3. **Orthogonal complement**: For L ⊂ M_ambient, the orthogonal complement L^⊥_M_ambient
   = {v ∈ M_ambient | (v, L) = 0}.

4. **Isometry definition**: Two lattices L and L' are isometric if there exists an
   isomorphism L → L' preserving the bilinear form.

5. **K3 lattice**: Λ_K3 is the unique even unimodular lattice of signature (22,0).
   Standard basis conventions from T-1001 apply.

6. **T_Co basis**: T_Co uses the basis verified in T-3002 (signature (2,9), determinant
   1).
