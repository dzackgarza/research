---
unit: reference
status: open
tags:
  - open-problems
  - conjectures
  - register
---

# Open questions and conjectures {#sec-open-questions}

::: {.remark title="Scope"}

This page lists the questions, conjectures and required theorems of this book whose answer is not known, each with the block or section that states it.
Items stated in the dissertation are cited by their path under `writing/dissertation/`.
The last section lists the questions that a finite derivation or computation decides.
:::

## Category theory

| Unknown | Stated in |
|:---|:---|
| **Inverting the hyperbolic stabilization** | @sec-open-statements; sharpened by @thm:invertible-summand |
| **Monoidal structures with an invertible object of nonzero Witt class** | @sec-open-statements; sharpened by @thm:invertible-summand |
| **The discriminant construction as a functor on Poincaré complexes** | @sec-open-statements |
| **A canonical universe for the equality predicate** | @sec-equality-universe |
| **$K_0$ of the $2$-elementary forms** | @thm:2elementary-decomposition; `sections/1-part-combinatorial/2-chapter-lattice-theory/300-classification.md` |

: {tbl-colwidths="[35,65]"}

## Lattice theory and hyperbolic reflection groups

| Unknown | Stated in |
|:---|:---|
| **Vector-level transitivity for $\latI_{1,8}$** | after @prop:rank-nine-line-transitivity in @sec-embeddings-overlattices |
| **The reflection subgroup of each Sterk fundamental domain** | @qst:sterk-reflection-subgroup, @qst:sterk-ideal-vertices |
| **Global questions on hyperbolic Coxeter diagrams** | @qst:maximal-parabolic-complexity, @conj:galois-invariance-parabolics, @qst:parabolic-count-growth, @qst:arithmeticity, @qst:exact-covolume, @qst:regularized-theta |

: {tbl-colwidths="[35,65]"}

## The Coble arithmetic group and its cusps

| Unknown | Stated in |
|:---|:---|
| **The number of $1$-cusps of $\fco$** | @sec-open-problems; the full-group case, @thm:plane-transitivity-tco |
| **A generating set of the group $\Gamma_\Co$** | @prob:coxeter-completeness; the reflective set is decided — it is exactly the short roots, @prop:gamma-co-reflective-set — and what is open is the index $[\Gamma_\Co : W(T_\Co)]$ |
| **Equality of the four arithmetic groups** | @prob:group-identification, @sec-four-groups, @sec-gamma-co-comparison; reduced to finite groups by @prop:gamma-co-two-definitions, and the Heegner and $\theta$ overgroups are strictly larger, both with index $\abs{W(E_8)}$ (@prop:gamma-co-heegner-strict, @prop:theta-co-index); under block-compatibility of the gluing — an instance of @prob:coble-rigidity, and a *real* condition, since both summand decompositions fail to be $\Orth(q)$-invariant (computed: `computations/reports/coble_gluing_discriminants.py`, `computations/reports/coble_a20-block-invariance.py`) — the Heegner description is the congruence one cut down to $\Orth^+$, the index being $\abs{W(E_8)} = 696\,729\,600$ inside $\Orth^+$ and $2\abs{W(E_8)} = 1\,393\,459\,200$ for the full preimage, both unconditional (@prop:gamma-cong-eq-heegner); what is open is the comparison with the direct and geometric entries (@prob:coble-rigidity, @prob:B24, @prob:B25) together with the same block-compatibility for $\gamma_\Co$, which would identify the $\theta$ description with them; `computations/reports/smw0_accepted-proofs.md`, `computations/reports/coble_gamma_co_two_definitions.py` |
| **Which quotient of $D(T_\Co)$ is the Coble moduli space** | @qst:sextic-group-comparison |
| **Labeled Coble rigidity** | @prob:coble-rigidity, @prob:effective-cone-agreement, @prob:twist-identification, @rmk:a21-open |
| **Projective coverage and the moduli equivalence** | @prob:projective-coverage, @prob:cover-singular-equivalence, @prob:period-diagram |
| **The Enriques-to-Coble cusp correspondence** | @sec-enriques-coble-correspondence; the reduction @prop:cusp-map-separates-mod-two |
| **The Coble cusps in the morphism chain** | @sec-cusp-correspondence-morphism-chain |
| **The distinguished elliptic fibration of the K3 cover** | @sec-open-problems |
| **The home of the group action** | @qst:coble-mukai-naturality |

: {tbl-colwidths="[35,65]"}

## Stable limits and the compactification of $\fco$

| Unknown | Stated in |
|:---|:---|
| **Root-orbit uniqueness under $\gent$** | @qst:coble_root_orbit_uniqueness |
| **The quarter singularity** | @conj:coble_quarter_singularity |
| **KSBA versus semitoroidal** | @conj:ksba_semitoroidal_comparison, @conj:no_moduli_loss, @conj:restricted_ramification_semifan |
| **Admissibility of Coble roots at a cusp** | @qst:coble_cusp_admissibility |
| **An equivariant triangulation compatible with the marked root** | @qst:equivariant_triangulation |
| **Is $\mch^*_{10A_1}$ empty, and where do the three semifans sit** | @qst:coble-arrangement-empty, @qst:semifan-poset-position |
| **The direct Coble theory** | @sec-status-ledger; @prob:coxeter-completeness, @prob:affine-realization, @prob:algebraic-extension, @prob:dlt-quotient, @prob:stable-proj, @prob:component-classification, @prob:direct-semifan, @prob:restricted-semifan, @prob:autonomous-theorem, @prob:comparison-theorem |

: {tbl-colwidths="[35,65]"}

## The degree-$2$ Enriques comparison

| Unknown | Stated in |
|:---|:---|
| **The classifying map of $\fentwo$** | @conj:enriques_involution_extension, @conj:classifying_map_finite, @conj:classifying_map_isomorphism; `sections/3-part-main-theorem/6-chapter/600-finite-coarsening.md` |
| **Descent of the semitoroidal data** | @conj:descent_semitoroidal_data_En2, @warn:restrict-semifan; `sections/3-part-main-theorem/6-chapter/500-descent-semitor.md` |

: {tbl-colwidths="[35,65]"}

## The other families

| Unknown | Stated in |
|:---|:---|
| **The families $F_{\Co,n}$ for $2\leq n\leq 10$** | @sec-coble-families-research-program; the constraint of @sec-reflective-two-elementary |
| **Nodal Enriques surfaces** | @sec-nodal-enriques-moduli-program |
| **Halphen surfaces of index $2$** | @sec-halphen-index-2-moduli-program |
| **The Dolgachev--Zhang classification** | beside @qst:coble-mukai-naturality |

: {tbl-colwidths="[35,65]"}

## The dissertation

| Unknown | Stated in |
|:---|:---|
| **Do the integral-affine data determine the stable limit** | `conj:classification-ia-data` in `sections/3-part-main-theorem/7-chapter/800-divisor-models.md` |
| **The semifan of a recognizable divisor** | `sections/2-part-moduli/4-chapter-cpt/300-semitoroidal.md` |
| **The cusp bijection across two discriminants** | `sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md` |

: {tbl-colwidths="[35,65]"}

## Questions decidable by a finite computation

| Unknown | Stated in |
|:---|:---|
| **Dawes' Example 2.2** | @qst:dawes-example-22; the two complements are isometric (@lem:complement-determinant, `computations/reports/coble_dawes-example-2-2_complements.py`) |

: {tbl-colwidths="[35,65]"}
