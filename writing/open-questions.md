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
| **Equality of the four arithmetic groups** | @prob:group-identification, @sec-four-groups, @sec-gamma-co-comparison, @qst:gamma-co-generators; the Heegner and $\theta$ descriptions are compared with the congruence one in @prop:gamma-cong-eq-heegner, which leaves block-compatibility of the two gluings (@def:congruence-group, @lem:coble-discriminant-blocks, item 2 of @qst:gamma-co-generators), and the direct and geometric entries are @prob:coble-rigidity and @prob:B24, @prob:B25 |
| **Which quotient of $D(T_\Co)$ is the Coble moduli space** | @qst:sextic-group-comparison |
| **Labeled Coble rigidity** | @prob:coble-rigidity, @qst:chamber-clause-one-node, @qst:reflected-pair-conjugacy, @qst:del-pezzo-saturation-higher-k |
| **Projective coverage and the moduli equivalence** | @prob:projective-coverage, @prob:cover-singular-equivalence, @prob:period-diagram |
| **The Enriques-to-Coble cusp correspondence** | @sec-enriques-coble-correspondence; the reduction @prop:cusp-map-separates-mod-two |
| **The Coble cusps in the morphism chain** | @sec-cusp-correspondence-morphism-chain |
| **The distinguished elliptic fibration of the K3 cover** | @qst:distinguished-elliptic-fibration |
| **The home of the group action** | @qst:coble-mukai-naturality |

: {tbl-colwidths="[35,65]"}

## Stable limits and the compactification of $\fco$

| Unknown | Stated in |
|:---|:---|
| **KSBA versus semitoroidal** | @conj:coble-ksba-semitoroidal-morphism, @conj:ksba_semitoroidal_comparison, @conj:no_moduli_loss (no face of the restricted semifan carries the marking: every admissible $T_\Co$-root at the marked cusps is irrelevant, so all of them cut one cone, @thm:face-irrelevant-marking; the open step is the $\Gamma_{\Co,2}$-orbits of the three classes at cusp $5$: roots $13$ and $14$ are one orbit, proved by an explicit integral isometry of $T_\En$ that fixes $\delta$ and exchanges them (`computations/reports/coble_759-lift-1314-run.txt`), and only the pair $(12,13)$ is undecided: the orbit operation's three singleton orbits at cusp $5$ are not a proof either way, its acting family being uncertified for completeness and demonstrably incomplete here (sage-extensions `results/issue370-the-coble-root-orbits.md`) — the reflection route is closed, the widest witness search over all fourteen printed roots finds nothing to depth $10$ over $135\,571$ classes, and the pair's own direct-sum construction fails at index $2$ (`computations/reports/coble_760-orbit-witness-run.txt`, `computations/reports/coble_759-swap-1213-run.txt`); the contracted-curve route reads off the divisor @def:coble-descended-ramification, whose datum exists, but the recovery has no referent without the dictionary from the chamber's roots to curves of the Coble surface, which a search of the two sources the warning names finds nowhere — the marking is a definition to be made, not a citation (`computations/reports/coble_760-cusp-marking-search-run.txt`), and the cusp's symmetries do not supply it either (`computations/reports/coble_760-cusp-symmetry-run.txt`), @warn:coble-marking), @conj:restricted_ramification_semifan |
| **An equivariant triangulation compatible with the marked root** | @qst:equivariant_triangulation |
| **The position of the three Coble semifans** | @qst:semifan-poset-position |
| **Do the integral-affine data determine the stable limit** | @conj:classification-ia-data |
| **The semifan of a recognizable divisor** | @qst:recognizable-semifan |
| **The direct Coble theory** | @sec-status-ledger; @prob:coxeter-completeness, @prob:affine-realization, @prob:algebraic-extension, @prob:dlt-quotient, @prob:stable-proj, @prob:component-classification, @prob:direct-semifan (answered at the four $0$-cusps of $F_{\Co,2}$: @thm:coble-pair-semifan), @prob:restricted-semifan, @prob:autonomous-theorem, @prob:comparison-theorem |

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
