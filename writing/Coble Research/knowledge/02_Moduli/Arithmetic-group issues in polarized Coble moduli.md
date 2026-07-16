---
title: Arithmetic-group issues in polarized Coble moduli
tags:
  - subject/algebraic-geometry
  - subject/moduli-spaces
  - surface/coble
  - type/remark
aliases:
  - Gamma_{Co,2}
  - arithmetic group for polarized Coble moduli
created: 2026-05-11
---

> [!remark] Arithmetic-group issues in polarized Coble moduli
> The current corrected framework defines the polarized Coble arithmetic group from the **stabilizer of a Coble root** inside the degree-2 Enriques group, rather than from a larger ad hoc subgroup.
> This is the minimal group that makes the period-map inclusion behave equivariantly.

## Corrected framework

- Fix a candidate Coble root $\delta$ in the polarized Enriques period lattice.

- The durable group-theoretic object is the image of the stabilizer of $\mathbf{Z}\delta$ in the polarized Enriques group acting on $\delta^\perp$.

- This is the group attached to a **branch** of the polarized Coble divisor, not automatically to the whole divisor.

- The remaining arithmetic gap is exactly whether the polarized subgroup still has a single root orbit, so that this branchwise stabilizer-image construction really collapses to one global arithmetic quotient.

## Equivariance issue

- The inclusion of period domains
  $$
  D(\delta^\perp) \hookrightarrow D(T_{\mathrm{En}})
  $$
  only gives a well-defined map of arithmetic quotients after the stabilizer is chosen correctly.

- In the Talks correction chain, this replaced a hand-waved equivariance claim.

## Historical refinement

- Earlier inbox notes used a more naive formula for $\Gamma_{\mathrm{Co},2}$ built from polarization stabilizers alone.

- The correction chain also rules out importing Namikawa's single $\Gamma_{\mathrm{En}}$ root orbit as though it already settled the finite-index polarized subgroup $\Gamma_{\mathrm{En},2}$.

- The later correction was that the relevant group must also remember the chosen Coble root.

- This preserves the possibility that different polarized root orbits produce different branches.

## How uniqueness could still be proved

- The preserved correction packets narrow the two safe routes to a single global quotient:

  - an arithmetic double-coset / orbit computation for the polarized subgroup, or

  - a geometric transitivity argument for the $D_4$-action on the torus-fixed-point branches in the Horikawa model.

- Until one of those routes is carried out, this note should be read as branchwise arithmetic scaffolding rather than as the final group for the whole polarized Coble locus.

## See Also

- [[Branchwise models of polarized Coble moduli]]

- [[Branch-curve model for polarized Coble surfaces]]

- [[Narrative MOC#Current blockers in Section 7]]

## Type and provenance

- **Type:** remark.

- **Question:** whether the polarized root orbit is unique, so that a single group really controls the whole polarized Coble locus.

- **Portable provenance:** mined from the 2026-05-11 Talks inbox; the stabilizer-image formulation replaced an earlier larger-group heuristic.

- **Source packet:** `SRC-NLM-2026-05-11-arithmetic-chat`, `SRC-NLM-2026-05-11-formal-refinement`, `SRC-NLM-2026-05-11-refining-moduli`.
