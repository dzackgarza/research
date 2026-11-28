# Task T-1007: Canonical 10-Nodal Sextic Fixture Package

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 1.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - GOAL.md lines 8-13: "A **Coble surface** $S$ is obtained via the blowup $\pi: S \to
    \mathbb{P}^2$ at the 10 $A_1$ nodes of an irreducible rational plane sextic $C = \{
    F(x,y,z) = 0 \}$... The polynomial $F$ is a homogeneous sextic... satisfying the
    **nodal conditions** $F(p_m) = \frac{\partial F}{\partial x}(p_m) = \frac{\partial
    F}{\partial y}(p_m) = \frac{\partial F}{\partial z}(p_m) = 0$ for 10 'special' point
    positions $p_1, \dots, p_{10} \in \mathbb{P}^2$. The moduli space of such sextics is
    9-dimensional."
  - GOAL.md line 25: "**Task 1.1**: Derive an explicit equation $F(x,y,z)=0$ for a
    rational sextic with 10 nodes and the corresponding K3 surface $w^2 = F(x,y,z)$."
  - GOAL.md lines 109-111: References to the "image of $\mathbb{P}^1$ under a map $(s:t)
    \to [f_0:f_1:f_2]$" realization and Steiner sextic.
- GOAL linkage: Fixture support for G1.1 and T-0007

## Objective

Assemble a canonical 10-nodal sextic fixture package from local literature, including
the point configuration, expected nodal profile, and parametrization data when
available. The fixture package must include:

1. **Point configuration**: 10 distinct points in $\mathbb{P}^2(\mathbb{C})$ that
   satisfy the nodal conditions for a rational sextic
2. **Nodal profile**: Explicit verification that each point is an $A_1$ singularity
   (Milnor number 1, modality 0)
3. **Sextic coefficients**: The 28 monomial coefficients for $F(x,y,z)$ of degree 6 that
   vanish at all 10 points with first derivatives
4. **K3 cover equation**: The double cover $w^2 = F(x,y,z)$ in $\mathbb{P}(1,1,1,3)$
   with branch divisor verification
5. **Parametrization data**: If available, the rational parametrization $(s:t) \mapsto
   [f_0(s,t):f_1(s,t):f_2(s,t)]$ mapping $\mathbb{P}^1$ to the sextic
6. **Moduli dimension verification**: Confirmation that this configuration lies in the
   9-dimensional component of the moduli space

## Parent Sufficiency Map

Provides the literature-anchored target for the explicit sextic task; does not verify it
by itself.

## Deliverable Type

fixture data

## Current Dependencies

- Prerequisite tasks: none
- Local sources:
  - **GOAL.md** (primary): Mathematical specifications in lines 8-13 define the nodal
    conditions for constructing the sextic.
    These specifications are the canonical source for fixture construction.
  - **REFERENCES.md**: For verification purposes only; fixture construction uses
    computational methods from GOAL.md specs, not direct paper extraction.
  - theory/literature_claim_map.md — literature claims for verification
  - theory/mathematical_background.md — background on nodal conditions

## Acceptance Criteria

1. **Point count verification**: The fixture must contain exactly 10 distinct points in
   $\mathbb{P}^2$
2. **Nodal condition verification**: Each point must satisfy $F(p) = \frac{\partial
   F}{\partial x}(p) = \frac{\partial F}{\partial y}(p) = \frac{\partial F}{\partial
   z}(p) = 0$ for the provided sextic coefficients
3. **A1 singularity verification**: The Hessian at each point must be non-zero (ensuring
   $A_1$ not worse singularity)
4. **Rationality verification**: The sextic curve must be irreducible (geometric genus
   0\) as required for Coble surfaces
5. **K3 cover verification**: The double cover must have exactly 10 $A_1$ singularities
   (no extra singularities from non-smooth branch)
6. **Moduli dimension**: The configuration must correspond to the 9-dimensional
   component, not a proper subvariety
7. **Serialization roundtrip**: All fixture data must survive JSON
   serialization/deserialization correctly

## Non-Goals

1. **No algorithmic sextic search**: This task provides pre-computed fixtures;
   algorithmic construction is T-3001
2. **No proof of rationality**: Assumes the fixture from literature is rational;
   verification is T-0007
3. **No full moduli computation**: Only provides one canonical example; full moduli is
   beyond scope
4. **No automorphism computation**: The fixture provides the sextic; automorphisms are
   separate
5. **No deformation family**: Only provides the canonical fixture; family enumeration is
   separate

## Allowed Dependencies

- **Prerequisite tasks**: none (this is T-1 foundation)
- **Local sources** (for verification, not primary construction):
  - GOAL.md lines 8-13 — primary source for nodal condition specifications
  - REFERENCES.md — verification of sextic properties
  - theory/literature_claim_map.md — verification claims
  - theory/mathematical_background.md — background on nodal conditions

## Required Conventions

1. **Point representation**: Points in $\mathbb{P}^2$ are represented as homogeneous
   coordinates $[x:y:z]$ with rational or algebraic number coordinates
2. **Sextic coefficient ordering**: Use lexicographic ordering on monomials $x^i y^j
   z^k$ with $i+j+k=6$
3. **Singularity classification**: Use $A_1$ to mean a double point with non-vanishing
   Hessian (ordinary double point)
4. **K3 cover convention**: The weighted projective space is $\mathbb{P}(1,1,1,3)$ with
   coordinates $[x:y:z:w]$
5. **Fixture format**: JSON with keys `points`, `sextic_coefficients`, `k3_cover`,
   `parametrization` (if available)

## Failure Conditions

1. **Duplicate points**: If any two points in the configuration coincide, the fixture is
   rejected
2. **Non-nodal singularity**: If any point has a singularity worse than $A_1$ (higher
   Milnor number), the fixture is rejected
3. **Non-rational sextic**: If the sextic has higher geometric genus, it does not yield
   a Coble surface
4. **Extra K3 singularities**: If the double cover has singularities beyond the 10
   nodes, the fixture is rejected
5. **Coefficient overflow**: If coefficients are not in $\mathbb{Q}$ or a documented
   number field, the fixture is rejected
