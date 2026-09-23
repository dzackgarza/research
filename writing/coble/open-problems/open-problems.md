# Open problems and technical gaps

::: {.Remark}
### Orientation

This section records the known open problems and computational obstacles of the Coble moduli program.
Each entry is a genuine gap between the results established elsewhere in this document and the fully rigorous, coordinate-explicit statements one would want for parity with the Enriques degree-$2$ program of [@AEGS25]. The problems are grouped by theme: lattice-theoretic verifications, the enumeration of isotropic orbits and cusps together with the reflection-group combinatorics, the *dlt* and KSBA stable models, and the foundational equations and computational checks.
None of the statements below is claimed to be settled; several cross-reference partial results already in the text, and in each case the *residue* that remains open is stated explicitly.
:::

## Lattice-theoretic gaps

::: {.Remark}
### Open problem: isometry class and genus of the Coble lattices

The invariants $(r,a,\delta)$ of the geometric lattice $S_\Co \cong (11,11,1)_1$ (signature $(1,10)$, Gram matrix $\operatorname{diag}(2,-2,\dots,-2)$, equivalently $\gens{-2}\oplus E_{10}(2)$) and of the transcendental lattice $T_\Co = S_\Co^{\perp \lkt} \cong (11,11,1)_2$ (signature $(2,9)$) are recorded in [the Coble lattice table](coble-lattice-table.md), and both satisfy $q_{S_\Co} \cong q_{T_\Co} \cong (\ZZ/2\ZZ)^{11}$ with $q_{S_\Co} = -q_{T_\Co} \bmod 2\ZZ$.
What is not yet formally established is the *isometry-class verification* and the *genus decomposition*: whether the genus of $T_\Co$ contains a unique isometry class.
Concretely:

- compute the Gram matrices of $S_\Co$ and $T_\Co$ and verify their $(r,a,\delta)$ invariants and genus cardinality via Nikulin's classification (the $r > a$ check for a $2$-elementary lattice) [@Nik80];

- confirm that $r > a$ forces a unique class in the genus, so that the reduction of isotropic-orbit questions to the discriminant form $q_{T_\Co}$ ([the Sterk-orbit theorem](#thm:sterk-orbit)) is justified.
:::

::: {.Remark}
### Open problem: explicit primitive embedding matrices

The chain of primitive embeddings
$$
T_\Co \injects T_\En \injects T_\dP \injects \lkt
$$
is used throughout ([the sequence-of-embeddings lemma](#lem:sequence_of_embeddings), [the primitive-embedding lemma](#lem:primitive_embedding_eta)), and Nikulin's apparatus [@Nik80 Prop. 1.14.4, 1.15.2] is the intended tool for the uniqueness of the primitive embedding $T_\Co \injects T_\En$ and for the surjectivity of $\Orth(L) \to \Orth(T_\Co)$.
What remains is to *exhibit the embedding matrices in coordinate bases*: derive the explicit primitive-embedding matrices realizing the chain above, and verify their primitivity directly rather than by invocation.
The same coordinate deficit affects the derivation of the explicit equations for $C$ and $X$ (below): the invariants are listed, but the primitivity of the lattice embeddings lacks a rigorous derivation in terms of coordinate bases.
:::

::: {.Conjecture}
### Open problem: the horizontal folding involution and its eigenspaces

There is an orthogonal involution $\theta$ on the K3 lattice $\lkt \cong U^{3}\oplus E_8^{2}$ whose invariant and coinvariant sublattices are
$$
\lkt^{\theta} \cong T_\Co,
\qquad
\lkt^{-\theta} \cong S_\Co,
$$
and whose action on roots induces the *horizontal folding* of the $(18,0,0)_1$ Coxeter diagram, as a functorial consequence of the lattice isometry (cf.
[the folded-root definition](#def:folded-root), [the root-folding lemma](#lem:root-folding-tdp), and [the invariant/coinvariant-lattice definition](#def:invariant_coinvariant_lattices)). The involution should swap the polarization generators between sectors, $h_\En \leftrightarrow h_\Co$.
Existence and the eigenlattice description are settled: the pair $(-\id_{S_\Co}, \id_{T_\Co})$ preserves the gluing graph of the Coble primitive embedding, so it extends to an isometry $\theta_\Co$ of $\lkt$ with the stated eigenlattices ([the folding-involution proposition](#prop:theta-co-exists)).
The open technical content is to *write down the $22\times 22$ matrix of $\theta_\Co$ on the standard basis of $U^{3}\oplus E_8^{2}$*, which requires exhibiting the primitive embedding and the gluing anti-isometry in coordinates, and then to compare the polarization classes and the roots of the Coxeter diagram in that basis.
:::

## Isotropic orbits, cusps, and reflection groups

::: {.Question}
### Open problem: enumeration of isotropic orbits by Sterk's technique

How many orbits of primitive isotropic vectors does $T_\Co$ have under $\Orth(T_\Co)$, $\Orth^{*}(T_\Co)$, and the arithmetic group $\Gamma_\Co$?
Sterk's technique [@Ste91] determines these by analyzing the orbits of the images (lifts) in the discriminant group $A_{T_\Co} \cong (\ZZ/2\ZZ)^{11}$ under $\Orth(q_{T_\Co})$: for a $2$-elementary lattice with $r > a$ the genus contains a unique class and $\Orth(T) \to \Orth(q_T)$ is surjective [@Nik80], so a primitive isotropic vector $v$ with $\operatorname{div}(v)=d$ is determined up to $\Orth(T)$ by the tuple $(\operatorname{div}(v),\, \bar v \in A_T,\, v^2 = 0)$.
The finite half of this is settled: $A_{T_\Co}$ has $528$ isotropic classes, on which $\Orth(q_{T_\Co})$ acts with two orbits, of sizes $1$ and $527$ ([the Coble $Q$-fiber proposition](#prop:coble-q-fibers), [the isotropic-class orbit theorem](#thm:coble-isotropic-class-orbits)), and every primitive isotropic vector of $T_\Co$ lands in the nonzero one ([the primitive-isotropic-class proposition](#prop:coble-primitive-isotropic-classes)).
Under the degree-$2$ Enriques group the same $528$ classes split as $[1, 2, 120, 135, 270]$ ([the finite-image orbit theorem](#thm:coble-heegner-finite-orbits)).
The open work is the passage from these finite decompositions back to the lattice:

- lift the $\Orth(q_{T_\Co})$-orbits to $T_\Co$ and verify that exactly one $\Orth^{*}(T)$-orbit exists in divisibility $2$, the Eichler criterion being unavailable because $T_\Co$ contains no copy of $U$ ([the Eichler criterion](#thm:eichler-criterion) and the remark following it);

- decide whether the four nonzero orbits of $\Gamma_{\En, 2}$-induced classes lift to four orbits of primitive isotropic vectors or to more, an integral parabolic stabilizer being permitted to have proper image in the finite one;

- verify that the $\Orth(T)$-orbits coincide with the $\Gamma_\Co$-orbits, so that the Baily--Borel $0$-cusp is unique.

That every primitive isotropic $v \in T_\Co$ has $\operatorname{div}_{T_\Co}(v) = 2$ is already known ([the divisibility lemma](#lem:divisibilityAlwaysTwoTco)), which fixes the divisibility datum but not the orbit count.
:::

::: {.Remark}
### Open problem: explicit generators of $\Gamma_\Co$ and uniqueness of the 1-cusp

The arithmetic group governing the Coble locus is the stabilizer of the polarization $h_\Co$ inside $\Orth(T_\En)$, cut further by the horizontal folding involution $\theta$,
$$
\Gamma_\Co = \operatorname{Stab}_{\Orth(T_\En)}(h_\Co) \cap Z_{\Orth(T_\En)}(\theta),
$$
where in the Enriques sector $h_\En = e + f\in U(2)$ is the degree-$2$ polarization vector, of square $4$ on the K3 side ([the discriminant description of $\Gamma_{\En,2}$](#prop:gamma-en-two-gluing)), and $h_\Co\in K_S^{\perp}\subseteq\Pic(S)$ is [the degree-$2$ Coble polarization](#def:coble-polarization-classes), of square $2$ downstairs with K3 pullback $\tilde h_\Co = f^{*}h_\Co$ of square $4$.
The class $h_\Co$ is not the plane class $H$, whose K3 pullback $e_0 = f^{*}H$ has square $2$; the two must be kept apart, and it is $h_\Co$ that is the analogue of $h_\En$.
A source-backed candidate for $\Gamma_\Co$, defined from the Enriques side by the Heegner line rather than by $\theta$, is $\Gamma_\Co^\En(\delta)$ from [the induced Coble subgroup definition](#def:gamma-co-en); identifying the two is part of the open work below.
An explicit representation of $\Gamma_\Co$ by *matrix generators* is presently a stub.
The open work is to:

- compute the stabilizer/centralizer intersection in the Enriques (equivalently $\lkt$) lattice to produce a minimal set of matrix generators for $\Gamma_\Co$, as the intersection of the reflection group $W(T)$ with the centralizer $Z(\theta)$ and the stabilizer of the primitive vector $\tilde h_\Co$ ($\tilde h_\Co^2 = 4$).
  The involution $\theta$ itself exists as a lattice isometry without any coordinate description ([the folding-involution proposition](#prop:theta-co-exists)), and the image of the resulting group in $\Orth(q_{T_\Co})$ is already known ([the finite-image orbit theorem](#thm:coble-heegner-finite-orbits)); what a generating set adds is the lattice group above that finite image;

- verify the *uniqueness of the $1$-cusp for $\Gamma_\Co$*.
  For the full orthogonal group this is settled: $\Orth^+(T_\Co)$ is transitive on primitive isotropic planes and $J^{\perp}/J\cong\latI_{0,7}(2)\cong A_1^{\oplus 7}$ ([the unpolarized-cusp theorem](#theorem-unpolarized-cusps), with the split maximal hypothesis supplied by [the split-maximal proposition](#prop:tco-split-maximal)).
  The residue is the subgroup statement, which does not follow from the full-group one.

This refines, at the level of orbits and generators, the $1$-cusp correspondence $(7,7,1)_0 \mapsto (8,6,0)_0$ established in [the $1$-cusp correspondence lemma](#lem:1_cusp_correspondence).
:::

::: {.Remark}
### The maximal parabolic subdiagrams of $S_\Co$, and what they count

The Coxeter diagram $\Gamma_r$ of $S_\Co = (11,11,1)_1$ has $12$ roots, trivial
automorphism group, and **two** maximal parabolic subdiagrams,
$\widetilde{E}_8(2)\widetilde{A}_1$ and $\widetilde{B}_9(2)$, both of even
ordinary type ([the Coble Picard parabolic theorem](#thm:coble-picard-parabolics)).
By [the parabolic/isotropic correspondence theorem](#thm:parabolic-isotropic-correspondence) these correspond to the two
$\Orth^+(S_\Co)$-orbits of primitive isotropic vectors in $S_\Co$, and by
[the isotropic-trichotomy theorem](#thm:isotropic-trichotomy) both associated quotients $v^{\perp}/v$ have
invariants $(9,9,1)$, so the two orbits are not separated by the invariants of the
boundary lattice.

These orbits are elliptic fibrations of the K3 cover
([the elliptic-fibration/isotropic theorem](#thm:elliptic-fibrations-isotropic)); they are not the $0$-cusps of the
Coble period space, which are the orbits of primitive isotropic vectors in the
transcendental lattice $T_\Co$ of signature $(2,9)$.
Of the latter there is exactly one under the full orthogonal group
([the unpolarized-cusp theorem](#theorem-unpolarized-cusps)), by the split maximal argument of
[the split-maximal proposition](#prop:tco-split-maximal).
The two lattices share the invariant triple $(11,11,1)$ but not the signature, and
a count taken in one is not a count in the other.

What remains open is the geometric identification: which of the two elliptic
fibration classes of the K3 cover is distinguished by the Coble structure, and how
the pair of maximal parabolic subdiagrams matches the boundary data of the
degree-$2$ polarized moduli space.
:::

::: {.Question}
### Open problem: the reflection group of each Sterk fundamental domain

Sterk's published fundamental domains for the five cusps of $F_{\En,2}$ have $12, 10, 12, 11, 14$ walls [@Ste91], while Vinberg's algorithm applied to the corresponding hyperbolic quotients $\eta_j^{\perp}/\eta_j$ returns ten walls in each case.
The quotients for $j = 2,3,4,5$ are mutually isometric, so their full Weyl groups are conjugate and cannot account for four inequivalent published diagrams.
The open work is to identify, for each $j$, the reflection subgroup $W_j\leq W(\eta_j^{\perp}/\eta_j)$ for which the published diagram bounds a fundamental domain, to exhibit that domain as a union of chambers of the full group, and to determine the index $[W(\eta_j^{\perp}/\eta_j) : W_j]$ as a covolume ratio.
Cusp $2$, to which the Coble $0$-cusp is claimed to correspond, is the case in which the two computations agree.
The data and the derivation are in [[sterk-root-counts-and-computed-chambers]].
:::

::: {.Remark}
### Open problem: hyperbolic-quotient derivation of the cusp correspondence

The cusp correspondence between the Coble cusps $(9,9,1)$, $(7,7,1)$ and their Enriques predecessors is established in [the cusp-correspondence theorem](#thm:cusp_correspondence) (via the divisibility computations of [the $w_1^\perp$ calculation](#lem:w1_perp_calculation) and [the $1$-cusp correspondence lemma](#lem:1_cusp_correspondence)). The migrated notes propose an independent *hyperbolic-quotient* derivation that would place the correspondence on a self-contained lattice footing rather than resting on the alignment of invariants:

- compute the isometry type of the hyperbolic quotient $e^{\perp}/e$ directly for a primitive isotropic $e \in T_\Co$;

- use $\operatorname{div}_{T_\Co}(e)$ to pin down the unique $\Orth(T_\Co)$-orbit and verify that the quotient matches the Enriques signatures $(10,8,0)_1$ for $0$-cusps and $(8,6,0)_0$ for $1$-cusps.

The residue that is genuinely open is the *orbit-uniqueness input*: the proof of [the divisibility lemma used there](#lem:divisibilityTcoOne) presently *assumes* a unique $\Gamma_\Co$-orbit of isotropic vectors in $T_\Co$, which is exactly the enumeration left open above.
:::

### General questions on hyperbolic reflection groups

The entries above ask for specific subdiagram and orbit computations in the Coble and Enriques lattices.
The following are the corresponding questions asked of hyperbolic Coxeter diagrams in general; each is open, and each bears on how far the specific computations can be pushed.

::: {.Question #qst:maximal-parabolic-complexity}
### Open problem: the cost of enumerating maximal parabolic subdiagrams

Given a Coxeter--Vinberg diagram $\Sigma$ on $n$ vertices, what is the cost of determining its maximal parabolic subdiagrams, equivalently the ideal vertices of the chamber ([the ideal-vertices/parabolic corollary](#cor:ideal-vertices-are-parabolic))?

Enumerating the $2^{n}$ subsets is an upper bound, and [the subdiagram-inheritance corollary](#cor:subdiagram-inheritance) prunes it: a subset that fails to be elliptic can be discarded together with every subset containing it, so the search runs over the order ideal of elliptic subsets.
No lower bound is known, and no polynomial-time algorithm is known even for the decision problem asked of the whole diagram:

- decide whether a given hyperbolic Coxeter diagram has finite covolume ([the Coxeter-polytope volume theorem](#thm:coxeter-polytope-volume)) without enumerating its maximal parabolic subdiagrams;

- exhibit a family of diagrams on which the elliptic order ideal is of exponential size, or show that it is polynomial for the diagrams of finite-covolume groups.

The concrete instance in this monograph is the uniqueness of $\widetilde{B}_7(2)$ as a maximal parabolic subdiagram of the ten-node diagram $G_{S_\Co}$, stated above; the general question is whether such uniqueness claims admit an argument short of the subdiagram search.
:::

::: {.Conjecture #cnj:galois-invariance-parabolics}
### Open problem: Galois invariance of the maximal parabolic count

Let $\Sigma$ be a Coxeter--Vinberg diagram whose Gram form is defined over a totally real number field $K$, and let $\sigma\in\operatorname{Gal}(K/\QQ)$.
The conjecture is that $\Sigma$ and its conjugate $\sigma(\Sigma)$ have the same number of maximal parabolic subdiagrams.

By [the Galois-conjugate Gram-form remark](#rmk:galois-conjugate-gram-form) the signature of $\sigma(G)$ is not determined by that of $G$, so the conjugate diagram need not be hyperbolic at all and the statement requires the hypothesis that it is.
The open work is to determine the action of $\operatorname{Gal}(K/\QQ)$ on the set of maximal parabolic subdiagrams --- whether it permutes them, and if so with what orbits.
The diagrams of this monograph have Gram field $\QQ$ or $\QQ(\sqrt2)$, the latter arising from the $m_{ij} = 4$ bonds of the $B$-type diagrams, so the smallest instance is the nontrivial automorphism of $\QQ(\sqrt2)$ acting on the folded Sterk diagrams.
:::

::: {.Question #qst:parabolic-count-growth}
### Open problem: growth of the maximal parabolic count with the rank

How does the number of maximal parabolic subdiagrams of a hyperbolic Coxeter diagram grow with its rank $n$?

Is there a bound, exponential or otherwise, valid for all diagrams of rank $n$, and does the finite-covolume condition of [the Coxeter-polytope volume theorem](#thm:coxeter-polytope-volume) improve it?
The recorded data for this monograph is the count of vertices at infinity in the CoxIter runs on the five folded Sterk diagrams and the three $0$-cusp lattices, all of rank $9$ or $10$; a family of increasing rank is needed before a growth statement can be made.
:::

::: {.Question #qst:arithmeticity}
### Open problem: which finite-covolume reflection groups are arithmetic

Which finite-covolume hyperbolic Coxeter groups are arithmetic?

The datum available from the diagram is the Gram form over its base field $K$ ([the Coxeter-base-field definition](#def:coxeter-base-field)) together with its Galois conjugates ([the Galois-conjugate Gram-form remark](#rmk:galois-conjugate-gram-form)).
The open work is to decide arithmeticity from that datum, and to determine how the property interacts with the maximal parabolic structure of the diagram.
The reflection groups appearing in this monograph act on lattices defined over $\ZZ$, so they are arithmetic; the question governs whether the techniques used here extend to [the non-crystallographic base-ring examples](#ex:noncrystallographic-base-rings).
:::

::: {.Question #qst:exact-covolume}
### Open problem: exact covolumes of hyperbolic Coxeter polytopes

Compute $\vol(P)$ exactly for a hyperbolic Coxeter polytope $P$ given by its diagram ([the covolume definition](#def:covolume)).

In even dimension the volume is a rational multiple of the Euler characteristic and is computable from the diagram; in odd dimension the Euler characteristic vanishes and supplies no information, which is the case for every nine-dimensional chamber recorded in the Computations section.
The open work is:

- closed-form volume formulas for specific families, through Schläfli's volume differential or through polylogarithmic values;

- the relation between $\vol(P)$ and the maximal parabolic structure of $\Sigma$;

- a covolume computation sharp enough to decide the index $[W : W_j]$ of a reflection subgroup, which is the quantity that would settle the discrepancy between Sterk's published fundamental domains and the computed Vinberg chambers.
:::

::: {.Question #qst:regularized-theta}
### Open problem: theta series of indefinite lattices

For a positive-definite lattice the theta series $\theta_L(q) = \sum_{v\in L} q^{v^2/2}$ converges and is a modular form.
For an indefinite lattice each level set $L[k]$ can be infinite (see the Lattice Theory section), the series does not converge, and a regularization is required before any modular statement can be made.

The open work is to define a regularized theta series for the hyperbolic lattices of this monograph, determine its transformation behaviour, and relate it to the lattice invariants --- discriminant form, genus, and the reflection group --- that the rest of this document computes.
:::

## The GIT and Looijenga models of the Coble moduli space

::: {.Question #que:coble-arrangement-empty}
### Open problem: is the Coble arrangement $\cH^{*}_{10A_1}$ empty?

The GIT compactification of the moduli of ten-nodal sextics is the Looijenga
compactification of $\Gamma_{10A_1}\backslash(D(T_\Co) - \cH^{*}_{10A_1})$, for
the arrangement
$$
\cH^{*}_{10A_1} = \cH_\infty \cap D(T_\Co)
$$
cut out by the divisibility-two roots of $\Lambda_1 = H^{\perp\lkt}$
([the GIT--Looijenga theorem](#thm:git-equals-looijenga)).
Whether that arrangement is empty decides the shape of the compactification:

- if $\cH^{*}_{10A_1} = \varnothing$, the Looijenga construction returns the
  Baily--Borel compactification ([the Looijenga-compactification definition](#def:looijenga-compactification)), so the
  GIT boundary of the ten-nodal sextics consists of the $0$-cusp point and the
  $1$-cusp curve and nothing else;

- if $\cH^{*}_{10A_1} \neq \varnothing$, the GIT compactification carries a
  boundary divisor for each $\Gamma_{10A_1}$-orbit in the arrangement, and is a
  proper semitoroidal model strictly between Baily--Borel and toroidal.

The question is a lattice computation in $\Lambda_1$: is there a divisibility-two
root of $\Lambda_1$ whose orthogonal hyperplane meets $D(T_\Co)$ in a proper
hyperplane section?
It is *not* answered by [the divisibility lemma](#lem:divisibilityAlwaysTwoTco), which computes
divisibility inside $T_\Co$ and says nothing about divisibility inside the larger
lattice $\Lambda_1$.
One reduction is available: every root of the root lattice $L$ has divisibility
$1$ in $\Lambda_1$ [@YZZ25 §4.2], so no root arising from a node of the sextic
contributes, which is why $\cH^{*}_{10A_1}$ is contained in the larger
arrangement $\cH_{10A_1}$ of [the occult-period-map theorem](#thm:occult-period-map-sextics).
:::

::: {.Question #que:semifan-poset-position}
### Open problem: the position of the three semifans

The Coxeter, KSBA, and Looijenga semifans of the Coble period domain are
determined by three unrelated inputs, and no one of them constrains another
([the Looijenga-compactification definition](#def:looijenga-compactification) and the remark following it).
Once $\cH^{*}_{10A_1}$ is computed, three questions remain:

- is the resulting Looijenga semifan the Coxeter semifan of a reflection group,
  as it would be if the traces of $\cH^{*}_{10A_1}$ on a cusp boundary were the
  walls of a chamber?

- does the Looijenga semifan refine the KSBA semifan, coarsen it, or is it
  incomparable?

- which sextic degenerations lie over which cusp?
  Shah's classification of the semistable sextics is explicit [@Sha80], and the
  cusp correspondence of [the cusp-correspondence theorem](#thm:cusp_correspondence) is known, so tracing a
  named degeneration such as a double cubic to the $0$-cusp $(9,9,1)_1$ or the
  $1$-cusp $(7,7,1)_0$ is a finite computation rather than a new theory.
:::

## dlt and KSBA stable models

::: {.Remark}
### Open problem: Coble-specific dlt models and pot geometry

The degree-$2$ Enriques program modernizes Morrison's flowerpots [@Mor81] into *dlt* stable pairs, but the *Coble-specific dlt models* are not yet detailed.
The open geometric content is:

- **Coble pot geometry.** Define the explicit stable pair $(\mathcal V, \mathcal D)$ whose "Pot" component is a rational Coble surface, carrying a $\tfrac14(1,1)$ cyclic quotient singularity corresponding to the nodes of the rational sextic $C$.
  This is the local singularity package already conjectured for the stable quotient in [the quarter-singularity conjecture](#conj:coble_quarter_singularity), seen here on the *dlt* model (cf.
  [the dlt-involution-pair definition](#def:dlt-involution-pair), [the divisor-model definition](#def:divisor-model)).

- **Stalk assembly.** Describe the transition of the stalk assembly and the integral-affine configuration as the Enriques surface log-collapses onto the discriminant divisor $\Delta$, where the K3 cover becomes nodal.
:::

::: {.Remark}
### Open problem: monodromy invariants and stable models $B(\lambda)$

Stable limits of Coble surfaces arise as $S_2$-quotients of nodal K3 surfaces, parameterized by a monodromy invariant $\ell \in \check{\cH}$ (surgery sizes) through the construction $B(\lambda)$ of [@AEGS25]. The open work is to:

- determine the map from the Coble polarization to the discretization $\ell$ on the dual complex.
  The surgery sizes are the pairings $\ell_i = h\cdot\alpha_i$ against the roots $\alpha_i$ of the relevant Coxeter diagram, so the first step is to record which polarization class is meant and in which lattice the pairing is taken: the downstairs class $h_\Co\in K_S^{\perp}$ or its K3 pullback $\tilde h_\Co\in S_\Co$ ([the Coble-polarization definition](#def:coble-polarization-classes)), the roots living in the lattice of the chosen cusp.
  An orthogonal direct-sum presentation on its own does not make $\ell = 0$;

- verify the slc stability of the resulting stable pair $(Z, \varepsilon C)$ for specific surgery vectors $\ell$.

This is the discrete-datum side of the KSBA program whose stability obligations are recorded in [the quarter-singularity conjecture](#conj:coble_quarter_singularity) and the surrounding KSBA discussion.
:::

## Foundational equations and computational verification

::: {.Remark}
### Open problem: explicit equations for the Coble curve and its K3 cover

A Coble surface $S$ is the blowup of $\PP^2$ at the ten $A_1$ nodes of an irreducible rational plane sextic
$$
C = \ts{ F(x,y,z) = 0 },
\qquad
F(x,y,z) = \sum_{i+j+k=6} a_{ijk}\, x^i y^j z^k,
$$
subject to the nodal conditions $F(p_m) = \partial_x F(p_m) = \partial_y F(p_m) = \partial_z F(p_m) = 0$ at the ten special positions $p_1,\dots,p_{10} \in \PP^2$; the moduli space of such sextics is $9$-dimensional, and explicit models may be sought from the Steiner sextic or from index-$2$ Halphen pencils (cf.
[the Coble--Halphen blowdown lemma](#lem:coble_halphen_blowdown), [the ten-nodal-sextic lemma](#lem:rational_sextic_ten_nodes)). The K3 cover is the double cover $X \xrightarrow{2:1} S$ of $\PP^2$ branched along $C$, with equation $w^2 = F(x,y,z)$ in $\PP(1,1,1,3)$, whose ten $A_1$ nodes lie above the positions $p_m$ (at $w = 0$, $[x:y:z] = p_m$). What is missing is a *worked instance*: derive an explicit equation $F(x,y,z) = 0$ for a rational sextic with ten nodes together with the corresponding cover $w^2 = F$, realizing $C$ as the image of $\PP^1$ under a degree-$6$ map $(s:t) \mapsto [f_0 : f_1 : f_2]$.
Such an instance would anchor the coordinate derivations demanded by the lattice-embedding and involution problems above.
:::

::: {.Remark}
### Lattice and orbit anchors for the computations

The problems above share a small set of concrete starting data, recorded here for reference:

- **Isotropic vectors.** In $S_\Co$, primitive isotropic lines are represented by $v = e_0 \pm e_i$ (with $e_0^2 = 2$, $e_i^2 = -2$).

- **Polarization basis.** The degree-$2$ polarization is $h = e + f\in U(2) = S_\dP\subseteq S_\En$, with $e\cdot f = 2$ and $h^2 = 4$ ([the discriminant description of $\Gamma_{\En,2}$](#prop:gamma-en-two-gluing)); it lies in the invariant lattice, not in $T_\En$, and must be identified in a basis compatible with $\theta$.

- **Heegner line.** The complement realizing $T_\Co$ inside $T_\En$ is $\delta^{\perp}$ for $\delta = u - w$ in the unimodular $U$ summand, and this line is unique up to $\Gamma_{\En, 2}$ ([the explicit Heegner-vector lemma](#lem:coble-heegner-vector), [the Heegner-line uniqueness theorem](#thm:coble-heegner-line-unique)).

- **Discriminant forms.** $q_{S_\Co} \colon (\mathbb{F}_2)^{11} \to \QQ/2\ZZ$ and $q_{T_\Co} \colon (\mathbb{F}_2)^{11} \to \QQ/2\ZZ$, with isometry of complements forcing $q_{S_\Co} = -q_{T_\Co} \bmod 2\ZZ$.

- **Sterk orbit lift.** For the $2$-elementary $T_\Co$, an orbit is determined by the tuple $(\operatorname{div}(v),\, \bar v \in A_{T_\Co},\, v^2 = 0)$, reducing the search to $\mathbb{F}_2$-vector-space orbits under $\Orth(q_{T_\Co})$.

- **$\Gamma_\Co$ generators.** Computed as the intersection of the reflection group $W(T)$ with the centralizer $Z(\theta)$ and the stabilizer of the primitive vector $\tilde h_\Co = f^{*}h_\Co$, of square $4$.
:::
