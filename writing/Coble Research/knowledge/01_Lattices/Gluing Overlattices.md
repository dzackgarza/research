---
title: Gluing Overlattices
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/proposition
aliases:
  - Gluing Overlattices
created: 2026-05-08
---

> [!proposition] Gluing Overlattices via Isotropic Subgroups
> 
> Let $S$ be a lattice.
> There is a bijection between even [[Overlattices and Gluing Theory|overlattices]] $L$ of $S$ and isotropic subgroups $H \leq A_S$:
> \begin{align*}
> \{\text{Even overlattices } L \text{ of } S\} &\rightleftharpoons \{\text{Isotropic subgroups } H \leq A_S\} \\
> L &\mapsto H_L \mathrel{\mathop:}= L / S \\
> L \mathrel{\mathop:}= \eta^{-1}(H) \subseteq S^{\vee} &\mathrel{\reflectbox{\ensuremath{\mapsto}}} H
> \end{align*}

A primitive embedding $S \hookrightarrow L$ with $T \mathrel{\mathop:}= S^{\perp L}$ is determined by the embedding subgroup $H \leq A_L$ and an embedding isometry $\gamma: H \xrightarrow{\sim} H' \subseteq A_S$.
We have the discriminant formula: $$ |\operatorname{disc} T| = \frac{|\operatorname{disc} L| \cdot |\operatorname{disc} S|}{(\sharp H)^2} $$
