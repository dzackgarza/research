---
title: 2-Elementary Lattices
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - 2-elementary lattice
  - co-even
  - co-odd
  - coparity
created: 2026-05-08
---

> [!definition] 2-Elementary Lattices A 2-elementary [[Lattice]] is a lattice whose discriminant group is a 2-elementary abelian group.
> The exponent $a = \operatorname{rank}_{\mathbf{F}_2} A_L$ is the **2-rank** of the discriminant group.
> 
> Let $L^\dagger \mathrel{\mathop:}= L^{\vee}(2)$.
> We say $L$ is **co-even** if $L^\dagger$ is even and define the invariant $\delta = 0$, and **co-odd** otherwise and set $\delta = 1$.
> Equivalently, the **coparity** is defined as
> $$
> \delta(L) \mathrel{\mathop:}= \begin{cases}
> 0 & \text{ if } q_{A_L}(x) \in \mathbf{Z} \,\,\forall\,\, x \in A_L \\
> 1 & \text{ otherwise }
> \end{cases}
> $$

## Classification

Let $L$ be an even, indefinite, 2-elementary lattice with $\operatorname{rank}(L) \geq 4$.
The classification of such lattices is determined by three invariants:
1. the rank $r = \operatorname{rank}_{\mathbf{Z}}(L)$,
2. the 2-rank $a = \dim_{\mathbf{F}_2}(A_L)$, or equivalently $\ell(L)$, and
3. the coparity $\delta \in \{0,1\}$.

We denote by $(r, a, \delta)*{n*+}$ the 2-elementary lattice with these invariants and signature $(n_+, n_-)$.
For each admissible triple $(r, a, \delta)$ satisfying $r \geq 4$, there exists a unique isometry class of even, indefinite, 2-elementary lattice with these invariants (Nikulin 1980).
