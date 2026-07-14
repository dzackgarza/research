---
title: Coxeter Groups and Polytopes
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - Coxeter group
  - Coxeter polytope
created: 2026-05-08
---

> [!definition] Coxeter Groups and Polytopes A **Coxeter group** is a group $S$ with presentation $$ S = \left\langle s_1,\cdots, s_n \mathrel{\Big|} s_i^2 = (s_i s_j)^{m_{ij}} = e \right\rangle $$ where $m_{ii} = 1$ and $m_{ij} = m_{ji} \geq 2$ for $i\neq j$.
> 
> A **Coxeter polytope** $P$ in $X = \mathbb{E}^n, S^n$, or $\mathbb{H}^n$ is a polytope such that:
> 1. Each face lies in a hyperplane $H_i \mathrel{\mathop:}= \alpha_i^\perp$.
> 2. Dihedral angles between adjacent faces are $\pi/m_{ij}$ for integers $m_{ij}\geq 1$.
> 3. The reflection group $W = \langle s_{\alpha_i} \rangle$ acts properly discontinuously on $X$ with fundamental domain $P$.
