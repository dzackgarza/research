# Implementation Plan

## Mathematical Claim

Derive an explicit rational plane sextic F(x,y,z)=0 with exactly 10 nodes and its K3
double cover w^2 = F in P(1,1,1,3).

## Subtasks

1. **Load point configuration**: Use T-1007 fixture to obtain the canonical 10-point
   configuration.

2. **Construct nodal linear system**: Use T-0007 primitives to build the linear system
   of sextics passing through the 10 points with multiplicity 2.

3. **Derive sextic equation**: Solve the linear system to obtain explicit coefficients
   for F(x,y,z).

4. **Verify nodal profile**: Use T-0007 singularity checks to verify exactly 10 A_1
   singularities at the specified points.

5. **Compute K3 cover**: Use T-0007 K3 cover generation to produce w^2 = F in
   P(1,1,1,3).

6. **Verify K3 singularities**: Verify the double cover has exactly 10 A_1 singularities
   above the nodal points.

7. **Rationality verification**: Use T-0007 rationality/birationality checks to confirm
   the base surface is rational.

## Exit Criteria

All 7 subtasks must pass with verification reports.
If any check fails, task fails.

## Validation

- Each subtask produces a verification report (pass/fail with evidence).
- Final report aggregates all subtask results.
- Reduction ledger must be created documenting each computation's GOAL.md rationale.
