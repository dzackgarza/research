---
title: Quadratic Form
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - quadratic form
  - polar form
created: 2026-05-08
---

> [!definition] Quadratic Form and Associated Bilinear Form A **quadratic form** on a $\mathbf{Z}$-module $L$ is a map of sets $q: L \to \mathbf{Q}$ such that $q(\lambda v) = \lambda^2 q(v)$ for all $v \in L, \lambda \in \mathbf{Q}$, and such that its **polar form** $\beta_q$ is a symmetric bilinear form on $L$:
> $$
> \begin{aligned}
> \beta_q: L \otimes_{\mathbf{Z}} L &\to \mathbf{Q} \\
> (v,w) &\mapsto \beta_q(v,w) \mathrel{\mathop:}= q(v+w) - q(v) - q(w)
> \end{aligned}
> $$
> 
> We say $q$ is **integral** if $q(L) \subseteq \mathbf{Z}$.
> The pair $(L,q)$ is called a **quadratic $\mathbf{Z}$-module**.

## See Also

- [[Correspondence between Bilinear and Quadratic Forms]]
