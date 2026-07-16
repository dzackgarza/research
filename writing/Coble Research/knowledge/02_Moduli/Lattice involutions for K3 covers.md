---
title: Lattice involutions for K3 covers
tags:
  - subject/lattice-theory
  - subject/algebraic-geometry
  - type/definition
aliases:
  - del Pezzo involution
  - Enriques involution
  - Nikulin involution
created: 2026-05-08
---

> [!definition] Lattice involutions for K3 covers
> Fix a basis of the [[K3 lattice]] $L_{\mathrm{K3}}$ corresponding to the decomposition $U^3 \oplus E_8^2$.
> We consider three morphisms on $L_{\mathrm{K3}}$, acting on vectors $(u_1, u_2, u_3, \alpha_1, \alpha_2)$ in this basis:
> 
> $$
> \begin{aligned}
>     I_{\operatorname{dP}}(u_1, u_2, u_3, \alpha_1, \alpha_2)        &= (-u_1, u_3, u_2, -\alpha_1, -\alpha_2) \\
>     I_{\mathrm{En}}(u_1, u_2, u_3, \alpha_1, \alpha_2)  &= (-u_1, u_3, u_2, \alpha_2, \alpha_1) \\
>     I_{\mathrm{Nik}}(u_1, u_2, u_3, \alpha_1, \alpha_2) &= (u_1, u_2, u_3, -\alpha_2, -\alpha_1)
> \end{aligned}
> $$
> 
> These arise as the lattice involutions on $L_{\mathrm{K3}}$ induced by three types of geometric involutions—$\iota_{\operatorname{dP}}$ (del Pezzo), $\iota_{\mathrm{En}}$ (Enriques), and $\iota_{\mathrm{Nik}}$ (Nikulin)—on a [[K3 surface]] $X$.

## Properties

- The group $\langle I_{\operatorname{dP}}, I_{\mathrm{En}}, I_{\mathrm{Nik}} \rangle$ is isomorphic to $\mathbf{Z}_2^2$, meaning these involutions mutually commute.

- For each involution $I_\star$, the invariant sublattice is denoted $S_\star \mathrel{\mathop:}= L_{\mathrm{K3}}^{I_\star = 1}$ and the co-invariant sublattice is $T_\star = L_{\mathrm{K3}}^{I_\star = -1}$.

- The transcendental lattices $T_Z$ of [[Enriques surface|Enriques surfaces]] $Z$ primitively embed into these invariant sublattices.

## (Co)Invariant Lattices

| $L$ | Isometry Class | $\operatorname{rank}_{\mathbf{Z}}(L)$ | $\operatorname{sig}(L)$ | $(r,a,\delta)_n$ | $A_L$ |
| --- | --- | --- | --- | --- | --- |
| $S_{\operatorname{dP}}$ | $U(2)$ | $2$ | $(1,1)$ | $(2,2,0)_1$ | $\mathbf{Z}_2^2$ |
| $T_{\operatorname{dP}}$ | $U \oplus U(2) \oplus E_8^2$ | $20$ | $(2,18)$ | $(20,2,0)_2$ | $\mathbf{Z}_2^2$ |
| $S_{\mathrm{En}}$ | $U(2) \oplus E_8(2)$ | $10$ | $(1,9)$ | $(10,10,0)_1$ | $\mathbf{Z}_2^{10}$ |
| $T_{\mathrm{En}}$ | $U \oplus U(2) \oplus E_8(2)$ | $12$ | $(2,10)$ | $(12,10,0)_2$ | $\mathbf{Z}_2^{10}$ |
| $L_{\mathrm{Nik}}^{+}$ | $U^3 \oplus E_8(2)$ | $14$ | $(3,11)$ | $(14,8,0)_3$ | $\mathbf{Z}_2^8$ |
| $L_{\mathrm{Nik}}^{-}$ | $E_8(2)$ | $8$ | $(0,8)$ | $(8,8,0)_0$ | $\mathbf{Z}_2^8$ |
