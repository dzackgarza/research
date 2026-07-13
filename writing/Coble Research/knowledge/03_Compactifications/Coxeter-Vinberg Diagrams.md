---
title: Coxeter-Vinberg Diagrams
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - type/definition
aliases:
  - Coxeter-Vinberg Diagram
created: 2026-05-08
---

> [!definition] Coxeter-Vinberg Diagrams The **Coxeter diagram** of a hyperbolic Coxeter polytope is a graph whose vertices correspond to simple roots $r_i$ and edges encode the angle between mirrors $H_i, H_j$ via: $$ g_{i,j} \mathrel{\mathop:}= \frac{r_i \cdot r_j}{\sqrt{r_i^2 r_j^2}} = \cos\left(\frac{\pi}{m_{ij}}\right) $$
> 
> Edges are drawn as:
> - Omitted if $m_{ij} \leq 2$.
> - Multiple lines if $3 \leq m_{ij} < \infty$ ($H_i \cap H_j$ in interior).
> - Thick/bold if $g_{ij} = 1$ ($H_i \cap H_j$ on boundary).
> - Dotted if $g_{ij} > 1$ (ultra-parallel).
> 
> For 2-elementary lattices, vertices are white for $v^2=-2$ and black for $v^2=-4$.
