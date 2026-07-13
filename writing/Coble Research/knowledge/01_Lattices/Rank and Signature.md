---
title: Rank and Signature
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - positive definite
  - negative definite
  - indefinite
  - signature
  - hyperbolic lattice
created: 2026-05-08
---

> [!definition] Rank and Signature Let $(L, \beta)$ be a nondegenerate [[Lattice]]. We say it is:
> - **positive definite** if $\beta(v,v) > 0$ for all nonzero $v \in L$.
> - **positive semidefinite** if $\beta(v,v) \geq 0$ for all $v \in L$.
> - **negative definite** if $\beta(v,v) < 0$ for all nonzero $v \in L$.
> - **negative semidefinite** if $\beta(v,v) \leq 0$ for all $v \in L$.
> - **indefinite** if it is neither positive nor negative semidefinite.
> 
> Letting $(L_{\mathbf{R}}, \beta_{\mathbf{R}})$ be the extension of $L$ to $\mathbf{R}$, the diagonalization of the [[Gram Matrix|Gram matrix]] has $p$ positive terms and $q$ negative terms.
> We define:
> - The **rank** of $L$ is $\operatorname{rank}(L) = p + q$.
> - The **signature** of $L$ is $\operatorname{sig}(L) = (p,q)$.
> - The **index** of $L$ is $\tau(L) = p - q$.

## Properties

- $L$ is positive-definite if $q=0$, negative-definite if $p=0$, and indefinite if both $p,q > 0$.
- We say $L$ is **hyperbolic** if its signature is $(1, n-1)$ or $(n-1, 1)$.
