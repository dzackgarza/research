---
title: Isomorphism between KSBA and Semitoroidal Compactifications of F_{En,2}
tags:
  - subject/algebraic-geometry
  - type/theorem
aliases:
  - Main Theorem
created: 2026-05-08
---

> [!theorem] Isomorphism between KSBA and Semitoroidal Compactifications of $F_{\mathrm{En}, 2}$
> Let $F_{\mathrm{En}, 2}$ be the [[Moduli space of degree 2 numerically polarized Enriques surfaces]], and let $\overline{F_{\mathrm{En}, 2}}$ be its [[KSBA stable pair|KSBA compactification]]. There is a morphism $$ (\overline{F_{\mathrm{En}, 2}}^{\mathcal{F}_{\bullet}})^{\nu} \xrightarrow{\sim} (\overline{F_{\mathrm{En}, 2}})^{\nu} $$ where $(-)^\nu$ denotes the normalization.
> The left-hand side is the semitoroidal compactification corresponding to an explicit collection $\mathcal{F}_{\bullet} = \{ \mathcal{F}_1, \Sigma_2, \mathcal{F}_3, \Sigma_4, \mathcal{F}_5 \}$ of semifans, one for each $0$-cusp of the Baily-Borel compactification $\overline{F_{\mathrm{En}, 2}}^{\operatorname{BB}}$, and the right-hand side is the KSBA compactification.
> 
> The semifans $\Sigma_2, \Sigma_4$ are fans, while $\mathcal{F}_1, \mathcal{F}_2, \mathcal{F}_3$ are strict semifans.

## Background

- The normalization is a technical condition often applied in KSBA compactifications because taking a Zariski closure can introduce non-normal points where degenerations are identified, leading to a non-separated stack.
  Since the normalization morphism is finite, birational, and relatively smooth in codimension one, it restricts the worst singularities to lie in high codimension sub-loci.

- The proof leverages the result of Alexeev and Engel (2023) that the normalization of the KSBA compactification of stable [[K3 surface|K3 pairs]] $(X, \varepsilon R)$ for a recognizable divisor $R$ is isomorphic to a semitoroidal compactification.

## Polarized Coble extension

- The new note [[KSBA vs. semitoroidal comparison for polarized Coble moduli]] records the Coble analogue as an **open program** rather than a theorem.

- Its extra difficulties are exactly the ones absent from the established Enriques theorem: branchwise root data, ramification-semifan restriction, and the [[No-moduli-loss issue in polarized Coble compactification|no-moduli-loss]] problem.
