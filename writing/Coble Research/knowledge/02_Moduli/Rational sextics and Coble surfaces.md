---
title: Rational sextics and Coble surfaces
tags:
  - subject/algebraic-geometry
  - surface/coble
  - type/lemma
aliases:
  - rational sextic with ten A1 singularities
  - Severi sextics for Coble surfaces
created: 2026-05-10
---

> [!lemma] Rational sextic criterion for the classical Coble construction
> Let $C \subset \mathbf{P}^2$ be an irreducible sextic curve with at worst $A_1$-singularities. Then $C$ is rational if and only if it has exactly ten $A_1$-singularities [@Cob19].

## Proof idea

- The genus-degree formula gives
  $$
  g(C) = \frac{(6-1)(6-2)}{2} - \sum_p \delta_p = 10 - k
  $$
  when all singularities are nodes, since each $A_1$ contributes $\delta_p = 1$.
- Hence $g(C)=0$ exactly when $k=10$.

## Coble consequence

If $S$ is the blowup of the ten nodes of such a sextic and $B$ is the proper transform, then
$$
B \sim -2K_S, \qquad K_S^2 = 9 - 10 = -1,
$$
so $S$ is a terminal Coble surface of K3 type [@AS15; @CDL24].

## Severi-variety caveat

- The locus of plane sextics with ten nodes forms the Severi variety $V_{6,10}$ [@BHO+11].
- Rational sextics need not always have ten nodes: more degenerate singularity types can occur provided the total $\delta$-invariant remains 10 [@GK20].
- The classical Coble construction uses the generic Severi stratum of sextics with exactly ten $A_1$-singularities [@Cob19].
