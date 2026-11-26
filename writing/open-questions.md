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
| **The forgetful degree from the sextic presentation** | The actual stack images are $\Gamma_\Co=\Orth^+(T_\Co)$ and $\Gamma_{\Co,2}=R_{\gent}\cap\Orth^+(T_\Co)$ by @thm:gamma-co-is-the-stack-monodromy. Their arithmetic forgetful map has degree $67\,456$. The particular labelled presentation has group $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$; its equality with the latter remains @qst:gamma-co-sign-is-realised. The invariant-marked stack has exactly the stable positive monodromy by @cor:coble-invariant-marking-monodromy. No universal-family equivalence with the plane presentation or degree for its coarse map follows from these image statements. |
| **Projective coverage and the moduli equivalence** | @prob:projective-coverage, @prob:cover-singular-equivalence, @prob:period-diagram |
| **Which divisibility-$2$ $0$-cusps lie over a Coble $0$-cusp** | @sec-enriques-coble-correspondence; the orbit map $\Phi$ is defined and equivariant (@thm:coble-strong-lifting), injective (@prop:cusp-map-injective) and not onto the primitive isotropic locus (@prop:cusp-map-not-onto); the **classes** of its image are exactly the $527$ nonzero isotropic classes of $A_{\ten}$ (@prop:cusp-map-surjective-on-classes), so the classes are settled and the open question is the number of $\Gamma_\En$-orbits of divisibility-$2$ primitive isotropic vectors carried by each class: $\Phi$ is onto the divisibility-$2$ locus exactly when that number is one (@prop:cusp-map-onto-criterion) |
| **Actual Coble monodromy against the stable group (research#780)** | The stable-group equality for the unmarked stack is refuted by @thm:gamma-co-is-the-stack-monodromy: its image is $\Orth^+(T_\Co)$, whose nontrivial discriminant quotient has order $46\,998\,591\,897\,600$. The stable positive image is instead the invariant-marked stack's group (@cor:coble-invariant-marking-monodromy); the chosen labelled presentation is not that stack. The degree-two group equals the positive restricted Enriques stabilizer. The separate reflection-generation and labelled-parameter-space questions remain. |
| **The distinguished elliptic fibration of the K3 cover** | @qst:distinguished-elliptic-fibration |
| **The home of the group action** | @qst:coble-mukai-naturality |
| **A20. The four arithmetic groups, and what is left of them** | The four-label arithmetic group equals $\Gamma^{\mathrm{Hdg}}_{\Co,2}=\Gamma^\theta_\Co=\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ (@thm:reflected-pair-integral-gluing, @prop:direct-eq-heegner, @cor:four-groups-decided); the congruence group is the union of the positive subgroup with its $s_\zeta$-coset. The actual reflected labelled datum, including the polarization, both involutions and the effective root, is integrally conjugate to the reflected AEGS marking (@thm:reflected-pair-integral-gluing); the unreflected pair has the wrong invariant ranks. The memberwise chamber-preserving direct group equals the four-label group when $\Pic=S_\Co$, and is strictly smaller at $b_\star$ (@qst:chamber-subscript-image): preservation of the actual chamber is equivalent to preservation of the Picard lattice, and the root reflection exhibited there sends an algebraic class outside it. Thus both the labelled extension and the memberwise comparison have been decided, without assuming the Picard rank of $b_\star$. Of the absorbed research#720 entries, (RI) and (INV) are decided false (@prop:kernel-exceeds-short-roots, @thm:chamber-subscript-is-a-condition), (D1) is decided false (@thm:d1-minus-four-half), and (REL) holds (@cor:coble-rel-section): the block sign and $-\id_{T_\Co}$ lie in $W(T_\Co)$ (@thm:coble-block-sign-in-w). The actual degree-two family monodromy equals the positive restricted Enriques stabilizer by @thm:gamma-co-is-the-stack-monodromy. The proof uses the actual two-label ambient stabilizer and paths of polarized objects, not memberwise chamber preservation of a special reflected direct-construction object. This determines the arithmetic group of the degree-two quotient; it does not identify the two moduli functors or prove a KSBA comparison. |

: {tbl-colwidths="[35,65]"}

## Stable limits and the compactification of $\fco$

| Unknown | Stated in |
|:---|:---|
| **KSBA versus semitoroidal** | @conj:coble-ksba-semitoroidal-morphism, @conj:ksba_semitoroidal_comparison, @conj:no_moduli_loss. The exact decorated cusp-five orbit partition is now $\{12\},\{13,14\}$ for the actual polarized monodromy, by @rmk:coble-root-orbits-cusp-five: the projected discriminant quadratic invariant separates $12$ from either other root even after cusp translations, and an explicit integral isometry fixing an oriented positive plane interchanges $13,14$. No provider stabilizer completeness assumption is needed. This decides the decorated orbit calculation (@thm:no-moduli-loss), not separation of stable pairs. The three roots cut the same restricted semifan cone (@thm:face-irrelevant-marking); the contracted anti-bicanonical curve recovers the Heegner root $[\pm\delta]$, not these $T_\Co$-roots (@prop:coble-marking-class-is-heegner). The original geometric question remains whether actual degenerations with distinct root decorations give distinct stable pairs, with the existence and identification of the relevant stable limits and comparison of their period maps proved. The transport lemma @lem:coble-root-separation-transport is conditional, including its decorated-boundary hypothesis (1); an identification of unmarked compactifications alone does not prove it. @conj:restricted_ramification_semifan. |
| **An equivariant triangulation compatible with the marked root** | @qst:equivariant_triangulation |
| **The position of the three Coble semifans** | @qst:semifan-poset-position |
| **The cones of the rational-curve divisor at the $0$-cusps of $F_{2d}$, $d\ge2$** | @qst:recognizable-semifan; the question whether a *recognizable* divisor can fail (W) is answered affirmatively by @lem:rcop-refinement-criterion at the unique $0$-cusp of $F_2$ --- $R_{\rcop}$ is recognizable ([@AE23, Thm. 10.11]) and the universal family of $(X,\eps R_{\rcop})$ does not extend over the Coxeter toroidal compactification (@prop:semifan-coarsening-extension), the restriction of the semifan to the unigonal hyperplane being the fan of [@ABE22, §4C] ([@AE23, Thm. 10.16]) whose cutting hyperplanes are not mirror traces --- and what remains is the same question at the $0$-cusps of $F_{2d}$ for $d\ge2$, where the explicit description is open in the literature: [@AE23, Intro.] states that "we have no explicit description, because the structure of a hypothetical 'tropical K3-rational curves pair' $(B,R^{\mathrm{rc}}_{\mathrm{trop}})$ is unknown", and calls such a description "an interesting open question"; no cone of $\mcf_{R_\rcop}$ is recorded in any source read there, and the computation needs the stable limit of the pair over a cone, not an operation of `sage-extensions` (@rmk:missing-stable-limit); the Coxeter fan the comparison needs is printed at the $F_2$ cusp, which is also the fan at every cusp with $d=p^2$ ($k=1$); the unigonal locus meets only the cusp with $p_*=1$ (@lem:unigonal-locus-cusp-support), so the ABE22 identification is unavailable at the others; the boundary lattice at every cusp with $p_*>1$ is $\langle-2d/p_*^2\rangle\oplus U\oplus E_8(-1)^{\oplus2}$ (@lem:cusp-lattice-p-greater-one), not the $\langle-2d/p_*\rangle$ printed in [@AE23, §10C]; for $k=d/p_*^2\ge2$ it is the unigonal cusp lattice of $F_{2k}$, whose diagram is not printed, whose fan is not the product of the printed $F_2$ fan with a line (@lem:k-greater-one-fan-not-prism), and whose reflection group is not a lattice, so that the comparison there is a semifan and not a fan; the boundary lattice is two-reflective exactly at $k=1$, i.e. at $p_*=\sqrt d$ (@lem:k-not-two-reflective), so the unigonal cusp of $F_{2d}$ for $d\ge2$ also has non-reflective boundary lattice; every $p_*>1$ cusp shares a $1$-cusp with the unigonal cusp (@lem:p-cusp-meets-unigonal), whose lattice is $\langle-2k\rangle\oplus E_8(-1)^{\oplus2}$ (@lem:shared-one-cusp-lattice), so the two semifans satisfy the compatibility clause of [@AE23, Def. 5.11] there; an inventory of the cones such a computation would label is printed only at the $F_2$ cusp (@thm:cone-inventory-printed, [@AET23, Def. 4.2, Thm. 4.3, Lemmas 4.4--4.5]); what is decided beyond $d=1$ is the constraint @lem:generalized-unigonal-constraint, which by @lem:cusp-census and @lem:k-one-two-sharp forces $(\mathrm H_p)$ to fail at every $p_*>1$ cusp except the unit classes of $F_{N^2}$ and $F_{2N^2}$, $N\ge2$, those being the cusps with $k=d/p_*^2\in\{1,2\}$ where the generalized-unigonal hyperplane is itself a root mirror and neither criterion fires, so that $(W)$ is decided at every other $p_*>1$ cusp (conditionally, through $(\mathrm H_p)$) and open exactly at those classes, on the stable limit of $(X,\eps R_{\rcop})$ over a cone there (@rmk:missing-stable-limit) |
| **The direct Coble theory** | @sec-status-ledger; @prob:coxeter-completeness, @prob:affine-realization, @prob:algebraic-extension, @prob:dlt-quotient, @prob:stable-proj, @prob:component-classification, @prob:direct-semifan (answered at the four $0$-cusps of $\bD(T_\Co)/R_{\gent}$: @thm:coble-pair-semifan; the $0$-cusps of $F_{\Co,2}$ map onto these four, and whether one of them splits is open, @lem:d2-degree-two-base(3)), @prob:restricted-semifan, @prob:autonomous-theorem (**open in clauses two and three and in the last piece of clause one**; decided there: the unpolarized open identification is published [@DK13, Prop. 3.2]; no $(-2)$-Heegner divisor of $T_\Co$ is met (@thm:direct-period-misses-root-walls) and one $(-4)$-divisor is (@thm:direct-period-meets-minus-four); the level sets of both discriminant forms are computed (@rmk:coble-discriminant-levels); the polarized refinement is decided, $-\id_{T_\Co}$ being in the group and in its $\Orth^+$-half (@lem:minus-id-in-labeled-centralizer(2)), in no loop (@thm:no-loop-carries-the-sign) and in the orbifold group through the isotropy (@thm:sign-is-isotropy), so that @qst:b25-sign-holonomy asked the coarse-versus-stacky distinction; clause three has the cusps and one cusp lattice $I_{1,8}(2)$, computed at the four public representatives (`computations/reports/coble_671-four-cusps-run.txt`), and owes the four folded Coxeter diagrams, which need the stabilizer images $\Gamma_e\le\Orth(I_{1,8}(2))$ (@prob:coxeter-completeness) and the relevance marking (@warn:coble-marking); at a labelled cusp the image is the stabilizer of one class of $A_K$ and contains every reflection of the cusp lattice, so the labelled chamber there is the unpolarized chamber and the diagram is the nine-node one (@thm:labelled-chamber-is-the-unpolarized-chamber), while the transport of that class to each of the four published representatives is still to be made; clause two owes the semitoroidal identification and waits on the direct dlt and stable-model theorem (@sec-coble-dlt); still open in clause one: which $(-4)$-divisors the image meets), @prob:comparison-theorem (**open**: the canonical isomorphism at the head of its statement and clauses 2 to 6; clause 1 is @cor:four-groups-decided, clause 4 waits on the folded diagrams, clause 5 on the discerned ramification divisor and the marking (@def:coble-descended-ramification, @warn:coble-marking), clause 6 on clause two of Target A) |

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


The effective plane-presentation family is now constructed with its resultant square-root line (@lem:d2-unpolarised-family). Its integral monodromy has index at most two in the stable positive group, and the remaining question for this specified lift is the central sign (@thm:gamma-co-is-stable). The cover-retaining plane-presentation stack and the nonzero-equation labelled base have full stable integral image; neither is the unmarked universal stack.
