---
unit: reference
status: open
tags:
  - open-problems
  - conjectures
  - register
---

# Open questions and conjectures {#sec-open-questions}


::: {.remark title="What this page registers"}

This page is the register of the statements in this book and in the dissertation that have no proof: the questions, conjectures, and required theorems whose answer is not known.
Each row names the unknown, the block or section that states it, and its work unit in the [issue tree](https://github.com/dzackgarza/research/issues/641), which holds the acceptance condition.
The cited block is the statement of record; this page states no mathematics.
Dissertation items are cited by path under `writing/dissertation/`, since the dissertation is outside the book.

The register excludes three kinds of gap that the issue tree also holds: a standard proof not yet attached to a standard theorem, coordinate work such as an explicit matrix, and a repair to the text.
A question that a finite derivation or computation decides is listed in the last section, apart from the research unknowns.

A row leaves this page when its owner holds a proof, a disproof, or a computation record, and the pages that cite the open form are updated.
:::

## Category theory

| Unknown | Statement of record | Work unit |
|:---|:---|:---|
| **Inverting the hyperbolic stabilization** | @sec-open-statements; sharpened by @thm:invertible-summand | [#682](https://github.com/dzackgarza/research/issues/682) |
| **Monoidal structures with an invertible object of nonzero Witt class** | @sec-open-statements; sharpened by @thm:invertible-summand | [#682](https://github.com/dzackgarza/research/issues/682) |
| **The discriminant construction as a functor on Poincaré complexes** | @sec-open-statements | [#682](https://github.com/dzackgarza/research/issues/682) |
| **A canonical universe for the equality predicate** | @sec-equality-universe | |
| **$K_0$ of the $2$-elementary forms** | @thm:2elementary-decomposition; `sections/1-part-combinatorial/2-chapter-lattice-theory/300-classification.md` | [#683](https://github.com/dzackgarza/research/issues/683) |

: {tbl-colwidths="[32,48,20]"}

## Lattice theory and hyperbolic reflection groups

| Unknown | Statement of record | Work unit |
|:---|:---|:---|
| **Vector-level transitivity for $\latI_{1,8}$** | settled by @prop:rank-nine-vector-transitivity in @sec-embeddings-overlattices: $\Orth(\latI_{1,8})$ is transitive on primitive isotropic vectors, and $\Orth^+(\latI_{1,8})$ has exactly two orbits, $v$ and $-v$, the two sides of the positive cone, exchanged by $-\id\notin\Orth^+$; no reflection inside $v^{\perp}$ moves between them, $v^{\perp}/v\cong\latI_{0,7}$ being negative definite, so every such reflection lies in $\Orth^+$ | [#659](https://github.com/dzackgarza/research/issues/659) |
| **The reflection subgroup of each Sterk fundamental domain** | @qst:sterk-reflection-subgroup, @qst:sterk-ideal-vertices: the five cusps are the five $M$-orbits of isotropic classes, and each published diagram is the folded Enriques diagram $G(\bar T_\dP)^{J_j}$ of \[@AEGS25], which is the diagram of $W(\Gamma_{\En,2,\eta_j})$; every root Sterk prints is a root of $T_\En$ orthogonal to his $\eta_j$ whose walls bound a polytope of finite covolume with the recorded CoxIter vertex counts (@thm:sterk-reflection-subgroups). Open: the index $[W(\eta_j^\perp/\eta_j):W_j]$, a covolume ratio; the chamber as a polyhedron at cusps $1$, $3$, $4$ (sage-extensions#312, #297) | [#654](https://github.com/dzackgarza/research/issues/654) |
| **Global questions on hyperbolic Coxeter diagrams** | @qst:maximal-parabolic-complexity, @conj:galois-invariance-parabolics, @qst:parabolic-count-growth, @qst:arithmeticity, @qst:exact-covolume, @qst:regularized-theta | [#660](https://github.com/dzackgarza/research/issues/660) |

: {tbl-colwidths="[32,48,20]"}

## The Coble arithmetic group and its cusps

| Unknown | Statement of record | Work unit |
|:---|:---|:---|
| **The number of $0$-cusps of $\fco$** | @prob:cusp-lifting; answered (@sec-cusp-lifting): the lifting theorem holds, every nonzero isotropic class lifts and the zero one does not, and the $\widetilde\Orth^+(T_\Co)$-orbits of primitive isotropic lines number $527$, one per nonzero isotropic class; those are the $0$-cusp orbits of the stable quotient, while $\fco = \bD(T_\Co)/\Gamma_\Co$ with $\Gamma_\Co = \Orth(T_\Co)$ (@prop:gamma-co-images(3)) has one $0$-cusp, by @thm:unpolarized-cusps, computed by sage-extensions#286 in its $\Orth(T_\Co)$ row; the four finite orbits 135, 2, 270, 120 are the count for $\rho^{-1}(G_\Co)$, not for $\widetilde\Orth^+(T_\Co)$: computed on $A_{S_\En}$ in `computations/reports/coble_gco_orbit-decomposition.py` and carried to $A_{T_\Co}$ by @lem:gco-orbit-transfer; the stabilizer index being the equality proved in @sec-cusp-lifting, @prop:coble-cusp-count, where the count is marked proved in prose only with sage-extensions#286 as the computation owed; @sec-open-problems | [#644](https://github.com/dzackgarza/research/issues/644), [#667](https://github.com/dzackgarza/research/issues/667) |
| **The number of $1$-cusps of $\fco$** | @sec-open-problems; the full-group case, @thm:plane-transitivity-tco, is a theorem of this book; the $\widetilde\Orth^+(T_\Co)$-orbit count and the $\Gamma_{\Co,2}$-orbit count are open, the last until sage-extensions#286, while $\Gamma_\Co = \Orth(T_\Co)$ gives one $1$-cusp (@thm:plane-transitivity-tco), certified by the same operation | [#645](https://github.com/dzackgarza/research/issues/645) |
| **A generating set of the group $\widetilde\Orth^+(T_\Co)$** | @prob:coxeter-completeness; the reflective set is decided — it is exactly the short roots, @prop:gamma-co-reflective-set — and what is open is the index $[\widetilde\Orth^+(T_\Co) : W(T_\Co)]$ | [#646](https://github.com/dzackgarza/research/issues/646) |
| **Equality of the four arithmetic groups** | @prob:group-identification, @sec-four-groups, @sec-gamma-co-comparison; reduced to finite groups by @prop:gamma-co-two-definitions, and the Heegner and $\theta$ overgroups are strictly larger, both with index $\abs{W(E_8)}$ (@prop:gamma-co-heegner-strict, @prop:theta-co-index); under block-compatibility of the gluing — an instance of @prob:coble-rigidity, and a *real* condition, since both summand decompositions fail to be $\Orth(q)$-invariant (computed: `computations/reports/coble_gluing_discriminants.py`, `computations/reports/coble_a20-block-invariance.py`) — the Heegner description is the congruence one cut down to $\Orth^+$, the index being $\abs{W(E_8)} = 696\,729\,600$ inside $\Orth^+$ and $2\abs{W(E_8)} = 1\,393\,459\,200$ for the full preimage, both unconditional (@prop:gamma-cong-eq-heegner); what is open is the comparison with the direct and geometric entries (@prob:coble-rigidity, @prob:B24, @prob:B25) together with the same block-compatibility for $\gamma_\Co$, which would identify the $\theta$ description with them; `computations/reports/smw0_accepted-proofs.md`, `computations/reports/coble_gamma_co_two_definitions.py` | [#647](https://github.com/dzackgarza/research/issues/647), [#663](https://github.com/dzackgarza/research/issues/663), [#720](https://github.com/dzackgarza/research/issues/720) |
| **Which quotient of $D(T_\Co)$ is the Coble moduli space** | @qst:sextic-group-comparison | |
| **Labeled Coble rigidity** | @prob:coble-rigidity, @prob:effective-cone-agreement, @prob:twist-identification, @rmk:a21-open | [#664](https://github.com/dzackgarza/research/issues/664) |
| **Projective coverage and the moduli equivalence** | @prob:projective-coverage, @prob:cover-singular-equivalence, @prob:period-diagram | [#665](https://github.com/dzackgarza/research/issues/665), [#666](https://github.com/dzackgarza/research/issues/666) |
| **The Enriques-to-Coble cusp correspondence** | @sec-enriques-coble-correspondence; the reduction @prop:cusp-map-separates-mod-two | [#658](https://github.com/dzackgarza/research/issues/658) |
| **The Coble cusps in the morphism chain** | @sec-cusp-correspondence-morphism-chain | [#672](https://github.com/dzackgarza/research/issues/672) |
| **The distinguished elliptic fibration of the K3 cover** | @sec-open-problems | |
| **The home of the group action** | @qst:coble-mukai-naturality | [#673](https://github.com/dzackgarza/research/issues/673) |

: {tbl-colwidths="[32,48,20]"}

## Stable limits and the compactification of $\fco$

| Unknown | Statement of record | Work unit |
|:---|:---|:---|
| **Root-orbit uniqueness under $\gent$** | @qst:coble_root_orbit_uniqueness | [#648](https://github.com/dzackgarza/research/issues/648) |
| **The quarter singularity** | @conj:coble_quarter_singularity | [#649](https://github.com/dzackgarza/research/issues/649) |
| **KSBA versus semitoroidal** | @conj:ksba_semitoroidal_comparison, @conj:no_moduli_loss, @conj:restricted_ramification_semifan | [#650](https://github.com/dzackgarza/research/issues/650) |
| **Admissibility of Coble roots at a cusp** | @qst:coble_cusp_admissibility | [#651](https://github.com/dzackgarza/research/issues/651) |
| **An equivariant triangulation compatible with the marked root** | @qst:equivariant_triangulation | [#655](https://github.com/dzackgarza/research/issues/655) |
| **Is $\mch^*_{10A_1}$ empty, and where do the three semifans sit** | @qst:coble-arrangement-empty, @qst:semifan-poset-position | [#652](https://github.com/dzackgarza/research/issues/652), [#653](https://github.com/dzackgarza/research/issues/653) |
| **The direct Coble theory** | @sec-status-ledger; @prob:coxeter-completeness, @prob:affine-realization, @prob:algebraic-extension, @prob:direct-semifan --- whose Coxeter half at the one $0$-cusp of $\fco$ is @thm:coble-coxeter-semifan, and whose generalized half waits on a definition of the Coble stable pair, @prob:dlt-quotient, @prob:stable-proj, @prob:component-classification, @prob:direct-semifan, @prob:restricted-semifan, @prob:autonomous-theorem, @prob:comparison-theorem | [#668](https://github.com/dzackgarza/research/issues/668) to [#671](https://github.com/dzackgarza/research/issues/671), [#674](https://github.com/dzackgarza/research/issues/674) |

: {tbl-colwidths="[32,48,20]"}

## The degree-$2$ Enriques comparison

| Unknown | Statement of record | Work unit |
|:---|:---|:---|
| **The classifying map of $\fentwo$** | @conj:enriques_involution_extension, @conj:classifying_map_finite, @conj:classifying_map_isomorphism; `sections/3-part-main-theorem/6-chapter/600-finite-coarsening.md` | [#680](https://github.com/dzackgarza/research/issues/680) |
| **Descent of the semitoroidal data** | @conj:descent_semitoroidal_data_En2, @warn:restrict-semifan; `sections/3-part-main-theorem/6-chapter/500-descent-semitor.md` | [#681](https://github.com/dzackgarza/research/issues/681) |

: {tbl-colwidths="[32,48,20]"}

## The other families

| Unknown | Statement of record | Work unit |
|:---|:---|:---|
| **The families $F_{\Co,n}$ for $2\leq n\leq 10$** | @sec-coble-families-research-program; the constraint of @sec-reflective-two-elementary | [#675](https://github.com/dzackgarza/research/issues/675), [#676](https://github.com/dzackgarza/research/issues/676) |
| **Nodal Enriques surfaces** | @sec-nodal-enriques-moduli-program | [#686](https://github.com/dzackgarza/research/issues/686) |
| **Halphen surfaces of index $2$** | @sec-halphen-index-2-moduli-program | |
| **The Dolgachev--Zhang classification** | beside @qst:coble-mukai-naturality | [#677](https://github.com/dzackgarza/research/issues/677) |

: {tbl-colwidths="[32,48,20]"}

## The dissertation

| Unknown | Statement of record | Work unit |
|:---|:---|:---|
| **Do the integral-affine data determine the stable limit** | `conj:classification-ia-data` in `sections/3-part-main-theorem/7-chapter/800-divisor-models.md` | [#678](https://github.com/dzackgarza/research/issues/678) |
| **The semifan of a recognizable divisor** | `sections/2-part-moduli/4-chapter-cpt/300-semitoroidal.md` | [#679](https://github.com/dzackgarza/research/issues/679) |
| **The cusp bijection across two discriminants** | settled in `sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md` (`sec:fen-unpolarized-cusps`): the transport through $K$ is withdrawn, since $A_{\ten}\cong(\ZZ/2)^{10}$ against $A_K=0$ and $K$ has a single 0-cusp, and the count is the proposition proved there from the type trichotomy, with `computations/reports/coble_enriques-zero-cusps.py` | [#684](https://github.com/dzackgarza/research/issues/684) |

: {tbl-colwidths="[32,48,20]"}

## Decidable by a finite derivation, not yet decided

| Unknown | Statement of record | Work unit |
|:---|:---|:---|
| **Scattone's diagram against the AET19 diagram** | @sec-root-vectors-and-folded-sterk-diagrams | [#657](https://github.com/dzackgarza/research/issues/657) |
| **Dawes' Example 2.2** | decided in @qst:dawes-example-22: $v_1\sim v_2$ in $U\oplus A_3$, by the gluing — the complements are both $-A_4$ (@lem:complement-determinant), the "pure $N$" class carries $q = 4/5, 6/5$ and the "pure $\generators{v}$" class contradicts $\div_L(v) = 4$, leaving one diagonal class — `computations/reports/coble_dawes-example-2-2_gluing-class.py` | [#662](https://github.com/dzackgarza/research/issues/662) |
| **Two forms of the embedding $S_\En\hookrightarrow S_\Nod$** | @sec-nodal-enriques-moduli-program | [#685](https://github.com/dzackgarza/research/issues/685) |

: {tbl-colwidths="[32,48,20]"}
