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
Each entry states the unknown, what is established around it, what would settle it, and the block or section that owns it.
The owning block is the statement of record; this page restates nothing and adds no mathematics.
Each entry also names its work unit in the [issue tree](https://github.com/dzackgarza/research/issues/641), which holds the acceptance condition.

The register excludes three kinds of gap that the issue tree also holds: a standard proof not yet attached to a standard theorem, coordinate work such as an explicit matrix, and a repair to the text.
A question that a finite derivation or computation decides is listed in the last section, apart from the research unknowns.

An entry leaves this page when its owner holds a proof, a disproof, or a computation record, and the pages that cite the open form are updated.
:::

## Category theory

**Inverting the hyperbolic stabilization.**
Whether the hyperbolic stabilization $S = F_{H(R)}$ of $\mathbf{Lat}_R$ can be inverted into a pointed $\infty$-category: a $\mcc$ with $\iota\colon \mathbf{Lat}_R^{\simeq}\to\mcc^{\simeq}$ and $\iota\circ S\simeq\Sigma\circ\iota$.
Stated in @sec-open-statements.
@thm:invertible-summand sharpens it: on $\mathbf{Lat}_R$ itself, invertibility and a nonzero Witt class are incompatible.
Issue [#682](https://github.com/dzackgarza/research/issues/682).

**Monoidal structures with an invertible object of nonzero Witt class.**
Whether any symmetric monoidal structure on a category built from $\mathbf{Lat}_R$, other than the orthogonal sum, has an invertible object $M$ with $[M]\neq 0$ in $W(R)$.
Stated in @sec-open-statements, sharpened by the same theorem.
Issue [#682](https://github.com/dzackgarza/research/issues/682).

**The discriminant construction as a functor on Poincaré complexes.**
Whether the discriminant construction factors through the $\epsilon$-quadratic Poincaré complexes over $\bZ$, and through which functor.
Stated in @sec-open-statements.
Issue [#682](https://github.com/dzackgarza/research/issues/682).

**A canonical universe for the equality predicate.**
The equality predicate of the foundations part is conditional on a choice of higher category $W$ over which the identifications are taken; a canonical choice of $W$, and hence of $\operatorname{Way}$, is not settled.
Stated in @sec-equality-universe.

**$K_0$ of the $2$-elementary forms.**
@thm:2elementary-decomposition presents the monoid of $2$-elementary forms; imposing its relations freely on the free commutative monoid gives the group $\bZ\times\bZ/4\bZ$.
Whether this group is the Grothendieck group $K_0$ of the category of $2$-elementary quadratic forms is not known.
The question is recorded in the dissertation, `sections/1-part-combinatorial/2-chapter-lattice-theory/300-classification.md`.
Issue [#683](https://github.com/dzackgarza/research/issues/683).

## Lattice theory and hyperbolic reflection groups

**Vector-level transitivity for $\latI_{1,8}$.**
@prop:rank-nine-line-transitivity proves that $\Orth^+(\latI_{1,8})$ is transitive on primitive isotropic lines.
Transitivity on primitive isotropic vectors is open: in signature $(2,9)$ the element $-\id$ lies in $\Orth^+$ and supplies the sign, and in signature $(1,8)$ it does not.
Stated after that proposition in @sec-embeddings-overlattices.
Issue [#659](https://github.com/dzackgarza/research/issues/659).

**The reflection subgroup of each Sterk fundamental domain.**
Sterk's domains for the five cusps of $\fentwo$ have $12, 10, 12, 11, 14$ walls; Vinberg's algorithm on the hyperbolic quotients returns ten walls in each case, and the quotients for cusps $2$ to $5$ are mutually isometric.
The missing datum is the subgroup of the quotient's reflection group induced by the stabilizer of each cusp in the arithmetic group of $F_{\En,2}$, and the index is a covolume ratio that no Euler characteristic supplies in odd dimension.
@qst:sterk-reflection-subgroup and @qst:sterk-ideal-vertices.
Issue [#654](https://github.com/dzackgarza/research/issues/654).

**Global questions on hyperbolic Coxeter diagrams.**
Open in the literature, not only here: the cost of finding the maximal parabolic subdiagrams of a Coxeter diagram (@qst:maximal-parabolic-complexity), Galois invariance of their count (@conj:galois-invariance-parabolics), the growth of that count with the rank (@qst:parabolic-count-growth), arithmeticity read from the diagram (@qst:arithmeticity), exact covolumes in odd dimension (@qst:exact-covolume), and a regularized theta series for an indefinite lattice (@qst:regularized-theta).
Issue [#660](https://github.com/dzackgarza/research/issues/660).

## The Coble arithmetic group and its cusps

**The number of $0$-cusps of $\fco$.**
The number of $\Gamma_\Co$-orbits of primitive isotropic vectors of $T_\Co$.
Established: at least $527$, one for each nonzero isotropic class of $A_{T_\Co}$, with the exact count an index of stabilizers (@prop:coble-stable-cusp-lower-bound); the same number for the discriminant kernel (@prop:discriminant-kernel-orbits); on the finite side, $A_{T_\Co}$ has $528$ nonzero isotropic classes and the finite group acts with orbit lengths $[1,2,120,135,270]$ (@thm:coble-heegner-finite-orbits, whose orbit lengths are still an unverified computation, see the last section).
No upper bound is known.
The Eichler criterion does not apply because $T_\Co$ contains no copy of $U$.
The open content is the lifting theorem @prob:cusp-lifting: whether the image of the integral parabolic stabilizer is the finite group whose orbits were computed.
Issues [#644](https://github.com/dzackgarza/research/issues/644) and [#667](https://github.com/dzackgarza/research/issues/667).

**The number of $1$-cusps of $\fco$.**
The number of $\Gamma_\Co$-orbits of primitive isotropic planes of $T_\Co$.
Established: $\Orth^+(T_\Co)$ is transitive (@thm:plane-transitivity-tco).
For $\Gamma_\Co$ nothing is known; the candidate invariant is the subspace $\bar J\subseteq A_{T_\Co}$ a plane cuts out, and $A_{T_\Co}$ has $23\,715$ totally isotropic planes, so the invariant is not constant, but whether it separates orbits is undecided.
Stated in @sec-open-problems.
Issue [#645](https://github.com/dzackgarza/research/issues/645).

**A generating set of the group $\Gamma_\Co$.**
No generating set of $\Gamma_\Co = \Orth^+(T_\Co)\cap\ker\rho_{T_\Co}$ is known.
Established: the reflections in the $(-2)$-vectors of $T_\Co$ lie in $\Gamma_\Co$; the stabilizer of the degree-$2$ polarization in $\Orth(S_\En)$ is generated by nine reflections (@prop:polarization-stabilizer-enriques).
The obligation is a Vinberg-type theorem: an explicit reflective set together with finitely many further isometries that generate $\Gamma_\Co$ (@prob:coxeter-completeness).
Issue [#646](https://github.com/dzackgarza/research/issues/646).

**Equality of the four arithmetic groups.**
Whether $\Gamma_\Co$, the Coble-side centralizer group $\Gamma^\theta_\Co$, the Heegner group $\Gamma^{\mathrm{Hdg}}_{\Co,2}$, and the direct group of the projective construction are one group (@prob:group-identification, @sec-four-groups).
Established in @sec-gamma-co-comparison: $\Gamma^\theta_\Co$ and $\Gamma^{\mathrm{Hdg}}_{\Co,2}$ contain $\Gamma_\Co$ as the kernel of their action on $A_{T_\Co}$, with index at most $\abs{W(E_8)}$ (@prop:gamma-co-in-heegner-group, @prop:gamma-co-in-theta-centralizer); the congruence group strictly contains $\Gamma_\Co$.
Open: strictness of the two other inclusions, which is a computation in a finite group once group generators of $\gent$ exist; the comparison with the direct group; and, from the same circle, whether $\ker\rho_{T_\Co}$ is generated by the $(-2)$-reflections of $T_\Co$, the relation statement for a section of $\rho_{T_\Co}$, invariance of the model-effective root arrangement under a general stabilizer, and monodromy maximality, whose statements of record are in `computations/reports/smw0_accepted-proofs.md`.
Issues [#647](https://github.com/dzackgarza/research/issues/647), [#663](https://github.com/dzackgarza/research/issues/663), [#720](https://github.com/dzackgarza/research/issues/720).

**Which quotient of $D(T_\Co)$ is the Coble moduli space.**
$\fco$ is defined as an open subset of $D(T_\Co)/\Orth^+(T_\Co)^*$, and the moduli space of ten-nodal sextics is a quotient by $\Gamma_{10A_1}$, which contains $\Orth^+(T_\Co)^*$ and may be strictly larger.
@qst:sextic-group-comparison.

**Labeled Coble rigidity.**
Whether two labeled tuples $(L_{K3}, I_\Co, I_{\mathrm{dP}}, H, \alpha, \mathcal C)$ from the projective construction are conjugate under an element of $\Orth(L_{K3})$ preserving the labels (@prob:coble-rigidity).
This is stronger than uniqueness of the primitive embedding of $S_\Co$, and without it no direct period quotient is coordinate-independent.
Established: the unlabelled comparison of the two polarizations, and the restriction @cor:no-del-pezzo-involution-coble-cover on the del Pezzo slot.
Open: the chamber clause, which rests on the nefness of the Coble polarization class, a premise no source here supplies (@prob:effective-cone-agreement); the identification of the construction's involution pair with the reflection twist (@prob:twist-identification); and the saturation question of @rmk:a21-open.
Issue [#664](https://github.com/dzackgarza/research/issues/664).

**Projective coverage and the moduli equivalence.**
Whether the quotient of the open nodal invariant $(4,4)$ locus by the full centralizer is the complete direct moduli stack (@prob:projective-coverage); whether the resolved-cover and singular-pair moduli stacks are equivalent compatibly with base change and automorphisms (@prob:cover-singular-equivalence); and whether the period diagram relating the direct and Heegner constructions commutes (@prob:period-diagram).
Issues [#665](https://github.com/dzackgarza/research/issues/665) and [#666](https://github.com/dzackgarza/research/issues/666).

**The Enriques-to-Coble cusp correspondence.**
Three statements of @sec-enriques-coble-correspondence are open.
Injectivity of the $0$-cusp orbit map is reduced by @prop:cusp-map-separates-mod-two to one class in $T_\Co/2T_\Co$, where a subgroup-descent step remains.
Surjectivity onto the divisibility-$2$ locus needs a statement about the $(-2)$-vectors in the $\Gamma_\En$-orbit of the cusp vector.
The strong form of the correspondence, equivariance with a comparison of stabilizers, needs a homomorphism of arithmetic groups that only pointwise orbit compatibility supports so far.
Issue [#658](https://github.com/dzackgarza/research/issues/658).

**The Coble cusps in the morphism chain.**
Two conjectures of @sec-cusp-correspondence-morphism-chain: that the Coble cusps correspond, under the extension to the degree-$(2,2,0)$ space, to the cusp $U\oplus E_8^2 = (18,0,0)_1$; and that the Coble $0$-cusp is Sterk's cusp $2$.
The second implies the independently stated claim that Coble degenerations are of $\mathbb D^2$-type, and that consistency check has not been exercised.
Issue [#672](https://github.com/dzackgarza/research/issues/672).

**The distinguished elliptic fibration of the K3 cover.**
The two $\Orth^+(S_\Co)$-orbits of primitive isotropic vectors of $S_\Co$ are elliptic fibration classes of the K3 cover with the same boundary invariants $(9,9,1)$.
Which class the Coble structure distinguishes, and how the pair of maximal parabolic subdiagrams matches the boundary data of the degree-$2$ polarized space, is open.
Stated in @sec-open-problems.

**The home of the group action.**
Whether the Coble--Mukai lattice $\CM(S)$ rather than $S_\Co$ is the natural home for the action of $\Gamma_\Co$, and how the two are related (@qst:coble-mukai-naturality).
The odd part of the discriminant of the boundary configuration, invisible to the $2$-elementary invariants of $S_\Co$, is where a difference would show.
Issue [#673](https://github.com/dzackgarza/research/issues/673).

## Stable limits and the compactification of $\fco$

**Root-orbit uniqueness under $\gent$.**
Namikawa gives uniqueness of the root orbit for the full Enriques group; the polarized problem needs it for the finite-index subgroup $\gent$, where it is not settled (@qst:coble_root_orbit_uniqueness).
Every statement in the KSBA branch below depends on it.
Issue [#648](https://github.com/dzackgarza/research/issues/648).

**The quarter singularity.**
@conj:coble_quarter_singularity states the local model $\tfrac14(1,1)$ at an $A_1$-node of the K3 cover fixed by the involution.
It is the input awaited by the slc and ampleness verifications of the stable model.
Issue [#649](https://github.com/dzackgarza/research/issues/649).

**KSBA versus semitoroidal.**
@conj:ksba_semitoroidal_comparison and @conj:no_moduli_loss identify the KSBA compactification of $\fco$ with a semitoroidal one and assert that no moduli are lost.
Open on four counts: root-orbit uniqueness above; the restriction identity for the ramification semifan (@conj:restricted_ramification_semifan); the injection from a stable quotient to its marked root; and an explicit cusp computation.
Issue [#650](https://github.com/dzackgarza/research/issues/650).

**Admissibility of Coble roots at a cusp.**
@qst:coble_cusp_admissibility asks for the test deciding which roots are admissible at each cusp; Sterk cusps $3$ and $5$ are the delicate cases.
The boundary dictionaries of the preliminary KSBA work stay unverified without it.
Issue [#651](https://github.com/dzackgarza/research/issues/651).

**An equivariant triangulation compatible with the marked root.**
@qst:equivariant_triangulation.
Without it the marked-root prescription is a principle and not a model.
Issue [#655](https://github.com/dzackgarza/research/issues/655).

**Is $\mch^*_{10A_1}$ empty, and where do the three semifans sit.**
@qst:coble-arrangement-empty decides whether the GIT compactification of ten-nodal sextics is the Baily--Borel compactification or a semitoroidal model strictly between.
A reduction is recorded: the roots of the sextic locus have divisibility $1$, and the remaining case is the divisibility-$2$ roots whose hyperplane meets $D(T_\Co)$ properly.
@qst:semifan-poset-position, the position of the Coxeter, KSBA and Looijenga semifans relative to one another, depends on it.
Issues [#652](https://github.com/dzackgarza/research/issues/652) and [#653](https://github.com/dzackgarza/research/issues/653).

**The direct Coble theory.**
The research report states the required theorems of an autonomous compactification, and its ledger @sec-status-ledger records each as not established:
Coble Vinberg and root completeness at every polarized $0$-cusp (@prob:coxeter-completeness), where the four candidate wall-slice arrangements have $1,3,3,9$ maximal parabolic faces and these counts disagree with the finite-shadow orbit counts;
the degeneration chain, which stands or falls together: integral-affine realization (@prob:affine-realization), algebraic extension of the two involutions to divisor models (@prob:algebraic-extension), the dlt quotient (@prob:dlt-quotient), the stable contraction (@prob:stable-proj), and the component classification (@prob:component-classification);
the direct semifan and the semitoroidal restriction (@prob:direct-semifan, @prob:restricted-semifan), for which the report lists seven statements needed before intersecting the AEGS semifans is a theorem;
and the two targets, the autonomous theorem (@prob:autonomous-theorem) and the comparison with the Enriques Heegner divisor (@prob:comparison-theorem), where the first does not imply the second.
The strategy lemmas of the report's three routes are stated at their own labels there.
Issues [#668](https://github.com/dzackgarza/research/issues/668) to [#671](https://github.com/dzackgarza/research/issues/671), [#674](https://github.com/dzackgarza/research/issues/674).

## The degree-$2$ Enriques comparison

**The classifying map of $\fentwo$.**
Three conjectures: the Enriques involution extends over the Noether--Lefschetz closure (@conj:enriques_involution_extension), the classifying map $\phi$ from its normalization to the KSBA compactification is finite (@conj:classifying_map_finite), and $\phi$ is an isomorphism (@conj:classifying_map_isomorphism).
The dissertation states the finiteness as a theorem, and its proof rests on a semifan comparison whose argument assumes its conclusion through a notion of maximal degeneration introduced for the purpose, `sections/3-part-main-theorem/6-chapter/600-finite-coarsening.md`.
Issue [#680](https://github.com/dzackgarza/research/issues/680).

**Descent of the semitoroidal data.**
@conj:descent_semitoroidal_data_En2: the ramification semifan restricts to the normalized Noether--Lefschetz closure and folds under the involution.
The source tags it as a proposition with no proof; the dissertation's version, `sections/3-part-main-theorem/6-chapter/500-descent-semitor.md`, takes the restriction as formal, and @warn:restrict-semifan lists the statements that formality omits.
Issue [#681](https://github.com/dzackgarza/research/issues/681).

## The other families

**The families $F_{\Co,n}$ for $2\leq n\leq 10$.**
Three conjectures of @sec-coble-families-research-program: the Baily--Borel boundaries of all ten families are computable by the $n=1$ techniques; the ramification locus of the K3 cover is a recognizable divisor, which would give a semitoroidal compactification; and the resulting semifans refine or coarsen the Coxeter fans at the cusps.
A constraint on the second and third: the Picard lattices of the rows $n=7,8,9$ are not reflective (@sec-reflective-two-elementary), so for those three families there is no finite Coxeter diagram and no Coxeter fan, and the K3 covers have infinite automorphism group by @thm:k3-automorphism-sequence.
What replaces the reflection data there is open.
Issues [#675](https://github.com/dzackgarza/research/issues/675) and [#676](https://github.com/dzackgarza/research/issues/676).

**Nodal Enriques surfaces.**
The conjecture of @sec-nodal-enriques-moduli-program: the orbits of isotropic vectors and planes under $\Orth(T_\Nod)$ can be classified, and the embedding into the degree-$2$ Enriques space gives the KSBA compactification, its dlt models, and the integral-affine structures.
$T_\Nod$ is not $2$-elementary, and the Sterk--Nikulin orbit apparatus of this book assumes $2$-elementarity, so the classification of the boundary needs orbit techniques the book does not have.
Issue [#686](https://github.com/dzackgarza/research/issues/686).

**Halphen surfaces of index $2$.**
Two conjectures of @sec-halphen-index-2-moduli-program: the Coble-line lattices give period domains for index-$2$ Halphen surfaces with an $I_{2k}$ fibre whose stable-pair compactifications are semitoroidal; and the unique multiple fibre supplies the recognizable divisor that the first conjecture needs.

**The Dolgachev--Zhang classification.**
A Coble surface has finitely many smooth rational negative curves up to automorphism.
Classifying all surfaces with this property is open in the source, as recorded beside @qst:coble-mukai-naturality.
Issue [#677](https://github.com/dzackgarza/research/issues/677).

## The dissertation

**Do the integral-affine data determine the stable limit.**
The conjecture `conj:classification-ia-data` of `sections/3-part-main-theorem/7-chapter/800-divisor-models.md`: for a fixed monodromy invariant, the combinatorial type of the dual complex with its integral-affine data determines the KSBA stable limit, and the type is locally constant in families.
Only the converse, from the divisor model to the data, is established.
The forward direction is the hinge of the divisor-model method: without it the computed $B(\lambda)$ is a candidate for the limit.
Issue [#678](https://github.com/dzackgarza/research/issues/678).

**The semifan of a recognizable divisor.**
Describing the semifan of a recognizable divisor $R$ is open in the literature, including for the rational-curve divisor, where the semifan is characterised only as the coarsest subdivision on which the combinatorial type of stable pairs is constant; `sections/2-part-moduli/4-chapter-cpt/300-semitoroidal.md`.
The Enriques case is available because the ramification-locus semifans are supplied explicitly in the source.
Issue [#679](https://github.com/dzackgarza/research/issues/679).

**The cusp bijection across two discriminants.**
`sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md` uses a bijection between the cusp sets of $T_\En$ and of a lattice $K$ with a different discriminant group, and the $F_\En$ cusp count depends on it; no proof is given.
Issue [#684](https://github.com/dzackgarza/research/issues/684).

## Decidable by a finite derivation, not yet decided

**The orbit lengths on the $528$ isotropic classes.**
The order $696\,729\,600$ of the finite group in @thm:coble-heegner-finite-orbits is verified; its orbit lengths $[1,2,120,135,270]$ are not, and neither is the claim that $[1,255,272]$ are the orbits of the polarization stabilizer.
Both wait on group generators of $\gent$.
Issues [#688](https://github.com/dzackgarza/research/issues/688) and [#689](https://github.com/dzackgarza/research/issues/689).

**Scattone's diagram against the AET19 diagram.**
The two published diagrams for the $(18,2,0)$ lattice should agree and reportedly do not; which is right is unresolved, and the folded Sterk diagrams of @sec-root-vectors-and-folded-sterk-diagrams inherit the discrepancy.
Issue [#657](https://github.com/dzackgarza/research/issues/657).

**Dawes' Example 2.2.**
@qst:dawes-example-22: the paper concludes that two vectors of $U\oplus A_3$ are equivalent, the in-tree computation finds complements of different discriminants, and one of the paper's conclusion, the transcription, or the computed complements is wrong.
Algorithm 2.3 of the same paper is the published route to the $0$-cusp count.
Issue [#662](https://github.com/dzackgarza/research/issues/662).

**Two forms of the embedding $S_\En\hookrightarrow S_\Nod$.**
@sec-nodal-enriques-moduli-program records the primitive embedding in two bases, attributed to two places in the same source, and the two have not been checked against each other.
Issue [#685](https://github.com/dzackgarza/research/issues/685).
