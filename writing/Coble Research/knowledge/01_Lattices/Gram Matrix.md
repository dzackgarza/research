---
title: Gram Matrix
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - Gram matrix
  - unimodular
  - discriminant
created: 2026-05-08
---

> [!definition] Gram Matrix
> Given a basis $B_L = (e_i)_{1 \leq i \leq n}$ for a bilinear module $(L,\beta)$, the **Gram matrix** of $\beta$ is $G_\beta \mathrel{\mathop:}= (\beta(e_i, e_j))_{i,j} \in \operatorname{Mat}_{n \times n}(\mathbf{Q})$.
> 
> For vectors $v = \sum a_j e_j$ and $w = \sum b_j e_j$, we have $\beta(v,w) = v^t G_\beta w$. Similarly, for a quadratic module $(L,q)$, a **Gram matrix** $G_q$ is any matrix such that $q(v) = v^t G_q v$.


## Properties
- We define the **discriminant** $\operatorname{disc}(L)$ of $L$ as $\operatorname{det}(G_\beta)$ in any choice of basis.
- For any sublattice $S \leq L$, we have the formula $\operatorname{disc}(S) = [L:S]^2 \operatorname{disc}(L)$, so the discriminant typically _increases_ when passing to a sublattice.
- We say $L$ is **unimodular** if $\operatorname{disc}(L) = \pm 1$.
- The Gram matrix reflects properties of the form: $\beta$ is symmetric iff $G_\beta^t = G_\beta$, skew-symmetric iff $G_\beta^t = -G_\beta$, and an integral [[Lattice]] is even iff $G_\beta$ is an integer matrix with diagonal entries in $2\mathbf{Z}$.
