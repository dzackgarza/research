---
title: Lattice Morphisms and Embeddings
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - lattice morphism
  - lattice embedding
  - primitive embedding
  - isometry
  - orthogonal group
created: 2026-05-08
---

> [!definition] Lattice Morphisms and Embeddings A **morphism** between [[Lattice|lattices]] $(L_1, \beta_1)$ and $(L_2, \beta_2)$ is a morphism of $\mathbf{Z}$-modules $f: L_1 \to L_2$ that preserves the bilinear form: $\beta_1(v,w) = \beta_2(f(v), f(w))$ for all $v,w \in L_1$.
> We write $\operatorname{Lat}$ for the category of integral lattices.
> 
> An **embedding** is an injective morphism.
> An embedding is **primitive** if its cokernel, $\operatorname{coker}(f)$, is a torsion-free $\mathbf{Z}$-module.
> 
> An **isometry** is a morphism of lattices that is also an isomorphism of $\mathbf{Z}-modules.
> Two lattices $L_1, L_2$ are **isometric**, written $L_1 \xrightarrow{\sim} L_2$, if an isometry exists between them.
> 
> The **orthogonal group** of a lattice $L$ is its group of self-isometries $\operatorname{O}(L) \mathrel{\mathop:}= \operatorname{Aut}*{\operatorname{Lat}}(L)$.
> In terms of a [[Gram Matrix|Gram matrix]] $G*\beta$, the orthogonal group has the characterization: $$ \operatorname{O}(L) = \{M \in \operatorname{GL}*n(\mathbf{Z}) \mathrel{\Big|} M G*\beta M^t = G_\beta\} $$
