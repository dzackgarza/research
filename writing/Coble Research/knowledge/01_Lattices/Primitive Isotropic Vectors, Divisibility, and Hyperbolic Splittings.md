---
title: Primitive Isotropic Vectors, Divisibility, and Hyperbolic Splittings
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/proposition
aliases:
  - Primitive Isotropic Vectors, Divisibility, and Hyperbolic Splittings
  - orthogonal complement
created: 2026-05-08
---

> [!proposition] Primitive Isotropic Vectors, Divisibility, and Hyperbolic Splittings
> Let $S$ be any unimodular [[Lattice]] admitting a primitive embedding into a nondegenerate lattice $L$. Then $L \cong S \oplus T$ where 
> $$ T\mathrel{\mathop:}= S^{\perp} = \{v\in L \mathrel{\Big|} \beta(v, S) = 0\} $$ 
> is the **orthogonal complement** of $S$ in $L$.
> 
> Moreover, if $S$ is unimodular, then so is $T$.


## Proof Idea
We can write $\operatorname{disc}(S) = [S\oplus T: L]\cdot c_S$ for some $c_S\in \mathbf{Z}$. By unimodularity, $\operatorname{disc}(S) = \pm 1$ forces $c_S = \pm 1$ and $[S\oplus T: L] = 1$, yielding the first claim. For the second, we note that $\operatorname{disc}(S\oplus T) = \operatorname{disc}(S) \cdot \operatorname{disc}(T)$, forcing $\operatorname{disc}(T) = \pm 1$.
