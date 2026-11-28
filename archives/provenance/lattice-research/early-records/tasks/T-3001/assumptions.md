# Assumptions

- Canonical task backlog source is
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md).
- Local grounding must come from [GOAL.md](/home/dzack/research/GOAL.md),
  [REFERENCES.md](/home/dzack/research/REFERENCES.md), and the listed theory notes.
- Trusted shared code must follow the shared-code boundary in
  [AGENTS.md](/home/dzack/research/AGENTS.md#L176).

## Mathematical Assumptions

1. **Nodal condition definition**: A point p on a plane curve is a node (A_1
   singularity) if the curve is smooth at p and the Hessian matrix of second derivatives
   has rank 0 at p (i.e., both partial derivatives vanish to order 1, and the quadratic
   part is nondegenerate).

2. **Blowup construction**: The Coble surface S is obtained by blowing up P^2 at the 10
   nodal points. The exceptional divisors become part of the Picard lattice.

3. **K3 cover definition**: The double cover of P^2 branched along a sextic C is a K3
   surface when the branch curve has only A_1 singularities (nodes) and no other
   singularities.

4. **Weighted projective space**: The K3 cover lives in P(1,1,1,3) with coordinates
   [x:y:z:w] where w has weight 3 and the equation is w^2 = F(x,y,z).

5. **Rational surface**: A rational surface is one birational to P^2; equivalently, it
   has numerically trivial irregularity (q = 0) and geometric genus (p_g = 0).

6. **Point configuration**: The 10 points must be in general position (no 3 collinear,
   no 6 on a conic) to ensure the linear system of sextics through them has the expected
   dimension.
