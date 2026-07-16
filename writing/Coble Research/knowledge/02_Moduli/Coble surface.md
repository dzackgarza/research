---
title: Coble surface
tags:
  - subject/algebraic-geometry
  - surface/coble
  - type/definition
aliases:
  - Coble surface
  - terminal Coble surface
created: 2026-05-08
---

> [!definition] Coble surface
> A **Coble surface** is a smooth rational projective surface with an empty anti-canonical linear system $|-K| = \varnothing$, but a non-empty anti-bicanonical system $|-2K| \neq \varnothing$ [@DM19; @DK24].

## Terminal Coble surfaces of K3 type

- A terminal Coble surface of K3 type is a Coble surface for which $|-2K_S|$ contains a reduced divisor $C = C_1 + \cdots + C_n$ of disjoint smooth rational curves with $C_i^2 = -4$ [@DM19; @DK24].

- The curves $C_i$ are the **boundary components**.

- One has
  $$
  n = -K_S^2, \qquad n \le 10.
  $$

- In the case $n=1$, the anti-bicanonical divisor is a single smooth rational curve $C$ with
  $$
  C^2 = -4.
  $$
  [@DK24; @CDL24]

## Classical construction

- Such a surface is a basic rational surface: it admits a birational morphism to $\mathbf{P}^2$ obtained by blowing up $N = 9+n$ points [@DK24].

- For $n=1$, one gets the classical Coble surface by blowing up the ten $A_1$-singularities of an irreducible rational plane sextic, the historical example studied in [@Cob19] and [@Oda85] and later classified in [@DZ99].

- Conversely, the proper transform of such a sextic lies in $|-2K_S|$, so the blowup produces a terminal Coble surface of K3 type [@AS15; @CDL24].

- A terminal Coble surface is **minimal** if blowing down any $(-1)$-curve destroys the Coble property [@DZ99].

## Quartic del Pezzo model

- Following [@Dol12, §5.1], one can degenerate a fixed-point-free involution on a K3 surface to an involution whose fixed locus is a smooth rational curve; the quotient is then a Coble surface.

- For an isotropic sequence $(f_i)$ in a modified basis $e_0,\dots,e_{10}$ of $K_S^{\perp \operatorname{Num}(S)} \cong E_{10}$, the linear system $|2f_i+2f_j|$ defines a degree-2 map
  $$
  \phi_{ij}\colon S \to D
  $$
  to a quartic del Pezzo surface with four $A_1$-singularities [@Dol12].

- In the Coble case this map is never finite, and its deck transformation is a biregular automorphism of $S$ [@Dol12].

## Related geometric classes

- Unnodal Coble surfaces are the Coble analog of unnodal Halphen surfaces in the theory of Cremona-special point configurations [@CD12].

- Every terminal Coble surface of K3 type is closely related to both a [[K3 covers of Coble surfaces|K3 double cover]] and an [[Halphen surfaces and Coble surfaces|index-2 Halphen surface]] [@DK24; @CD12].
