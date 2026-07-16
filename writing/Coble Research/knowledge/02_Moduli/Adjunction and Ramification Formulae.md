---
title: Adjunction and Ramification Formulae
tags:
  - subject/algebraic-geometry
  - type/formula
aliases:
  - adjunction formula
  - ramification formula
created: 2026-05-10
---

> [!formula] Adjunction and Ramification Formulae
> Two formulas used repeatedly in the Coble-surface constructions are the blowup formula for canonical classes and the ramification formula for branched covers.

## Blowups

Let
$$
f \colon Y = \operatorname{Bl}_V X \to X
$$
be the blowup of a smooth variety $X$ along a smooth center $V$, with exceptional divisor $E$.
Then
$$
K_Y = f^*K_X + (\operatorname{codim}_X V - 1)E.
$$

For the blowup of a smooth surface at a point, this specializes to
$$
K_Y = f^*K_X + E.
$$

## Branched covers

Let
$$
f \colon Y \to X
$$
be a branched cover with branch locus $B$ and ramification divisor $R$.
Then
$$
K_Y = f^*K_X + R.
$$

In the Coble/K3 setup, this is used with a double cover branched along a divisor in $|-2K_X|$, so that
$$
K_Y = f^*(K_X + L)
$$
for the line bundle $L$ with $2L \sim B$.
