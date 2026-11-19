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
| **Which divisibility-$2$ $0$-cusps lie over a Coble $0$-cusp** | @sec-enriques-coble-correspondence; the orbit map $\Phi$ is defined and equivariant (@thm:coble-strong-lifting), injective (@prop:cusp-map-injective) and not onto (@prop:cusp-map-not-onto), and a class is in its image exactly when it is orthogonal to a $(-2)$-vector of the $\Gamma_\En$-orbit of $k$; which divisibility-$2$ classes these are is open |
| **The monodromy group of the Coble family against the stable group** | @conj:gamma-co-stable, @qst:sextic-group-comparison; $\Gamma_\Co$ is the monodromy of the family of unpolarized Coble surfaces (@def:gamma-co-groups(1)), and the strong lifting for it is @prop:gamma-co-strong-lifting, which holds exactly when $\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$ and therefore rests on @conj:gamma-co-stable; the sign half of that inclusion is unconditional (@lem:monodromy-is-spinor-positive) and the discriminant half is governed by the action on $A_M$, hence by the ten exceptional classes (@cor:gamma-co-lifting-criterion, and on $A_{S_\Co}$ for @cor:construction-monodromy); the containment holds outright for the monodromy of the lattice polarized family, which is a different group [@DK13, printed p. 512] |
| **The distinguished elliptic fibration of the K3 cover** | @qst:distinguished-elliptic-fibration |
| **The home of the group action** | @qst:coble-mukai-naturality |
| **A20. The four arithmetic groups, and what is left of them** | decided: $\Gamma^{\mathrm{dir}}_{\Co,2} = \Gamma^{\mathrm{Hdg}}_{\Co,2} = \Gamma^\theta_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ (@prop:direct-eq-heegner), the last as the union of that group with its $s_\zeta$-coset (@cor:four-groups-decided); the geometric entry is the direct group in the orbifold sense (@thm:sign-is-isotropy) with no loop carrying the sign (@thm:no-loop-carries-the-sign), and $G_3$, $G_4$ of research#720 are settled in @cor:g3-g4-decided. Open: (i) whether the chamber subscript of @def:direct-group changes the image at a member whose Picard lattice is larger than $S_{\Co,b}$ — it is a genuine condition there (@thm:chamber-subscript-is-a-condition), it is linear in the period (@lem:chamber-condition-is-period-condition) and it is implied by preserving the Picard lattice (@cor:chamber-preserved-by-picard-stabilizer), and the input it waits on is an explicit $\Pic(\widehat X_{b_\star})$ (@qst:chamber-subscript-image); (ii) the labelled comparison, research#664. Of the absorbed research#720 entries, (RI) and (INV) are decided false (@prop:kernel-exceeds-short-roots, @thm:chamber-subscript-is-a-condition), (D1) is decided false (@thm:d1-minus-four-half), and (REL) is met at @qst:gamma-co-generators(3): the block sign and $-\id_{T_\Co}$ lie in $W(T_\Co)$ (@thm:coble-block-sign-in-w) and the block-diagonal section exists (@cor:coble-rel-section) |

: {tbl-colwidths="[35,65]"}

## Stable limits and the compactification of $\fco$

| Unknown | Stated in |
|:---|:---|
| **KSBA versus semitoroidal** | @conj:coble-ksba-semitoroidal-morphism, @conj:ksba_semitoroidal_comparison, @conj:no_moduli_loss, @thm:no-moduli-loss (the stable quotient $\bD(T_\Co)/\Gamma_{\Co,2}$ separates the $\Gamma_{\Co,2}$-orbits of marked roots at every marked cusp, and its KSBA-boundary form is @conj:no_moduli_loss's, whose one open step is the boundary Torelli statement of research#760 --- an isomorphism of stable pairs over the cusp induces an element of $\Gamma_{\Co,2}$ carrying one marked root to the other, and the converse --- the theorem being its quotient-side half; no face of the restricted semifan carries the marking: every admissible $T_\Co$-root at the marked cusps is irrelevant, so all of them cut one cone, @thm:face-irrelevant-marking; the $\Gamma_{\Co,2}$-orbits at cusp $5$ are decided and there are two of them: roots $13$ and $14$ are one orbit, by an explicit integral isometry of $T_\En$ that fixes $\delta$ and exchanges them and preserves the two summands of $A_{T_\En}$, so it lies in $\gent = \rho^{-1}(M)$ (`computations/reports/coble_759-lift-1314-run.txt`, `computations/reports/coble_760-gent-membership-run.txt`), and Sterk's label $12$ is in another, by the coset computation that reduces the pair to one subspace orbit of $A_{T_\Co}$ and exhausts it without the target, the pair $(13,14)$ serving as a positive control (`computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`, @thm:face-irrelevant-marking(3)), on the stabilizer family the library labels untrusted, whose own construction is the operation that step waits on (`computations/reports/coble_760-vector-stabilizer-certification-run.txt`); the hypothesis of the conjecture is therefore met at cusp $5$, it is not vacuous, and what is open there is the identification step and not the orbit; the weaker class reading agrees and is decided too, the shift by a multiple of $\eta_5$ being removed by the shear $s_{r_{13}+\eta_5}s_{r_{13}}$ in $\Gamma_{\Co,2}$ and the two odd targets $\pm(r_{13}\pm\eta_5)$ being themselves unreachable (`computations/reports/coble_759-class-reading-1213-run.txt`); the contracted-curve route is closed: @prop:coble-marking-class-is-heegner proves that the vanishing class of the node is the Heegner vector --- primitive of square $-2$ by adjunction, anti-invariant under $\iota_\Co$ because $\iota_\Co$ acts on the vanishing cycle as the antipodal map, hence a class of $T_\En$, and orthogonal to the period lattice $T_\Co$ of the resolved K3 cover, hence $\pm\delta$ --- so the class of the contracted anti-bicanonical curve is the same $[\pm\delta]$ at every degeneration at a marked cusp (@def:coble-marking-dictionary, @rmk:coble-marking-dictionary-scope); that closes the reading in which the marked root is that class, and it leaves the $T_\Co$-root reading where it was, which is what @conj:no_moduli_loss states: no $T_\Co$-root is the class of a curve of $\bar S$, the roots $12$, $13$, $14$ at cusp $5$ being Sterk's labels for the three $T_\Co$-roots against label $11$ for the curve, and the hypothesis of the conjecture is met at cusp $5$ on one decision and not unconditionally: $13$ and $14$ are one $\Gamma_{\Co,2}$-orbit by an explicit integral isometry, while the inequivalence of $12$ and $13$ is item 1 of research#759, computed on the page only over the subgroup the family `vector_stabilizer_generators` generates and so decided modulo that family (sage-extensions#603, `computations/reports/coble_759-vector-stabilizer-absence-run.txt`); so the conjecture is not vacuous, its cusp-$5$ instance is conditional on that family, and the two marking conventions and what each leaves of the statement are @rmk:coble-marking-conventions, and the transport to the KSBA boundary is stated and proved as @lem:coble-root-separation-transport, whose only missing hypothesis is the comparison itself (@rmk:coble-transport-hypotheses) and whose unpolarized reading is refuted at cusp $5$ by the explicit isometry of $T_\Co$ (@rmk:coble-transport-failure); the marking's identity is not what is open, since @thm:coble-cusp-admissibility(2) and @prop:marking-line-no-coble-lift fix it: what no source read supplies is the pairing of a *simple root of the chamber* with a curve (`computations/reports/coble_760-cusp-marking-search-run.txt`), and no operation of the library supplies a pair of stable pairs to compare, no name in its 318 files referring to a stable pair, a semifan or a marked root, `Coble.rank_ten_diagram().stable_pairs()` raising `AttributeError` (`computations/reports/coble_759-limit-pair-call-probe-run.txt`), and the comparison this result feeds, @conj:ksba_semitoroidal_comparison, names this result among its own inputs, so the two cannot discharge each other; and the cusp's symmetries do not supply it either (`computations/reports/coble_760-cusp-symmetry-run.txt`), @warn:coble-marking), @conj:restricted_ramification_semifan |
| **An equivariant triangulation compatible with the marked root** | @qst:equivariant_triangulation |
| **The position of the three Coble semifans** | @qst:semifan-poset-position |
| **The cones of the rational-curve divisor at the $0$-cusps of $F_{2d}$, $d\ge2$** | @qst:recognizable-semifan; the question whether a *recognizable* divisor can fail (W) is answered affirmatively by @lem:rcop-refinement-criterion at the unique $0$-cusp of $F_2$ --- $R_{\rcop}$ is recognizable ([@AE23, Thm. 10.11, printed p. 36]) and the universal family of $(X,\eps R_{\rcop})$ does not extend over the Coxeter toroidal compactification (@prop:semifan-coarsening-extension), the restriction of the semifan to the unigonal hyperplane being the fan of [@ABE22, §4C, printed p. 14] ([@AE23, Thm. 10.16, printed p. 38]) whose cutting hyperplanes are not mirror traces --- and what remains is the same question at the $0$-cusps of $F_{2d}$ for $d\ge2$, where the explicit description is open in the literature: [@AE23, Intro., printed p. 3] states that "we have no explicit description, because the structure of a hypothetical 'tropical K3-rational curves pair' $(B,R^{\mathrm{rc}}_{\mathrm{trop}})$ is unknown", and calls such a description "an interesting open question"; no cone of $\mcf_{R_\rcop}$ is recorded in any source read there, and the computation needs the stable limit of the pair over a cone, not an operation of `sage-extensions` (@rmk:missing-stable-limit); the Coxeter fan the comparison needs is printed at the $F_2$ cusp, and by @lem:cusp-lattice-p-greater-one it is the same fan at the cusps with $d=p^2$ ($k=1$); at the cusps with $k\ge2$ covered by that lemma the boundary lattice is $\langle-2k\rangle\oplus U\oplus E_8(-1)^{\oplus2}=\langle-2d/p_*^2\rangle\oplus U\oplus E_8(-1)^{\oplus2}$, not the $\langle-2d/p_*\rangle$ printed in [@AE23, §10C, printed p. 38], and it is the unigonal cusp lattice of $F_{2k}$, whose diagram is not printed and whose fan is not the product of the printed $F_2$ fan with a line (@lem:k-greater-one-fan-not-prism); at the other $p_*>1$ cusps neither the fan nor the boundary lattice is settled here, and an inventory of the cones such a computation would label is printed only at the $F_2$ cusp (@thm:cone-inventory-printed, [@AET23, Def. 4.2, Thm. 4.3, Lemmas 4.4--4.5, printed p. 22]); and the $p_*>1$ cusp of @lem:cusp-lattice-p-greater-one shares a $1$-cusp with the unigonal cusp (@lem:p-cusp-meets-unigonal), whose lattice is $\langle-2k\rangle\oplus E_8(-1)^{\oplus2}$ (@lem:shared-one-cusp-lattice), so the two semifans satisfy the compatibility clause of [@AE23, Def. 5.11, printed p. 14] there |
| **The direct Coble theory** | @sec-status-ledger; @prob:coxeter-completeness, @prob:affine-realization, @prob:algebraic-extension, @prob:dlt-quotient, @prob:stable-proj, @prob:component-classification, @prob:direct-semifan (answered at the four $0$-cusps of $F_{\Co,2}$: @thm:coble-pair-semifan), @prob:restricted-semifan, @prob:autonomous-theorem (**open in clauses two and three and in the last piece of clause one**; decided there: the unpolarized open identification is published [@DK13, Prop. 3.2, printed p. 513]; no $(-2)$-Heegner divisor of $T_\Co$ is met (@thm:direct-period-misses-root-walls) and one $(-4)$-divisor is (@thm:direct-period-meets-minus-four); the level sets of both discriminant forms are computed (@rmk:coble-discriminant-levels); the polarized refinement is decided, $-\id_{T_\Co}$ being in the group and in its $\Orth^+$-half (@lem:minus-id-in-direct-group(2)), in no loop (@thm:no-loop-carries-the-sign) and in the orbifold group through the isotropy (@thm:sign-is-isotropy), so that @qst:b25-sign-holonomy asked the coarse-versus-stacky distinction; clause three has the cusps and one cusp lattice $I_{1,8}(2)$, computed at the four public representatives (`computations/reports/coble_671-four-cusps-run.txt`), and owes the four folded Coxeter diagrams, which need the stabilizer images $\Gamma_e\le\Orth(I_{1,8}(2))$ (@prob:coxeter-completeness) and the relevance marking (@warn:coble-marking); at a labelled cusp the image is the stabilizer of one class of $A_K$ and contains every reflection of the cusp lattice, so the labelled chamber there is the unpolarized chamber and the diagram is the nine-node one (@thm:labelled-chamber-is-the-unpolarized-chamber), while the transport of that class to each of the four published representatives is still to be made; clause two owes the semitoroidal identification and waits on the direct dlt and stable-model theorem (@sec-coble-dlt); still open in clause one: which $(-4)$-divisors the image meets), @prob:comparison-theorem (**open**: the canonical isomorphism at the head of its statement and clauses 2 to 6; clause 1 is @cor:four-groups-decided, clause 4 waits on the folded diagrams, clause 5 on the discerned ramification divisor and the marking (@def:coble-descended-ramification, @warn:coble-marking), clause 6 on clause two of Target A) |

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
