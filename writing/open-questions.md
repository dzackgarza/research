---
unit: reference
status: open
tags:
  - open-problems
  - conjectures
  - register
---

# Open questions and conjectures {#sec-open-questions}

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
| **The cusp-stabilizer containment** | @qst:cusp-stabilizer-containment |
| **Global questions on hyperbolic Coxeter diagrams** | @qst:maximal-parabolic-complexity, @conj:galois-invariance-parabolics, @qst:parabolic-count-growth, @qst:exact-covolume, @qst:regularized-theta |

: {tbl-colwidths="[35,65]"}

## The Coble arithmetic group and its cusps

| Unknown | Stated in |
|:---|:---|
| **A generating set of the group $\widetilde\Orth^+(T_\Co)$** | @qst:gamma-co-generators, @prob:coxeter-completeness |
| **Which quotient of $D(T_\Co)$ is the Coble moduli space** | @qst:sextic-group-comparison |
| **Projective coverage and the moduli equivalence** | @prob:projective-coverage, @prob:cover-singular-equivalence, @prob:period-diagram |
| **The Enriques-to-Coble cusp correspondence** | @sec-enriques-coble-correspondence; the reduction @prop:cusp-map-separates-mod-two |
| **The Coble cusps in the morphism chain** | @sec-cusp-correspondence-morphism-chain |
| **The distinguished elliptic fibration of the K3 cover** | @qst:distinguished-elliptic-fibration |
| **The home of the group action** | @qst:coble-mukai-naturality |

: {tbl-colwidths="[35,65]"}

## Stable limits and the compactification of $\fco$

| Unknown | Stated in |
|:---|:---|
| **KSBA versus semitoroidal** | @conj:coble-ksba-semitoroidal-morphism, @conj:ksba_semitoroidal_comparison, @conj:no_moduli_loss, @thm:no-moduli-loss (the stable quotient $\bD(T_\Co)/\Gamma_{\Co,2}$ separates the $\Gamma_{\Co,2}$-orbits of marked roots at every marked cusp, and its KSBA-boundary form is @conj:no_moduli_loss's, whose one open step is the boundary Torelli statement of research#760 --- an isomorphism of stable pairs over the cusp induces an element of $\Gamma_{\Co,2}$ carrying one marked root to the other, and the converse --- the theorem being its quotient-side half; no face of the restricted semifan carries the marking: every admissible $T_\Co$-root at the marked cusps is irrelevant, so all of them cut one cone, @thm:face-irrelevant-marking; the $\Gamma_{\Co,2}$-orbits at cusp $5$ are decided and there are two of them: roots $13$ and $14$ are one orbit, by an explicit integral isometry of $T_\En$ that fixes $\delta$ and exchanges them and preserves the two summands of $A_{T_\En}$, so it lies in $\Gent = \rho^{-1}(M)$ (`computations/reports/coble_759-lift-1314-run.txt`, `computations/reports/coble_760-gent-membership-run.txt`), and Sterk's label $12$ is in another, by the coset computation that reduces the pair to one subspace orbit of $A_{T_\Co}$ and exhausts it without the target, the pair $(13,14)$ serving as a positive control (`computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`, @thm:face-irrelevant-marking(3)), on the stabilizer family the library labels untrusted, whose own construction is the operation that step waits on (`computations/reports/coble_760-vector-stabilizer-certification-run.txt`); the hypothesis of the conjecture is therefore met at cusp $5$, it is not vacuous, and what is open there is the identification step and not the orbit; the weaker class reading agrees and is decided too, the shift by a multiple of $\eta_5$ being removed by the shear $s_{r_{13}+\eta_5}s_{r_{13}}$ in $\Gamma_{\Co,2}$ and the two odd targets $\pm(r_{13}\pm\eta_5)$ being themselves unreachable (`computations/reports/coble_759-class-reading-1213-run.txt`); the contracted-curve route reads off the divisor @def:coble-descended-ramification, whose datum exists, but the recovery has no referent without the dictionary from the chamber's roots to curves of the Coble surface, which a search of the two sources the warning names finds nowhere — and the marking's identity is not what is open, since @thm:coble-cusp-admissibility(2) and @prop:marking-line-no-coble-lift fix it: the passage from the curve to its class is in no source read (`computations/reports/coble_760-cusp-marking-search-run.txt`) and in no operation of the library, no name in its 318 files referring to a stable pair, a semifan or a marked root, `Coble.rank_ten_diagram().stable_pairs()` raising `AttributeError` (`computations/reports/coble_759-limit-pair-call-probe-run.txt`), and the comparison this result feeds, @conj:ksba_semitoroidal_comparison, names this result among its own inputs, so the two cannot discharge each other; and the cusp's symmetries do not supply it either (`computations/reports/coble_760-cusp-symmetry-run.txt`), @warn:coble-marking), @conj:restricted_ramification_semifan |
| **An equivariant triangulation compatible with the marked root** | @qst:equivariant_triangulation |
| **The position of the three Coble semifans** | @qst:semifan-poset-position |
| **The semifan of the rational-curve divisor** | @qst:recognizable-semifan; the semifan of a recognizable divisor is described when it is a ramification divisor --- it is the generalized Coxeter semifan of the boundary diagram, its cones being the loci of a fixed KSBA combinatorial type (@thm:semifan-recognizable-divisor), with the split recorded in the three computed families (@cor:semifan-computed-cases; [@AET23, Def. 4.16 and Prop. 4.17, printed pp. 26--27; @AE22, Def. 9.5, printed p. 54]) --- and no split, hence no cone, of $\mcf_{R_\rcop}$ is recorded in any source read |
| **The direct Coble theory** | @sec-status-ledger; @prob:coxeter-completeness, @prob:affine-realization, @prob:algebraic-extension, @prob:dlt-quotient, @prob:stable-proj, @prob:component-classification, @prob:direct-semifan (answered at the four $0$-cusps of $F_{\Co,2}$: @thm:coble-pair-semifan), @prob:restricted-semifan, @prob:autonomous-theorem (its first clause is published in the unpolarized form, [@DK13, Prop. 3.2, printed p. 513], and the direct period image misses every $(-2)$-Heegner divisor of $T_\Co$ by @thm:direct-period-misses-root-walls, the polarized refinement being @prob:B25's up to its two-element ambiguity, whose candidate $-\id_{T_\Co}$ is in the group and outside $\Orth^+(T_\Co)$ (@lem:minus-id-in-direct-group, @warn:direct-group-orth-plus); clauses two and three wait on @sec-coxeter and @sec-coble-dlt), @prob:comparison-theorem |

: {tbl-colwidths="[35,65]"}

## The degree-$2$ Enriques comparison

| Unknown | Stated in |
|:---|:---|
| **Descent of the semitoroidal data** | @conj:descent_semitoroidal_data_En2, @prob:restricted-semifan |

: {tbl-colwidths="[35,65]"}

## The other families

| Unknown | Stated in |
|:---|:---|
| **A polarizing divisor positive on the fixed locus, for the $g = 0$ rows** | @qst:coble-n-polarizing-divisor |
| **Nodal Enriques surfaces** | @sec-nodal-enriques-moduli-program |
| **Halphen surfaces of index $2$** | @sec-halphen-index-2-moduli-program |
| **The Dolgachev--Zhang classification** | beside @qst:coble-mukai-naturality |

: {tbl-colwidths="[35,65]"}

## Questions decidable by a finite computation

| Unknown | Stated in |
|:---|:---|
| **Two forms of the embedding $S_\En\hookrightarrow S_\Nod$** | @sec-nodal-enriques-moduli-program |

: {tbl-colwidths="[35,65]"}
