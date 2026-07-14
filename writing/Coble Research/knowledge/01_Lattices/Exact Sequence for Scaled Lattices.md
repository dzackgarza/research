---
title: Exact Sequence for Scaled Lattices
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/proposition
aliases:
  - Exact Sequence for Scaled Lattices
  - stable orthogonal group
created: 2026-05-08
---

> [!proposition] Exact Sequence for Scaled Lattices
> For any [[Lattice]] $L$ and positive integer $m$, there is a short exact sequence:
> $$ 0 \to L/mL \hookrightarrow A_{L(m)} \to A_L \to 0 $$
> If $L$ is unimodular, this implies $A_{L(m)} \cong L/mL$. 
> 
> Similarly, by functoriality, any isometry $f \in \operatorname{O}(L)$ lifts to an isometry of $L^{\vee}$ and thus induces an isometry on the discriminant group $A_L$. This defines a group homomorphism $\psi: \operatorname{O}(L) \to \operatorname{O}(A_L)$, which fits into an exact sequence:
> $$ 0 \to \operatorname{O}^*(L) \to \operatorname{O}(L) \xrightarrow{\psi} \operatorname{O}(A_L) \to \operatorname{O}^*(A_L) \to 0 $$
> where $\operatorname{O}^*(L) \mathrel{\mathop:}= \ker(\psi)$ and $\operatorname{O}^*(A_L) \mathrel{\mathop:}= \operatorname{coker}(\psi)$ are the **stable orthogonal groups** of $L$ and $A_L$.


## Details
- The cokernel $\operatorname{O}^*(A_L)$ measures the obstruction to lifting isometries from the discriminant form $A_L$ to the lattice $L$. 
- The homomorphism $\psi$ is surjective (i.e., $\operatorname{O}^*(A_L) = 0$) when $L$ is indefinite and satisfies $\ell(A_L) + 2 \leq \operatorname{rank}(L)$, where $\ell(A_L)$ is the minimal number of generators of $A_L$. 
- For unimodular lattices like $U$ and $E_8$, the discriminant group is trivial, so $\operatorname{O}^*(L) = \operatorname{O}(L)$.
