---
title: KSBA model for polarized Coble surfaces
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - subject/compactifications
  - surface/coble
  - type/construction
aliases:
  - polarized Coble stable pair
  - KSBA stable model for polarized Coble surfaces
created: 2026-05-11
---

> [!construction] KSBA model for polarized Coble surfaces
> The intended polarized-Coble KSBA boundary object is a quotient surface together with the descended ramification divisor. The divisor is identified, while the singularity package and comparison theorem remain conjectural.

## Stable-pair package

- The intended open object is a pair of the form
  $$
  (\bar{S}, \epsilon R_{\bar{S}})
  $$
  with $0 < \epsilon \ll 1$.
- The durable correction is not the final theorem, but the checklist:
  - prove the descended divisor is $\mathbf{Q}$-Cartier,
  - prove it is ample,
  - prove the pair is slc,
  - and track how the anti-bicanonical $(-4)$-curve is seen on the resolution versus the stable model.
- A derivative local picture proposed in the source packets is that an $A_1$-node on the K3 cover, fixed by the Enriques involution, should descend to the $\frac{1}{4}(1,1)$ singularity on the stable quotient.

## Conjectural local package

- The derivative reports repeatedly describe the stable quotient as carrying a cyclic quotient singularity of type
  $$
  \frac{1}{4}(1,1).
  $$
- In the Horikawa model on $Y = \mathbf{P}^1 \times \mathbf{P}^1$ with $\tau(x,y) = (-x,-y)$, the proposed local input is a $\tau$-invariant $(4,4)$-curve passing through a fixed point with nondegenerate quadratic term, producing the $A_1$-node on the K3 double cover.
- They also treat the anti-bicanonical $(-4)$-curve on the smooth Coble resolution as the curve contracted to that singularity.
- One proposed local argument for the slc package runs through du Val singularities on the K3 cover and a finite quasi-etale quotient in codimension one.
- These statements are intellectually central to the program, but they should currently be read as **migrated research claims with portable provenance**, not as settled vault theorems.

## Historical refinement

- Earlier inbox drafts hand-waved the KSBA step by saying “the quotient is stable”.
- The correction cluster replaced that with the specific obligations above, especially ampleness and Cartier descent for the ramification divisor.
- The derivative correction packets also point toward running ampleness through the ample ramification divisor on the K3 cover and its descent, not through a blanket assertion that the quotient is automatically stable.
- In the more explicit local package, this is phrased as pulling back $K_{\bar{S}} + \epsilon R_{\bar{S}}$ to $\epsilon R_X$, with $R_X$ coming from the $(2,2)$-divisor on $Y$.

## See Also

- [[KSBA Compactifications]]
- [[No-moduli-loss issue in polarized Coble compactification]]
- [[KSBA vs. semitoroidal comparison for polarized Coble moduli]]

## Type and provenance

- **Type:** construction.
- **Conjectural local package:** the $A_1 \leadsto \frac{1}{4}(1,1)$ singularity story and the slc/ampleness verification still need proof.
- **Portable provenance:** mined from the 2026-05-11 Talks inbox; the stable-pair obligations are durable, while the exact singularity package remains a research claim awaiting direct corroboration.
- **Source packet:** `SRC-NLM-2026-05-11-rigorous-analysis`, `SRC-NLM-2026-05-11-ksba-a`, `SRC-NLM-2026-05-11-refining-moduli`.
