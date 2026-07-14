---
title: Moduli space of degree 2 numerically polarized Enriques surfaces
tags:
  - subject/algebraic-geometry
  - type/definition
aliases:
  - F_{En, 2}
created: 2026-05-08
---

> [!definition] Moduli space of degree 2 numerically polarized Enriques surfaces ($F_{\mathrm{En}, 2}$)
> The moduli space $F_{\mathrm{En}, 2}$ parameterizes pairs $(Z, [\mathcal{L}_Z])$, where $Z$ is an [[Enriques surface]], possibly with ADE singularities, and $[\mathcal{L}_Z] \in \operatorname{Pic}(Z)/\mathbf{Z}_2 \cong \operatorname{Num}(Z)$ is the [[Numerical polarization|numerical class of an ample polarization]] of degree 2. 
> 
> Equivalently, it may be described as the moduli space of pairs $(Z, \mathcal{M})$, where $\mathcal{M} = \mathcal{L}_Z^{\otimes 2} \in \operatorname{Pic}(Z)$ is a 2-divisible polarization of degree 8.


## Properties
- The set of primitive classes $h$ with $h^2 = 2d$, up to the action of $\operatorname{O}(L_{\mathrm{En}})$, may consist of more than one orbit, except in the case $d = 1$, where the orbit is unique. Therefore, the moduli space $F_{\mathrm{En}, 2}$ is distinguished by this uniqueness property.
- For a pair $(Z, \mathcal{M})$, the linear system $|\mathcal{M}|$ is basepoint-free and defines a morphism $\rho\colon Z \to W$ where $W$ is a quartic del Pezzo surface with singularities of type $4A_1$ or $A_3 + 2A_1$. The morphism $\rho$ is a double cover of $W$ branched along a divisor $B \subset W$ [@CDL24].
- The corresponding ramification divisor $R_Z = \rho^{-1}(B)$ is ample, $\mathbf{Q}$-Cartier, and in the linear system $|\mathcal{M}|$ [@CDL24].
- The pair $(Z, \varepsilon R_Z)$ is log-canonical for sufficiently small $\varepsilon > 0$, allowing $F_{\mathrm{En}, 2}$ to admit a [[KSBA stable pair|KSBA compactification]] $\overline{F_{\mathrm{En}, 2}}$ [@CDL24].

## Polarized Coble boundary

- The 2026-05-11 inbox mining pass extracted a polarized-Coble cluster inside the degree-2 Enriques problem. Its safe current form is **branchwise**, not yet a single established quotient; see [[Branchwise models of polarized Coble moduli]].
- The main ambient issues are separated into:
  - [[02_Moduli/Arithmetic-group issues in polarized Coble moduli|Arithmetic-group issues in polarized Coble moduli]]
  - [[Branch-curve model for polarized Coble surfaces]]
  - [[KSBA model for polarized Coble surfaces]]
- These notes intentionally distinguish established ambient Enriques facts from the still-open polarized Coble comparison program.

## See Also
- [[Isomorphism between KSBA and Semitoroidal Compactifications of F_{En,2}]]
- [[Narrative MOC#Section 7: KSBA stable limits]]
