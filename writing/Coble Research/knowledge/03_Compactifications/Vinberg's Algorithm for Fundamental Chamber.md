---
title: Vinberg's Algorithm for Fundamental Chamber
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/theorem
aliases:
  - Vinberg's Algorithm
created: 2026-05-08
---

> [!theorem] Vinberg's Algorithm for Fundamental Chamber
> For an arithmetic reflection subgroup $\Gamma \subset \operatorname{O}(L)$, Vinberg's algorithm constructs a fundamental chamber $P \subset \mathbb{H}^n$:
> 1. **Control vector**: Choose generic positive-norm $v_0 \in C_L^+$.
> 2. **Enumerating roots**: Find primitive $v \in L$ with $v^2 < 0$, $s_v \in \Gamma$, and $H_v$ intersecting the current cone $\tilde P$.
> 3. **Ordering/pruning**: Order roots by height $h(v) \mathrel{\mathop:}= -2(v_0 \cdot v)/v^2$.
>    Discard those whose hyperplanes do not intersect $\tilde P$ transversely.
> 4. **Constructing the diagram**: When $\tilde P$ becomes a convex polytope, the Gram matrix determines the Coxeter diagram.
> 
> The algorithm terminates if and only if $\Gamma$ has finite covolume.
