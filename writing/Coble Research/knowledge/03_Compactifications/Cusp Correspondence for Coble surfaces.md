---
title: Cusp Correspondence for Coble surfaces
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - surface/coble
  - type/theorem
aliases:
  - Enriques to Coble cusp correspondence
  - Coble cusp map
created: 2026-05-10
---

> [!theorem] Cusp correspondence for the Coble moduli space The embedding $F_{\mathrm{Co}} \hookrightarrow F_{\mathrm{En}}$ sends the two Coble boundary cusps to the Enriques boundary cusps [@AE22; @CDL24]
> $$
> (9,9,1)_1 \mapsto (10,8,0)_1, \qquad (7,7,1)_0 \mapsto (8,6,0)_0.
> $$
> Under the further embedding into the degree-2 K3 moduli space,
> $$
> (9,9,1)_1 \mapsto (18,0,0)_1, \qquad (7,7,1)_0 \mapsto (16,0,0)_0.
> $$

## 0-cusp argument

- In
  $$
  T_{\mathrm{Co}} = \langle 2 \rangle \oplus E_{10}(2),
  $$
  every nonzero pairing is even, so primitive isotropic vectors have divisibility 2 [@AE22].
- For the standard isotropic vector $v_1 = e'$, its image $w_1 = \tilde e'$ in $T_{\mathrm{En}}$ also has divisibility 2 [@AE22].
- Therefore
  $$
  w_1^\perp / w_1 \cong U \oplus E_8(2) \cong (10,8,0)_1,
  $$
  giving the 0-cusp correspondence [@AE22; @CDL24].

## 1-cusp argument

- Let
  $$
  v_2 = 2h + \alpha_1 + \alpha_2, \qquad
  w_2 = 2\tilde e + 2\tilde f + \tilde\alpha_1 + \tilde\alpha_2.
  $$
- Inside
  $$
  w_1^\perp / w_1 \cong U \oplus E_8(2),
  $$
  the vector $w_2$ has divisibility 2 because both the $U$-part and the $E_8(2)$-part pair evenly [@AE22].
- This identifies the image 1-cusp as $(8,6,0)_0$ rather than $(8,8,0)_0$ [@AE22; @CDL24].

## Degree-2 K3 interpretation

- In $T_{\mathrm{dP}} = U \oplus U(2) \oplus E_8^{\oplus 2}$, the image of $v_1$ has quotient lattice [@AEGS23]
  $$
  \tilde w_1^\perp / \tilde w_1 \cong U \oplus E_8^{\oplus 2} \cong (18,0,0)_1.
  $$
- The image $\tilde w_2$ has divisibility 1, so its cusp is of odd type and gives $(16,0,0)_0$ [@AEGS23].
- The 0-cusp therefore matches **Sterk cusp 2** after folding the Coxeter diagram of $(18,0,0)_1$, explaining the expected disk-type IAS and Kulikov behavior [@AEGS23; @Ste91].
