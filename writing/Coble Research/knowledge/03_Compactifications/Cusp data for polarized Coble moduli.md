---
title: Cusp data for polarized Coble moduli
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - subject/compactifications
  - surface/coble
  - type/construction
aliases:
  - polarized Coble cusps
  - cusp pairs for polarized Coble moduli
created: 2026-05-11
---

> [!construction] Cusp data for polarized Coble moduli
> The durable boundary mechanism from the Talks inbox is not a table of final cusp counts, but a **reduction strategy**: encode polarized Coble cusps by isotropic data together with a marked Coble root, and compare them to Sterk's Enriques representatives.

## Working boundary objects

- A polarized Coble 0-cusp is modeled by an orbit of a pair $(I,r)$ consisting of an isotropic line and a compatible Coble root.

- A polarized Coble 1-cusp is modeled by an orbit of a pair $(J,r)$ consisting of an isotropic plane and the same compatible root.

- A provisional incidence rule retained from the derivative packets is the containment relation $I \subset J$ with the same marked root fixed on both sides.

- This is the conceptual replacement for earlier unsupported cusp tables.

## Reduction to Sterk

- The rigorous part of the inbox correction is that any actual cusp count has to reduce to explicit lattice-orbit work, typically through Sterk representatives together with stabilizers or direct period-domain enumeration.

- In the refinement packet, the comparison target is specifically Sterk's established five 0-cusps and nine 1-cusps for the Enriques space; the polarized Coble side is encoded by marked-root pairs before any count is claimed.

- This source also supports one durable exclusion: because primitive isotropic vectors in the Coble lattice $T_{\mathrm{Co},2} \cong I_{2,9}(2)$ pair evenly in the ambient Enriques lattice, the divisibility-one Sterk cusp 1 should not occur on the polarized Coble boundary.

- So the only source-justified Sterk labels in play here are the divisibility-two cusps 2-5; the full polarized Coble incidence picture still has to come from explicit orbit work.

- Discriminant-form shortcuts may suggest candidates, but they do not by themselves prove the cusp diagram.

- The durable content here is this reduction mechanism together with admissibility bookkeeping, not any final label table.

## Discarded numerical attempts

- Earlier numerical tables and incidence diagrams were explicitly rejected inside the Talks corpus as unproved.

- They should be remembered only as discarded attempts, not as results to copy into canonical notes.

- In particular, the explicit boundary tables in `SRC-NLM-2026-05-11-rigorous-analysis` remain quarantined as unverified synthesis, apart from the divisibility-based exclusion of Sterk cusp 1; the incidence rule $I \subset J$ is retained.

## See Also

- [[Cusp Diagrams]]

- [[Admissibility issues for polarized Coble cusps]]

- [[Narrative MOC#Current blockers in Section 7]]

## Type and provenance

- **Type:** construction.

- **Portable provenance:** mined from the 2026-05-11 Talks inbox, where a major correction was to replace unsupported numerical data by a reduction mechanism to explicit orbit computations.

- **Source packet:** `SRC-NLM-2026-05-11-formal-refinement`, `SRC-NLM-2026-05-11-rigorous-analysis`, `SRC-NLM-2026-05-11-math-framework`, `SRC-NLM-2026-05-11-unresolved-obstacles`.
