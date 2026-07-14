---
title: Generalized Coxeter Semifans
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - type/definition
aliases:
  - generalized Coxeter semifans
  - relevant root
  - irrelevant root
  - semitoroidal compactification
created: 2026-05-08
---

> [!definition] Generalized Coxeter Semifans
> The main geometric application of folded [[Coxeter-Vinberg Diagrams|diagrams]] is the construction of **semitoroidal compactifications** of moduli spaces $F_\Gamma$ via **generalized Coxeter semifans**.
> 
> For a $0$-cusp with Coxeter diagram $G(\Gamma_\eta)$, partition the simple roots into $\Phi = \Phi^{\mathrm{rel}} \sqcup \Phi^{\mathrm{irr}}$ [@AT17].
> - **Irrelevant roots ($\Phi^{\mathrm{irr}}$)**: Correspond to strata that are contracted in the KSBA stable model over $\eta$.
> - **Relevant roots ($\Phi^{\mathrm{rel}}$)**: The active walls where combinatorial types of stable models change.
> 
> The **generalized Coxeter semifan** $\mathcal{F}_{\mathrm{gen}}$ is obtained by omitting the walls defined by irrelevant roots [@AT17, Def. 4.16]. Its maximal cones are unions of Weyl chambers $g(\bigcup_{h \in W^{\mathrm{irr}}} h(\mathfrak{C}))$. 
> 
> Unlike classical toroidal compactifications where all walls of the Weyl chamber are preserved, semitoroidal compactifications allow certain **irrelevant roots** to be removed. 
> 
> The distinction between toroidal and strictly semitoroidal behavior depends on the order of the irrelevant root subgroup ($W^{\mathrm{irr}}$): 
> - **Toroidal**: $|W^{\mathrm{irr}}| < \infty$ (finite irrelevant subgroups).
> - **Strictly semitoroidal**: $|W^{\mathrm{irr}}| = \infty$ (infinite irrelevant subgroups, semifan is not locally finite).

## Polarized Coble trace picture

- The polarized Coble program asks for the **trace** of the Enriques ramification semifan on a Coble hyperplane, together with an admissibility condition for which restricted walls survive.
- This is recorded in [[Restriction of the ramification semifan to polarized Coble moduli]] and [[Admissibility issues for polarized Coble cusps]].
