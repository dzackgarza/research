# Task T-0007: Exact Nodal-Sextic Primitives

## Status

Selected in Wave A. TASK_SPECIFICATION complete as of 2026-04-02.

## Tier

Tier 0.

## Origin

- GOAL.md source: lines 8-13 describe Coble surface construction from nodal sextic
- GOAL.md line 25: "Derive an explicit equation F(x,y,z)=0 for a rational sextic with 10
  nodes and the corresponding K3 surface w² = F"
- GOAL.md line 109-111: sextic construction from P¹ map, K3 cover with A₁ singularities
- GOAL.md Task 1.1: explicit equation for sextic and K3 cover

## Objective

Expose exact nodal-sextic primitives:
- linear_system(points, degree=6) → homogeneous polynomial coefficients
- check_A1_singularities(F, points) → Boolean list (one per point)
- is_rational_curve(F) → Boolean (sextic is rational via genus computation)
- is_birational_to_P2(F) → Boolean (map degree matches)
- k3_cover_equation(F) → homogeneous polynomial in P(1,1,1,3) coordinates
- nodal_profile(F, points) → list of singularity types at each point

## Deliverable Type

shared tool — reusable primitives with explicit contracts.

## Acceptance Criteria

1. **Linear system**: Given 10 point configuration, produce coefficient vector for
   sextic with prescribed nodal conditions (value and first derivatives vanish at each
   point)

2. **A₁ singularity check**: For each of 10 points, verify the Hessian matrix at that
   point has rank 0 (double point with ordinary tangents)

3. **Rationality check**: Compute genus of plane curve {F=0} via arithmetic genus
   formula; genus=0 confirms rationality

4. **Birationality**: Verify the degree of the rational map P¹ → P² is 6 and map is
   injective on open set

5. **K3 cover**: Given F(x,y,z), produce G(x,y,z,w) = w² - F(x,y,z) in weighted
   coordinates

6. **Nodal profile**: Verify all 10 points are ordinary double points (A₁
   singularities), not higher multiplicities

7. **Import test**: All functions importable from coble_geometry_foundation

## Non-Goals

- Does not prove existence of sextic for arbitrary point configurations (theorem claim)
- Does not compute moduli space or classify all sextics (GOAL.md Task 1.1 is one
  example)
- Does not compute automorphism group of sextic (T-0004 territory)
- Does not compute Picard group of K3 cover (beyond singularity profile)
- Does not implement all possible sextic constructions (Steiner, Halphen) — just
  primitives

## Allowed Dependencies

- Prerequisite tasks: none (this is independent primitive construction)
- Local sources:
  - theory/literature_claim_map.md (which constructions are canonical)
  - theory/mathematical_background.md (singularity theory)
  - REFERENCES.md (Dolgachev-Kondyrev, Steiner sextic refs)

## Required Conventions

- Function naming: `<operation>_sextic()` or `<operation>_k3()`
- Polynomial representation: homogeneous polynomial in x,y,z via PolynomialRing
- Points represented as [x:y:z] in projective coordinates
- K3 cover uses weighted projective space P(1,1,1,3) with coordinate w

## Failure Conditions

1. If linear system produces coefficients that don't satisfy nodal conditions → fail
2. If A₁ check misidentifies singularity type → fail
3. If rationality check gives wrong genus → fail
4. If K3 cover equation is not degree 6 in x,y,z and degree 2 in w → fail
5. If nodal profile returns wrong types for known nodal sextic → fail
6. If any function raises exception on valid input → fail

## Parent Sufficiency Map

Supplies sextic infrastructure for:
- T-2006: gates sextic primitives using T-1007 fixture
- T-3001: produces the explicit sextic and K3 cover example
- T-3012: maps polarization to surgery vector

Discharges no GOAL.md burden by itself (provides tool, not proof).
