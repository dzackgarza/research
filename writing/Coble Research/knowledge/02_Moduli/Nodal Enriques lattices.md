---
title: Nodal Enriques lattices
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - subject/moduli-spaces
  - type/example
aliases:
  - nodal Enriques lattice
  - S_Nod
  - T_Nod
created: 2026-05-10
---

> [!example] Nodal Enriques lattices
> For the moduli space of nodal Enriques surfaces, one has
> $$
> S_{\mathrm{Nod}} = (11,10,1)_1 \cong \langle -4 \rangle \oplus E_{10}(2),
> \qquad
> T_{\mathrm{Nod}} = (11,8,1)_2 \cong \langle 4 \rangle \oplus U \oplus E_8(2).
> $$
> These lattices are extracted from [@DK13, Prop. 3.1].

## Embedding from the Enriques lattice

There is a primitive embedding
$$
\begin{aligned}
S_{\mathrm{En}} &\injects S_{\mathrm{Nod}}, \\
U(2)\oplus E_8(2) &\injects U \oplus \langle -4 \rangle \oplus E_8(2),
\end{aligned}
$$
given by
$$
((e,f),x) \longmapsto ((2\tilde f + \tilde g + h,\tilde g),x),
$$
where
$$
U(2) = \langle e,f \rangle, \qquad U = \langle \tilde e,\tilde f \rangle, \qquad \langle -4 \rangle = \langle h \rangle.
$$
The map is the identity on the $E_8(2)$ summand [@CDL24].

## Moduli interpretation

- The induced period-domain map identifies the nodal Enriques locus as a subspace of the Enriques moduli space [@DK13; @CDL24].

- Geometrically, this is the lattice-theoretic avatar of the locus of Enriques surfaces containing a nodal curve [@DK13; @CDL24].
