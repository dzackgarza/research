---
title: Branchwise models of polarized Coble moduli
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - surface/coble
  - type/construction
aliases:
  - F_{Co,2}
  - polarized Coble moduli
  - branchwise Coble moduli
created: 2026-05-11
---

> [!construction] Branchwise models of polarized Coble moduli
> A provisional polarized analogue of [[Moduli space of Coble surfaces|$F_{\mathrm{Co}}$]] is obtained by taking the Coble Heegner divisor inside [[Moduli space of degree 2 numerically polarized Enriques surfaces|$F_{\mathrm{En},2}$]] and normalizing it branchwise.
> The durable point is that one should not assume a single global quotient until root-orbit uniqueness for the polarized arithmetic group is proved.

## Proposed shape

- The working picture is a union of branchwise quotients attached to candidate Coble roots in the degree-2 Enriques period lattice.

- This keeps the polarized story compatible with the unpolarized Heegner-divisor description while avoiding premature irreducibility claims.

- The branchwise viewpoint is the corrected replacement for earlier one-branch formulations mined from the Talks inbox.

- More concretely, Namikawa's root-orbit uniqueness is stated only modulo the full Enriques group $\Gamma_{\mathrm{En}}$, so the finite-index subgroup $\Gamma_{\mathrm{En},2}$ could split one unpolarized orbit into several polarized branches.

- The preserved correction packets sharpen the remaining fork: to replace this union by a single normalized divisor, one still needs either a polarized double-coset computation or a proof that the $D_4$-symmetry acts transitively on the torus-fixed-point branches of the Horikawa model.

## Historical refinement

- An earlier proof sketch treated the polarized Coble locus as though it were already a single arithmetic quotient.

- The correction is to separate:

  - the **existence of a Coble divisor** inside the polarized Enriques space, from

  - the **uniqueness of its polarized branch**, which remains an open proof obligation.

- On the Horikawa side, the one-fixed-point condition describes only the generic branch; the closure can meet several torus fixed points, so normalization has to separate those branches.

- The derivative source packets make the normalization issue explicit: the Heegner divisor can be used safely only branchwise until the orbit question is closed.

## See Also

- [[02_Moduli/Arithmetic-group issues in polarized Coble moduli|Arithmetic-group issues in polarized Coble moduli]]

- [[Narrative MOC#Current blockers in Section 7]]

- [[Moduli space of Coble surfaces]]

## Type and provenance

- **Type:** construction.

- **Question:** whether the polarized Coble divisor is irreducible, so that this branchwise construction collapses to a single normalized divisor.

- **Portable provenance:** mined from the 2026-05-11 Talks inbox, especially the correction cluster around root-orbit uniqueness and Heegner normalization.

- **Source packet:** `SRC-NLM-2026-05-11-arithmetic-chat`, `SRC-NLM-2026-05-11-formal-refinement`, `SRC-NLM-2026-05-11-math-framework`, `SRC-NLM-2026-05-11-unresolved-obstacles`.

- **Established anchors:** this note extends the existing Heegner-divisor viewpoint for the unpolarized space [[Moduli space of Coble surfaces]] into the polarized setting.
