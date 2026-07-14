---
title: Mirror Moves
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - mirror move
created: 2026-05-08
---

> [!definition] Mirror Moves A **mirror move** is a lattice-theoretic operation governed by the existence of a primitive isotropic vector $\eta \in T$ of a specified type and splitting:
> - **Odd/simple:** $\operatorname{div}_T(\eta) = 1$, splitting as $T \cong U \oplus K$.
>   The new invariants are $(r-2, a, 1)$.
> - **Even, ordinary:** $\operatorname{div}_T(\eta) = 2$ and $\eta^*$ is ordinary, splitting as $T \cong U(2) \oplus K$.
>   The new invariants are $(r-2, a-2, 1)$.
> - **Even, characteristic:** $\operatorname{div}_T(\eta) = 2$ and $\eta^*$ is characteristic, splitting as $T \cong I_{1,1}(2) \oplus K$.
>   The new invariants are $(r-2, a-2, 0)$.
> 
> The move replaces $T$ with $\overline{T}_\eta = \eta^{\perp T}/\eta$, navigating Nikulin's pyramid of 2-elementary lattices to compute cusp diagrams when $\Gamma = \operatorname{O}^+(T)$.
