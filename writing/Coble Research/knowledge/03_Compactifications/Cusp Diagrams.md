---
title: Cusp Diagrams
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - type/definition
aliases:
  - cusp diagram
  - 0-cusp
  - 1-cusp
created: 2026-05-08
---

> [!definition] Cusp Diagrams
>
> Let $X$ be a complex analytic space equipped with a stratification $\partial X = \bigsqcup_{i \geq 0} \partial_i X$ by boundary strata indexed by codimension.
> 
> The **cusp diagram** of $X$ is the directed graph whose vertices index the irreducible components of $\partial_i X$, with a directed edge $e_{i \to j}$ corresponding to components $V_i$ and $V_j$ whenever $V_j$ lies in the Zariski closure of $V_i$.

For Baily-Borel compactifications $\overline{F_\Gamma}^{\operatorname{BB}}$, **0-cusps** correspond to $\Gamma$-orbits of isotropic lines $I \subset L$, and **1-cusps** correspond to orbits of isotropic planes $J \subset L$.
1-cusps adjacent to a 0-cusp $[I]$ correspond to maximal parabolic subdiagrams of the Coxeter diagram for the reflection group of $M \mathrel{\mathop:}= I^\perp / I$.

For the polarized Coble program, the boundary objects are a marked refinement of this picture: one tracks pairs $(I,r)$ and $(J,r)$ rather than plain isotropic data, and one must separate established reduction mechanisms from still-open cusp counts; see [[Cusp data for polarized Coble moduli]].
