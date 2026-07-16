---
title: KSBA Compactifications
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - type/definition
aliases:
  - KSBA stable pair
  - KSBA compactification
created: 2026-05-08
---

> [!definition] KSBA Compactifications
> The **KSBA compactification** generalizes the Deligne-Mumford compactification of curves to higher dimensions.
> It compactifies moduli of varieties of log general type by considering **stable slc pairs** $(X, D)$ [@KSB88; @Ale96].
> 
> A pair $(X, D=\sum b_j D_j)$ is KSBA-stable if:
> 1. $X$ is a projective demi-normal variety.
> 2. $0 < b_j \le 1$.
> 3. The pair $(X, D)$ has **semi log canonical (slc)** singularities.
> 4. $K_X + D$ is ample and $\mathbf{Q}$-Cartier.
> 
> For K-trivial varieties (like K3 or Enriques surfaces), one uses pairs $(X, \varepsilon R)$ for $0 < \varepsilon \ll 1$ and a polarizing divisor $R$.
> The KSBA moduli space $\overline{F}_\Gamma$ provides a modular, proper, algebraic compactification where boundary divisors correspond to geometric stable degenerations [@AET23; @AEGS23].

## Polarized Coble application

- The new note [[KSBA model for polarized Coble surfaces]] records the Coble-specific stable-pair package extracted from the Talks inbox.
- In that application, the durable content is a list of KSBA obligations: descent of the ramification divisor, $\mathbf{Q}$-Cartierness, ampleness, and slc control.
- The resulting comparison target is [[KSBA vs. semitoroidal comparison for polarized Coble moduli]], which remains an open program rather than a settled theorem.
