---
title: Marked-root integral-affine structures for Coble surfaces
tags:
  - subject/algebraic-geometry
  - subject/degenerations
  - subject/integral-affine-geometry
  - surface/coble
  - type/construction
aliases:
  - marked-root IAS
  - zero-length-root IAS for Coble surfaces
created: 2026-05-11
---

> [!construction] Marked-root integral-affine structures for Coble surfaces
> The Talks inbox replaces an unclear “read the IAS directly from the Enriques Coxeter diagram” slogan by an upstairs construction: build the integral-affine data on the K3 side first, then impose the Coble condition by marking a zero-length root before folding to the Enriques/Coble picture.

## Upstairs-before-downstairs principle

- Start from the K3 Coxeter / monodromy data behind the integral-affine sphere.

- Impose the Coble constraint as a marked root with zero length:
  $$
  \lambda \cdot r = 0.
  $$

- Only after that should one pass to the folded Enriques data and then to the Coble trace picture.

- The source-local diagrammatic sequence is:

  - K3 Coxeter data,

  - then folded Enriques data,

  - then the Coble hyperplane / marked-root trace data.

## Why the marked root matters

- The marked root is meant to remember the vanishing cycle giving the node on the K3 cover.

- In the Coble quotient story, this marked vanishing data is what prevents the IAS from being just an ordinary Enriques boundary object.

## Compatibility question

- The Talks framework still leaves open the existence of an equivariant triangulation compatible with the marked root.

- So the durable content is the construction principle, not yet a finished combinatorial theorem.

## See Also

- [[Integral Affine Structures on Degenerations]]

- [[Restriction of the ramification semifan to polarized Coble moduli]]

- [[Narrative MOC#Current blockers in Section 7]]

## Type and provenance

- **Type:** construction.

- **Question:** whether an equivariant triangulation compatible with the marked root exists.

- **Portable provenance:** mined from the 2026-05-11 Talks inbox, where the IAS mechanism was explicitly moved from a diagram-only heuristic to a marked-root K3 construction.

- **Source packet:** `SRC-NLM-2026-05-11-rigorous-analysis`, `SRC-NLM-2026-05-11-refining-moduli`, `SRC-NLM-2026-05-11-math-framework`.
