---
title: Divisibility of Isotropic Vectors in Unimodular Lattices
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/lemma
aliases:
  - Divisibility of Isotropic Vectors in Unimodular Lattices
created: 2026-05-08
---

> [!lemma] Divisibility of Isotropic Vectors in Unimodular Lattices
> Let $L$ be a nondegenerate unimodular [[Lattice]], and let $v \in L$ be a primitive [[Isotropic Submodules and Vectors|isotropic vector]]. Then there exists $w \in L$ such that $(v, w) = 1$.
> In particular, $\operatorname{div}_L(v) = 1$ for all $v\in L$.

## Proof Idea

Since $L$ is unimodular, $L \xrightarrow{\sim} L^{\vee}$.
The linear form $x \mapsto (v, x)$ is a nonzero element of $\operatorname{Hom}(L, \mathbf{Z})$, and is surjective because $v$ is primitive and $L$ is unimodular.
Hence there exists $w \in L$ with $(v, w) = 1$.
