---
title: Symmetric Bilinear Form
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - bilinear form
  - symmetric bilinear form
created: 2026-05-08
---

> [!definition] Symmetric Bilinear Form
> Let $L$ be a $\mathbf{Z}$-module. A **bilinear form** $\beta$ on $L$ is a morphism $\beta: L \otimes_{\mathbf{Z}} L \to \mathbf{Q}$. We often write $v \cdot w$ or $vw$ for $\beta(v,w)$.
> 
> A bilinear form $\beta$ is:
> - **$\varepsilon$-symmetric** for $\varepsilon \in \mathbf{Q}$ if $\beta(a,b) = \varepsilon \cdot \beta(b,a)$.
> - **Symmetric** if $\varepsilon = 1$.
> - **Skew-symmetric** if $\varepsilon = -1$.
> - **Alternating** if $\beta(a,a) = 0$ for all $a \in L$.
> - **Integral** if its image $\beta(L,L)$ is contained in $\mathbf{Z}$.
> - **Nondegenerate** if the map $L\to \operatorname{Hom}_{\mathbf{Z}}(L, \mathbf{Z})$ given by $v\mapsto \beta(v, \cdot)$ is injective.

