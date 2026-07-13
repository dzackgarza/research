---
title: Integral Affine Structures on Degenerations
tags:
  - subject/algebraic-geometry
  - type/definition
aliases:
  - singular integral-affine structure
  - Symington polytope
  - integral-affine polarization
created: 2026-05-08
---

> [!definition] Integral Affine Structures on Kulikov Models The dual complex $\Gamma({\mathcal{X}}_0)$ of a Type III Kulikov model carries a canonical **singular integral-affine structure** (IAS). Away from singularities, charts map to $\mathbf{R}^2$ with transition functions in $\operatorname{GL}_2(\mathbf{Z}) \ltimes \mathbf{R}^2$.
> 
> Singularities in the IAS correspond to components of positive charge (non-toric anticanonical pairs).
> The total charge of 24 dictates the number and type of singularities (e.g. 24 $I_1$ singularities).

> [!definition] Symington Polytope and Monodromy Given a monodromy invariant $\lambda$ with barycentric coordinates $\ell_i = \lambda \cdot \alpha_i$, the **Symington polytope** $P(\lambda)$ is an integral-affine polygon determined by these coordinates.
> The integral-affine sphere $B(\lambda)$ is constructed by gluing two copies: $$ B(\lambda) = P(\lambda) \cup P(\lambda)^{\mathrm{op}} $$ This sphere is the dual complex $\Gamma({\mathcal{X}}*0)$ for the given monodromy.
> The equator connecting the two copies supports the **integral-affine polarization** $R*{\mathrm{IA}}$.

## Marked-root Coble constraint

- In the polarized Coble program, the integral-affine data is refined by a marked root satisfying $\lambda \cdot r = 0$ before one folds from the K3 picture to the Enriques/Coble picture.
- This is recorded in [[Marked-root integral-affine structures for Coble surfaces]], where the remaining open point is compatibility with an equivariant triangulation.

## Polarized Coble landing zone

- The preserved Coble source packets route the IAS continuation as an upstairs-to-downstairs sequence:
  - start with K3 monodromy / Coxeter data,
  - fold to Enriques boundary data,
  - then impose the marked-root constraint $\lambda \cdot r = 0$ for the polarized Coble branch.
- In this vault, that means this card remains the generic IAS entry point, while the Coble-specific section-6 payload lives in [[Marked-root integral-affine structures for Coble surfaces]].
