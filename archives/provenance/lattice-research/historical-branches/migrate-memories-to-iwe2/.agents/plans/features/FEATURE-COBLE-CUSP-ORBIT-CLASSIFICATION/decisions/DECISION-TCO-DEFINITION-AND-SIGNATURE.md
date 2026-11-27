---
id: DECISION-TCO-DEFINITION-AND-SIGNATURE
trackerStatus:
  type: decision
parents:
- '[[FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION]]'
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
title: Decide Coble algebraic and transcendental lattice notation
status: decided
chosen: T_Co is the K3 orthogonal complement of S_Co
tags:
- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
---
# Decision: Coble algebraic and transcendental lattice notation

## Decision

Use three distinct lattice names, and do not conflate them:

| Symbol | Definition | Signature | Rank |
|--------|-----------|-----------|------|
| `Pic(S)` | Picard lattice of the blowup Coble surface before K3 pullback | (1, 10) | 11 |
| `K_S^perp` | Enriques-type numerical sublattice inside `Pic(S)`; Dolgachev-Kondo identify it with `E_10` | (1, 9) | 10 |
| `S_Co` | Algebraic K3 pullback lattice `f^*Pic(S)` inside `Lambda_K3`; primary notation `I_{1,10}(2)` | (1, 10) | 11 |
| `T_Co` | Orthogonal complement `S_Co^perp` in `Lambda_K3`; Dolgachev-Kondo call this `N` | (2, 9) | 11 |
| `T_En` | Enriques period lattice `U + E_10(2)` in the Dolgachev-Kondo comparison | (2, 10) | 12 |

Concretely:

- `Pic(S)` is the unimodular odd lattice `I_{1,10}` with the geometric line and
  exceptional divisor basis.
- In the blowup basis, `K_S = -3H + sum_i E_i`. Hence
  `D = aH + sum_i c_i E_i` belongs to `K_S^perp` iff
  `D.K_S = -3a - sum_i c_i = 0`; equivalently, if
  `D = aH - sum_i b_i E_i`, then `sum_i b_i = 3a`.
- The K3 cover doubles intersections, so the algebraic pullback lattice is
  `S_Co = f^*Pic(S) = I_{1,10}(2)`. The diagonal spelling
  `<2> + <-2>^10` is a presentation of that family member, not the primary name.
- The period/transcendental lattice used for Coble cusp orbit work is
  `T_Co = S_Co^perp` in `Lambda_K3`. It has discriminant form `q_T = -q_S` and
  is the type-IV lattice `N = <2> + E_10(2)`. With the convention
  `E_10 = U + E_8(-1)`, this is `<2> + U(2) + E_8(-2)`.
- `T_Co` is not `I_{1,10}(2)`. That notation belongs to `S_Co`.

## Polarization Normalization

Use separate names for the plane-blowup class and the degree-2 Coble polarization:

| Symbol | Parent | Square | Meaning |
|--------|--------|--------|---------|
| `H` | `Pic(S)` | 1 | Pullback of the plane hyperplane class in the ten-node blowup model |
| `f^*H` / `e_0` | `S_Co` | 2 | K3 pullback of the plane-line class; part of the `I_{1,10}(2)` construction basis |
| `h_Co` | `K_S^perp subset Pic(S)` | 2 | Degree-2 Enriques-type Coble polarization, non-degenerately `F_1 + F_2` |
| `tilde h_Co = f^*h_Co` | `f^*(K_S^perp) subset S_Co` | 4 | K3-side polarization vector used when comparing with K3-cover conventions |

For unnodal Coble surfaces, Dolgachev-Kondo use
`K_S^perp subset Pic(S) ~= E_10` and choose the same degree-2 polarization pattern as
for Enriques surfaces: `h_Co = F_1 + F_2`, with `F_i^2 = 0` and `F_1.F_2 = 1`.
Thus `h_Co.K_S = 0`, equivalently `h_Co` has degree zero on the Coble boundary
`C in |-2K_S|`. In the explicit blowup coordinates above this imposes
`sum_i b_i = 3a` for any expression `h_Co = aH - sum_i b_i E_i`. The K3 pullback
doubles the square, so `tilde h_Co^2 = 4`.

## Task Routing

- Tasks 2.1--2.2 use the discriminant form of `T_Co`.
- Task 3.2 uses primitive isotropic planes in `T_Co`.
- Task 4.1 uses the Coxeter/root data of the algebraic lattice `S_Co`.
- Arithmetic-group and stable-model cards use `h_Co` for the downstairs degree-2
  polarization in `K_S^perp`, and `tilde h_Co` for its K3 pullback in `S_Co`.
  When relating the Coble quotient to the Enriques period lattice, they must introduce
  the corresponding typed Heegner vector, K3 pullback, or embedding data explicitly.
  Dolgachev-Kondo identify `T_Co` with the orthogonal complement of a `(-2)` vector in
  `T_En = U + E_10(2)`.

## Sources

- `GOAL.md`: Picard lattice, K3 pullback lattice, orthogonal-complement lattice, and
  Task 2 input contract.
- `theory/references/literature/dolgachev_kondo_2013.md`: the K3 pullback lattice
  `M`, written here as `I_{1,10}(2)`, its complement `N`, the identification
  `N=<2>+E_10(2)`, and the degree-2 Coble polarization in `K_S^perp`.
- `theory/references/literature/aegs_2023.md`: K3-side degree-2 Enriques convention
  `h=e+f in U(2)`.
- `theory/foundations/coble-task-background.md`: task-local operational summary,
  updated to use this notation.
