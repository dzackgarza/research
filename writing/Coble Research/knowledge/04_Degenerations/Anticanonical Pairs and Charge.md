---
title: Anticanonical Pairs and Charge
tags:
  - subject/algebraic-geometry
  - type/definition
aliases:
  - Anticanonical pair
  - log Calabi-Yau surface
  - Charge of an anticanonical pair
  - Friedman-Morrison Charge Theorem
created: 2026-05-08
---

> [!definition] Anticanonical Pairs and Charge
> An **anticanonical pair** $(V, D)$ consists of a smooth projective rational surface $V$ and a reduced effective snc divisor $D$ such that $K_V + D \sim_{\mathbf{Q}} 0$.
> Also known as log Calabi-Yau surfaces.
> 
> The **charge** of an anticanonical pair measures its deviation from being toric: $$ Q(V, D) := 12 - \sum_j (D_j^2 + 3) $$ For toric surfaces, $Q(V, \partial V) = 0$.
> 
> **Corner blowups** (at nodes of $D$) preserve charge.
> **Interior blowups** (at smooth points of $D$) increase charge by 1.

> [!theorem] Friedman-Morrison Charge Theorem
> For a Type III Kulikov degeneration of K3 surfaces with central fiber ${\mathcal{X}}_0 = \bigcup_{i=1}^n V_i$, let $D_i = V_i \cap \overline{({\mathcal{X}}_0 \setminus V_i)}$.
> Then the sum of the charges of all components is exactly 24: $$ \sum_{i=1}^n Q(V_i, D_i) = 24 $$ This imposes severe constraints on the possible combinatorial types of degenerations.
