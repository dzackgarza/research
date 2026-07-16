---
title: Moduli space of Coble surfaces
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - surface/coble
  - type/definition
aliases:
  - F_Co
  - moduli of Coble surfaces
created: 2026-05-10
---

> [!definition] Moduli space of Coble surfaces
> For Coble surfaces with one boundary component, the coarse moduli space $F_{\mathrm{Co}}$ is a 9-dimensional arithmetic quotient that can be presented in two compatible ways:
> $$
> F_{\mathrm{Co}} = \mathcal{H}_{-2} / \operatorname{O}(T_{\mathrm{En}})
> $$
> as a Heegner divisor inside the Enriques period space, and
> $$
> F_{\mathrm{Co}} \subset D_{T_{\mathrm{Co}}} / \operatorname{O}(T_{\mathrm{Co}})
> $$
> as an open subset of the Coble period domain [@DK13; @PS71; @CDL24].

## Key properties

- $F_{\mathrm{Co}}$ is a boundary divisor in the 10-dimensional moduli space of unpolarized Enriques surfaces [@DK13; @CDL24].

- It is a normal quasiprojective rational variety of dimension 9 [@DK13; @CDL24].

- On the Enriques side, this divisor appears when the K3 cover acquires an $A_1$-singularity fixed by the Enriques involution; the quotient has a quartic singularity whose resolution is the $(-4)$ boundary curve of a Coble surface [@Nue15].

- The locally closed embeddings induced by
  $$
  T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}}
  $$
  extend to morphisms on Baily-Borel compactifications [@KK72].

- The Baily-Borel boundary of $F_{\mathrm{En}}$ consists of $F_{\mathrm{Co}}$ together with two modular curves $X$ and $X_0(2)$, and the closure of $\mathcal{H}_{-2}$ contains $X$ [@CDL24].

## Geometric constructions

- **GIT point of view:** the blowup construction starts from ten points in $\mathbf{P}^2$, so $(\mathbf{P}^2)^{10} / \operatorname{PGL}_3$ has dimension $12$, and the Coble condition imposes three independent discriminant conditions, leaving $\dim F_{\mathrm{Co}} = 9$ [@Cob19; @DK13].

- **Horikawa point of view:** a $\tau$-invariant anti-bicanonical curve on $\mathbf{P}^1 \times \mathbf{P}^1$ passing through a fixed point yields a nodal K3 cover whose quotient is a Coble surface [@Hor78; @AEGS23]; see [[Horikawa model for Coble surfaces]].

## Polarized analogue

- The unpolarized space $F_{\mathrm{Co}}$ is now complemented by a status-aware cluster for the degree-2 polarized problem.
  The safe current entry point is [[Branchwise models of polarized Coble moduli]], not a finalized single quotient.

- The polarized story separates:

  - branch structure and arithmetic groups,

  - branch-curve geometry,

  - KSBA boundary objects,

  - and the ramification-semifan restriction problem.

- See [[Narrative MOC#Section 7: KSBA stable limits]] for the current paper-level checklist.
