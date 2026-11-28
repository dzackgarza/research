# Task T-2006: Gate Sextic Primitives

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - GOAL.md lines 8-13: Detailed description of Coble surface, nodal conditions, and K3
    cover
  - GOAL.md line 25: "**Task 1.1**: Derive an explicit equation $F(x,y,z)=0$ for a
    rational sextic with 10 nodes and the corresponding K3 surface $w^2 = F(x,y,z)$."
  - GOAL.md line 109-111: References to Steiner sextic and parametrization
- GOAL linkage: Gate for T-3001

## Objective

Gate the sextic primitives by checking exact nodal multiplicities, rationality or
birationality criteria, and K3-cover singularity profiles against T-1007. This gate
verifies:

1. **Nodal count verification**: The sextic produced by T-0007 must have exactly 10
   nodes (A_1 singularities)
2. **Nodal position verification**: Each node must be at a position matching the T-1007
   fixture coordinates
3. **Rationality verification**: The sextic curve must be rational (geometric genus 0)
   per T-1007
4. **K3 cover verification**: The double cover must have exactly 10 A_1 singularities
   matching the nodes
5. **Birationality criteria**: The Cremona transformation relating the sextic to
   $\mathbb{P}^2$ must be explicit

## Parent Sufficiency Map

Blocks the explicit sextic example until the chosen construction really matches the
literature-backed geometry.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: T-0007, T-1007
- Local sources:
- tasks/goal_expansion.md
- STATE_MACHINE.md
- PROOF_AUDITING.md

## Acceptance Criteria

1. **Node count**: Exactly 10 A_1 singularities must be present
2. **Node positions**: All 10 nodes must coincide with T-1007 fixture point coordinates
3. **Hessian non-vanishing**: At each node, the Hessian matrix must be non-zero
   (ensuring A_1 type)
4. **Curve rationality**: The sextic must be irreducible with geometric genus 0
5. **K3 singularities**: The double cover must have exactly 10 nodes, no worse
   singularities
6. **Moduli component**: The configuration must lie in the 9-dimensional component

## Non-Goals

1. **No new sextic construction**: This is a gate, uses T-0007 as black box
2. **No full moduli space exploration**: Only verifies one canonical fixture
3. **No automorphism computation**: Does not compute curve automorphisms
4. **No deformation theory**: Only verifies the given example, not the full family

## Allowed Dependencies

- **Prerequisite tasks**: T-0007 (sextic primitives), T-1007 (sextic fixture)
- **Local sources** (must cite):
  - tasks/goal_expansion.md — task ordering
  - STATE_MACHINE.md — tier semantics
  - PROOF_AUDITING.md — audit criteria

## Required Conventions

1. **Node definition**: A node is an A_1 singularity (double point with non-vanishing
   Hessian)
2. **K3 cover convention**: Weighted projective space $\mathbb{P}(1,1,1,3)$ with
   equation $w^2 = F(x,y,z)$
3. **Failure format**: Report as `gate_fail: sextic - <mismatch-details>`

## Failure Conditions

1. **Wrong node count**: If number of nodes ≠ 10, gate fails with `fail_node_count`
2. **Position mismatch**: If any node position differs from fixture, fails with
   `fail_node_position`
3. **Non-A1 singularity**: If any singularity is worse than A_1, fails with
   `fail_singularity_type`
4. **Non-rational**: If sextic has higher genus, fails with `fail_rationality`
5. **Extra K3 singularities**: If K3 cover has more than 10 nodes, fails with
   `fail_k3_singularities`
