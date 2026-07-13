---
title: Coble lattice
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - surface/coble
  - type/example
aliases:
  - S_Co
  - T_Co
  - Coble transcendental lattice
created: 2026-05-10
---

> [!example] Coble lattice For a classical Coble surface with one boundary component, the invariant lattice of the K3 cover is
> $$
> S_{\mathrm{Co}} = (11,11,1)_1 \cong \langle -2 \rangle \oplus E_{10}(2),
> $$
> and its orthogonal complement in the K3 lattice is
> $$
> T_{\mathrm{Co}} = (11,11,1)_2 \cong \langle 2 \rangle \oplus E_{10}(2).
> $$ [@DM19; @DK13]
> $$

## Basic properties

- $S_{\mathrm{Co}}$ has signature $(1,10)$.
- $T_{\mathrm{Co}}$ has signature $(2,9)$.
- Both are even 2-elementary lattices with discriminant group $(\mathbf{Z}/2)^{11}$ and $\delta = 1$ [@DM19; @DK13].
- The identification of $T_{\mathrm{Co}}$ follows from the anti-isometry of discriminant forms in the primitive embedding
  $$
  S_{\mathrm{Co}} \hookrightarrow \Lambda_{K3}
  $$
  together with Nikulin's classification [@Nik79; @DK13].

## Primitive embeddings

There is a sequence of primitive embeddings
$$
T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}} \hookrightarrow \Lambda_{K3},
$$
where
$$
T_{\mathrm{En}} = U \oplus E_{10}(2), \qquad T_{\mathrm{dP}} = U \oplus U(2) \oplus E_8^{\oplus 2}.
$$

For the first map, writing $T_{\mathrm{Co}} = \langle h \rangle \oplus E_{10}(2)$, one may send
$$
h \longmapsto \tilde e + \tilde f \in U
$$
and act as the identity on the $E_{10}(2)$ summand.
The embedding is primitive, and its uniqueness up to the orthogonal group is justified using Nikulin's results and the Enriques compactification arguments in [@AEGS23; @Nik79].

- These embeddings induce locally closed maps on period domains and extend to Baily-Borel compactifications [@KK72].
